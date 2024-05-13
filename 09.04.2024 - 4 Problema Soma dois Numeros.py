# ------------- entrada -------------
print("Digite 3 numeros reais")
num1 = float(input())
num2 = float(input())
num3 = float(input())

#------------ processamento ---------
somadois_ult = num2 + num3

#----------- saida -----------
if somadois_ult > num1:
    print("A soma dos dois últimos numeros(", somadois_ult,") \né maior que",
           "o primeiro numero digitado (",num1,")")
elif somadois_ult < num1:
    print("A soma dos dois últimos numeros(", somadois_ult,") \né menor que",
           "o primeiro numero digitado (",num1,")")
else:
    print("A soma dos dois últimos numeros(", somadois_ult,") \né igual ",
           "o primeiro numero digitado (",num1,")")