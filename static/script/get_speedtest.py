import subprocess

import sys

def test_speed(val):

    save_path = '/var/www/container/log/'
    test_command = ['/usr/local/bin/speedtest-cli', '--secure']
    start_script = subprocess.Popen(test_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8')

    match val:
        case "ok":
            with open(f'{save_path}speed.log', 'w') as speed:
                res = []
                for line in start_script.stdout:
                   if 'Download' in line or 'Upload' in line:
                        res.append(line.strip())
                speed.write(" ".join(res))
                speed.close()
        case "bad":
            with open(f'{save_path}speed.log', 'w') as speed:
                speed.write("Not connection")
                speed.close()

try:
    subprocess.check_call(["ping", "-c 1", "8.8.8.8"])
    test_speed("ok")
except subprocess.CalledProcessError:
    test_speed("bad")