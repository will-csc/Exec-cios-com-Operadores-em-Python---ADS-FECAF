#---------- entrada ---------
qnt_valores = int(input("Digite a quantidade de valores que voce deseja verificar: \n"))
while qnt_valores < 1:
    print("\nDigite uma quantidade maior que 0")
    qnt_valores = int(input("Digite a quantidade de valores que voce deseja verificar: \n"))
    
cont = 0
valores = list()

while cont != qnt_valores:
    print("\nA contagem está em ",cont+1)
    valor = float(input("Digite o valor que você deseja: \n"))
    valores.append(valor)
    cont = cont + 1
    
#----------- processamento ------------
valores_negativos = list()
for num in valores:
    if num < 0:
        valores_negativos.append(num)

print("\nA quantidade de valores negativos é de ",len(valores_negativos))
print("Os números negativos dos valores repassados são: \n")
for num_neg in valores_negativos:
    print(num_neg)