#Leandro Guilherme dos Santos
#RA 0220482523020
#Bora para o quinto! :)

print("Olá, Marcus! Meu nome é Leandro Santos, RA 0220482523020! Essa é a avaliação nº 05!")

C_inicial = float(input("Informe o custo inicial: "))
Q = int(input("Informe a quantidade de itens produzidos: "))
Dias = int(input("Quantos dias de atraso? "))
Defeito = float(input("Informe o percentual de defeitos (em decimal): "))

if Q > 1000 and C_inicial > 5000:
    F_comp = 1.15
else:
    F_comp = 1.05

C_corrigido = C_inicial * F_comp

if Defeito > 0.10 or Dias > 5:
    print("Penalidade Alta: 20% de redução no lucro.")
    C_final = C_corrigido * 1.25
elif Defeito >= 0.05 and Defeito <= 0.10 and Dias> 0:
    print("Penalidade Média: 10% de redução no lucro.")
    C_final = C_corrigido * 1.10
else:
    print("Sem penalidade. Custo final apenas com correção.")
    C_final = C_corrigido

print(f"O Custo Base Corrigido é R${C_corrigido:.2f} e o custo final do lote R${C_final:.2f}.")