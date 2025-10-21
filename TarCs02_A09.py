numero = int(input("Digite um número para ver a tabuada: "))

print (f"Tabuada do número {numero}.")

#O programa executa uma ação até que se finalize a contagem informado
#Nesse caso, iniciamos a contagem em 1... ele irá executas os comandos dentro do FOR até chegar em 11
for fator in range(1,11):
    resultado = numero * fator
    print(f"{numero} x {fator} = {resultado}")