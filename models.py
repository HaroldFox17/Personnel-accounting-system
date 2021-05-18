# Клас для роботи з базою даних

import sqlite3


class DBHandler:
    def __init__(self):  # задаємо БД
        self.db = "project13.db"

    def add_worker(self, name, month_sal, dep_id, job_id):  # Додати робітника
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""SELECT * FROM departments WHERE id=?""", (dep_id,))
        res1 = curs.fetchone()
        curs.execute("""SELECT * FROM jobs WHERE id=?""", (job_id,))
        res2 = curs.fetchone()
        if res1 and res2:
            curs.execute("""INSERT INTO workers(name, month_salary, department_id, job_id) VALUES (?, ?, ?, ?)""",
                         (name, month_sal, dep_id, job_id))
            conn.commit()
            curs.execute("""SELECT amount_of_workers FROM departments WHERE id=?""", (dep_id,))
            red = curs.fetchone()
            red = red[0]
            curs.execute("""UPDATE departments SET amount_of_workers=? WHERE id=?""", (red+1, dep_id))
            conn.commit()
            conn.close()
            return "Ok"
        else:
            conn.close()
            return "Помилка"

    def delete_worker(self, idw):  # Видалити робітника
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""SELECT * FROM workers WHERE id=?""", (idw,))
        res = curs.fetchone()
        if res:
            curs.execute("""DELETE FROM workers WHERE id=?""", (idw,))
            conn.commit()
            curs.execute("""SELECT amount_of_workers FROM departments WHERE id=?""", (res[3],))
            red = curs.fetchone()
            red = red[0]
            curs.execute("""UPDATE departments SET amount_of_workers=? WHERE id=?""", (red - 1, res[3]))
            conn.commit()
            conn.close()
            return "Ok"
        else:
            conn.close()
            return "Такого id не існує"

    def move_worker(self, idw, month_sal, dep_id, job_id):  # Перевести робітника
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""SELECT * FROM workers WHERE id=?""", (idw,))
        res = curs.fetchone()  # вся інформація
        curs.execute("""SELECT id FROM departments""")
        res_c = curs.fetchall()
        res_c = [i[0] for i in res_c]
        if dep_id not in res_c:
            conn.close()
            return "Неможливо перевести в неіснуючий відділ"
        curs.execute("""SELECT id FROM jobs""")
        res_d = curs.fetchall()
        res_d = [i[0] for i in res_d]
        if job_id not in res_d:
            conn.close()
            return "Неможливо перевести на неіснуючу посаду"
        if res:  # якщо він є
            curs.execute("""SELECT amount_of_workers FROM departments WHERE id=?""", (dep_id,))
            res_a = curs.fetchone()
            res0 = res_a[0]  # скільки працюють там де він працюватиме
            curs.execute("""SELECT amount_of_workers FROM departments WHERE id=?""", (res[3],))
            res_b = curs.fetchone()
            res1 = res_b[0]  # скільки працюють там де він працює
            curs.execute("""UPDATE departments SET amount_of_workers=? WHERE id=?""", (res1-1, res[3]))
            conn.commit()  # зменшуєм кількість робітників там де він працює на 1
            curs.execute("""UPDATE departments SET amount_of_workers=? WHERE id=?""", (res0+1, dep_id))
            conn.commit()  # збільшуємєм кількість робітників там де він працюватиме на 1
            curs.execute("""UPDATE workers SET month_salary=?, department_id=?, job_id=? WHERE id=?""",
                         (month_sal, dep_id, job_id, idw))  # міняєо інформацію про самого робітника
            conn.commit()
            conn.close()
            return "Ok"
        else:
            conn.close()
            return "Такий робітник відсутній"

    def redact_worker(self, idw, name, month_sal, dep_id, job_id):  # Редагувати робітника
        mov = self.move_worker(idw, month_sal, dep_id, job_id)
        if mov == "Ok":
            conn = sqlite3.connect(self.db)
            curs = conn.cursor()
            curs.execute("""UPDATE workers SET name=? WHERE id=?""", (name, idw))
            conn.commit()
            conn.close()
            return "Ok"
        elif mov == "Такий робітник відсутній":
            return mov
        else:
            return "Неможливо відредагувати інформацію про робітника"

    def delete_department(self, idd):  # Видалити відділ
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""SELECT * FROM departments WHERE id=?""", (idd,))
        res = curs.fetchone()
        if res:
            curs.execute("""DELETE FROM departments WHERE id=?""", (idd,))
            conn.commit()
            conn.close()
            return "Ok"
        else:
            conn.close()
            return "Такого id не існує"

    def add_department(self, name, descr, amount_w):  # Додати відділ
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""INSERT INTO departments(name, description, amount_of_workers) VALUES (?, ?, ?)""",
                     (name, descr, amount_w))
        conn.commit()
        conn.close()
        return "Ok"

    def redact_department(self, idd, name, descr, amount_w):  # Редагувати відділ
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""SELECT * FROM departments WHERE id=?""", (idd,))
        res = curs.fetchone()
        if res:
            curs.execute("""UPDATE departments SET name=?, description=?, amount_of_workers=? WHERE id=?""",
                         (name, descr, amount_w, idd))
            conn.commit()
            conn.close()
            return "Ok"
        else:
            conn.close()
            return "Таке id не існує"

    def add_job(self, name, descr, sal):  # Додати посаду
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""INSERT INTO jobs(name, description, salary) VALUES (?, ?, ?)""", (name, descr, sal))
        conn.commit()
        conn.close()
        return "Ok"

    def delete_job(self, idj):  # Видалити відділ
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""SELECT * FROM jobs WHERE id=?""", (idj,))
        res = curs.fetchone()
        if res:
            curs.execute("""DELETE FROM jobs WHERE id=?""", (idj,))
            conn.commit()
            conn.close()
            return "Ok"
        else:
            conn.close()
            return "Такого id не існує"

    def redact_job(self, idj, name, descr, sal):  # Редагувати відділ
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute("""SELECT * FROM jobs WHERE id=?""", (idj,))
        res = curs.fetchone()
        if res:
            curs.execute("""UPDATE jobs SET name=?, description=?, salary=? WHERE id=?""",
                         (name, descr, sal, idj))
            conn.commit()
            conn.close()
            return "Ok"
        else:
            conn.close()
            return "Таке id не існує"
