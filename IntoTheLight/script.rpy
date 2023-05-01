define p = Character(_("You"), color="#007777")
define tp = Character(_("Princess"), color="#ff7777")
define s = Character(_("Soldier"), color="#dd3333")
define cc = Character(_("Clockwork Council"), color="#eebb00")

define inventory = []
define eProg = 1
define wProg = 1


label start:
    scene bg cave
    call prelude

    while (eProg < 5 and wProg < 5):
        menu:
            "What will you do?"
            "Go to the forest" if eProg > 0:
                if(eProg == 1):
                    call e1
                elif (eProg == 2):
                    call e2
            "Go to the ruins" if wProg > 0:
                if(wProg == 1):
                    call w1
                elif (wProg == 2):
                    call w2
                elif (wProg == 3 or wProg == 4):
                    call w3
            "Go to the field beyond the ruins" if wProg == 3:
                call field
            "Examine self":
                call viewInventory
    return

label viewInventory:
    "You examine your possessions."
    define i = 0
    define inventory_text=""
    while i<len(inventory):
        python:
            inventory_text += inventory[i]
        $i += 1
        "[inventory_text]"
        $inventory_text=""

    "And that's it."
    return

label field:
    scene bg black
    scene bg skyhookcrack with Dissolve(5.0):
        size (1920, 1080) crop (0, 140, 1280, 720)
        linear 4 crop (160, 140, 1280, 720)
    scene bg skyhookcrack with fade
    "You pass the ruins and head into the field beyond. The eternal light of dawn bathes everything in a weak glow, and you search the grass for a golden thread. The sky above is marred by thin cracks, through which seeps a darkness blacker than night."
    "A single golden thread could be anywhere. Your fruitless search lasts for hours, and you eventually have to sit down for a rest. The sky above you darkens as though from a passing cloud, but there are no clouds in this place."
    scene bg skyhooks with dissolve
    "Looking up, you see that the cracks have widened. Ropes as thick as your waist descend through the cracks, and each rope is tipped with an iron hook. One of them is hanging just above your head."
    "You take a moment to consider your options."
    menu:
        "Flee the SkyHooks":
            pass
    "Deciding that this is the best idea, you begin to run. At least, you would begin to run, if you weren't currently feeling a cold metal hook against your skin and not feeling the ground under your feet."
    "The unnaturally cold hook dangles you a good ten feet above the ground, and other hooks migrate closer in case you manage to wiggle free."
    menu:
        "Fight the SkyHooks":
            pass
    "You are comparatively the size of a pea and presumably just as squishy. All the same, you punch one of the hooks that is closing in on you."
    "Your fist clenches in pain, and the hook barely sways."
    menu:
        "Commune with the SkyHooks":
            pass
    "You're not even sure if all these hooks are one entity or individual creatures, but in the most polite and not-panicky way you can currently manage, you ask what the SkyHooks want."
    "To your surprise, the SkyHooks deign to respond:"
    define longShake = Move((25, 0), (-25, 0), .20, bounce=True, repeat=True, delay=.5)
    scene bg skyhooksleep with longShake
    $renpy.pause()
    scene bg skyhookless with fade
    "You wake up in the field. The cracks in the sky are gone, as are the SkyHooks. You have the unpleasant feeling that all your internal organs have been removed and poked at, but at least the SkyHooks were polite enough to put you back together once they were finished."
    "Oh, hey, there's also a dead body next to you. It's holding a golden thread and appears to be one of the thieves who stole it from the Toymaker. The Clockwork Council will be pleased."
    $wProg += 1
    return

