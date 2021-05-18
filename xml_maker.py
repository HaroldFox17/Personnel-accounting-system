# Створення наказів в XML

import xml.dom.minidom as md
import os
import sqlite3


# функція створення наказу про прийняття на роботу
def xml_hire(name, month_salary, department_id, job_id):
    conn = sqlite3.connect('project13.db')
    curs = conn.cursor()
    curs.execute("""SELECT COUNT(*) FROM workers""")
    res = curs.fetchone()
    curs.execute("""SELECT * FROM departments WHERE id=?""", (department_id,))
    res1 = curs.fetchone()
    curs.execute("""SELECT * FROM jobs WHERE id=?""", (job_id,))
    res2 = curs.fetchone()
    if res2 and res1:  # перевірка чи є робітник з таким id чи є такий відділ і чи є така посада
        st = "Прийняття на роботу"
        root = md.Document()
        xm = root.createElement(st)
        root.appendChild(xm)
        idt = root.createElement("id")
        text = root.createTextNode(str(res[0]+1))
        xm.appendChild(idt)
        idt.appendChild(text)
        namet = root.createElement("name")
        text0 = root.createTextNode(name)
        xm.appendChild(namet)
        namet.appendChild(text0)
        salt = root.createElement("salary")
        text1 = root.createTextNode(str(month_salary))
        xm.appendChild(salt)
        salt.appendChild(text1)
        dept = root.createElement("department_id")
        text2 = root.createTextNode(str(department_id))
        xm.appendChild(dept)
        dept.appendChild(text2)
        jobt = root.createElement("job_id")
        text3 = root.createTextNode(str(job_id))
        xm.appendChild(jobt)
        jobt.appendChild(text3)
        xml_str = root.toprettyxml(indent="\t")
        conn.close()
        path = os.path.join(os.getcwd(), "xml-nakazy")
        try:
            os.makedirs(path)
        except Exception:
            pass
        filepath = os.path.join(path, "hiring{}.xml".format(str(res[0]+1)+name))
        with open(filepath, "w") as f:
            f.write(xml_str)
        return "Ok"
    elif not res1:
        conn.close()
        return "Такого відділу не існує"
    elif not res2:
        conn.close()
        return "Такої посади не існує"


# функція створення наказу про звільнення з роботи
def xml_fire(idw):
    conn = sqlite3.connect('project13.db')
    curs = conn.cursor()
    curs.execute("""SELECT * FROM workers WHERE id=?""", (idw,))
    res = curs.fetchone()
    if res:  # перевірка чи є робітнк з таким id
        st = "Звільнення"
        root = md.Document()
        xm = root.createElement(st)
        root.appendChild(xm)
        idt = root.createElement("id")
        text = root.createTextNode(str(idw))
        xm.appendChild(idt)
        idt.appendChild(text)
        namet = root.createElement("name")
        text0 = root.createTextNode(res[1])
        xm.appendChild(namet)
        namet.appendChild(text0)
        salt = root.createElement("salary")
        text1 = root.createTextNode(str(res[2]))
        xm.appendChild(salt)
        salt.appendChild(text1)
        dept = root.createElement("department_id")
        text2 = root.createTextNode(str(res[3]))
        xm.appendChild(dept)
        dept.appendChild(text2)
        jobt = root.createElement("job_id")
        text3 = root.createTextNode(str(res[4]))
        xm.appendChild(jobt)
        jobt.appendChild(text3)
        xml_str = root.toprettyxml(indent="\t")
        conn.close()
        path = os.path.join(os.getcwd(), "xml-nakazy")
        try:
            os.makedirs(path)
        except Exception:
            pass
        filepath = os.path.join(path, "firing{}.xml".format(str(idw)+res[1]))
        with open(filepath, "w") as f:
            f.write(xml_str)
        return "Ok"
    else:
        conn.close()
        return "Таке id не існує"


# функція створення наказу про переведення
def xml_move(idw, month_salary, department_id, job_id):
    conn = sqlite3.connect('project13.db')
    curs = conn.cursor()
    curs.execute("""SELECT * FROM workers WHERE id=?""", (idw,))
    res = curs.fetchone()
    curs.execute("""SELECT * FROM departments WHERE id=?""", (department_id,))
    res1 = curs.fetchone()
    curs.execute("""SELECT * FROM jobs WHERE id=?""", (job_id,))
    res2 = curs.fetchone()
    if res and res1 and res2:  # перевірка чи є робітнк з таким id чи є такий відділ і чи є така посада
        st = "Переведення"
        root = md.Document()
        xm = root.createElement(st)
        root.appendChild(xm)
        idt = root.createElement("id")
        text = root.createTextNode(str(idw))
        xm.appendChild(idt)
        idt.appendChild(text)
        namet = root.createElement("name")
        text0 = root.createTextNode(res[1])
        xm.appendChild(namet)
        namet.appendChild(text0)
        salt = root.createElement("salary_new")
        text1 = root.createTextNode(str(month_salary))
        xm.appendChild(salt)
        salt.appendChild(text1)
        salto = root.createElement("salary_old")
        text1o = root.createTextNode(str(res[2]))
        xm.appendChild(salto)
        salto.appendChild(text1o)
        dept = root.createElement("department_to_id")
        text2 = root.createTextNode(str(department_id))
        xm.appendChild(dept)
        dept.appendChild(text2)
        depto = root.createElement("department_from_id")
        texto = root.createTextNode(str(res[3]))
        xm.appendChild(depto)
        depto.appendChild(texto)
        jobt = root.createElement("job_to_id")
        text3 = root.createTextNode(str(job_id))
        xm.appendChild(jobt)
        jobt.appendChild(text3)
        jobto = root.createElement("job_from_id")
        text3o = root.createTextNode(str(res[4]))
        xm.appendChild(jobto)
        jobto.appendChild(text3o)
        xml_str = root.toprettyxml(indent="\t")
        conn.close()
        path = os.path.join(os.getcwd(), "xml-nakazy")
        try:
            os.makedirs(path)
        except Exception:
            pass
        filepath = os.path.join(path, "moving{}.xml".format(str(idw)+res[1]))
        with open(filepath, "w") as f:
            f.write(xml_str)
        return "Ok"
    elif not res:
        conn.close()
        return "Таке id не існує"
    elif not res1:
        conn.close()
        return "Такого відділу не існує"
    elif not res2:
        conn.close()
        return "Такої посади не існує"
