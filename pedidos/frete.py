FRETE_BASE = 15.0
LIMITE_FRETE_GRATIS = 200.0


def calcular_frete(subtotal, express=False):
    """Frete grátis a partir de R$ 200,00 (inclusive). Express custa o dobro."""
    if subtotal >= LIMITE_FRETE_GRATIS:
        return 0.0
    return FRETE_BASE * 2 if express else FRETE_BASE
