a,b = str(input()).split(" ")
a = int(a)
b = int(b)
for _ in range(b):
	if a % 10 == 0:
		a /= 10
	else:
		a -= 1
print (int(a))