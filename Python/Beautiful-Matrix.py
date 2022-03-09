r1 = str(input()).replace(' ', '')
r2 = str(input()).replace(' ', '')
r3 = str(input()).replace(' ', '')
r4 = str(input()).replace(' ', '')
r5 = str(input()).replace(' ', '')
y = 0

if '1' in r1 or '1' in r5: #2
  if r1[0] == '1' or r1[4] == '1' or r5[0] == '1' or r5[4] == '1':
    y += 4
  elif r1[1] == '1' or r1[3] == '1' or r5[1] == '1' or r5[3] == '1':
    y += 3
  else:
    y += 2
elif '1' in r2 or '1' in r4: #1
  if r2[0] == '1' or r2[4] == '1' or r4[0] == '1' or r4[4] == '1':
    y += 3
  elif r2[1] == '1' or r2[3] == '1' or r4[1] == '1' or r4[3] == '1':
    y += 2
  else:
    y += 1
elif '1' in r3:
  if r3[0] == '1' or r3[4] == '1':
    y += 2
  elif r3[1] == '1' or r3[3] == '1':
    y += 1

print(y)

