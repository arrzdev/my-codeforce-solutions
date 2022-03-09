n = int(input())
string = str(input())
count = 0

for i in range(1, n):
  if string[i] == string[i-1]:
    count += 1

print(count)
