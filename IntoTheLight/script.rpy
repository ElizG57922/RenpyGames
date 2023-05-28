define m = Character(_("Captive Lass"), color="#007777")
define jf = Character(_("Jack Fetcher"), color="#007700")
define tp = Character(_("Tower Princess"), color="#ff7777")
define s = Character(_("Toy Soldier"), color="#dd3333")
define cc = Character(_("Clockwork Council"), color="#eebb00")

define inventory = []
define eProg = 1
define wProg = 1


label start:
    scene bg cave with fade
    call prelude

    while (eProg < 5 and wProg < 5):
        menu:
            "What will you do?"
            "Go to the forest" if eProg > 0:
                if(eProg == 1):
                    call e1
                elif (eProg == 2):
                    call e2
                elif (eProg == 3):
                    call e3
                elif (eProg == 4):
                    call e4
            "Go to the ruins" if wProg > 0:
                if(wProg == 1):
                    call w1
                elif (wProg == 2):
                    call w2
                elif (wProg == 3 or wProg == 4):
                    call w3
            "Search the field beyond the ruins" if wProg == 3:
                call field
            "Head to Jack's casino" if eProg == 3:
                call casino
            "Examine self":
                call viewInventory
    menu:
        "Prepare for the coronation" if eProg == 5:
            call e5
        "Visit the Artful Savant's realm" if wProg == 5:
            call craft
    return

label viewInventory:
    "You examine your possessions."
    $i = 0
    $inventory_text=""
    while i<len(inventory):
        python:
            inventory_text += inventory[i]
        $i += 1
        "[inventory_text]"
        $inventory_text=""
    "And that's it."
    return

label craft:
    scene bg black
    scene bg craft with Dissolve(5.0):
        size (1920, 1080) crop (0, 140, 1280, 720)
        linear 4 crop (160, 140, 1280, 720)
    scene bg craft with fade
    "The Artful Savant's realm appears to be the result of if a dozen craft shops became locked in mortal combat with one another. Colored cotton balls, fancy scissors, and other craft supplies form crude walls hundreds of feet high, and haphazard piles of the stuff make this place a labyrinth. You're not even sure if there is a ceiling. If you look far enough in one direction, the distance seems to warp."
    "There is a sound like slow squelching, and the Council nudges you forward."
    cc "He will be here soon. You'd best make yourself scarce."
    "You take off in the direction opposite from the squelching, not pausing for breath until your lungs scream for it. Looking around, you see that you are in a cavernous room. The walls glitter with sequins, and the dyed popsicle sticks that cover the floor provide a smooth surface to walk upon. Not a single living thing moves, and you cannot even hear the normally ubiquitous sound of insects."
    "Deciding it's best to keep moving, you keep walking. After a few minutes, you end up in a smaller room. A cage lies in the corner, and through the pipe-cleaner bars a pair of very human, very alive eyes stares back at you."
    m "What are you doing here? Hurry, and escape while you still can!"
    "You acknowledge that you are very much trying to escape and then ask if she knows where the Artful Savant keeps the keys to the cage, since you'd like to get her out."
    m "Oh, that's his proper name? I've just been calling him the Craft Clump. Though I don't suppose it matters much in the end."
    "You retrieve the keys from the shelf she's been pointing at and unlock the cage. The girl stumbles out."
    m "Thank you."
    $done=False
    while not done:
        menu:
            "How did you come to this place?":
                m "I displeased my mistress and was sent here as a punishment."
                m "Before then...I was a student. Times were difficult and, well, I suppose we've all made some bad deals to get here."
            "What do you think the Savant wanted with you?":
                m "I fear that he was just waiting for me to die. He has no use for living things."
                m "What he planned for me after that, I cannot guess."
            "Done talking":
                $done=True
    "You also ask if, by any chance, she might know where the tweezers might be."
    m "Tweezers? I might."
    "She heads over to a shelf and, after a bit of rummaging, produces a sufficiently magical-looking pair of tweezers. You use them to remove the golden thread. "
    "Awesome! You've gotten free of the golden thread and can now rest assured that your chance of being strangled by it has decreased. It is a good thing that you have gotten out of one predicament, as you've just heard the squelching sound that marks the arrival of a new one."
    m "The Savant is coming! Hurry, we must escape!"
    "She pulls you along. Racing after her, you cannot help but glance behind you when you turn the corner."
    "The Savant is crawling after you. Crawling, yes, that is an appropriate description. It heaves the tangle of yarn it calls a body along the floor, and the glitter glue oozing from its base sticks and unsticks with every step, making the squelching sound. Hundreds of googly eyes sway in your direction. In that instant, you round the corner and lose sight of the monster."
    "And then, far in front of you, a spot of hope. The Clockwork Council is tapping the floor with its many hands, wondering just how badly you've screwed things up. And, much closer, a swirling portal."
    "You're struck with the sudden fear that the Council thinks you've outlived your usefulness and will leave you to your fate as soon as it has the thread. The girl tugs you forward, pulling you away from the portal with such terror that she seems to fear it will lash out and seize her. If you want to go through it, you only have a few more seconds to make that decision before you're pulled past it."
    menu:
        "Go through the portal":
            call wEnd1
        "Go to the Council":
            call wEnd2
    return

