import threading

from pedidos.estoque import Estoque


def test_reserva_concorrente():
    estoque = Estoque({"SSD": 1})
    resultados = []

    def tarefa():
        resultados.append(estoque.reservar("SSD", 1))

    threads = [threading.Thread(target=tarefa) for _ in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert sorted(resultados) == [False, True]
    assert estoque.disponivel("SSD") == 0
