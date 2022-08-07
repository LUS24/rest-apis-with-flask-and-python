import sqlite3 

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "User1", "Password1")
inser_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(inser_query, user)
users = [
    (2, "User2", "Password2"),
    (3, "User3", "Password3"),
]
cursor.executemany(inser_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
