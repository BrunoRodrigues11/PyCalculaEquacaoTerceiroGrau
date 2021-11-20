# Resolver Equação de 3º Grau
def armazenarValores(a, b, c, d, x1):
    global valores
    global results
    valores = []
    results = []
    valores.append(a)
    valores.append(b)
    valores.append(c)
    valores.append(d)
    valores.append(x1)


def calculaDelta(a, b, c, d, x1):
    # Atribuido variável soma1 -> a * raiz(x1) + b
    soma1 = a*x1+b

    # Atribuido variável soma2 -> soma1 * raiz(x1) + c
    soma2 = soma1 * x1 + c

    # Atribuido variável soma3 -> soma2 * raiz(x1) + d
    soma3 = soma2 * x1 + d

    print("")
    print("-"*10, "Equação de 3º Grau", "-"*10)
    # Representação da Equação de 3º Grau
    print(x1, "|", a, b, c, d)
    print("  |", a, soma1, soma2, soma3)

    print("")
    print("-"*10, "Equação de 2º Grau", "-"*10)
    # soma1 negativo e soma2 positivo
    if (soma1 < 0) and (soma2 > 0):
        print(
            "Equação: {}x² {}x + {} = {}".format(valores[0], soma1, soma2, soma3))
    # soma1 positivo e soma2 negativo
    elif (soma1 > 0) and (soma2 < 0):
        print(
            "Equação: {}x² + {}x {} = {}".format(valores[0], soma1, soma2, soma3))
    # soma1 e soma2 negativos
    elif (soma1 < 0) and (soma2 < 0):
        print("Equação: {}x² {}x {} = {}".format(
            valores[0], soma1, soma2, soma3))
    # soma1 e soma2 positivos
    else:
        print(
            "Equação: {}x² + {}x + {} = {}".format(valores[0], soma1, soma2, soma3))
    print("")

    #  soma1 negativo e soma2 positivo
    if (soma1 < 0) and (soma2 > 0):
        print("Δ = ({})² - (4 * {} * {})".format(soma1, valores[0], soma2))
    # soma1 positivo e soma2 negativo
    elif (soma1 > 0) and (soma2 < 0):
        print("Δ = {}² - (4 * {} * ({}))".format(soma1, valores[0], soma2))
    # soma1 e soma2 negativos
    elif (soma1 < 0) and (soma2 < 0):
        print("Δ = ({})² - (4 * {} * ({}))".format(soma1, valores[0], soma2))
    # soma1 e soma2 positivos
    else:
        print("Δ = {}² - (4 * {} * {})".format(soma1, valores[0], soma2))

    # Calculando o Delta1 -> valor de B (soma1) elevado ao quadrado
    delta1 = soma1*soma1
    # Calculando o Delta2 -> 4 * valor de A * C (soma2)
    delta2 = 4*valores[0]*soma2
    # Calculando o Delta3 -> valor do delta1 - valor do delta2
    delta3 = delta1-delta2

    # Delta1 negativo e Delta2 positivo
    if (delta1 < 0) and (delta2 > 0):
        print("Δ = ({}) - {}".format(delta1, delta2))
    # Delta1 positivo e Delta2 negativo
    elif(delta1 > 0) and (delta2 < 0):
        print("Δ = {} - ({})".format(delta1, delta2))
    # Delta1 e Delta2 negativos
    elif (delta1 < 0) and (delta2 < 0):
        print("Δ = ({})- ({})".format(delta1, delta2))
    # Delta1 e Delta2 positivos
    else:
        print("Δ = {} - {}" .format(delta1, delta2))

    if delta3 > 0:
        print("Δ = {}".format(delta3))
    else:
        print("Sem raizes reais.")

    x1 = valores[4]
    valorA = valores[0]
    div = 2 * valorA
    # Calculando a razi do delta
    raiz = delta3 ** 0.5

    # Verificando se o valor de B (soma1) é negativo
    if soma1 < 0:
        # Caso B (soma1) for negativo, ele será transformado em positivo
        # Seguindo a fórmula de Bhaskara, X = -b +- √Δ / 2*A
        soma1 = soma1 * -1
        somax2 = soma1 + raiz
        x2 = somax2 / div

        somax3 = soma1 - raiz
        x3 = somax3 / div
    # Verificando se o valor de B (soma1) é positivo
    elif soma1 > 0:
        # Caso B (soma1) for positivo, ele será transformado em negativo
        soma1 = soma1 * -1
        somax2 = soma1 + raiz
        x2 = somax2 / div

        somax3 = soma1 - raiz
        x3 = somax3 / div

    print("Raiz = {}".format(int(raiz)))
    print("")
    print("x = ({}) +- √{} / 2 * {}".format(soma1, delta3, valores[0]))
    print("x1 = ({}) + {} / {} = {}".format(soma1, raiz, div, x2))
    print("x2 = ({}) - {} / {} = {}".format(soma1, raiz, div, x3))
    print("")
    print("-"*10, "Resultado", "-"*10)
    results.append(x1)
    results.append(x2)
    results.append(x3)
    print("S = {}".format(sorted(results)))
    print("")
