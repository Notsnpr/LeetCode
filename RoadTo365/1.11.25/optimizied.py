s="())()))()(()(((())(()()))))((((()())(())"
locked = "1011101100010001001011000000110010100101"

if len(s)%2==1:
    print(False)
s_locked=0
s_unlocked=0
for i in range(len(s)):
    if locked[i] =="0":
        s_unlocked+=1
    elif s[i]=="(":
        s_locked+=1
    else:
        if s_locked:
            s_locked-=1
        elif s_unlocked:
            s_unlocked-=1
        else:
            print(False)
s_locked=0
s_unlocked=0
for i in reversed(range(len(s))):
    if locked[i] =="0":
        s_unlocked+=1
    elif s[i]==")":
        s_locked+=1
    else:
        if s_locked:
            s_locked-=1
        elif s_unlocked:
            s_unlocked-=1
        else:
            print(False)
print(True)
