lista = []
print(type(lista))

print(len(lista)) # len = tamanho da lista em números de posições

lista.append(1) # append = adicionar no final da lista
lista.append(5)
print(lista)

print(lista[0])
print(len(lista))

nova_lista = [1, 5, 'Ana', 'Bia',['C#', 'Python', 'Node'], 3.14]
print(nova_lista)
print(nova_lista[3])
print(nova_lista[4])
print(nova_lista[4][1][3]) #No elemento de índice 4, o elemento de índice 1, o caractere de índice 3 = "h"

print(nova_lista)
nova_lista.remove(5) # () = elemento 
print(nova_lista)
nova_lista.reverse() #inverte as posições da lista
print(nova_lista)

del nova_lista[2] # del = deletar
print(nova_lista)

#######################

lista2 = [1, 5, 'Raquel', 'Guilherme', 3.1415, 'Guilherme']
print((lista2.index(5))) # posição da lista
print((lista2.index('Raquel')))
print((lista2.index('Guilherme')))

'Andre' in lista2 # procurar elemento
'Raquel'in lista2

lista2.append('Andre')
print(lista2)

lista2.insert(2, 'Ana') # inserir um elemento em uma certa posição
print(lista2)

lista2.insert(2,['Metalica', 'Led', 'Ozy'])
print(lista2)

#######################

lista3 = ['Ana', 'Aline', 'Guilherme', 'Andre', 'Dani']
print(lista3[1:3]) # imprimir o elemento apartir do 1 até o 2
print(lista3[1:-1])
print(lista3[1:])