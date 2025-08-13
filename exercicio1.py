print('Bem-vindo à loja da Milena Magno')
preco_unitario = float(input('Qual o valor unitario do produto?'))
quantidade = int(input('Qual a quantidade do produto?'))

preco2 = preco_unitario * quantidade
#Condicões para serem aplicados possíveis descontos
if(preco2 >= 2500 and preco2 < 6000):
    percentual = 4
    desconto = preco2 * (percentual / 100)
    preco_final = preco2 - desconto
    print(f'Valor total SEM desconto: {preco2}. Valor total COM desconto: {preco_final}.')

elif(preco2 >= 6000 and preco2 < 10000):
    percentual = 7
    desconto = preco2 * (percentual / 100)
    preco_final = preco2 - desconto
    print(f'Valor total SEM desconto: {preco2}. Valor total COM desconto: {preco_final}')

elif(preco2 >= 10000):
    percentual = 11
    desconto = preco2 * (percentual / 100)
    preco_final = preco2 - desconto
    print(f'Valor total SEM desconto: {preco2}. Valor total COM desconto: {preco_final}')

#Se não estiver de acordo com nenhuma alternativa acima, não será aplicado nenhum desconto.
else:
    print(f'Valor total SEM desconto: {preco2}. Valor total COM desconto: {preco2}')
#No final é informado ao cliente o valor bruto e depois o valor com o desconto já aplicado