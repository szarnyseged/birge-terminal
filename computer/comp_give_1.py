import magyar_pakli
import variables
import utility
import computer.comp_utility
import copy



def comp_giving():
    if len(variables.table) == 0 and variables.comp_can_give and len(variables.computer_cards) > 0:
        print("------------------")
        print("a gép ad")
        computer.comp_utility.check_and_set_endgame()
        pairs = check_for_pairs(variables.computer_cards)
        if pairs != None:
            pairs = magyar_pakli.Lap.sort_strength(pairs, variables.tromf)
        if pairs == None:
            give_one()
        #change tactics here. need exclude or not?
        else:
            #give_three default
            if len(pairs) == 1 and len(variables.computer_cards) >= 3 and len(variables.player_cards) >= 3:
                companion = choose_companion(pairs)
                if companion.color == variables.tromf and companion.power > variables.strong_tromf and variables.is_endgame == False:
                    give_one()
                elif variables.is_endgame:
                    give_three_endgame(pairs, companion)
                else:
                    pairs = exclude_tromf(pairs, variables.tromf)
                    if len(pairs) < 1:
                        give_one()
                    else:
                        give_three_ordinary(pairs, companion)

            #give_five default
            elif len(pairs) >= 2 and len(variables.computer_cards) >= 5 and len(variables.player_cards) >= 5:
                pairs = exclude_tromf(pairs, variables.tromf)
                if len(pairs) < 1:
                    give_one()
                else:
                    companion = choose_companion(pairs)
                    # if variables.is_endgame:
                    #     give_five_endgame(pairs, companion)
                    if companion.color == variables.tromf and companion.power > variables.strong_tromf and variables.is_endgame == False:
                        if len(pairs) >= 2:
                            give_five_ordinary(pairs, companion)                                       
                        elif len(pairs) < 2:
                            give_three_ordinary(pairs, companion)

                    else:
                        if len(pairs) >= 2:
                            give_three_ordinary(pairs, companion)
                        elif len(pairs) < 2:
                            give_three_ordinary(pairs, companion)


def check_for_pairs(computer_cards):
    """
    check pairs in comp hand. \n
    returns a list of lists with pair objects\n
    returns None if there are no pairs. \n

    logic: check every card with every card. \n
        if the cards pairs store there indexes. \n
        store all of them in list(pairs) \n
    """


    def convert_to_obj(pairs):
    #convert pairs elements back to list of objs
        for index in range(len(pairs)):
            pairs[index] = list(pairs[index])
        for inner_list_i in range(len(pairs)):
            for inner_number_i in range(len(pairs[inner_list_i])):
                pairs[inner_list_i][inner_number_i] = computer_cards[pairs[inner_list_i][inner_number_i]]
        return pairs


    pairs = []
    for index in range(len(computer_cards)):
        one_card_pair_indexes = set()
        for inner_index in range(len(computer_cards)):
            #if the pair already exists in list(pairs), skip iteration.
            #use break flag to breakout 2 for loops and skip iteration.
            break_flag = False
            for pair in pairs:
                if index in pair or inner_index in pair:
                    break_flag = True
                    break
            if break_flag == False and index != inner_index:
                if computer_cards[index].power == computer_cards[inner_index].power:
                    one_card_pair_indexes.add(index)
                    one_card_pair_indexes.add(inner_index)
        if len(one_card_pair_indexes) > 0:
            pairs.append(one_card_pair_indexes)
    
    
    if len(pairs) == 0:
        return None
    pairs = convert_to_obj(pairs)
    return pairs


