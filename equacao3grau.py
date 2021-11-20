# Resolver Equação de 3º Grau
from calcular import *

print("-"*10, "Entrada de Dados", "-"*10)
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))
d = float(input("Informe o valor de d: "))
x1 = float(input("Informe o valor de x1: "))

armazenarValores(a, b, c, d, x1)
calculaDelta(a, b, c, d, x1)
