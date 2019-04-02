# JRiver MCWS Interface

A python library to interact with JRiver Media Center (C) via the built in web-server.

Especially useful on Linux where the command line cannot be used to send commands to the media player.

## Installation

`pip install jrivermcws` -- This is not on the PyPy index but will be added when I have time (soon)

or

```
git clone https://github.com/mikeza/jrivermcws.git
pip install -e jrivermcws
```

# CLI

Command-line tool `jriverctl` which can pass commands to the server or retrieve information

## Get the currently playing track information
```
mz@mzxps:~ > jriverctl --auth mz pass --current
      JRiver Playing        Hadal Zone (The Waves by ASC)      7/8
```

## Sending an invalid password
```
mz@mzxps:~ > jriverctl --auth mz passx --current
Failed to authenticate connection to JRiver
 HTTP status code: 401 Authorization Required
```

## Go to the next track
```
mz@mzxps:~ > jriverctl --auth mz pass next
```

## Go to the previous track (example of passing wrong commands)
```
mz@mzxps:~ > jriverctl --auth mz pass prev
Traceback (most recent call last):
  File "/usr/bin/jriverctl", line 11, in <module>
    load_entry_point('jrivermcws', 'console_scripts', 'jriverctl')()
  File "/home/mzjrivermcws/__main__.py", line 53, in main
    r = request(opts.cmd, token=token)
  File "/home/mzjrivermcws/api.py", line 88, in request
    raise BadCommandException('Command could not be found')
jrivermcws.exceptions.BadCommandException: Command could not be found
```

## Go to the previous track
```
mz@mzxps:~ > jriverctl --auth mz pass previous
```

## Print information about currently selected tracks
```
mz@mzxps:~ > jriverctl --auth mz pass -p current
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<MPL Version="2.0" Title="MCWS - Files - 139976624805632" PathSeparator="/">
<Item>
<Field Name="Key">6659617</Field>
<Field Name="Filename">/home/mz/media/torrents/Ross From Friends - Family Portrait (2018) [WEB FLAC]/01 - Happy Birthday Nick.flac</Field>
<Field Name="Name">Happy Birthday Nick</Field>
<Field Name="Artist">Ross From Friends</Field>
<Field Name="Album">Family Portrait</Field>
<Field Name="Genre">electronic; lo.fi; house</Field>
<Field Name="Date (readable)">2018</Field>
<Field Name="Date">43101</Field>
<Field Name="Bitrate">725</Field>
<Field Name="Image File">Ross From Friends - Family Portrait.jpg</Field>
<Field Name="Duration">97.3732425999999975</Field>
<Field Name="Track #">1</Field>
<Field Name="Disc #">1</Field>
<Field Name="Media Type">Audio</Field>
<Field Name="Album Artist">Ross From Friends</Field>
<Field Name="Get Cover Art Info">&lt;XMLPH version="1.0"&gt;
...
```

## Use MCC to set a rating for the track
```
mz@mzxps:~ > jriverctl --auth mz pass -m 10023 4

```

# API Usage Examples

## Get all artists

```
r = jr.request('Values', Field='Album Artist (auto)', Files='')
    if not r:
        return None
    p = r.parsed()
    return p['Items']
```

## Get all albums by an artist

```
artist = 'Radiohead'
r = jr.request('Values', Field='Album', Files="[Album Artist (auto)]=[{}] {}".format(artist, ''))
```

