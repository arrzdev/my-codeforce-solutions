k,n,w = str(input()).split(' ')
cost = 0 

for i in range(1, int(w)+1):
  cost += (int(k) * i)

#PRECISA DE
b = cost-int(n) #b de borrow

if b >= 0:
  print(b)
else:
  print('0')
 