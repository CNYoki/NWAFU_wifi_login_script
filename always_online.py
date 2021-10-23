import os
import time
from NWAFU_WIFI_login.LoginManager import LoginManager


def is_connect_internet(testip):
    status = os.system(u"ping {} -c 8".format(testip))
    return status == 0


def always_login(username, password, testip, checkinterval):
    lm = LoginManager()
    login = lambda: lm.login(username=username, password=password)
    timestamp = lambda: print(time.asctime(time.localtime(time.time())))

    timestamp()
    try:
        login()
    except Exception:
        pass
    while 1:
        time.sleep(checkinterval)
        if not is_connect_internet(testip):
            timestamp()
            try:
                login()
            except Exception:
                pass


if __name__ == "__main__":
    username = "nwafu_account"
    password = "nwafu_password"
    testip = "nwafu.edu.cn"  # IP to test whether the Internet is connected
    checkinterval = 5 * 60

    always_login(username, password, testip, checkinterval)
