define sgb = Character(_("Strange Godlike Being"), color="#aa7777", what_color="#aa7777")
define time = 0
define adv = 0
define favor = 0
define attack = 1
define faith = 0
define faithText = 0
define totalTime = 25

label start:
    call intro from _call_intro
    menu:
        "But how, may I ask, do I manage these humans?":
            sgb "I'm glad you asked, small friend."
            "Your fellow abomination sidles up next to you and takes a bite out of the moon. This abomination sounds very sinister and knowledgeable. It probably knows what it's doing. It was probably sent to give you a detailed TUTORIAL, from the great cosmic force of EXPOSITION."
            sgb "Well, I'd be happy to lend an appendage. They're so easy to manage, they practically take care of themselves. Which is a good thing, since you technically can't take care of them."
            sgb "By that, I mean that if you're going to be a strange godlike being like me, you're not allowed to interfere with them. You just get to watch them and wait for them to mature as a colony. From my experience, that takes about [totalTime] centuries."
            sgb "Here, take these 5000 humans and a nice little plot of land. Have fun!"
            "It spirals into the void. You have a good feeling about this."
        "Just generate me some humans, I know what I'm doing!":
            pass

    show screen bars(time, totalTime)
    "All right, you have your humans and your time bar (in the top left corner) and [totalTime] centuries to make this work. Let's get this story going!"
    while time < totalTime:
        "Century [time]."
        define event = 0
        python:
            time += 1
            event = renpy.random.randint(0, 4)
        if event == 0:
            call culture from _call_culture
        elif event == 1:
            call attack from _call_attack
        elif event == 2:
            call callFavor from _call_callFavor
        elif event == 3:
            call religion from _call_religion
        else:
            "Hey, nothing horrible has happened lately! Granted, nothing great has happened either, but you could use a quiet moment from time to time. You do have a life outside of waiting for populations to get large enough for you to devour, after all. Another century flits by without much fuss."
        show screen bars(time, totalTime)
    call end from _call_end
    return
label intro:
    "Hello, you! As you probably know, you are a gigantic, godlike abomination, and you've just discovered the planet Earth."
    "You also discovered you really like eating people."
    "You also discovered that you ate too many people, and now they are going extinct."
    "..."
    "You think you ought to manage things better, so you can keep eating them."
    return
label end:
    "Now your colony is mature."
    "The delicious civilization spreads before you. Some of these people you've watched their entire lives. Others, you've known generations of. Some of them may even have faith in you. Is this really...worth it?"
    "Gosh darn it, you're an abomination! You have no feelings! You came here to eat some humans and you spent a good long time waiting for this!"
    menu:
        "Right.":
            "You eat the humans and they are very delicious. You feel very good about this. Congratulations."
        "Right?":
            "You tearfully refuse to eat the humans. They continue to go about their meaningless, short lives, mostly unaware of your feelings. You could care less. You, at least, are a nice monstrosity, and that is what matters."
    "{b}End.{/b}"
    return
label religion:
    "Despite your best efforts toward the contrary, some people have taken notice of the planet-sized abomination watching them day after day from the clouds."
    if faith == 0:
        "Looks like a new cult has dedicated itself to you."
    elif faithText == 1:
        "Since you already have a small following, you decide to preach to them the doctrine of {color=#aa0000}THOU SHALL NOT KILL THY FELLOW HUMANS, BECAUSE THAT MEANS THAT THERE WILL BE FEWER HUMANS FOR ME TO, UM, LOVE. THAT'S IT, LOVE.{/color}"
    elif faithText == 2:
        "Your cult eagerly awaits your next teaching. {color=#aa0000}YOU SHOULD ALL BE FRUITFUL AND HAVE LOTS AND LOTS OF KIDS. AND IF YOU DON'T WANT THAT MANY KIDS, OR YOU'RE NOT ATTRACTED TO THE OPPOSITE SEX, OR YOU HAVE SOME FERTILITY ISSUE, THEN YOU CAN GO OUT AND CONVINCE OTHER PEOPLE TO HAVE LOTS AND LOTS OF KIDS INSTEAD!{/color}"
    elif faithText == 3:
        "At this point, your cult is now a full religion. {color=#aa0000}YOU KNOW WHAT? YOU SHOULD ALL LEARN HOW TO COOK. COME UP WITH A NEW RECIPE OR TWO. CALL THE CHIEF PRIEST THE CHEF PRIEST. JUST THINK UP SOME COOL NEW WAYS TO SERVE MAN--I MEAN YOUR FELLOW MAN, AND ALSO WOMAN, AT THE TABLE, RATHER THAN ON IT, EVEN IF YOU LOOK SO DELICIOUS...I OUGHT TO STOP TALKING RIGHT NOW.{/color}"
        "Verbatim, this enters your holy book."
    else:
        "Running out of things to tell the people, you just declare a random religious holiday dedicated to pacifism, having more kids, and creating new cooking recipes. No, no, they won't lose your blessing if they don't do all three at once. But you certainly won't laugh in the face of efficiency."
    $faith+=1
    $faithText+=1
    return
