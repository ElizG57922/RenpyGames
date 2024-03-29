define yourname = "John Smith"

#define characters
define ter = Character(_("Terrence"), color="#aaaaaa")
define pris = Character(_("Prismec"), color="#c80000")
define mer = Character(_("Merina"), color="#1111d8")
define spin = Character(_("Spinner"), color="#c800c8")
define fel = Character(_("Felicia"), color="#33eeee")
define me = Character(_("Me"), color="#b5ffb5")

default points = [0, 0, 0, 0, 0]
default daysSpent = [0, 0, 0, 0, 0]

label start:
    scene bg intro
    with fade

    python: #get your name
        yourname = renpy.input("What is your name?", length=32)
        yourname = yourname.strip()
        if not yourname:
            yourname = "John Smith"
    me "All right, my name is [yourname] and oh no the Java game is now Python and anime."

    call intro from _call_intro

    call day1Intro from _call_day1Intro
    call day2Intro from _call_day2Intro
    call day3Intro from _call_day3Intro
    call day4Intro from _call_day4Intro
    call day5Intro from _call_day5Intro
    call day6Intro from _call_day6Intro
    return



label chooseEnd:
    if points[0] >= 3:
        call endSpin from _call_endSpin
    elif points[1] >= 4:
        call endMisty from _call_endMisty
    elif points[2] >= 3:
        call endMer from _call_endMer
    elif points[3] >= 3:
        call endPris from _call_endPris
    elif points[4] >= 4:
        call endTer from _call_endTer
    else:
        call endBad from _call_endBad
    return

label choosePath:
    menu:
        "Check on Spinner":
            if daysSpent[0] == 0:
                call day1SpinPath from _call_day1SpinPath
            elif daysSpent[0] == 1:
                call day2SpinPath from _call_day2SpinPath
            elif daysSpent[0] == 2:
                call day3SpinPath from _call_day3SpinPath
            elif daysSpent[0] == 3:
                call day4SpinPath from _call_day4SpinPath
            else:
                call day5SpinPath from _call_day5SpinPath
            
        "Check on the other monsters":
            if daysSpent[2] == 0:
                call day1MonsterPath from _call_day1MonsterPath
            elif daysSpent[2] == 1:
                call day2MonsterPath from _call_day2MonsterPath
            elif daysSpent[3] == 2:
                call day4PrisPath from _call_day4PrisPath
            elif daysSpent[3] == 3:
                call day5PrisPath from _call_day5PrisPath
            elif daysSpent[2] == 2:
                call day3MonsterPath from _call_day3MonsterPath
            elif daysSpent[2] == 3:
                call day4MerPath from _call_day4MerPath
            else:
                call day5MerPath from _call_day5MerPath

        "Take Terrence up on his offer" if daysSpent[1] == 1:
            call day2MisPath from _call_day2MisPath
        "Find Misty" if daysSpent[1] > 1:
            scene bg hallfront
            with fade
            if daysSpent[1] == 2:
                call day3MisPath from _call_day3MisPath
            elif points[4] == 3:
                call day5TerPath from _call_day5TerPath
            elif daysSpent[1] == 3:
                call day4MisPath from _call_day4MisPath
            elif daysSpent[1] == 4:
                call day5MisPath from _call_day5MisPath
    return

        

label intro:
    "Okay then."

    menu:
        "Would you like to see the instructions?":
            "House of Monsters is set in an underground facility that holds, you guessed it, monsters. As befits such an interesting setting, the main character is...you! And your goal is to make friends with the monsters! How very realistic and sweet."
            "Anyway, the society is divided into 5 classes based on psychic ability, with 1s being godlike rulers and non-psychic 5s hardly getting by. 10 out of 10 society, I say."
            "You are a Class Three who's researching monster behavior. You can be a boy, girl, or whatever - your character's gender isn't specified."
            "You talk to the monsters and sometimes make choices - good answers give you points. If you get enough good answers, you can score a character point the end of the day."
            "The goal is to get a certain number of these, usually 3, but more for the harder characters. Hint: Merina and Spinner are easy."
            "Make the choices you think are best and have fun. Now, enough hand holding. Let's play!"

        "Or just get straight to playing?":
            "Okay then! Let us start!"
    return

label day1Intro:
    scene bg intro
    with fade

    "Day 1"
    "Welcome to your new job. As the elevator carries you down, you cannot help but notice how quiet the atmosphere is. The air barely moves. What adventures will this job bring you? What will you do? Will you, perhaps, find true friendship?"
    "You exit the elevator and look around. To put it plainly, this place needs some serious TLC. It looks like the very foundations of the building want to give up and die."
    "But hey, at least you aren't in it alone. There's one other person in this room, a Class Five janitor, by the looks of him. Maybe he can help you figure this place out."
    "What will you do?"

    menu:
        "Ask for help":
            call day1HelpPath from _call_day1HelpPath
        "Venture off on your own":
            call day1MonsterPath from _call_day1MonsterPath_1
    return


label day2Intro:
    scene bg intro
    with fade
    "Day 2"
    "The elevator groans as you make the descent once again to the proper floor. Another day has begun."
    "As you breathe in the stale air, rich with the perfume of large animals and hay, you wonder where you're going."
    call choosePath from _call_choosePath
    call printPoints from _call_printPoints
    return

label day3Intro:
    scene bg intro
    with fade

    "Day 3"
    "Yet another sunny, cloudless, over 100 degree day has started. Your boss, a Class Two named Felicia, passes by you in the hall and nods curtly. You head off to start work, wondering what adventures this day will bring."
    call choosePath from _call_choosePath_1
    call printPoints from _call_printPoints_1
    return
 
label day4Intro:
    scene bg intro
    with fade
    "Day 4"
    "Here goes another day. Perhaps, despite the dreary work ahead of you, you can get some quality conversations in. True friendship awaits!"
    call choosePath from _call_choosePath_2
    call printPoints from _call_printPoints_2
    return
 
label day5Intro:
    scene bg intro
    with fade
    "Day 5"
    "The monsters seem agitated today. Somehow, the way they pace around in their cages reminds you of the way that small animals act before a large storm. Something big may be coming."
    "Best make friends while the weather is fair, and they may help you when the storm hits."
    call choosePath from _call_choosePath_3
    call printPoints from _call_printPoints_3
    return
 
label day6Intro:
    scene bg intro
    with fade
    "Day 6"
    "The elevator stops. You wait for the doors to open. When they remain closed, you press the button again. The doors remain firmly shut."
    "They open. Quickly, you step off the elevator, eager to get away from its confines. The light above you flickers."
    "An aura of unease hangs around the air. It could just be a lingering fear from your earlier accident, but you cannot seem to shake it. The monsters know, but you do not."
    "It's late into your shift when the storm hits."
    "This is not a drill. If it was a drill, the halls around you would not be echoing with the sounds of inhuman screams."
    "The cage in front of you would not be open, and the canine monstrosity that was its former inhabitant would not be crouched menacingly outside of it."
    "There is nowhere for you to run. Psychically, you try to push it back, but it shrieks and your control is suddenly snapped. You try again and again, but each time, it mentally pushes you away."
    "You realize that there is no way to fight back. You close your eyes..."
    call chooseEnd from _call_chooseEnd
    return
 
label day1HelpPath:
    show ter neutral
    "You wave at the man and he notices you. He stops his work and comes over, and you notice that his name tag reads 'Terrence.'"
    "You explain to him that this is your first day and you're not really sure where you're supposed to go. He nods, understanding, and points you in the right direction."
    hide ter
    "You head off and find the monster you were assigned to take care of: Spinner. It looks like a giant spider, but instead of having eight arms, you count 12."
    show spinner neutral
    with dissolve
    "Some of them end in claws and others in spikes, and one pair of them are odd little cones whose purpose you cannot begin to guess."
    "He sees you (lol im spi-derp) and his purple eyes narrow."
    spin "Hello there :P"

    menu:
        "Answer the monster":
            call day1SpinPath from _call_day1SpinPath_1
        "Ignore him and run back to Terrence":
            call day1MisPath from _call_day1MisPath
    return


