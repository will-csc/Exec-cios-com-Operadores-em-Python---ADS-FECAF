#-------------- entrada ------------------
produto = str(input("Qual o nome do produto?: \n"))
qnt_estoque = int(input("Qual a quantidade em estoque do "+produto+": \n"))
qnt_estoque_max = int(input("Qual a quantidade maxima do estoque do "+produto+": \n"))
qnt_estoque_min = int(input("Qual a quantidade minima do estoque do "+produto+": \n"))

#----------- processamento e saida -------------
while len(produto) < 2 or produto.strip() == "":
    print("\nDigite um nome valido, que nao seja vazio ou pequeno demais")
    produto = str(input())
while qnt_estoque < 1 or qnt_estoque_max < 1 or qnt_estoque_min < 1:
    print("\nDigite as quantidades em estoque com valores positivos")
    qnt_estoque = int(input("Qual a quantidade em estoque do "+produto+": \n"))
    qnt_estoque_max = int(input("Qual a quantidade maxima do estoque do "+produto+": \n"))
    qnt_estoque_min = int(input("Qual a quantidade minima do estoque do "+produto+": \n"))

qnt_media = int((qnt_estoque_max +  qnt_estoque_min)/2)

if qnt_estoque >= qnt_media:
    print("O ",produto," não precisa ser comprado")
else:
    print("O ",produto," precisa ser comprado")