# Створення бази даних для тесту

import sqlite3

conn = sqlite3.connect("project13.db")
curs = conn.cursor()
# створення таблиці робітнків
curs.execute("""CREATE TABLE workers(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
month_salary INTEGER,
department_id INTEGER,
job_id INTEGER)""")
conn.commit()
# створення таблиці відділів
curs.execute("""CREATE TABLE departments(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
description TEXT,
amount_of_workers INTEGER)""")
conn.commit()
# створення таблиці посад
curs.execute("""CREATE TABLE jobs(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
description TEXT,
salary INTEGER)""")
conn.commit()
# заповнення таблиць
for i in range(3):
    curs.execute("""INSERT INTO departments VALUES (?, ?, ?, ?)""", (i+1, f"department{i+1}", "Doing stuff", 2))
conn.commit()  # Заповнення відділів
curs.execute("""INSERT INTO jobs VALUES (?, ?, ?, ?)""", (1, f"job{1}", "Doing stuff", 12000))
conn.commit()
curs.execute("""INSERT INTO jobs VALUES (?, ?, ?, ?)""", (2, f"job{2}", "Doing stuff", 10000))
conn.commit()
for i in range(6):  # Заповнення працівників
    curs.execute("""INSERT INTO workers VALUES (?, ?, ?, ?, ?)""", (i+1, f"Petrovich{i + 1}", (i+5)*1000,
                                                                    1 + (i//2), 1 + (i//3)))
conn.commit()
