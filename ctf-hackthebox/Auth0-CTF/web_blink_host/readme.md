![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_blink_host/src/Untitled.png)
ta tiến hành đọc code và thấy rằng ở tệp __challenge/views/settings.html__ có flag nằm ở thẻ input
![alt](https://github.com/magnetohvcs/ctf/blob/main/ctf-hackthebox/Auth0-CTF/web_blink_host/src/4.png)

trong tệp challenge/routes/index.js
``` router.get('/settings', (req, res) => {
	if(req.ip != '127.0.0.1') return res.redirect('/');
	return res.render('settings.html');
});
```
đường dẫn __/settings__ chỉ cho phép ip localhost mới được truy cập
<br />
``` router.get('/tickets', async (req, res, next) => {
	if(req.ip != '127.0.0.1') return res.redirect('/');

	return db.getTickets()
		.then(allTickets => {
			res.render('ticket.html', { allTickets });
		})
		.catch(() => res.status(500).send(response('Something went wrong!')));
}); 
``` 
đường __/tickets__ cũng chỉ cho ip localhost mới được truy cập.
