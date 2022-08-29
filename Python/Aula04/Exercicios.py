# 1
class Produto:
    def __init__(self, nome, preco, estoque):
        self.preco = preco
        self.estoque = estoque
    

class Pedido:
    def __init__(self, item, pagamento):
        self.pagamento = pagamento