label day1SpinPath:
    $ daysSpent[0]+=1
    hide ter
    show spinner happy
    "You greet the giant spider. \"Hi :D\" he hisses. You notice that he's watching you rather intently (with his lolSexy eyes)."
    "Spinner's twelve legs fly about almost hypnotically (oOo). You should be wondering why you are talking to a gigantic spider, but here you are. Good job for playing this game. I think Spinner will be a good friend. Yay."
    $ points[0]+=1
    return


label day2SpinPath:
    $ daysSpent[0]+=1
    define spinPoints = 0
    show spinner neutral
    with dissolve
    "Here you are, talking to Spinner the giant spi-derp. You should think of something to say."
    menu:
        "1: Talk about the weather":
            "The 100 plus degree weather is, in fact, quite nice. It is too bad that Spinner is a giant spider and in a cage, or he would certainly appreciate all the wonderful things you have to say about the sun."
        "2: Talk about bugs":
            "Being that you are talking to a giant spider, you decide to talk about bugs. Spinner discusses ate a mosquito."
            $ spinPoints+=1

        "3: Talk about football":
            show spinner sad
            "This does not work. You have failed. You have seriously failed. I hope that you are regretting each and every one of the life choices that led up to you picking this option. Boo."
            $ spinPoints-=1

    "Spinner stretches his legs and yawns :O."
    spin "Well, it certainly was interesting, speaking with you."
    "You nod, feeling the exact same way."
    show spinner neutral
    "Spinner has one last thing to say, though. His LOLpurple eyes narrow and his spidery fangs glisten."
    spin "So..."
    "He turns around slowly. Your heart begins to flutter in anticipation."
    spin "What do u think..."
    "You're holding on to his every word."
    spin "of outdated memes?"
    show spinner memes
    "His second body segment is entirely covered in outdated memes."

    menu:
        "I seek true memeship. We are a match made in an underground facility.":
            "Ask and you shall receive, my friend."
            $ spinPoints+=1
        "No.":
            show spinner sad
            "Nu!1!1! Yu have to ste focused! Mek friends wit da spi-derp, remember?!"

    if spinPoints >= 1:
        $ points[0]+=1
    return

label day3SpinPath:
    $ daysSpent[0]+=1
    show spinner neutral
    with dissolve
    "These long, meaningful conversations, they are really going places! As the passionate friendship between you and Spinner continues, the great cosmic clock of loldom ticks down to the end of this magical time."
    "You wonder, are you really ready to be friends with Spinner?"
    "There may still be time left. If you back out now, you might still have a chance to get a different ending. Are you really ready to commit to this spider?"
    menu:
        "I would give him my mind, body, soul, and (most importantly) heart. I am ready for this.":
            show spinner happy
            "uwu! Let's see this friendship through!"
            $ points[0]+=1
        "Actually, no.":
            "You run the heck out of there and find some other monsters to bother."
            hide spinner
            if daysSpent[2] == 0:
                call day1MonsterPath from _call_day1MonsterPath_2
            elif daysSpent[2] == 1:
                call day2MonsterPath from _call_day2MonsterPath_1
            elif daysSpent[3] == 2:
                call day4PrisPath from _call_day4PrisPath_1
            elif daysSpent[3] == 3:
                call day5PrisPath from _call_day5PrisPath_1
            elif daysSpent[2] == 2:
                call day3MonsterPath from _call_day3MonsterPath_1
            elif daysSpent[2] == 3:
                call day4MerPath from _call_day4MerPath_1
    return
            
label day4SpinPath:
    $ daysSpent[0]+=1
    show spinner neutral
    with dissolve
    "Spinner, Spinner, in a web."
    "Spinner is an awesome spi-derp."
    "I hope you have no regrets."
    "Because I certainly do after writing this."
    $ points[0]+=1
    return

label day5SpinPath:
    show spinner neutral
    with dissolve
    "I warned you. There is no turning back."
    "But here you are."
    "You have nothing in common with a giant spider. Do you realize this?"
    "But nooooooo. You had to ask for this."
    "OMG! Spinner is like, so cool! U hav so much in common wit a giant spider! U r such friends!"
    "It is a beautiful day."
    $ points[0]+=1
    return

label endSpin:
    show spinner neutral
    with dissolve
    "Spinner drops from the ceiling, landing between you and the monster. It is quick, brutal, and executed with an almost cartoonish level of violence, but Spinner comes out without a single scratch."
    show spinner happy
    "Then Spinner turns to you. It's awesome. You love him so much (as a friend). You do not wonder why the writing quality of this branch is so bad."
    "You do not wonder this because you are too busy admiring his anthro form. It is so awesome. You are now making out (in an absolutely platonic way)."
    show spinner kiss
    "If there was a picture here, and there now is, you would totally be swooning, which means you now are. You have lost your dignity, but won the friendship sim. ;D"
    "gg"
    "{b}Literally any other ending is better than this ending Ending{/b}"
    return

label day1MisPath:
    hide spinner
    "The monster mumbles something about u suk at manners, but does not attempt to make conversation again. You cannot find Terrence, so you study a pair of rodent monsters in peace. When you head out, you see the janitor."

    menu:
        "Wave him over. You want to talk.":
            show ter neutral with dissolve
            "You call him over. As you're walking, you make conversation about your day. When you tell him about your experience with Spinner, he seems to understand."
            show ter fear
            ter "He's really not that bad, though. Most of the monsters aren't."
            "You chatter on for a little while. Eventually, you find yourself at the bus stop, and you stop with Terrence to wait for it. Suddenly, he turns to you."
            ter "You're here tomorrow, too, right? If you would like, I could introduce you to one of the nicer monsters."
            "You'll definitely think about it."
            $ daysSpent[1]+=1

        "Just head home.":
            "So home you go."
    return

label day2MisPath:
    $daysSpent[1]+=1
    define terPoints = 0
    define misPoints = 0
    show ter smile
    with dissolve
    "You find Terrence almost immediately."
    me "Hi, I decided to take you up on that offer. What kind of monster are we up against today?"
    "He grins as you walk with him down the cement halls."
    ter "Nothing too serious. Misty is actually really nice. I think you'll like her."
    "He turns the corner and you follow."
        
    menu:
        "Walk in silence":
            pass
        "Make conversation":
            "You ask him how long he's been working here, and it turns out that he has had this job for a little over a year."
            "He speaks as quickly as he walks, and whenever it's your turn to say something, you realize that you're nearly panting!"
            $ terPoints+=1

    scene bg hallfront
    show mis neutral at right
    show ter smile at left
    with fade
    "Eventually, you both stop. The monster in front of you presses her nose against the glass and chirps happily at Terrence. Her eyes are black and glassy, and there is a white butterfly resting on her head."
    show mis upset
    "She notices you and tilts her head to the side, apparently confused."
    ter "Misty, this is [yourname]."

    "Well, an introduction has two halves."
    menu:
        "Hi there.":
            pass
        "I like your butterfly.":
            "Misty blushes pale pink at the compliment."
            $ misPoints+=1
    show mis neutral
    "She smiles at you and waves. The butterfly on her head flutters for a moment before settling down again."
        
    "Terrence has to go back to his job, and so do you, but at lunchtime, the three of you reconvene."
    "You unwrap the food bar you brought, Terrence unwraps his, and Misty digs into whatever unidentifiable monster food she has to eat. She takes a bite and then looks at you."
    "Catching your attention, she tosses it into the air and the butterfly snatches it out of the air."
    show mis happy at right
    "She giggles and performs the trick again."
    "After showing off for a little while, Misty puts her hands on her hips and chirps at Terrence. She makes a series of complicated gestures with her hands, but Terrence seems to understand them because he starts shaking his head."
    ter "No, Misty. That isn't very professional."
    "You're still waiting for a translation, and he starts blushing furiously."
    ter "She, um, she really wants me to show you this stupid food tossing trick."
    "He flashes Misty a dirty look, which she innocently ignores."
    show ter fear
    ter "I don't usually do this at work. I-I mean, this is stupid."
    "At about this time, he realizes that it's in his best interest to quit talking. He shakes his head pleadingly. Misty points at him and nods."
        
    menu:
       "Side with Terrence":
           "You've had your fun, and you decide to give the janitor a break."
           me "All right, we'll just have to see Terrence's award winning food toss some other day."
           show mis neutral
           show ter neutral
           "You smile, Misty shrugs, and Terrence folds his arms, mumbling something about not being anyone's trick monkey."
           "Still, the look he gives you is one of gratefulness. It's not often that somebody sides with a Class Five, even for something unimportant like this."
           $ terPoints+=1
       "Side with Misty":
           me "Come on, Terrence, I have to see this!"
           show mis happy
           "Misty joins you in your encouragement."
           show ter neutral
           "Terrence rolls his eyes and breaks a piece off of his Food Bar. With a spectacular toss, he makes the catch with his mouth before declaring that the rest of the food has to go in his mouth the normal way or he'll be starved."
           "Misty catches your attention and giggles."
           $ misPoints+=1

    "With that little adventure over, the bell rings, signaling the end of lunch. It's time for you to head back to work."
        

    if terPoints >= 2:
        $ points[4]+=1
    elif misPoints >= 1:
        $ points[1]+=1
    return

