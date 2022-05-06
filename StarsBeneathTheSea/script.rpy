# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define person = Character(_(""))
define player = Character(_("You"), color="#00dd00")
define cultist = Character(_("Cultist"), color="#aa7777")
define randy = Character(_("Randy the Cultist"), color="#777777")
default sanity = 3
define isMale = True

label start:
    menu:
        "Choose a character..."
        "Marina":
            $person = Character(_("Marina"), color="#dd0000")
            $pronouns = ["Princess", "princess", "She","she","Her","her","Her","her"]
            $isMale = False
        "Davy":
            $person = Character(_("Davy"), color="#0000dd")
            $pronouns = ["Prince", "prince", "He","he","Him","him","His","his"]
    jump intro

label intro:
    person "The sea is vast and dark and dangerous. Caught between the furious sky and churning waters, I can only think that we are utterly foolish to think we can tame either."
    person "As the rope I'm tying yanks itself out of my hands, I catch a glance at the rest of the ship. The crew are trying desperately to keep things controlled, and like me, the other passengers doing what we can to help and avoid getting in the way."
    person "The mate is shouting orders, although his words are lost in the wind. The sea washes over the deck, and another man is lost."
    person "They have already cut the mast. I lose my balance and slide halfway across the deck, drenched in freezing water. I struggle to regain my footing, for I am numb with cold and fear. A voice from below is calling, ordering me to come."
    person "God help me, for mercy will be found in no one else."

    centered "Stars Beneath the Sea"

    scene bg ocean with fade
    if isMale:
        show man sad with dissolve
    else:
        show woman sad with dissolve

    "Wow, what an unfortunate person! Luckily, you are not this person! Instead, you are a 5000 year old sea monster who lives at the bottom of the ocean and feeds off of dead organic matter."
    "Having noticed this commotion in the ocean and inferred that a number of dead organic sailors may be showing up soon, you have arrived at the surface just in time to save the hapless [pronouns[1]]!"
    show screen gameUI
    "You take a moment to check their sanity, which has conveniently shown up in the Stats button that just appeared."
    "It appears to be at 3, which is very good, considering what they have been through!"
    player "So, how's it going?"
    "The [pronouns[1]] coughs up seawater."
    if isMale:
        show man fear
    else:
        show woman fear
    person "Where are you taking me? Who are you? Heeeelp!"
    player "Hey, I'm just trying to save you here. You looked like you were in trouble."
    "The [pronouns[1]] regains [pronouns[7]] composure."
    if isMale:
        show man sad
    else:
        show woman sad
    person "I'm sorry. Where are my manners?"
    "[pronouns[2]] coughs up some more water and looks up at you."
    person "Thank you. If there's any way I can royally demonstrate my gratitude, please let me know."
    player "Actually, there is one thing."
    player "Will you marry me?"
    if isMale:
        show man mad
    else:
        show woman mad
    person "What?!"
    player "Hey! You said 'anything'!"
    person "Yes, but I can't marry you! I'm a [pronouns[1]] and you're, well, a monster!"
    person "No offense."
    "Darn. You had hoped you could just marry the [pronouns[1]], thus placing you within the proximity of a human soul, which you could then STEAL THROUGH THE ANCIENT RITE OF MARRIAGE!"
    if isMale:
        show man sad
    else:
        show woman sad
    player "Okay, I get it, it was a little forward of me."
    player "Can I at least try to change your mind?"
    player "Can I take you on a date?"
    "The [pronouns[1]] thinks about it for a moment."
    person "Well I guess one date couldn't hurt. Okay then."
    if isMale:
        show man glad
    else:
        show woman glad
    player "Great!"
    "You see a sailor drift by, struggling to keep his head above the water."
    menu:
        "Eat the delicious sailor":
            "You grab the sailor and cram him into your mouth. He is delicious!"
            if isMale:
                show man fear
            else:
                show woman fear
            player "You have great taste in crew members, [pronouns[1]]!"
            $sanity -= 1
            "The [pronouns[1]] seems horrified. [pronouns[6]] sanity is decreasing! This date is not off to a good start!"

        "Rescue the sailor":
            "You pick up the sailor with one of your other tentacles. He screams and faints."
            player "He'll be fine."
            "The [pronouns[1]] smiles wanly."

    "Okay, it's time to get this date on! You head to the most idyllic island you know of and put down the [pronouns[1]]."
    scene bg beach with fade
    if isMale:
        show man glad with dissolve
    else:
        show woman glad with dissolve
    player "So, this is a really nice place, I think."
    person "Yeah, I guess it is."
    player "Yeah."
    person "Yeah."
    "Oh no! You are at a loss for what to say! Any moment now, the conversation will enter the dreaded 'awkward phase' - in fact, it has entered that phase right now!"
    "And it looks like the [pronouns[1]] has become aware of the awkwardness! Quick! You must come up with a topic with which to converse about with this human!"
    menu:
        "Talk about the weather":
            player "It is sunny."
            "The [pronouns[1]] is practically sinking into the awkwardness."
            person "That appears to be a correct observation. Yes."
            player "There are a number of interesting atmospheric phenomena that are caused by the solar emissions, which are emissions of photons, which are both a particle and a wave."
            "The [pronouns[1]] seems slightly more interested now."
            player "Indeed, though past mortals would insist that the weather is caused by the whims of the gods, this current age is scientifically enlightened enough to realize the complex meteorological interactions that bring about the weather."
            if isMale:
                show man yay
            else:
                show woman yay
            "The [pronouns[1]] is absolutely astounded! Great job, you smooth charmer! Sometimes, you impress even yourself!"
        "Get personal":
            player "To be honest, it's difficult for me to talk to people. Living in the abyssal depths of the ocean, it's a little hard to be sociable."
            "The [pronouns[1]] looks sympathetic."
            person "I think I get what you mean. In the castle, even though I'm surrounded by so many people, it can be really difficult to make friends. To them, I'm a [pronouns[1]], not a person."
            person "The only one who was always there for me was my dog, Lucky. He was just about my best friend in the whole world. I miss him a lot."
            player "I'm sorry."
            if isMale:
                show man sad
            else:
                show woman sad
            person "It's in the past."
            "[pronouns[2]] is quiet."
            player "Hey, there might be a way I can help."
            "You reach into the void and search for Lucky's soul. Seizing the nearest fish, you mould its flesh into the approximation of a puppy."
            if isMale:
                show man fear
            else:
                show woman fear
            "'HEll0 aGaiN FriENd,' the puppyfish rasps. It writhes, gasping. The [pronouns[1]] screams and chucks it back into the ocean."
            $sanity -= 1
            "You may have caused some sanity damage."

    "So, that went well."
    if isMale:
        show man glad at center
    else:
        show woman glad at center
    "You decide that that's enough chatting with the [pronouns[1]]. [pronouns[2]] stretches and leans back on the picturesque beach. [pronouns[2]] watches the sky's clouds drift by."
    "It's really nice out here, with just the two of you."
    if isMale:
        show man glad
    else:
        show woman glad
    show cultist glad at left with moveinleft
    cultist "Mirovia, great mistress of the deep! She has blessed us with her horrific appearance!"
    if isMale:
        show man sad
    else:
        show woman sad
    "Ah, darn, it's your cultists."
    cultist "All hail Mirovia! Accept our devotion and bless our cult, please!"
    person "You know these people?"
    "[pronouns[2]] looks very unimpressed."
    player "It's really not what it looks like..."
    cultist "We've got a really pretty virgin we're ready to sacrifice! Quick, Randy, prepare the altar and the unholy incense."
    randy "Aye aye captain!"
    player "Okay, fine, it's exactly what it looks like."
    player "But it's not that bad of a cult, I swear!"
    person "Okay, look. I can accept that you're a giant undersea monster. I can accept that you have very poor social skills. But sacrificing virgins is where I draw the line."
    "Argh! You really want to eat that random virgin! But you also really want to date the [pronouns[1]]! Why must you be forced to choose?!"
    menu:
        "Eat the virgin":
            "When the [pronouns[1]] is not looking, you stuff the virgin into your mouth. Then you toss some gold you found in an old shipwreck at the cultists as thanks."
            if isMale:
                show man mad
            else:
                show woman mad
            person "I cannot believe you just ate that virgin in front of me."
            person "They're practically an endangered species!"
            player "...you saw that?"
            person "YES."
            player "Oops."
            $sanity -= 1
            "Sanity damage incurred."
        "Do not eat the virgin":
            player "Sorry, cultists, could we do this another time?"
            show cultist sad at left
            "The [pronouns[1]] raises an eyebrow."
            player "And also, please let the virgin go?"
            cultist "Fine."
            person "Well, thank you."


    scene bg castle with fade
    if isMale:
        show man sad with dissolve
    else:
        show woman sad with dissolve
    "By this time, it is late. You take the [pronouns[1]] back to their castle and drop them off."
    player "So, how did the date go? Will you marry me now please?"

    if sanity == 3:
        jump end2
    elif sanity == 2:
        jump end1
    elif sanity == 1:
        jump end3
    else:
        jump end4

