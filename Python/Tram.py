n = int(input())
r = 0
c = 0


for _ in range(n):
	a,b = str(input()).split(" ")
	r += int(b)
	r -= int(a)
	if r > c:
		c = r
		
print(c)
	