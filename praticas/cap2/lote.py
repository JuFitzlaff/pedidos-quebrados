PEDIDOS = [
    {"cliente": "Cliente 01", "preco": 11.50, "qtd": 2},
    {"cliente": "Cliente 02", "preco": 12.50, "qtd": 3},
    {"cliente": "Cliente 03", "preco": 13.50, "qtd": 1},
    {"cliente": "Cliente 04", "preco": 14.50, "qtd": 2},
    {"cliente": "Cliente 05", "preco": 15.50, "qtd": 3},
    {"cliente": "Cliente 06", "preco": 16.50, "qtd": 1},
    {"cliente": "Cliente 07", "preco": 17.50, "qtd": 2},
    {"cliente": "Cliente 08", "preco": 18.50, "qtd": 3},
    {"cliente": "Cliente 09", "preco": 19.50, "qtd": 1},
    {"cliente": "Cliente 10", "preco": 20.50, "qtd": 2},
    {"cliente": "Cliente 11", "preco": 21.50, "qtd": 3},
    {"cliente": "Cliente 12", "preco": 22.50, "qtd": 1},
    {"cliente": "Cliente 13", "preco": 23.50, "qtd": 2},
    {"cliente": "Cliente 14", "preco": 24.50, "qtd": 3},
    {"cliente": "Cliente 15", "preco": 25.50, "qtd": 1},
    {"cliente": "Cliente 16", "preco": 26.50, "qtd": 2},
    {"cliente": "Cliente 17", "preco": 27.50, "qtd": 3},
    {"cliente": "Cliente 18", "preco": "28.50", "qtd": 2},
    {"cliente": "Cliente 19", "preco": 29.50, "qtd": 2},
    {"cliente": "Cliente 20", "preco": 30.50, "qtd": 3},
    {"cliente": "Cliente 21", "preco": 31.50, "qtd": 1},
    {"cliente": "Cliente 22", "preco": 32.50, "qtd": 2},
    {"cliente": "Cliente 23", "preco": 33.50, "qtd": 3},
    {"cliente": "Cliente 24", "preco": 34.50, "qtd": 1},
    {"cliente": "Cliente 25", "preco": 35.50, "qtd": 2},
    {"cliente": "Cliente 26", "preco": 36.50, "qtd": 3},
    {"cliente": "Cliente 27", "preco": 37.50, "qtd": 1},
    {"cliente": "Cliente 28", "preco": 38.50, "qtd": 2},
    {"cliente": "Cliente 29", "preco": 39.50, "qtd": 3},
    {"cliente": "Cliente 30", "preco": 40.50, "qtd": 1},
]


def total_do_pedido(pedido):
    return pedido["preco"] * pedido["qtd"]


def resumo_do_lote(pedidos):
    totais = []
    for pedido in pedidos:
        totais.append(total_do_pedido(pedido))
    return sum(totais)


if __name__ == "__main__":
    print(resumo_do_lote(PEDIDOS))
