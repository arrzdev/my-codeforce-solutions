s = str(input())
l = 0
u = 0

#FAZER A CONTAGEM DE LETRAS MAIUSCULAS E MINUSCULAS
for i in range(len(s)):
    if s[i].islower():
        l += 1
    if s[i].isupper():
        u += 1

#SE A QUANTIDADE DE MINUSCULAS FOR MENOR QUE A DE MAIUSCULAS ENTÃO COLOCAR TODAS AS LETRAS MAIUSCULAS
if l < u:
    s = s.upper()
else: #SENÃO COLOCAR MINUSCULAS
    s = s.lower()

print(s)
