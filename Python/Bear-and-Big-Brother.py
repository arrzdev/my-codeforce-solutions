a,b = str(input()).split(' ')
a = int(a)
b = int(b)
y = 0

while True:
  if a <= b:  
    a *= 3
    b *= 2
    y += 1
  else:
    break

print(y)
  