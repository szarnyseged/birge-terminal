import magyar_pakli


#global variables
player_cards = []
computer_cards = []
table = []
tromf = None
pakli = magyar_pakli.Lap.pakli
how_start = None    #0=player, 1=computer
player_can_give = True
comp_can_give = True
is_warned = False
strong_tromf = 10
endgame_number = 3 #length of the deck where endgame tactics start
is_endgame = False
deck_graveyard = [] #for advanced comp tactics


def set_to_default():
    """
    set variables to default
    """

    global player_cards
    global computer_cards
    global table
    global tromf
    global pakli
    global how_start
    global player_can_give
    global comp_can_give
    global is_warned
    global strong_tromf
    global endgame_number
    global is_endgame
    global deck_graveyard
    
    player_cards = []
    computer_cards = []
    table = []
    tromf = None
    pakli = magyar_pakli.Lap.pakli
    how_start = None    #0=player, 1=computer
    player_can_give = True
    comp_can_give = True
    is_warned = False
    strong_tromf = 10
    endgame_number = 3 #length of the deck where endgame tactics start
    is_endgame = False
    deck_graveyard = []