label day3MisPath:
    $ daysSpent[1]+=1
    define terPoints = 0
    define misPoints = 0
    show mis neutral with dissolve
    "You head over to Misty's pen, deciding it is the best place to find her and Terrence. The janitor isn't there, but Misty waves at you."

    menu:
        "Chat with her":
            call chatMistyD3 from _call_chatMistyD3
            $ misPoints+=1
        "Search for Terrence":
            hide mis
            "You head off to look for the Class Five. He's bent over one of the smaller cages, pulling something away from the furry creature on the ground. It's a monster!"
            show ter fear with dissolve
            "Before you can run for help, Terrence pulls his mop out of the creature's grasp."
            ter "It's okay! This is a phase mole! They aren't dangerous, but they get out all the time."
            "It isn't exactly the most comforting speech, but it makes you take a second look at the creature."
            "It's small and furry and it resembles a mole very closely. Using its tiny front paws, it takes hold of the mop once again and pulls."
            $ terPoints+=1
            "It's actually kind of cute. Feeling a little bolder, you reach out with your mind and and pry it away from its wooden treasure. You plop it back into its cage and it wanders around."
            show ter smile
            ter "Thanks."
            "You both head back to Misty."
            show ter smile at left with move
            show mis neutral at right
            with dissolve

    "The three of you sit down to lunch. After a few lazy comments about the weather, Terrence starts complaining about his boss. According to him, she's incredibly strict and most of all, rude."
    "You don't know Felicia too well, but she didn't strike you as particularly awful."
    ter "Yeah, well, she is. Creepy, too."
    show mis upset
    "He scoffs."
    ter "Just look at the way she's always..."
    show ter fear
    "He stops suddenly."
    ter "Never mind. She's not that bad, really."
    "He doesn't seem to want to talk about it."
        
    menu:
        "Press him about Felicia":
            "He really doesn't seem to want to talk about it, but apparently, she's been singling him out for trouble for some really pointless things."
            show ter neutral
            ter "It's nothing, really. Honestly."
            "He avoids your gaze and quickly returns to work when the bells signal the end of lunch. Maybe you shouldn't have pushed him so much."
            $ terPoints-=1
        "Change the subject":
            show mis happy
            "You instead start praising the remarkable triple butterfly toss that Misty just pulled off."
            show ter smile
            "All three of you are happy, and lunch ends far too soon."

    if terPoints >= 1:
        $ points[4]+=1
    elif misPoints >= 1:
        $ points[1]+=1
    return

label chatMistyD3:
    "You can't really talk with Misty, but she does seem to enjoy hearing what you have to say. You ramble on about the weather and your job and whatever else happens to come to your mind."
    "When you run out of things to say, it's so quiet that you can hear the monsters breathing heavily in their prisons."
    "A chirp breaks the silence. You turn and see Misty tapping on the glass."
    "When she realizes she's got your attention, she starts miming the act of eating with a spoon."
    me "What are you doing? Do you need to eat?"
    "She shakes her head and makes a series of gestures with her hands. You understand. She is trying to teach you what the word \"eat\" is in her language."
    "You learn a few more words: \"butterfly,\" \"light,\" \"see,\" before Terrence finally jogs up. He puts one hand on the wall."
    show mis neutral at right
    with move
    show ter smile at left
    with moveinleft
    ter "Hi guys. Sorry I'm late. One of the smaller monsters got out and tried to eat my mop."
    return

label day4MisPath:
    define misPoints = 0
    define talkMis = True
    $ daysSpent[1] +=1
    show mis neutral
    with dissolve
    "You find that Misty girl and give her a cheerful hello."
    "The two of you sit, you leaning against the glass and Misty sitting against it on the other side."
    if points[1] >= 2:
        "Misty chirps at you happily."
        
    "So, let's interview this monster!"
    show mis happy
    if points[4] == 2:
        "Actually, now that you think about it, you haven't seen Terrence all day. Would you like to find him?"
            
        menu:
            "Yes":
                $ talkMis = False
                hide mis
                call day4TerPath from _call_day4TerPath
            "No":
                pass
    if talkMis:
        "Misty chirps happily at your questions. You're not quite sure if she understands all of them, and you know that you don't understand all of her answers, but it's still a good time."
        "She pantomimes things out and the two of you play charades while her little white butterflies flutter."
        show mis neutral
        "After a little while, you notice that she's getting tired."
        "Suddenly, you have a new question for her."
        me "Hey, Misty! Can you do this?"
        "Breaking off a piece of your Food Bar, you toss it into the air and spectacularly fail at catching it."
        "She bursts into giggles and attempts the trick with her own lunch. Of course, it always helps to have a few butterflies."
        "How loudly are you going to cheer?"
        menu:
            "Quiet":
                show mis upset
                "Misty tosses it higher, not wanting to disappoint you. You barely clap, and the pale blush creeps into her cheeks."
            "Loud":
                show mis happy
                "You applaud. Beaming, she gives a little clap and makes the catch again and again."
                $ misPoints+=1
            "Ultra":
                show mis happy
                "You attempt to break the sound barrier. Misty beams with pride, and her face suddenly reddens because just about every monster in the hallway starts shouting that you have no idea what peace and quiet is."
                "Your face floods with blush."
                $ misPoints+=1
        show mis neutral
        "Misty's butterflies seem to be tiring out. She sits down and moves a little closer to the glass."
        "She squeaks."
        "Tell her a story?"
        menu:
            "Yes":
                $ misPoints +=1
                "You lean back against the glass, thinking of a good tale to tell. After a bit of thinking, you settle on a fantasy one about a magical shaft of silver light."
                "It isn't as good as you remember it to be, but it brings back memories of childhood and true friends and summers long ago but not forgotten."
                "Misty listens, her wide eyes drinking in every word. She curls up and sits so close that you barely remember that only a thick sheet of containment glass separates you from the monster."
                "She hugs her knees to her chest and twitters."
            "No":
                "You sit together in silence. Eventually, you look over to find Misty fast asleep."
        hide mis with dissolve
        "That's when the sirens start."
        "Your first though is, \"Breach!\" But that isn't it. The people you see running aren't moving quickly enough for that."
        "The crowd is too thick. Most of the people are Class Fours who let you through once they realize your status. Still, a pair of medics, both Class Threes, shoo you back as they try to assess the situation for themselves."
        "There has been an attack. Your own boss, Felicia, sits in the corner, in shock as a Class Three doctor bandages her wounds. She is gasping."
        "Terrence, the Class Five janitor, is dead."
        "Well, at least it could have been a whole lot worse. He was only a Class Five, after all."
        "Still, he was Misty's friend. She is devastated."

        if misPoints >= 1:
            $ points[1]+=1
        $ points[4] = 0
    return

