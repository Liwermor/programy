def main():
    for diamondSize in range(0,6):
        displayOutlineDiamond(diamondSize)
       # print()
        displayFilledDIamond(diamondSize)


def displayOutlineDiamond(size):
    for i in range(size):
        print(' ' * (size - i - 1),end='')#odstęp z lewej strony
        print('/', end='') #Lewa strona diamentu
        print(' ' * (i * 2), end='')
        print('\\') #Prawa strona diamentu

    for i in range(size):
        print(' ' * i,end='') #Odstęp z lewej
        print('\\',end='') # Lewa strona diameny
        print(' ' * ((size - i - 1) * 2),end='') #Srodek diamentu
        print('/') # prawa strona diamentu


def displayFilledDIamond(size):
    #Górna połowa diamenta
    for i in range(size):
        print(' ' * (size - i - 1),end='') # Odstęp z lewej
        print('/' * (i + 1), end='') #Lewa strona diamentu
        print('\\' * (i + 1)) # Prawa strona diamentu
    #Dolna połowa diamenta
    for i in range(size):
        print(' ' * i, end='')
        print('\\' * (size - i),end='') #Lewa strona diamentu
        print('/' * (size - i))

if __name__ == '__main__':
    main()
