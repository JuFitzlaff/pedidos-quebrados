from pedidos.modelo import Pedido


def test_adicionar_soma_no_total():
    p = Pedido("Ana")
    p.adicionar("Mouse", 80.0)
    assert p.total == 80.0


def test_total_confere_com_itens():
    p = Pedido("Ana")
    p.adicionar("Mouse", 80.0)

    itens = p.listar_itens()
    try:
        itens.clear()
    except AttributeError:
        pass  # devolver uma tupla também é uma solução válida

    assert len(p.listar_itens()) == 1
    assert p.total == 80.0
