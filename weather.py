#!/usr/bin/python
# print weather forecast message
# p1=empty(today) or "tomorrow"

import urllib, sys, json
#key="96934a5c320e505396eb946b34e6f720"
key="802bcbc0941f44d4b538935923afbfca"
#latitude="51.770963"
#longditude="-1.072445"
latitude="51.754130"
longditude="-1.124867"

#url=("https://api.darksky.net/forecast/%s/%s,%s?lang=en&units=uk2" % (key,latitude,longditude))
url=("http://api.weatherbit.io/v2.0/forecast/daily?lat=%s&lon=%s&key=%s&days=2" % (latitude,longditude,key))
print(url)
r=urllib.urlopen(url)
d=json.loads(r.read())
when = "today"
if ((len(sys.argv) > 1) and (sys.argv[1] == "tomorrow")) :
    when = "tomorrow"

if False :
    if when == "tomorrow":
        summary=d["daily"]["data"][0]["summary"]
        temperature=d["daily"]["data"][0]["temperatureMax"]
        day="Tomorrows"
    else:
        summary=d["currently"]["summary"]
        temperature=d["currently"]["temperature"]
        day="Current"
else:
    if (when == "tomorrow"):
        n=1
        day="Tomorrows"
    elif (when == "today"):
        n=0
        day="Current"
    summary=d["data"][n]["weather"]["description"]
    temperature=d["data"][n]["max_temp"]


print ("%s weather:    %s    Temperature: %d degrees celsius" %(day,summary,temperature))
