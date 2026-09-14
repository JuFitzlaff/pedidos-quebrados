# pedidos-quebrados

Sistema de Gestão de Pedidos da **TechPedidos**, com erros propositais.
Material da aula da disciplina *Linguagem de Programação e Paradigmas* (UNIDAVI).

## Preparar o ambiente
```
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q                      # 5 failed, 7 passed
```

## Estrutura
- `pedidos/`  sistema (cinco estações com erro: E1 a E5)
- `tests/`    testes do sistema
- `praticas/` exercícios dos capítulos da aula
- `specs/`    especificações (leia antes de depurar)
- `CLAUDE.md` regras para o agente de IA

Não corrija as estações antes do laboratório.
