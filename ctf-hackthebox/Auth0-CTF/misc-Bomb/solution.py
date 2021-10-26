host = '165.22.121.146'
port = 31328

import socket

s = socket.socket()
s.connect((host,port))

while True:
    res = s.recv(1000).decode('UTF-8')
    print(res)
    if 'HTB{' in res: 
        break
    try:
        res = res.split('\n\n')[1][:-3]
        s.send(bytes(str(f'{int(eval(res))}\n').encode()))
    except:
        break
  
