import variables


def player_draw():
    while len(variables.player_cards) <5 and len(variables.pakli) > 0:
        draw = variables.pakli[0]
        variables.player_cards.append(draw)
        variables.pakli.remove(draw)
        sort_hand()
        deck_warning()


def deck_warning():
    if variables.is_warned == False:
        if len(variables.pakli)<1:
            print("!a pakli elfogyott!")
            variables.is_warned = True
        elif len(variables.pakli)<8:
            print("!még", len(variables.pakli), "lap van a pakliban!")


def sort_hand():
    """
    sorbarendezés szinek szerint átláthatóság kedvéért
    """
    variables.player_cards.sort(key=lambda x: x.color)

