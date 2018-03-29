This is a simple audio file generator for use with Google's new wavenet text-to-speech system.
Since this voice is so realistic, it is ideal for interactive voice response systems and
so I wrote a simple script to batch create sound files.

Currently this is using Python 2, and depends on the following packages:
  json
  requests
  base64

It calls the API service and writes the decoded response to an mp3 file. If you have
mpg321 you can uncomment the convert line and it will also create WAV files for you.
You might have to tweak the command to create the proper WAV files for your PBX,
but this is working for me on freeswitch.
