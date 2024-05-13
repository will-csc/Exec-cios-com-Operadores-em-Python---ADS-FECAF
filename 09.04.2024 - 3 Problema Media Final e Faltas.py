#-------------- entrada -----------
nome = str(input("Qual o nome do aluno?: "))

print("Digite as notas das 3 provas do aluno ",nome," em sequencia")
prova1 = int(input())
prova2 = int(input())
prova3 = int(input())

while prova1 < 0 or prova2 < 0 or prova3 < 0:
    print("Digite as 3 notas com numeros positivos")
    prova1 = int(input())
    prova2 = int(input())
    prova3 = int(input())

qnt_faltas = int(input("Qual a quantidade de faltas do aluno "+nome+"?: "))

while qnt_faltas < 0:
    print("Digite a quantidade de faltas com numeros positivos")
    qnt_faltas = int(input())

#------------ processamento -------------
media = float((prova1 + prova2 + prova3) / 3)
media =  float("{:.2f}".format(media))

situacao_aluno = True
#------------ saida ---------------
if qnt_faltas <  16:
    if media >= 6:
        print("O Aluno ",nome,"foi aprovado com uma média de ",media)
    elif media >=3 and media < 6:
        print("O Aluno ",nome,"ficou de recuperação com uma média de ",media)
    elif media < 3:
        print("O Aluno ",nome,"foi reprovado com uma média de ",media)
        situacao_aluno = False
        
else:
    print("O Aluno ",nome,"foi reprovado")
    situacao_aluno = False
    
if situacao_aluno == False:
    prova4 = int(input("O Aluno precisa fazer outra prova, Qual a nota do aluno na 4° prova?: "))
    media = float((prova1 + prova2 + prova3 + prova4) / 4)
    if media >= 6:
        print("O Aluno ",nome,"foi aprovado com uma média de ",media)
    else:
        print("O Aluno ",nome,"foi reprovado com uma média de ",media)
        
