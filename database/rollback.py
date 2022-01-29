import sqlite3
from venv import create


con = sqlite3.connect("sample.db")
cursor = con.cursor()
create_history_table_query = """
CREATE TABLE IF NOT EXISTS history (
    name TEXT,
    age INTEGER
)
"""
cursor.execute(create_history_table_query)

target_name = input("whose 'age' do you want to update?: ")
new_age = input("Tell me new age: ")

print(target_name, new_age)


update_query = "UPDATE user SET age = ? WHERE name = ?"
insert_history_query = "INSERT INTO history VALUES (?, ?)"

try:
    cursor.execute(insert_history_query, (target_name, new_age))
    cursor.execute(update_query, (new_age, target_name))
except sqlite3.Error:
    print("sqlite3 error ocurred.")
    con.rollback()
else:
    con.commit()
