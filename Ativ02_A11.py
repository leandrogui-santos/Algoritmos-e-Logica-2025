quest = int(input("Informe o número de questões do quiz: "))

pontuacao_bruta = 0
erros_consecutivos = 0

for i in range (quest):
    pontuacao = float(input("Informe a pontuação obtida (entre 00.00 e 10.00): "))
    if pontuacao == 10.0:
        pontuacao_bruta = pontuacao_bruta + pontuacao   
        erros_consecutivos = 0
    elif pontuacao < 5:
        pontuacao_bruta = pontuacao_bruta + pontuacao
        erros_consecutivos = erros_consecutivos + 1
    else:
        pontuacao_bruta = pontuacao_bruta + pontuacao
        erros_consecutivos = 0

if pontuacao_bruta > 40 and erros_consecutivos == 0:
    print("Resultado Excelente! Bônus de 10% aplicado.")
    pontuacao_ajustada = pontuacao_bruta * 1.10
elif pontuacao_bruta < 20 or erros_consecutivos > 2:
    print("Resultado Fraco. Penalidade de 15% aplicada.")
    pontuacao_ajustada = pontuacao_bruta * 0.85
else:
    print("Resultado Padrão. Sem bônus ou penalidade.")
    pontuacao_ajustada = pontuacao_bruta

print(f"A pontuação bruta é {pontuacao_bruta:.2f} e a ajustada {pontuacao_ajustada:.2f}.")