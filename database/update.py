import sqlite3


con = sqlite3.connect("sample.db")
cursor = con.cursor()

target_name = input("whose 'age' do you want to update?: ")
new_age = input("Tell me new age: ")

print(target_name, new_age)

# SQLインジェクションの脆弱性あり
# update_query = f"UPDATE user SET age = {new_age} WHERE name = '{target_name}'"
# cursor.executescript(update_query)

# UPDATE user SET age = ' 33';DELETE FROM user; select * from user

update_query = "UPDATE user SET age = ? WHERE name = ?"
cursor.execute(update_query, (new_age, target_name))
con.commit()
