define p = Character(_("You"), color="#007777")
define tp = Character(_("Princess"), color="#ff7777")
define s = Character(_("Soldier"), color="#dd3333")

define inventory = []
define eProg = 1
define wProg = 1
    
label start:
    call prelude
    while (eProg < 3 and wProg < 3):
        "What will you do?"
        menu:
            "Go East"  if eProg > 0::
                call e1
            "Go West"  if eProg > 0::
                if(wProg == 1):
                    call w1
            "Examine self":
                call viewInventory
    return

label viewInventory:
    "You examine your possessions."
    python:
        inventory_text = '\n\n'.join(inventory)
    "[inventory_text]"
    "And that's it."
    return


label w1:
    "Rows of old houses, most of them crumbling, line the path into the city. You pick your way along, avoiding the potholes and dislodged flagstones. Even though it's not the same city, there are so few signs of civilization in this place that it reminds you of your home from all those years ago, before you were taken here."
    "One building seems a lot better maintained than the rest. You head over to it. It might have some canned food and water, and it will hopefully not collapse on top of your head."
    "Rummaging through the drawers, you find some stored provisions. You eat your fill and put the rest in your pack for later. Then, you exit the building and get ready to take your leave of the city."
    "As you head back outside, however, you hear footsteps and catch sight of a figure walking down the street. Its torso swivels and it turns toward you sharply, sword drawn."
    s "Halt. Identify yourself."
    "You duck beneath the window, narrowly avoiding a swipe of its sword. After a few moments, you hear the footsteps continue on. Peeping back out the window, you see that the soldier has resumed its patrol down the street. As soon as it hears you, however, it swivels back with a mechanical whir and once again draws its sword."
    s "Halt. Identify yourself."
    "The soldier seems to have a very short memory, and when he once again turns around to continue on his patrol, you see the reason why. A large key protrudes from his back, not unlike the one you would find on a windup toy. This soldier is nothing more than a life-sized toy."
    "You watch him mechanically step into another building at the end of the road. He does not come out, but another soldier, identical except for some damage around its left arm, marches out for presumably the same circuit. It appears that you've found their headquarters."
    "Deciding that that's been enough adventure for the moment, you head back to the entrance to the caverns to think things over. The troll is squatting behind a rock half its height just inside the cave, and it glances hopefully in your direction. It looks like you still have some time to kill."
    "You can either head back to the west and look into the headquarters, or explore the forest to the east."
    return

label e1:
    "You wander through the forest, the grass cool against your feet. Although the sun never rises above the glow of early dawn, songbirds and other creatures of the daytime can be heard around the trees. But no monsters leap out to devour you, and you gradually begin to relax."
    "That's when you see the tower."
    "It looks rickety but quaint. Innocent, even. You stand at the base of the structure, trying to weigh the prospect of it having food against the possibility of it having an awful abomination, when a face appears at the window."
    tp "Greetings. Welcome to my forest."
    "The girl disappears, and a window at the base of the tower slides open. She appears and blinks with her large, dark-rimmed eyes."
    tp "Hello. I'm the tower princess."
    "You would like to question how she just moved from the top of the tower to down here in three seconds flat, but the princess leans forward and continues speaking."
    tp "It's nice to meet you. My animal friends and I were just about to have some tea and biscuits. Would you like to join us?"
    "You are still very much confused over who this girl is, or what she's doing in a tower in the middle of the woods. Still, you haven't been eating too well lately, and the offer of food is too enticing to pass up."
    p "Just to be clear, they're regular animal friends, right? Not monsters or, um, bears or wolves or anything?"
    tp "Yes, they're regular animal friends. I promise, on my honor as a princess."
    p "Okay then. Sure, thanks."
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
    tp "I realize I don't have much to offer, and I apologise for it. If you'd seen how I was at the height of my power, before my sister stole my magic crown..."
    "She breaks her reminiscing off with a sigh and looks away. A mouse has perched on her shoulder, and it looks around with bright eyes. It offers the princess a sunflower seed."
    tp "Thank you, Flit."
    "The mouse scurries down her arm and into the tower. The princess's smile fades."
    tp "Of course, I do appreciate it greatly, but there's only so far one can get with the help of mice and humans and other small animal friends."
    tp "And to be candid, I'm not sure how much longer I'll be able to stay hidden from my sister."
    "She gives yet another sigh and then seems to remember you."
    tp "Oh, what's wrong with me, burdening a guest with my woes? I'm sorry, I'm all out of sorts and not presentable in the slightest. Pardon my manners, I believe I ought to return to bed. Oh, I've such a headache..."
    "She closes the window, one hand against her forehead. Suddenly, she is back at the top of the tower, opening the upper window."
    tp "Please, help yourselves to the rest of the biscuits."
    "Well fed, you return to the entrance of the caverns and look around. The cave troll has resorted to all the cunning its pea-sized brain can muster, and it's now attempting to pretend to be a rock. This ruse would be far more effective if it didn't stop to scratch it's rear every twelve seconds."
    "Well, it looks like it will still be some time yet before you can return to your sleeping nook. You can either head back to the east and agree to help the princess, or explore the ruins to the west."
    $ eProg += 1
    return

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
