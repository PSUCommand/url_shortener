from app import app, check_url, generate_url as gen
from flask import render_template, request, url_for, redirect, abort

our_domain = 'http://localhost:5000/'
link_size = 5
#our_domain = 'http://' +"The_best_domain_in_the_world/"
@app.route('/')
@app.route('/make_short', methods = ["POST", "GET"])
def make_short():
    #если пользователь нажал на кнопку
    if request.method == "POST":
        #если кнопка сгенерировать
        if request.form['submit_button'] == "Random generate": # нажатие кнопки сгенерировать рандомныую ссылку
            new_link_size = link_size
            while(True):
                user_url=our_domain+gen.generate_url(new_link_size) #генерируем ссылку
                if not check_url.check_url(user_url):# проверка ссылки
                    new_link_size += 1 # увеличиваем длинну ссылки для большего кол-ва вариантов 
                    user_url=our_domain+gen.generate_url(new_link_size)#генерируем новую ссылку
                else:
                    break
            #TODO: добавляем в БД
            # в БД закидывать request.form["text_field"]   как начальная ссылка пользователя 
            # user_url как сгенерированная ссылка
            return render_template("main_page.html", user_url=user_url)#вывод рандомной короткой ссылки для копирования
        #если кнопка Готово
        elif request.form['submit_button'] == 'Get URL!': # нажатие кнопки  ссылку
            user_url = our_domain + request.form["text_field"] #TODO: заменить text_field на имя tb из которого берем 
            #пользовательскую короткую ссылку  # получить инфу из поля ввода короткой пользовательской ссылки 
            if not check_url.check_url(user_url):# проверка ссылки
                abort(400)    # кидаем ошибку 404
            else:
                #TODO: добавляем в БД
                # в БД закидывать request.form["text_field"]   как начальная ссылка пользователя
                # user_url как пользовательская короткая ссылка
                return render_template("main_page.html", user_url=user_url) #вывод пользовательсокй короткой ссылки для копирования
           
        else:
            pass # unknown
    #если метод "Get"
    else:
        return render_template("main_page.html", user_url="")    #отобразить главную страницу

@app.route('/<short_url>', methods = ["GET"])
def redirect_short_url(short_url):
    #TODO: проверка есть ли ссылка в БД
    long_url = "https://2x2tv.ru/"
    if long_url!="":
        return redirect(long_url)
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