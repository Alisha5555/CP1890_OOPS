import sqlite3

conn = sqlite3.connect("class_example2.sqlite")

c = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        marks INTEGER);"""
print(query)
c.execute(query)
print("Table created successfully")


c.execute("""INSERT INTO students values (2, 'Alisha', 30, 100)""")
conn.commit()
conn.close()