#!/bin/bash

###Задаём пути и файлы
room=$(date -I)_room_temp.log
path_log=var/www/container/log
path_log_archive=var/www/container/log/archive
temp=/usr/bin/Adafruit_Python_DHT/examples/AdafruitDHT.py

###Проверим кол-во строк в файле 
lines=`cat /$path_log/$room |wc -l`
if [ $lines -ge 720 ]
then
mv /$path_log/$room/$path_log_archive/$(date +"%Y-%m-%d-%H-%M")_room_temp.log.bak
fi

###Снимаем температуру с датчика находящийся на 4м пине
$temp 11 4 >> /$path_log/$room
$temp 11 4
