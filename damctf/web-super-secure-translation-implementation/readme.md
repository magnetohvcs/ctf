![img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/4.png)
</br>
tôi rất là vui vì đội solve bài này lượt thứ 6 là đội của tôi, đây là lần đầu trong một cuộc thi ctf mà tôi solve nhanh như vậy
![img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/5.png)

bài này tác giả có cho `super-secure-translation-implementation.zip` một file zip để tải về nhưng thật ra bên trong chẳng có gì ngoài tệp __Dockerfile__ giúp ta xác định được vị trí của flag
</br> đây là giao diện của website khi ta vào
![img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/6.png)
source code được hiển thị rõ
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
  Bằng cách chèn __/path__ thì ta có thể đọc bất kỳ file trong thư mục __/chal__ vì dấu `..` và `/` đã bị filter
  ```
from check import detect_remove_hacks
from filters import *
```
để ý đoạn này, tệp app.py có tham chiếu đến 2 file khác là __check.py__ và __filters.py__ vậy ta chỉ cần truy cập đến 
đường dẫn `https://super-secure-translation-implementation.chals.damctf.xyz/check.py` để đọc tệp __check.py__ 
![img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/7.png)
và đường dẫn `https://super-secure-translation-implementation.chals.damctf.xyz/filters.py` để đọc tệp __filters.py__
![img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/8.png)
sau khi đọc qua các tệp thì tóm tắt là tại path __/secure_translate__ chỉ cần chèn payload vào parameter __payload__ thì ta sẽ thấy web bị lỗi ssti nhưng chỉ có một vài  ký tự được cho phép còn lại đều bị chặn
```  allowlist = [
        "c", "{","}","d","6","l","(","b","o","r",")",'"',"1","4","+","h","u","-","*","e","|","'",
    ]
```

</br>
