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

default_server = 'http://localhost:52199/MCWS/v1/'
token = ''
username = ''
password = ''

def request(cmd, cat=None, server=default_server, **kwargs):
	params = {'Token': authenticate(username, password)}
	if cat is None:
		cat = cmds.categoryof(cmd)
	else:
		if not cat in cmds.details:
			raise BadCommandException('Category does not exist')
	if (not cat) or (not cmd in cmds.details[cat]):
		raise BadCommandException('Command could not be found')
	det = cmds.details[cat][cmd]
	# Commented until optional parametres handled
	#if len(kwargs < cmds.param_count(cmd, cat)):
		# Raise MissingParametersException()
	#	pass
	if det['cmdstr'] == 'Control/MCC':
		if not 'Command' in kwargs:
			raise MissingParametersException('Command number must be included')
		try:
			cmdnum = int(kwargs['Command'])
		except:
			if kwargs['Command'] in mcc.mcc_codes:
				cmdnum = mcc.mcc_codes[kwargs['Command']]
				kwargs['Command'] = str(cmdnum)
			else:
				raise BadCommandException("MCC command '{}' not found".format(kwargs['Command']))
		if not cmdnum in mcc.mcc_cmds:
			raise BadCommandException("MCC command '{}' not found".format(kwargs['Command']))
	params.update(kwargs)
	url = server + det['cmdstr']
	# Manually build request so we can replace '+' with '%20'
	# 		Session used in with to ensure the session closes
	#		as recommended in the requests package
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
	r = Result(response=requests.get(server + 'Authenticate', auth=HTTPBasicAuth(username, password)))
	if r.response.status_code == 200:
		token = r.parsed()['Token']
		return token
	else:
		raise FailedAuthenticationException("HTTP status code: {} {}".format(r.response.status_code, r.response.reason))
