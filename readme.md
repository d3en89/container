Рабочий сервис для снятия температуры с датчика для разбериПИ 
для работы необходим Python3.10

Скрипт снятия температуры лежит static/script/room_temp.sh
 - Его надо ставить в крон

Скрипт измерения скорости интернета static/script/get_speedtest.py
 - для  его работы необходима программа speedtest-cli
   - софт использую от сюда "https://lindevs.com/install-speedtest-cli-on-raspberry-pi"
     . sudo wget -O /usr/local/bin/speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
     . sudo chmod a+x /usr/local/bin/speedtest-cli
 - Его надо ставить в крон
