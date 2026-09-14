# Especificação: Sistema de Gestão de Pedidos

## Feature: Reserva de estoque
RF-01  Uma reserva só é concluída se houver quantidade disponível
       no momento da confirmação.
RF-02  Duas reservas simultâneas do último item: exatamente uma é aceita.
RF-03  Pagamento recusado libera a reserva e informa o motivo ao cliente.

CA-01  Dado estoque SSD = 1, quando dois clientes reservam ao mesmo tempo,
       então uma reserva é aceita, a outra recusada, e o estoque final é 0.
CA-02  Dado um pedido reservado, quando o pagamento é recusado,
       então o estoque volta ao valor anterior à reserva.

## Feature: Pedido
RF-04  Um pedido novo começa sempre vazio, independentemente de outros pedidos.
RF-05  O total do pedido é sempre a soma dos preços dos seus itens.
RF-06  Um pedido expresso é um pedido: aceita itens e o frete é o dobro.

## Feature: Frete
RF-07  Frete grátis para subtotal a partir de R$ 200,00 (inclusive).

## Estações do laboratório
| Estação | Requisito | Teste                                         |
|---------|-----------|-----------------------------------------------|
| E1      | RF-04     | tests/test_e1.py::test_pedido_novo_comeca_vazio |
| E2      | RF-05     | tests/test_e2.py::test_total_confere_com_itens  |
| E3      | RF-06     | tests/test_e3.py::test_express_aceita_itens     |
| E4      | RF-03     | tests/test_e4.py::test_recusa_libera_estoque    |
| E5      | RF-02     | tests/test_e5.py::test_reserva_concorrente      |