label wEnd1:
    "You tug the girl into the portal. You hear a groan from the Clockwork Council, but it's already far away.Blinking, you examine your new surroundings."
    "You appear to be in a toy shop, but everything is scaled up. Scraps of fabric, paintbrushes, and gears pile up in bins that would outsize a mature tree. There's an organized, yet slightly chaotic air to this place."
    m "No no no no no no no no no no no no no no no no no no no no no no..."
    m "We're in the Toy Maker's workshop!"
    "She takes off, screaming. You follow, but lose sight of her in the labyrinthine halls of the workshop. Like the Artful Savant's domain, this place has no natural sounds."
    "In the distance, you see a group of people."
    "After the people do not respond to your calls, you approach and realize why. Several sport mortal wounds, which have been sewn shut with garish orange thread. Their eyes have been replaced with colored marbles, and though their mouths have been sewn shut, clumps of yarn hang from between their lips."
    "The one closest to you is holding a sword up to his own throat, but he never quite made it. His cheeks are still flushed with life."
    "And just when you think that it can't get much worse, you sense a presence in the room. Turning around, you see the sad face of an old man, so large that you feel like a doll in comparison. No, you see a giant toy soldier. A windup lion. A tangle of rainbow ribbons. He puts down the doll he's been working on and reaches you in one massive step."
    "Crouching down, he speaks in a voice that sounds like used razors. The words are incomprehensible, but you see that he is pointing at the golden thread clutched in your hand."
    "You drop the thread and attempt to explain that you are returning the thread rather than taking it, but you find you can't speak. There's something at the back of your throat, and when you cough to clear it, you end up pulling out a glob of bright orange threads. Oh, that's not supposed to be there."
    "He picks up the thread with one old, wrinkled hand (or is it a gnarled mechanical claw?), and it winds happily around his fingers. He places it in his heart, which ticks just a little brighter."
    "You get the sense that, even though you're unsure whether he's about to reward or punish you, he doesn't want you to be crying. You get the sense that he wants you to smile, that it would look prettier if you smiled, and that it would be perfect if you never stopped. Dolls should look happy, after all, the Toy Maker's thought tell you."
    "Your thoughts tell the Toy Maker to buzz off, albeit with more expletives."
    "The Toy Maker reminds you that dolls are not supposed to think."
    "His thoughts flood into yours, overwhelming any sense of being you may have once had. It's like attempting to fill a cup with the ocean. Nothing of you could possibly remain when faced with the absolute surety of his will."
    "Hah."
    "Hah, hah."
    "...hah."
    show bg badCity
    centered "End"
    return

