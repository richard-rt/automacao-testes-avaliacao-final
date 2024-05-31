def verficiaTriangulo(a, b, c):
    #  Testando se é triângulo
    if (a + b < c) or (a + c < b) or (b + c < a):
        return 'Nao é um triangulo'

    elif (a == b) and (a == c):
        return 'Equilatero'

    elif (a == b) or (a == c) or (b == c):
        return 'Isósceles'

    else:
        return 'Escaleno'