label end1:
    person "Well, I'll admit I had my doubts, but..."
    if isMale:
        show man yay
    else:
        show woman yay
    person "It was actually a really nice date. Thank you."
    player "Great! Will you marry me?"
    person "An ancient sea monster is as good of a match as any, both in aesthetic and political terms. Eh, why not?"
    player "AWESOME!!!!!"
    "You are married and you now have a human soul so you can get legs. Yey."
    return

label end2:
    person "It was okay, I guess. Thanks for saving me."
    player "Will you marry me??????"
    "The [pronouns[1]] looks up at you."
    if isMale:
        show man glad
    else:
        show woman glad
    person "No way. I mean, you're nice and all, but we've just barely met. I'd have to be JUST a little crazy to marry you right now."
    person "Let's take it one day at a time, okay?"
    "You've been friendzoned! But at least you both have a new friend, and you also get some great fish and ships out of the [pronouns[1]]'s enemies."
    return

label end3:
    if isMale:
        show man mad
    else:
        show woman mad
    person "What?! After all that?! No way!"
    person "You are a horrible monster and I am never going back to the ocean!"
    player "Darn."
    "You feel kind of depressed at this rejection, and so you launch a tidal wave at the castle, which makes you feel a lot better."
    return

label end4:
    "The [pronouns[1]] is giggling madly and does not answer."
    player "Um, are you okay?"
    if isMale:
        show man crazy
    else:
        show woman crazy
    person "There are eyes in the deep! There are eyes in the stars! Nothing is right! Nothing is right!"
    "The [pronouns[1]] appears to have gone insane. Oops."
    "You quickly eat them to cover your mistake."
    "At least you got a royal snack."
    return
