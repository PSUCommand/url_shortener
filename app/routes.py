from app import app, generate_url as gen
from flask import render_template, request, url_for, redirect, abort, g
from app.db import get_db

our_domain = 'http://localhost:5000/'
link_size = 5
#our_domain = 'http://' +"The_best_domain_in_the_world/"
@app.route('/')
@app.route('/make_short', methods = ["POST", "GET"])
def make_short():
    #если пользователь нажал на кнопку
    if request.method == "POST":
        #если кнопка сгенерировать
        if request.form['gen'] == "GEN":
            user_url = request.form["input2"]
            if user_url == "": 
                return render_template("index.html")
            db = get_db()
            new_url=""
            new_link_size = link_size
            while True:
                new_url = our_domain + gen.generate_url(new_link_size) #TODO:генерируем ссылку
                if db.execute('SELECT short_link FROM links WHERE short_link=?', (new_url,)).fetchone() is None:
                    break
                new_link_size += 1

            #TODO: добавляем в БД
            db.execute('INSERT INTO links (short_link, long_link) VALUES (?, ?)', (new_url, user_url))
            db.commit()

            return render_template("index.html", new_url=new_url, user_url = user_url, new_user_url=our_domain)

        #если кнопка сократить
        elif request.form['cut'] == "CUT":
            user_url = request.form["input1"]
            new_url = request.form["output1"]
            if user_url == "" or new_url == our_domain or new_url == "": 
                return render_template("index.html", new_user_url=our_domain)

            db = get_db()

            if db.execute('SELECT short_link FROM links WHERE short_link=?', (new_url.lower(),)).fetchone() is None:
            #TODO: добавляем в БД
                db.execute('INSERT INTO links (short_link, long_link) VALUES (?, ?)', (new_url, user_url))
                db.commit()
            else:
                return render_template("index.html", new_user_url=our_domain, old_user_url = user_url)
            return render_template("index.html", new_user_url=new_url, old_user_url = user_url)
    #если метод "Get"
    else:
        return render_template("index.html", new_user_url=our_domain)    #отобразить главную страницу

@app.route('/<short_url>', methods = ["GET"])
def redirect_short_url(short_url):
    #TODO: проверка есть ли ссылка в БД
    db = get_db()
    long_url = db.execute('SELECT long_link FROM links WHERE short_link=?', (our_domain+short_url.lower(),)).fetchone()
    if long_url is not None:
        return redirect(long_url['long_link'])
    else:
        abort(404)


@app.errorhandler(400)
def not_found(error):
    return render_template('400.html'), 400

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404