label callFavor:
    "As watching a bunch of people go about their meaningless lives while their civilization slowly matures toward your standard of consumption is boring, you decide to call upon your best buddy, {b}Moj*r1!?th{/b}, to watch them while you take the day off. {b}It{/b} promises to keep them from destroying themselves in your absence."
    if favor > 0:
        menu:
            "As {b}Moj*r1!?th{/b} owes you a favor for almost getting your colonists eaten, {b}it{/b} also decides to help your colonists while you're away. How can {b}it{/b} be of assistance?"
            "With fighting power":
                "{b}Moj*r1!?th{/b} manifests one continent-sized tentacle in the sky above your largest city. The people, deciding that anything this ugly must be automatically evil, take up arms to destroy the beast. {b}Moj*r1!?th{/b} doesn't actually hurt anyone, of course, but it looks like they've learned a thing or two about fighting by the time they're done."
                $attack+=1
                "Their attack power is now [attack]."
            "With religion":
                "{b}Moj*r1!?th{/b} puts on {b}its{/b} least horrifying flesh suit and presents {b}itself{/b} to the unsuspecting people. They scream. They cry. They praise the heavens. Thousands are converted. The skeptics are stoned."
                $faith+=1
                "Their faith in you is now [faith]."
        $favor-=1
    "You, meanwhile, go deep space fishing and have an awesome time!"
    return
label attack:
    $name = ""
    define cons=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    define vows=["a","e","i","o","u"]
    python:
        nameLength = renpy.random.randint(2, 5)
        startVowel = renpy.random.randint(0, 5)
        if startVowel == 0:
            name += vows[renpy.random.randint(0, len(vows)-1)]
        for i in range(nameLength):
            name += cons[renpy.random.randint(0, len(cons)-1)]
            name += vows[renpy.random.randint(0, len(vows)-1)]
    "Hey, it's your best buddy {b}Moj*r1!?th{/b}, come to visit you and your colony! And {b}it's{/b} brought along {b}its{/b} new pet, a wild new species called [name]!"
    "What does a [name] look like, you ask? Well, you wish you could say, but it looks like it's escaped from its cage."
    "Oh, there it is, attacking your colonists."
    $m_attack = renpy.random.randint(0, 15)
    "A wild [name] attacks! Its strength is [m_attack]! Your colonists' strength is [attack], with a bonus of [adv] for population size and societal advancements, plus [faith] for their faith in a higher power that may or may not be able to bail them out in time!"
    if(attack+adv+faith) > m_attack:
        "Your colonists soundly defeat the monster! They revel in their victory, and many new songs about the great battle are composed. Some of them discuss actual tactics used in the fight, which will be remembered."
        $attack+=1
        "Your attack increases to [attack]!"
    else:
        "Your colonists are no match for the terrible [name]! It gobbles up a dozen of them before you can lure it away with a tasty asteroid pie."
        "This will take years of screwing with the government to convince your people that this was all the Russians' fault. Darn you {b}Moj*r1!?th{/b}! You owe me one!"
        $favor+=1
    return
label culture:
    "Your culture is advancing!"
    if adv == 0:
        "Your humans have learned to control fire. By cooking their meat, they decrease the chance of contracting diseases, and their population grows. Plus you learn a dozen new recipes from which to serve man."
    elif adv == 1:
        "Your humans have begun farming, allowing them to settle down long term. While the denser population escalates a host of problems including the transmission of disease and social inequality, that doesn't concern you because their population is increasing."
    elif adv == 2:
        "Your humans have invented the wheel. This benefits them by greatly saving on labor, allowing them to have more leisure time. This in turn benefits you, as they spend that leisure time further increasing their population."
    elif adv == 3:
        "Your humans have started forging iron tools. As these are far better than their bronze counterparts, the people cheerfully begin inventing new and exciting ways to kill each other. They form armies and empires, resulting in a net increase to their population."
    elif adv == 4:
        "Industry revolves as the industrial revolution kicks off! Necessities are mass produced, the marriage age drops, and people learn that they can pack 15 of themselves into a small, filthy flophouse room. Birth rates soar!"
    else:
        "A golden age of culture begins, and art and science flourish! This morning, you had to knock a few of their spaceships out of the sky. You can't let them get too advanced, right?"
    $adv += 1
    return