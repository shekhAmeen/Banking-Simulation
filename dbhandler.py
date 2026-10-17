import sqlite3

conobj = sqlite3.connect('bank.sqlite')
curobj = conobj.cursor()

query = '''create table if not exists users(
acn integer primary key autoincrement,
name text,
password text,
email text,
mob text,
adhar text,
age int,
bal float,
gender text,
opendate text
)
'''

curobj.execute(query)
conobj.commit()
conobj.close()
print("Table managed")