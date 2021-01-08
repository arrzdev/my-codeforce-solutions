n = int(input())
y = 0

for _ in range(n):
  x = str(input())
  if '++' in x:
    y += 1
  if '--' in x:
    y-=1

print(y)