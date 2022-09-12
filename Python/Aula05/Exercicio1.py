# 1
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def atualizarEstoque(self, produto, quantidade):
        self.estoque = produto.estoque - quantidade

    def __str__(self):
        preco = str(self.preco)
        estoque = str(self.estoque)
        return "Produto: " + self.nome + "; Estoque: " + estoque + "; Preço: R$" + preco

class Item:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Pedido:
    def __init__(self, item = [], pagamento = ''):
        self.item = []
        self.pagamento = pagamento

    def addlista(self, itemnovo):
        self.item.append(itemnovo)
    
    def pagar(self):
        print(f'A forma de pagamento escolhida foi: {self.pagamento}')

def main():
    produto1 = Produto('Doritos', 8.90, 34)
    produto2 = Produto('Fandangos', 10.9, 12)
    produto3 = Produto('Cheetos', 12.99, 25)

    print(produto1)
    print(produto2)
    print(produto3)
    print()

    item = []
    item1 = Item(produto1, 2)
    item2 = Item(produto2, 8)
    item3 = Item(produto3, 3)
    
    produto1.atualizarEstoque(produto1, 2)
    produto2.atualizarEstoque(produto2, 8)
    produto3.atualizarEstoque(produto3, 3)
    
    pedido1 = Pedido(item, 'Cartão')
    pedido1.addlista(item1)
    pedido1.addlista(item2)
    pedido1.addlista(item3)
    pedido1.pagar()

    # print(pedido1.item[0].produto.nome)  ---> Doritos
    
if __name__ == '__main__':
    main()