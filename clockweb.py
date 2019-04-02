from flask import Flask,request,redirect
import random
import sys
import os
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def page():
    return (
'''<html>
<head><title>Matthew's Clock</title></head>
<body>
<form action = "/post" method = "POST">
<p>
<input type = "submit" value = "Send Message:" />
<input type = "text" name = "msg" />
</p>
</form>
<form action = "/joke" method = "POST">
<p><input type = "submit" value = "Tell me a joke" /></p>
</form>
<hr/>
<table border="1">
<tr>
<td><a href="/manage?action=restartclock">Restart Clock</a></td>
<td><a href="/manage?action=reboot">Reboot Clock</a></td>
<td><a href="/manage?action=shutdown">Shutdown Clock</a></td>
</tr>
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

@app.route('/joke',methods = ['POST'])
def joke():
    if request.method == 'POST':
        joke = random.randint(1,numjokes)
        msg=jokes[joke]

        #print >> sys.stderr, ("Joke %d of %d: %s\n" % (joke,numjokes,msg))
        with open(("/run/clockmsg/%d" % random.randint(1,99999999)), "w") as text_file:
            text_file.write(msg)
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


if __name__ == '__main__':
    jokes = [line.rstrip('\n') for line in open("/home/pi/jokes.txt")]
    numjokes = len(jokes)
    app.run(host='0.0.0.0', port=80)
