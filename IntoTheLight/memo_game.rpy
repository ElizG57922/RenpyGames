# Adapted from https://lemmasoft.renai.us/forums/viewtopic.php?t=18047

screen memo_scr:
    zorder 100
    timer memo_timer_full action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose") ) repeat True
    bar value AnimatedValue(value=0, range=memo_timer_full, old_value=memo_timer_full, delay=memo_timer_full) xalign 0.5 yalign 0.15 xsize 500
    timer 1.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose") ) repeat True
    text str(memo_timer) xalign 0.5 yalign 0.3

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
    textbutton "Click this to skip if you don't like memory games :)" action Jump("memo_game_win") yalign 0.6

init:
    python:
        def cards_shuffle(x):
            renpy.random.shuffle(x)
            return x

label memory_game():
    # Make the cards
    $ values_list = ["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C"]

    # Shuffle cards
    $ values_list = cards_shuffle(values_list)

    $ cards_list = []
    python:
        for i in range (0, len(values_list) ):
            cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )

    # Set the timer
    $ memo_timer_full = 30
    $ memo_timer = memo_timer_full

    # Shows the game screen
    show screen memo_scr

    # The game loop
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []

        # Set the amount of cards that should be opened each turn
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
                # Remove opened cards from game field
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
    "The man in charge of the table sweeps a hand over the cards, informing you that you have run out of time. You walk away empty handed, knowing that it's easy come, easy go."
    return

label memo_game_win:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    "Hey, you matched all the cards! Aside from bragging rights, this nets you a total of two coins. They're useless for anything outside the casino, and most of the other games here require a small pile of tokens as a starting bet, so you decide to hold onto them."
    python:
        inventory.append("Two casino coins. The face of Lady Luck looks remarkably human, although you know that nothing of the sort lies beneath her mask.")
    return