from flask import Flask,request,redirect
import random
import sys
import os
import subprocess
import re
app = Flask(__name__)

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
'''<html>
<head><title>Matthew's Clock</title></head>
<body>
<table>
<tr>
<form action = "/post" method = "POST">
<td>
<input type = "submit" value = "Send Message:" />
</td>
<td>
<input type = "text" name = "msg" />
</td>
</form>
</tr>
<tr>
<form action = "/speak" method = "POST">
<td>
<input type = "submit" value = "Speak Message:" />
</td>
<td>
<input type = "text" name = "msg" />
</td>
</form>
</tr>
<tr>
<form action = "/joke" method = "POST">
<td>
<input type = "submit" value = "Tell me a joke" />
</td>
<td/>
</form>
</tr>
<tr>
<form action = "/jokeread" method = "POST">
<td>
<input type = "submit" value = "Read me a joke" />
</td>
<td/>
</form>
</tr>
</table>
<hr/>
<table border="1">
<tr>
<td width="80"><a href="/volume?level=0">Mute</a></td>
<td width="80"><a href="/volume?level=1">Lowest</a></td>
<td width="80"><a href="/volume?level=10">1</a></td>
<td width="80"><a href="/volume?level=20">2</a></td>
<td width="80"><a href="/volume?level=30">3</a></td>
<td width="80"><a href="/volume?level=40">4</a></td>
<td width="80"><a href="/volume?level=50">Max</a></td>
</tr>
<tr>
<td>Volume:<br/>''' + curvolume + '''</td>
<td><a href="/radio?name=stop">Stop Radio</a></td>
<td><a href="/radio?name=jackfm">Jack FM</a></td>
<td><a href="/radio?name=radio1">BBC Radio 1</a></td>
<td><a href="/radio?name=radio2">BBC Radio 2</a></td>
<td><a href="/radio?name=radio3">BBC Radio 3</a></td>
<td><a href="/radio?name=radio4">BBC Radio 4</a></td>
</tr>
</table>
<hr/>
<table border="1">
<tr>
<td><a href="/manage?action=restartclock">Restart Clock</a></td>
<td><a href="/manage?action=reboot">Reboot Clock</a></td>
<td><a href="/manage?action=shutdown">Shutdown Clock</a></td>
</tr>
<tr>
<td>Temperature: ''' + str(int(temp/1000)) + '''</td></tr>
</table>
</body>
</html>'''
)

@app.route('/post',methods = ['POST'])
def result():
    if request.method == 'POST':
        #print request.form['msg']
        with open(("/run/clockmsg/%d" % random.randint(1,99999999)), "w") as text_file:
            text_file.write(request.form['msg'])
    return redirect("/", code=302)

@app.route('/speak',methods = ['POST'])
def speak():
    if request.method == 'POST':
        #print request.form['msg']
        subprocess.check_call(['/home/pi/audio.sh', 'say', msg])
    return redirect("/", code=302)

@app.route('/joke',methods = ['POST','GET'])
def joke():
    joke = random.randint(1,numjokes)
    msg=jokes[joke]

    #print >> sys.stderr, ("Joke %d of %d: %s\n" % (joke,numjokes,msg))
    with open(("/run/clockmsg/%d" % random.randint(1,99999999)), "w") as text_file:
        text_file.write(msg)
    return redirect("/", code=302)

@app.route('/jokeread',methods = ['POST','GET'])
def jokeread():
    joke = random.randint(1,numjokes)
    msg=jokes[joke]

    #print >> sys.stderr, ("Joke %d of %d: %s\n" % (joke,numjokes,msg))
    subprocess.check_call(['/home/pi/audio.sh', 'say', msg])

    return redirect("/", code=302)

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

    return redirect("/", code=302)

@app.route('/volume',methods = ['GET'])
def volume():
    if request.method == 'GET':
        print >>sys.stderr, request.args.get("level")
        l = int(request.args.get("level"))
        if ((l >= 0) and (l <= 51)):
            subprocess.check_call(['amixer', 'cset', 'numid=1', ('%d%%' % l)])
        else:
            print >>sys.stderr, ("Bad volume %d\n" % l)

    return redirect("/", code=302)

@app.route('/radio',methods = ['GET'])
def radio():
    if request.method == 'GET':
        print >>sys.stderr, request.args.get("action")
        r = request.args.get("name")
        if (r == "stop"):
            subprocess.check_call(['/home/pi/audio.sh', 'stop'])
        else:
            subprocess.check_call(['/home/pi/audio.sh', 'radio', r])

    return redirect("/", code=302)


if __name__ == '__main__':
    jokes = [line.rstrip('\n') for line in open("/home/pi/jokes.txt")]
    numjokes = len(jokes)
    app.run(host='0.0.0.0', port=80)
