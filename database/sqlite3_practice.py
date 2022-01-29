from distutils.sysconfig import customize_compiler
import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

create_user_table_query = """
CREATE TABLE IF NOT EXISTS user (
    userid INTEGER PRIMARY KEY NOT NULL,
    name TEXT DEFAULT 'anonymous',
    email TEXT NOT NULL,
    age INTEGER CHECK(age > 0)
)
"""
cursor.execute(create_user_table_query)


insert_user_query = """
DELETE FROM user;
INSERT INTO user VALUES (1, 'John', 'john@test.com', 30);
INSERT INTO user VALUES (2, 'Emily', 'emily@test.com', 28);
INSERT INTO user VALUES (3, 'Taro', 'taro@test.com', 13);
"""
# cursor.execute(insert_user_query)
cursor.executescript(insert_user_query)  # commitなしでOK

con.commit()
