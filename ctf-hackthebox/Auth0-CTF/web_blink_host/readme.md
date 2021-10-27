![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_blink_host/src/Untitled.png)
ta tiến hành đọc code và thấy rằng ở tệp __challenge/views/settings.html__ có flag nằm ở thẻ input
![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_blink_host/src/4.png)
<br />
tệp challenge/routes/index.js có đoạn code mô tả
chỉ cần truy cập vào đường dẫn __/settings__ thì sẽ nhận response là __settings.html__ nhưng mà đường dẫn này chỉ có ip localhost mới được truy cập.
![](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_blink_host/src/1.png)

ở đoạn mã này có mô tả, ta chỉ cần gửi 1 gói __json gồm có name, email, website, message__ thì sẽ lưu vào database
![](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_blink_host/src/3.png)
và sau đó con bot sẽ tiến hành truy cập đến đường dẫn __/tickets__
![](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_blink_host/src/%60.png)

đường __/tickets__ cũng chỉ cho ip localhost mới được truy cập.
![](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_blink_host/src/2.png)
