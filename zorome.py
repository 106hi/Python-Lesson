s = input().rstrip().split(' ')
ss = s[0] + s[1]
if len(ss) == ss.count(s[0][0]):
    print("Yes")
else:
    print("No")