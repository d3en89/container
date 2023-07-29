Рабочий сервис для снятия температуры с датчика для разбериПИ 
- для работы необходим Python3.10


Так же необходим web сервер  в данном случае  nginx:

    server {
     listen 80;
     server_name app;
     access_log  /var/log/nginx/app.log;
    
     location / {
     #include proxy_params
     proxy_pass http://127.0.0.1:8000;
     proxy_set_header Host $host;
     proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
     }
    }

Для запуска сервиса при старте системы создаем файл демона:
    - создаем файл сервиса в /etc/systemd/system/container.service

        [Unit]
        Description=Container Automaitic System
        After=multi-user.target
        
        [Service]
        User=root
        Group=root
        WorkingDirectory=/var/www/container
        ExecStart=/usr/local/bin/gunicorn -b 127.0.0.1:8000 wsgi:app
        ExecReload=/bin/kill -s HUP $MAINPID
        KillMode=mixed
        TimeoutStopSec=5
        PrivateTmp=true
        Restart=on-failure
        RestartSec=2
        
        [Install]
        WantedBy=multi-user.target
        
 - sudo systemctl daemon-reload && sudo systemctl enable container.service && sudo systemctl start container.service

Скрипт снятия температуры лежит static/script/room_temp.sh
 - Его надо ставить в крон

Скрипт измерения скорости интернета static/script/get_speedtest.py
 - для  его работы необходима программа speedtest-cli
   - софт использую от сюда "https://lindevs.com/install-speedtest-cli-on-raspberry-pi"
     - sudo wget -O /usr/local/bin/speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
     - sudo chmod a+x /usr/local/bin/speedtest-cli
 - Его надо ставить в крон