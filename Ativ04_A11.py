meses = int(input("Informe o número de meses a serem avaliados: "))

consumo_total_kwh = 0
valor_total_pago = 0

for i in range (meses):
    consumo = float(input("Informe o consumo em kWh: "))
    if consumo <= 100:
        tarifa = 0.55
    elif consumo > 100 and consumo <= 200:
        tarifa = 0.70
    else:
        tarifa = 0.95
    custo_mensal = consumo_total_kwh * tarifa
    consumo_total_kwh = consumo_total_kwh + consumo
    valor_total_pago = valor_total_pago + custo_mensal

media_consumo = consumo_total_kwh / meses

if media_consumo > 180:
    print("Alerta! O consumo médio está elevado. Sugerir medidas de economia.")
else:
    print("Consumo médio dentro dos limites normais.")

print(f"Consumo total em kWh é {consumo_total_kwh:.2f} e o valor total pago foi de R${valor_total_pago:.2f}. Sua média de consumo em kWh é de {media_consumo:.2f}.")