label w1:
    scene bg black
    scene bg city with Dissolve(5.0):
        size (1920, 1080) crop (0, 140, 1280, 720)
        linear 4 crop (160, 140, 1280, 720)
    scene bg city with fade
    "Rows of old houses, most of them crumbling, line the path into the city. You pick your way along, avoiding the potholes and dislodged flagstones that mark your path. Even though it's not the same city, there are so few signs of civilization in this place that it reminds you of your home from all those years ago, before you were taken here."
    "Eventually you reach a set of buildings that seem a lot better maintained than the rest, and you head over to one of them. It might have some canned food and water, and it will hopefully not collapse on top of your head."
    "Rummaging through the drawers, you find some stored provisions. You eat your fill and put the rest in your pack for later. Then, you exit the building and get ready to take your leave of the city."
    python:
        inventory.append("A can of food. The writing is in a language you don't recognize, but the stuff inside seems edible.")
    "As you head back outside, however, you hear footsteps and catch sight of a figure walking down the street. Its torso swivels and it turns toward you sharply, sword drawn."
    s "Halt. Identify yourself."
    "You duck beneath the window, narrowly avoiding a swipe of its sword. After a few moments, you hear the footsteps continue on. Peeping back out the window, you see that the soldier has resumed its patrol down the street. As soon as it hears you, however, it swivels back with a mechanical whir and once again draws its sword."
    s "Halt. Identify yourself."
    "The soldier seems to have a very short memory, and when he once again turns around to continue on his patrol, you see the reason why. A large key protrudes from his back, not unlike the one you would find on a windup toy. This soldier is nothing more than a life-sized doll."
    "You watch him mechanically step into another building at the end of the road. He does not come out, but another soldier, identical except for some damage around its left arm, marches out for presumably the same circuit. It appears that you've found their headquarters."
    "Wisely deciding that the headquarters of a bunch of life-sized toy soldiers armed with distinctly not-toy weapons is not the place you'd like to go, you creep back the way you came, intending to head back to the caverns. Unfortunately for you, you seem to have misjudged the soldiers' route and run into one on your way out."
    s "Halt. Identify yourself."
    "Unfortunately, it doesn't take 'please let me go' as a valid identification. The soldier drags you back down the path and into the headquarters, ignoring your struggles. It takes you into the building and heads over to a pile of junk, where several other toy soldiers are standing at attention."
    s "Intruder apprehended. Awaiting orders."
    "It goes still, but its grip holds firm. The other soldiers also remain motionlessly at attention, guarding their pile of junk."
    "Except, as you look closer, you realize that it isn't a pile of junk. It's a pile of broken toy soldiers and windup dolls and other old clockwork toys, all melted together in a heap. Scores of painted eyes examine you, and when the dozen mechanical mouths that still function open, a cacophony of voices speaks to you."
    cc "You are not a toy. Why do you intrude upon our domain?"
    "You attempt to give a reasonable explanation for your presence, which breaks down into sobbing hysterics after about two words. The Clockwork Council grumbles in annoyance, cutting you off."
    cc "This one is harmless. Leave, before I grow more vexed with your presence."
    "You gratefully scamper toward the exit. Unfortunately, the toy solders guarding it cross their swords and block it."
    s "Intruder apprehended. Awaiting orders."
    "A few of the Clockwork Council's heads look up from the map it's studying and give a dismissive nod for them to let you go."
    "This would be all well and good, except that there are at least a dozen toys on patrol outside. You make it as far as the street before they bring you back. The Council looks more than slightly annoyed to see you again, and even more annoyed when two of the soldiers bump into one another and domino-fall the who lot into a flailing heap."
    cc "Idiots. We deserve better than this, cast away to this forsaken outpost with cogs-for-brains soldiers as our only assistants."
    cc "If they would just find the last of those golden threads, we could leave this scrap heap and focus on more important tasks."
    "Its mechanical jaws clatter and it deliberates with itself for a moment. It looks at you, deciding if you might just be a step up from a cogs-for-brains toy."
    cc "Fine. Since you seem so intent on showing up here, we will allow you to assist us. I am in good standing with my master, and if you can find our last golden thread, you will not find us ungrateful."
    "You twitch uncomfortably. You know nothing about golden threads or how they might be obtained, but you're pretty sure the Council won't stab you in the back if you help it. The monsters here are real sticklers about reciprocity."
    cc "Consider it. Now, to deal with these toys."
    "After the soldiers get up and receive some detailed orders on how they are not to apprehend any intruders for the next five minutes, you make your escape and head back to the entrance to the caverns to think things over. The troll is squatting behind a rock half its height just inside the cave, and it glances hopefully in your direction. It looks like you still have some time to kill."
    "You can either head back to the west and return to the Council, or explore the forest to the east."
    $wProg += 1
    return

