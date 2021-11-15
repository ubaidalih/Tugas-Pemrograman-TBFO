def state1(c):
    if(ord(c) >= 65 and ord(c) <= 90):
        state = 2
    elif(ord(c) == 95):
        state = 2
    elif(ord(c) >= 97 and ord(c) <= 122):
        state = 2
    else :
        state = 3
    return state

def state2(c):
    if(ord(c) >= 65 and ord(c) <= 90):
        state = 2
    elif(ord(c) == 95):
        state = 2
    elif(ord(c) >= 97 and ord(c) <= 122):
        state = 2
    elif(ord(c) >= 48 and ord(c) <= 57):
        state = 2
    else :
        state = 3
    return state

def state3(c):
    state = 3
    return state

def isAccepted(s):
    state = 1
    for i in range (len(s)):
        if (state == 1):
            state = state1(s[i])
        if (state == 2):
            state = state2(s[i])
        if (state == 3):
            state = state3(s[i])
    if (state == 2):
        return True
    else :
        return False

str = "123"
if(isAccepted(str)):
    print("Variable accepted")
else:
    print("Variable error")
        