quant_dias = int(input("Informe a quantidade de dias em que houve viagem: "))

total_km_percorridos = 0.0

for i in range (quant_dias):
    total_km_percorridos = total_km_percorridos + float(input("Informe os KM percorridos no dia: "))

total_litros = total_km_percorridos / 12
custo_total = total_litros * 4.80

if custo_total > 500:
    print("Alerta de Gastos: O custo total com combustível foi alto (Acima de R$ 500,00).")
else:
    print("Gastos sob controle: O custo total com combustível foi baixo ou moderado.")

print(f"Foram percorridos {total_km_percorridos:.2f} KM e o custo total com combustível foi de R${custo_total:.2f}.")