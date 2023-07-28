import os.path
import datetime

### Read syslog file
### Читаем файл сислога с конца на указанное кол-во
def file_read(files, rows):
    read =[]
    with open(files, "r", encoding='utf-8') as file:
        lines = file.readlines()
    for i in range(int(rows), 0, -1):
        read.append(lines[-i])
    return read


###вытаскиваем последнюю запись от датчика температуры №1
def room_degree():
    day = datetime.datetime.now().strftime('%Y-%m-%d')
    with open(f'log/{day}_room_temp.log', "r", encoding='utf-8') as file:
        sign = u'\N{DEGREE SIGN}'
        lines = file.readlines()[-1].replace('Temp', f'С{sign}').replace("Humidity", 'Влажность').replace("*", ",")
    return lines

def speed_internet():
    with open(f'log/speed.log', "r", encoding='utf-8') as file:
        lines = file.readline()
    return lines


### Функция записи в лог файл контайнера
def log_write(text):
    day = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    log_w = open("/var/www/container/log/container.log", "r+", encoding='utf-8')
    log_w.seek(0, 2)
    log_w.write(f'{day} {text}')
    log_w.close()


##Проверяем наличие файлов если нет файла то создаём его
def check_file(file):
    check = os.path.exists(f'{file}')
    if check == True:
        log_write(f'Файл %s существует\n' % file)
    else:
      open(file, "a").close()
      log_write(f'Файл %s создан\n' % file)


##Проверяем наличие каталогов
def check_dir(dir):
    check = os.path.isdir(f'{dir}')
    if check == True:
        log_write("Директория " + f'{dir}' + " существует\n")
    else:
        try:
            os.makedirs(dir)
        except OSError:
            log_write(f'Создать директорию {dir} не удалось\n')
        else:
            log_write(f'Успешно создана {dir} директория\n')
