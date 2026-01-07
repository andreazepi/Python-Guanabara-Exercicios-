import aula8.bebidas as bebidas


def test_listar_bebidas():
    lst = bebidas.listar_bebidas()
    assert isinstance(lst, list)
    assert "Água" in lst
