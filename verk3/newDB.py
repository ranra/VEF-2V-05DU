import sqlite3

with sqlite3.connect("test.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
userID integer primary key,
userName varchar(2) not null,
firstName varchar (20) not null,
lastName varchar (20) not null,
password varchar (20) not null
);

''')

cursor.execute('''
INSERT INTO users(userName, firstName, lastName, password)
VALUES("user1", "arnar", "orri", 1234)
''')
db.commit()
cursor.execute("SELECT * FROM users")