def exclude_tromf(pairs, tromf):
    """
    pairs: 2d list of objects \n
    returns cleared pairs excluded tromfs \n
    shouldn't give tromfs most of the time
    """
    if pairs != None:
        pairs_copy = copy.deepcopy(pairs)
        for inner_list_i in range(len(pairs_copy)):
            for one_obj_i in range(len(pairs_copy[inner_list_i])):
            # for one_obj in pairs[inner_list_i]:
                if pairs[inner_list_i][one_obj_i].color == tromf:
                    #can remove, cause only 1 can be tromf. only happen once
                    pairs[inner_list_i].remove(pairs[inner_list_i][one_obj_i])


        #clear pairs (if only 2 card pairs but 1 is tromf, then pairs must be cleared)
        helper_i = 0
        while helper_i < len(pairs):
            if len(pairs[helper_i]) < 2:
                del pairs[helper_i]
                helper_i -= 1
            helper_i += 1

        return pairs


def choose_worst_pair_index(pairs):
    """
    pairs: 2d list of pairs objects \n
    returns int(worst pair index) \n
    returns None if there are no pairs. \n
    """
    if pairs != None:
        worst_card = pairs[0][0]
        worst_card_pair_index = 0
        for inner_list_i in range(len(pairs)):
            for elem in pairs[inner_list_i]:
                if elem.power < worst_card.power:
                    worst_card = elem
                    worst_card_pair_index = inner_list_i
        return worst_card_pair_index


def give_one():
    """
    give 1 card only. depending on the gamestate. \n
    usually the worst one.
    """
    #ordinary tactics
    worst_card = magyar_pakli.Lap.choose_worst_card(variables.computer_cards, variables.tromf)
    variables.table.append(worst_card)
    variables.computer_cards.remove(worst_card)


def choose_companion(pairs):
    """
    choose the worst card for companion \n
    returns obj
    """
    #choose companion
    #choose worst pairs (why? even if it could give five, it is not always a good choice to do so)
    copied_computer_card = variables.computer_cards.copy()
    pairs_deep = copy.deepcopy(pairs)


    for _ in pairs:
        worst_card_pair_index = choose_worst_pair_index(pairs_deep)
        copied_computer_card.remove(pairs[worst_card_pair_index][0])    
        copied_computer_card.remove(pairs[worst_card_pair_index][1])
        pairs_deep[worst_card_pair_index].remove(pairs_deep[worst_card_pair_index][0])
        pairs_deep[worst_card_pair_index].remove(pairs_deep[worst_card_pair_index][0])
    worst_card = magyar_pakli.Lap.choose_worst_card(copied_computer_card, variables.tromf)
    return worst_card


def give_three_ordinary(pairs, companion):
    #pairs can be more then 1, so choose the worst pairs
    worst_card_pair_index = choose_worst_pair_index(pairs)
    #always gives the first pair occurence in pairs. (after sorted)
    variables.table.append(pairs[worst_card_pair_index][0])
    variables.table.append(pairs[worst_card_pair_index][1])
    variables.computer_cards.remove(pairs[worst_card_pair_index][0])
    variables.computer_cards.remove(pairs[worst_card_pair_index][1])
    variables.table.append(companion)
    variables.computer_cards.remove(companion)


def give_three_endgame(pairs, companion):
    worst_card_pair_index = choose_worst_pair_index(pairs)

    variables.table.append(pairs[worst_card_pair_index][0])
    variables.table.append(pairs[worst_card_pair_index][1])
    variables.computer_cards.remove(pairs[worst_card_pair_index][0])
    variables.computer_cards.remove(pairs[worst_card_pair_index][1])
    variables.table.append(companion)
    variables.computer_cards.remove(companion)


def give_five_ordinary(pairs, companion):
    #pairs can be more then 2, so choose the 2 worst pairs
    new_pairs = []
    for _ in range(2):
        worst_card_pair_index = choose_worst_pair_index(pairs)
        new_pairs.append(pairs[worst_card_pair_index])
        pairs.remove(pairs[worst_card_pair_index])

    variables.table.append(new_pairs[0][0])
    variables.table.append(new_pairs[0][1])
    variables.table.append(new_pairs[1][0])
    variables.table.append(new_pairs[1][1])
    variables.table.append(companion)
    variables.computer_cards.remove(new_pairs[0][0])
    variables.computer_cards.remove(new_pairs[0][1])
    variables.computer_cards.remove(new_pairs[1][0])
    variables.computer_cards.remove(new_pairs[1][1])
    variables.computer_cards.remove(companion)


