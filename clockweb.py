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
#key="96934a5c320e505396eb946b34e6f720"
key="802bcbc0941f44d4b538935923afbfca"
#latitude="51.770963"
#longditude="-1.072445"
latitude="51.74641015523559"
longditude="-1.1340588461934575"



@app.route('/')
@app.route('/index')
def page():
    soundfiles=""
    for s in sorted(os.listdir(sys.path[0]+'/sounds')):
        soundfiles = soundfiles + '<option value="'+s+'">'+s.replace(".wav","").replace("-"," ")+'</option>'

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

<tr>
<td><select name="sound">'''+soundfiles+'''</select></td>
<td><input type="submit" name="action" value="Play Sound" /></td>
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
<tr>
<td width="80"></td>
<td><a href="radio?name=rne1">RNE 1</a></td>
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
<td>Light: ''' + format(readLight(),'.2f') + '''lx</td>
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
    #url=("https://api.darksky.net/forecast/%s/%s,%s?lang=en&units=uk2" % (key,latitude,longditude))
    url=("http://api.weatherbit.io/v2.0/forecast/daily?lat=%s&lon=%s&key=%s&days=2" % (latitude,longditude,key))
    r=urllib.urlopen(url)
    d=json.loads(r.read())
    day=""
    if (when == "tomorrow"):
        n=1
        day="Tomorrows"
    elif (when == "today"):
        n=0
        day="Current"

    if (day != ""):
        summary=d["data"][n]["weather"]["description"]
        temperature=d["data"][n]["max_temp"]
        return ("%s weather:    %s    Temperature: %d degrees celsius" %(day,summary,temperature))

    return ""

def playsound(sound):
    subprocess.call(["aplay",sys.path[0]+"/sounds/"+sound])

@app.route('/post',methods = ['POST'])
def result():
    #print >> sys.stderr, ("%s\n" % request.form['action'])
    #print >> sys.stderr, ("%s\n" % request.form['msg'])
    if (request.method != 'POST'):
        return redirect("index", code=302)

    lang=request.form['lang']
    action=request.form['action']

    if (action == 'Play Sound'):
        playsound(request.form['sound'])
        return redirect("index", code=302)

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
            subprocess.check_call(['/home/pi/audio.sh', 'nokill', 'say', msg, lang])

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

######################################
# taken from https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bh1750.py
import smbus
import time

# Define some constants from the datasheet

DEVICE     = 0x23 # Default device I2C address

POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

# Start measurement at 4lx resolution. Time typically 16ms.
CONTINUOUS_LOW_RES_MODE = 0x13
# Start measurement at 1lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
# Start measurement at 0.5lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20
# Start measurement at 0.5lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_2 = 0x21
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_LOW_RES_MODE = 0x23

#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number. Optional parameter 'decimals'
  # will round to specified number of decimal places.
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr=DEVICE):
  # Read data from I2C interface
  try:
      data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_2)
  except:
      return 0
  return convertToNumber(data)


######################################

if __name__ == '__main__':
    jokes = [line.rstrip('\n') for line in open("/home/pi/jokes.txt")]
    numjokes = len(jokes)
    app.run(host='0.0.0.0', port=80)
