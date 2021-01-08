n,h = str(input()).split(' ')
gh = str(input()).split(' ')

w = 0

for i in range(int(n)):
    if int(gh[i]) > int(h):
        w += 2
    else:
        w += 1

print(w)