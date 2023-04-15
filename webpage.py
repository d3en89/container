from flask import Flask, render_template, request
import subprocess
import funct
app = Flask(__name__)

##Проверяем структуру папок если её нет то создаём
funct.check_dir("/var/www/container/log")
funct.check_dir("/var/www/container/log/archive")

###Проверяем наличие файлов логов если их нет то создаём
funct.check_file("/var/www/container/log/container.log")
funct.check_file("/var/www/container/log/room_temp.log")
funct.check_file("/var/www/container/log/speed.log")

@app.route('/')
def index():
    try:
        degree_1 = funct.room_degree()
        degree_2 = funct.speed_internet()
    except FileNotFoundError:
        degree_1 = '-'
        funct.log_write("Ошибка, файл room_temp.log - не найден\n")
    return  render_template('index.html', room_degree=degree_1, speed_internet=degree_2)

@app.route('/hardware.html')
def hardware():
    return  render_template('hardware.html')

@app.route('/user_settings.html')
def user():
    return  render_template('user_settings.html')

@app.route('/server_settings.html')
def server():
    return  render_template('server_settings.html')

@app.route('/syslog.html', methods=['GET', 'POST'])
def syslog():
### Получаем число трок с вебморды по POST
    if request.method == 'POST':
        if request.form.get("log") == "Syslog":
            rows = request.form["rsys"]
            if rows == "":
               rows = 0
            try:
                cat_syslog = funct.file_read("/var/log/syslog", f'{rows}')
                return render_template('syslog.html', cat_syslog=cat_syslog)
            except IndexError:
                funct.log_write(f'Вы указали больше строчек чем существует в файле /var/log/syslog\n')
                rows = 5
                cat_syslog = funct.file_read("/var/log/syslog", f'{rows}')
                return render_template('syslog.html', cat_syslog=cat_syslog)
            else:
                return render_template('syslog.html', cat_syslog=cat_syslog)

        elif request.form.get("log") == "Container":
            rows = request.form["rsys"]
            if rows == "":
                rows = 0
            try:
                cat_container = funct.file_read("/var/www/container/log/container.log", rows)
                return render_template('syslog.html',  cat_syslog=cat_container)
            except IndexError:
                funct.log_write(f'Вы указали больше строчек чем существует в файле /var/www/container/log/container.log\n')
                rows = 5
                cat_container = funct.file_read("/var/www/container/log/container.log", rows)
                return render_template('syslog.html', cat_syslog=cat_container)
            else:
                return render_template('syslog.html', cat_syslog=cat_container)

    elif request.method == 'GET':
        return render_template('syslog.html')

