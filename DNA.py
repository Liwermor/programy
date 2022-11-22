import random, sys, time

PAUSE = 0.15

# To są pojednyncze wiersze animacji DNA:
ROWS = [
    #123456789 <- Użyj tego do zmierzenia liczby spacji:
    '         ##',  # Indeks 0 nie ma {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # Indeks 9 nie ma {}.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']
    # 123456789 <- Użyj tego do zmierzenia liczby spacji:

try:
    rowIndex = 0
    while True:
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0

        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()