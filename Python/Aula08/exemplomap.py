lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 28}
]

so_nomes = map(lambda p: p['nome'], lista_2)
print(so_nomes)
print(list(so_nomes))
