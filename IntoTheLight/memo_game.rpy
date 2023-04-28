#adapted from https://lemmasoft.renai.us/forums/viewtopic.php?t=18047
##### The game screen
screen memo_scr:
    ##### Timer

    timer 30.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose") ) repeat True
    bar value AnimatedValue(value=0, range=30, old_value=30, delay=30.0) xalign 0.5 xsize 500
    timer 1.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose") ) repeat True
    text str(memo_timer) xalign 0.5 yalign 0.05


    ##### Cards
    grid 3 4:
        xalign 0.5
        yalign 0.5
        spacing 5
        for card in cards_list:
            button:
                background None
                if card["c_chosen"]:        # shows the face of the card
                    text card["c_value"]
                else:                       # shows the back of the card
                    text "X"

                action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )

init:
    python:
        def cards_shuffle(x):
            renpy.random.shuffle(x)
            return x

label memory_game():
    #####
    # At first, let's set the cards to play (the amount should match the grid size - in this example 12)
    $ values_list = ["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C"]

    # Then - shuffle them
    $ values_list = cards_shuffle(values_list)

    # And make the cards_list that describes all the cards
    $ cards_list = []
    python:
        for i in range (0, len(values_list) ):
            cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )

    # Set the timer
    $ memo_timer = 30.0

    # Shows the game screen
    show screen memo_scr

    # The game loop
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []

        # Let's set the amount of cards that should be opened each turn (all of them should match to win)
        $ matchesNeeded = 2

        label turns_loop:
            if matchesNeeded > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                $ matchesNeeded -= 1
                jump turns_loop

        # To prevent further clicking before chosen cards will be processed
        $ can_click = False
        # If not all the opened cards are matched, will turn them face down after pause
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause (1.0, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False

        # If cards are matched, will check if player has opened all the cards
        else:
            $ renpy.pause (1.0, hard = True)
            python:
                # Let's remove opened cards from game field
                # But if you prefer to let them stay - just comment out next 2 lines
                for i in range (0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_value"] = Null()

                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("memo_game_loop")
                renpy.jump ("memo_game_win")
        jump memo_game_loop

label memo_game_lose:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    "You lose! Try again."
    jump memory_game

label memo_game_win:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    "You win!"
    return