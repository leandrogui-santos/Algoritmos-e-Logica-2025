sal_base_sem = 800
contagem_falhas = 0
soma_produtividade = 0

for i in range (5):
    p_dia = int(input("Informe a Pontuação de Produtividade Diária: "))
    if p_dia < 60:
        contagem_falhas = contagem_falhas + 1
        soma_produtividade = soma_produtividade + p_dia
    else:
        soma_produtividade = soma_produtividade + p_dia

produtividade_media = soma_produtividade / 5

if produtividade_media > 80 and contagem_falhas <= 1:
    print("Pagamento Máximo: Bônus de 10% aplicado.")
    pagamento_final = sal_base_sem * 1.10
elif produtividade_media >= 60 and produtividade_media <= 80 or contagem_falhas > 1:
    print("Pagamento Padrão: Penalidade de 5% aplicada (Devido a falhas).")
    pagamento_final = sal_base_sem * 0.95
else:
    print("Penalidade Severa: Pagamento reduzido em 25%.")
    pagamento_final = sal_base_sem * 0.75

print(f"Produtividade média: {produtividade_media}, quantidade de falhas: {contagem_falhas} e o pagamento final R${pagamento_final:.2f}.")