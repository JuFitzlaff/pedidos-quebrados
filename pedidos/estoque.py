import time


class Estoque:
    def __init__(self, quantidades):
        self._qtd = dict(quantidades)

    def disponivel(self, produto):
        return self._qtd[produto]

    def reservar(self, produto, qtd):
        if self._qtd[produto] >= qtd:
            time.sleep(0.01)  # latência do banco de dados
            self._qtd[produto] -= qtd
            return True
        return False

    def liberar(self, produto, qtd):
        self._qtd[produto] += qtd
