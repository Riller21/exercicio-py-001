nota_1 = float(input("Insira a primeira nota: "))

nota_2 = float(input("Insira a segunda nota: "))

nota_3= float(input("Insira a terceira nota: "))

média = (nota_1 + nota_2 + nota_3) / 3

if média > 10:
    print("valor inválido")
else:
    if média >= 7 and média < 10:
        print("Aprovado")
    elif média == 10:
        print("Aprovado com Distinção")
    else:
         print("Reprovado")