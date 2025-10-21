custo_fixo = 500
custo_materia = float(input("Informe o custo da matéria prima por item: "))
custo_total_variavel = 0

for i in range (100):
    desperdicio = custo_materia * 0.05
    custo_total_variavel = custo_total_variavel + custo_materia + desperdicio

custo_total = custo_fixo + custo_total_variavel

if custo_total < 3000:
    margem = 0.35
elif custo_total >= 3000 and custo_total <= 5000:
    margem = 0.20
else:
    margem = 0.15

preco_minimo = (custo_total/100) * (1 + margem)

print(f"O custo total da produção é R${custo_total:.2f}, a margem de lucro aplicado é de {margem * 100}% e o preço mínimo de venda R${preco_minimo:.2f}.")