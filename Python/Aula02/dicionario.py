pessoa = {}
print(type(pessoa))

pessoa = {'nome': 'Andre', 'idade': 35, 'altura': 1.83}
print(pessoa)
print(pessoa['idade'])


pessoa = {'nome': 'Andre', 'idade': 35, 'altura': 1.83, 'cursos': ['C#', 'Node', 'React', 'Python']}
print(pessoa)
print(pessoa['altura'])
print(pessoa['cursos'])
print(pessoa['cursos'][2])

print(pessoa.keys()) #imprimir as chaves
print(pessoa.values()) # imprmir os valores
print(pessoa.items()) # imprimir os itens

items = list(pessoa.items())
print(items[2])

############################

lista_pessoas = [{'nome': 'Andre', 'idade': 35, 'altura': 1.83},
                {'nome': 'Ana', 'idade': 22, 'altura': 1.57},
                {'nome': 'João', 'idade': 39, 'altura': 1.78},
                {'nome': 'Bia', 'idade': 27, 'altura': 1.63}]

print(lista_pessoas[2]['idade'])

###########################

pessoa1 = {'nome': 'Andre', 'idade': 35, 'altura': 1.83}
pessoa1.update({'idade': 34, 'genere': 'não binerie'})

print(pessoa1)