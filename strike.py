import variables
import utility
import magyar_pakli


def player_strike():
    if len(variables.table) > 0:
        print("------------------")
        utility.print_player_hand()
        utility.print_table()
        strike = get_strike_input()
        strike = convert_strike_input(strike)
        if strike_rules(strike):
            check_for_can_give(strike)
            execute(strike)


def get_strike_input():
    strike_input = input("te következel, üss (nevezd meg mivel) vagy vedd fel (írd: felvesz)(sorrendben) \n").split(", ")
    return strike_input


def convert_strike_input(strike):
    """
    convert input into a list of objects
    """
    for index in range(len(strike)):
        for elem in variables.player_cards:
            if strike[index] == elem.name:
                strike[index] = elem
    return strike


#nem jó megoldás, rekurzív a return-ok miatt.
#de a rekurziós lánc csak jó input esetén tér vissza true-val,
#így az execute() csak egyszer fut le. utána más nem történik, ezért működik.
#megoldás lehet, ha a több inputhiba csekkolás csak true-false értékkel tér vissza,
# és az újabb func-t csak akkor hívjuk meg, ha az előző True.
def strike_rules(strike): 
    try:
        for elem in strike:
            if elem !="felvesz":
                elem.name
    except AttributeError:
        print("elírtad a lap nevét, vagy nincs ilyen lapod (több esetén vesszővel kell elválasztani)")
        return player_strike()

    #check card strength
    if len(variables.table) == len(strike):
        for index in range(len(variables.table)):
            if strike[index] !="felvesz" and magyar_pakli.Lap.is_stronger(strike[index], variables.table[index], variables.tromf) == False:
                print(f"a kivalasztott lapod ({strike[index].name}) nem üti az asztalon lévő lapot ({variables.table[index].name}) (sorrendben kell ütnöd)")
                return player_strike()
    else:
        print("minden lapra reagálnod kell")
        return player_strike()

    #check for multiple same card
    strike_set = set()
    number_of_felvesz = 0
    for elem in strike:
        if elem == "felvesz":
            number_of_felvesz +=1
        elif elem != "felvesz":
            strike_set.add(elem)
    if len(strike_set)+number_of_felvesz != len(strike):
        print("egy lapot csak egyszer használhatsz fel!")
        return player_strike()
    else:
        return True


def check_for_can_give(strike):
    if "felvesz" in strike:
        variables.player_can_give = False
    else:
        variables.player_can_give = True


def execute(strike):
    while len(variables.table) > 0:
        if strike[0] == "felvesz":
            variables.player_cards.append(variables.table[0])
            variables.table.remove(variables.table[0])
            strike.remove(strike[0])
        else:
            variables.deck_graveyard.append(strike[0])
            variables.deck_graveyard.append(variables.table[0])
            variables.player_cards.remove(strike[0])
            variables.table.remove(variables.table[0])
            strike.remove(strike[0])
        


