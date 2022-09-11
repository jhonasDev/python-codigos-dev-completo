# -*- coding: utf-8 -*-
"""exercício derivadas de 0 a 15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JE29U_EB7GoHHtc5oHE8xSoLckZcjFrX

#### Jonatas da Silva Nonato  202104403216

## Usando os numeros de 0 a 15.
"""

listas = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(listas)

"""###Intervalo de 1 a 9"""

listas[1:10]

"""###Intervalo de 8 a 13"""

listas[8:14]

"""###Números pares e ímpares"""

pares = []
impares = []

for num in listas:
  if num % 2 == 0:
     pares.append(num)
  else:
     impares.append(num)

print(pares)

print(impares)

"""###todos os multiplos de 2, 3 e 4"""

y1 = [x**1 for x in listas if x % 2 == 0] 
print(y1)

y2 = [x**1 for x in listas if x % 3 == 0]
print(y2)

y3 = [x**1 for x in listas if x % 4 == 0]
print(y3)

"""###lista reversa"""

listas[::-1]

"""###Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9 em float:"""

sum(listas[10:16])/sum(listas[3:9])