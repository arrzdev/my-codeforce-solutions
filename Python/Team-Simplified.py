y = 0

for _ in range(int(input())):
  a,b,c = input().split(' ')
  if int(a) + int(b) + int(c) > 1:
    y += 1

print(y)