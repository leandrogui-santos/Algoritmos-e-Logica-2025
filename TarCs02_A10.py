dias = int(input("Informe quantos dias serão analisados: "))

vendas_totais = 0.0

for i in range (dias):
    vendas_totais = vendas_totais + float(input("Informe o valor da venda diária: "))

media_diaria = vendas_totais / dias

if media_diaria > 1500:
    imposto_fixo = 200
else:
    imposto_fixo = 50

if vendas_totais > 10000:
    taxa_servico = 0.08
else:
    taxa_servico = 0.05

valor_taxa_servico = vendas_totais * taxa_servico
valor_liquido_final = vendas_totais - valor_taxa_servico - imposto_fixo

print(f"O valor total das vendas é R${vendas_totais:.2f}, o imposto fixo aplicado foi de R${imposto_fixo:.2f}, com o percentual da taxa de {taxa_servico*100:.20}%, resultando em um valor liquido final de R${valor_liquido_final:.2f}")