label w2:
    "Finding the Council is easy. Within half an hour of entering the city, one of the soldiers is once again dragging you before the conglomerated abomination. It tells you to state your business, and that it hopes for both your sakes that this is for something important."
    $done=False
    while not done:
        cc "For what have you come?"
        menu:
            "I'll help you find your golden thread.":
                $ wProg += 1
                $ eProg = 0
                cc "Your assistance is, of course, appreciated."
                "It produces a map."
                cc "By our calculations, it should be in the field just past these ruins. The soldiers found the other threads here, but this last one has been eluding them."
                cc "A word of warning: the threads do tend to strangle anyone who attempts to steal them, so we suggest that you bring it here promptly and not get any ideas about taking it for yourself."
                "You assure the Council that you will return with the thread promptly, no threats of violence needed."
                $done=True
            "I have a few questions.":
                call askCouncil
            "Never mind, I have some things to take care of first.":
                "The Clockwork Council mutters that it would be simpler to kill you if it didn't make so much of a mess, but it calls off the soldiers and you make your escape. The troll is still maintaining its vigil at the entrance of the caverns."
                $done=True
    return

label w3:
    "You head back to the ruins and the Clockwork Council. A head and uniformed torso are budding off of it, twitching slightly. The new soldier steps off, fully formed, and stands at attention."
    cc "Why have you come?"
    $done = False
    while not done:
        menu:
            "I've found the thread." if wProg == 4:
                $ wProg += 1
                cc "Excellent."
                "Several hands take it from you and pluck it taught. The Council examines it."
                $done=True
            "I have a few questions.":
                call askCouncil
            "Never mind, I have some things to take care of first.":
                "The Clockwork Council looks disinterested and waits for you to leave."
                $done=True
    return

label askCouncil:
    $ stillTalking = True
    while stillTalking:
        menu:
            "Who is your master?":
                "The Council practically glows with pride."
                cc "I serve the Toymaker, greatest of the masters of this land."
                "Ah. You don't know much about the Toymaker, only that he's one of the capricious gods of this land and that he enjoys paralyzing people to make them into dolls. All the 'fate worse than death' stuff in this place is pretty par for the course at this point."
            "What would you do if you had this golden thread?":
                cc "Take it and the other threads to my master, of course."
                "You ask what its master plans to do with the threads. The Council fixes you with a dozen steely glares."
                cc "Ours is not to reason why, but he surely has his objectives."
                "It's a fair enough answer. A small mortal speck like you couldn't possibly fathom the motives of one of the masters of this land, but if he wants a bunch of golden threads, you're sure he has his reasons."
            "How did the golden threads go missing?":
                cc "It was stolen by servants of the Glass Weaver. No doubt the thieves were strangled by the threads, but they'd already taken them past the bounds of his domain. We hope to return them quickly, before more servants are sent, but this last thread is eluding us."
                "Oh, you know about the Glass Weaver. She was the one who'd killed your old master. You'd been lucky to be working by the caverns that day, and you've been hiding down there pretty much until now."
            "That's enough questions for now.":
                $ stillTalking=False
    return

