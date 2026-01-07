# Python Exercicios 

Repositório com exercícios e explicações das aulas de Python do professor Guanabara.

---

## Sobre este repositório
Este repositório organiza material das aulas: explicações teóricas, exemplos executáveis e exercícios resolvidos.
O conteúdo principal foi reorganizado por aula para facilitar navegação e estudo.

### Estrutura (pastas na raiz)
- `aula8/` — **Conteúdo da Aula 8**: explicação (`aula8.md`), exemplos executáveis (`exemplos.py`) e módulos relacionados (`meu_modulo.py`, `bebidas.py`, `doce/`, etc.).
- `exercicios/` — **Exercícios resolvidos** (ex001 → ex015) — soluções e exercícios práticos das aulas.
- `tests/` — **Testes unitários** para os exemplos (`pytest`).
- `LICENSE` — arquivo de licença do repositório.
- `.gitignore` — padrões de arquivos/pastas ignorados pelo Git (ex.: `.venv/`, `.pytest_cache/`).

> Observação: para manter compatibilidade, alguns módulos podem ser importados via `aula8.*` (ex.: `aula8.meu_modulo`).

## Como executar
1. Rodar os exemplos da Aula 8:

```bash
python -m aula8.exemplos
```

2. Rodar os testes (recomenda-se usar um ambiente virtual):

```bash
pip install -r aula8/requirements.txt
python -m pytest -q
```

---

Se quiser, abra `aula8/aula8.md` para a explicação teórica ou `exercicios/README.md` para navegar pelos exercícios resolvidos.
