import variables


def check_and_set_endgame():
    if variables.is_endgame == False:
        if len(variables.pakli) < variables.endgame_number:
            variables.is_endgame = True

            