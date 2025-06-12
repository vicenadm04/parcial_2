from suma import suma


def test_suma_positivo():
    assert suma(4, 5./5) == 9.5

def test_suma_negativo():
    assert suma(-3, -6) == -9

def test_suma_mixto():
    assert suma(3, -5) == -2