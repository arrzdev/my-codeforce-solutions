n = int(input())

if n % 5 == 0:
	x = n/5
else:
	x,t = str(n/5).split(".")
	x = int(x) + 1
	
print(int(x))
	