label day5MisPath:
    show mis sad
    with dissolve
    "When Misty sees you, she chirrups sadly. Her eyes are filled with tears."
    "If you could reach through the glass, you would hold her. Instead, you sit in silence, listening to her soft, hiccupy breaths through the glass."
    me "It's going to be okay."
    show mis tearsa
    "She sniffles again, but looks into your eyes."
    me "It's going to be okay."
    "Still, the words sound hollow."
    show mis tearsb
    "What are you doing? You're supposed to be monster caretaker! If nothing else is clear to you, this monster needs some care right now!"
    show mis tearsa
    "You slip on your gloves and open the enclosure. Misty looks up at you, still weeping."
    "You take her into your arms and let her tears wet the front of your uniform. Her little body shakes, and it feels so cold against yours. You hold her close."
    "She lets the tears run their course. As the two of you stand, sharing your sadness, the echoes of distant howls grow unimportant. Misty finally stops crying."
    show mis upset
    "She stays in your arms for another moment before letting go. In the distance, a monster wildly screams. You think Misty is going to start crying again, but instead, she looks up with her wide, glassy eyes and makes a single sign."
    "'Friend.'"
    $ points[1]+=1
    return

label endMisty:
    image flies = SnowBlossom("fly.png", count=100)
    show flies
    "All of a sudden, pale white butterflies surround the creature. At first, you take it as a welcome distraction. While they swarm the monster, you take your chance and run. Behind you, your would-be attacker growls."
    "Suddenly, it lets out a scarp cry."
    "The butterflies swarm the monster, turning crimson as they drain its blood. The monster howls in pain and blindly runs."
    show mis neutral
    with dissolve
    "You hear Misty's familiar chirping. The butterflies flock to her, and once they are all accounted for, she slips into your arms for a moment before the two of you take off running."
    hide flies
    "When you get to the surface, she turns around and squeezes your hand. You made it. Both of you."
    "Through the morning light, butterflies swirl, and the sun rises in the distance."
    "You are home."
    "{b}Butterfly buddies Ending{/b}"
    return

label day4TerPath:
    scene bg elevator
    with fade
    "You poke around for a bit, looking for Terrence. You pause for a moment, and one monster with cascading tentacles starts slamming its body against the side of its pen. You move on."
    show ter neutral at right
    show fel neutral at left
    with dissolve
    "Ah, there's Terrence. He's mopping up a spill on the floor, and the boss, Felicia, is watching him. They seem to be busy. You hang back and listen."
    fel "You missed a spot."
    "Terrence moves to clean it. Suddenly, the Class Two grabs for the mop and snatches it."
    fel"I got it."
    "She daintily brushes the head of the mop against the floor. She smiles, handing it back to the janitor."
    "Suddenly, she swipes it back."
    fel "Missed another spot."
    "She smiles, bringing the dripping mop lightly down on Terrence's head."
    ter "Ha ha, Felicia, very funny."
    "He gives a smile, but it looks forced."
        
    menu:
        "Intervene":
            me "Hi, am I interrupting something?"
            "You step forward. Felicia wheels toward you in surprise, blushing as she tries to figure out just how much of her unprofessional behavior you just witnessed."
            fel "No, it's all good."
            "Regaining her composure, she walks away quickly."
            "You catch Terrence staring at you with a strange expression before he returns to his cleaning."
            $points[4]+=1
        "Keep watching":
            "Felicia hands the mop back, and this time, Terrence gets to take it. He resumes his work, but Felicia stays where she is. She folds her arms."
            fel "I was thinking about how to improve the hiring process, and I'm deciding to add a literacy test to the application. Do you think that would affect your candidacy for this job?"
            "He barely looks up."
            ter "No, I don't think it would."
            fel "A shame."
            "Her eyes narrow slightly."
            fel "You're just a stupid Class Five."
            "Terrence focuses a little harder on the floor."
            fel "Why would anyone even bother to teach you lot to read?"
            "Felicia pushes herself off of the wall to circle around Terrence."
            fel "Sometimes I wonder why Class Fives are even kept around. How do you make a society function with that burden?"
            "She pauses in front of Terrence."
            fel "Maybe it would be better if we just got rid of people like you before they're even born."

            menu:
                "Intervene":
                    "You step forward and Felicia notices you. Quickly, she resumes a proper posture and glares at you."
                    fel "Class Three, do you not have a job to complete?"
                    "You stammer out an explanation, but Felicia is already storming away."
                    fel "Let this be your only warning."
                    "She leaves it at that."
                    "You shiver despite the heat and glance at Terrence. He glances at you for a brief second before returning to his work, as if this has been the most ordinary day in the universe."
                    $ points[4]+=1
                "Keep watching":
                    "In the corner, a monster growls and pounds against its cage."
                    fel "Class Five, are you listening to me?"
                    "Felicia suddenly lunges forward. She wrenches the mop out of the surprised Terrence's hands and he takes a step backward to avoid being hit by the cleaning instrument."
                    "The monster growls and pounds harder against the cage. The door gives way."
                    "It's over in a moment. Felicia steps out of the way and watches. She could stop the monster, but she chooses not to. You could stop it, but you're frozen with fear. Terrence can't stop it."
                    show ter hurt
                    "There is a horrible crunch, and for a moment, Terrence is wide-eyed with terror and shock. The next, he is missing a few vital organs. It's not a pretty sight."
                    hide ter
                    with dissolve
                    show fel mad at left with hpunch
                    "Felicia screams. Blasting the monster into the wall, she screams and bolts away."
                    "When people gather to assess the damage, they're glad that a Class Five was the only loss. It could have been a whole lot worse. The monster could have killed someone actually useful."
                    "Misty, however, is devastated."
                    $ points[4] = 0
    return

