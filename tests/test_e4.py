from pedidos.checkout import finalizar
from pedidos.estoque import Estoque


def test_pagamento_aprovado_mantem_a_reserva():
    estoque = Estoque({"SSD": 5})
    pedido = {"produto": "SSD", "qtd": 1, "cartao": "ok"}

    assert finalizar(pedido, estoque) == "Pagamento aprovado"
    assert estoque.disponivel("SSD") == 4


def test_recusa_libera_estoque():
    estoque = Estoque({"SSD": 5})
    pedido = {"produto": "SSD", "qtd": 1, "cartao": "recusado"}

    assert finalizar(pedido, estoque) == "Pagamento recusado"
    assert estoque.disponivel("SSD") == 5
