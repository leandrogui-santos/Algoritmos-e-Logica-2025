quant_prod = int(input("Informe a quantidade de produtos: "))

total_compra = float(input("Informe o valor do primeiro produto: "))

for i in range (quant_prod-1):
    total_compra = total_compra + float(input("Informe o valor do próximo produto: "))

print(f"O valor total da compra é R${total_compra:.2f}")