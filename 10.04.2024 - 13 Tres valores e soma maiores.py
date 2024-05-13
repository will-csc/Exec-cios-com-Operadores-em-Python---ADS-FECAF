#---------------- entrada -----------------
print("Digite 3 valores")
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

#------------ processamento ----------
menor = int(min(valor1, valor2, valor3))
soma = int(valor1 + valor2 + valor3)
soma_dois_maiores = int(soma - menor)

#---------- saida -----------
print("A soma dos dois maiores numeros é de :",soma_dois_maiores)
        