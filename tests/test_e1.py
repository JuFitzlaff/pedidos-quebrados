from pedidos.criacao import novo_pedido


def test_pedido_guarda_o_cliente():
    assert novo_pedido("Ana")["cliente"] == "Ana"


def test_pedido_novo_comeca_vazio():
    p1 = novo_pedido("Ana")
    p1["itens"].append("Teclado")

    p2 = novo_pedido("Bruno")

    assert p2["itens"] == []