label day5TerPath:
    define terPoints = 0
    "There's a tense silence over lunch today. Misty doesn't chirp happily and Terrence eats quickly, but you notice him glance over at you more than once."
    "Lunch ends. You go back to work. For the rest of the day, studying monsters occupies your full attention, but at the end of the day, you run into Terrence again."
    show ter neutral with dissolve
    "He pauses and seems like he wants to say something, but instead he puts his hands in his pockets and gives you a quiet goodbye before hurrying to the bus stop."
    "You don't take that bus, but today, curiosity overcomes you and you follow him. He's walking quickly, but something tells you he realizes you're following him."
    "He reaches his usual stop and turns around."
    show ter fear
    ter "Are you going to follow me all night?"
    
    menu:
        "Yes":
            "Wow. You have no subtlety whatsoever."
        "No":
            $ terPoints +=1
            "You blush, embarrassed, and mutter that you were just about to leave. Quickly, you turn around."
            ter "Wait."
            "Terrence is looking at you. He stands there, awkwardly, and remains paused."
            ter "I’m sorry, okay? I didn't mean to say it that way."

    "He sighs and turns away again."
    ter "Look, I think I get what you're looking for."
    ter "These things never work. You’re a Class Three and I'm, well, I’m a Class Five. Do you understand?"

    menu:
        "Yeah":
            ter "Thank you."
            "He looks relieved."
        "Not really":
            show ter neutral
            "He folds his arms."
            ter "Tell me one person you know who wouldn't think you're pretty trashy for hanging out with a Class Five."
            show ter fear
            ter "The fact is, you'll always outrank me in every way. You make more money, you can get any job you like, you can walk down the street and feel safe...you name it."
            ter "And me? I'll only ever get a job out of 'equal opportunity' pity. Not to mention that you could force me to do just about whatever with your psychic control, and there’s really not much I can do to stop it."
            ter "I like you, really, but I’ve just seen too many bad situations to want to jump into a relationship right away."

    "You leave to walk back to your bus stop, but something makes you turn back."
    me "Can we at least be friends?"
    "Terrence blinks at you. He looks small compared to the cityscape behind him, and he seems aware of it. The sun's light has almost faded from the sky."
    ter "Um, sure."
    "He looks a little surprised."
    "A bus drives by, its headlights illuminating the street with a split second of brightness."
    "Terrence closes his eyes."
    show ter neutral
    ter "First I get all chatty with a killer monster, and now here I am, making friends with a Class Three. I must really have a death wish. You sure you still want to hang out with me?"
    "Heck yes. This is the one moment you've been waiting five days for. There is absolutely no option to say no to this friendship."
    "It's time to befriend the janitor."
    show ter smileb
    ter "Hey, um, if you aren't doing anything tonight, do you want to go to the bar together?"
    "He pauses."
    ter "My treat."
    "Well, he's paying."
    me "Okay."
    show ter smile
    "You shrug and step next to him. Work tomorrow is going to be EXTREMELY awkward."
    "The bus arrives, and you both get on. There's one other person sitting in it, a haggard Class Five man who coughs to the side before going back to picking at his frayed sun jacket. Terrence glances at you."
    ter "Let's sit here?"
    "He gestures toward a seat closer to the front. You take it, and he fills the one next to you."
    scene bg city
    show ter smile
    with fade
    "The scenery outside changes. In the darkness, you can see people and buildings whiz by. This looks like it's an older part of town."
    "Terrence remains quiet. Every once in a while, he'll glance behind him and then go back to watching the driver. After a little while, he reaches past you to pull the stop cord."
    ter "This is it."
    "It's probably the ugliest bar you've ever seen. The neon lights are way too bright, and the Class Four behind the counter looks like he might have had a few drinks himself."
    "It's not crowded, at least, and you and Terrence find an empty booth easily enough."
    "He gets up and stands next to the table like a sort of waiter."
    ter "Can I take your order?"
    "He's got the mock proper accent and everything."

    menu:
        "Something regular":
            $ terPoints +=1
            "He brings back your order, and you see that he got the same for himself. He sets yours in front of you and takes a small sip of his."
        "Something expensive":
            "Everything on the menu is cheap, but you pick something on the higher end of the price scale. When Terrence comes back with your drink, you notice he didn't get anything for himself."
        "Nothing":
            $ terPoints +=1
            ter "You sure?"
            "When you insist, Terrence sits back down. He doesn't get anything for himself."
            ter "I get you. I don't usually drink, either."
            "Then he starts to blush."
            ter "Well, except coffee."

    "You sit together for a few minutes. Why not make some conversation?"
    define stillTalking = True
    while stillTalking:
        menu:
            "Are you scared of monsters?":
                ter "It's odd, but, not really."
                "He shrugs."
                show ter smileb
                ter "I mean, it could be worse. At least there's a containment cage between us and the monsters, right? And it's not like they treat me any differently from other folks. They'll eat all of us just the same."
                "He bites his lip and smiles halfheartedly."
                show ter smile
            "What is your favorite food?":
                "Terrence thinks for a moment."
                ter "Berry muffin breakfast food bars."
                ter "The extra caffeinated ones. You should really try them."
            "How is your family?":
                ter "Um, I guess they're okay."
                "He shrugs and glances at the bartender."
                ter "I mean, it's really just my aunt and me at this point. And my aunt's a Class Four, so it's really just me."
            "What fabulously mysterious things do you do when you're not at work?":
                ter "Fabulously mysterious?"
                "He laughs."
                ter "Not much, I'm afraid. I guess I like to walk in the afternoon, and the bar's a place to go once in a while."
                "He shrugs."
                show ter smileb
                ter "I like my job, though. It's quiet and nobody really bothers me, and working around monsters is really interesting."
                show ter smile
            "Finished talking":
                $ stillTalking = False

    "Eventually, you get tired of talking. You both head out, and you realize how late it is. Terrence, being psychically defenseless, produces a can of pepper spray and discretely holds it at the ready."
    "He says goodbye and heads for the bus stop."

    if terPoints >= 1:
        $ points[4]+=1
    menu:
        "Follow him":
            show ter fear
            "He looks a little surprised, but he slows down so you can catch up."
            ter "Sorry, do you need something?"

            menu:
                "Nope, I just wanted to walk with you.":
                    "He looks visibly relieved."
                    show ter smileb
                    ter "Ah, okay. Sorry, I was just a little confused because we'd said goodbye and I wasn't sure if I'd left something or--"
                    show ter smile
                    ter "Thanks."
                    "You both head down the empty street. Terrence seems a lot quieter now, but it's probably just because you're alone outside in the dead of night."
                    "Eventually, you get to his apartment and he unlocks the door."
                    ter "It's pretty late. We should both get some sleep."
                    "He starts to close the door, but then he pauses."
                    ter "Would you mind giving me a quick call when you get home, just so I know you made it all right?"
                    show ter smileb
                    ter "I-I mean, obviously no one would dare attack a Class Three like you, but, er, just in case?"
                    show ter smile
                    "You trade numbers and then head for home. The brightest stars are visible above you, and all seems right with the world."
                    $ points[4] = 4

                "I'm stalking you creepily.":
                    "He blinks and looks at you a little nervously."
                    ter "What?"
                    menu:
                        "Quickly apologize and attempt to amend the situation.":
                            me "Sorry, bad joke."
                            "Awkward silence reigns supreme."
                            ter "Oh. Heh. You sure got me on that one."
                            "He gives a very nervous, very forced laugh and says goodbye for the second time. You notice he's holding the pepper spray a little tighter."
                            $ points[4] = 4
                        "No, I came here to commit class genocide and I have to take it all the way.":
                            me "I hate Class Fives, especially you, and I am going to make you suffer now."
                            "You see the color drain out of Terrence's face. And you get blasted with approximately one can full of pepper spray."
                            show ter hurt
                            "If you were a Class Four, he'd have probably gotten away, but your psychic powers have a pretty good reach."
                            "You have now killed one janitor."
                            hide ter
                            menu:
                                "Loot the body!":
                                    "In his pocket, you find one bottle of caffeine pills and a pittance of cash."
                                "Get the heck away before someone sees you":
                                    pass

                            "I'm pretty sure you just committed a hate crime against non psychics."
                            "Rather than waste my time lecturing you on your awful sense of morality, I will just say that the point of this game was to form friendships, and you have just done the exact opposite of that."
                            "You done goofed."
                            $ points[4] = 0

        "Head home. It's pretty late, after all.":
            hide ter with dissolve
            "You head home for the night. Above you, the brightest stars glitter."
            $ points[4] = 4
    return


label endTer:
    ter "Hey! Get away from them!"
    show ter fear at left
    show mis neutral at right
    with dissolve
    "You and the monster both turn, surprised, and see Terrence. He's brandishing a broom and standing next to Misty, who is surrounded by fluttering white butterflies."
    "You have to admit, your rescue party is kind of underwhelming."
    image flies = SnowBlossom("fly.png", count=100)
    show flies
    "This opinion, of course, immediately changes once those butterflies swarm the attacking monster, latching onto it and biting it until it howls. The good janitor stares awkwardly at that Misty girl, but he turns to you."
    hide flies
    ter "Are you all right, [yourname]?"
    "When your answer is affirmative, he grabs you with one hand and Misty with the other, and the three of you take off running. He knows his way around, luckily, and soon you are all free."
    "The escape is bittersweet, however. When you reach the surface and Misty chirps her goodbye, you wonder if you will ever see her again. You wonder where in this vast world she might be going."
    hide mis with dissolve
    "Terrence seems to share your feelings. He turns to you and gives a little half smile, trying to lighten the sadness. You return it. Misty may be gone, but at least you still have Terrence."
    show ter smile
    "And honestly, you wouldn't have it any other way."
    "{b}Good clean friendship Ending{/b}"
    return

