# Python_Event_Parser
This is a simple Python script for parsing the discord data package for events in a given channel sent on a certain date.

You need to use the files found in the activity directory in your discord data package. Copy the file into a directory with the main.py.

Args
-h, --help,     Displays information
-c, --channel   Give the channel ID to search for
-f, --file      Give the name of the file of JSON objects to read from
-d, --date      Give the date in YEAR-MONTH-DAY format to search for

You can get the channel ID from the discord web app, it shows up as the string of numbers at the end of the url
IE:
https://discord.com/channels/@me/843736257623359498
The channel ID would be "843736257623359498"

The file parameter needs the filename. For example "events-2021-00000-of-00001.json" Is the name that was in my discord data package. 

The date parameter needs to be given in the format YEAR-MONTH-DAY
IE:
"2021-09-01" or "2020-12-18"


I'll be uploading an example discord data package in the future.
