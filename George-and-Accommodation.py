n = int(input())
c = 0

for _ in range(n):
    t,p = str(input()).split(' ')
    t = int(t)
    p = int(p)
    if (p - t) >= 2:
        c += 1

print(c)