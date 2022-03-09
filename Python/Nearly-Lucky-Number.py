s = str(input())
c = 0

for i in range(len(s)):
    if s[i] == '4' or s[i] == '7':
        c += 1
if c == 4 or c == 7:
    print('YES')
else:
    print('NO')




"""
nl = 0

if '7' in s and '4' in s:
    if s.replace('4', '').replace('7', '') == '':
        print('YES')
    else:
        for i in range(0, len(s)):
            if s[i] == '4' or s[i] == '7':
                nl += 1
        if nl == 4 or nl == 7:
            print('YES')
        else:
            print('NO')
    
else:
    for i in range(0, len(s)):
        if s[i] == '4' or s[i] == '7':
            nl += 1
    if nl == 4 or nl == 7:
        print('YES')
    else:
        print('NO')
"""
