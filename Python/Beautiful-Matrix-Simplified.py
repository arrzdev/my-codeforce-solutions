r1 = str(input()).replace(' ', '')
r2 = str(input()).replace(' ', '')
r3 = str(input()).replace(' ', '')
r4 = str(input()).replace(' ', '')
r5 = str(input()).replace(' ', '')

lista_de_rows = [r1, r2, r3, r4, r5]

#CHECK ROW
for i in range(0, 5, 1): #descobrir em qual row das 5rows se encontra o '1'
  if '1' in lista_de_rows[i]:
    n_row = i+1 #algarismo correspondente a row certa
    row_certa = lista_de_rows[i] #armazenar a row certa numa variavel r

#CHECK COLUMN
for i in range(0, 5 , 1): #para a row certa descobrir em que column se encontra o '1'
  if '1' in row_certa[i]:
    n_column = i+1 #algarismo correspondete a column certa

print(abs(3-n_row)+abs(3-n_column)) #Calculo da interseção??

'''
EXERCICO COM VARIAVEIS SIMPLIFICADAS:

r1 = str(input()).replace(' ', '')
r2 = str(input()).replace(' ', '')
r3 = str(input()).replace(' ', '')
r4 = str(input()).replace(' ', '')
r5 = str(input()).replace(' ', '')

p = [r1, r2, r3, r4, r5]

#CHECK ROW
for i in range(0, 5, 1): #descobrir em qual row das 5rows se encontra o '1'
  if '1' in p[i]:
    nr = i+1 #algarismo correspondente a row certa
    r = p[i] #armazenar a row certa numa variavel r

#CHECK COLUMN
for i in range(0, 5 , 1): #para a row certa descobrir em que column se encontra o '1'
  if '1' in r[i]:
    nc = i+1 #algarismo correspondete a column certa

print(abs(3-nr)+abs(3-nc)) #Calculo da interseção??
'''