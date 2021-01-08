n = int(input())

if n % 5 == 0:
  n /= 5
else:
  n,t = str(n/5).split(".") #t == trash
  n = int(n) + 1
  
print(int(n))