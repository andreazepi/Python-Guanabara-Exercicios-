"""Exemplos executáveis para a Aula 8: Módulos e Packages
Este arquivo contém funções de exemplo e pode ser executado:

python -m aula8.exemplos
"""

import aula8
from aula8 import saudacao
import aula8.bebidas as bebidas
from aula8 import fazer_pudim


def exemplo_saudacao_e_soma():
    nome = "Maria"
    print(aula8.saudacao(nome))
    print(saudacao("João"))
    print(f"A soma de 5 e 7 é: {aula8.soma(5, 7)}")


def exemplo_bebidas():
    print("Bebidas disponíveis:", bebidas.listar_bebidas())


def exemplo_pudim_como_package():
    print(fazer_pudim())
    import aula8.doce.pudim as pudim_mod
    print(pudim_mod.fazer_pudim())


if __name__ == "__main__":
    print("Executando exemplos da Aula 8 (módulos e packages):\n")
    exemplo_saudacao_e_soma()
    print()
    exemplo_bebidas()
    print()
    exemplo_pudim_como_package()
    print("\nFim dos exemplos.")
