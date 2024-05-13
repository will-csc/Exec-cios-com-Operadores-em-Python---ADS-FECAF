#------------ entrada -------------
qnt_eleitores = int(input("Digite a quantidade de eleitores: \n"))

qnt_brancos = int(input("Digite a quantidade de votos brancos: \n"))
qnt_nulos = int(input("Digite a quantidade de votos nulos: \n"))
qnt_validos = int(input("Digite a quantidade de votos validos: \n"))

#------------------ processamento ----------------
soma_votos = int(qnt_brancos + qnt_nulos + qnt_validos)
cond1 = bool(qnt_eleitores < 1 or qnt_brancos < 1 or qnt_nulos < 1 or qnt_validos < 1)
cond2 = bool(soma_votos > qnt_eleitores)
cond3 = bool(soma_votos < qnt_eleitores)

if cond1 == True or cond2 == True or cond3 == True: # analisa condições p/ correções
        
        if cond1 == True: #looping até os numeros serem positivos
            while cond1 == True:
                print("\nDigite numeros positivos e não nulos\n")
                qnt_eleitores = int(input("Digite a quantidade de eleitores: \n"))
                qnt_brancos = int(input("Digite a quantidade de votos brancos: \n"))
                qnt_nulos = int(input("Digite a quantidade de votos nulos: \n"))
                qnt_validos = int(input("Digite a quantidade de votos validos: \n"))
                cond1 = bool(qnt_eleitores < 1 or qnt_brancos < 1 or qnt_nulos < 1 or qnt_validos < 1)
        
        soma_votos = int(qnt_brancos + qnt_nulos + qnt_validos)
        cond2 = bool(soma_votos > qnt_eleitores)
        cond3 = bool(soma_votos < qnt_eleitores)
        
        if cond2 == True: #looping até as somas estarem certas
            while cond2 == True:
                print("A soma dos votos brancos,nulos e validos (total de",soma_votos,") \n",
                      "é maior do que a quantidade de eleitores(total de",qnt_eleitores,") \n",
                      "refaça até os valores de ambos serem iguais \n")
                qnt_brancos = int(input("Digite a quantidade de votos brancos: \n"))
                qnt_nulos = int(input("Digite a quantidade de votos nulos: \n"))
                qnt_validos = int(input("Digite a quantidade de votos validos: \n"))
                soma_votos = int(qnt_brancos + qnt_nulos + qnt_validos)
                cond2 = bool(soma_votos > qnt_eleitores)
            
        elif cond3 == True: #looping até as somas estarem certas
            while cond3 == True:
                print("A soma dos votos brancos,nulos e validos (total de",soma_votos,") \n",
                      "é menor do que a quantidade de eleitores(total de",qnt_eleitores,") \n",
                      "refaça até os valores de ambos serem iguais \n")
                qnt_brancos = int(input("Digite a quantidade de votos brancos: \n"))
                qnt_nulos = int(input("Digite a quantidade de votos nulos: \n"))
                qnt_validos = int(input("Digite a quantidade de votos validos: \n"))
                soma_votos = int(qnt_brancos + qnt_nulos + qnt_validos)
                cond3 = bool(soma_votos < qnt_eleitores)
       
#regra de 3 p/ descobrir o percentual
# 100 --- 100
# 80 --- x (multiplica cruzado)
perc_brancos = float((qnt_brancos*100)/qnt_eleitores)
perc_nulos = float((qnt_nulos*100)/qnt_eleitores)
perc_validos = float((qnt_validos*100)/qnt_eleitores)

#------------------ saida ----------------
print("O percentual de votos em branco foi de %",perc_brancos)
print("O percentual de votos nulos foi de %",perc_nulos)
print("O percentual de votos validos foi de %",perc_validos)