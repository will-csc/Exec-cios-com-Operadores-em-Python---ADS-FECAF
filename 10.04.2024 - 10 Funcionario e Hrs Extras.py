#---------- entrada ----------
nome_func = str(input("Digite o nome do funcionario: \n"))
horas_trab = float(input("Digite as horas trabalhas pelo "+nome_func+"(apos a virgula = % em minutos): \n"))
valor_hr = float(input("Qual o valor da hora do funcionario "+nome_func+": \n"))

#--------- processamento e saida ---------
while nome_func.strip() == "" and len(nome_func) < 2:
    print("Escreva um nome valido")
    nome_func = str(input())
while horas_trab < 1:
    print("Escreva uma hora positiva do funcionario")
    horas_trab = float(input())
while valor_hr < 1:
    print("Escreva uma valor positivo para hora do funcionario")
    valor_hr = float(input())

#conversão das horas em minutos para que o calculo das horas seja mais correto
min_trab = float(horas_trab * 60)
valor_min = float(valor_hr / 60)

if horas_trab > 40:
    extras = round(float((valor_min * min_trab) * 0.50),2)
    salario = round(float(extras + (valor_min * min_trab)),2)
else:
    salario =  round(float(valor_min * min_trab),2)
    
print("O funcionario ",nome_func," vai receber R$",salario)
if extras > 0:
    print("Com um total de R$",extras," referente a horas extras")
