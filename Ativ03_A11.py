v_inicial = float(input("Informe o valor inicial do investimento: "))
meses = int(input("Simulação em quantos meses: "))

valor_acumulado = v_inicial
juros_totais = 0.00

for i in range (meses):
    taxa_cresc = float(input("Informe a porcentagem da Taxa de Crescimento Mensal (em decimais): "))
    if taxa_cresc > 0.015:
        juros = valor_acumulado * taxa_cresc
    elif taxa_cresc > 0.005 and taxa_cresc <= 0.015:
        juros = valor_acumulado * taxa_cresc * 0.9 #penalidade de 10%
    else:
        juros = 0
    valor_acumulado = valor_acumulado + juros
    juros_totais = juros_totais + juros

if juros_totais > (v_inicial * 0.10):
    print("Investimento de Alto Sucesso! (Retorno superior a 10%)")
else:
    print("Investimento Moderado. Retorno abaixo do esperado.")

print(f"O valor acumulado é R${valor_acumulado:.2f} e os juros totais ganhos R${juros_totais:.2f}.")