def montar_pedido(cliente, itens):
    return {"cliente": cliente, "itens": itens}


def frete_do_pedido(pedido):
    if pedido["express"]:
        return 30.0
    return 15.0


def fechar_pedido(pedido):
    subtotal = sum(preco for _, preco in pedido["itens"])
    return subtotal + frete_do_pedido(pedido)


if __name__ == "__main__":
    pedido = montar_pedido("Ana", [("Mouse", 80.0)])
    print(fechar_pedido(pedido))
