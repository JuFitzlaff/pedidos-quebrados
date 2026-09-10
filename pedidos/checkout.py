class PagamentoRecusado(Exception):
    pass


def cobrar(pedido):
    if pedido["cartao"] == "recusado":
        raise PagamentoRecusado("cartão recusado")


def finalizar(pedido, estoque):
    estoque.reservar(pedido["produto"], pedido["qtd"])
    try:
        cobrar(pedido)
        return "Pagamento aprovado"
    except Exception:
        return "Erro inesperado"
    except PagamentoRecusado:
        estoque.liberar(pedido["produto"], pedido["qtd"])
        return "Pagamento recusado"
