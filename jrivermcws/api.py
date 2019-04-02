"""
jrivermcws.api
~~~~~~~~~~~~~~~

Primary interface for use of the library

~~~~~~~~~~~~~~~

Copyright Michael Adkins 2017
Distributed under the MIT License.
See accompanying file LICENSE.md file or copy at http://opensource.org/licenses/MIT

"""

import requests
from requests import Request, Session
from requests.auth import HTTPBasicAuth
from . import cmds
from . import mcc
from .exceptions import BadCommandException, MissingParametersException, FailedAuthenticationException
from .models import Result

default_server = 'http://localhost:52198/MCWS/v1/'
default_username = ''
default_password = ''


def request(cmd, cat=None, server=default_server, username=default_username, password=default_password, token=None, **kwargs):
    """Sends a command request to the JRiver MCWS server

    Arguments
    ----------
    cmd : string, integer
        the command to send
    cat (optional = None) : string
        the higher level category of the command, if not provided it will be looked up
    server (optional = 'http://localhost:52198/MCWS/v1/') : string, url
        the address of the JRiver MCWS
    username : string
        the username to login to the server with
    password : string
        the password to login to the server with
    token : string
        A pre-authenticated token to use instead of username/password
    kwargs :
        additional keyword arguments are passed as parameters with the command

    Returns
    -------
    A jrivermcws.models.Result object which provides JSON parsing and
    access to the requests.request result

    Examples
    --------
    import jrivermcws as jr

    # Go to the next track
    r = jr.request('Next', cat='Playback')
    if not r:
        print("Request error")

    # Call MCC_VOLUME_UP by 10%
    jr.request(cmd='MCC', Command=10018, Parameter=10)

    # Check if the server is online
    try:
        jr.request('Alive')
    except:
        print("Could not establish connection to JRiver")
        return

    # Get the currrently playing song
    r = jr.request("Info", cat="Playback")
    p = r.parsed()
    print("Playing {} by {}".format(p['Name'], p['Artist']))

    """

    params = {'Token': authenticate(username, password, server=server) if token is None else token}

    # Validate the category of the command with automatic lookup if not supplied
    if cat is None:
        cat = cmds.categoryof(cmd)
    else:
        if cat not in cmds.details:
            raise BadCommandException('Category does not exist')
    if (not cat) or (cmd not in cmds.details[cat]):
        raise BadCommandException('Command could not be found')

    det = cmds.details[cat][cmd]

    # Commented until optional parametres handled
    # if len(kwargs < cmds.param_count(cmd, cat)):
        # Raise MissingParametersException()
    #   pass

    # Validate MCC type commands
    if det['cmdstr'] == 'Control/MCC':
        if 'Command' not in kwargs:
            raise MissingParametersException('Command number must be included')
        try:
            cmdnum = int(kwargs['Command'])
        # TODO: Choose a more specific exception to catch
        except Exception as e:
            if kwargs['Command'] in mcc.mcc_codes:
                cmdnum = mcc.mcc_codes[kwargs['Command']]
                kwargs['Command'] = str(cmdnum)
            else:
                raise BadCommandException("MCC command '{}' not found".format(kwargs['Command']))
        if cmdnum not in mcc.mcc_cmds:
            raise BadCommandException("MCC command '{}' not found".format(kwargs['Command']))

    # Update arguments and construct a call url
    params.update(kwargs)
    url = server + det['cmdstr']

    # Manually build request so we can replace '+' with '%20'
    #       Session used in with to ensure the session closes
    #       as recommended in the requests package
    with Session() as s:
        req = Request('GET', url, params=params)
        prepped = s.prepare_request(req)
        prepped.url = prepped.url.replace('+', '%20')
        try:
            resp = s.send(prepped)
        except Exception as e:
            print("An exception occured on the request for '{}'. Details: {}".format(url, e.args[0]))
            resp = None
            pass

    result = Result(cat, cmd, resp)
    return result


def authenticate(username, password, server=default_server):
    """Authenticate with JRiver MCWS given a username/password pair and the server address

    Returns the JRiver MCWS authentication token or raises an exception with the status code.
    """
    r = Result(response=requests.get(server + 'Authenticate', auth=HTTPBasicAuth(username, password)))
    if r.response.status_code == 200:
        return r.parsed()['Token']
    else:
        raise FailedAuthenticationException("HTTP status code: {} {}".format(r.response.status_code, r.response.reason))
