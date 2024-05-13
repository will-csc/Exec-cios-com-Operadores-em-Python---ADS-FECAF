#------------ entrada ------------
salario_fixo = float(input("Digite o salario fixo do vendedor: \n"))
vendas_realizadas = float(input("Digite o valor das vendas do vendedor: \n"))

#----------- processamento ----------
while salario_fixo < 1:
    print("Digite um salario positivo")
    salario_fixo = float(input())
while vendas_realizadas < 1:
    print("Digite o valor das vendas com numeros positivos")
    vendas_realizadas = float(input())

if vendas_realizadas < 1500:
    comissão_vendas = round(float(vendas_realizadas * 0.03),2)
else:
    comissão_vendas = round(float(vendas_realizadas * 0.05),2)
    
salario_total = salario_fixo + comissão_vendas

#---------- saida ----------
print("O vendedor vai receber um salario de R$",salario_total)
print("com um total de R$",comissão_vendas," em comissões")