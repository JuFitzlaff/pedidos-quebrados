import pytest

from praticas.cap5.parcelas import parcelar


def test_ca01_divisao_exata():
    assert parcelar(100.0, 4) == [25.0, 25.0, 25.0, 25.0]


def test_ca02_resto_nas_primeiras_parcelas():
    assert parcelar(100.0, 3) == [33.34, 33.33, 33.33]


def test_ca03_soma_igual_ao_total():
    for n in range(1, 13):
        assert round(sum(parcelar(199.99, n)) * 100) == 19999


def test_ca04_quantidade_invalida():
    with pytest.raises(ValueError):
        parcelar(100.0, 0)
    with pytest.raises(ValueError):
        parcelar(100.0, 13)
