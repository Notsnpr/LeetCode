s="())()))()(()(((())(()()))))((((()())(())"
locked = "1011101100010001001011000000110010100101"
if len(s) % 2 != 0:
    print(False)
    exit()
    exit()
s_locked=[]
s_unlocked=[]
for i in range(len(s)):
    if locked[i] =="0":
        s_unlocked.append(i)
    elif s[i]=="(":
        s_locked.append(i)
    else:
        if s_locked:
            s_locked.pop()
        elif s_unlocked:
            s_unlocked.pop()
        else:
            print(False)
while s_locked and s_unlocked and s_locked[-1]<s_unlocked[-1]:
    s_locked.pop()
    s_unlocked.pop()
if s_locked:
    print(False)
print(True)