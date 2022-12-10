from random import randint, shuffle
import variables


def game_start():
    shuffle(variables.pakli)
    variables.tromf = randint(1,4)
    draw_cards()
    variables.how_start = randint(0,1)   ##0=player, 1=computer
    #variables.how_start = 0   #hardcoded for testing
    print_start()
    return variables.how_start
    

def print_start():
    if variables.how_start == 0:
        print("játékos kezd")
    elif variables.how_start == 1:
        print("gép kezd")

    if variables.tromf == 1:
        print("piros a tromf")
    elif variables.tromf == 2:
        print("tok a tromf")
    elif variables.tromf == 3:
        print("zold a tromf")
    elif variables.tromf == 4:
        print("makk a tromf")


def draw_cards():
    """
    draw 5 cards both player and computer
    """
    while len(variables.player_cards) <5:
        draw = variables.pakli[0]
        variables.player_cards.append(draw)
        variables.pakli.remove(draw)
        #sorbarendezés szinek szerint
        variables.player_cards.sort(key=lambda x: x.color)
    while len(variables.computer_cards) <5:
        draw = variables.pakli[0]
        variables.computer_cards.append(draw)
        variables.pakli.remove(draw)
        variables.computer_cards.sort(key=lambda x: x.color)