label day1MonsterPath:
    $ daysSpent[2]+=1
    scene bg hall
    with fade
    "You wander down the halls, noting all the snouts and toothy grins that seem to jump out from every wall. The cages that line the hallway are filled with prowling, pacing, and growling beasts. Unsettled, you speed up without really knowing it."
    "Suddenly, the ground is rushing towards you."
    "Some impression you're making. Having tripped and fallen flat on your face, you feel less embarrassed and more scraped up. Scratch that. Somebody's laughing at you. Okay, now you're embarrassed."
    show mer neutral at right
    show pris happy at left
    with dissolve
    "You look up. There's a monster pointing at you. Two, to be precise. Both of them are in cages, but it's still unnerving."
    "The one that looks more human sees you dust yourself off and doubles over, laughing."
    "???" "Prismec!"
    "The other monster glares angrily at the laugher, who must be Prismec."
    show mer sad at right
    "???" "You have no manners whatsoever! The poor little sweetie could be seriously hurt!"
    show mer neutral at right
    "The nicer of the two monsters puts her hands together and smiles at you."
    "???" "I am so sorry about her!"
    "???" "You're new here, aren't you? I'll have to introduce myself! I'm Merina, princess of the mer people!"
    "Her voice is bubbly and cheerful."
    show pris mad at left
    "Prismec makes a remark that you're pretty sure is incredibly offensive to all of ocean life, but the fish princess prattles on with her introductions."
    show mer neutral
    with move
    hide pris with moveoutleft
    mer "...and of course, Spinner didn't--you know Spinner, don't you? The spider monster?"
    mer "Well, Spinner didn't care..."
    "You're not entirely sure how the conversation got to this point. She finally notices how agape your mouth is and pauses for a second."
    mer "Oh goodness! I must be prattling on! You have a job to get back to, don't you? Oh wait, your job is to talk to me?"
    "She giggles."
    mer "I'll carry on, then!"
    "And this is exactly what she does."
        
    $ points[2]+=1
    return

label day2MonsterPath:
    $ daysSpent[2]+=1
    scene bg hall
    with fade
    show mer neutral
    with dissolve
    "The moment you show up, Merina starts chattering away."
    mer "Hi there! How was your walk over here?"
    mer "I've been thinking about starfish. Did you know that there are over 400 types of starfish in the tide pools alone? That is just fintastic, I think. I once saw one with twenty four arms!"
    mer "I love starfish! They have so many uses! You can stew them, wear them in your hair, decorate your dresses...you can even have them as pets!"
    mer "They're really boring, though. One of my sisters once had a pet starfish that..."
        
    menu:
        "Keep listening":
            mer "...she trained to shovel sand! She also had four pet sea urchins! My sister did, I mean. Not the starfish, of course!"
            show mer happy
            mer "I have two hundred sisters and one hundred ninety two brothers besides her, though! But I think I have prettier hair than them. Don't tell them, though! They get so jealous..."
            "It's interesting to hear all about Merina's highly extended family. She even has some good stories in among the happy chattering. You really enjoy your work."
            $ points[2]+=1
        "Interrupt":
            "You cough and try to get a word in."
            me "Er, that's a great story you're telling, but I really have to interview some monsters, Merina."
            mer "Oh! Silly me! I completely forgot that you had a job to get back to!"
            mer "I once had a job where I sorted sea shells! I know I'm a princess, but--"
            show pris mad at left
            with moveinleft
            show mer smile at right with move
            pris "For the love of all that you can find crawling underneath a sandwich, can you please just shut up?!"
            "It's the other monster who says this. She has her hands pressed over her ears and she looks about ready to kill someone. Probably Merina."
            show pris angry
            show mer sad
            pris "Great Snakes of Atlanta! I'd think a mer-ditz like you wouldn't have enough brainpower to think, let alone speak, but here I am, stuck with the chattiest cell neighbor in all the multiverse!"
            "Merina looks about ready to cry. True, she is a chatterbox, but it's still kind of sad."
            
            menu:
                "Comfort the mermaid":
                    "You flash Prismec a cross look and turn to Merina."
                    me "Just ignore her. I liked your story."
                    hide pris
                    with moveoutleft
                    "Merina sniffles."
                    "You do?"
                    show mer smile
                    "She perks up."
                    show mer neutral
                    mer "Oh thank goodness! I was afraid I was chatting your ear slits off! I just love to talk! One time, I was talking with..."
                    "You cannot help but shrug. This probably counts as an interview, at least. By the time you go to lunch, Merina is still chatting away."
                    $ points[2]+=1
                "Well, she was pretty annoying":
                    $ daysSpent[3]+=1
                    show pris mad
                    pris "Yeesh, at least someone has a brain around here."
                    "Prismec sneers. She turns to you."
                    hide mer
                    with moveoutright
                    pris "I'm Prismec. You have a name? [yourname], huh? That's kinda cute. Don't go prancin' around thinkin' you're so great, though."
                    "She tosses her head and in a smooth sweep, her hair turns neon pink."
                    pris "You're still here? Whatcha waiting for, a cookie?"
                    show pris happy
                    "She smirks and folds her arms."
                    pris "Well, you're out of luck with that. Try me tomorrow, kay? Now get outta here."
                    $ points[3]+=1
    return

label day3MonsterPath:
    $ daysSpent[2]+=1
    scene bg hall
    with fade
    define prisPoints = 0
    define merPoints = 0
    "You find your two monstrous acquaintances."
    show mer neutral at right
    show pris mad at left
    with dissolve
    mer "Heloooooooo!"
    if points[3] >= 1:
        show pris happy at left
        "Prismec rolls her eyes, but the corners of her mouth turn up at you."
    mer "...and I can't believe it, but Shelldon, he's my brother, asked me to be the codmother of his second child! Me, of all mer people!"
    "...Of course, Merina's talking again."
    menu:
        "Well, I want to hear this":
            hide pris
            mer "...so he asked me to pick out an outfit for the baby! But I just couldn't decide between the red sea silk or the green!"
            show mer smile
            "She pauses suddenly and looks at you."
            mer "Which one do you like better?"
            "She's...she's actually waiting for you to speak."
            menu:
                "Red":
                    show mer happy
                    mer "Oooooooh, lovely! I once saw a red sea anemone, you know? It had red swirls and red..."
                "Green":
                    show mer happy
                    mer "I like that, too! It reminds me of kelp! Kelp has so many uses, like..."

            "Hours later..."
            mer "...Well, anyway, I can't wait to see the baby!"
            show mer smile
            "She smiles happily and folds her hands."
            mer " Well, I'm all storied out for today."
            "She plops down with a squelching sound."
            "You've almost forgotten the concept of silence. It's fairly alarming."
            "Maybe you should tell her a story."
            "What type of story is this?"
            menu:
                "Science fiction":
                    pass
                "Fantasy":
                    $ merPoints +=1
                "A lecture":
                    pass
            "What's the setting?"
            menu:
                "An undersea kingdom":
                    $ merPoints +=1
                "A palace in the sky":
                    pass
                "Antarctica":
                    pass
            "Who is the main character?"
            menu:
                "A plucky young sea turtle":
                    $ merPoints +=1
                "A spirited finch":
                    pass
                "A farmer":
                    pass
            if merPoints == 3:
                "Merina is entranced by your story. The moment you finish, the only thing breaking the silence is the sound of wet, squelching applause."
            elif merPoints == 2:
                "Merina claps enthusiastically."
                mer "Lovely! I sincerely enjoyed the plot, although it could have done with a bit more sea life..."
            elif merPoints == 1:
                "Merina is trying hard to hide her boredom."
                mer "Well, thank you for the story. You know, if you're looking to improve, try adding more sea life! That could be the extra touch it needs to turn from good to great!"
            else:
                "You finish the story and find that Merina is asleep."
                mer "What? No! I'm not asleep! I was just listening to your story and I'm sure you really tide, but...do you want to change the subject?"

        "Save me Prismec!":
            $ daysSpent[3]+=1
            show pris happy at left
            "Very quietly, you shimmy over to the monster next to you."
            me "She really talks a lot."
            "Prismec slams her fist into her face."
            show pris angry at left
            pris "Hey Mer-ditz! The human over here wants you to shut your big fat fish mouth!"
            show mer sad
            "Merina looks at you with wide, glassy eyes and then bursts into tears."
            pris "Just shut it, won't you?!"
            hide mer with moveoutright
            "Prismec covers her ears for a moment and then remembers you."
            show pris mad
            with move
            pris "As you can see, I live in a mad house with the idiot queen. Interview me."
            "Well, it is your job."
            "Question 1"
            me "What kind of a monster are you, anyway?"
            "Prismec flips her hair and it, along with the rest of her body, turns into bronze scales."
            show pris happier
            pris "A shapeshifter, can't you tell?"
            "She grins, not too kindly."
            show pris mad
            pris "Any other questions to waste my time with?"
            me "Actually, yes."
            "Question 2"
            menu:
                "What do you do for fun?":
                    "She kicks back against the wall."
                    show pris happy
                    pris "I mess with people."
                    $ prisPoints +=1
                "What is your favorite food?":
                    show pris unsure
                    pris "I dunno. Stuff."
                    pris "Are all your questions this boring?"
                "What is the scientific name of your species?":
                    pris "I-don't-have-a-friggin-clue-nor-do-I-care Rex."
                    show pris unsure
                    pris "Are all your questions this boring?"
            show pris mad
            "Question 3"
            menu:
                "Do you ever go on the internet?":
                    show pris happier
                    "Like heck, yes. If you ever come across anything written by LOLiHax, do me a favor and give it a like, will ya?"
                    $ prisPoints+=1
                "Are you friends with any of the monsters here?":
                    show pris mad
                    pris "Like Merina? No way."
                    "She scoffs and folds her arms."
                    show pris unsure
                    pris "Eh, I guess the thing with one thousand tentacles isn't that bad, though. And I don't mind hanging with Spinner, even though his memes suck."
                    "Huh, that's odd. Both of those monsters live at just about the other end of this complex."
                    "You can see how gossip gets around, but hanging out is a little different. Maybe it was just bad word choice on her part."
                    $ prisPoints+=1
                "What is the meaning of life?":
                    show pris mad
                    pris "Not to pepper me with meaningless questions, that's what."
            show pris mad
            "Question 4"
            menu:
                "Do you eat people?":
                    show pris happy
                    pris "Um, no. I prefer transforming into a pigeon and defecating on their heads. I can always make an exception for you, though."
                    "She smiles. You honestly can't tell if she's joking or being serious."
                    $ prisPoints +=1
                "Are you religious?":
                    show pris unsure
                    pris "All praise the great Yog-Sothulhu. May its tentacles grow ever longer."
                    $ prisPoints +=1
                "Will you be my BEST FRIEND FOREVER AND EVER AND EVER?":
                    show pris mad
                    pris "Looks like someone's still learning their social skills."
                    pris "You'll have to work a little harder for that one, kiddo. Try chatting with someone more on your level, like Merina here."
            "That seems like enough questioning for today."
        
    if merPoints >= 2:
        $ points[2]+=1
    elif prisPoints >= 2:
        $ points[3]+=1
    return

