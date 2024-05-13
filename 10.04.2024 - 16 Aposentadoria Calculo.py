#--------- entrada -------------
import time
ano = int(time.strftime("%Y",time.localtime())) #ano de hoje

cod_func = int(input("Qual o codigo do funcionario?: \n"))
ano_func =  int(input("Qual o ano de nascimento do funcionario?: \n"))
ingresso_emp = int(input("Qual o ano que o funcionario entrou na empresa?: \n"))
idade_func = ano - ano_func

#---------- processamento -----------

while ingresso_emp > ano: # analisa se os dados digitados foram corretos
    print("\nO ano de ingresso na empresa esta maior do que o ano vigente")
    ingresso_emp = int(input("Qual o ano que o funcionario entrou na empresa?: \n"))
while ingresso_emp < 1:
    print("\nO ano de ingresso na empresa não é um ano valido")
    ingresso_emp = int(input("Qual o ano que o funcionario entrou na empresa?: \n"))
    
while idade_func < 14: # analisa se o ano de nascimento do funcionario
    print("\nO funcionario é muito novo, digite uma data de nascimento valida")
    ano_func =  int(input("Qual o ano de nascimento do funcionario?: \n"))
    idade_func =  ano - ano_func
while ano_func < 1:
    print("\nO ano de nascimento não é um ano valido")
    ano_func =  int(input("Qual o ano de nascimento do funcionario?: \n"))
    idade_func =  ano - ano_func

tempo_trab = ano - ingresso_emp

cond1 = bool(idade_func >= 65)
cond2 = bool(tempo_trab >= 30)
cond3 = bool(tempo_trab >= 35 or idade_func >= 60)

#---------------- saida ----------
if cond1 == True or cond2 == True or cond3 == True:
    print("\nO funcionario ",cod_func," deve se aposentar")
else:
    print("\nO funcionario ",cod_func," não deve se aposentar")