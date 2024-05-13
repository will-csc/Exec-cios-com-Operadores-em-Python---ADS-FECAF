#---------- entrada ----------
import datetime

nome_prod = str(input("Qual o nome do produto: "))
descrição_prod = str(input("Qual a descrição do produto: "))
preço = round(float(input("Qual o preço do produto: ")),2)

ano = int(input("Qual o ano de validade: "))
mes = int(input("Qual o mes de validade: "))
dia = int(input("Qual o dia de validade: "))

#---------- processamento -------------
cond_data1 = bool(dia < 1 or dia > 31)
cond_data2 = bool(mes < 1 or mes > 12)
cond_data3 = bool(ano < 1)

if len(nome_prod) < 1:
    while len(nome_prod) < 1:
        print("\nCorrija o nome do produto, foram digitados poucos caracters")
        nome_prod = str(input("Qual o nome do produto: "))
if len(descrição_prod):
    while len(descrição_prod) < 1:
        print("\nCorrija a descrição do produto, foram digitados poucos caracters")
        descrição_prod = str(input("Qual a descrição do produto: "))
if preço < 1:
    while preço < 1:
        print("\nCorrija o preço do produto, o numero digitado foi menor que 1")
        preço = round(float(input("Qual o preço do produto: ")),2)
if cond_data1 == True:
    while cond_data1 == True:
        print("\nDigite um dia valido")
        dia = int(input("Qual o dia de validade: "))
        cond_data1 = bool(dia < 1 or dia > 31)
if cond_data2 == True:
    while cond_data2 == True:
        print("\nDigite um mes valido")
        mes = int(input("Qual o mes de validade: "))
        cond_data2 = bool(mes < 1 or mes > 12)
if cond_data3 == True:
    while cond_data3 == True:
        print("\nDigite um ano valido")
        ano = int(input("Qual o ano de validade: "))
        cond_data3 = bool(ano < 1)


validade = str(datetime.date(ano, mes, dia))

print("\nO produto ",nome_prod," com preço R$",preço,
      "\ne descrição: """,descrição_prod,"""| tem data de validade até """,validade)