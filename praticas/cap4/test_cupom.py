import pytest

from praticas.cap4.cupom import aplicar_cupom  # noqa: F401


def test_ca01_desconto_acima_do_minimo():
    # Dado um subtotal acima do mínimo e um cupom válido
    # Quando aplico o cupom
    # Então o resultado tem 10% de desconto
    raise NotImplementedError


def test_ca02_desconto_no_limite_do_minimo():
    # TODO: escreva você (o limite exato é um bom candidato a bug!)
    raise NotImplementedError


def test_ca03_sem_desconto_abaixo_do_minimo():
    raise NotImplementedError


def test_ca04_cupom_desconhecido_e_recusado():
    with pytest.raises(ValueError):
        raise NotImplementedError
