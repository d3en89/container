import sys
import subprocess
sys.path.insert(1, '/mnt/D2A44A41A44A2875/YandexDisk/dev/container')

from webpage import app
from static.script.get_speedtest import test_speed

try:
    subprocess.check_call(["ping", "-c 1", "8.8.8.8"])
    test_speed("ok")
except subprocess.CalledProcessError:
    test_speed("bad")


if __name__ == "__main__":
    app.run()
