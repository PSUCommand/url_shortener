from app import app, check_url, generate_url as gen
from flask import render_template, request, url_for, redirect, abort

our_domain = 'http://localhost:5000/'
link_size = 6
#our_domain = 'http://' +"The_best_domain_in_the_world/"
@app.route('/')
@app.route('/make_short', methods = ["POST", "GET"])
def make_short():
    #если пользователь нажал на кнопку
    if request.method == "POST":
        #если кнопка сгенерировать
        if request.form['submit_button'] == "Random generate":
            user_url=our_domain+gen.generate_url(link_size) #TODO:генерируем ссылку
            #TODO: добавляем в БД
            return render_template("main_page.html", user_url=user_url)
        #если кнопка Готово
        elif request.form['submit_button'] == 'Get URL!':
            user_url = request.form["text_field"]  # получить инфу из поля
            # проверка ссылки
            if not check_url.check_short_url(user_url):
                abort(400)    # кидаем ошибку 404
            else:
                return render_template("main_page.html", user_url=user_url)
        else:
            pass # unknown
    #если метод "Get"
    else:
        return render_template("main_page.html", user_url="")    #отобразить главную страницу

@app.route('/<short_url>', methods = ["GET"])
def redirect_short_url(short_url):
    #TODO: проверка есть ли ссылка в БД
    if check_url.check_short_url(short_url):
        return redirect(long_url)
    #long_url = "https://2x2tv.ru/"
    #if long_url!="":
        #return redirect(long_url)
    else:
        abort(404)

# @app.route('/<user_url>', methods = ["GET"])
# def show_new_url(user_url):
#     return render_template("new_url.html", user_url=our_domain + user_url)


@app.errorhandler(400)
def not_found(error):
    return render_template('400.html'), 400

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404