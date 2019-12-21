from flask import Flask,request,redirect
import random
import sys
import os
import subprocess
import re
import time
from googletrans import Translator
app = Flask(__name__)

# for looking up weather
import urllib, json
key="96934a5c320e505396eb946b34e6f720"
latitude="51.770963"
longditude="-1.072445"


@app.route('/')
@app.route('/index')
def page():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as text_file:
        temp = int(text_file.read())
        v1=subprocess.check_output(['amixer', 'get', 'PCM'])
        v2=re.search(r'([0-9]+)%', v1)
        if v2:
            curvolume=v2.group(1)
        else:
            curvolume="unknown"

    return (
'''<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<meta http-equiv="Content-Language" content="en"/>
<title>Matthew's Clock</title>
</head>
<body>
<form action = "post" method = "POST">
<table>
<tr>
<td colspan="2">
<input type = "text" name = "msg" />
</td>
</tr>
<tr>
<td colspan="2">
<select name="lang">
<option value="en">English</option>
<option value="fr">French</option>
<option value="es">Spanish</option>
<option value="de">German</option>
<option value="zh-cn">Chinese</option>
<option value="la">Latin</option>
<option value="cy">Welsh</option>
</select>
</td>
</tr>

<tr>
<td>
<input type="submit" name="action" value="Send Message" />
</td>
<td>
<input type="submit" name="action" value="Speak Message" />
</td>
</tr>

<tr>
<td>
<input type="submit" name="action" value="Tell me a joke" />
</td>
<td>
<input type="submit" name="action" value="Read me a joke" />
</td>
</tr>

<tr>
<td colspan=2><input type="submit" name="action" value="Weather forecast for today" /></td>
</tr>
<tr>
<td colspan=2><input type="submit" name="action" value="Weather forecast for tomorrow" /></td>
</tr>

</table>
</form>

<hr/>
<table border="1">
<tr>
<th>Volume</th>
<th>Radio</th>
</tr>
<tr>
<td width="80"><a href="volume?level=0">Mute</a></td>
<td>Volume:<br/>''' + curvolume + '''</td>
</tr>
<tr>
<td width="80"><a href="volume?level=1">Lowest</a></td>
<td><a href="radio?name=stop">Stop Radio</a></td>
</tr>
<tr>
<td width="80"><a href="volume?level=10">1</a></td>
<td><a href="radio?name=jackfm">Jack FM</a></td>
</tr>
<tr>
<td width="80"><a href="volume?level=20">2</a></td>
<td><a href="radio?name=radio1">BBC Radio 1</a></td>
</tr>
<tr>
<td width="80"><a href="volume?level=30">3</a></td>
<td><a href="radio?name=radio2">BBC Radio 2</a></td>
</tr>
<tr>
<td width="80"><a href="volume?level=40">4</a></td>
<td><a href="radio?name=radio3">BBC Radio 3</a></td>
</tr>
<tr>
<td width="80"><a href="volume?level=50">Max</a></td>
<td><a href="radio?name=radio4">BBC Radio 4</a></td>
</tr>
<tr>
<td width="80"></td>
<td><a href="radio?name=jack2">Jack 2</a></td>
</tr>
</table>
<hr/>
<table border="1">
<tr>
<th colspan="3">Lamp</th>
</tr>
<tr>
<td width="30%" align="center"><a href="lamp?button=0">Off</a></td>
<td/>
<td width="30%" align="center"><a href="lamp?button=1">On</a></td>
</tr>
<tr>
<td width="30%" align="center"><a href="lamp?button=red">Red</a></td>
<td width="30%" align="center"><a href="lamp?button=green">Green</a></td>
<td width="30%" align="center"><a href="lamp?button=blue">Blue</a></td>
</tr>
<tr>
<td width="30%" align="center"><a href="lamp?button=yellow">Yellow</a></td>
<td width="30%" align="center"><a href="lamp?button=cyan">Cyan</a></td>
<td width="30%" align="center"><a href="lamp?button=magenta">Magenta</a></td>
</tr>
<tr>
<td width="30%" align="center"><a href="lamp?button=-">Dimmer</a></td>
<td/>
<td width="30%" align="center"><a href="lamp?button=%2b">Brighter</a></td>
</tr>
<tr>
<td width="30%" align="center"><a href="lamp?button=a">Auto</a></td>
<td width="30%" align="center"><a href="lamp?button=white">White</a></td>
<td width="30%" align="center"><a href="lamp?button=m">Manual</a></td>
</tr>
</table>
<hr/>
<table border="1">
<tr>
<td>Temperature: ''' + str(int(temp/1000)) + '''</td>
<td><a href="manage?action=restartclock">Restart Clock</a></td>
</tr>
<tr>
<td/>
<td><a href="manage?action=reboot">Reboot Clock</a></td>
</tr>
<tr>
<td/>
<td><a href="manage?action=shutdown">Shutdown Clock</a></td>
</tr>
</table>
</body>
</html>'''
)