label wEnd2:
    "You bolt to the safety of the Clockwork Council, which whisks both you and the girl back to the ruins. The Council takes the thread and decides that everything is satisfactory."
    cc "Our master will be well pleased to have this back."
    cc "Although your antics have been sometimes unbearable, we must confess that you have been a useful servant."
    "You decide to take this as a compliment."
    cc "In fact, if you chose it, we would even be willing to take you in as an assistant."
    "You politely decline, informing it that the last time you took that kind of offer, all the wonderful complexity of your life was replaced with two rules: Obey your master and be rewarded, and disobey him and be punished. And since his rewards typically involved copious amounts of body horror, that really meant that there was one rule, which was to stay off his radar as often as possible."
    cc "Of course. Well, we suppose you deserve some reward."
    "You and the girl look at one another. You both agree that you would very much like to go home."
    cc "Very well then. Why you would wish to return to that dull place is beyond us, but you've proven your merit. At least it gets the two of you out of my wires."
    "It nonchalantly creates a portal and several arms direct you and the girl through it. You get the sense that it will miss you, but hey, you've made it home!"
    show bg goodCity
    centered "End"
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
        "Flee the Sky Hooks":
            pass
    "Deciding that this is the best idea, you begin to run. At least, you would begin to run, if you weren't currently feeling a cold metal hook against your skin and not feeling the ground under your feet."
    "The unnaturally cold hook dangles you a good ten feet above the ground, and other hooks migrate closer in case you manage to wiggle free."
    menu:
        "Fight the Sky Hooks":
            pass
    "You are comparatively the size of a pea and presumably just as squishy. All the same, you punch one of the hooks that is closing in on you."
    "Your fist clenches in pain, and the hook just sways a little closer."
    menu:
        "Commune with the Sky Hooks":
            pass
    "You're not even sure if all these hooks are one entity or individual creatures, but in the most polite and not-panicky way you can currently manage, you ask what the Sky Hooks want."
    "To your surprise, the SkyHooks deign to respond:"
    define longShake = Move((25, 0), (-25, 0), .20, bounce=True, repeat=True, delay=.5)
    scene bg skyhooksleep with longShake
    $renpy.pause()
    scene bg skyhookless with fade
    "You wake up in the field. The cracks in the sky are gone, as are the Sky Hooks. You have the unpleasant feeling that all your internal organs have been removed and poked at, but at least the Sky Hooks were polite enough to put you back together once they were finished."
    "Oh, hey, there's also a dead body next to you. After overcoming your initial horror, you realize that it has a golden thread wrapped around its neck. It appears you've found one of the thieves. The Clockwork Council will be pleased."
    "As you gingerly reach to pick it up, it unwinds from the thief's neck and coils around your wrist. As it does so, you feel a flash of strange happiness, as though you're witnessing the memories of a toy in the hands of a loving child. When the feeling passes, you find that the thread has wrapped fully around your wrist and cannot be coaxed off."
    "Hopefully the Clockwork Council will be able to remove it. You'd best return to the ruins."
    python:
        inventory.append("A golden thread. Touching it makes you feel strangely happy and carefree.")
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
    scene bg city with fade
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
                cc "A word of warning: the threads do have minds of their own and tend to strangle anyone who attempts to steal them, so we suggest that you bring it here promptly and not get any ideas about taking it for yourself."
                "You assure the Council that you will return with the thread promptly, no threats of violence needed."
                $done=True
            "I have a few questions.":
                call askCouncil
            "Never mind, I have some things to take care of first.":
                "The Clockwork Council mutters that it would be simpler to kill you if it didn't make so much of a mess, but it calls off the soldiers and you make your escape. The troll is still maintaining its vigil at the entrance of the caverns."
                $done=True
    return

