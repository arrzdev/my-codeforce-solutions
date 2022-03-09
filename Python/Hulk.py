one = 'I hate'
two = 'I love'

t = int(input())
s = '' 


for i in range(1, t+1):
    if i % 2 == 0:
        s = s + ' that ' + two
    else:
        if s == '':
            s = one
        else:
            s = s + ' that ' + one
    

print(s + ' it')
    
        