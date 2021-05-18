# HTML сторінки що використовуються в проєкті
# Головна HTML сторінка
HTML_MAIN_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Main Page</title>
    <style>
      input{width:400px;
      height:40px;
      border-radius:10px;
      text-align:center}
    </style>
</head>
<body bgcolor=009933>
    <h3 style="color:White">Оберіть можливий тип дій</h3>
    <hr>
    <form method=POST action="to_workers">
        <input type=submit value="Перейти до дій з робітниками">
    </form>
    <hr>
    <form method=POST action="to_departments">
        <input type=submit value="Перейти до дій з відділами">
    </form>
    <hr>
    <form method=POST action="to_jobs">
        <input type=submit value="Перейти до дій з посадами">
    </form>
    <hr>
</body>
</html>"""

# HTML сторінка дій з працівниками
HTML_WORKERS_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Workers actions</title>
    <style>
      input{width:400px;
      height: 40px;
      border-radius:10px;
      text-align:center}
    </style>
</head>
<body bgcolor=228B22>
    <h3 style= "color:White">Оберіть дію</h3>
    <hr>
    <form method=POST action="firing">
        <input type="submit" value="Звільнити">
    </form>
    <hr>
    <form method=POST action="moving">
        <input type="submit" value="Перевести">
    </form>
    <hr>
    <form method=POST action="hiring">
        <input type="submit" value="Взяти на роботу">
    </form>
    <hr>
    <form method=POST action="redacting_worker">
        <input type="submit" value="Редагувати особисту інформацію">
    </form>
</body>
</html>"""

# HTML сторінка дій з відділами
HTML_DEPARTMENTS_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Departments actions</title>
    <style>
      input{width:400px;
      height: 40px;
      border-radius:10px;
      text-align:center}
    </style>
</head>
<body bgcolor=228B22>
    <h3 style="color:White">Оберіть дію</h3>
    <form method=POST action="adding_department">
        <input type="submit" value="Додати відділ">
    </form>
    <hr>
    <form method=POST action="redacting_department">
        <input type="submit" value="Змінити інформацію про відділ">
    </form>
    <hr>
    <form method=POST action="deleting_department">
        <input type="submit" value="Видалити відділ">
    </form>
</body>
</html>"""

# HTML сторінка дій з посадами
HTML_JOBS_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jobs actions</title>
    <style>
      input{width:400px;
      height: 40px;
      border-radius:10px;
      text-align:center}
    </style>
</head>
<body bgcolor=228B22>
    <h3 style="color:White">Оберіть дію</h3>
    <form method=POST action="adding_job">
        <input type="submit" value="Додати посаду">
    </form>
    <hr>
    <form method=POST action="redacting_job">
        <input type="submit" value="Змінити інформацію про посаду">
    </form>
    <hr>
    <form method=POST action="deleting_job">
        <input type="submit" value="Видалити посаду">
    </form>
</body>
</html>"""

# HTML сторінка заповнення повної форми для робітника
HTML_FULL_WORKER_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jobs actions</title>
</head>
<body bgcolor=008000 text="white">
    <form method=POST action="{}_worker">
        {}
        {}
        Введіть заробітну платню за місяць(в грн):<br><input type="text" name="salary_enter" style ="width:400px">
        <br>
        Введіть id департаменту{}:<br><input type="text" name="dep_id_enter" style ="width:400px">
        <br>
        Введіть id посади:<br><input type="text" name="job_id_enter" style ="width:400px">
        <br><br>
        <input type="submit" style = "width:50px" value="Ok">
    </form>
</body>
</html>"""

# HTML сторінка заповнення короткої форми для робітників
HTML_SHORT_WORKER_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jobs actions</title>
</head>
<body bgcolor=134D44 text="white">
    <form method=POST action="fire_worker">
        Введіть id:<br><input type="text" name="id_enter" style ="width:400px">
        <br>
        <input type="submit" value="Ok">
    </form>
</body>
</html>"""

# HTML сторінка заповнення повної форми для департамента
HTML_FULL_DEP_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jobs actions</title>
</head>
<body bgcolor=008000 text="white">
    <form method=POST action="{}_department">
        {}
        Введіть назву:<br><input type="text" name="name_enter" style ="width:400px">
        <br>
        Введіть опис:<br><input type="text" name="descr_enter" style ="width:400px">
        <br>
        Введіть кількість робітників:<br><input type="text" name="workers_enter" style ="width:400px">
        <br><br>
        <input type="submit" style = "width:50px" value="Ok">
    </form>
</body>
</html>"""

# HTML сторінка заповнення короткої форми для департамента
HTML_SHORT_DEP_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jobs actions</title>
</head>
<body bgcolor=134D44 text="white">
    <form method=POST action="delete_department">
        Введіть id:<br><input type="text" name="id_enter" style ="width:400px">
        <br>
        <input type="submit" value="Ok">
    </form>
</body>
</html>"""

# HTML сторінка заповнення повної форми для посади
HTML_FULL_JOB_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jobs actions</title>
</head>
<body bgcolor=008000 text="white">
    <form method=POST action="{}_job">
        {}
        Введіть назву:<br><input type="text" name="name_enter" style ="width:400px">
        <br>
        Введіть опис:<br><input type="text" name="descr_enter" style ="width:400px">
        <br>
        Введіть ставку по посаді:<br><input type="text" name="salary_enter" style ="width:400px">
        <br><br>
        <input type="submit" style = "width:50px" value="Ok">
    </form>
</body>
</html>"""

# HTML сторінка заповнення короткої форми для посади
HTML_SHORT_JOB_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jobs actions</title>
</head>
<body bgcolor=134D44 text="white">
    <form method=POST action="delete_job">
        Введіть id:<br><input type="text" name="id_enter" style ="width:400px">
        <br>
        <input type="submit" value="Ok">
    </form>
</body>
</html>"""

# HTML сторінка результату дії
HTML_OUTPUT_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jobs actions</title>
</head>
<body bgcolor=234E54 text="white">
    <form method=POST action="result">
        <h3>{}<h3>
        <input type="submit" value="Ok">
    </form>
</body>
</html>
"""

# HTML сторінка, яка треба
STUFF = """Введіть ім'я:<br><input type="text" name="name_enter" style ="width:400px">
        <br>"""

STUFF1 = """Введіть id:<br><input type="text" name="id_enter" style ="width:400px">
        <br>"""
