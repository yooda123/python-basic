import sqlite3


con = sqlite3.connect("sample.db")
cursor = con.cursor()


# for row in cursor.execute("SELECT * FROM user"):
#     print(row)

cursor.execute("SELECT * FROM user")
# print(next(cursor))
# print(next(cursor))

# .fetchall(): 現在のcursor以下すべてを返す
# print(cursor.fetchall())

# .fetchone(): 現在のcursorのレコードをタプルで返す
# print(cursor.fetchone())
