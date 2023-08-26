from PIL import Image
import random
import os

numbers = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

suits = ["clubs", "diamonds", "hearts", "spades"]

generated = []

while True:
    input()

    n = random.randint(0, 12)
    s = random.randint(0, 3)

    card = numbers[n] + '_of_' + suits[s] + '.png'

    while card in generated:
            n = random.randint(0, 12)
            s = random.randint(0, 3)

            card = numbers[n] + '_of_' + suits[s] + '.png'

    print("Opening " + numbers[n] + " of " + suits[s])

    generated.append(card)
    
    cardfile = os.path.join(os.getcwd(), 'images', card)
    with Image.open(cardfile) as img:
        img.show()

