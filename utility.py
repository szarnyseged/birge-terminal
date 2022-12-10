import variables


def print_player_hand():
    if len(variables.pakli < 1):
        print(f"a te lapjaid:  (a pakli elfogyott!)")
        for elem in variables.player_cards:
            print("    ", elem.name)
    else:
        print(f"a te lapjaid:  (még {len(variables.pakli)} lap van a pakliban)")
        for elem in variables.player_cards:
            print("    ", elem.name)
    print()


def print_comp_hand():
    print("gép lapjai: ")
    for elem in variables.computer_cards:
        print("    ", elem.name)
    print()


def print_table():
    print("az asztalon:")
    for elem in variables.table:
        print("    ", elem.name)

