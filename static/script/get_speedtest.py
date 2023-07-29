import subprocess

import sys

def test_speed(val):

    save_path = '/var/www/container/log/'
    #test_command = ['/usr/local/bin/speedtest-cli', '--secure']
    start_script = subprocess.Popen('/usr/local/bin/speedtest-cli --secure', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8')

    match val:
        case "ok":
            with open(f'{save_path}speed.log', 'w') as speed:
                res = []
                for line in start_script.stderr:
                    if 'ERROR' in line:
                        res += "" + line.strip()
                for line in start_script.stdout:
                    if 'Download' in line or 'Upload' in line:
                        res.append(line.strip())
                speed.write(" , ".join(res))
                speed.close()
                return res.split('Mbit/s')[0].replace("Download: ", "")
        case "bad":
            with open(f'{save_path}speed.log', 'w') as speed:
                speed.write("Not connection")
                speed.close()
                return 'Not connection'

if __name__ == "__main__":
    try:
        subprocess.check_call(["ping", "-c 1", "8.8.8.8"])
        print(test_speed("ok"))
    except subprocess.CalledProcessError:
        print(test_speed("bad"))