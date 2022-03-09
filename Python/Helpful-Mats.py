s = input()
n1 = n2 = n3 = 0

for i in s:
  if '1' == i:
    n1 += 1
  if '2' == i:
    n2 += 1
  if '3' == i:
    n3 += 1

ss = ('1+' * n1 + '2+' * n2 + '3+' * n3)
print(ss[:-1])
