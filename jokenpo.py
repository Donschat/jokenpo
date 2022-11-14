import random
import time
print('Vamos jogar um Jokenpô')
e=('pedra','papel','tesoura')
for c in range(0,3):
    usu=int(input('qual a sua jogada?\n[0]=pedra \n[1]=papel \n[2]=tesoura \n jogada: '))
    if(usu>2 or usu<0):
        print('jogada invalida')
    else:
        comp=random.randint(0,2)

        print('Jo')
        time.sleep(0.5)
        print('Ken')
        time.sleep(0.5)
        print('Pô')

        print('o jogador escolheu: \n\033[4;33m{}\033[m'.format(e[usu]))
        print('o com putador escolheu: \n\033[4;33m{}\033[m\n'.format(e[comp]))

        if usu==comp:
            print('\033[4;33mParece que temos um empate\033[m \n')
        elif usu==0 and comp==1:
            print('\033[31mQue pena, computador venceu \033[m\n')
        elif usu==0 and comp==2:
            print('\033[32mParabéns, voce venceu \033[m\n')
        elif usu==1 and comp==0:
            print('\033[32mParabéns, voce venceu\033[m \n')
        elif usu==1 and comp==2:
            print('\033[31mQue pena, computador venceu \033[m\n')
        elif usu==2 and comp==0:
            print('\033[31mQue pena, computador venceu\033[m \n')
        elif usu==2 and comp==1:
            print('\033[32mParabéns, voce venceu \033[m\n')
        else:
            print('Sua jogada é invalida \n')
print('FIM')

