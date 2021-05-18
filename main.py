# Основна програма

import cgi
from html_pages import *
from xml_maker import *
from models import *


def application(environ, start_response):
    db = DBHandler()
    body = HTML_MAIN_PAGE
    if environ.get('PATH_INFO', '').lstrip('/') == '' or\
            environ.get('PATH_INFO', '').lstrip('/') == 'result':  # перейти на головну
        body = HTML_MAIN_PAGE
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'to_workers':  # перейти до робітників
        body = HTML_WORKERS_PAGE
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'to_departments':  # перейти до підрозділів
        body = HTML_DEPARTMENTS_PAGE
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'to_jobs':  # перейти до посад
        body = HTML_JOBS_PAGE
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'moving':  # перейти до форми перевести
        body = HTML_FULL_WORKER_PAGE.format("move", STUFF1, "", ", до якого перевести")
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'hiring':  # перейти до форми найняти
        body = HTML_FULL_WORKER_PAGE.format("hire", "", STUFF, ", до якого прийняти")
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'redacting_worker':  # перейти до форми редагувати
        body = HTML_FULL_WORKER_PAGE.format("redact", STUFF1, STUFF, ", в якому тепер працює робітник")
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'firing':  # перейти до форми звільнити
        body = HTML_SHORT_WORKER_PAGE
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'fire_worker':  # перейти від звільнення до результату
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if 'id_enter' in form:
            id_enter = int(form['id_enter'].value)
            s = xml_fire(id_enter)
            db.delete_worker(id_enter)
            body = HTML_OUTPUT_PAGE.format(s)
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'hire_worker':  # перейти від прийнття до результату
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if "name_enter" in form and "salary_enter" in form and "dep_id_enter" in form\
                and "job_id_enter" in form:
            name_enter = str(form['name_enter'].value)
            sal_enter = int(form['salary_enter'].value)
            dep_id_enter = int(form['dep_id_enter'].value)
            job_id_enter = int(form['job_id_enter'].value)
            s = xml_hire(name_enter, sal_enter, dep_id_enter, job_id_enter)
            db.add_worker(name_enter, sal_enter, dep_id_enter, job_id_enter)
            body = HTML_OUTPUT_PAGE.format(s)
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'redact_worker':  # перейти від редагування до результату
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if "id_enter" in form and "name_enter" in form and "salary_enter" in form and "dep_id_enter" in form \
                and "job_id_enter" in form:
            id_enter = int(form['id_enter'].value)
            name_enter = str(form['name_enter'].value)
            sal_enter = int(form['salary_enter'].value)
            dep_id_enter = int(form['dep_id_enter'].value)
            job_id_enter = int(form['job_id_enter'].value)
            s = db.redact_worker(id_enter, name_enter, sal_enter, dep_id_enter, job_id_enter)
            body = HTML_OUTPUT_PAGE.format(s)
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'move_worker':  # перейти від переведення до результату
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if "id_enter" in form and "salary_enter" in form and "dep_id_enter" in form \
                and "job_id_enter" in form:
            id_enter = int(form['id_enter'].value)
            sal_enter = int(form['salary_enter'].value)
            dep_id_enter = int(form['dep_id_enter'].value)
            job_id_enter = int(form['job_id_enter'].value)
            xml_move(id_enter, sal_enter, dep_id_enter, job_id_enter)
            s = db.move_worker(id_enter, sal_enter, dep_id_enter, job_id_enter)
            body = HTML_OUTPUT_PAGE.format(s)
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'adding_department':  # перейти до додавання департаменту
        body = HTML_FULL_DEP_PAGE.format("add", "")
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'redacting_department':  # перейти до редагування департаменту
        body = HTML_FULL_DEP_PAGE.format("redact", STUFF1)
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'deleting_department':  # перейти до видалення департаменту
        body = HTML_SHORT_DEP_PAGE
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'delete_department':  # видалити департамент
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if "id_enter" in form:
            id_enter = int(form['id_enter'].value)
            s = db.delete_department(id_enter)
            body = HTML_OUTPUT_PAGE.format(s)
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'add_department':  # додати департамент
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if "name_enter" in form and "descr_enter" in form and "workers_enter" in form:
            name_enter = str(form['name_enter'].value)
            descr_enter = str(form['descr_enter'].value)
            workers_enter = int(form['workers_enter'].value)
            s = db.add_department(name_enter, descr_enter, workers_enter)
            body = HTML_OUTPUT_PAGE.format(s)
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'redact_department':  # редагувати департамент
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if "id_enter" in form and "name_enter" in form and "descr_enter" in form and "workers_enter" in form:
            id_enter = int(form['id_enter'].value)
            name_enter = str(form['name_enter'].value)
            descr_enter = str(form['descr_enter'].value)
            workers_enter = int(form['workers_enter'].value)
            s = db.redact_department(id_enter, name_enter, descr_enter, workers_enter)
            body = HTML_OUTPUT_PAGE.format(s)
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'adding_job':  # перейти до додавання посади
        body = HTML_FULL_JOB_PAGE.format("add", "")
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'redacting_job':  # перейти до редагування посади
        body = HTML_FULL_JOB_PAGE.format("redact", STUFF1)
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'deleting_job':  # перейти до видалення посади
        body = HTML_SHORT_JOB_PAGE
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'add_job':  # додати посади
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if "name_enter" in form and "descr_enter" in form and "salary_enter" in form:
            name_enter = str(form['name_enter'].value)
            descr_enter = str(form['descr_enter'].value)
            salary_enter = int(form['salary_enter'].value)
            s = db.add_job(name_enter, descr_enter, salary_enter)
            body = HTML_OUTPUT_PAGE.format(s)
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'redact_job':  # редагувати посади
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if "id_enter" in form and "name_enter" in form and "descr_enter" in form and "salary_enter" in form:
            id_enter = int(form['id_enter'].value)
            name_enter = str(form['name_enter'].value)
            descr_enter = str(form['descr_enter'].value)
            salary_enter = int(form['salary_enter'].value)
            s = db.redact_job(id_enter, name_enter, descr_enter, salary_enter)
            body = HTML_OUTPUT_PAGE.format(s)
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    elif environ.get('PATH_INFO', '').lstrip('/') == 'delete_job':  # видалити посади
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        if "id_enter" in form:
            id_enter = int(form['id_enter'].value)
            s = db.delete_job(id_enter)
            body = HTML_OUTPUT_PAGE.format(s)
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    else:
        # якщо команда невідома, то виникла помилка
        start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
        body = 'Сторінку не знайдено'
    return [bytes(body, encoding='utf-8')]


if __name__ == '__main__':
    # створити та запуститити WSGI-сервер
    from wsgiref.simple_server import make_server
    print('=== Local WSGI webserver ===')
    httpd = make_server('localhost', 3009, application).serve_forever()
