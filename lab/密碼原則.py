# 作業 2：密碼原則
import getpass
import time

def isPwdRuleOK(strPwd):

    iUpCase = 0
    iDownCase = 0
    iNum = 0
    iSymbol = 0
    iOther = 0
    for i in range(0,len(userPwd)):
        # 符號 33-47, 58-64, 91-96, 123-126
        # 大寫 65-90
        # 小寫 97-122
        # 數字 48-57
        iASCII = ord(userPwd[i])
        isSymbol = (iASCII in range(33,48)) or (iASCII in range(58,65)) or (iASCII in range(91,97)) or (iASCII in range(123,127))
        isUpCase = iASCII in range(65,97)
        isDownCase = iASCII in range(97,123)
        isNum = iASCII in range(48,58)

        if isSymbol:
            iSymbol += 1
        elif isUpCase:
            iUpCase += 1
        elif isDownCase:
            iDownCase += 1
        elif isNum:
            iNum += 1
        else:
            iOther += 1
        
    Score = [iSymbol, iUpCase,iDownCase,iNum]

    # print(Score)
    return Score.count(0) < 2


isPass = False
iInput = 0

while isPass == False:
    userPwd = getpass.getpass() 
    # print(userPwd)

    isPwdLenGt12 = len(userPwd) >= 12
    isPass = isPwdLenGt12 and isPwdRuleOK(userPwd)

    if isPass:
        print('password 符合規則')
        break
    else:
        print('password 不符合規則')
        print(userPwd)
        iInput += 1

    if iInput == 3:
        iInput = 0
        print('規則不符 3 次以上暫停輸入 5 秒鐘。')
        time.sleep(5)
            