def give_five_endgame(pairs, companion):
    #pairs can be more then 2, so choose the 2 worst pairs
    new_pairs = []
    for _ in range(2):
        worst_card_pair_index = choose_worst_pair_index(pairs)
        new_pairs.append(pairs[worst_card_pair_index])
        pairs.remove(pairs[worst_card_pair_index])

    variables.table.append(new_pairs[0][0])
    variables.table.append(new_pairs[0][1])
    variables.table.append(new_pairs[1][0])
    variables.table.append(new_pairs[1][1])
    variables.table.append(companion)
    variables.computer_cards.remove(new_pairs[0][0])
    variables.computer_cards.remove(new_pairs[0][1])
    variables.computer_cards.remove(new_pairs[1][0])
    variables.computer_cards.remove(new_pairs[1][1])
    variables.computer_cards.remove(companion)


"""
#old one
def give_three(pairs, is_endgame):
    #ordinary tactics
    worst_card = choose_companion(pairs)
    worst_card_pair_index = choose_worst_pair_index(pairs)
    #endgame tactics
    if worst_card.color == variables.tromf:
        if is_endgame:
            variables.table.append(pairs[worst_card_pair_index][0])
            variables.table.append(pairs[worst_card_pair_index][1])
            variables.computer_cards.remove(pairs[worst_card_pair_index][0])
            variables.computer_cards.remove(pairs[worst_card_pair_index][1])
            variables.table.append(worst_card)
            variables.computer_cards.remove(worst_card)
        else:
            if worst_card.power <  variables.strong_tromf:
                pass
    else:
        #always gives the first pair occurence in pairs. (after sorted)
        variables.table.append(pairs[worst_card_pair_index][0])
        variables.table.append(pairs[worst_card_pair_index][1])
        variables.computer_cards.remove(pairs[worst_card_pair_index][0])
        variables.computer_cards.remove(pairs[worst_card_pair_index][1])
        variables.table.append(worst_card)
        variables.computer_cards.remove(worst_card)


def give_five(pairs):
    #pairs can be more then 2, so choose the 2 worst pairs
    new_pairs = []
    for _ in range(2):
        worst_card_pair_index = choose_worst_pair_index(pairs)
        new_pairs.append(pairs[worst_card_pair_index])
        pairs.remove(pairs[worst_card_pair_index])

    #choose companion
    copied_computer_card = variables.computer_cards.copy()
    copied_computer_card.remove(new_pairs[0][0])
    copied_computer_card.remove(new_pairs[0][1])
    copied_computer_card.remove(new_pairs[1][0])
    copied_computer_card.remove(new_pairs[1][1])
    worst_card = magyar_pakli.Lap.choose_worst_card(copied_computer_card, variables.tromf)
    if worst_card.color == variables.tromf:
        if worst_card.power < variables.strong_tromf:
            variables.table.append(new_pairs[0][0])
            variables.table.append(new_pairs[0][1])
            variables.table.append(new_pairs[1][0])
            variables.table.append(new_pairs[1][1])
            variables.table.append(worst_card)
            variables.computer_cards.remove(new_pairs[0][0])
            variables.computer_cards.remove(new_pairs[0][1])
            variables.computer_cards.remove(new_pairs[1][0])
            variables.computer_cards.remove(new_pairs[1][1])
            variables.computer_cards.remove(worst_card)
        else:
            pass
    else:
        variables.table.append(new_pairs[0][0])
        variables.table.append(new_pairs[0][1])
        variables.table.append(new_pairs[1][0])
        variables.table.append(new_pairs[1][1])
        variables.table.append(worst_card)
        variables.computer_cards.remove(new_pairs[0][0])
        variables.computer_cards.remove(new_pairs[0][1])
        variables.computer_cards.remove(new_pairs[1][0])
        variables.computer_cards.remove(new_pairs[1][1])
        variables.computer_cards.remove(worst_card)
"""