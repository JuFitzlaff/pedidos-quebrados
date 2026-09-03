from pedidos.frete import calcular_frete


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.total = 0.0

    def adicionar(self, produto, preco):
        self.itens.append((produto, preco))
        self.total += preco

    def listar_itens(self):
        return self.itens

    def frete(self):
        return calcular_frete(self.total)
