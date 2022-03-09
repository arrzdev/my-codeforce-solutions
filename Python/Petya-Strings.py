n1 = str(input()).lower()
n2 = str(input()).lower()

if n1 < n2:
  print('-1')
elif n1 == n2:
  print('0')
elif n1 > n2:
  print('1')

#################################################################
#COISAS A RECORDAR:
#################################################################
#n1c = [ord(c) for c in n1]
#n2c = [ord(c) for c in n2]

#################################################################
# PARA CADA CARACTER NA STRING ATRIBUIR-LHE O NUMERO E ADICIONA-LO AO NUMERO TOTAL DA CONTAGEM n1c OU n2c
#n1c = 0
#n2c = 0
#for c in n1:
#  n1c += ord(c)
#for c in n2:
#  n2c += ord(c)
#################################################################