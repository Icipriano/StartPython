# -*- CODING MARK: 13 -*-

#Exercicio 3
# -----------------------------------------

import math # OBTEMOS A BIBLIOTECA MATH, PARA EXTRAIRMOS A RAIZ QUADRADA
import time # OBTEMOS A BIBLIOTECA TIME, PARA COLOCAR A TELA DE CARREGAMENTO

print("\t APRENDENDO FAZER EQUAÇÕES EM PYHTON!!! \n")

print("\t PARA CONTINUAR, ESCOLHA UMA DAS SEGUINTES OPÇÕES: \n")

a = input("EQUAÇÕES DO 1º GRAU DIGITE 1 \n"
          "EQUAÇÕES DO 2º GRAU DIGITE 2 \n"
          "SAIR DIGITE SAIR \n")


if a == 'SAIR':
    print("\t CARREGANDO....\n")

    loop = 0
    time.sleep(1.2) #TEMPO DE CARREGAMENTO

    exit() #FECHOU O PROGRAMA


elif a == '1': #ENTRA NA 1º OPÇÃO
    print("\t CARREGANDO....\n") 

    loop = 0
    time.sleep(1.2)

    print("\t EQUAÇÕES DE 1º GRAU: \n")

    ax = input("DIGITE O VALOR DE A: ")
    b = input("DIGITE O VALOR DE B: ")
    c = input("DIGITE O VALOR DE C: ")

    resp = (float(b) - float(c)) / float(ax) #FORMULA

    if resp == '0':
        print("\t CALCULANDO....\n")

        loop = 0
        time.sleep(1.3)

        print("\t O VALOR DE X É NULO \n")


    else:
        print("\t CALCULANDO....\n")

        loop = 0
        time.sleep(1.3)

        print("\t O VALO DE X É:",resp," \n")


elif a == '2': #ENTRA NA 2º OPÇÃO
    print("\t CARREGANDO....\n")

    loop = 0
    time.sleep(1.2)

    print("\t EQUAÇÕES DE 2º GRAU: \n")

    ax2 = input("DIGITE O VALOR DE A: ")
    bx = input("DIGITE O VALOR DE B: ")
    c = input("DIGITE O VALOR DE C: ")


    delta = (float(bx) * float(bx)) - 4*float(ax2) * float(c) #DEFINE O VALOR DE DELTA

    if delta < 0:
        print("\t A EQUAÇÃO POSSUI APENAS UMA RESPOSTA REAL \n")

        x = (float(bx) * -1) / 2* float(ax2) #DEFINE O VALO DE X

        print("\t CALCULANDO....\n")

        loop = 0
        time.sleep(1.2)

        print("\t O VALOR DE X É:",X," \n")

    else:
        print("\t A EQUAÇÃO POSSUI DUAS RAIZES REAIS: \n")

        x1 = ((float(bx) * -1) + math.sqrt(delta)) / 2* float(ax2)
        x2 = ((float(bx) * -1) - math.sqrt(delta)) / 2* float(ax2)

        print("\t CALCULANDO....\n")

        loop = 0
        time.sleep(1.3)

        print("\t O VALOR DE X1 É:",x1," E DE X2 É:",x2," \n")