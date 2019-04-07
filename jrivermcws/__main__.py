import sys
import argparse
from .api import *
from .exceptions import FailedAuthenticationException

def setup_parser():
    p = argparse.ArgumentParser(
        description="jriverctl passes commands to a jriver-media-center web server instance",
        argument_default=False,)
    p.add_argument('cmd', nargs='?')
    p.add_argument(*['-a', '--auth'], nargs=2, metavar=('USERNAME', 'PASSWORD'), type=str, help='Authentication username and password')
    p.add_argument(*['-s', '--server'], nargs=2, metavar=('SERVER'), type=str, help='The http url of the mcws server')
    p.add_argument(*['-m', '--mcc'], nargs=2, metavar=('COMMAND', 'PARAMETER'), help='Send to mcc handler')
    p.add_argument(*['-p', '--print'], action='store_true', default=False, help='Print results')
    p.add_argument(*['-c', '--current'], action='store_true', default=False, help='Print the current track information')
    return p


def main():
    parser = setup_parser()
    opts = parser.parse_args()

    token = None
    if opts.auth:
        username, password = opts.auth
        try:
            if opts.server:
                token = authenticate(username, password, opts.server)
            else:
                token = authenticate(username, password)
        except FailedAuthenticationException as e:
            print("Failed to authenticate connection to JRiver\n", e)
            return
        except Exception as e:
            print("Could not establish connection to JRiver. Verify MCWS is running.\n", e)
            return
    else:
        try:
            request('Alive')
        except Exception as e:
            print("Could not establish connection to JRiver. Verify MCWS is running and authentication is not required.\n", e)
            return

    r = None

    if opts.mcc:
        r = request(cmd='MCC', Command=opts.mcc[0], Parameter=opts.mcc[1], token=token)

    if opts.cmd:
        scmd = opts.cmd.split("/")
        if len(scmd) > 1:
            cmd = scmd[1]
            cat = scmd[0]
            r = request(cmd, cat=cat, token=token)
        else:
            r = request(opts.cmd, token=token)

    if opts.current:
        r = request("Info", cat="Playback", token=token)
        s = '      JRiver '
        p = r.parsed()
        if p['State'] == 0 or 'Status' not in p:    # Handle startup stopped, status key doesn't exist
            s += 'Stopped'
        else:
            s += p['Status']
            s += "        "
            if p['Status'] == 'Playing':
                stars = ""
                rating = ''
                if 'Rating' in p:
                    rating = '  ' + stars[:int(p['Rating'])] + '    '
                s += "{} {}({} by {})      {}/{} ".format(p['Name'], rating, p['Album'], p['Artist'], int(p['PlayingNowPosition']) + 1, p['PlayingNowTracks'])
        s += "        "
        print(s)

    if r is None or not opts.print:
        return

    print(r.response.text)


if __name__ == "__main__":
    main()
