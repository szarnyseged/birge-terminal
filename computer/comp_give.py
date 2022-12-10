import variables
import magyar_pakli


def comp_giving():
    if len(variables.table) == 0 and variables.comp_can_give and len(variables.computer_cards) > 0:
        print("------------------")
        print("a gép ad")
        comp_basic_give()


def comp_basic_give():
    """
    give 1 card always. for testing.
    """
    variables.table.append(magyar_pakli.Lap.choose_worst_card(variables.computer_cards, variables.tromf))
    variables.computer_cards.remove(magyar_pakli.Lap.choose_worst_card(variables.computer_cards, variables.tromf))


