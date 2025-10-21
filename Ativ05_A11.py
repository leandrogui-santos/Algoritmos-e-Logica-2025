quant_nf = int(input("Informe a quantidade notas fiscais: "))

soma_das_notas = 0

for i in range (quant_nf):
    soma_das_notas = soma_das_notas + float(input("Informe o valor da NF: "))

if soma_das_notas < 1000:
    aliquota = 0.05
elif soma_das_notas >= 1000 and soma_das_notas < 5000:
    aliquota = 0.09
elif soma_das_notas >= 5000 and soma_das_notas < 15000:
    aliquota = 0.12
else:
    aliquota = 0.16

valor_imposto = soma_das_notas * aliquota

print(f"O valor total das é R${soma_das_notas:.2f}, a alíquota aplicada foi de {aliquota * 100}% e o valor do imposto a ser pago será R${valor_imposto:.2f}")