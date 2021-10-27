
![Alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/img/Untitled5.png)
<space><space>
ở hàm __getPost__ trong tệp __database.js__ bị lỗi sqli
  <space><space>
![Alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/img/Untitled1.png)
<space><space>
ở đường dẫn __/posts/:id__ dùng hàm getPost này
  <space><space>
![Alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/img/Untitled2.png)
  <space><space>
flag được để trong tables __users__ ở dòng password có username là __flagholder__
    <space><space>
![Alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/img/Untitled.png)
    <space><space>
ta chỉ cần truy cập vào đường dẫn này là có thể lấy được flag __http://157.245.32.65:32516/posts/0' union select 1,2,3,password from users where username='flagbearer__
<space><space>
[source code của bài này](https://github.com/magnetohvcs/ctf/raw/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/web_tour_blog.zip)