label e1:
    scene bg black
    scene bg pines with Dissolve(5.0):
        size (1920, 1080) crop (0, 140, 1280, 720)
        linear 4 crop (160, 140, 1280, 720)
    scene bg pines with fade
    "You wander through the forest, the grass cool against your feet. Although the sun never rises above the glow of early dawn, songbirds and other creatures of the daytime can be heard around the trees. But no monsters leap out to devour you, and you gradually begin to relax."
    "That's when you see the tower."
    "It looks rickety but quaint. Innocent, even. You stand at the base of the structure, trying to weigh the prospect of it having food against the possibility of it having an awful abomination, when a face appears at the window."
    tp "Greetings. Welcome to my forest."
    "The girl disappears, and a window at the base of the tower slides open. She appears and blinks with her large, dark-rimmed eyes."
    tp "Hello. I'm the tower princess."
    "You would like to question how she just moved from the top of the tower to down here in three seconds flat, but that would be rude. The monsters here seem to have a very good sense of manners, even if they don't quite understand concepts such as 'mercy'."
    tp "My animal friends and I were just about to have some tea and biscuits. Would you like to join us as a guest?"
    "This makes you pause. The rules against hurting guests here rival those of ancient Greece, meaning that your safety is guaranteed while you're in the princess's domain. And moreover, as any food and drink given to a guest counts as a gift, you won't be in her debt for this. You're still wary of who this princess is and what her goals are, but you haven't been eating too well lately, and a free meal is too good to pass up."
    "Just to be on the safe side, you do ask if her animal friends are bears or wolves or monsters or anything dangerous. The princess assures you that they are indeed regular animal friends."
    tp "I promise, on my honor as a princess."
    "You thank the lovely princess and prepare to attend her tea party."
    "The tower princess extends a hand and begins to sing. Sparrows and squirrels and a dozen mice swarm the tower. True to her word, only normal animals are present, although one of the badgers looks surly enough to attack anyone who tries to pet it."
    tp "Please, take a biscuit. I'll start brewing the tea."
    "She steps away from the window and retrieves a plate of biscuits from the tower's pantry. She hands one to you, picks up one herself, and passes the rest over to the animals. As they begin to eat their share, you take a tentative bite. It's buttery and melts in your mouth, and reminds you of just how hungry you are. You devour the rest of it with significantly less grace than the princess."
    tp "You're welcome to have a second one. I have plenty."
    "A curious squirrel perches on your shoulder and flicks its tail. The princess plays idly with her hair and looks to the side, closing her eyes."
    tp "It's nice to have a few moments of peace, just sitting with friends. I can pretend for a moment that the world isn't filled with awful things vying for power. If I close my eyes, I can almost convince myself that it's peaceful."
    "The kettle whistles and her eyes flutter open."
    tp "Oh, the tea's ready."
    "She sets down the remaining half of her biscuit and gets up. When she goes to the stove to retrieve the kettle, you realize that you can't recall her turning it on."
    tp "Let me see...ah, we'll need teacups."
    "She hums at the squirrel on your shoulder, which scampers off to sit in front of her. The tower princess strokes one manicured hand along its spine, and it flattens out. Its arms and legs disappear as the skin stretches into a mat. The princess brings up the edges of the flattened creature, giving it the shape of a cup. The squirrel's tail curves to form a handle, which she picks up to pass over to you."
    tp "Here, you can have this one."
    "You very politely decline the furry teacup, the handle of which is still twitching."
    "The princess reshapes the teacup into a squirrel, which scampers back to the remaining biscuits. She takes a small sip of her own cup, which had previously been a robin, and sighs."
    tp "I realize I don't have much to offer, and I apologise for it. If you'd seen how I was at the height of my power, before my sister stole my crown..."
    "She breaks her reminiscing off with a sigh and looks away. A mouse has perched on her shoulder, and it looks around with bright eyes. It offers the princess a sunflower seed."
    tp "Thank you, Flit."
    "The mouse scurries down her arm and into the tower. The princess's smile fades."
    tp "It's not a paradise that we've carved out here, but it's peaceful, and there's only so much I can do in this diminished state."
    tp "And to be candid, I'm not sure how much longer I'll be able to stay hidden from my sister."
    "She gives yet another sigh and then seems to remember that you're still present."
    tp "I'm sorry, I shouldn't be burdening a guest with my woes. I'm all out of sorts and not presentable in the slightest. Pardon my manners, I believe I ought to return to bed. Oh, I've such a headache..."
    "She closes the window, one hand against her forehead. Suddenly, she is back at the top of the tower, opening the upper window."
    tp "Please, help yourselves to the rest of the biscuits."
    python:
        inventory.append("A half-eaten biscuit. The half appears to have been eaten by a squirrel.")
    "You snag one more biscuit and return to the entrance of the caverns. The cave troll has resorted to all the cunning its pea-sized brain can muster, and it's now attempting to pretend to be a rock. This ruse would be far more effective if it didn't stop to scratch it's rear every twelve seconds."
    "Well, it looks like it will still be some time yet before you can return to your sleeping nook. You can either head back to the east and agree to help the princess, or explore the ruins to the west."
    $ eProg += 1
    return

