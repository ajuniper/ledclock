#!/usr/bin/python
# print weather forecast message
# p1=empty(today) or "tomorrow"

import urllib, sys, json
key="96934a5c320e505396eb946b34e6f720"
latitude="51.770963"
longditude="-1.072445"

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
