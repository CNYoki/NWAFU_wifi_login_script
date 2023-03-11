import os
import sys
import time
from NWAFU_WIFI_login.LoginManager import LoginManager


def isConnected(testIp):
    print("Checking connection to {}".format(testIp))
    print("----------------")
    status = os.system(u"ping {} -w 1".format(testIp))
    print("----------------")
    return status == 0


def loginToInternet(username, password):
    loginObj = LoginManager()
    currentTime = time.asctime(time.localtime(time.time()))
    print("At {}:".format(currentTime))
    try:
        loginObj.login(username=username, password=password)
    except Exception:
        pass
    if isConnected("210.27.84.131"):
        return True
    else:
        return False


def main(username=None, password=None):
    username = sys.argv[1]
    password = sys.argv[2]

    loginStatus = loginToInternet(username, password)

    if loginStatus:
        print("Login successful!")
        return 0
    else:
        print("Login failed!")
        return 1


if __name__ == "__main__":
    returnVal = main()
    sys.exit(returnVal)
