#-------------- entrada ---------------
num_tabuada = int(input("Digite o numero que você deseja ver a tabuada: "))

#---------- processamento e saída ------------
for num in range(1,11):
    num_process = int(num_tabuada * num)
    print(num_tabuada," x ",num," = ",num_process," \n")

