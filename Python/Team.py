y = 0 

for _ in range(int(input())):
  x = str(input()).replace(' ', '')
  if x[0] == '0' and x[1] == '1' and x[2] == '1':
    y += 1
  if x[1] == '0' and x[0] == '1' and x[2] == '1':
    y += 1
  if x[2] == '0' and x[0] == '1' and x[1] == '1':
    y += 1
  if x[0] == '1' and x[1] == '1' and x[2] == '1':
    y += 1

print(y)
