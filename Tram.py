n = int(input())
r = 0
c = 0

for _ in range(n):
  a,b = str(input()).split(" ")
  r -= int(a)
  r += int(b)
  if r > c:
    c = r
    c
print(c)