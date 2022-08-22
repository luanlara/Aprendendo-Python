a = 10

while a > 0: 
    print(a)
    a = a -1

# O range fará com que o intervalo entre 1 e 11 seja inserido na variável (o 11 não conta, pois é aberto)
for x in range(1, 11):   
    for y in range(1,11):
        print(f'{x} * {y} = {x * y}') 
        # O y irá diminuir até chegar no 10, e então o x diminui em 1, repetindo o y do 1 ao 10
        # Transformação de x e y em caracteres com o f  
        # # As chaves buscam o valor e entrega o resultado convertendo string pra numérico

# Repetição para lista
dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
for dia in dias_semana:
    print(f'Hoje é {dia}')


# Repetição para lista com maior número de dados (listas dentro da lista que contém dicionários)
lista_pessoas = [{'id':1, 'nome': 'Andre', 'idade': 35, 'altura': 1.83, 'cursos': ['C#', 'Python', 'React']},
                {'id':2, 'nome': 'Ana', 'idade': 22, 'altura': 1.57, 'cursos': ['C#', 'Python', 'Node', 'C++']},
                {'id':3, 'nome': 'João', 'idade': 39, 'altura': 1.78, 'cursos': ['Python', 'Node']},
                {'id':4, 'nome': 'Bia', 'idade': 27, 'altura': 1.63, 'cursos': ['C#', 'Java', 'React']}]

for pessoa in lista_pessoas:
    for curso in pessoa['cursos']:
        nome = pessoa['nome']
        print(f'A pessoa {nome} faz o curso {curso}')