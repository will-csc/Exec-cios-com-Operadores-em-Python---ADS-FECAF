#-------------- entrada -------------
qnt_desejada = int(input("Digite a quantidade de valores desejada para iterações: \n"))+1
while qnt_desejada < 1:
    print("Digite uma quantidade acima de 1")
    qnt_desejada = int(input("Digite a quantidade de valores desejada para iterações: \n"))+1
    
numeros_digitados = list()
soma = float()

for i in range(1,qnt_desejada):
    print("\nA contagem está em ",i)
    num = float(input("Digite um valor: \n"))
    numeros_digitados.append(num)
    
#------------ processamento -------------
for num in numeros_digitados:
    soma = soma + num

#------------ saida ---------------
print("\nA soma é de todos os numeros digitados é de ",soma)