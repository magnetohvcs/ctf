# __Slippy__
</br> [source](https://github.com/magnetohvcs/CTF/raw/main/ctf-hackthebox/Uni%20CTF%202021%20Quals/src/web_slippy.zip)

__tóm tắt__ : cố gắng upload file tar.gz để lấy flag, ta không thể dùng symlinks để cố gắng truy cập file flag mà ta sẽ dùng [công cụ này](https://github.com/ptoomey3/evilarc). Sau đó ta chèn đoạn như sau `return [os.popen('ls -al && cat flag').read()]` vào hàm `extract_from_archive` trong file __util.py__ giống như trong hình ![hinh](https://github.com/magnetohvcs/CTF/blob/main/ctf-hackthebox/Uni%20CTF%202021%20Quals/src/2.png)
