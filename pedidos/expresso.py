from pedidos.modelo import Pedido


class PedidoExpress(Pedido):
    def __init__(self, cliente, prazo_horas):
        self.prazo_horas = prazo_horas

    def frete(self):
        return super().frete() * 2
