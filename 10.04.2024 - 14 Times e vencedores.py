#------------- entrada -------------
print("Escreva o nome dos times que est√£o se enfrentando")
time1 = str(input())
time2 = str(input())

if time1.strip() == "" or time2.strip() == "": #verifica se o nome dos times estão vazios
    while time1.strip() == "" or time2.strip() == "":
        print("\nO nome dos times não podem estar vazios")
        print("Escreva o nome dos times que est√£o se enfrentando")
        time1 = str(input())
        time2 = str(input())

golstime1 = int(input("Escreva a quantidade de gols marcados pelo "+time1+": "))
golstime2 = int(input("Escreva a quantidade de gols marcados pelo "+time2+": "))
while golstime1 < 0 or golstime2 < 0:
    print("\nEscreva a quantidade de gols que nao seja negativa")
    golstime1 = int(input("Escreva a quantidade de gols marcados pelo "+time1+": "))
    golstime2 = int(input("Escreva a quantidade de gols marcados pelo "+time2+": "))

#------------- processamento e saida ---------------
if golstime1 > golstime2:
    print("Placar = ",time1," ",golstime1," x ",golstime2," ",time2," \n O(a) ",time1," saiu vencedor do duelo")
elif golstime1 < golstime2:
    print("Placar = ",time2," ",golstime2," x ",golstime1," ",time1," \n O(a) ",time2," saiu vencedor do duelo")
else:
    print("Placar =",time1," x ",time2," \n Os dois times empataram")