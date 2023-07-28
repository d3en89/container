import subprocess

from webpage import app
from .static.script.get_speedtest import test_speed

try:
    subprocess.check_call(["ping", "-c 1", "8.8.8.8"])
    test_speed("ok")
except subprocess.CalledProcessError:
    test_speed("bad")


if __name__ == "__main__":
    app.run()
