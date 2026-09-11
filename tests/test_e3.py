from pedidos.expresso import PedidoExpress
from pedidos.modelo import Pedido


def test_pedido_normal_tem_frete_base():
    p = Pedido("Ana")
    p.adicionar("Mouse", 80.0)
    assert p.frete() == 15.0


def test_express_aceita_itens():
    p = PedidoExpress("Carla", 24)
    p.adicionar("Monitor", 90.0)

    assert len(p.listar_itens()) == 1
    assert p.frete() == 30.0
