nota = float(input("Digite a nota: "))

parte_inteira = int(nota)
resto = nota - parte_inteira

if resto > 0.5:
    nota_arredondada = parte_inteira + 1
else:
    nota_arredondada = parte_inteira

print(f"Nota aproximada: {nota_arredondada:.1f}")
