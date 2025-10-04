#Leandro Guilherme dos Santos
#RA 0220482523020
#Bora para o desafio!!! Em busca do 10!

print("Olá, Marcus! Meu nome é Leandro Santos, RA 0220482523020! Essa é a avaliação nº 07!")

pureza = float(input("Informe a pureza do lote em porcentagem (decimal): "))
massa = float(input("Informe a massa em KG: "))
taxa_cont = float(input("Informe a taxa de contaminação em porcentagem (decimal): "))

FD = (pureza * 100) - (taxa_cont * 50)

if massa > 1000:
    P_base = 10
else:
    P_base = 12.50

if FD > 90 and pureza > 0.98:
    print("Classificação: PREMIUM (Venda Imediata")
    P_final_kg = P_base * 1.50
elif FD >= 70 and FD <= 90 and taxa_cont < 0.05:
    print("Classificação: PADRÃO (Venda Normal)")
    P_final_kg = P_base * 1.10
elif FD < 70 or pureza < 0.90:
    print("Classificação: REPROVADO (Descarte ou Re-processamento")
    P_final_kg = P_base * 0.25
else:
    print("Classificação: ACEITÁVEL (Margem Mínima")
    P_final_kg = P_base * 0.90

Preco_Total_Final = P_final_kg * massa

print(f"O preço base por KG será R${P_base:.2f} e o Preço Final Total R${Preco_Total_Final:.2f}, considerando os parâmetros informados.")