label w3:
    scene bg city with fade
    "You head back to the ruins and the Clockwork Council. A head and uniformed torso are budding off of it, twitching slightly. The new soldier steps off, fully formed, and stands at attention."
    cc "Why have you come?"
    $done = False
    while not done:
        menu:
            "I've found the thread." if wProg == 4:
                $ wProg += 1
                cc "Excellent."
                "Several hands reach for it and pluck it taught. The thread does not unwind from your wrist."
                "You politely request that, if it's not too much trouble, would the Council mind taking the thread before it starts strangling anyone (i.e. you)?"
                cc "We are trying, but it appears there are...complications. The threads have minds of their own, and this one seems to have taken a liking to you. Why in the daylights it would want that, we cannot begin to guess."
                "You choose to not comment on the insult and instead politely inquire if there might be a way to get the thread off, preferably without it strangling you in the process."
                cc "A peer of ours, a fellow servant of the Toy Maker, may have something that can help. He's an expert at craft-making, and his tweezers are said to be capable of untangling any string. If anything aside from the Toy Maker himself can remove this thread, it will be that. And we believe that all parties would prefer it if the Toy Maker did not need to get involved."
                cc "The only caveat is that this peer of ours, the Artful Savant, has few organics in his realm. The concept of life...confuses him, and it may be best if he does not see you."
                "With a tremendous creaking noise, the Council lifts itself up to stand on its plethora of bent and rusted legs. It scuttles toward the wall, reminding you somewhat of a crab."
                cc "We can get you into the Savant's realm and do what we can to keep him occupied while you find the tweezers. We trust, of course, that you will return them and not get caught. We would, after all, still like to return the threads to our master, and would prefer to not have to track down another corpse."
                "You assure the Council that you will try your best, and you watch it create a portal on the wall to the Artful Savant's realm."
                $done=True
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
                cc "We serve the Toy Maker, greatest of the masters of this land."
                "Ah. You don't know much about the Toy Maker, only that he's one of the capricious gods of this land and that he enjoys paralyzing people to make them into living dolls. Just more 'fate worse than death' stuff that's pretty par for the course at this point."
            "What would you do if you had this golden thread?":
                cc "Take it and the other threads to my master, of course."
                "You ask what its master plans to do with the threads. The Council fixes you with a dozen steely glares."
                cc "Ours is not to reason why, but he surely has his objectives."
                "It's a fair enough answer. A small mortal speck like you couldn't possibly fathom the motives of one of the masters of this land, but if he wants a bunch of golden threads, you're sure he has his reasons."
            "How did the golden threads go missing?":
                cc "They were stolen by servants of the Glass Weaver. No doubt the thieves were strangled by the threads, but they'd already taken them past the bounds of our master's domain. We hope to return them quickly, before more thieves are sent, but this last thread is eluding us."
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
    tp "Greetings, little one. Welcome to my forest."
    "The girl (who has no right to call you 'little', seeing as she is shorter than you) disappears, and a window at the base of the tower slides open. She appears and blinks with her large, dark-rimmed eyes."
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
    tp "I realize I don't have much to offer, and I apologise for it. If you'd seen how I was at the height of my power, before my sister stole my magic crown..."
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
    scene bg pines with fade
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
                tp "If you wish it, there is one whose help we may be able to procure, though I am in hiding here and cannot enlist him myself. If you could deliver a message to him and let him know that I offer him a wager, I would be most grateful."
                tp "You would be looking for Jack Fetcher. He's one of Lady Luck's men, but I've had deals with him before. I shall mark the location of his favorite haunt, where you are sure to find him."
                tp "Flit would have delivered the message to him ages ago, but Jack has a fondness for mouse pie. I appreciate the help of mice and humans and other small animals, but this world is, alas, a dangerous place."
                "You promise you'll be careful, and look at the map she's drawn up. It seems that Jack Fetcher likes hanging out at the Sungrave Casino, which shouldn't be too far away."
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
    return
label e3:
    scene bg pines with fade
    "You head back to the Tower Princess. She is chatting with one of the squirrels."
    tp "Hello, can I get you anything?"
    "You hang out for a few minutes before deciding that you should really get back to working on your goal."
    return

label e4:
    scene bg pines with fade
    "You and Jack head deep into the woods. The tower rises before you, looking even more decrepit in the early light."
    tp "Greetings, Jack Fetcher. Welcome to my forest."
    "The princess stands at the window, her face wreathed in shadow. Flit perches on her shoulder. His bright eyes are fixed on Jack, but he stands his ground."
    jf "All right, princess, what's your wager? This had better be worth my while."
    tp "It shall be. I ask only that you hold contest with me in a game of trivia. If I win, you must steal back my crown from my wicked sister."
    jf "And if I win? What, will you make me a king? Is that a thematically appropriate reward?"
    "The princess considers it for a moment."
    tp "That can be arranged."
    jf "Then I accept your wager. But what would a lass like you even know of old lore? Out of fairness, I'll start with an easy one."
    jf "What became of the Glass Weaver's muse, three centuries past?"
    tp "He was devoured whilst the Weaver created her magnum opus. She commemorates him in her webs and lamentations, still weeping today."
    tp "What was the color the Carrion King's waistcoat when he rode into battle in his conquest of the cobbled roads?"
    jf "None, for he wore only his own black feathers that evening."
    "And so it goes, question after question."
    jf "What is the final destination of the River Eternal?"
    "The princess does not answer right away."
    tp "It...it has no end, but rather loops into itself forever."
    jf "False! It flows into the void, ending in nothingness."
    jf "I have won this wager. Your claim on the crown is forfeit, as it always has been."
    "The princess looks resigned to her loss. You figure you've had a good run with her, but it looks like it's just about over and you should probably be heading back to your cave. You stand up to excuse yourself."
    tp "Very well then, Jack Fetcher. I shall make you a king, if that is your wish."
    "The princess waves a hand over Jack's fur and it shifts. You see his mouth open in protest a moment before it is absorbed into the shapeless blob of his own skin and fur. Within minutes, the sculpting is complete, and what appears to be a king from a giant chess set stands in front of you."
    "The princess turns to you."
    tp "Well, I believe I've upheld my end of the bargain. I lost the wager, and so I've 'made him a king'. I have fulfilled his wish to the letter, I hope you agree?"
    "You nod, agreeing that she has indeed fulfilled Jack's wish to the letter. You hope to never get on her good side enough to be rewarded in the same way."
    tp "I would, of course, be happy to turn Jack back into his old self, but that would be doing him a favor, meaning that he would owe me. And that favor would, of course, be to retrieve my crown. I hope that Jack will assist me with this, as it would be in the best interests of both of us."
    "And wouldn't you know it, but the next time the princess shapes a mouth on the chess piece, Jack agrees to help. It's crazy how things work out like this."
    "When Jack has fled from your view, once again in his normal shape, the princess leans heavily against her windowsill."
    tp "Well, I suppose that's taken care of. I assume he'll twist my request in the same way I've twisted his, and likely return with my sister's army at his back. We'd best be prepared for when that happens."
    $eProg+=1
    return

