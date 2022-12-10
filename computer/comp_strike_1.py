import variables
import magyar_pakli
import utility
import computer.comp_utility


def comp_strike():
    """
    tactics: will always strike if possible, with the weakest card.
    """
    if len(variables.table) > 0:
        print("a gép következik")
        utility.print_comp_hand()

        variables.table = magyar_pakli.Lap.sort_strength(variables.table, variables.tromf)
        computer.comp_utility.check_and_set_endgame()
        comp_strike_cards = choose_all_strikes(variables.is_endgame)
        check_for_can_give(comp_strike_cards)
        execute(comp_strike_cards)


def choose_strike_card(strike_with, strike_to, is_endgame):
    """
    strike_with = list[]    \n
    strike_to = obj(Lap)    \n
    returns obj() the worst possible strike card(the most weak)  \n
    returns None if strike not possible
    """
    current_strike_cards = []
    if type(strike_with) is list:
        for comp_card in strike_with:
            is_stronger = magyar_pakli.Lap.is_stronger(comp_card, strike_to, variables.tromf)
            if is_stronger:
                if comp_card.color == variables.tromf:
                    if is_endgame == True:
                        current_strike_cards.append(comp_card)
                    else:
                        if comp_card.power < variables.strong_tromf:
                            current_strike_cards.append(comp_card)
                else:
                    current_strike_cards.append(comp_card)

        worst_strike_card = magyar_pakli.Lap.choose_worst_card(current_strike_cards, variables.tromf)
        return worst_strike_card
    else:
        return strike_with


def choose_all_strikes(is_endgame):
    """
    retruns a list of obj and None
    """
    copied_computer_card = variables.computer_cards.copy()
    comp_strike_cards = []
    for table_card in variables.table:
        strike_card = choose_strike_card(copied_computer_card, table_card, is_endgame)
        if strike_card != None:
            copied_computer_card.remove(strike_card)
        comp_strike_cards.append(strike_card)
    return comp_strike_cards


def check_for_can_give(comp_strike_cards):
    if None in comp_strike_cards:
        variables.comp_can_give = False
    else:
        variables.comp_can_give = True


def execute(comp_strike_cards):
    while len(variables.table) > 0:
        if comp_strike_cards[0] == None:
            print(f"a gép felvette: {variables.table[0].name}")
            variables.computer_cards.append(variables.table[0])
            variables.table.remove(variables.table[0])
            comp_strike_cards.remove(comp_strike_cards[0])
        else:
            print(f"a gép ütötte ezt: {variables.table[0].name} ezzel: {comp_strike_cards[0].name}")
            variables.deck_graveyard.append(variables.table[0])
            variables.deck_graveyard.append(comp_strike_cards[0])
            variables.computer_cards.remove(comp_strike_cards[0])
            variables.table.remove(variables.table[0])
            comp_strike_cards.remove(comp_strike_cards[0])

            