def getweather(when):
    url=("https://api.darksky.net/forecast/%s/%s,%s?lang=en&units=uk2" % (key,latitude,longditude))
    r=urllib.urlopen(url)
    d=json.loads(r.read())
    day=""
    if (when == "tomorrow"):
        summary=d["daily"]["data"][0]["summary"]
        temperature=d["daily"]["data"][0]["temperatureMax"]
        day="Tomorrows"
    elif (when == "today"):
        summary=d["currently"]["summary"]
        temperature=d["currently"]["temperature"]
        day="Current"

    if (day != ""):
        return ("%s weather:    %s    Temperature: %d degrees celsius" %(day,summary,temperature))

    return ""

@app.route('/post',methods = ['POST'])
def result():
    #print >> sys.stderr, ("%s\n" % request.form['action'])
    #print >> sys.stderr, ("%s\n" % request.form['msg'])
    if (request.method != 'POST'):
        return redirect("index", code=302)

    lang=request.form['lang']
    action=request.form['action']

    if (action == 'Send Message') or (action == 'Speak Message'):
        msg=request.form['msg']

    if (action == 'Tell me a joke') or (action == 'Read me a joke'):
        joke = random.randint(1,numjokes)
        msg=jokes[joke]

    if (action.startswith('Weather forecast')):
        msg=getweather(action.split()[-1])

    if (lang != "en"):
        translator = Translator()
        msg=translator.translate(msg,dest=lang).text

    if (action == 'Read me a joke') or (action == 'Speak Message') or (action.startswith("Weather forecast")):
        if (msg):
            subprocess.check_call(['/home/pi/audio.sh', 'say', msg, lang])

    with open(("/run/clockmsg/%d" % random.randint(1,99999999)), "w") as text_file:
        text_file.write(msg.encode("utf-8"))

    return redirect("index", code=302)

@app.route('/manage',methods = ['GET'])
def manage():
    if request.method == 'GET':
        print >>sys.stderr, request.args.get("action")
        a = request.args.get("action")
        if (a == "restartclock"):
            os.system("systemctl restart ledclock")
        elif (a == "reboot"):
            os.system("echo 'sleep 5 ; /sbin/shutdown -r now' | at now")
        elif (a == "shutdown"):
            os.system("echo 'sleep 5 ; /sbin/shutdown -h now' | at now")

    return redirect("index", code=302)

@app.route('/lamp',methods = ['GET'])
def lamp():
    if request.method == 'GET':
        print >>sys.stderr, request.args.get("button")
        subprocess.check_call(['/home/pi/irsling', '-f', '/home/pi/jedi_new.conf', '-p', '4', '--', request.args.get("button")])

    return redirect("index", code=302)

@app.route('/volume',methods = ['GET'])
def volume():
    if request.method == 'GET':
        print >>sys.stderr, request.args.get("level")
        l = int(request.args.get("level"))
        if ((l >= 0) and (l <= 51)):
            subprocess.check_call(['amixer', 'cset', 'numid=1', ('%d%%' % l)])
        else:
            print >>sys.stderr, ("Bad volume %d\n" % l)

    return redirect("index", code=302)

@app.route('/radio',methods = ['GET'])
def radio():
    if request.method == 'GET':
        print >>sys.stderr, request.args.get("action")
        r = request.args.get("name")
        if (r == "stop"):
            subprocess.check_call(['/home/pi/audio.sh', 'stop'])
        else:
            subprocess.check_call(['/home/pi/audio.sh', 'radio', r])

    return redirect("index", code=302)


if __name__ == '__main__':
    jokes = [line.rstrip('\n') for line in open("/home/pi/jokes.txt")]
    numjokes = len(jokes)
    app.run(host='0.0.0.0', port=80)
