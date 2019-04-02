"""
jrivermcws.cmds
~~~~~~~~~~~~~~~

Contains details of all MCWS commands and some functions to help
extract information about them


* Processed from MCWS docs with script at bottom of file

~~~~~~~~~~~~~~~

Copyright Michael Adkins 2017
Distributed under the MIT License.
See accompanying file LICENSE.md file or copy at http://opensource.org/licenses/MIT


"""

_functions = {

  'Meta': { 'Alive': { 'desc': 'Simple query to ensure the server is running and to check versions.',
                       'params': [],
                       'response': [
                         'RuntimeGUID: The runtime GUID of this web service.',
                         'LibraryVersion: The version number of the library.',
                         'ProgramName: The name of the program.',
                         'ProgramVersion: The version number of the program.',
                         'FriendlyName: The friendly name of this server.',
                         'AccessKey: The access key of this server.']},
            'Authenticate': { 'desc': 'Simple query to test and establish authentication.',
                              'params': [],
                              'response': ['Token: The token that can be appended to calls in place of HTTP authentication.']}},
  'Audio': { 'ErrorFreeMode': { 'desc': 'Set the error free mode.',
                                'params': ['ErrorFree: The state of the error free mode (0 or 1). (default: )'],
                                'response': ['ErrorFree: The new state of the error free mode.']},
             'GetDevice': { 'desc': 'Get the audio output device.',
                            'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                        "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                        'index; Name: zone name). (default: ID)'],
                            'response': [ 'DeviceIndex: The index of the active audio device.',
                                          'DeviceName: The name of the active audio device.',
                                          'DevicePlugin: The plugin of the active audio device.']},
             'ListDevices': { 'desc': 'List the available audio output devices.',
                              'params': [],
                              'response': [ 'NumberDevices: The number of available devices.',
                                            'DeviceName#: The name of the device at index #.',
                                            'DevicePlugin#: The Name of the plugin of the device at index #.']},
             'SetDevice': { 'desc': 'Set the audio output device.',
                            'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                        "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                        'index; Name: zone name). (default: ID)',
                                        'DeviceIndex: The index of the device to set as the active device. (default: '
                                        '-1)'],
                            'response': []}},
  'Browse': { 'Children': { 'desc': 'Returns child browse items for a location, enabling traversal of the browse '
                                    'hierarchy.',
                            'params': [ 'ID: The parent ID (empty to start at root). (default: )',
                                        'Skip: Set to 1 to skip browse levels that contain only one choice. (default: '
                                        ')',
                                        'Version: The version of the data used for results (2 is the newest version). '
                                        '(default: 1)'],
                            'response': []},
              'Files': { 'desc': 'Gets files for a browse item.',
                         'params': [ 'ID: The ID of the browse item. (default: )',
                                     'Action: The action to perform with the files (MPL: return MPL playlist; Play: '
                                     'plays files; Save: saves the files (as a playlist in the library, etc.); '
                                     'Serialize: return serialized file array (basically a list of file keys); M3U: '
                                     'saves the list as an m3u). (default: mpl)',
                                     'Shuffle: Set to 1 to shuffle the files. (default: )',
                                     'ActiveFile: A file key to set as active (used as the file that playback starts '
                                     'with, etc.). (default: -1)',
                                     'ActiveFileOnly: Set to 1 to trim the returned files to only contain the active '
                                     'file. (default: )',
                                     'PlayMode: Play mode flags delimited by commas (Add: adds to end of playlist; '
                                     'NextToPlay: adds files in the next to play position). (default: )',
                                     'Fields: The fields to include in an MPL (use empty to include all fields). '
                                     '(default: )',
                                     'NoLocalFilenames: Set to 1 to filter out local filenames from MPL output (since '
                                     'they might be meaningless to a server). (default: )',
                                     'PlayDoctor: Set to 1 to change the files to a Play Doctor generated playlist '
                                     'using these files as a seed. (default: )',
                                     'SaveMode: Playlist: playlist (overwrites existing; returns ID) (default: )',
                                     "SaveName: A backslash delimited path used with the action 'Save'. (default: )",
                                     'NoUI: Set to one to put the player in no UI mode. (default: )',
                                     'Zone: The zone the command is targetted for. (default: -1)',
                                     "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone index; "
                                     'Name: zone name). (default: ID)'],
                         'response': []},
              'Image': { 'desc': 'Gets the image for a browse item.',
                         'params': [ 'ID: The ID of the browse item. (default: )',
                                     'Fallback: The name of the fallback image to use if ID is invalid. (default: )',
                                     'Width: The width for the returned image. (default: )',
                                     'Height: The height for the returned image. (default: )',
                                     'FillTransparency: A color to fill image transparency with (hex number). '
                                     '(default: )',
                                     'Square: Set to 1 to crop the image to a square aspect ratio. (default: )',
                                     'Pad: Set to 1 to pad around the image with transparency to fullfill the '
                                     'requested size. (default: )',
                                     'Format: The preferred image format (jpg or png). (default: jpg)'],
                         'response': []}},
  'Configuration': {},
  'Control': { 'CommandLine': { 'desc': 'Run a command line.',
                                'params': [ 'Arguments: The command line arguments (default: )',
                                            'Target: The target for the command line (uses launcher when empty) '
                                            '(default: )'],
                                'response': []},
               'Key': { 'desc': 'Simulate the press of a keyboard key.',
                        'params': [ 'Key: The key sequence to simulate, separated by semicolons. Keys can be a single '
                                    'letter or any of the following special keys: Insert, Menu, Delete, +, -, Left, '
                                    'Right, Up, Down, Backspace, Enter, Escape, Apps, Page Up, Page Down, Home, End, '
                                    'Space, Print Screen, Tab, NumPad0...NumPad9, F1...F24 (default: )',
                                    'Focus: Brings the program to the front and takes focus if set to 1. (default: )'],
                        'response': []},
               'MCC': { 'desc': 'Perform a Media Core Command (MCC).',
                        'params': [ 'Command: The command (an integer value from the MC_COMMANDS enumeration; visit '
                                    'DevZone for the command list). (default: )',
                                    'Parameter: The parameter to the command. (default: 0)',
                                    'Block: 0: return immediately (command is posted and processed asynchronously); 1: '
                                    'wait for the command to finish before returning. (default: 0)',
                                    'Zone: The zone the command is targetted for. (default: -1)',
                                    "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone index; "
                                    'Name: zone name). (default: ID)'],
                        'response': []}},
  'DSP': { 'Loudness': { 'desc': 'Get and set the loudness.',
                         'params': [ 'Set: Set to 0 for off, 1 for on, and -1 to toggle. (default: )',
                                     'Zone: The zone the command is targetted for. (default: -1)',
                                     "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone index; "
                                     'Name: zone name). (default: ID)'],
                         'response': ['Current: The current value of the Loudness after the setting.']},
           'Set': { 'desc': 'Set whether a DSP is on or off.',
                    'params': [ 'DSP: The name of the DSP. (default: )',
                                'On: 1 for on and 0 for off. (default: )',
                                'Zone: The zone the command is targetted for. (default: -1)',
                                "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone index; Name: "
                                'zone name). (default: ID)'],
                    'response': []},
           'SetEqualizer': { 'desc': 'Set the level of an EQ slider.',
                             'params': [ 'Slider: The number of the slider. (default: )',
                                         'Level: The level of the slider. (default: )',
                                         'On: Set to one to turn on the equalizer. (default: )',
                                         'Zone: The zone the command is targetted for. (default: -1)',
                                         "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                         'index; Name: zone name). (default: ID)'],
                             'response': []},
           'SetTempo': { 'desc': 'Set the tempo.',
                         'params': [ 'Tempo: The tempo. (default: )',
                                     'Relative: Set to 1 to set the tempo relative to the current tempo. (default: )',
                                     'Zone: The zone the command is targetted for. (default: -1)',
                                     "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone index; "
                                     'Name: zone name). (default: ID)'],
                         'response': []}},
  'File': { 'CreateParticle': { 'desc': 'Create particles.',
                                'params': [ 'File: The key of the file. (default: -1)',
                                            "FileType: The type of value provided in 'File' (Key: file key; Filename: "
                                            'filename of file). (default: Key)',
                                            'Count: The number of particles to create. (default: )'],
                                'response': ['Keys: The keys of the created particles.']},
            'Delete': { 'desc': 'Deletes a file.',
                        'params': [ 'File: The key of the file. (default: -1)',
                                    "FileType: The type of value provided in 'File' (Key: file key; Filename: filename "
                                    'of file). (default: Key)'],
                        'response': []},
            'GetFile': { 'desc': 'Get the contents of a file in the database.',
                         'params': [ 'File: The key of the file. (default: -1)',
                                     "FileType: The type of value provided in 'File' (Key: file key; Filename: "
                                     'filename of file). (default: Key)',
                                     'Helper: Allows getting sidecar / helper files (used internally). (default: )',
                                     'Conversion: The conversion settings to use. (default: )',
                                     'Quality: The conversion quality to use (low, medium, high, etc.). (default: )',
                                     'Resolution: The resolution of the target device (allows making better conversion '
                                     'decisions). (default: )',
                                     'AndroidVersion: The Android version of the target device (if applicable). '
                                     '(default: )',
                                     'Prepare: Set to 1 to prepare the file (useful when waiting for video conversion, '
                                     'etc.). (default: )',
                                     'Playback: 0: Downloading (not real-time playback); 1: Real-time playback with '
                                     'update of playback statistics, Scrobbling, etc.; 2: Real-time playback, no '
                                     'playback statistics handling. (default: )',
                                     'Start: The start position for playback. This is normally seconds (decimal '
                                     'supported), but usage can vary based on playback type. (default: )',
                                     'MimeType: The mime type to use in the response (leave blank for default mime '
                                     'type). (default: )',
                                     'HLS: Use HTTP Live Streaming. (default: )',
                                     'Context: The context used to access the file (used for HTTP Live Streaming). '
                                     '(default: )'],
                         'response': [ 'PercentPrepared: The integer progress percentage of a file preparation '
                                       'operation, such as transcoding.']},
            'GetImage': { 'desc': 'Get an image for a file in the database.',
                          'params': [ 'File: The key of the file. (default: -1)',
                                      "FileType: The type of value provided in 'File' (Key: file key; Filename: "
                                      'filename of file). (default: Key)',
                                      'Type: The type of image to get: Thumbnail (default), Full, ThumbnailsBinary '
                                      '(default: Thumbnail)',
                                      'ThumbnailSize: The size of the thumbnail (if type is thumbnail): Small, Medium, '
                                      'Large (default) (default: )',
                                      'Width: The width for the returned image. (default: )',
                                      'Height: The height for the returned image. (default: )',
                                      'FillTransparency: A color to fill image transparency with (hex number). '
                                      '(default: )',
                                      'Square: Set to 1 to crop the image to a square aspect ratio. (default: )',
                                      'Pad: Set to 1 to pad around the image with transparency to fullfill the '
                                      'requested size. (default: )',
                                      'Format: The preferred image format (jpg or png). (default: jpg)'],
                          'response': []},
            'GetInfo': { 'desc': 'Get information or play a file object.',
                         'params': [ 'File: The key of the file. (default: -1)',
                                     "FileType: The type of value provided in 'File' (Key: file key; Filename: "
                                     'filename of file). (default: Key)',
                                     'Action: The action to perform with the files (MPL: return MPL playlist; Play: '
                                     'plays files; Save: saves the files (as a playlist in the library, etc.); '
                                     'Serialize: return serialized file array (basically a list of file keys); M3U: '
                                     'saves the list as an m3u). (default: mpl)',
                                     'PlayMode: Play mode flags delimited by commas (Add: adds to end of playlist; '
                                     'NextToPlay: adds files in the next to play position). (default: )',
                                     'Fields: The fields to include in an MPL (use empty to include all fields). '
                                     '(default: )',
                                     'NoLocalFilenames: Set to 1 to filter out local filenames from MPL output (since '
                                     'they might be meaningless to a server). (default: )',
                                     'PlayDoctor: Set to 1 to change the files to a Play Doctor generated playlist '
                                     'using these files as a seed. (default: )',
                                     'SaveMode: Playlist: playlist (overwrites existing; returns ID) (default: )',
                                     "SaveName: A backslash delimited path used with the action 'Save'. (default: )",
                                     'NoUI: Set to one to put the player in no UI mode. (default: )',
                                     'Zone: The zone the command is targetted for. (default: -1)',
                                     "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone index; "
                                     'Name: zone name). (default: ID)'],
                         'response': []},
            'Played': { 'desc': 'Update the play stats after a file has been played.',
                        'params': [ 'File: The key of the file. (default: -1)',
                                    "FileType: The type of value provided in 'File' (Key: file key; Filename: filename "
                                    'of file). (default: Key)'],
                        'response': []},
            'Rotate': { 'desc': 'Rotate an image file.',
                        'params': [ 'File: The key of the file. (default: -1)',
                                    "FileType: The type of value provided in 'File' (Key: file key; Filename: filename "
                                    'of file). (default: Key)',
                                    'Degrees: The degrees to rotate the image. (default: )'],
                        'response': []},
            'SetImage': { 'desc': 'Set the image for a file in the database.',
                          'params': [ 'File: The key of the file. (default: -1)',
                                      "FileType: The type of value provided in 'File' (Key: file key; Filename: "
                                      'filename of file). (default: Key)',
                                      'Type: The type of image (jpg, gif, etc.). (default: jpg)',
                                      'Image: The image (as base 64 encoded). (default: )'],
                          'response': []},
            'SetInfo': { 'desc': 'Set information about a file object.',
                         'params': [ 'File: The key of the file. (default: -1)',
                                     "FileType: The type of value provided in 'File' (Key: file key; Filename: "
                                     'filename of file). (default: Key)',
                                     'Field: The field to set. (default: )',
                                     'Value: The value to set the field to. (default: )',
                                     "List: Set to 'CSV' and comma delimit (RFC 4180) the field and value to set "
                                     'multiple values in one call. (default: )',
                                     "Formatted: Set to 1 if you're passing a formatted value (like a formatted date). "
                                     '(default: 1)'],
                         'response': []}},
  'Files': { 'Current': { 'desc': 'Get the currently selected files.',
                          'params': [ 'Action: The action to perform with the files (MPL: return MPL playlist; Play: '
                                      'plays files; Save: saves the files (as a playlist in the library, etc.); '
                                      'Serialize: return serialized file array (basically a list of file keys); M3U: '
                                      'saves the list as an m3u). (default: mpl)',
                                      'Shuffle: Set to 1 to shuffle the files. (default: )',
                                      'ActiveFile: A file key to set as active (used as the file that playback starts '
                                      'with, etc.). (default: -1)',
                                      'ActiveFileOnly: Set to 1 to trim the returned files to only contain the active '
                                      'file. (default: )',
                                      'PlayMode: Play mode flags delimited by commas (Add: adds to end of playlist; '
                                      'NextToPlay: adds files in the next to play position). (default: )',
                                      'Fields: The fields to include in an MPL (use empty to include all fields). '
                                      '(default: )',
                                      'NoLocalFilenames: Set to 1 to filter out local filenames from MPL output (since '
                                      'they might be meaningless to a server). (default: )',
                                      'PlayDoctor: Set to 1 to change the files to a Play Doctor generated playlist '
                                      'using these files as a seed. (default: )',
                                      'SaveMode: Playlist: playlist (overwrites existing; returns ID) (default: )',
                                      "SaveName: A backslash delimited path used with the action 'Save'. (default: )",
                                      'NoUI: Set to one to put the player in no UI mode. (default: )',
                                      'Zone: The zone the command is targetted for. (default: -1)',
                                      "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone index; "
                                      'Name: zone name). (default: ID)'],
                          'response': []},
             'Search': { 'desc': 'Perform a database search for files.',
                         'params': [ 'Query: The search string (empty returns full library) (default: )',
                                     'Action: The action to perform with the files (MPL: return MPL playlist; Play: '
                                     'plays files; Save: saves the files (as a playlist in the library, etc.); '
                                     'Serialize: return serialized file array (basically a list of file keys); M3U: '
                                     'saves the list as an m3u). (default: mpl)',
                                     'Shuffle: Set to 1 to shuffle the files. (default: )',
                                     'ActiveFile: A file key to set as active (used as the file that playback starts '
                                     'with, etc.). (default: -1)',
                                     'ActiveFileOnly: Set to 1 to trim the returned files to only contain the active '
                                     'file. (default: )',
                                     'PlayMode: Play mode flags delimited by commas (Add: adds to end of playlist; '
                                     'NextToPlay: adds files in the next to play position). (default: )',
                                     'Fields: The fields to include in an MPL (use empty to include all fields). '
                                     '(default: )',
                                     'NoLocalFilenames: Set to 1 to filter out local filenames from MPL output (since '
                                     'they might be meaningless to a server). (default: )',
                                     'PlayDoctor: Set to 1 to change the files to a Play Doctor generated playlist '
                                     'using these files as a seed. (default: )',
                                     'SaveMode: Playlist: playlist (overwrites existing; returns ID) (default: )',
                                     "SaveName: A backslash delimited path used with the action 'Save'. (default: )",
                                     'NoUI: Set to one to put the player in no UI mode. (default: )',
                                     'Zone: The zone the command is targetted for. (default: -1)',
                                     "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone index; "
                                     'Name: zone name). (default: ID)'],
                         'response': []}},
  'Handheld': { 'Sync': { 'desc': 'Run a sync of an attached handheld.',
                          'params': [ 'Device: The device to sync. (default: )',
                                      "DeviceType: The type of value provided in 'Device' (Name: device name; ID: "
                                      'session id). (default: Name)',
                                      'ShowWarnings: If warnings are allowed. (default: 1)'],
                          'response': []}},
  'Library': { 'Connect': { 'desc': 'Connects to a remote library.',
                            'params': ['URL: A URL for connecting to a library server. (default: )'],
                            'response': []},
               'CreateField': { 'desc': 'Creates a library field.',
                                'params': [ 'Name: The name of the field. (default: )',
                                            'Type: The data type of the field (string or integer). (default: string)'],
                                'response': ['Field: The name of the updated or created field.']},
               'CreateFile': { 'desc': 'Creates a library file.',
                               'params': [],
                               'response': ['Key: The key of the new file.']},
               'Fields': {'desc': 'Gets the fields in the library.', 'params': [], 'response': []},
               'Get': { 'desc': 'Get a copy of the library.',
                        'params': [ 'Settings: Whether settings should be included with the library. (default: 0)',
                                    'IncrementalFileSignaturesXML: A block of XML containing file signatures. When '
                                    'this is provided, only changed files will be returned. (default: )'],
                        'response': []},
               'GetRevision': { 'desc': 'Get the revision number of the library.',
                                'params': [],
                                'response': [ 'Master: The master revision number of the database.',
                                              'Sync: The revision number of the database (only included sync-worthy '
                                              'revisions).',
                                              'LibraryStartup: Timestamp of the Library Startup (ie. the last reset of '
                                              'the revision counter).']},
               'GetStats': { 'desc': 'Get some stats about the library.',
                             'params': [],
                             'response': [ 'Files: The number of files in the library.',
                                           'Artists: The number of artists in the library.',
                                           'Albums: The number of albums in the library.']},
               'Import': { 'desc': 'Imports files from a folder.',
                           'params': [ 'Path: The path to search for files. (default: )',
                                       'Block: Whether the import should finish before the function returns. (default: '
                                       '0)'],
                           'response': []},
               'List': { 'desc': 'Gets a list of libraries.',
                         'params': [],
                         'response': ['NumberOfLibraries: The number of libraries.']},
               'Load': { 'desc': 'Loads a library.',
                         'params': ['Library: The index of the library to load (from Library/List). (default: )'],
                         'response': []},
               'Merge': { 'desc': 'Merge changes into the library.',
                          'params': ['Delta: A binary package describing the changes. (default: )'],
                          'response': [ "MasterRevision: Library 'Master' revision number after changes have been "
                                        'applied.',
                                        "SyncRevision: Library 'Sync' revision number after changes have been applied.",
                                        'NewFiles: A semicolon delimited list of new files in the form: client '
                                        'key;server key;client key;server key;etc.']},
               'Values': { 'desc': 'Get a list of values from the database (artists, albums, etc.).',
                           'params': [ 'Filter: Empty to get all values for a particular field, or some search to get '
                                       'matching values from any number of fields. (default: )',
                                       'Field: A comma-delimited list of fields to get values from (leave blank when '
                                       'searching to search default fields). (default: )',
                                       'Files: A search to use to get the files to retrieve values from (use empty to '
                                       'use all imported files). (default: )',
                                       'Limit: Maximum number of values to return. (default: )',
                                       'Version: The version of the data used for results (2 is the newest version). '
                                       '(default: 1)'],
                           'response': []}},
  'Playback': { 'AudioPath': { 'desc': 'Gets the audio path information for the current playback.',
                               'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                           "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                           'index; Name: zone name). (default: ID)'],
                               'response': [ 'AudioPath: The list of changes being made.',
                                             "Direct: Whether we're in direct mode."]},
                'ClearPlaylist': { 'desc': 'Clear the current playlist and stop playback.',
                                   'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                               "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: "
                                               'zone index; Name: zone name). (default: ID)'],
                                   'response': []},
                'EditPlaylist': { 'desc': 'Edit the current playlist (move, remove, etc.)',
                                  'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                              "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: "
                                              'zone index; Name: zone name). (default: ID)',
                                              'Action: The edit action (Move, Remove). (default: )',
                                              'Source: The source file index (0-based). (default: )',
                                              'Target: The target index when moving (0-based). (default: )'],
                                  'response': []},
                'Info': { 'desc': 'Get information about the current playback.',
                          'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                      "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone index; "
                                      'Name: zone name). (default: ID)'],
                          'response': [ 'ZoneID: The zone ID of this zone.',
                                        'ZoneName: The display name of this zone.',
                                        'State: The playback state of the player.',
                                        'FileKey: The database key of the playing file.',
                                        'NextFileKey: The database key of the next file to play.',
                                        'PositionMS: The position of the playback in milliseconds.',
                                        'DurationMS: The duration of the playing file in milliseconds.',
                                        'ElapsedTimeDisplay: The elapsed playback time as a display friendly string.',
                                        'RemainingTimeDisplay: The remaining playback time as a display friendly '
                                        'string.',
                                        'TotalTimeDisplay: The total playback time as a display friendly string.',
                                        'PositionDisplay: The playback position as a display friendly string.',
                                        'PlayingNowPosition: The index of the current track in Playing Now.',
                                        'PlayingNowTracks: The number of files in Playing Now.',
                                        'PlayingNowPositionDisplay: The current Playing Now position formatted for '
                                        'display.',
                                        'PlayingNowChangeCounter: A counter that increments any time the playlist is '
                                        'changed.',
                                        'Bitrate: The current bitrate, in kbps.',
                                        'Bitdepth: The current bitdepth.',
                                        'SampleRate: The current sample rate in Hz.',
                                        'Channels: The number of audio channels in the current output.',
                                        'Chapter: The current playback chapter.',
                                        'Volume: The current volume.',
                                        'VolumeDisplay: A display friendly string version of the current volume.',
                                        'ImageURL: An image URL for the current file.',
                                        'Artist: Artist of current file.',
                                        'Album: Album of current file.',
                                        'Name: Name of current file.',
                                        'Rating: Rating of current file.',
                                        'Status: Playback status as a displayable string.',
                                        'LinkedZones: Semicolon delimited list of zone names in the link (only '
                                        'provided if this zone is part of a link).']},
                'LinkZones': { 'desc': 'Links the specified zones.',
                               'params': [ 'Zone1: The zone the command is targetted for. (default: -1)',
                                           "ZoneType1: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                           'index; Name: zone name). (default: ID)',
                                           'Zone2: The zone the command is targetted for. (default: -1)',
                                           "ZoneType2: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                           'index; Name: zone name). (default: ID)'],
                               'response': []},
                'Next': { 'desc': 'Advance to the next track.',
                          'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                      "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone index; "
                                      'Name: zone name). (default: ID)',
                                      'Block: Set to one to block the call from returning until the next has finished. '
                                      '(default: )'],
                          'response': []},
                'Pause': { 'desc': 'Set the pause state.',
                           'params': [ 'State: The new pause state (0: unpaused, 1: paused, -1: toggle). (default: -1)',
                                       'Zone: The zone the command is targetted for. (default: -1)',
                                       "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                       'index; Name: zone name). (default: ID)'],
                           'response': []},
                'PlayAdvanced': { 'desc': 'Plays files using a PLAY_COMMAND object (for internal use).',
                                  'params': [ 'PlayCommand: Serialized PLAY_COMMAND object (for internal use only). '
                                              '(default: )',
                                              'Zone: The zone the command is targetted for. (default: -1)',
                                              "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: "
                                              'zone index; Name: zone name). (default: ID)'],
                                  'response': []},
                'PlayByFilename': { 'desc': 'Play a set of files by filename.',
                                    'params': [ 'Filenames: A pipe delimited list of filenames to play. (default: )',
                                                "Location: The location of the file. Use 'End' to add to the end of "
                                                "the current playlist, 'Next' to play next, or a number to insert at a "
                                                'specific index. (default: End)',
                                                'Zone: The zone the command is targetted for. (default: -1)',
                                                "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: "
                                                'zone index; Name: zone name). (default: ID)'],
                                    'response': []},
                'PlayByIndex': { 'desc': 'Play a file in Playing Now.',
                                 'params': [ 'Index: The index of the file to play (0 based). (default: 0)',
                                             'NoUI: Set to one to put the player in no UI mode. (default: )',
                                             'Zone: The zone the command is targetted for. (default: -1)',
                                             "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                             'index; Name: zone name). (default: ID)'],
                                 'response': []},
                'PlayByKey': { 'desc': 'Play a file by database key.',
                               'params': [ 'Key: The key of the file to play. (default: -1)',
                                           "Location: The location of the file. Use 'End' to add to the end of the "
                                           "current playlist, 'Next' to play next, or a number to insert at a specific "
                                           'index. (default: )',
                                           'Album: Set to 1 to play the entire album starting at this file. (default: '
                                           ')',
                                           'Zone: The zone the command is targetted for. (default: -1)',
                                           "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                           'index; Name: zone name). (default: ID)'],
                               'response': []},
                'PlayDoctor': { 'desc': 'Plays using Play Doctor.',
                                'params': [ 'Seed: The Play Doctor seed. (default: )',
                                            'Zone: The zone the command is targetted for. (default: -1)',
                                            "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                            'index; Name: zone name). (default: ID)'],
                                'response': []},
                'PlayLive': { 'desc': 'Play from a live source.',
                              'params': [ 'Mode: The mode of live playback. (default: )',
                                          'Zone: The zone the command is targetted for. (default: -1)',
                                          "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                          'index; Name: zone name). (default: ID)'],
                              'response': []},
                'PlayPause': { 'desc': 'Start playback or toggle the pause state.',
                               'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                           "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                           'index; Name: zone name). (default: ID)'],
                               'response': []},
                'PlayPlaylist': { 'desc': 'Plays a playlist.',
                                  'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                              "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: "
                                              'zone index; Name: zone name). (default: ID)',
                                              'Playlist: The ID of the playlist to play or the path. (default: )',
                                              "PlaylistType: The type of value provided in 'Playlist' (ID: playlist "
                                              'id; Path: playlist path). (default: ID)'],
                                  'response': []},
                'Playlist': { 'desc': 'Get the current playlist.',
                              'params': [ 'Action: The action to perform with the files (MPL: return MPL playlist; '
                                          'Play: plays files; Save: saves the files (as a playlist in the library, '
                                          'etc.); Serialize: return serialized file array (basically a list of file '
                                          'keys); M3U: saves the list as an m3u). (default: mpl)',
                                          'Shuffle: Set to 1 to shuffle the files. (default: )',
                                          'ActiveFile: A file key to set as active (used as the file that playback '
                                          'starts with, etc.). (default: -1)',
                                          'ActiveFileOnly: Set to 1 to trim the returned files to only contain the '
                                          'active file. (default: )',
                                          'PlayMode: Play mode flags delimited by commas (Add: adds to end of '
                                          'playlist; NextToPlay: adds files in the next to play position). (default: )',
                                          'Fields: The fields to include in an MPL (use empty to include all fields). '
                                          '(default: )',
                                          'NoLocalFilenames: Set to 1 to filter out local filenames from MPL output '
                                          '(since they might be meaningless to a server). (default: )',
                                          'PlayDoctor: Set to 1 to change the files to a Play Doctor generated '
                                          'playlist using these files as a seed. (default: )',
                                          'SaveMode: Playlist: playlist (overwrites existing; returns ID) (default: )',
                                          "SaveName: A backslash delimited path used with the action 'Save'. (default: "
                                          ')',
                                          'NoUI: Set to one to put the player in no UI mode. (default: )',
                                          'Zone: The zone the command is targetted for. (default: -1)',
                                          "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                          'index; Name: zone name). (default: ID)'],
                              'response': []},
                'Position': { 'desc': 'Get / set the position.',
                              'params': [ 'Position: The position to seek to, in milliseconds. (default: )',
                                          "Relative: When set to 1, 'Position' will be added to the current position "
                                          "to allow jumping forward. When set to -1, 'Position' will be subtracted "
                                          "from the current position to allow jumping backwards. Use a 'Position' of "
                                          '-1 to jump the default amount based on the media type. (default: )',
                                          'Zone: The zone the command is targetted for. (default: -1)',
                                          "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                          'index; Name: zone name). (default: ID)'],
                              'response': ['Position: The position in milliseconds (after applying changes, if any).']},
                'Previous': { 'desc': 'Advance to the previous track.',
                              'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                          "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                          'index; Name: zone name). (default: ID)',
                                          'Block: Set to one to block the call from returning until the previous has '
                                          'finished. (default: )'],
                              'response': []},
                'Repeat': { 'desc': 'Get / set the repeat state (Modes: Off, Playlist, Track, Stop, Toggle).',
                            'params': [ 'Mode: The new repeat mode. Leave this blank to query for the current mode. '
                                        '(default: )',
                                        'Zone: The zone the command is targetted for. (default: -1)',
                                        "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                        'index; Name: zone name). (default: ID)'],
                            'response': ['Mode: The repeat mode (after applying changes, if any).']},
                'SetPlaylist': { 'desc': 'Set the current playlist.',
                                 'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                             "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                             'index; Name: zone name). (default: ID)',
                                             'Playlist: A serialized playlist. (default: )'],
                                 'response': []},
                'SetZone': { 'desc': 'Set the active zone.',
                             'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                         "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                         'index; Name: zone name). (default: ID)'],
                             'response': []},
                'Shuffle': { 'desc': 'Get / set the shuffle state (Modes: Off, On, Automatic, Toggle, Reshuffle).',
                             'params': [ 'Mode: The new shuffle mode. Leave this blank to query for the current mode. '
                                         '(default: )',
                                         'Zone: The zone the command is targetted for. (default: -1)',
                                         "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                         'index; Name: zone name). (default: ID)'],
                             'response': ['Mode: The shuffle mode (after applying changes, if any).']},
                'Stop': { 'desc': 'Stops playback.',
                          'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                      "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone index; "
                                      'Name: zone name). (default: ID)'],
                          'response': []},
                'UnlinkZones': { 'desc': 'Unlinks the specified zone.',
                                 'params': [ 'Zone: The zone the command is targetted for. (default: -1)',
                                             "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                             'index; Name: zone name). (default: ID)'],
                                 'response': []},
                'UpdatePlayStats': { 'desc': 'Update the play stats.',
                                     'params': ['File: The file to update play stats for. (default: )'],
                                     'response': []},
                'Volume': { 'desc': 'Get / set the volume.',
                            'params': [ 'Level: Level to change the volume to as a decimal from 0 to 1. Leave this '
                                        'blank to leave the volume unchanged and query for the current volume. '
                                        '(default: )',
                                        "Relative: When set to 1, 'Level' will be added to the current volume to allow "
                                        'increasing or descreasing the volume by some amount. (default: )',
                                        'Zone: The zone the command is targetted for. (default: -1)',
                                        "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                        'index; Name: zone name). (default: ID)'],
                            'response': [ 'Level: The volume as a decimal between 0 and 1 (after applying changes, if '
                                          'any).',
                                          'Display: The volume as a display string (after applying changes, if any).']},
                'Zones': { 'desc': 'Get information about all zones.',
                           'params': ['Hidden: Set to 1 to see hidden zones. (default: )'],
                           'response': [ 'NumberZones: The number of zones.',
                                         'CurrentZoneID: The current zone ID.',
                                         'CurrentZoneIndex: The current zone index.',
                                         'ZoneName#: The name of the zone at index #.',
                                         'ZoneID#: The ID of the zone at index #.',
                                         'ZoneGUID#: The GUID of the zone at index #.',
                                         'ZoneDLNA#: Whether the zone at index # is a DLNA zone.']}},
  'Playlist': { 'AddFile': { 'desc': 'Add a file to a playlist.',
                             'params': [ 'Playlist: The playlist the command is targetted for. (default: )',
                                         "PlaylistType: The type of value provided in 'Playlist' (ID: playlist id; "
                                         'Path: playlist path). (default: ID)',
                                         'File: The key of the file. (default: -1)',
                                         "FileType: The type of value provided in 'File' (Key: file key; Filename: "
                                         'filename of file). (default: Key)'],
                             'response': []},
                'Delete': { 'desc': 'Deletes the playlist.',
                            'params': [ 'Playlist: The playlist the command is targetted for. (default: )',
                                        "PlaylistType: The type of value provided in 'Playlist' (ID: playlist id; "
                                        'Path: playlist path). (default: ID)'],
                            'response': []},
                'Files': { 'desc': 'Gets the files of a playlist.',
                           'params': [ 'Playlist: The playlist the command is targetted for. (default: )',
                                       "PlaylistType: The type of value provided in 'Playlist' (ID: playlist id; Path: "
                                       'playlist path). (default: ID)',
                                       'Action: The action to perform with the files (MPL: return MPL playlist; Play: '
                                       'plays files; Save: saves the files (as a playlist in the library, etc.); '
                                       'Serialize: return serialized file array (basically a list of file keys); M3U: '
                                       'saves the list as an m3u). (default: mpl)',
                                       'Shuffle: Set to 1 to shuffle the files. (default: )',
                                       'ActiveFile: A file key to set as active (used as the file that playback starts '
                                       'with, etc.). (default: -1)',
                                       'ActiveFileOnly: Set to 1 to trim the returned files to only contain the active '
                                       'file. (default: )',
                                       'PlayMode: Play mode flags delimited by commas (Add: adds to end of playlist; '
                                       'NextToPlay: adds files in the next to play position). (default: )',
                                       'Fields: The fields to include in an MPL (use empty to include all fields). '
                                       '(default: )',
                                       'NoLocalFilenames: Set to 1 to filter out local filenames from MPL output '
                                       '(since they might be meaningless to a server). (default: )',
                                       'PlayDoctor: Set to 1 to change the files to a Play Doctor generated playlist '
                                       'using these files as a seed. (default: )',
                                       'SaveMode: Playlist: playlist (overwrites existing; returns ID) (default: )',
                                       "SaveName: A backslash delimited path used with the action 'Save'. (default: )",
                                       'NoUI: Set to one to put the player in no UI mode. (default: )',
                                       'Zone: The zone the command is targetted for. (default: -1)',
                                       "ZoneType: The type of value provided in 'Zone' (ID: zone id; Index: zone "
                                       'index; Name: zone name). (default: ID)'],
                           'response': []}},
  'Playlists': { 'Add': { 'desc': 'Add a new playlist.',
                          'params': [ 'Type: The type of playlist to create (Playlist, Smartlist, Playlist Group). '
                                      '(default: )',
                                      'Path: The full path to the new playlist. (default: )',
                                      'Search: The search search to use to get the files to retrieve values from (use '
                                      'empty to use all imported files). (default: )',
                                      'CreateMode: The creation mode (Overwite: overwrite the existing playlist at the '
                                      'path; Rename: rename the new playlist if a playlist already exists at the '
                                      'path). (default: )'],
                          'response': ['PlaylistID: The ID of the newly created playlist.']},
                 'List': {'desc': 'Gets a list of all playlists.', 'params': [], 'response': []}},
  'Podcast': { 'Delete': { 'desc': 'Delete a podcast.',
                           'params': ['Name: The name of the podcast to delete. (default: )'],
                           'response': []}},
  'Settings': { 'AddNetworkDrive': { 'desc': 'Adds a network drive.',
                                     'params': [ 'SourcePath: The path to the network drive. (default: )',
                                                 'MountPath: The directory name for the mounted drive. (default: )',
                                                 'IsWindows: Whether or not the drive is on a Windows computer. '
                                                 '(default: )',
                                                 'AccessOptions: Whether the mounted drive is read-only or read-write. '
                                                 '(default: )',
                                                 'Guest: Whether or not the user is a guest. (default: )',
                                                 'Username: The username on the network drive. (default: )',
                                                 'Password: The user password on the network drive. (default: )'],
                                     'response': []},
                'ChangeRemotePassword': { 'desc': 'Changes the remote access password for the Id.',
                                          'params': ['Password: The new password for remote access. (default: )'],
                                          'response': []},
                'ChangeSystemName': { 'desc': 'Changes the Id system name.',
                                      'params': ['Name: The new Id system name. (default: )'],
                                      'response': []},
                'CheckForUpdates': { 'desc': 'Checks for updates and updates Id to the latest version',
                                     'params': [],
                                     'response': []},
                'ConfigureNetwork': { 'desc': 'Configure the protperties for a selected wireless network.',
                                      'params': [ 'SecurityType: The security type of the network. (default: )',
                                                  'NetworkName: The name of the wireless network (ESSID). (default: )',
                                                  'NetworkKey: The wireless network access key. (default: )'],
                                      'response': []},
                'CreateStaticIP': { 'desc': 'Create a static IP address.',
                                    'params': [ 'Interface: The interface to create the static IP address for, such as '
                                                'eth0. (default: )',
                                                'Address: The static IP address to use. (default: )',
                                                'Netmask: The static netmask (default: )',
                                                'Broadcast: The static broadcast IP address. (default: )',
                                                'Gateway: The default gateway address. (default: )'],
                                    'response': []},
                'DoDHCP': { 'desc': 'Use DHCP to assign an IP address network connection.',
                            'params': [ 'Interface: The interface to set a DHCP IP address for, such as eth0. '
                                        '(default: )'],
                            'response': []},
                'MixerSetVolume': { 'desc': 'Set the volume level in the AlsaMixer.',
                                    'params': [ 'SoundCard: The sound card to configure the volume for. (default: )',
                                                'Output: The output device. (default: )',
                                                'Volume: The volume level to set. (default: )',
                                                'UnmuteMute: Mutes or unmutes the output device. (default: )'],
                                    'response': []},
                'Reboot': { 'desc': 'Reboots the system.',
                            'params': [],
                            'response': ['Status: Displays the status of the system.']},
                'ReenterLicenseKey': { 'desc': 'Allows the user to re-install the Id license',
                                       'params': ['License: The license key for the Id. (default: )'],
                                       'response': []},
                'RemoveNetwork': { 'desc': 'Removes all network configurations for a given interface.',
                                   'params': [ 'Interface: The interface to remove the network configurations from. '
                                               '(default: )'],
                                   'response': []},
                'RemoveNetworkDrive': { 'desc': 'Removes a selected network drive.',
                                        'params': ['DriveSelection: The drive selected to be removed. (default: )'],
                                        'response': []},
                'ResetToDefaultSettings': { 'desc': 'Resets the Id to the default settings and clears the library.',
                                            'params': ['Confirmation: Confirmation for this option. (default: )'],
                                            'response': []},
                'RestartNetworking': { 'desc': 'Restart networks to load any networking changes.',
                                       'params': [],
                                       'response': []},
                'ShowAudioDeviceInfo': { 'desc': 'Shows thwe information for connected audio devices.',
                                         'params': [],
                                         'response': [ 'ShowAudioDeviceInfo: The information for connected audio '
                                                       'devices.']},
                'ShowNetworkDrives': { 'desc': 'Shows a list of mounted network drives.',
                                       'params': ['MenuOption: The menu option selection. (default: )'],
                                       'response': ['NetworkDrives: A list of the available network drives.']},
                'ShowNetworkInfo': { 'desc': 'Show the network information for the device.',
                                     'params': [],
                                     'response': [ 'IPConfig: Displays the IP configuration.',
                                                   'Netstat: The routing table information.']},
                'ShowWirelessNetworks': { 'desc': 'Lists the avialable wireless networks.',
                                          'params': [],
                                          'response': ['WirelessNetworks: A list of the available wireless networks.']},
                'Shutdown': {'desc': 'Shutdown the system.', 'params': [], 'response': []},
                'UIMode': { 'desc': 'Reboots the Id into selected UI mode.',
                            'params': [ 'UIMode: The mode to reboot the Id into ("1" for GUI mode, "2" for Headless '
                                        'text, "3" for text with HDMI intiliazation). (default: 2)'],
                            'response': []},
                'USBDrivesOptions': { 'desc': 'Options for configuring or showing USB drives.',
                                      'params': ['MenuOption: The menu option selection. (default: )'],
                                      'response': ['USBDrivesStatuses: Shows the statuses for usb drives.']}},
  'UserInterface': { 'Info': { 'desc': 'Gets information about the state of the user interface.',
                               'params': [],
                               'response': [ 'Mode: The user interface mode expressed as a UI_MODES integer (defined '
                                             'in MCCommands.h).',
                                             'InternalMode: The internal user interface mode as a UI_MODES integer '
                                             '(will be in the UI_MODE_INTERNAL_* block).',
                                             'ViewDisplayName: The display name of the current view.',
                                             'SelectionDisplayName: The display name of the current selection.']}}
  }


from .exceptions import BadCommandException, NullCommandException
from requests.structures import CaseInsensitiveDict


# Make function details available
details = CaseInsensitiveDict(name='command_details')
for cat in _functions:
    details[cat] = CaseInsensitiveDict(name=cat + '_command_details')
    for cmd in _functions[cat]:
        if cat == 'Meta':
            cmdstr = cmd
        else:
            cmdstr = cat + '/' + cmd
        details[cat][cmd] = {**_functions[cat][cmd], 'cmdstr': cmdstr}



# Find the category by the command string
categorybycommand = CaseInsensitiveDict(name='command_categories')
for (k, v) in _functions.items():
    for c in v:
        categorybycommand[c] = k

def categoryof(cmd):
    if cmd in categorybycommand:
        return categorybycommand[cmd]
    else:
        return None


# Helper functions for command details


def param_count(command, category=None):

    if command == None:
        raise NullCommandException
    if category == None:
        category = categorybycommand(command)
    if category == None:
        raise BadCommandException

    return len(details[category][command]['params'])


def expected_response_count(command, category=None):

    if command == None:
        raise NullCommandException
    if category == None:
        category = categorybycommand(command)
    if category == None:
        raise BadCommandException

    return len(details[category][command]['response'])


"""

# Raw was pulled in a weird way so it's not shown
# Maybe will fix eventually

# raw = readlines from file, join into single content, parse into dictionary by category
#  e.g. {'   Audio': [['      ListDevices', ...], ['      SetDevice',
#    '         Set the audio output device.',
#    '         Parameters:', ...

# Strip leading whitespace from content
sraw = {}
for k in raw:
    content = []
    for i in raw[k]:
        subcontent = []
        for j in i:
            subcontent.append(j.lstrip())
        content.append(subcontent)
    sraw[k.lstrip()] = content
commands = {}

# Build functions nested dictionary 'commands'
for cat in sraw:
    commands[cat] = {}
    for cmd in sraw[cat]:
        name = cmd[0]
        commands[cat][name] = {}
        commands[cat][name]['desc'] = cmd[1]
        mode = ''
        commands[cat][name]['params'] = []
        commands[cat][name]['response'] = []
        for i in range(2,len(cmd)):
            if cmd[i] == 'Parameters:':
                mode = 'params'
            elif cmd[i] == 'Response:':
                mode = 'response'
            elif cmd[i] == 'Examples:':
                mode = 'exam'
            else:
                if mode == 'exam': continue
                commands[cat][name][mode].append(cmd[i])
import pprint
pp = pprint.PrettyPrinter(indent=2,width=120)
pp.pprint(commands)functions

"""
