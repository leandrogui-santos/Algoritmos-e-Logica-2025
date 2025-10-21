notas = int(input("Informe a quantidade de notas que serão inseridas: "))

soma_das_notas = 0.0

for i in range (notas):
    soma_das_notas = soma_das_notas + float(input("Informe o valor da nota: "))

if soma_das_notas <= 1000:
    aliquota = 0.05
elif soma_das_notas > 1000 and soma_das_notas < 5000:
    aliquota = 0.09
elif soma_das_notas >= 5000 and soma_das_notas <15000:
    aliquota = 0.12
else:
    aliquota = 0.16

valor_imposto = soma_das_notas * aliquota

print(f"O valor total das notas é R${soma_das_notas:.2f}, a alíquota aplicada (em %) foi de {aliquota} % e o valor total do imposto a ser pago é R${valor_imposto:.2f}")