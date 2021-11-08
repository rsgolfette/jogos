import forca
import jogocomfor

def escolhe_jogo():
    print("*****************************************")
    print("***Escolha o seu jogo!***")
    print("*****************************************")

    print("(1) Forca (2) Adivinhação")

    jogo= int(input("Qual jogo você quer jogar? "))

    if jogo ==1 :
        print("Jogando Forca")
        forca.jogar()
    elif jogo ==2 :
        print ("Jogando Adivinhação")
        jogocomfor.jogar()


if (__name__ == "__main__"):
    escolhe_jogo()