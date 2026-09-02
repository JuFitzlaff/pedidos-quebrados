from pedidos.frete import calcular_frete


def test_frete_normal():
    assert calcular_frete(100.0) == 15.0


def test_frete_express():
    assert calcular_frete(100.0, express=True) == 30.0


def test_frete_gratis_acima_do_limite():
    assert calcular_frete(350.0) == 0.0
