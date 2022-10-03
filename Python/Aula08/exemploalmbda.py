def processar(titulo, lista, funcao):
    print(f'Processsando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))

if __name__ == '_main_':
   p = processar
   print('print para teste')
   p('Dobros de 1 a 10', range(1,11),lambda x: x*2)