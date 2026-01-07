import aula8.meu_modulo as meu_modulo


def test_saudacao():
    assert meu_modulo.saudacao("Ana") == "Olá, Ana!"


def test_soma():
    assert meu_modulo.soma(2, 3) == 5
