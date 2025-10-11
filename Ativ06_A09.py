quant_alunos = int(input("Informe a quantidade de alunos: "))

soma_notas = float(input("Informe a primeira nota: "))

for i in range (quant_alunos-1):
    soma_notas = soma_notas + float(input("Informe a próxima nota: "))

media = soma_notas / quant_alunos

print(f"A média da turma é: {media:.1f}.")