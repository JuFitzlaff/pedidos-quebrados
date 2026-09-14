# Feature: Parcelamento

## Requisitos
RF-01  `parcelar(total, n)` devolve uma lista com `n` valores em reais.
RF-02  `n` deve estar entre 1 e 12. Fora disso, levanta `ValueError`.
RF-03  A soma das parcelas é **exatamente** o total (em centavos).
RF-04  As parcelas diferem no máximo R$ 0,01 entre si. A diferença de
       centavos fica nas **primeiras** parcelas.

## Critérios de aceitação
CA-01  Dado total 100,00 e n = 4, então [25.0, 25.0, 25.0, 25.0].
CA-02  Dado total 100,00 e n = 3, então [33.34, 33.33, 33.33].
CA-03  Dado total 199,99 e qualquer n de 1 a 12, a soma é 199,99.
CA-04  Dado n = 0 ou n = 13, então ValueError.

## Invariante
A soma das parcelas nunca difere do total, para nenhum n válido.
