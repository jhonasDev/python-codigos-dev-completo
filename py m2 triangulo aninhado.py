r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3= float(input('terceiro segmento: '))
if r1 < r2+r3 and r2 < r1 + r3 and r3< r2+r1:
    print('os segmentos forma um triângulo')
    if r1 == r2 ==r3:
        print('equilatero')
    elif r1!= r2!= r3 != r1: 
        print('escaleno')
    else:
        print('isosceles')
else:
    print('não forma uma triangulo!')
