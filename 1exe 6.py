n1 = float(input("Digite o primeiro valor (a): "))
n2 = float(input("Digite o segundo valor (b): "))
n3 = float(input("Digite o terceiro valor (c): "))

delta = n2 * n2 - 4 * n1 * n3

if n1 == 0:
    print("O valor de 'a' não pode ser 0 para uma equação de 2º grau.")

elif delta < 0:
    print("A equação não possui raízes reais.")

elif delta == 0:
    x1 = -n2 / (2 * n1)
    print(f"A equação tem uma raiz real dupla: x1 = {x1}")

else:  # delta > 0
    x1 = (-n2 + delta ** 0.5) / (2 * n1)
    x2 = (-n2 - delta ** 0.5) / (2 * n1)
    print(f"As raízes reais são: x1 = {x1}, x2 = {x2}")
