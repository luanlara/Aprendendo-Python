class Contato:
    def __init__(self, nome, numero, email):
        self.nome = nome
        self.numero = numero
        self.email = email

class Agenda:
    def __init__(self, contato = []):
        self.contato = contato

    def addlista(self, contatonovo):
        self.contato.append(contatonovo)


def main():
    contato1 = Contato('Luan Lara', 11987577273, 'luanlaramoraes@gmail.com')
    contato2 = Contato('Nereu Augusto', 66996208927, 'nereubecker@gmail.com')
    contato3 = Contato('Julia Brito', 11927497457, 'juliabrito@hotmail.com')

    agenda = Agenda([])
    agenda.addlista(contato1)
    agenda.addlista(contato2)
    agenda.addlista(contato3)

    print("Agenda do André:")
    print(f'Contato 1 -> Nome: {agenda.contato[0].nome}, Número: {agenda.contato[0].numero}, Email: {agenda.contato[0].email}')
    print(f'Contato 2 -> Nome: {agenda.contato[1].nome}, Número: {agenda.contato[1].numero}, Email: {agenda.contato[1].email}')
    print(f'Contato 3 -> Nome: {agenda.contato[2].nome}, Número: {agenda.contato[2].numero}, Email: {agenda.contato[2].email}')

if __name__ == '__main__':
    main()