label e2:
    "You head back into the forest and find the tower princess. Her animal friends are still eating happily, and the princess herself gazes out the tower, watching you approach."
    tp "Hello again. Did you need something?"
    $ done = False
    while not done:
        menu:
            "I've decided to help you get your crown.":
                $ eProg += 1
                $ wProg = 0
                "The princess looks surprised. After a moment she closes the upper window and, with inhuman speed, is back at the base of the tower."
                tp "You would do this for me?"
                "Whatever motive you have, be it out of genuine kindness or simply the chance to have a powerful creature in your debt, you nod."
                "The princess turns away, looking stricken."
                tp "I...could not ask you to brave this danger for me. No more than I could ask Flit and his mice to face her armies."
                tp "My sister is for me to face alone. But if...if you do wish to help me, I would appreciate it."
                "She pulls herself up, looking tired but regal."
                tp "If you wish it, there is one whose help we may be able to procure, though I am in hiding here and cannot enlist him myself. If you could deliver a message to him and let him know where I am, I would be most grateful."
                tp "You would be looking for Jack Fetcher. He's one of Lady Luck's men, but he owes me a favor. I shall mark the location of his favorite haunt, where you are sure to find him."
                tp "Flit would have delivered the message to him ages ago, but Jack has a fondness for mouse pie. I appreciate the help of mice and humans and other small animals, but this world is a dangerous place."
                $ done=True
            "I have a few questions.":
                call askPrincess
            "Never mind, I have to do something else first.":
                "You excuse yourself and head back to the entrance of the caverns, where the troll is still waiting hopefully."
                $ done=True
    return
label askPrincess:
    $ stillTalking = True
    while stillTalking:
        menu:
            "Why did your sister take your crown?":
                tp "That's easy. It's for the same reason everyone does anything around here: power. She didn't want to share, and here we are."
            "What would you do if you had your crown back?":
                "The princess sighs. You've noticed she does this often."
                tp "It is, of course, only a dream, but I would like to see this place change."
                tp "You realize how cruel it is here, I'm sure. Strong creatures prey on the weak, and just about the only way to stay alive is to indenture oneself to one of the masters of this place. It's not right."
                tp "If I could regain my crown and restore myself to my full power, maybe I could make a difference. I could bring the peace of this place to more of the world. It's merely an idea, of course, and my sister very well may catch me long before it comes to pass."
            "That's enough questions for now.":
                $ stillTalking=False


label prelude:
    "It appears that your day has been off to a rough start. After leaving the relative safety of your sleeping nook this morning, you went out wandering the caverns in search of food. Unfortunately, a very large cave troll was also searching for food, which it appears to have found, as it has found you. You started running and just paused for breath a few seconds ago, and it looks like we're pretty much caught up to the present."
    "And that was excellent timing, as the cave troll has just picked up your scent again. It roars and charges, and once again you find yourself on the run. Scurrying up the tunnel, your frantic flight takes you to the entrance of the caverns. The weak light hurts your eyes, but you don't stop until you're fully outside. Only then do you allow yourself to turn back."
    "The troll stops short of the entrance. Pacing angrily, it skirts the edge of the darkness, deprived of its breakfast. It looks like you won't be heading back to your sleeping nook anytime soon."
    "Well, if you're stuck out here for the day, you'd like to make the most of it and procure some breakfast. You take stock of your surroundings, squinting in the eternal dawn's light."
    "To the right, a forest stretches on as far as you can see. To the left are the ruins of an old city. There are likely monsters in both directions, so take your pick."
    python:
        inventory.append("A small dagger, more useful for skinning rats than fending off monsters.")
        inventory.append("The tattered livery of your old master. It doesn't mean much now that he's dead.")
        inventory.append("Fifteen dollars worth of American bills and coins. Such currency is useless in this land.")
    return