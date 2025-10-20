A = float(input("Digite o lado A: "))
B = float(input("Digite o lado B: "))
C = float(input("Digite o lado C: "))

if A < B + C and B < A + C and C < A + B:
    print("Os lados formam um triângulo.")

    if A == B == C:
        print("O triângulo é equilátero.")
    elif A == B or A == C or B == C:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os lados fornecidos não formam um triângulo.")
