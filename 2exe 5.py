total_salarios = 0

while True:
    salario_bruto = float(input("\nDigite o salário bruto (ou 0 para encerrar): "))
    if salario_bruto == 0:
        break

    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

    if salario_bruto < 800:
        desconto = 0
    elif salario_bruto <= 1600:
        desconto = salario_bruto * (0.08 + 0.05)
    else:
        desconto = salario_bruto * (0.15 + 0.07)

    salario_liquido = salario_bruto - desconto

    if horas_trabalhadas > 160:
        valor_hora = salario_bruto / 160
        horas_excedentes = horas_trabalhadas - 160
        adicional = horas_excedentes * valor_hora * 0.5
        salario_liquido += adicional

    print(f"Salário líquido: R$ {salario_liquido:.2f}")
    total_salarios += salario_liquido

print(f"\nTotal geral dos salários líquidos: R$ {total_salarios:.2f}")
