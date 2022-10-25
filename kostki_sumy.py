from binascii import Incomplete
import random, time

#Deklaracja stałych

DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3 # -3 w celu zaoszczędzenia miejsca na dole dla pola do wprowadzania

#Czas trwania w sekundach
QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6

REWARD = 4 #Nagroda za poprawny wynik
PENALTY = 1 #Kara za złą odpowiedź


D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)
 
D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)
 
D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
 
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''Dodaj oczka wszystkich kości na ekranie. Masz {} sekund,
by podać jak największą liczbę odpowiedzi. Otrzymujesz {} punkty, za poprawną odpowiedż
tracisz {} punktów za złą odpowiedź.   '''.format(QUIZ_DURATION, REWARD, PENALTY))
input("Wciśnij enter aby rozpocząć")

correctAnswers = 0
incorrectAnswers  = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION:
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        dice = random.choice(ALL_DICE)
        #die[0] zawierta listę stringów przedstawiających grafiki kostek
        diceFaces.append(dice[0])
        #dice[1] zawiera inta reprezentującego liczbę oczek
        sumAnswer += dice[1]
    #tupla zawierająca (x, y) górnego rogu kostek
    topLeftDiceCorners = []
    #OKreślmy gdzie mna być kostka
    for i in range(len(diceFaces)):
        while True:
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)
            # znajdźmy koordynaty x,y każdego rogu
            #      left
            #      v
            #top > +-------+ ^
            #      | O     | |
            #      |   O   | DICE_HEIGHT (5)
            #      |     O | |
            #      +-------+ v
            #      <------->
            #      DICE_WIDTH (9)
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH 
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            #Sprawdź, czy kostki się nie nachodzą
            overlaps = False
            for prevDiceLeft, prevDiceTop in topLeftDiceCorners:
                prevDiceRight = prevDiceLeft + DICE_WIDTH
                prevDiceBottom = prevDiceTop + DICE_HEIGHT
                for cornerX, cornerY in ((topLeftX, topLeftY),
                                         (topRightX, topRightY),
                                         (bottomLeftX, bottomLeftY),
                                         (bottomRightX, bottomRightY)):
                    if (prevDiceLeft <= cornerX < prevDiceRight
                    and prevDiceTop <= cornerY < prevDiceBottom):
                        overlaps = True
            if not overlaps:
                topLeftDiceCorners.append((left, top))
                break
    canvas = {}
    for i, (diceLeft, diceTop) in enumerate(topLeftDiceCorners):
        diceFace = diceFaces[1]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                canvasX = diceLeft + dx
                canvasY = diceTop + dy
                canvas[(canvasX, canvasY)] = diceFace[dy][dx]
    
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '),end='')
        print()

    response = input("Podaj sume oczek: ").strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        print("Błędna odpowiedź, poprawna odpowiedź to ", sumAnswer)
        time.sleep(2)
        incorrectAnswers += 1
score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Poprawne odpowiedzi: ', correctAnswers)
print('Niepoprawne odp: ', incorrectAnswers)
print('Wynik: ',score)
