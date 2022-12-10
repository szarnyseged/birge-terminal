import utility
import variables


def player_giving():
    if len(variables.table) == 0 and variables.player_can_give and len(variables.player_cards) > 0:
        print("------------------")
        utility.print_player_hand()
        giving = get_giving_input()
        giving = convert_giving_input(giving)
        if giving_rules(giving):
            execute(giving)


def get_giving_input():
    giving_input = input("te adhatsz (nevezd meg a lapod, több esetén vesszővel elválasztva) \n").split(", ")
    return giving_input


def convert_giving_input(giving):
    """
    returns a list of objects
    """
    for index in range(len(giving)):
        for elem in variables.player_cards:
            if giving[index] == elem.name:
                giving[index] = elem
    return giving


#nem jó megoldás, rekurzív a return-ok miatt.
#de a rekurziós lánc csak jó input esetén tér vissza true-val,
#így az execute() csak egyszer fut le. utána más nem történik, ezért működik.
#megoldás lehet, ha a több inputhiba csekkolás csak true-false értékkel tér vissza,
# és az újabb func-t csak akkor hívjuk meg, ha az előző True.
def giving_rules(giving):
    #check for correct input
    try:
        for elem in giving:
            elem.name
    except AttributeError:
        print("elírtad a lap nevét, vagy nincs ilyen lapod (több esetén vesszővel kell elválasztani)")
        return player_giving()

    if len(giving) !=1 and len(giving) !=3 and len(giving) !=5:
        print("rosszul adtál, csak 1, 3 vagy 5 lapot adhatsz egyszerre")
        return player_giving()

    #3 és 5 lap adás. a halmaz csak egyszer tartalmazhatja ugyan azt az értéket,
    # ezért minden pár 1-el csökkenti a halmaz hosszát.
    # 3 lap esetén 1-nek pározni kell->halmaz hossza nem lehet több 2-nél.
    giving_set = set()
    for elem in giving:
        giving_set.add(elem.power)
    if len(giving) == 3:
        if len(giving_set) >2:
            print("rosszul adtál, 3 lap esetén kettőnek pároznia kell + kisérő")
            return player_giving()
    if len(giving)==5:
        if len(giving_set) >3:
            print("rosszul adtál, 5 lap esetén kettőnek-kettőnek pároznia kell + kisérő")
            return player_giving()

    #check for multiple same card
    giving_set = set()
    for elem in giving:
        print(elem.name)
    for elem in giving:
        giving_set.add(elem)
    if len(giving_set) != len(giving):
        print("egy lapot csak egyszer használhatsz fel!")
        return player_giving()
    else:
        return True


def execute(giving):
    for elem in giving:
        variables.table.append(elem)
        variables.player_cards.remove(elem)

