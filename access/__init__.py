import win32com.client
import pythoncom
import sys
import access.login as lgn


if __name__ == "__main__":
    server_addr = 'hts.ebestsec.co.kr'
    server_port = 200001
    server_type = 0
    user_id = 'kaniza79'
    user_pass = 'ldh79369'
    user_cert = 'kaniza793692!'

    inXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", lgn.XASessionEvents)
    bConnect = inXASession.ConnectServer(server_addr, server_port)

    if not bConnect:
        # 로그인 실패
        nErrCode = inXASession.GetLastError()
        strErrMsg = inXASession.GetErrorMessage(nErrCode)
        print(strErrMsg)
        sys.exit(0)

    # 로그인 성공
    inXASession.Login(user_id, user_pass, user_cert, server_type, 0)

    while lgn.XASessionEvents.logInState == 0:
        pythoncom.PumpWaitingMessages()

    # 계좌정보 불러오기
    nCount = inXASession.GetAccountListCount()
    for i in range(nCount):
        print("Account : %d - %s" % (i, inXASession.GetAccountList(i)))