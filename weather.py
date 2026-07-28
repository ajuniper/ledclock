#!/usr/bin/python
# print weather forecast message
# p1=empty(today) or "tomorrow"

import urllib, sys, json
#key="xxx"
latitude="50.5"
longditude="-1.0"

url=("https://api.darksky.net/forecast/%s/%s,%s?lang=en&units=uk2" % (key,latitude,longditude))
r=urllib.urlopen(url)
d=json.loads(r.read())

if ((len(sys.argv) > 1) and (sys.argv[1] == "tomorrow")) :
    summary=d["daily"]["data"][0]["summary"]
    temperature=d["daily"]["data"][0]["temperatureMax"]
    day="Tomorrows"
else:
    summary=d["currently"]["summary"]
    temperature=d["currently"]["temperature"]
    day="Current"

print ("%s weather:    %s    Temperature: %d degrees celsius" %(day,summary,temperature))
