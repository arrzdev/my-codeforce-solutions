#n,t = str(input()).split(' ')
t = int(input()[2:])
s = str(input())

for _ in range(t):
    s = s.replace('BG', 'GB')    
print(s)