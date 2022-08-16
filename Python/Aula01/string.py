# print(dir(str))

nome = 'Luan Lara'
print(nome)

print(nome[3]) #retorna a 4° letra (começa no 0,1,2,3...)

print("Luan Lara" == 'Luan Lara') #True

texto = 'Texto entre apóstrofos pode ter "aspas"'
print(texto)

doc = """texto com multiplas
linhas..."""
print(doc)


nome = 'Um nome qualquer'
print(nome[0])
print(nome[6])
print(nome[-3]) #vai do lado oposto (fim da string) sem contar 0 porque não existe -0
print(nome[4:]) #não conta os 4 primeiros caracteres
print(nome[-5:]) #conta os últimos 5 caracteres
print(nome[:4]) #conta os 4 primeiros caracteres

# O PRIMEIRO NÚMERO/LETRA ESTÁ CONTIDO E O ÚLTIMO NÃO EM PYTHON (DENTRO DE INTERVALOS)
# LEMBRAR O INDEX DE CADA VARIÁVEL, COMEÇA NO 0, 1, 2, 3, 4...
print(nome[1:5]) #intervalo entre os caracteres 2 a 5 (o último não será incluso, apenas para nele)

numeros = '1234567890'
print(numeros[::]) #imprime todos os valores
print(numeros[::2]) #imprime pulando números de 2 em 2
print(numeros[::3]) #imprime pulando números de 3 em 3
print(numeros[::-1]) #imprime todos os valores ao contrário
print(numeros[3::2]) #imprime a partir do 4° caractere pulando de 2 em 2 (o index 3 é o caractere "4")
print(numeros[3:5]) #imprime do index 3 a 5 ("4" e "5")
