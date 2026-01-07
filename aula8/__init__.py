"""Package da Aula 8 — agrupa módulos e exemplos sobre módulos e packages."""

# Exporta os utilitários mais usados para conveniência
from .meu_modulo import saudacao, soma
from .bebidas import listar_bebidas
# `fazer_pudim` está no subpackage `doce`
from .doce import fazer_pudim

__all__ = ["saudacao", "soma", "listar_bebidas", "fazer_pudim"]
