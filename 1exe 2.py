nota1= float(input("Digite a primeira nota:"))
nota2= float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
media = (nota1 + nota2 + nota3) /3

if media >=6:

    print("Aprovado ´%f'" %(media))

else :

    nx=(float(input("Entre com a nota de exame:")))

    media= media+ nx

    if media>=5:

        print("Aprovado")

    else:

            print("Reprovado")