label casino:
    scene bg black
    scene bg casino with Dissolve(5.0):
        size (1920, 1080) crop (0, 140, 1280, 720)
        linear 4 crop (160, 140, 1280, 720)
    scene bg casino with fade
    "The casino looks remarkably similar to the ones from your world. It's easy to find, too: you just follow the flashing signs until you're at the building. The light of dawn is brighter here, being that you're so close to the grave of the sun."
    "Like the rest of the people and creatures waiting in line to enter the casino, you take a moment to pay your respects to the Tyrant Sun, the first and truest god of this land. Here he lies beneath the earth, dead for all time, slain by the squabbling lesser deities that call themselves the masters of this world. Or perhaps he is merely sleeping, for to such higher beings, are sleep and death not the same?"
    "After that moment of silence, you enter the casino. Inside, the noise and lights are almost overwhelming. Beings of all types crowd around felt-covered tables or fight for a pull at the slot machines. You resist the urge to join them, reminding yourself that you are basically broke and do NOT want to get into debt here, and instead start asking around for Jack."
    "Eventually, someone points you to one of the card tables, where a black cat the size of a panther is dealing out hands of poker. When the round finishes, one player leaves with a small pile of coins. The cat puts a 'Back in 15' card on the table and stretches."
    jf "Been looking for Lucky Jack? I do hope it's for something dire, or I can't say I'll be interested."
    "He listens to your request while sharpening his claws."
    jf "Fine, I'm enticed. It's not every day one gets a chance to bet against royalty, and you know they say the house always wins."
    jf "I've got to finish my shift, but I'll be sure to accompany you back once I'm done. Can't keep the pretty princess waiting too long, can we?"
    "Jack Fetcher stretches and pads back to the poker table. It looks like you have some time to kill."
    "Perusing the card tables, you decide to spectate on a game of blackjack. At least, it looks like blackjack, although the cards are blue and gold and instead of jacks, the face cards show figures of hunters and other beings. The suits are also unfamiliar, and there are several cards showing numbers that don't exist, and honestly, it's kind of making your head spin. You look down for a moment and, hey, someone dropped a coin on the floor."
    "You pick it up, feeling the warm metal against your hand. One side shows Lady Luck's masked visage, while the back has the symbol of a clover. A single coin can't buy much in any of Lady Luck's casinos, and such a small amount can't even be exchanged for outside currency."
    "You do, however, notice a small memory game that only costs one coin to play. Deciding to join, you see that you have 30 seconds to match all the pairs of cards. It seems easy enough."
    "The timer starts."
    call memory_game()
    "When you walk away from the table, you notice that Jack has finished his shift. You follow him out, leaving both the boisterous fanfare that surrounds lucky winners and the quieter terror of those who have fallen into debt."
    $eProg+=1
    return

label e5:
    "But no army is forthcoming. And neither is Jack."
    "You wait anxiously with the princess. Flit paces across her shoulders, and the wary eyes of several small animals flicker in the trees. You ask the princess what you should do."
    tp "What can we do but wait and hope?"
    "You would prefer to do a bit more than that, so you take a walk to relieve your nerves. You're passing by the umpteenth tree when you see Jack staggering down the path in front of you. He's carrying a golden crown in his mouth, and without pausing his flight, he spits it out at your feet."
    jf "You can tell the royal brat that I'll take no further 'rewards' for this. Pfah!"
    "With that, he bounds off into the depths of the forest. You hear the sound of shrieking and many footsteps approaching, likely due to the princess's sister's army."
    "Well, this looks unfortunate. You have a magic crown at your feet, a royally murderous army approaching, and a princess in distress somewhere far behind you. You'd like to get the crown back to the Tower Princess (especially since magic items tend to be treacherous, especially when not used by their actual owner), but you're not sure if you can make it back to her in time."
    menu:
        "Use the crown yourself":
            call eEnd1
        "Take the crown to the princess":
            call eEnd2
    return

