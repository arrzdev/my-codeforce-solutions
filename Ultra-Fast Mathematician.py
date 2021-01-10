n1 = list(str(input()))
n2 = list(str(input()))

for i in range(len(n1)):
	if n1[i] == '1' and n2[i] == '0' or n1[i] == '0' and n2[i] == '1':
		n1[i] = '1'
	else:
		n1[i] = '0'
#t
print("".join(n1))
