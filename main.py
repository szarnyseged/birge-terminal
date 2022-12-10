import variables
import game_start
import draw_card
import give
import strike
import computer.comp_strike_1, computer.comp_draw, computer.comp_give_1


hows_turn = game_start.game_start()

#main loop
while True:
    if hows_turn == 0:
        strike.player_strike()
        draw_card.player_draw()
        give.player_giving()
        draw_card.player_draw()
        if len(variables.player_cards) == 0:
            print("\n", "gratulálok, a játékos nyert!", sep="")
            break
        hows_turn = 1
    if hows_turn == 1:
        computer.comp_strike_1.comp_strike()
        computer.comp_draw.computer_draw()
        computer.comp_give_1.comp_giving()
        computer.comp_draw.computer_draw()
        if len(variables.computer_cards) == 0:
            print("\n", "a gép nyert, legközelebb több szerencséd lesz!", sep="")
            break
        hows_turn = 0

print("játék vége. akarsz újat játszani?")