label day4MerPath:
    scene bg hall
    with fade
    $ daysSpent[2]+=1
    show mer neutral
    with dissolve
    "I have a new gaaaaaaaaaame!"
    "Here you find yourself, interviewing Merina again."
    "Honestly, at this point, you aren't even interviewing monsters anymore. You're just listening to her talk on and on and on and on."
    "This friendship thing is weird."
    "Merina grins on, oblivious to whatever you may or may not be thinking."
    show mer happy
    mer "Let's plaaaaay!"
    define noun = ""
    define adj = ""
    define verb = ""
    python:
        noun = renpy.input("I need you to give me a noun: ", length=32)
        noun = noun.strip()
        adj = renpy.input("Now an adjective: ", length=32)
        adj = adj.strip()
        verb = renpy.input("And a verb: ", length=32)
        verb = verb.strip()
    show mer neutral
    mer "Okay! I have a story for you!"
    mer "Once upon a time, there was a [adj] trout who loved to swim. It decided that it was going to enter a swimming contest!"
    mer "It packed its favorite [noun] and went to the stadium. There were a lot of other fish there! But our hero could [verb] faster than all of them, and it won! Yay!"
    "..."
    "......"
    show mer happy
    "I rate this story 10 out of 10."
    $ points[2]+=1
    return

label day5MerPath:
    scene bg hall
    with fade
    show mer neutral
    with dissolve
    "Merina is so great. You love hearing her talk and you wish you could hear her even more."
    "You dream about it every night."
    "You have even made a mixtape of her lecture on kelp."
    "Kelp is green. K-k-kelp is green."
    "I hope that you get more sleep than I do."
    $ points[2] +=1
    return

label endMer:
    show mer neutral
    with dissolve
    mer "Helooooooooooo-eeeek!"
    "Merina gasps, calling to you from the other end of the room."
    "The monster turns to her and growls. She shrieks, and you cover your ears against the sound."
    "And then the whole place is flooded with water."
    mer "Daddyyyyyyyyyyy!"
    show mer happy
    "And there he is, the sea king himself. This rescue party sure is something."
    "The sea king makes a squeaking sound like a dolphin. Merina and her several hundred siblings shoal around him."
    "\"Thou hath saveth my daughter!\" the sea king yells. You didn't actually save her, but okay."
    "\"You may now choose to stay on the land or live under the sea!\""
    menu:
        "I want to sea this":
            "\"If you are to live among us, you must have a tail!\" the sea king bawls. You clap slowly."
            "He slaps you in the face with a magic piece of kelp. Light envelops your body. You look down and yes, you are now the owner of a large, bushy squirrel tail. All of your dreams have come true. All of them."
            "You enjoy your new life as a magical mer-squirrel. You make lots of friends and on Merina's birthday, you get her a wall. She loves it and talks to it every day."
            "{b}Princess of sea and speech Ending{/b}"
            return
        "Land 4 life":
            mer "Then goodbye!"
            "Merina blows you a quick, fishy kiss as she and her family disappear under the churning waves."
            "The sea king summons an angel whale to fly you back to the surface. It has anime eyes and its whole body is bright pink. You have decided that you want to name it Frederick, in honor of nothing."
            "The joy."
            "{b}Parted in friendSHIP Ending{/b}"
            return

label day4PrisPath:
    $ daysSpent[3]+=1
    show pris happy
    with dissolve
    pris "Hey. Hey, person. [yourname], I'm talking to you. Come'ere."
    "Prismec is calling you over."
    pris "I heard about this really old and awful game the other day."
    pris "I need someone to play it with me so I can see how stupid it is."

    define guessed = False
    define guess = 0
    define count = 1
    define upperBound = 0
    define target = 0
    python:
        upperBound = renpy.input("Pick an upper bound number or something: ", length=32)
        upperBound = int(upperBound.strip())
    if upperBound <= 100:
        "Not so very quietly, Prismec whispers, \"Lightweight.\""

    pris "Great. I'm thinking of a number between 0 and [upperBound]."

    python:
        target = renpy.random.randint(0, upperBound)

    while not guessed:
        python:
            guess = int(renpy.input("Guess it: ", length=20))
        $ count += 1
        if guess == target:
            $ guessed = True
        elif guess > target:
            pris "Nope, too high."
        else:
            pris "Nah, too low."

    pris "Yep! It only took you a full [count] guesses. Not half bad."
    "She shrugs."
    show pris happy
    pris "Meh, I'd give it a 2 outta 10. Let's say we never play this again?"
    "The two of you proceed to spend the next hour guessing numbers. It's ironic and hilarious."
    $ points[3]+=1
    return

