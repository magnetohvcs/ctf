
![Alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/img/Untitled5.png)
<br />
ở hàm __getPost__ trong tệp __database.js__ bị  sqli
<br />
![Alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/img/Untitled1.png)
<br />
ở đường dẫn __/posts/:id__ dùng hàm getPost này
<br />
![Alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/img/Untitled2.png)
<br />
flag được để trong tables __users__ ở dòng password có username là __flagbearer__
<br />
![Alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/img/Untitled.png)
<br />
ta chỉ cần truy cập vào đường dẫn này là có thể lấy được flag __http://157.245.32.65:32516/posts/0%27%20union%20select%201%2C2%2C3%2Cpassword%20from%20users%20where%20username%3D%27flagbearer__
<br />
[source code của bài này](https://github.com/magnetohvcs/ctf/raw/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/web_tour_blog.zip)
