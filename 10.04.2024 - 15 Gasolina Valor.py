#------------ entrada ------------
tipo_combus = str(input("Escolha entre as opções de combustível, a que foi usada: \n"+
                        "G -> Gasolina | A -> Alcool\n")).upper()
litros_vend = float(input("Qual a quantidade de litros vendidas: \n"))

while litros_vend < 1:
    print("Digite um numero maior que 0")
    litros_vend = float(input("Qual a quantidade de litros vendidas: \n"))
while tipo_combus != 'G' and tipo_combus != 'A':
    print("Escolha uma opção correta")
    tipo_combus = str(input("Escolha entre as opções de combustível, a que foi usada: \n"+
                            "G -> Gasolina | A -> Alcool \n")).upper()

preco_g = 4.89
preco_a = 3.39

#----------- processamento -------------
if tipo_combus == "A":
    if litros_vend < 21:
        valor = preco_a * litros_vend
        preco_pagar = valor - (valor * 0.03)
    else:
        valor = preco_a * litros_vend
        preco_pagar = valor - (valor * 0.05)
elif tipo_combus == "G":
    if litros_vend < 21:
        valor = preco_g * litros_vend
        preco_pagar = valor - (valor * 0.04)
    else:
        valor = preco_g * litros_vend
        preco_pagar = valor - (valor * 0.06)

#----------- saida -------------
print("O valor deve à ser pago é de R$",round(preco_pagar,2))