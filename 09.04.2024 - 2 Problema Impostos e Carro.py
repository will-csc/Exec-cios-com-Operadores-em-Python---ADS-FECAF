#-------------- entrada de dados ----------
preco_carro = int(input("Qual o valor do carro? :"))
while preco_carro < 1:
    print("Digite um preço valido para o carro")
    preco_carro = int(input())

#------------ processamento ---------------
valorpago_imp = preco_carro * 0.45
custo_carro = valorpago_imp + preco_carro

lucro = custo_carro * 0.12

#------------ saida -------------
print("O distribuidor pagou um total de R$",valorpago_imp," em imposto \n",
      "aumentando o preço do carro para R$", custo_carro,
      "\n oque levou à um lucro de R$", lucro)


