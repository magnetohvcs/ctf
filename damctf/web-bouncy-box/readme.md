![Image](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/1.png)
</br>
Tôi phát hiện trang web này có chức năng đăng nhập
![Img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/2.png)
Ở form đăng nhập này bị lỗi SQL injection, với payload `trung' or '1'='1'-- -`  nhập vào ô username, tôi dễ dàng vượt qua cơ chế xác thực và xuất hiện nút button `Free flag`
khi ấn vào thì xuất hiện form đăng nhập lần nữa, có vẻ form này không bị lỗi SQL injection, tôi nghĩ chúng ta sẽ lợi form đăng nhập thứ nhất để dò tìm username password để đăng nhập
vào form đăng nhập thứ 2
![Img](https://github.com/magnetohvcs/ctf/blob/main/damctf/image/3.png)
