from app.primeiroExercicio import triangulo


def test_nao_e_triangulo():
    assert triangulo.verficiaTriangulo(1, 1, 3) == "Nao é um triangulo"
    assert triangulo.verficiaTriangulo(3, 3, 3) == "Equilatero"
    assert triangulo.verficiaTriangulo(2, 1, 2) == "Isósceles"
    assert triangulo.verficiaTriangulo(8, 7, 5) == "Escaleno"