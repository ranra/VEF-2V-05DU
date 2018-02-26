import sqlite3

def login():
    while True:

        username = input("username: ")
        password = input("password: ")
        with sqlite3.connect("test.db")as db:
            cursor = db.cursor()

        find_user = ("SELECT * FROM users WHERE userName = ? AND password = ?")
        cursor.execute(find_user, [(username), (password)])
        results = cursor.fetchall()

        if results:
            for x in results:
                print("welcome " + x[2])
            break
        else:
            print("not recognised")
            again = input("try again (y/n)")
            if again.lower() == "n":
                break



def create_user():
    found = False
    pass_check = False
    while found != True:
        username = input("username: ")
        with sqlite3.connect("test.db")as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM users WHERE userName = ?")
        cursor.execute(find_user, [(username)])
        if cursor.fetchall():
            print("username taken")

        else:
            found = True
    firstname = input("firstname: ")
    lastname = input("lastname: ")
    while pass_check != True:

        password = input("password: ")
        password1 = input("confirm password: ")
        if password == password1:
            print("confirmed")
            pass_check = True
        else:
            print("passwords dont match")

    add_user = ("INSERT INTO users(userName, firstName, lastName, password) VALUES (?, ?, ?, ?)")
    cursor.execute(add_user,[(username),(firstname), (lastname), (password)])


create_user()