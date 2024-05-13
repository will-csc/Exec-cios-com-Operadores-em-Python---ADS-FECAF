#------------ entrada --------------
soma = 0
opção = str(input("Digite Y para mudar valores de alcance, inicio e encerramento da soma"+
                  "\nDigite qualquer outro para deixar valores padrões de alcance, inicio=0 fim=100 \n")).upper()

if opção.strip() == "Y" or "y":
    pri_numero = int(input("Digite um numero p/ iniciar: "))
    ult_numero = int(input("Digite um numero p/ encerrar: "))+1
    if ult_numero <= pri_numero:
        while ult_numero <= pri_numero:
            print("Digite um numero p/ encerrar que seja maior que o de inicio")
            ult_numero = int(input("Digite um numero p/ encerrar: "))+1
else:
    pri_numero = 0
    ult_numero = 100

for i in range(pri_numero,ult_numero):
    soma = int(i + soma)

print("a soma dos numeros de",pri_numero," a ",ult_numero-1," é de", soma)