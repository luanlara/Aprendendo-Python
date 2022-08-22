a = int(input('Digite o valor de A: '))
#print(a)
#print(type(a))

b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

resultado = 0

if a > b and a > c:
    restulado = a
elif b > c and b > a:
    resultado = b
else:
    resultado = c

print(resultado)