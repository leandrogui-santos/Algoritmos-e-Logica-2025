numero = int(input("Digite um número para ver a tabuada: "))

print (f"Tabuada do número {numero}.")

for fator in range(1,11):
    resultado = numero * fator
    print(f"{numero} x {fator} = {resultado}")