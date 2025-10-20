n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

numeros = [n1, n2, n3]
numeros.sort()

print(f"Menor número: {numeros[0]}")
print(f"Número do meio: {numeros[1]}")
print(f"Maior número: {numeros[2]}")
