#-*- coding:utf-8 -*-

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    Roman = []
    # dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    M = num // 1000
    if M >= 1:
        for i in range(M):
            Roman.append('M')
    num = num - M * 1000
    if num >= 900:
        Roman.append('CM')
        num = num - 900
    if num >= 500:
        Roman.append('D')
        num = num - 500

    C = num // 100
    if C != 0 and C != 4:
        for i in range(C):
            Roman.append('C')
    if C == 4:
        Roman.append('CD')
    num = num - C * 100
    if num >= 90:
        Roman.append('XC')
        num = num - 90
    else:
        if num < 90 and num >= 50:
            Roman.append('L')
            num = num - 50
        else:
            if num < 50 and num >= 40:
                Roman.append('XL')
                num = num - 40
    X = num // 10
    if X != 0:
        for i in range(X):
            Roman.append('X')
        num = num - X * 10
    if num == 9:
        Roman.append('IX')
    if num == 8:
        Roman.append('VIII')
    if num == 7:
        Roman.append('VII')
    if num == 6:
        Roman.append('VI')
    if num == 5:
        Roman.append('V')
    if num == 4:
        Roman.append('IV')
    if num == 3:
        Roman.append('III')
    if num == 2:
        Roman.append('II')
    if num == 1:
        Roman.append('I')
    return ''.join(Roman)