label day5PrisPath:
    show pris happy
    with dissolve
    "Ah, there's your shapeshifting friend. Merina's pen is open, and you recall hearing that she was going to get tested today. It looks like it's just you and Prismec today."
    pris "Why did the flower put on glasses?"
    "You ask why."
    show pris happier
    pris "It wanted to seed the world."
    "You and Prismec both decide that top quality jokes are unfortunately a rare breed these days."
    show pris unsure
    "She stretches for a moment, and suddenly, she looks unsure of herself."
    pris "Look, I know this is gonna sound stupid, but we're really trying to make this friendship thing work, right?"
    "You nod. Friendship is the point the game."
    pris "Good."
    show pris worry
    pris "Tbh, I was getting kinda worked up about this."
    "Her outline flickers, and suddenly she's a perfect copy of you."
    pris "Tell me honestly, though, can I trust you?"

    menu:
        "Yes":
            show pris mad
            pris "And I'm supposed to take your word for it?"
            pris "Whatevs. I can kill you in about two secs if you rat me out."
            "You're pretty sure she isn't joking about this."
            pris "Okay. I need to tell you something."
            show pris worry
            "She takes a deep breath."
            me "Is it that you actually aren't as cool as you try to be, and this is all a facade that masks the deep feelings of insecurity that haunt the darkest parts of your mind and bring up memories of your tragic and unrevealed backstory?"
            show pris unsure
            "Prismec blinks at you."
            pris "Um, that was philosophical, but no."
            pris "I was just gonna say that I can get out of my cage, and I was wondering if you'd like to hang out some time, irl."
            "Huh. There goes your theory."
            show pris happy
            "Prismec shape shifts into a flea and squeezes through a tiny, almost invisible crack in the side of the wall. There's a small pop, and then a violet-haired girl is at your side."
            "Her outfit has changed from jeans and a tank top to a T-shirt and skirt."
            pris "I just wasn't feeling that look anymore."
            "She leans against the wall."
            pris "So, I'm bored. What now?"
            menu:
                "Let us engage in an activity together. One that is hip for the kids, like pranking.":
                    show pris happier
                    pris "I like your style."
                "How the hay did you figure out how to get out and why have you not run away by now?":
                    pris "Um, have you ever tried containing a shape shifter? I figured this out, like, two days after coming here."
                    pris "It's free rent, even if Merina sucks."
                    "She shrugs."
                    show pris mad
                    pris "I'm bored. Let's go prank someone."
            scene bg elevator
            with fade
            show pris happy
            with dissolve
            "Prismec creeps down the hall. She turns back to make sure you're following, and her clothes melt into those of a Class Four. She grins."
            "The hall branches just up ahead. Prismec produces a spool of thread and hands you one end of it."
            pris "Tape it to the wall on your side."
            "Meanwhile, she measures out a length and holds it about a foot above the ground."
            "You construct the tripwire and hide off to the side with the monster girl."
            "Someone's coming."
            "Heart pounding in anticipation, you peek out to see who it is, and oh gosh, it's a Class Three researcher. Her arms are laden with a small cage, in which rests a fuzzy monster. This is actually really mean."

            menu:
                "Divert her path so she doesn't trip":
                    me "Hi! Excuse me, but I think someone was looking for..."
                    "You glare at Prismec and she rolls her eyes but disables the trap. The Class Three looks at you, a little confused, and waits for you to continue."
                    me "Never mind."
                    "The Class Three gives you a funny look, but seems to realize you meant no harm. After a quick little shrug, she adjusts her burden and continues on her way."
                    "To your surprise, Prismec doesn't tease you about this."
                "Watch the magic happen":
                    "The Class Three is completely oblivious to the trap. She walks right into it, and the crash is glorious."
                    "The fuzzy monster squeaks furiously and scampers free. While you wonder if you've just become the start of a massive breakout, Prismec seizes your arm and pulls you out of there. You run until you're out of breath."
                    pris "Look, no worries. It was just a phase mole. Harmless even to squishy lil humans."

            "It's fairly quiet now."
            "Prismec plops down on the floor and pats the space next to her. You sit down."
            "She crosses her legs and stretches, and then uncrosses them."
            pris "You tired?"
            menu:
                "Yeah":
                    pris "Same here."
                    "She glances over at you and shakes her head, giving you a half smile."
                    pris "And still bored. Great life, isn't it?"
                "Nope":
                    pris "Lucky you, then."
                    "She yawns."
                    pris "Guess I'm the lightweight now."

            "She scooches a little closer to you and folds her arms behind her back."
            pris "Wanna talk about, I dunno, life and stuff?"
            "That's a topic that never runs dry."
            pris "I guess you kinda already interviewed me, though. Must be a fun job, talking with folks all day. 'slong as the folks are interesting."
            "True."
            show pris worry
            pris "I guess if I were to have a job, I'd rather have one that lets me go places. There's a big world out there. It's a cool place to see."
            "Honestly, you haven't given much thought to traveling the world. With all the monsters, it doesn't strike you as the safest thought."
            show pris happy
            pris "Eh, it's actually way less romantic than it sounds. I mean, it looks all cool, and at first everything's different and new, but after a while, it gets kind of repetitive."
            pris "Traveling the world! Seeing the sights! Getting sore feet! Woo hoo!"
            "She starts to laugh."
            me "Okay."
            show pris unsure
            "Prismec turns away. She's starting to look tired."
            pris "I dunno, maybe the problem's with me."
            show pris worry
            pris "Maybe I do have confidence issues."
            menu:
                "Girl, you are 100 percent uncool. All your insecurities are real.":
                    "She laughs."
                    show pris happy
                    pris "You sure know how to make someone feel better. 10 out of 10 for social skills."
                    "She rolls her eyes and smiles."
                "Well, for the record, I think you're cool.":
                    "She mutters something about \"stupid sentimental humans.\" The look on her face doesn't match her words, though."
                    "She takes your hand and squeezes it lightly."
                    show pris happy
                    pris "Thanks. Really."
            show pris cata
            "Prismec is looking really tired. She morphs into a cat and crawls onto your lap."
            menu:
                "Pet her":
                    "You stroke her gently. She rolls over and purrs."
                    show pris catb
                    pris "Ah, that's the spot."
                "Leave the cat be":
                    pass
            show pris cata
            "Prismec looks up at you and gives you half a smile."
            pris "Why did the chicken cross the road?"
            "You question why."
            pris "To get to the idiot's house."
            "She shifts to get a little more comfortable."
            pris "Knock knock."
            "You ask for the identity of who is there."
            pris "The chicken."
            "I'd rate that at least a 7 out of 10."
            show pris happy
            "Eventually, you realize you've been sitting there for a while. It probably wouldn't be the easiest thing to explain if someone were to walk by and see you. You nudge Prismec, and she gets up reluctantly."
            pris "We'll have to do this again sometime."
            pris "See who can come up with the worst joke."
            "You walk away with a little extra spring in your step."
            $ points[3]+=1

        "No":
            show pris angry
            pris "Wow. K then."
            "That's all she says."
            "Brutal honesty might not be the greatest strategy the next time around."
    return


label endPris:
    show pris beast
    with dissolve
    "???" "Hey, dirtbag! That's MY human, you know?"
    "At the other side of the room, a larger monster is growling. Your attacker's ears go down and it backs away. Now it's just you and the bigger beast."
    "You're out of the frying pan and into the fire, as the older folks say."
    "???" "Oh, quit cowering and get up. What are you, an idiot?"
    show pris mad
    with dissolve
    "The beast shudders and melts into the form of a girl with short, pink hair. It is Prismec, the one and only."
    pris "Remind me why I'm stopping to save you?"
    "Remind yourself why you became friends with her?"
    show pris happy
    "Anyway, Prismec rolls her eyes and grins at you."
    pris "Well, well. It looks like SOME damsel's in distress. You're lucky I happened to be in town, kiddo. Now come on, let's get outta this mess."
    "She turns into one heck of a mare and tosses her rainbow mane."
    pris "Do you ride? No? First time for everything, then."
    "She snorts. You climb on, and Prismec more or less charges up a hundred flights of stairs."
    "Daylight is streaming through some of the wider cracks in the ceiling, and you're beginning to wonder if Prismec has any idea what she's going to do when she gets to the surface."
    show pris happier
    pris "I'm winging this, kid."
    "As you burst through the final floor, electric blue wings erupt from Prismec's equine back and she shoots into the sky. Cries, stares, and quite a few bullets follow you up for a few seconds, and then you are free."
    "You have to admit, it's quite a ride."
    "{b}Sarcastic rainbow pegasus adventure Ending{/b}"
    return

label endBad:
    "And you die."
    "{b}Bad Ending{/b}"
    return


label printPoints:
    "End of the day.\nSpinner: [points[0]]\nMisty: [points[1]]\nMerina: [points[2]]\nPrismec: [points[3]]"
    return