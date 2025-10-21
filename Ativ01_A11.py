cont = int(input("Informe um número positivo: "))

soma_dos_quadrados = 0

for i in range (cont+1):
    quadrado = i **2
    if quadrado % 3 == 0:
        print(f"{quadrado} é multiplo de 3")
    elif quadrado % 2 == 0:
        print(f"{quadrado} é par")
        soma_dos_quadrados = soma_dos_quadrados + quadrado
    else:
        print(f"{quadrado} é ímpar. Ignorado.")

print(f"A soma dos quadrados é {soma_dos_quadrados}.")