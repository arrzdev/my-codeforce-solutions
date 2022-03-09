n = int(input())
s = str(input())

a = 0
d = 0

for i in range(n):
    if s[i] == 'A':
        a += 1
    else:
        d += 1

if a > d:
    print('Anton')
elif a == d:
    print('Friendship')
else:
    print('Danik')
    