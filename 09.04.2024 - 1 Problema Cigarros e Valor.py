#---------------- Entrada de dados ----------------
idade_usuario = int(input("Qual é a idade do usuário? : "))
inicio_fumar = int(input("Com qual idade ele começou a fumar: "))
qnt_cigarros_dia = int(input("Quantos cigarros o usuário fuma por dia? : "))
valor_maco = float(input("Qual o valor do maço de cigarros com 20? : "))

#-------------- Processamento ------------------
while (idade_usuario < 1):
    print("\nColoque uma idade valida para o usuario:")
    idade_usuario = int(input("Qual é a idade do usuário? : "))
while (inicio_fumar < 1 or inicio_fumar > idade_usuario):
    print("\nA idade em que o usuário começou a fumar não corresponde a uma data valida :")
    inicio_fumar = int(input("Com qual idade ele começou a fumar: "))
while valor_maco < 1:
    print("\nDigite um valor valido para o maço : \n")
    valor_maco = float(input("Qual o valor do maço de cigarros com 20? : "))
while qnt_cigarros_dia < 1:
    print("\nDigite uma quantidade valida de cigarros por dia :")
    qnt_cigarros_dia = int(input("Quantos cigarros o usuário fuma por dia? : "))
    


qnt_dias = (idade_usuario - inicio_fumar) * 365  # quantidade de dias que o usuário fumou
qnt_cigarros_necessaria = qnt_cigarros_dia * qnt_dias

qnt_macos = qnt_cigarros_necessaria // 20  # número exato de maços necessários

# Se houver cigarros restantes no último maço, adicione mais um maço
if qnt_cigarros_necessaria % 20 != 0:
    qnt_macos += 1

qnt_gasto = qnt_macos * valor_maco  # calcula o valor de maços comprados

#------------ saída ------------
print("\nO dinheiro gasto pelo usuário foi de ", qnt_gasto)