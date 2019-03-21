class XASessionEvents:
    logInState = 0

    def __init__(self):
        print('init')
        super().__init__()

    def OnLogin(self, code, msg):
        print("onLogin method is called")
        print(str(code))
        print(str(msg))

        # 0000이 입력될 때만 로그인 성공
        if str(code) == '0000':
            XASessionEvents.logInState = 1

    def OnLogout(self):
        print("OnLogout method is called")

    def OnDisconnect(self):
        print("OnDisconnect method is called")
