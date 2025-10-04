#Leandro Guilherme dos Santos
#RA 0220482523020
#Bora para o sexto! :)

print("Olá, Marcus! Meu nome é Leandro Santos, RA 0220482523020! Essa é a avaliação nº 06!")

print("Todos os valores informados na sequência devem ser em decimal, exemplo: 5% = 0.05!")

R_investimento = float(input("Informe o retorno do investimento: "))
R_livre = float(input("Informe a taxa livre de risco: "))
Sigma = float(input("Informe o desvio padrão da volatilidade: "))

if Sigma > 0:
    Sharp = (R_investimento - R_livre) / Sigma
else:
    print("O desvio padrão da volatilidade deve ser maior do que zero. Informe no campo abaixo novamente.")
    Sigma = float(input("Informe o desvio padrão da volatilidade: "))
    Sharp = (R_investimento - R_livre) / Sigma

Spread = R_investimento - R_livre

if Sharp > 1.5 and Spread > 0.05:
    print(f"O valor do Sharp Ratio Simples é {Sharp:.2f}. Investimento Excelente: Alta performance ajustada ao risco.")
elif Sharp >= 0.05 and Sharp <= 1.5 or Spread > 0.02:
    print(f"O valor do Sharp Ratio Simples é {Sharp:.2f}. Investimento Bom: Risco e retorno moderados.")
elif Sharp < 0.05 and R_investimento > 0:
    print(f"O valor do Sharp Ratio Simples é {Sharp:.2f}. Investimento Aceitável: Retorno positivo, mas risco alto para o ganho.")
else:
    print("Investimento Ruim: Não recomendado.")