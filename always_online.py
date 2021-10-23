import os
import time
from NWAFU_WIFI_login.LoginManager import LoginManager


def is_connect_internet(testip):
    status = os.system(u"ping {} -w 8".format(testip))
    return status == 0


def always_login(username, password, checkinterval):
    testip = "210.27.84.131"  # 只能由内网访问
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
            print("失败")
            timestamp()
            try:
                login()
            except Exception:
                pass


if __name__ == "__main__":
    username = "nwafu_account"
    password = "nwafu_password"
    checkinterval = 5 * 60  # 每五分钟检测一次

    always_login(username, password, checkinterval)
