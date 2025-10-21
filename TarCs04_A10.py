dias = int(input("Informe a quantidade de dias analisados: "))

soma_das_temperaturas = 0

for i in range (dias):
    soma_das_temperaturas = soma_das_temperaturas + float(input("Informe a temperatura do próximo dia: "))

temp_media = soma_das_temperaturas / dias

if temp_media > 28:
    print("Média de temperatura: Clima Quente.")
elif temp_media > 18 and temp_media <= 28:
    print("Média de temperatura: Clima Agradável.")
else:
    print("Média de temperatura: Clima Frio.")

print(f"A média da temperatura é {temp_media:.1f}º.")