'''
n = int(input())
t = 0 

for i in range(1, n+1):
    if i % 2 == 0:
        t += i
    else:
        t -= i
        
print(t)

# n/2-n*(n%2) #
'''


n = int(input())

if n % 2 == 0:
    print(int(n/2))
else:
    #print(int((-n/2)-0,5))
    print(int(-n//2))