label eEnd1:
    "You place the crown on your head and a surge of power wracks your whole being. When the army comes, you are ready. You plow through scores of peons, flicking them aside like gnats."
    "Unfortunately, being that you're only a regular person, you can only handle a fraction of the crown's power. As the minutes pass, each strike becomes stronger, but you grow more and more overwhelmed. You can hear someone screaming in the vague distance, although you're not sure if it's the princess or you."
    "And before long, stronger foes begin to arrive. The princess's sister waits in the back, not stooping so low as to intervene. She is beautiful like a flock of swans, if the swans in question were melted together into a heap of flesh and feathers."
    "When you are at last subdued, the princess's sister locks you in a jar. The battle quiets, and the princess is not counted among the dead, so you assume she's gotten away. You're not sure about Flit and the other animals, however. They are so small, their bodies would be easy to overlook."
    "The minutes still pass. You wonder if you'll be used as a hostage, if you have that much worth. The sister ignores your tapping on the glass."
    "You realize that the jar has no air holes."
    "The sister continues to ignore you. She runs her fingers through her marred flesh and screeches at some of her soldiers. You're not sure if her lack of attention is a genuine oversight, or if she's just waiting for you to run out of air."
    "Neither the sister or her soldiers take much notice of your muffled shouts and pounding on the glass. After all, you're only a little thing in a trap, and not worth their attention. Eventually, you slump over in the corner of the jar, every breath taking effort."
    "Your last coherent thought is, 'Maybe I won't be worth it to torture...'"
    show bg badForest
    centered "End"
    return

label eEnd2:
    "You race back to the princess, moving even faster than when you'd been running from the troll at the beginning of the game. The army at your heels, you just about collapse in front of the princess and hand her the crown. Wow, you really hope she doesn't turn out to be crazy or evil after all this."
    tp "At long last!"
    "The princess raises the crown up to a pair of birds. They fly it to the top of the tower and place it there. The princess seems to glow."
    "Indeed, her entire tower seems to glow. It no longer looks decrepit and the moss covering the stones has vanished. The tower rises out of the ground, and the princess's flesh melts into the wall."
    "You question whether the princess has turned her tower into a mecha, or if she is in fact a sapient piece of architecture."
    tp "Oh, well, I suppose the latter is the case. If you misled you with the doll I'd made, it was never my intention."
    "The tower sighs lightly, sounding exactly like the princess."
    tp "I do hope it isn't kitschy, a girl my age still having dolls."
    "You assure her that no, it's most certainly fine and not kitschy in the slightest. And now, if she'll excuse you, you'd like to be sick in the corner while she takes on the approaching army. She heartily agrees with this."
    "Congratulations, it looks like you've helped the princess. She obliterates her sister's army and her terrible sister flees. The princess holds good on her promise, and what is left of the world becomes a better place."
    "What the other masters think of this corner is a different story."
    show bg goodForest
    centered "End"
    return

label prelude:
    "It appears that your day has been off to a rough start. After leaving the relative safety of your sleeping nook this morning, you went out wandering the caverns in search of food. Unfortunately, a very large cave troll was also searching for food, which it appears to have found, as it has found you. You started running and just paused for breath a few seconds ago, and it looks like we're pretty much caught up to the present."
    "And that was excellent timing, as the cave troll has just picked up your scent again. It roars and charges, and once again you find yourself on the run. Scurrying up the tunnel, your frantic flight takes you to the entrance of the caverns. The weak light hurts your eyes, but you don't stop until you're fully outside. Only then do you allow yourself to look back."
    "The troll stops short of the entrance. Pacing angrily, it skirts the edge of the darkness, deprived of its breakfast. It looks like you won't be heading back to your sleeping nook anytime soon."
    "Well, if you're stuck out here for the day, you'd like to make the most of it and procure some breakfast. You take stock of your surroundings, squinting in the eternal dawn's light."
    "To the right, a forest stretches on as far as you can see. To the left are the ruins of an old city. There are likely monsters in both directions, so take your pick."
    python:
        inventory.append("A small dagger, more useful for skinning rats than fending off monsters.")
        inventory.append("The tattered livery of your old master. It doesn't mean much now that he's dead.")
        inventory.append("Fifteen dollars worth of American bills and coins. Such currency is useless in this land.")
    return