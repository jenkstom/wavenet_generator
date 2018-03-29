#!/usr/bin/python

import requests, json, base64, sys, os

apikey="myapikey"
url=r"https://texttospeech.googleapis.com/v1beta1/text:synthesize?fields=audioContent&key=%s"%apikey

request = """
{
    "voice":
    {
        "languageCode":"en-US-Wavenet-A",
        "ssmlGender":"FEMALE"
    },
    "input":
    {
        "text":"{text}"
    },
    "audioConfig":
    {
        "audioEncoding":"mp3"
    }
}
"""

# Go through lines of input file and create mp3 from each with the given file name
infile = open(sys.argv[1],"r")
for line in infile:
    fn, txt = line.rstrip().split(":")
    r=request.replace("{text}",txt)
    print fn, txt
    #print r
    r = requests.post(url, data=r, allow_redirects=False)
    j = json.loads(r.text)
    f=open("%s.mp3"%fn,"w")
    f.write(base64.b64decode(j["audioContent"]))
    f.close()

    #Convert to WAV file for pbx system
    #os.system("mpg321 -w %s.wav %s.mp3"%(fn,fn))
