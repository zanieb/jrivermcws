"""
jrivermcws.models
~~~~~~~~~~~~~~~~~

Contains core objects

~~~~~~~~~~~~~~~

Copyright Michael Adkins 2017
Distributed under the MIT License.
See accompanying file LICENSE.md file or copy at http://opensource.org/licenses/MIT

"""

import xml.etree.ElementTree as xmletree
import xmltodict
from . import cmds
from collections import OrderedDict

class Result(object):

    __attrs__ = [
        'cmd', 'cat', 'response'
    ]

    def __init__(self, cat=None, cmd=None, response=None):

        self.cmd = cmd
        self.category = cat
        self.response = response

    def __repr__(self):
        return '<Result of {}/{} [{}]>'.format(self.category, self.cmd, self.response.status_code)

    def __bool__(self):
        """Returns true if response.status_code is 'OK'"""
        """ and result is non-empty """
        if self.response is None: return False
        return self.response.ok

    def xml(self, **kwargs):
        """Returns an xml.etree.ElementTree parsing of the content

        :raises ValueError: If the response body does not contain valid xml.
        """
        return xmletree.fromstring(self.response.text)


    def json(self):
        """Convert the xml to json/dictionary"""
        j = xmltodict.parse(self.response.text)
        if 'Response' in j:
            return j['Response']
        else:
            return j

    def dict(self):
        return self.json()

    def parsed(self, collapse_singles=True):
        j = self.json()
        r = OrderedDict()

        if '@Status' in j:
            r['Status'] = j['@Status']
        else:
            r['Status'] = 'UNKNOWN'

        if 'Fields' in j:
            r = self.parse_json(j['Fields']['Field'], collapse_singles)
        elif 'Item' in j:
            r = self.parse_json(j['Item'], collapse_singles)

        return r

    def parse_json(self, j, collapse_singles=True):
        # Result dictionary
        r = OrderedDict()

        if not isinstance(j, list):
            j = [j]

        for d in j:
            if d is None:
                continue
            # Parse non-dictionary items
            if not isinstance(d, OrderedDict):
                if not 'Items' in r:
                    r['Items'] = []
                r['Items'].append(d)
                continue
            # Parse named items
            if '@Name' in d:
                name = d['@Name']
                if not name in r:
                    r[name] = []
                r[name].append(d['#text'])
            # Parse weird 'Field' items such as for Playlists/List query
            if 'Field' in d:
                if not 'Fields' in r:
                    r['Fields'] = []
                sr = self.parse_json(d['Field'], collapse_singles)
                r['Fields'].append(sr)

        if collapse_singles:
            for n in r:
                if len(r[n]) == 1:
                    r[n] = r[n][0]

        return r