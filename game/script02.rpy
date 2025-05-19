label Day02:
# reboot variables
$ day = 2
$ hour = 7
$ stamina = 5
$ beachtipgiven = False
$ workout = False
$ MCattitude = False
$ jointtaken = False
$ auntdebbyseen = False
$ helpedsiswin = False
$ busbeach = False
$ bustown = False
$ katsumifucked = False
$ nikkifucked = False

stop music
play sound "Sounds/yawning.mp3"
scene ryanyawning with dissolve
$ renpy.pause(1.0, hard=True)
p "Another beautiful day, it's so sunny on this island!"
p "I should probably check my computer to see if Google uploaded any other app without my authorization..."
scene ryanbedroomday with dissolve
$ lustaddedB = 2
call Challenger from _call_Challenger_4
$ lustaddedB = 3
call Challenger from _call_Challenger_5
$ challengercalls += 2
label Day02b:
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "What should I do?"
menu:
    "Take a shower":
        jump ShowerMorning02
    "Go for breakfast":
        jump NancyYogaMorning
    "Check the computer":
        jump Computer03
    "Go for a jog":
        $ wentforjog = True
        jump NancyYogaMorning
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump Day02b
        
label Computer03:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
p "Ah yes, Google DID upload another app called \"Inventory\"... Now they even check what I carry on me..."
label Computer03b:
scene ryancomputerday
menu:
    "Check the inventory":
        jump InventoryCheck
    "Check the map":
        jump Map02
    "Check the stats":
        jump Stats02
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump Computer03b
    "Turn the computer off":
        jump Day02b

label InventoryCheck:
play sound "Sounds/mouseclick.mp3"
hide screen statsbackground
show screen inventorybutton
play sound "Sounds/pigeon.mp3"
$ renpy.pause(1.0, hard=True)
p "To activate it, I should click on the backpack icon on the left..."
p "From now I will be able to check it at any time by searching through my backpack, the good old-fashioned way."
show screen statsbackground
jump Computer03b

label Map02:
play sound "Sounds/mouseclick.mp3"
hide screen inventorybutton
hide screen statsbackground
hide screen calendar
show islandmap with dissolve
$ renpy.pause(1.0, hard=True)
if (discoverrandybeach == True):
    show randybeachmap
if (discoveraunthouse == True):
    show aunthousemap
p "This shows all the places I know so far on Veri-Bosti Island..."
show screen statsbackground
show screen inventorybutton
show screen calendar
jump Computer03b

label Stats02:
play sound "Sounds/mouseclick.mp3"
scene stats
hide screen statsbackground
hide screen inventorybutton
hide screen calendar
show screen statsscreen
$ renpy.pause()
hide screen statsscreen
show screen statsbackground
show screen inventorybutton
show screen calendar
jump Computer03b

label ShowerMorning02:
play music "Sounds/shower.mp3"
scene bathroomdoorclosed with dissolve
$ renpy.pause(1.0, hard=True)
$ locbathroom = True
p "Someone's taking a shower..."
menu:
    "Have a peek":
        jump PeekBathroomDay02
    "Leave":
        jump Day02b

label PeekBathroomDay02:
$ nightbathroomseen = True
$ locroom = False
play sound "Sounds/doorsqueak.mp3"
scene bathroomdooropen with dissolve
$ renpy.pause(1.0, hard=True)
p "Shit, the door is squeaking..."
s "Hey, I'm in the shower, don't get in!"
p "Ah, sorry Nikki...I'm leaving..."
p "Damn, I should try and find a way of stopping that door from squeaking if I want to spy on Nancy or Nikki in the shower like every other MC..."
p "I'll wait for Nikki to finish so I can take a shower before breakfast then..."
"A while later"
stop music
p "Are you done Nikki? Can I come in?"
s "Yeah, I'm done, you can get in..."
scene nikkishowermorning01 with dissolve
$ renpy.pause(1.0, hard=True)
s "Hum...I just have to still brush my hair a bit...Don't mind me [name]!"
menu:
    "Wait for her to finish before entering the shower":
        s "OK, done! Enjoy your shower, I'm off to get dressed for our first day of school!"
        scene shower with dissolve
        play music "Sounds/shower.mp3"
        $ renpy.pause(1.0, hard=True)
        p "That's nice and relaxing..."
        stop music
        p "I should get dressed and go for breakfast now."
        jump NancyYogaMorning
    "Get totally undressed and enter the shower":
        scene nikkishowermorning02 with dissolve
        $ renpy.pause(1.0, hard=True)
        s "WOW!...Ooh...Sorry, I'll leave now..."
        window hide
        $ lust_points[17] += 1
        $ score += 1
        show lust01:
                xalign 0.45 yalign 0.4
                linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        scene shower with dissolve
        $ renpy.pause(1.0, hard=True)
        play music "Sounds/shower.mp3"
        $ renpy.pause(1.0, hard=True)
        p "Yeah, it worked... She couldn't take her eyes off my massive dong...I'm DA MAN!"
        stop music
        p "I should get dressed and go for breakfast now."
        jump NancyYogaMorning        

label Breakfast02:
scene breakfast02 with dissolve
$ renpy.pause(1.0, hard=True)
m "So are you two excited about your first day at your new school?"
s "Yes, I can't wait to meet all my classmates...and see José again..."
show breakfast02b
m "You quite fancy him don't you?"
show breakfast02c
s "Maybe (blush)..."
hide breakfast02b
hide breakfast02c
m "What about you [name]?"
menu:
    "Well, I miss my old friends but I'm sure I'll make some new ones.":
        m "Of course you will, just be nice to everyone, okay? I don't want any trouble."
        jump Breakfast02b
    "I hope there's a ton of hot girls.":
        m "Humpf...Don't do anything foolish, I don't want any trouble from you."
        window hide
        $ lust_points[16] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.6 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump Breakfast02b

label Breakfast02b:
m "Here's some pocket money for the day, five dollars each."
$ money += 5
show breakfast02d
s "Yeah, thanks mom!"
p "It's not much... Where could I make some extra money on this island?"
hide breakfast02d
m "I'm sure you could find some odd jobs if you look around. Or you could ask people to wash their cars? Debby might be interested."
if (storework == True):
    p "Actually, I've already found a job at the local convenience store. It doesn't pay that much but the girl I'll be working with is really... nice."
    show breakfast02d
    s "I bet she has huge tits! That's why you took the job, normally, you're just so lazy!..."
    p "That's not true, I'm actually going to be helping her. She has some... back problems."
if (storework == False):
    p "Hum... Okay, I'll look around, hopefully I can find a job that pays well and isn't too much work..."
    show breakfast02d
    s "Maybe next week, YOU'LL be the one giving Nancy some pocket money!"
    show breakfast02e
    m "Oh, Nikki, you're so funny sometimes!"
    p "I don't see what's so funny. I won't give away my hard-earned cash like that..."
    hide breakfast02e
    
hide breakfast02d
m "Enough chit-chatting, you need to eat up so you can get to school on time."
s "Sure mom, we'll be on our way straight after breakfast. The school is not too far, we can walk there, I know the way, José told me yesterday..."
jump School02

label NancyYogaMorning:
scene nancyyoga01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Nancy is doing her morning exercises... She hasn't seen me yet..."
menu:
    "Continue watching":
        scene nancyyoga02 with dissolve
        $ renpy.pause(3.0, hard=True)
        scene nancyyoga03 with dissolve
        $ renpy.pause(3.0, hard=True)
        scene nancyyoga04 with dissolve
        $ renpy.pause(1.0, hard=True)
        m "Oh, good morning sweetie, did you sleep well in your new bed?"
        p "Yeah, I'm all set and ready for a new day!"
        if (wentforjog == True):
            jump WentForJog
        elif (wentforjog == False):
            jump NancyYogaBreakfast
    "Call her so she knows you're here":
        p "Hey Nancy, good morning!"
        scene nancyyoga04 with dissolve
        $ renpy.pause(1.0, hard=True)       
        m "Oh,good morning sweetie, did you sleep well in your new bed?"
        p "Yeah, I'm all set and ready for a new day!"
        if (wentforjog == True):
            jump WentForJog
        elif (wentforjog == False):
            jump NancyYogaBreakfast

label WentForJog:
m "Were you going out for a jog? If you do, you might miss breakfast."
p "Yeah, but it's just that I'm so eager to see everything on this island Nancy!..."
m "Fine, your choice [name]. Don't forget to be back soon. You could stretch out here with me before going..."
menu:
    "OK, sure Nancy.":
        scene nancyyogaryan01 with dissolve
        $ renpy.pause(3.0, hard=True)       
        scene nancyyogaryan02 with dissolve
        play sound "Sounds/workoutgroan.mp3"
        $ renpy.pause(1.0, hard=True)
        m "Oh, wow, [name], you're so... hum... muscular!"
        window hide
        $ lust_points[16] +=1
        $ score += 1
        show lust01:
            xalign 0.9 yalign 0.8
            linear 1.0 yalign 0.6
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        $ longjog = True
        menu:
            "Go for a jog on the local beach":
                jump JogBeach
            "Go for a jog around the neighborhood":
                jump JogBurbs        
    "I'd better shoot off right now if I want to be back in time for breakfast...":
        $ shortjog = True
        m "Ok, See you in a bit then sweetie!"
        menu:
            "Go for a jog on the local beach":
                jump JogBeach
            "Go for a jog around the neighborhood":
                jump JogBurbs
                
label NancyYogaBreakfast:
p "Are we having breakfast soon?"
m "Give me a few minutes to finish my exercises and for Nikki to take her shower."
m "Why don't you sit and watch a bit of TV while you're waiting?"
p "Sure Nancy!"
scene ryantv with dissolve
play music "Sounds/laughter.mp3"
$ renpy.pause(1.0, hard=True)
p "God these morning sitcoms are so boring, nothing ever happens..."
m "Breakfast is ready!"
$ hour += 1
stop music
jump Breakfast02

label JogBeach:
scene ryanjog01 with dissolve
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
"You enjoy the fresh sea breeze as you jog along the beach..."
$ d3rollj=renpy.random.randint(0, 2)
if (shortjog == True):
    if (d3rollj==2):
        "After running a couple of miles, you head back home for breakfast."
        jump Breakfast02j        
    else:
        jump JogBeach02
if (longjog == True):
    if (d3rollj==2):
        jump JogBeach02
    else:
        "After running a couple of miles, you head back home for breakfast."
        jump Breakfast02j

label Breakfast02j:
stop music
$ hour += 1
scene morninglate with dissolve
$ renpy.pause(1.0, hard=True)
if (shortjog == True):
    m "Get a quick shower, we're about to start breakfast!"
    p "Oh, sure Nancy, sorry..."
    "You take a quick shower and head downstairs for breakfast."
    jump Breakfast02
elif (longjog == True): 
    m "You took too long, so we had breakfast without you. Get a quick shower and get dressed, I'll make a jam sandwich for you to eat on the way to school!"
    p "Oh, sure Nancy, sorry I took so long..."
    "You take a quick shower and hurriedly get dressed to join Nikki on the way to school."
    jump School02
    
label JogBeach02:
scene ryanjog02 with dissolve
$ renpy.pause(1.0, hard=True)
"There's a woman standing with her arms on her knees. She looks exhausted."
p "Hey, do you need help?"
ta "What? No, I'm just a bit out of breath from running so many miles. I'll be good in a moment."
scene ryanjog03 with dissolve
$ renpy.pause(1.0, hard=True)
ta "See? It takes more than a 10 mile morning jog to tire these muscles!"
p "(Wow, she's pretty damn fit...)"
p "Ok, I'll be on my way then..."
ta "Hang on, where do you think you're going boy? I think I will have some use for you..."
scene ryanjog04 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Yeah, definitely... That huge log snaking down your pants is real... My husband will like it..."
window hide
$ lust_points[21] +=2
$ score += 2
show lust02:
    xalign 0.2 yalign 0.5
    linear 1.0 yalign 0.3
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02 
p "What the fuck? What are you talking about?"
scene ryanjog05 with dissolve
$ renpy.pause(1.0, hard=True)
ta "I'm talking about you coming over to my place in the evening for some fun with those great big balls of yours... What are you afraid of? A stud like you should never be afraid..."
window hide
$ lust_points[21] +=1
$ score += 1
show lust01:
    xalign 0.8 yalign 0.5
    linear 1.0 yalign 0.3
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01 
p "Err... yeah, I'm da man, and so forth, but still, I don't even know you..."
ta "Well, you'll get to know me very well... I'm the famous \"webcamtanya\"... You want to become famous? Then come to my place on Tuesday or Wednesday evening..."
window hide
$ discovertanya = True
show addedlocation:
    xalign 0.4 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide addedlocation
ta "I'm on my way, still have ten miles to run back home... You'd better show up..."
p "Wow, what a crazy lady... Shit, I'm gonna be late, I should head back home for breakfast if I can..."
jump Breakfast02j

label JogBurbs:
scene burbsmorning with dissolve
play music "Sounds/morning.mp3"
$ renpy.pause(1.0, hard=True)
p "The burbs are so quiet in the morning."
scene burbsmorningstore with dissolve
$ renpy.pause(1.0, hard=True)
p "Oh, I discovered our local convenience store. Well, it was well hidden, not so \"convenient\" after all..."
$ discoverstore = True
show addedlocation:
    xalign 0.3 yalign 0.3
    linear 1.0 yalign 0.1
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide addedlocation
menu:
    "Enter the store":
        $ longjog = True
        jump Store01
    "Go back home in time for breakfast":
        $ shortjog = True
        jump Breakfast02j

label School02:
$ discoverschool = True
scene schoolentrance with dissolve
$ renpy.pause(1.0, hard=True)
$ hour += 1
s "Well, I have to head in a different direction from you [name]. My class is in Building C."
p "OK, maybe we'll see each other at lunchtime Nikki?"
s "We'll see... Enjoy your first day [name], bye!"

label ClassRoom:
scene classroomarrival with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, this school is huge... corridor F4, yes, that's it."
p "I guess this is my classroom... I hope my classmates are n..."
scene quentingreet
q "Hey there, you're the new guy [name], right?"
p "Hum, ye..."
q "I'm Quentin, I'm the class president. Do you like video games?"
p "Err...y..."
q "I've got tons of video games at home, you should come round so we can play together, it would be awesome!"
q "Come on in, I'll introduce you to everyone!" 
play music "Sounds/classambience.mp3"
scene classmeet01 with dissolve
$ renpy.pause(1.0, hard=True)
q "It's a pretty small class, we're all very close to each other, I'm the most popular of course since I'm the president."
scene classmeet02 with dissolve
$ renpy.pause(1.0, hard=True)
q "Here's Kate...(whispering) Between you and me, she's not the brightest of students..."
q "Say hi to my new friend Kate!"
k "What?...Ooh... Who's this?...Um...Hi..."
window hide
$ lust_points[11] +=1
$ score += 1
show lust01:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
p "I'm a n..."
q "He's a new student, he's called... [name] right? Anyway, Kate is my girlfriend, we're real close, always hanging out together and...like... kissing and stuff."
scene classmeet03 with dissolve
k "Ooh...What? Oh no... I'd rather die than kiss you like...ever...!"
q "Hah hah, she's funny, always joking like that. No but seriously, she's mine, OK?"
scene classmeet04 with dissolve
$ renpy.pause(1.0, hard=True)
q "Here's Frieda, she's from Sweden or something."
fr "Nein, from Germany! Hello mein friend."
window hide
$ lust_points[8] +=1
$ score += 1
show lust01:
    xalign 0.1 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01 
$ lust_points[14] +=1
$ score += 1
show lust01:
    xalign 0.85 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01 
q "And Maddy, she looks tiny but you should see how fit she is in a bikini man!"
md "God, you're such a freak Quentin, get off my face NERD!"

scene classmeet05 with dissolve
$ renpy.pause(1.0, hard=True)
q "Laura, she's like always moody, I don't know why..."
la "Cos you're around, that's why."
q "And she always wears black because she's a punk."
la "A goth, you dimwit!"
la "So you're the new guy hey? You seem kinda cool. Do you think about death a lot?"
menu:
    "Life is beautiful, like a flower.":
        la "Flowers die. Everything dies."
        p "Alright-eee then... Nice talking to you Laura..."
        jump ClassMeet06
    "I think you need to see a shrink...":
        jump LauraChat01
    "Mmh... Yeah, I think a lot about José dying in terrible pain, does this count?":
        jump LauraChat02

label LauraChat01:
la "That's what my parents keep saying. I hate my parents. What about you?"
menu:
    "My mother is great. She is the best mom I could ever wish for.":
        la "God, you're already boring me...to death... Go away."
        jump ClassMeet06
    "I don't know, I haven't met them yet.":
        show laurasmile with dissolve
        la "Hi hi..."
        window hide
        $ lust_points[13] +=2
        $ score += 2
        show lust02:
            xalign 0.5 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
        q "My god, you made her smile. I never saw her smile before I swear..."
        $ madelaurasmile = True
        jump ClassMeet06

label LauraChat02:
la "José? That knucklehead? Yeah, I can see why. He's a bore."
window hide
$ lust_points[13] +=1
$ score += 1
show lust01:
        xalign 0.5 yalign 0.8
        linear 1.0 yalign 0.6
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
jump ClassMeet06

label ClassMeet06:
scene classmeet06 with dissolve
$ renpy.pause(1.0, hard=True)   
q "And just ignore those two students at the back. He's a nobody and she's a local who only speaks French, between you and me, I think she's in the wrong school..."
play sound "Sounds/footsteps.mp3"
q "Shit, the teacher's arriving, I'm gonna sit at my place right away..."
stop music
$ renpy.pause(1.0, hard=True)
scene teacherenter with dissolve
stop sound
t "You must be [name] Johnson, correct?"
p "Yeah, that's me."
t "YES, that's me, Miss Cocque."
t "Go and stand in front of my desk, facing the class."
p "Yes, Miss Cocque..."

scene classintro with dissolve
$ renpy.pause(1.0, hard=True)
t "Listen up, we have a new student. [name], why don't you introduce yourself to the class?"
menu:
    "Errr... My name is [name]. Hi everyone.":
        t "Well, that was succinct to say the least. Go and sit between Laura and Maddy, there's an empty desk there."
        jump Lesson01
    "I'm from New Major City. It was dark, it was bleak, but I survived and now I'm so happy to be here!":
        t "Oh, poor boy, we'll try and make your stay as good as possible on our lovely island."
        window hide
        $ lust_points[22] +=1
        $ score += 1
        show lust01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        t "Go and sit between Laura and Maddy, there's an empty desk there."
        jump Lesson01
    "I came here yesterday with my landlady and her daughter and I really look forward to getting to know each of you better. Especially the girls...":
        window hide
        $ lust_points[11] +=1
        $ score += 1
        show lust01:
            xalign 0.1 yalign 0.8
            linear 1.0 yalign 0.6
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        $ lust_points[8] +=1
        $ score += 1
        show lust01:
            xalign 0.85 yalign 0.8
            linear 1.0 yalign 0.6
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01        
        t "Well, don't we have a charmer here... You'll do that in your spare time and NOT in my class [name], is that clear?"
        t "Go and sit between Laura and Maddy, there's an empty desk there."
        jump Lesson01

label Lesson01:
scene lesson01 with dissolve
$ renpy.pause(1.0, hard=True)
t "We will start the day with a French lesson. But first, you must understand why you need to learn French."
t "The Island of Veri-Bosti was first discovered by the Portuguese explorer Rambo de la Pimpa in 1669."
t "The French colonized the island for two centuries, that's why so many places have French names, like the capital Sainte-Nitouche."
t "Eventually, the English conquered the island which gained its independence in 1969."
t "Many locals still speak Créole, so it's important to learn French."
t "So listen up and repeat after me. \"Bonjour, je m'appelle Teagan.\""
"Everybody repeats after her: \"Bonjour, je m'appelle Teagan.\""
t "Are you kids retarded? Your names are NOT \"Teagan\"! Use your own names when you introduce yourself to a local."
t "Yadda Yadda. Blah blah blah."
p "God, this is ssoo boring."

menu:
    "Continue listening to the teacher":
        jump Lesson02  
    "Daydream about the teacher... In your dreams, she is naked...":
        jump DayDream
    
label Lesson02:
scene lesson01 with dissolve
$ renpy.pause(1.0, hard=True)    
t "The first president-governor of Veri-Bosti was Sir Ben Dover."
t "He served two terms until he was replaced by Harry Balzac who made French one of the two official languages of the island."
t "I see some people here are actually listening, like your new classmate, [name]..."
t "I can't say the same of some of you sorry lot... KATE! Were you listening or day-dreaming as per usual?"
k "Ooh, sorry Miss Cocque, I was thinking like...about what to wear at the Miss Hardcox Bikini pageant this Friday, it's like ssoo important, ya know?"
t "No, I don't actually, and since you were not listening, YOU are the one who will be tested."
p "Pfew, good thing I was listening..."
t "And if you don't answer correctly, maybe you'll be thinking about what you'll wear in DETENTION this afternoon!"
k "But...Oooh ooh...You can't do that to me!"
t "Shut up and listen, here's your question: What is the capital city of Veri-Bosti?"
k "Hum...ooh... Capital..Town?"
t "WRONG answer! I'll see you at detention later today then..."
t "Now who's been listening and is capable of answering a question?..."
menu:
    "Raise your hand":
        jump TeachQuestion02
    "Don't raise your hands":
        q "Me, me, Miss Cocque!"
        t "(sigh) Always the same student... Alright, what's the capital of Sainte-Nitouche?..."
        q "Sainte-Nitouche.... It's French."
        t "That is correct. Now let's move on."
        jump EndClass02

label TeachQuestion02:
$ d4rollt = renpy.random.randint(1, 4)
$ time = 4
$ timer_range = 4
$ timer_jump = 'menu1_slow'

if (d4rollt == 1):
    show screen countdown
    t "Who was the first president-governor of Veri-Bosti?"
    menu:
        "Harry Balzac":
            hide screen countdown
            jump WrongAnswer
        "Ben Dover":
            hide screen countdown
            jump RightAnswer
        "Chris P. Nutts":
            hide screen countdown
            jump WrongAnswer
        "Neil Anblomee":
            hide screen countdown
            jump WrongAnswer
    
if (d4rollt == 2):
    show screen countdown
    t "What is the capital city of Veri-Bosti?"
    menu:
        "Sainte-Nitouche":
            hide screen countdown
            jump RightAnswer
        "Sainte-Croix":
            hide screen countdown
            jump WrongAnswer
        "Santa Maria":
            hide screen countdown
            jump WrongAnswer
        "Santa Polla":
            hide screen countdown
            jump WrongAnswer
if (d4rollt == 3):
    show screen countdown
    t "Who first colonized the island?"
    menu:
        "The English":
            hide screen countdown
            jump WrongAnswer
        "The French":
            hide screen countdown
            jump RightAnswer
        "The Portuguese":
            hide screen countdown
            jump WrongAnswer
        "The Spaniards":
            hide screen countdown
            jump WrongAnswer
if (d4rollt == 4):
    show screen countdown
    t "Who discovered Veri-Bosti?"
    menu:
        "Juan Alaya":
            hide screen countdown
            jump WrongAnswer
        "Don Quidix de Cadix":
            hide screen countdown
            jump RightAnswer
        "Rambo de la Pimpa":
            hide screen countdown
            jump RightAnswer
        "Hughes Dildeaux":
            hide screen countdown
            jump WrongAnswer

label menu1_slow:
t "Too slow, you clearly don't know the answer!"
jump WrongAnswerB

label WrongAnswer:
t "WRONG!"
label WrongAnswerB:
if (daydreaming == True):
    t "I'll see YOU in detention this afternoon young man!"
    $ detention = True
    jump EndClass02
else:
    t "Next time raise your hands when you ACTUALLY know the answer..."
    q "I know the answer Miss Cocque!"
    t "(sigh) I'm sure you do, I'm sure you do..."
    jump EndClass02
label RightAnswer:
t "Correct!"
if (daydreaming == True):
    t "But you could have been lucky... I'm still keeping an eye on you..."
    jump EndClass02a
else:
    t "Well...I'm impressed young man... You're not the dumb jock I first thought you were..."
    window hide
    $ lust_points[22] +=1
    $ score += 1
    show lust01:
        xalign 0.3 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01    
    show lesson01d
    $ katepissedoff = True
    k "Umpf.....Loser!"
    window hide
    $ lust_points[11] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.1 yalign 0.4
        linear 1.0 yalign 0.6
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01    
    jump EndClass02
        
label DayDream:
play sound "Sounds/dreaming.mp3"
scene classroomdreaming01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
p "Mmmh, yeah..."
scene classroomdreaming02 with dissolve
$ renpy.pause(3.0, hard=True)
t "Ooh, [name], you're such a stud, I can't help myself but strip naked for you..."
p "Yeah, I'm da man, I'm DA MAN! Come here baby..."
scene classroomdreaming03 with dissolve
$ renpy.pause(3.0, hard=True)
t "Please fuck me [name]...I NEED that GIANT cock of yours right NOW!"
p "Yeah, get on your kn..."
stop music
play sound "Sounds/scratch.wav"
scene classroomyell
$ renpy.pause(1, hard=True)
t "[name]! I do not tolerate day-dreamers in my class!"
p "What? Oh, no, I was listening Miss Cocque, I swear!"
t "Is that so? Then you'll have no problem answering the following question..."
$ daydreaming = True
jump TeachQuestion02

label EndClass02a:
scene lesson01 with dissolve
$ renpy.pause(1.0, hard=True)
t "KATE! Were you listening or also day-dreaming as per usual?"
k "Ooh, sorry Miss Cocque, I was thinking like...about what to wear at the Miss Hardcox Bikini pageant this Friday, it's like ssoo important, ya know?"
t "No, I don't actually, and since you were not listening, YOU are the one who will be tested."
t "And if you don't answer correctly, maybe you'll be thinking about what you'll wear in DETENTION this afternoon!"
k "But...Oooh ooh...You can't do that to me!"
t "Shut up and listen, here's your question: What is the capital city of Veri-Bosti?"
k "Hum...ooh... Capital..Town?"
t "WRONG answer! I'll see you at detention later today then..."
show lesson01d
$ katepissedoff = True
k "Umpf..."

label EndClass02:
$ hour += 1
scene lesson01 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
t "OK, class dismissed, see you all back in fifteen minutes... [name], come over here..."
scene teacherenter with dissolve
$ renpy.pause(1.0, hard=True)
t "After the break, you are summoned to the principal's office. It's down the corridor on the right."
p "But, what have I done?"
t "Don't worry, Principal Titsworthy meets with every new student for a small chat, it's normal. Now off you go [name]!"

label Locker01:
stop music
play music "Sounds/lockersound.mp3"
scene locker with dissolve
$ renpy.pause(1.0, hard=True)
p "That nerd is standing right in front my locker..."
menu:
    "Talk to him":
        jump NerdTalk
    "Ignore him":
        jump NerdIgnore

label NerdTalk: 
p "Hi ner...I mean Quentin. What's up?"
q "Everyone's talking about the challenge between José and you..."
q "I don't like him, he makes fun of me in front of the girls."
menu:
    "Gee, I wonder why.":
        q "Mmh, maybe you're not such a nice boy after all..."
        $ quentinnotfriend = True
        "Quentin stops talking. You put some books back into your locker and head for the principal's office."
        stop music
        jump NikkiChantelleMeet01
    "What an arsehole.":
        q "I know, right? Listen, I'll gather info on the girls to help you."
        p "Thanks, that'll be very helpful I'm sure."
        q "Brittany is the prom queen and she desperately wants to win again this year."
        q "She loves glitzy stuff, as long as it looks like gold."
        q "Meet me after recess here everyday for some info."
        "You put some books back into your locker and head for the principal's office."
        stop music
        jump NikkiChantelleMeet01

label NerdIgnore:    
"You put some books back into your locker and head for the principal's office."
stop music
jump NikkiChantelleMeet01

label NikkiChantelleMeet01:
scene nikkichantelle01 with dissolve
$ renpy.pause(1.0, hard=True)
s "Oh, hi [name]! How was your first class?"
if (detention01 == True):
    p "Not so good, I have detention this afternoon..."
    show nikkichantelle01c
    s "Oh, [name], you never change... Nancy will not be pleased..."
    p "I know... Please don't tell her Nikki!"
    scene nikkichantelle01
    s "OK, but you owe me a favour then..."
if (detention01 == False):
    p "Pretty good, I met all my classmates and my teacher seems to like me."
    show nikkichantelle01b
    s "Oh, well done [name], I'm so proud of you!"
    window hide
    $ lust_points[17] += 1
    $ score += 1
    show lust01:
        xalign 0.15 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
scene nikkichantelle01
s "Here, I want you to meet my new best friend, Chantelle! She's in my class... Chantelle, this is my landboy [name]."
show nikkichantelle01d
ch "Oh, wow, you didn't tell me you had a landboy that was so...ho..I mean nice..."
window hide
$ lust_points[2] += 1
$ score += 1
show lust01:
    xalign 0.85 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
menu:
    "And Nikki didn't tell me she had such a beautiful classmate...":
        show nikkichantelle01c
        show nikkichantelle01d
        s "Of course I didn't tell you dumb dumb, I just met her a couple of hours ago!"
        window hide
        $ lust_points[17] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.15 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
        ch "Well, thank you...[name]..."
        window hide
        $ lust_points[02] += 1
        $ score += 1
        show lust01:
            xalign 0.85 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01        
        jump NikkiChantelleMeet02
    "Being nice runs in our family, that's why Nikki is so nice...":
        show nikkichantelle01b
        s "Oh, stop flattering me, you're embarrassing me..."
        window hide
        $ lust_points[17] += 1
        $ score += 1
        show lust01:
            xalign 0.15 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01        
        show nikkichantelle01e
        ch "Umpff..."
        window hide
        $ lust_points[2] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.85 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01 
        jump NikkiChantelleMeet02
    "Maybe we should all hang out together one day...":
        s "You wish!" 
        show nikkichantelle01d
        ch "That's a great idea, we could all get to know each other better..."
        window hide
        $ lust_points[2] += 1
        $ score += 1
        show lust01:
            xalign 0.85 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01        
        jump NikkiChantelleMeet02
            
label NikkiChantelleMeet02:
scene nikkichantelle01
s "Are you off to meet the principal, Ms Titsworthy?"
p "Yeah..."
show nikkichantelle01c
s "Watch out, she's tough...She wasn't nice to me..."
p "I can handle her, don't worry."
scene nikkichantelle01
s "OK, good luck, but try not to stare at her tits [name]..."
p "Pff, as if I'm the kind of guy who would do such a thing..."
jump Principal01

label Principal01:
scene principal01 with dissolve
$ renpy.pause(1.0, hard=True)
p "(Holy cow! Nikki wasn't kidding about her tits, they're huge!)"
so "[name] Johnson? Ah, yes, one of our new students from New Major City..."
menu:
    "Yes ma'am.":
        so "Good. Please sit down and let's look at your file."
        jump Principal02
    "Yeah, whatever.":
        so "Yes MA'AM. You will learn to show respect or you will not last long in our school."
        menu:
            "That's how we talk in New Major City. Deal with it.":
                so "Quite the attitude young man. I like a fighter... I'll deal with it later..."
                window hide
                $ lust_points[20] +=1
                $ score += 1
                show lust01:
                    xalign 0.55 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01                
                $ MCattitude = True
                so "For now, sit down and let's look at your file."
                jump Principal02
            "Sorry ma'am, I meant no disrespect.":
                so "Good. Please sit down and let's look at your file."
                jump Principal02

label Principal02:
scene principal02 with dissolve
$ renpy.pause(1.0, hard=True)
so "From what I read, you're a pretty average student..."
menu:
    "I've got a big sausage that's not average.":
        $ MCattitude = True
        so "...in the academic department. This is a school, not a stripclub."
        so "But perhaps you are indeed distracted by raging hormones and find it hard to concentrate on your studies?"
        scene principal03 with dissolve
        $ renpy.pause(1.0, hard=True)
        so "For example, right now, I can see you eyeing out my generous bosom..."
        jump PrincipalMenu   
    "I will try my best and study hard to get better grades.":
        so "Good, your landlady is paying a lot of money for you to be here, don't waste it."
        so "Perhaps one of your issues is that you are easily distracted by your raging hormones..."
        scene principal03 with dissolve
        $ renpy.pause(1.0, hard=True)
        so "For example, right now, I can see you eyeing out my generous bosom..."
        jump PrincipalMenu

label PrincipalMenu:        
menu:
    "I didn't even notice them!":
            so "I find that hard to believe. I have the largest boobs on the island. I KNOW every male is immediately drawn to them..."
            jump Principal03
    "Well, they are kind of sticking out...":
            so "These babies are what will get me elected in the senate... And what will get you to obey me..."
            window hide
            $ lust_points[20] +=1
            $ score += 1
            show lust01:
                xalign 0.4 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
            jump Principal03
            
label Principal03:
so "So here's the deal... You concentrate on your studies and you don't go around chasing all the girls to try and fuck them with that fat log I can see growing in your pants..."
so "Or you'll be stuck with me every afternoon, to get some GUIDANCE on how to improve your grades..."
menu:
    "Yes I promise I will not chase any girl from school...":
        if (MCattitude == True):
            so "Not sure I believe you considering your attitude..."
            jump Principal04
        if (MCattitude == False):
            jump PrincipalGood
    "I make no such promise, I'll fuck whoever I want! I'm da MAN!":
        so "(sigh)... I see, I thought it would come down to this..."
        jump Principal04

label Principal04:
scene principal04 with dissolve
$ renpy.pause(1.0, hard=True)
so "Clearly, you need some GUIDANCE right now. For example, to stop you from staring at women's boobs..."
so "Don't you like my legs too? They're so silky and smooth..."
p "gggg...."
scene principal05 with dissolve
$ renpy.pause(1.0, hard=True)
so "I'll take this as a yes... Focus on my legs... And on the delicate arches of my feet..."
so "Now lick the toe, you filthy boy, lick it!"
scene principal06 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/sucking.mp3"
so "There you go... Your place is down on your knees worshipping my feet. You understand that now?"
menu:
    "What? No way! I'm da MAN, my boner is my Master!":
        so "Then you need some more training... With my feet..."
        window hide
        $ lust_points[20] +=1
        $ score += 1
        show lust01:
            xalign 0.7 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump Principal07        
    "Yes, I can see the light! Hallelujah!":
        so "It was easier than I thought... You are a good little foot puppy..."
        jump Principal07

label Principal07:
scene principal07 with dissolve
$ renpy.pause(1.0, hard=True)
so "Now give that hard cock of yours a breather... The poor thing is straining against your shorts... And go and sit on the sofa while I get ready for your \"guidance\" session..."
scene principal08 with dissolve
$ renpy.pause(1.0, hard=True)
so "I don't recall telling you to put your hand on that thing, take it off!"
so "Just look at it, hard with lust, ready to explode and pump its mighty load all over my feet..."
menu:
    "I'd rather cover your huge knockers in an inch-thick layer of my cum....":
        so "I told you to focus on my feet, slave boy!"
        so "And I very much doubt you could cum enough to cover my jugs!"
        window hide
        $ lust_points[20] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        p "Well, hum... I could try..."
        so "No you couldn't. Now focus on the task at hand... or at foot in this case."
        jump Principal09
    "I'd rather pump it deep inside your pussy...":
        so "Well guess what? You can't..."
        so "And since you can't impregnate our school girls either, you will have to empty those balls on a regular basis... My way..."
        $ needfootjob = True
        jump Principal09
    "Oh yeah, I'm ready, atone for my fuckstick's sins with your feet Principal Titsworthy!":
        so "Get ready slave boy!"
        jump Principal09

label Principal09:
scene principal09 with dissolve
$ renpy.pause(1.0, hard=True)
so "Now focus on my legs and my feet as they tame your lusty shaft..."
$ principalfootjob = True
stop music
play music "Sounds/principalslow01.mp3"
show moviefootjobslow
show faster
call screen principalfootjob
screen principalfootjob:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("FootJobFast")

label FootJobFast:
stop music
hide faster
play music "Sounds/principalfast01.mp3"
show moviefootjobfast
show cum
call screen footjobfaster
screen footjobfaster:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PrincipalCum")

label PrincipalCum:
hide moviefootjobfast
hide moviefootjobslow
stop music
scene principal10
$ renpy.pause(1.0, hard=True)
so "Yes, that's a good boy, empty those massive balls of all their filthy cum..."
play sound "Sounds/cumming.mp3"
scene principal11 with dissolve
$ renpy.pause(1.0, hard=True)
so "OMG, you're really cumming like a stallion aren't you?"
so "My feet are covered in your sticky mess... Hopefully, that cum-cannon is empty so you won't be chasing our girls today."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
so "I need to get cleaned up. Off you go, your next appointment is with nurse Bigguns down the hallway for your physical check-up."

label Principal12:
scene principal12 with dissolve
$ renpy.pause(1.0, hard=True)
so "Oh, my poor plant... Why will you not give me flowers?"
p "What's wrong with it?"
so "It won't blossom... It's a \"Bostiboobicus Gigantus\" , a plant that's very rare and unique to our island...(sigh)"
p "Well, maybe I could try and find one for you Principal Titsworthy."
so "Oh really? Yes, why not, that will get your mind off girls' bosoms..."
p "(cough) Sure. What does it look like?"
so "It's in the shape of... two large boobs. Two large pink boobs."
p "Ah I see, that's very...unique indeed. "
so "Don't be late for your next appointment [name]!"
jump Nurse01
label PrincipalGood:
scene principal01 with dissolve
$ renpy.pause(1.0, hard=True)
so "Well, it seems you are a good boy after all... I won't have to give you \"guidance\" today..."
so "Off you go, your next appointment is with nurse Bigguns down the hallway for your physical check-up."
scene principal12b with dissolve
$ renpy.pause(1.0, hard=True)
so "Oh, my poor plant... Why will you not give me flowers?"
p "What's wrong with it?"
so "It won't blossom... It's a \"Bostiboobicus Gigantus\", a plant that's very rare and unique to our island... (sigh)"
p "Well, maybe I could try and find one for you Principal Titsworthy."
so "Oh really? Yes, why not, that will get your mind off girls' boobies..."
p "(cough) Sure. What does it look like?"
so "It's in the shape of... two large boobs. Two large pink boobs."
p "Ah I see, that's very...unique indeed. "
so "Don't be late for your next appointment [name]!"
scene williecorridor with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/willie.wav"
wi "I've got me eyes on ya lad!"
p "What? What are you talking about?"
wi "I've got me eyes on ya, I tell ya!"
p "Totally crazy guy. I'd better hurry up for my appointment with nurse Bigguns..."

label Nurse01:
scene nurse01 with dissolve
$ hour += 1
$ renpy.pause(1.0, hard=True)
p "(cough). Nurse Bigguns? Principal TitsWorthy sent me to see you."
je "You can call me Jennifer. You're [name], right?"
p "Yes, that's right. I came for my physical."
je "Let me finish tidying up here, you can get undressed down to your skivvies and hop onto the examination table, I'll be with you in a moment."
scene nurse02 with dissolve
$ renpy.pause(1.0, hard=True)
je "Now don't be scared, I won't bite. I've seen plenty of boys your age in their undies, there's nothing to be ashamed of."
p "It's not that..."
je "Come on, take your hands away, I need to have a look..."
scene nurse03 with dissolve
$ renpy.pause(1.0, hard=True)
je "Now I can tell you are in great shape, but THIS... You don't have to try and impress me by stuffing your underwear with socks young man..."
p "I'm not! I'm just...huge down there."
je "Nonsense. Even adults don't have a penis this size. Well, you've asked for it, I'm gonna take them off, I need to examine your ballsack anyway..."
scene nurse04 with dissolve
$ renpy.pause(1.0, hard=True)
je "What the...? My, you really are HUNG judging by the size of that root!"
window hide
$ lust_points[10] +=1
$ score += 1
show lust01:
    xalign 0.2 yalign 0.8
    linear 1.0 yalign 0.6
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
p "I tried to warn you..."
scene nurse05 with dissolve
$ renpy.pause(1.0, hard=True)
je "OMG, this thing is MONSTROUS! It's like an anaconda!"
p "And it's still soft, so it gets much bigger hard..."
je "What??? But it's already twice the length and width of my husband's hard cock... How could that be?"
scene nurse06 with dissolve
$ renpy.pause(1.0, hard=True)
je "Mmmh, I have an idea... Can you...cum already too? You know, spew some white stuff out of your...cock?"
p "Sure, tons of it!"
je "Wow... Well, don't move young man, I need to fetch something and I'll be right back..."
scene nursesnooping with dissolve
$ renpy.pause(1.0, hard=True)
p "I'm alone, I don't know where she went..."
menu:
    "Snoop around":
        jump NurseSnooping
    "Wait for the nurse to return...":
        jump Nurse02

label NurseSnooping:
play music "Sounds/snooping.mp3"
$ d2rollnurse=renpy.random.randint(0, 1)
if (d2rollnurse == 0):
    call screen nursesnoop01
if (d2rollnurse == 1):
    call screen nursesnoop02
$ renpy.pause(1.0, hard=True)
stop music
"You were too slow and didn't find anything. Nurse Jennifer is coming back..."
jump Nurse02

label FoundPendulum:
scene nursesnooping
$ renpy.pause(1.0, hard=True)
stop music
show pendulum
show square
play sound "Sounds/found.mp3"
"You found a hypnosis pendulum."
$ pendulum = True
hide pendulum
hide square

label Nurse02:
scene nurse07 with dissolve
$ renpy.pause(1.0, hard=True)
"After a short while, the nurse returns holding a small glass cup."
je "I would like you to... get hard and give me a sperm sample. Can you do that for me?"
menu:
    "Sure Jennifer!":
        jump NurseCum01
    "That sounds highly inappropriate...":
        jump Nurse03
    "I don't give out my sperm willy-nilly for free...":
        jump Nurse04

label Nurse03:
je "It's for science! I swear to God! I'll send it for analysis to the clinic, that's all..."
p "Ah, I see. Fine then."
jump NurseCum01

label Nurse04:
scene nurse07b with dissolve
$ renpy.pause(1.0, hard=True)
je "I see. A bargaining man... I'll give you ten dollars if you fill that cup to the brim."
menu:
    "Deal!":
        $ nursecumdeal = True
        $ money += 10
        jump  NurseCum01
    "Not enough, my sperm is sacred, it's worth a lot more.":
        je "Oh, gimme a break... Sacred? Who do you think you are? It's ten dollars or the deal is off!"
        window hide
        $ lust_points[10] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        p "Fine, fine... But it IS sacred!"
        $ nursecumdeal = True
        $ money += 10
        jump  NurseCum01
        
label NurseCum01:
p "Well, I might need a bit of...stimulation to get hard."
je "Humpf... Normally, boys your age get hardons for no reason at all... But OK, I'll show you what I'm wearing underneath my blouse if that can help..."
scene nurse08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Fuck yeah, they are so nice and firm... All the way nurse.."
scene nurse09 with dissolve
$ renpy.pause(1.0, hard=True)
je "No, that's it, I can't show you my breasts, they are reserved for my husband..."
p "Ok, but turn round then so I can admire that arse of yours..."
je "But... Aren't my big breasts in sexy lingerie enough for you to get turned on?"
p "I'm almost hard, but some more incentive..."
scene nurse10 with dissolve
$ renpy.pause(1.0, hard=True)
je "If my husband saw me like that... He would kill me..."
je "Are you hard yet?"
p "Oh yeah, I'm hard alright... You can turn round and see for yourself..."
scene nurse11 with dissolve
$ renpy.pause(1.0, hard=True)
je "Oh my GOD, you are so MASSIVE! I hope your sperm is as potent and virile as this giant weapon suggests..."
window hide
$ lust_points[10] +=1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
menu:
    "Wank me if you want my cum!":
        je "God, you are so... demanding... I need a free hand to hold the cup, so I'll just hold your cockhead, but you wank that monster yourself."
        jump NurseCum02
    "Let me jack off over those fat titties of yours and cover them in my cream":
        je "What??? No, you need to cum INSIDE the cup you idiot!" 
        window hide
        $ lust_points[10] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.2 yalign 0.6
            linear 1.0 yalign 0.8
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        je "I'll help you by tugging on that...thing, but be real quick will ya, this is not the normal procedure!"
        jump NurseCum02
        
label NurseCum02:
scene nurse12 with dissolve
$ renpy.pause(1.0, hard=True)
je "There's so much precum flowing out of it already... More than a full load from my hubby... Come on, cum for me!"
play sound "Sounds/wanking.mp3"
scene nurse13a
$ renpy.pause(0.3, hard=True)
scene nurse13b
$ renpy.pause(0.3, hard=True)
scene nurse13a
$ renpy.pause(0.3, hard=True)
scene nurse13b
$ renpy.pause(0.3, hard=True)
scene nurse13a
$ renpy.pause(0.3, hard=True)
scene nurse13b
$ renpy.pause(0.3, hard=True)
scene nurse13a
$ renpy.pause(0.3, hard=True)
scene nurse13b
$ renpy.pause(0.3, hard=True)
scene nurse13a
$ renpy.pause(0.3, hard=True)
scene nurse13b
$ renpy.pause(0.3, hard=True)
scene nurse13a
$ renpy.pause(0.3, hard=True)
scene nurse13b
$ renpy.pause(0.3, hard=True)
scene nurse13a
$ renpy.pause(0.3, hard=True)
scene nurse13b
$ renpy.pause(0.3, hard=True)
scene nurse13a
$ renpy.pause(0.3, hard=True)
scene nurse13b
$ renpy.pause(0.3, hard=True)
play sound "Sounds/ryancumming.mp3"
scene nurse14 with dissolve
$ renpy.pause(1.0, hard=True)
je "God, your cum is flying everywhere... BUT in the cup!"
p "I can't control it when it's spewing its sauce!"
je "I guess I'll just have to... catch it..."
scene nurse15 with dissolve
play sound "Sounds/randyboycumming.mp3"
$ renpy.pause(1.0, hard=True)
je "There, that's better, it's flowing into the cup at last!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01

scene nurse16 with dissolve
$ renpy.pause(1.0, hard=True)
je "Hum, I must say, it tastes... good... Oh God, I'm so ashamed of myself..."
window hide
$ lust_points[10] +=1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
je "Err, thanks for filling the cup... to overflowing... I'll be sending it to the lab for analysis... Off you go, lunch time is soon."
jump Lunch01

label Lunch01:
scene lunch01 with dissolve
$ hour += 1
stop music
play music "Sounds/lunchambience.mp3"
$ renpy.pause(1.0, hard=True)
$ lustaddedB = 2
call Challenger from _call_Challenger_6
$ lustaddedB = 3
call Challenger from _call_Challenger_7
$ lustaddedB = 1
call Challenger from _call_Challenger_8
$ lustaddedB = 1
call Challenger from _call_Challenger_9
$ challengercalls += 2
p "The school cafeteria is packed... Where should I sit?"
menu:
    "Sit with your classmates":
        jump LunchClass
    "Sit with Nikki":
        jump LunchSister

label LunchClass:
$ lunchclass = True
scene lunch02 with dissolve
$ renpy.pause(1.0, hard=True)
q "Hey [name], there you are! Have this empty seat next to me, I kept it for you."
menu:
    "Thanks. I guess...":
        jump LunchClass02
    "I don't want to sit there, move your arse and give me your seat!":
        q "I thought you were my friend! I guess I was wrong, you're just an arsehole..."
        q "Well, I'm not moving and I'll call the principal if you try anything..."
        $ quentinfriend = False
        jump LunchClass02

label LunchClass02:
scene lunch02sit with dissolve
$ renpy.pause(1.0, hard=True)
label LunchClassChoice:
scene lunch02sit with dissolve    
menu:
    "Talk to Laura" if (spokenlunchlaura == False):
        show lunchlaura
        la "I hate this food. I hate this school."
        p "Yeah, it's disgusting, makes me wanna puke."
        $ spokenlunchlaura = True
        jump LunchClassChoice
    "Talk to Kate" if (spokenlunchkate == False):
        if (katepissedoff == True):
            show lunchkateunhappy
            k "You let me down this morning during class... Now I have detention when I could be thinking about what bikini I could wear..."
            p "I'm sorry. I'll make it up to you. I'll be a dumb student just like you so we can end up in detention together."
            k "Ooh, thanks, hee hee."
            play sound "Sounds/katehihi.mp3"
            window hide
            $  lust_points[11] += 1
            $ score += 1
            show lust01:
                xalign 0.15 yalign 0.6
                linear 1.0 yalign 0.4
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
            $ spokenlunchkate = True
            jump LunchClassChoice
        else:
            show lunchkatehappy
            k "What bikini do you think I should wear on Friday [name]?"
            menu:
                "One that barely covers your huge tits.":
                    k "Oooh, you think so?"
                    play sound "Sounds/katehihi.mp3"
                    $ renpy.pause(1.0, hard=True)
                    window hide
                    $ lust_points[11] += 1
                    $ score += 1
                    show lust01:
                        xalign 0.15 yalign 0.6
                        linear 1.0 yalign 0.4
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lust01
                    $ spokenlunchkate = True
                    jump LunchClassChoice
                "You should surprise everyone by going naked.":
                    k "Ooh, you're ssooo silly! I can't do that, it's not allowed!"
                    play sound "Sounds/katehihi.mp3"
                    $ spokenlunchkate = True
                    jump LunchClassChoice                    
                "Anything will look good on you.":
                    k "Uuuh, that's not very useful... I need to know what to wear!"
                    p "Tell you what, I could take pictures of you so you can better decide which bikini to choose?"
                    k "Ooh, are you a photographer? I've been looking for someone who could show me what I look like, because I can't see myself."
                    p "Yeah sure... I have a great camera, I'll let you know when I set everything up and you can come round to my place to try on some bikinis."
                    k "oooh, I can't wait! Hee hee!"
                    p "(I'd better find a good camera real soon...)"
                    $ katephotoasked = True
                    $ spokenlunchkate = True
                    jump LunchClassChoice

    "Talk to Frieda":
        show lunchfrieda
        p "Hey Frieda, what are you doing this afternoon?"
        fr "I vill be studying in the school library."
        p "Oh? I didn't even know this school had a library..."
        fr "Yes, it is at the end of corridor F."        
        window hide
        $ discoverlibrary = True
        show addedlocation:
            xalign 0.7 yalign 0.3
            linear 1.0 yalign 0.1
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide addedlocation
        p "Ach, zo interesting."
        jump LunchClassChoice

    "Talk to Maddy":
        show lunchmaddy
        p "Will you also compete this Friday in the swimsuit pageant?"
        md "No! I'm not that kind of girl!"
        q "That's too bad... You're so fit in a bikini."
        md "Shut up FREAK!"
        p "Well, that escalated quickly..."
        jump LunchClassChoice

    "Talk to Quentin" if (spokenlunchquentin == False):
        if (quentinnotfriend == True):
            q "I ain't talking to you. You were mean to me."
            jump LunchClassChoice
        else:
            q "Isn't this school great? I love it!"
            menu:
                "Yeah, I like it a lot too.":
                    q "I'm the best student here. The teacher loves me for that."
                    jump LunchClassChoice
                "No, it sucks. I hate it.":
                    show lunchlaurahappy
                    window hide
                    $ lust_points[13] +=1
                    $ score += 1
                    show lust01:
                        xalign 0.35 yalign 0.4
                        linear 1.0 yalign 0.2
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lust01
                    q "If you were a better student like me, you'd love it too..."
                    $ spokenlunchquentin = True
                    jump LunchClassChoice

    "Just eat up already":
        jump LunchEnd


label LunchSister:
scene lunchsister01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I think I'll join you guys to be with Nikki."
j "Where do you think you're going? This table is for the SENIORS!"
show lunchchantelle01
ch "There is no such rule José, stop being a dickhead, he's Nikki's landboy."
show lunchjose01
j "I make the rules here! This is MY table!"
hide lunchjose01
show lunchjose02
j "Don't you agree with me babe?"
show lunchbrittany01
br "Oh, yeah, whatever..."
menu:
    "Please defend me Nikki!":
        if (lust_points[17] >= 5):
            hide lunchbrittany01
            show lunchnikki01
            s "I want [name] to sit with me on his first day of school. Come [name], there's an empty seat next to me right here."
            jump LunchSister02
        if (lust_points[17] <= 4):
            hide lunchbrittany01
            show lunchnikki01
            hide lunchjose02
            s "I don't know [name]... I think it's best not to piss off José. Go and sit with your classmates, they seem really nice. I'll see you at home tonight."
            hide lunchchantelle01
            p "Ok... I'll go and sit with my classmates then... Bye Chantelle..."
            ch "See you [name]... (sigh)"
            jump LunchClass
    "Ok, I'll go and sit with my classmates then. They are nicer than you sorry lot of old farts.":
        jump LunchClass

label LunchSister02:
$ lunchsister = True
$ chantellegym = False
scene lunchsister02 with dissolve
$ renpy.pause(1.0, hard=True)
label LunchSisterChoice:
menu:
    " Talk to Nikki":
        p "I think I'm ready to lift that dresser Nikki, I feel like...super-strong!"
        show lunchnikki02
        s "Oh good, cos I really want to find them tonight. If you fail, I will ask José to help me. He's really strong too."
        p "Pfff, he's puny compared to me..."
        jump LunchSisterChoice
    "Talk to Chantelle" if (chantellegym == False):
        $ chantellegym = True
        p "What do you plan on doing this afternoon Chantelle?"
        show lunchchantelle02
        ch "I might go to the school gym to do some exercise, I'm not sure. Will you go too?"
        menu:
            "Yes":
                ch "Then, I most DEFINITELY will go (wink)."
                $ lust_points[2] +=1
                $ score += 1
                show lust01:
                    xalign 0.35 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01                
                hide lunchchantelle02
                jump LunchSisterChoice
            "Maybe, I haven't decided yet.":
                hide lunchchantelle02
                ch "Oh, OK. It's pretty good, it has some heavy weightlifting equipment for boys like you (wink)."
                jump LunchSisterChoice
    "Talk to Brittany":
        show lunchbrittany02
        br "You're just a junior. I'm too important to be seen talking to a junior in public like that."
        br "People like you should, like, hide in the library down corridor F or something..."
        window hide
        $ discoverlibrary = True
        show addedlocation:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide addedlocation
        p "Al-rightee then. Nice talking to you too."
        hide lunchbrittany02
        jump LunchSisterChoice
    "Talk to José" if (spokenlunchjose == False):
        $ spokenlunchjose = True
        scene lunchjose03
        j "What do you want worm?"
        menu:
            "Your head on a spike.":
                show lunchjose04
                j "Before the end of the week, it will be your landlady's head on my mighty spike! Ha ha!"
                show lunchnikki03
                s "What? That's just...an awful thing to say!"
                window hide
                $ lust_pointsB[17] -=1
                show challengerlustminus01:
                    xalign 0.2 yalign 0.6
                    linear 1.0 yalign 0.8
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide challengerlustminus01
                hide lunchjose04
                show lunchjose05
                j "Sorry, I only meant it as a joke Nikki. I would... never of course..."
                p "You should be ashamed of yourself! I would never dare dream about fucking your landlady, that's just plain wrong..."
                scene lunchsister02
                jump LunchSisterChoice
            "I think we might have gotten off on the wrong foot...":
                j "Yeah, cos you want to steal my place as the legitimate school stud!"
                p "YOU challenged me, remember?"
                show lunchnikki03
                s "Enough bickering you two! We've had enough!"
                scene lunchsister02
                jump LunchSisterChoice
            "Don't talk to Nikki, she's off limits, you hear me?":
                scene lunchnikki04 with dissolve
                $ renpy.pause(1.0, hard=True)
                s "Hey! I talk to whoever I want, now eat up and be quiet [name]!"
                window hide
                $ lust_points[17] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.2 yalign 0.6
                    linear 1.0 yalign 0.8
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
                p "But... I was only trying to defend you Nikki... It's not fair... I just lost a lust point."
                scene lunchsister02
                jump LunchSisterChoice

    "Just eat up already":
        jump LunchEnd


label LunchEnd:
stop music
scene lunchempty with dissolve
$ hour += 1
$ renpy.pause(1.0, hard=True)
p "Everyone finished eating and left..."

if (detention == True):
    p "I have to go to detention or I'm in trouble..."
    jump Detention02

label Afternoon:
p "I've got the afternoon free. What should I do?"
menu:
    "Go to my locker" if (seenlocker02 == False):
        jump Locker02
    "Go to the school gym" if (seenschoolgym02 == False):
        jump SchoolGym01
    "Go to the school library" if (discoverlibrary == True):
        jump SchoolLibrary02
    "Go to the school backyard" if (seengoths == False):
        jump Goths01
    "Leave the school and go the Burbs":
        jump Burbs02

label Detention02:
scene detention01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Kate and [name], You both have detention for one hour. During that time, I want to see you studying hard, is that clear?"
p "Damn, this is going to be so boring... I wonder what I could do to pass the time?..."
p "Mmh, Kate is looking great in that schoolgirl outfit... But it would be better if she was naked..."
menu:
    "Daydream about Kate":
        jump KateDayDream
    "Pretend you're studying":
        jump EndDetention

label KateDayDream:
play sound "Sounds/dreaming.mp3"
scene katedreaming01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
k "oops, I just dropped my top. Hee hee..."
p "Now we're talking... Don't bother looking for it baby..."
scene katedreaming02 with dissolve
$ renpy.pause(3.0, hard=True)
k "Ooh, [name], can you see that my panties are soaking wet for you?..."
p "Yeah, they are, sssooo wet. Now play with that pussy Kate..."
scene katedreaming03 with dissolve
$ renpy.pause(3.0, hard=True)
k "Oooh, I wish that was your great big cock [name]...My hole needs a good stretching only you can satisfy!"
p "Yeah, I'll fuck you, don't worry, I'll fuck you before the end of the week..."
stop music

label EndDetention:
play sound "Sounds/schoolrecess.mp3"
scene detention01 with dissolve
$ hour += 1
$ renpy.pause(1.0, hard=True)
t "That's it, you're both free to go now. I hope you learnt your lesson and I won't have to see you again in detention this week."
scene katedetentiondoor with dissolve
$ renpy.pause(1.0, hard=True)
p "I'm so glad this is over, I was getting ssooo bored."
k "Me too, I didn't do any work at all, I was just thinking about I would wear at the Bikini pageant on Friday...Hi hi."
if (katephotoasked == False):
    p "Tell you what, I could take pictures of you so you can better decide which bikini to choose?"
    k "Ooh, are you a photographer? I've been looking for someone who could show me what I look like, because I can't see myself."
    p "Yeah sure... I have a great camera, I'll let you know when I set everything up and you can come round to my place to try on some bikinis."
    k "Oooh, I can't wait! Hee hee!"
    window hide
    $ lust_points[11] += 1
    $ score += 1
    show lust01:
        xalign 0.5 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    p "(I'd better find a good camera real soon...)"
    $ katephotoasked = True
jump Afternoon

label Locker02:
$ seenlocker02 = True
$ d3rollb=renpy.random.randint(0, 2)
if (d3rollb == 0):
    jump LockerKate01      
if (d3rollb == 1):
    jump LockerEmpty02    
if (d3rollb == 2):
    jump BritLocker
 
label LockerEmpty02:
scene lockerempty with dissolve
$ renpy.pause(1.0, hard=True)
$ seenlockerempty = True
p "There's no one around... Like everyone left school or something. And I'm here, wasting my time in empty corridors like an idiot."
jump Afternoon

label LockerKate01:
stop music
scene lockerkate01 with dissolve
$ renpy.pause(1.0, hard=True)
$ seenlockerkate = True
k "Ooops, I just dropped my pen."
menu:
    "Hang on, I'll pick it up for you.":
        k "Uh oooh... OK..."
        scene lockerkate06
        $ renpy.pause(1.0, hard=True)
        p "Here you are Kate, that pen that you just dropped accidentally..."
        scene lockerkate06
        $ renpy.pause(1.0, hard=True)
        k "Oh, look, I found my pen!"
        window hide
        $ lust_points[11] += 1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump LockerKate08
    "Well pick it up then.":
        k "Uh...oh...OK."
        scene lockerkate02
        $ renpy.pause(1.0, hard=True)
        k "Oooh, it's too far, I can't reach it...Uuh..."
        menu:
            "Well, bend over some more...":
                jump LockerKate03
            "Offer to help":
                k "No, I'm...OK....Ooh, I hope my panties aren't...like... showing.... Are they?"
                menu: 
                    "Not at all, I can't see a thing. You can bend more.":
                        jump LockerKate03
                    "Mmh, they're white and they're soaking wet?":
                        k "Wh..What... soaking wet? Hee hee..."
                        play sound "Sounds/katehihi.mp3"
                        $ renpy.pause(1.0, hard=True)
                        window hide
                        $ lust_points[11] +=1
                        $ score += 1
                        show lust01:
                            xalign 0.75 yalign 0.6
                            linear 1.0 yalign 0.4
                        play sound "Sounds/more.mp3"
                        $ renpy.pause(2, hard=True)
                        hide lust01
                        k "I should bend more you think?"
                        p "If you want to reach that pen, yes..."
                        jump LockerKate03
 
label LockerKate03:
scene lockerkate03 with dissolve
$ renpy.pause(1.0, hard=True)
k "Like that?... I still can't find my pen...Oooh, where is it?"
menu:
    "It's right in front of you, you dumb bimbo.":
        k "Oooh, yes, I see it now...Hee...hee..."
        play sound "Sounds/katehihi.mp3"
        jump LockerKate07
    "Look some more, meanwhile, I'll probe behind you, it might be stuck somewhere...":
        k "Ooh, OK...hee...hee..."
        play sound "Sounds/katehihi.mp3"
        scene lockerkate04 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "No, nothing there, maybe if I go a bit deeper..."
        k "Ooooh! What are you...? Did you find it? hee hee..."
        play sound "Sounds/katehihi.mp3"
        $ renpy.pause(1.0, hard=True)
        window hide
        $ lust_points[11] += 1
        $ score += 1
        show lust01:
            xalign 0.9 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        menu:
            "No, I think I need your help back there.":
                k "Uuh...hee...hee...OK..."
                play sound "Sounds/katewank.ogg"
                scene lockerkate05 with dissolve
                $ renpy.pause(1.0, hard=True)
                k "Ooh, no, I can't find it either...Aaah, Ooooh..."
                window hide
                $ lust_points[11] += 1
                $ score += 1
                show lust01:
                    xalign 0.9 yalign 0.8
                    linear 1.0 yalign 0.6
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
                k "Ooh, now I think I found it... hee hee..."
                play sound "Sounds/katehihi.mp3"
                scene lockerkate06 with dissolve
                $ renpy.pause(1.0, hard=True)
                k "Oh, look, I found my pen!"
                jump LockerKate08
            "Don't mind me, I'm in control of the situation...":
                jump LockerKate07

label LockerKate07:
scene lockerkate06 with dissolve
$ renpy.pause(1.0, hard=True)
k "Uh...OK...I'll continue looking... Oh, look, I found my pen!"
label LockerKate08:
scene lockerkate07 with dissolve
$ renpy.pause(1.0, hard=True)
p "Well done, you're such a smart girl! By the way, it's actually a pencil, not a pen."
label KateLockerEnd:
k "Ooh, thank you... [name]?..."
p "Yes, that's right. You can \"drop\" by anytime...."
k "Uh...OK."
if (katephotoasked == False):
    p "Since you will compete in the bikini pageant, I could maybe take pictures of you so you can better decide which bikini to choose?"
    k "Ooh, are you a photographer? I've been looking for someone who could show me what I look like, because I can't see myself."
    p "Yeah sure... I have a great camera, I'll let you know when I set everything up and you can come round to my place to try on some bikinis."
    k "Oooh, I can't wait! Hee hee!"
    window hide
    $ lust_points[11] += 1
    $ score += 1
    show lust01:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    p "(I'd better find a good camera real soon...)"
    $ katephotoasked = True
    jump Afternoon
else:
    jump Afternoon


label BritLocker:
scene
stop music
play sound "Sounds/footsteps.mp3"
$ renpy.movie_cutscene("Day2/britlocker.ogv")
show moviebritlocker with dissolve
show slowmo
call screen britslowmo
screen britslowmo:
    modal True
    button:
        xpos .82
        ypos .9
        xysize(120, 50)
        action Jump ("BritSlowMo")
label BritSlowMo:
hide moviebritlocker
hide slowmo
play sound "Sounds/britlockerslowmo.mp3"
show moviebritlockerslowmo with dissolve
scene lockerbritmovie
$ renpy.pause(5.0, hard=True)

label LockerBrit01:
$ seenlockerbrit = True
scene lockerbrit01 with dissolve
$ renpy.pause(1.0, hard=True)
j "Hey babe, how are you doing?"
br "Fabulous, I just got this new outfit on the weekend, do you like?"
j "Fuck yeah, you look so hot in it, you're sure to win the pageant on Friday babe..."
$ lust_pointsB[1] +=1
show challengerlustplus01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide challengerlustplus01

menu:
    "Continue eavesdropping on the conversation":
        jump LockerBritEavesdrop
    "Barge in on the conversation":
        jump LockerBrit02
label LockerBrit02:
scene lockerbrit02 with dissolve
$ renpy.pause(1.0, hard=True)
j "Can't you see I'm talking to Brittany? Get lost [name]!"
br "Who's he?"
j "Just some new junior student, not worth your time of day babe..."
br "I'll decide that."
menu:
    "Allow me to introduce myself, I'm [name] Johnson.":
        show lockerbrit02b
        br "OMG, that's ssooo interesting. Get outta of my sight kid."
        j "Hah hah, nice one Brittany! You heard her, leave us alone loser!"
        jump Afternoon
    "I might be a junior student, but I'm a senior in bed.":
        show lockerbrit02b
        br "So boring, another wannabe stud. I only date REAL studs."
        j "Yeah, like ME. Do you hear that [name]?"
        br "I don't recall saying YOU were a REAL stud either..."
        show lockerbrit02c
        j "But, babe, everyone knows I'm the school stud..."
        br "Well, maybe I should look OUTSIDE of this school... A goddess like me deserves the BEST..."
        jump BritLocker03
    "I was elected prom king at my old school.":
        show lockerbrit02d
        br "Really? Mmmh, maybe your old school was full of total losers then if you won...But still..."
        window hide
        $ lust_points[1] += 1
        $ score += 1
        show lust01:
            xalign 0.2 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump BritLocker03

label BritLocker03:
scene lockerbrit02 with dissolve
$ renpy.pause(1.0, hard=True)
br "I've wasted enough time talking to you. A true princess like me needs to spend more time pampering herself."
br "Do not disturb me until I grant you permission."
menu:
    "Sure ma'am, at your cervix your Magnificent Beautifulness! (snickers)":
        show lockerbrit02b
        br "Be gone!"
        jump Afternoon
    "Who the fuck do you think you are you cheap whore?":
        show lockerbrit02b
        br "WHAT did you say???"
        if (lust_points[1] >= 1):
            window hide
            $ lust_points[1] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.6
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
        show lockerbrit02c
        j "Do you want me to beat up this little shit for you baby?"
        br "No, he's not even worth it! But thanks for asking José... I like to have a protector at hand."
        window hide
        $ lust_pointsB[1] +=1
        show challengerlustplus01:
            xalign 0.2 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustplus01
        br "Now YOU.. Don't ever show your junior face again in my presence!"
        jump Afternoon
    "I have a present for you, a golden wristband that will befit a true princess like you. (offer wristband)" if (wristband == True):  
        show lockerbrit02d
        br "Oh, it's so nice! How can I thank you... [name]?"
        show lockerbrit02c
        j "Hang on a minute, I've seen this exact same wristband for like 5 dollars at the local store."
        show lockerbrit02b
        br "What??? How dare you? I am worth much more than that!"
        if (lust_points[1] >= 1):
            window hide
            $ lust_points[1] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.6
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            $ britpresentfail = True
            hide lockerbrit02c
            j "hah, hah, what a loser! I would never treat the prom queen as a cheap slut myself..."
            jump Afternoon
        menu: 
            "José is lying. It was actually 4 dollars.":
                br "Oh my God, that's even worse!!! Be gone and keep your cheap wristband!"
                jump Afternoon
            "Oh, hang on a minute, I seem to have given you the wrong one. My bad, this one was meant for...err.. Kate.":
                br "That would indeed suit that cheap bimbo... Who dares try to claim my throne as bikini pageant queen this year again!"
                br "Come back with your \"proper\" present tomorrow then. Or else..."
                p "Yeah... Of course... Ahem... Thank you, your...err.. majesty."
                $ britpresentfail = True
                jump Afternoon

label LockerBritEavesdrop:
scene lockerbrit01 with dissolve
if (brittanyjosewin == False):
    j "Listen babe, why don't we meet tonight at my place?"
    if (lust_pointsB[1]>=8):
        br "To do what exactly?"
        j "Talk about how beautiful you are and how hot you look in those expensive outfits you wear..."
        br "Oh, yes, I love that topic of conversation!"
        window hide
        $ lust_pointsB[1] +=1
        show challengerlustplus01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustplus01
    if (lust_pointsB[1]<=7):
        br "Maybe another night José, I need to try some new outfits."
        j "Can I come and help you?"
        br "No, I'm the best judge of what's best for me to wear, thank you..."
        j "Uh, OK, babe, whatever you say..."

if (brittanyjosewin == True):
    j "Hey babe, how great was it, pretty fucking great I'd say!"
    br "Yeah, that... huge cock... it was amazing, it hit all the right spots."
    j "I was hard as a rock since you're the most beautiful girl on the island...¨"
    br "Yeah, I know that..."

menu:
    "Barge in on the conversation":
        jump LockerBrit02
    "Leave, you are defeated, what's the point in arguing...":
        jump Afternoon

label SchoolLibrary02:
stop music
scene friedalibrary01 with dissolve
play music "Sounds/coughing.mp3"
$ renpy.pause(1.0, hard=True)
p "There's Frieda sitting in the library looking bored. Like everyone does in a library."
menu:
    "Talk to Frieda":
        jump Library02
    "Learn how to use the hypnosis pendulum" if (pendulum == True) and (pendulumactive == False):
        jump LibraryPendulum
    "Read the book about Goths Laura gave you" if (book == True) and (bookread == False):
        jump LibraryGoth
    "Leave":
        jump Afternoon

label LibraryPendulum:
scene ryanlibraryinternet with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/keyboard.ogg"
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump SchoolLibrary02

label LibraryGoth:
scene ryanreadinglibrary with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump SchoolLibrary02

label Library02:
scene friedalibrary02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Hi Frieda, what's up? You seem to be studying hard."
fr "I'm trying to but it's so boring... My parents vill kill me if I don't get an A grade this term."
label FriedaChoices:
menu:
    "That's too bad. They sound like real Nazis." if (friedanazis == False):
        show friedalibrary02b
        fr "Nein! My grandfather did nothing wrong, he was only obeying orders, klar?"
        window hide
        $ lust_points[8] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
        p "Oooh, touchy subject I see..."
        fr "Do not ever mention ze var again!"
        $ friedanazis = True
        hide friedalibrary02b
        jump FriedaChoices
    "Maybe you should wear lighter clothing to clear your mind. It's too hot here for what you're wearing." if (friedaclothes == False):
        show friedalibrary02c
        fr "You think so! Maybe you are right..."
        $ friedaclothes = True
        hide friedalibrary02c
        jump FriedaChoices
    "What if I helped you by... switching your grades?" if (friedahelped == False):
        show friedalibrary02d
        fr "That sounds naughty! How vill you do that? Zey are locked in Principal Titsworthy's office..."
        p "Well, I could try and sneak in somehow..."
        hide friedalibrary02d
        show friedalibrary02c
        fr "I hope you succeed. Not like the Germans during ze var."
        window hide
        $ lust_points[8] += 1
        $ score += 1
        show lust01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01        
        hide friedalibrary02c
        $ friedanazis = True
        $ friedahelped = True
        jump FriedaChoices
    "OK, I'll leave you alone to study then...":
        jump SchoolLibrary02
        
label Goths01:
stop music
$ seengoths = True
scene goth01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Apparently, this is where the goth kids hang out… Laura is here, with some douchebag dude and the local girl."
la "Hey [name], you decided to join us?"
go "What’s he doing here? Do you know him Laura?"
if (madelaurasmile == True):
    la "Yeah, he’s a new classmate, he’s kinda cool though."
elif (madelaurasmile == False):
    la "Yeah, he’s a new classmate, he’s kinda of a bore though."

label GothChoice01:
menu:
    "What's the local chick doing with you?" if (gothmenu <= 1):
        go "She's black, so she must be a goth."
        menu:
            "That makes absolutely no sense at all...":
                $ gothmenu += 1
                jump GothChoice01
            "Of course, silly me.":
                $ gothmenu += 1
                jump GothChoice01
    "Can I join your club?" if (gothmenu <= 1):
        go "No fucking way dude. You ain't no goth."
        $ gothmenu += 1
        jump GothChoice01
    "Talk to the black girl" if (gothmenu >= 2):
        show goth01d
        fc "Ou suis-je, que fais-je, dans quel état j’erre?"
        p "Hum... moi... non par-ley... frenchie."
        fc "Hein? Quoi?"
        p "Yeah, I think she got it..."
        hide goth01d
        jump GothChoice01
    "Talk to Laura" if (gothmenu >= 2):
        p "Hey Laura, I would really like to become a goth..."
        show goth01c
        la "You’re wearing a white tank top... You need to get a black t-shirt at least if you want to become a goth..."
        la "And it’s a matter of inner feelings. I don’t think you have what it takes…"
        menu:
            "Sure I do, I think about...like...killing myself all the time." if (jointtaken == False):
                go "Prove it!"
                p "What? You want me to...kill myself? Can't we wait at least till the end of the week?..."
                scene goth01b
                go "You can start by killing yourself slowly by taking a puff of this..."
                menu:
                    "Accept the joint and take a puff":
                        $ jointtaken = True
                        "You take a puff and feel nauseous..."
                        $ stamina -= 1
                        show staminaminus01:
                            xalign 0.9 yalign 0.2
                            linear 1.0 yalign 0.4
                        play sound "Sounds/panting.mp3"
                        $ renpy.pause(2, hard=True)
                        hide staminaminus01
                        show goth01c
                        la "Wow, you did... Now stop it Damian, he's had enough!"
                        window hide
                        $ lust_points[13] +=1
                        $ score += 1
                        show lust01:
                            xalign 0.35 yalign 0.4
                            linear 1.0 yalign 0.2
                        play sound "Sounds/more.mp3"
                        $ renpy.pause(2, hard=True)
                        hide lust01
                        scene goth01
                        jump GothChoice01
                    "Refuse and say that your body is your temple":
                        go "What a chicken..."
                        window hide
                        $ lust_points[13] -=1
                        $ score - 1
                        show lustminus01:
                            xalign 0.35 yalign 0.2
                            linear 1.0 yalign 0.4
                        play sound "Sounds/less.mp3"
                        $ renpy.pause(2, hard=True)
                        hide lustminus01
                        scene goth01
                        jump GothChoice01
            "I'm trying hard to think about death and shit, but it’s kinda depressing...":
                    la "It releases the darkness of your soul. Here, read this book."
                    $ book = True
                    show book
                    show square
                    play sound "Sounds/found.mp3"
                    "A book has been added to your inventory."
                    hide square
                    hide book
                    p "Uhh.. Thanks... guess..."
                    go "Now take a hike, we have some deep digging into the emptiness of the meaning of life to do..."
                    go "And don’t ever come back wearing this white tank top...DEATH TO ALL BUT METAL!"
                    show goth01c
                    la "DEATH TO ALL BUT METAL!"
                    show goth01d
                    fc "Hein? Quoi?"
                    jump Afternoon      
    "Talk to the goth kid" if (gothmenu >= 2):
        go "What’s your favorite band?"
        menu:
            "New Kids on the Block":
                go "What? Get the hell out of here!"
                la "So lame... I hate you."
                jump Afternoon
            "Pharell Williams":
                go "Someone please kill me... That's not even a band!"
                jump GothChoice01
            "The Cure":
                go "Nice..."
                jump GothChoice01
            "What's it to you dipshit?":
                go "What the fuck?..."
                la "Haha, he got you there..."
                go "He didn't answer the question..."
                la "Real goths don't have to answer questions..."
                jump GothChoice01

label SchoolGym01:
$ seenschoolgym02 = True
$ d3rolls=renpy.random.randint(0,2)
if (chantellegym == True):
    $ d3rolls = 1
    jump NextLabel

label NextLabel:
if (d3rolls==0):
    $ schoolgymempty = True
    jump SchoolGymEmpty
 
elif (d3rolls==1):
    stop music
    $ schoolgymchantelle = True
    play music "Sounds/gymmusic.mp3"
    scene chantellegym01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Chantelle is doing some curls... She hasn't seen me come in."
    menu:
        "Do some heavy training, better equipment means I can cut on my routine time (+1hr)":
            p "I hope you don't mind if I do some heavy training with barbells in my jockstrap?"
            ch "What?.. No, it's fine...Be my guest..."
            jump ChantelleRyanWorkout
        "Watch her for a while":
            jump SchoolGymChantelle02

elif (d3rolls==2):
    $ schoolgymmaddy = True
    jump SchoolGymMaddy01

label SchoolGymEmpty:
scene schoolgymempty with dissolve
$ renpy.pause(1.0, hard=True)
p "There's no one around, I could use this gym to train and get stronger..."
menu:
    "Do some heavy training, better equipment means I can cut on my routine time (+1hr)" if (workout == False):
        jump SchoolGymWorkout
    "Leave":
        jump Afternoon

label ChantelleRyanWorkout:
stop music
scene
play music "Sounds/workoutgroan.mp3"
$ renpy.movie_cutscene("Day2/schoolgymworkout.ogv", delay=-1, loops=-1, stop_music=False)
stop music
scene schoolgymworkout01
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
p "That was great, I can feel my muscles getting bigger and stronger already..."
window hide 
$ strength += 1
show strengthplus01:
    xalign 0.3 yalign 0.5
    linear 1.0 yalign 0.3
play sound "Sounds/more.mp3"
$ renpy.pause(3, hard=True)
hide strengthplus01
$ hour += 1
$ workout = True
scene schoolgymworkout02 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Sorry, I couldn't help but watch... Damn, you're so strong [name]!"
p "Yeah? You like my huge muscles?"
ch "Yes, I do, this made me...horny... I need to kiss you!"
scene schoolgymworkout03 with dissolve
$ renpy.pause(1.0, hard=True)
window hide
$ lust_points[2] += 2
$ score += 2
show lust02:
    xalign 0.7 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
p "What next?"
ch "This..is going too fast...maybe...I don't want to lose Nikki's friendship...sorry...I shouldn't have..."
p "But...What did I do wrong? It's not fair!"
ch "Another time maybe [name]... Let's leave it at that for now...I...should go now..."
$ muscleman += 1
jump Afternoon

label SchoolGymChantelle02:
scene chantellegym02 with dissolve
$ renpy.pause(2.0, hard=True)
p "Wow, Chantelle has such a fine body, nice big round arse and huge firm tits..."
scene chantellegym03 with dissolve
$ renpy.pause(2.0, hard=True)
ch "Do you like what you see [name]?"
p "Err, yeah, I was looking for some heavy curls..."
ch "The heaviest curls are over there... I assume these are the ones you plan to use to impress me right?"
menu:
    "No, I was thinking of a lighter short training today.":
        ch "Ah, sure, try these weights then... And let me watch how well you do with them..."
        jump SchoolGymChantelle03
    "Of course, I only use the biggest weights around all the time, piece of cake for me!":
        ch "Mmh, I want to see that..."
        jump SchoolGymChantelle04
    "Actually, I was planning on a serious routine with barbells, but I need to concentrate...(+1hr)":
        ch "Sure, I'll continue my exercises and I'll leave you alone, don't worry..."
        p "Also, I like to train with my shorts and tank top off, hope you don't mind..."
        ch "Ooh? No... I don't mind..."
        jump ChantelleRyanWorkout
        
label SchoolGymChantelle03:
stop music
scene chantellegym04a
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
ch "Mmmh, this looks a bit too easy for a muscle stud like you... I'll make it a tad harder..."
scene chantellegym05a
$ renpy.pause(1.0, hard=True)
p "AAAH, need to concentrate..."
ch "ooh, I can feel something stirring underneath me, what could it be? I'd better check by rubbing my arse against it..."
window hide
$ lust_points[2] += 1
$ score += 1
show lust01:
    xalign 0.8 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01

scene chantellegym06a
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
ch "Not bad, good self control there.... But they were rather small dumbbells, it was almost too easy..."
p "You almost got me, and now I've got a massive tent in my strap..."
ch "Well I'm not taking care of it here!... Not today anyway...! Bye bye [name]!"
$ hour += 1
scene schoolgymempty with dissolve
$ renpy.pause(1.0, hard=True)
p "Jeezus, what a tease!"
p "Now I lost an hour and this routine was not enough to build up my strength."
menu:
    "Do some further proper heavy training (+1hr)":
        jump SchoolGymWorkout    
    "Leave": 
        jump Afternoon
 

label SchoolGymChantelle04:
scene chantellegym04b
stop music
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
ch "Mmmh, this looks a bit too easy for a muscle stud like you... I'll make it a tad harder..."
scene chantellegym05b
$ renpy.pause(1.0, hard=True)
p "AAAH, need to concentrate..."
ch "ooh, I can feel something stirring underneath me, what could it be? I'd better check by rubbing my arse against it..."
window hide
$ lust_points[2] += 1
$ score += 1
show lust01:
    xalign 0.8 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01

scene chantellegym06b
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
if (strength <= 6):
    scene chantellegym06c
    play sound "Sounds/dumbbell.mp3"
    p "Shit, I dropped a dumbbell!"
    ch "Oh oh, little muscle stud can't take a bit of teasing... How disappointing..."
    ch "Well I guess you're not strong enough to impress me today... Bye bye [name]!"
    $ hour += 1
    p "Jeezus, what a tease!"
    p "Now I lost an hour and this routine was not enough to build up my strength."
    menu:
        "Do some further proper heavy training (+1hr)":
            jump SchoolGymWorkout
        "Leave":
            jump Afternoon
         
if (strength >= 7):
    ch "Wow, even with my teasing and me distracting you, you still managed to go through your routine with those massive dumbbells..."
    ch "I'm really impressed little muscle stud..."
    window hide
    $ lust_points[2] += 2
    $ score += 2
    show lust02:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    $ muscleman += 1
    p "You almost got me, and now I've got a massive tent in my strap..."
    ch "Well I'm not taking care of it here!... Not today anyway...! Bye bye [name]!"
    $ hour += 1
    p "Jeezus, what a tease!"
    p "Now I lost an hour and this routine was not enough to build up my strength."
    menu:
        "Do some further proper heavy training (+1hr)":
            jump SchoolGymWorkout
        "Leave":
            jump Afternoon
   
label SchoolGymWorkout:
play music "Sounds/workoutgroan.mp3"
$ renpy.movie_cutscene("Day2/schoolgymworkout.ogv", delay=-1, loops=-1, stop_music=False)
stop music
scene schoolgymworkout01
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
p "That was great, I can feel my muscles getting bigger and stronger already..."
window hide 
$ strength += 1
show strengthplus01:
    xalign 0.3 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(3, hard=True)
hide strengthplus01
$ hour += 1
$ workout = True
jump Afternoon
    
label SchoolGymMaddy01:
stop music
scene maddygym01 with dissolve
play music "Sounds/gymmusic02.mp3"
$ renpy.pause(1.0, hard=True)
p "Maddy is doing some gymnastics with a big ball..."
label SchoolGymMaddyChoice:
menu:
    "Do some heavy training, better equipment means I can cut on my routine time (+1hr)":
        scene
        play music "Sounds/workoutgroan.mp3"
        $ renpy.movie_cutscene("Day2/schoolgymworkout.ogv", delay=-1, loops=-1, stop_music=False)
        stop music
        scene schoolgymworkout01
        play sound "Sounds/panting.mp3"
        $ renpy.pause(2, hard=True)
        p "That was great, I can feel my muscles getting bigger and stronger already..."
        window hide
        $ strength += 1
        show strengthplus01:
            xalign 0.3 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(3, hard=True)
        hide strengthplus01
        $ hour += 1
        $ workout = True
        jump Afternoon
    "Watch her for a while" if (maddygymwatched == False):
        jump SchoolGymMaddy02

    "Interrupt her to talk to her" if (maddygymtalked == False):
        jump SchoolGymMaddy03


label SchoolGymMaddy02:
$ maddygymwatched = True
scene maddygym02 with dissolve
$ renpy.pause(2.0, hard=True)
p "I can see her cleavage when she bends over...nice..."
md "What are you looking at? Stop looking at me like that FREAK!"
jump SchoolGymMaddyChoice

label SchoolGymMaddy03:
$ maddygymtalked = True
if (maddygymwatched == True):
    scene maddygym02 with dissolve
    $ renpy.pause(2.0, hard=True)

label SchoolGymMaddy03b:
menu:
    "Hey Maddy, I've got some big balls you could play with...":
        md "That's just GROSS! Yuck! Don't talk to me anymore FREAK!"
        window hide
        $ lust_points[14] -=1
        $ score -= 1
        show lustminus01:
                xalign 0.8 yalign 0.2
                linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
        p "Gee, I really pissed her off, that line usually works a charm, I don't get it..."
        jump SchoolGymMaddyChoice
    "Hi Maddy, what are you doing exactly? I've never seen this before.":
        md "It's called a yoga ball. It helps improve strength and balance and it's great fun too!..."
        menu:
            "Oh... Can I try?":
                md "OK, I'll show you if you want, it's nice to see a boy who takes interest in this..."
                window hide
                $ lust_points[14] += 1
                $ score += 1
                show lust01:
                    xalign 0.8 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01        
                jump MaddyBalls01
            "Sounds kinda girly...":
                md "Whatever... I'm done anyway, you can do your \"manly\" things on your own now..."
                jump SchoolGymEmpty
    "What do you think about me hooking up with Frieda?":
        md "She's really busy with her studies, her parents put so much pressure on her, so I doubt she'll have time for a stupid boy like you..."
        p "Well, gee, thanks for putting it so mildly."
        jump SchoolGymMaddy03b
        
label MaddyBalls01:
scene maddygym03 with dissolve
$ renpy.pause(1.0, hard=True)
md "Here's a good exercise to stretch as many muscles as possible..."
md "Your turn..."
p "Okay, I'll try..."
scene maddygym04 with dissolve
$ renpy.pause(1.0, hard=True)
md "You're too stiff, you have to relax a bit..."
menu:
    "You bet I'm stiff, especially down there...":
        md "You're clearly not taking this seriously..."
        window hide
        $ lust_points[14] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
        jump MaddyBalls02
    "Easier said than done...":
        jump MaddyBalls02

label MaddyBalls02:
scene maddygym05 with dissolve
$ renpy.pause(1.0, hard=True)
md "How about this one then?"
menu:
    "I'm giving up, this is not for me...":
        md "Giving up that easily? Not so \"manly\" after all...(wink)..."
        p "It's too tough, I'm too muscular and not flexible enough for this kind of stuff..."
        md "Well, I'm off, I have to study a bit, I'll leave you to your \"muscular manly\" things..."
        $ hour +=1
        jump SchoolGymEmpty
    "I'll give it a try but don't make fun of me...":
        scene maddygym06 with dissolve
        $ renpy.pause(1.0, hard=True)
        md "Here, I'll help you... Not bad, you're getting the hang of it! But you're still quite...stiff..."
        p "Thanks for showing me Maddy, you're a great friend. Maybe I can show you how I train with huge barbells?"
        md "Mmmh, I was going to leave... But fine, why not..."
        
        play music "Sounds/workoutgroan.mp3"
        $ renpy.movie_cutscene("Day2/schoolgymworkout.ogv", delay=-1, loops=-1, stop_music=False)
        stop music
        scene schoolgymworkout01
        play sound "Sounds/panting.mp3"
        $ renpy.pause(2, hard=True)
        p "That was great, I can feel my muscles getting bigger and stronger already..."
        window hide
        $ strength += 1
        show strengthplus01:
            xalign 0.3 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(3, hard=True)
        hide strengthplus01
        $ hour += 1
        scene maddygym07 with dissolve
        $ renpy.pause(1.0, hard=True)
        md "I didn't realize you were so... manly..."        
        window hide
        $ lust_points[14] +=1
        $ score += 1
        show lust01:
            xalign 0.7 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01        
        md "I shouldn't have watched... It's not like me... I should leave now."        
        p "But... I didn't mind!..."
        $ workout = True
        $ muscleman += 1
        jump SchoolGymEmpty


label Burbs02:
stop music
if (hour == 7):
    $ longjog = True
    p "Time to jog back home, I think I might have missed breakfast."
    jump Breakfast02j

scene burbsday with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
if (challengercalls <= 8):
    $ lustaddedB = 3
    call Challenger from _call_Challenger_10
    $ lustaddedB = 2
    call Challenger from _call_Challenger_11
    $ lustaddedB = 1
    call Challenger from _call_Challenger_12
    $ lustaddedB = 1
    call Challenger from _call_Challenger_13
    $ challengercalls += 2

if (hour == 20):
    p "Just in time to head back home for dinner!"
    jump Dinner02
if (hour == 18 or hour == 19):
    p "I don't have time for much at this time of the day... Dinner is at 8pm."
    jump BurbsChoice02

p "The burbs are so quiet during the day. I guess everyone is at work. Except me!"

label BurbsChoice02:
if (hour == 20):
    p "Damn, it's 8pm already, I should really head back home for dinner..."
    jump Dinner02
p "What should I do?"
menu:
    "Explore the Burbs" if (discoverstore == False):
        jump BurbsExplore
    "Go to the convenience store" if (discoverstore == True) and (evictedfromstore == False):
        jump Store01
    "Go back home":
        jump Home02
    "Go to Debby's house" if (auntdebbyseen == False):
        jump AuntDebbyHouse
    "Take the bus to the beach" if (hour <= 17):
        $ busbeach = True
        jump BusDrive01
    "Take the bus heading downtown" if (hour <= 17):
        $ bustown = True
        jump BusDrive01
    "Go to the school" if (hour <= 15):
        jump Afternoon

label BurbsExplore:
scene burbsdaystore with dissolve
$ renpy.pause(1.0, hard=True)
$ hour += 1
p "Finally, after walking around for an hour, I found a sign of civilization!"
$ discoverstore = True
show addedlocation:
    xalign 0.4 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide addedlocation
jump BurbsChoice02

label BusStop01:
scene busdrive with dissolve
play sound "Sounds/busidle.mp3"
$ renpy.pause(1.0, hard=True)
p "Here it is finally..."
jump BusDrive01

label BusDrive01:
stop music
scene busdrive with dissolve
play music "Sounds/busidle.mp3"
$ renpy.pause(1.0, hard=True)
p "Here's the bus. Let's get on."

$ d2rollb=renpy.random.randint(0,1)

if (d2rollb == 0):
    jump OldWoman01
else:
    jump BusEnd

label OldWoman01:
stop music
scene oldwomanbus01 with dissolve
play music "Sounds/busdrive.mp3"
$ renpy.pause(1.0, hard=True)
ow "Well, here's a fine looking young man! Come and sit next to me boy."
menu:
    "Sit next to her":
        jump OldWoman02
    "Ignore her":
        ow "What a rude boy!"
        jump BusEnd
  
label OldWoman02:
scene oldwomanbus02 with dissolve
$ renpy.pause(1.0, hard=True)
ow "Did I tell you the story about the time I lost my cat Humphreys?"

menu:
    "I can't wait to hear it, I'm sure it's fascinating.":
        ow "Oh yes it is! You see, Humphreys normally eats his bowl of \"Crunchy Fishy Bits Deluxe\" at around 6am when I wake him up."
        ow "But the little rascal was not around and then...blah blah...blah...yadda yadda yadda..."
        jump Oldwoman03    
    "Let me guess, you lost it, and then you found it.":
        ow "Oh no, there's much more to the story young man! The little rascal was not around at 6am when I normally wake him up..."
        ow "...for his bowl of \"Crunchy Fishy Bits Deluxe\" and then yadda yadda yadda..."
        jump Oldwoman03

label Oldwoman03:
scene oldwomanbus03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oh God, she's gonna bore me to death..."
p "Wait, her wallet is right here on the side..."
menu:
    "Steal her wallet while she's rambling on":
        "You stole 20$ from a little old lady. Nice."
        $ money += 20
        jump BusEnd
    "Ask her politely where she gets off":
        ow "Oh, next stop, thank you for reminding me young man!"
        ow "You've been so kind, here is something I made at home for poor old Humphreys when he's feeling down and no female cat wants to approach him..."
        "The old woman gives you a small vial and leaves..."
        $ pheromone = True
        show pheromone
        show square
        play sound "Sounds/found.mp3"
        "You acquire a pheromone spray."
        hide square
        hide pheromone
        jump BusEnd

label BusEnd:
if (busbeach == True):
    $ hour += 1
    $ busbeach = False
    jump Beach02
elif (bustown == True):
    $ bustown = False
    $ hour += 1
    jump Downtown

label Store01:
stop music
scene store01 with dissolve
play music "Sounds/storemusic.mp3"
$ renpy.pause(1.0, hard=True)

if (storework == True) and (hour == 17):
    fa "Are you ready to start your shift today?"
    menu:
        "Yes, I'm ready.":
            jump StoreWork01
        "No, I'm too busy right now.":
            fa "Well, that's unfortunate... and rather annoying."
            window hide
            $ lust_points[7] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.3 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            jump ClerkChoiceDay02
elif (storework == True) and (hour == 18):
    fa "You're late for your shift! This is unacceptable!"
    window hide
    $ lust_points[7] -= 1
    $ score -= 1
    show lustminus01:
        xalign 0.3 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    fa "Come back tomorrow. At 5pm, not 6pm."
    $ evictedfromstore = True
    jump BurbsChoice02   
elif (hour == 19):
    fa "Welcome to \"Seven Square\", your local shop that's opened from seven till... seven."
    fa "I'm sorry, but it is seven o'clock. The second seven. So we are closing."
    fa "Please come back tomorrow to your local convenience store \"Seven Square\" between 7am and... 7pm!"
    jump Burbs02
    
else:
    fa "Welcome to \"Seven Square\", your local shop that's opened from seven till... seven."

label ClerkChoiceDay02:
scene store01 with dissolve
fa "My name is Francine, how may I help you?"
menu:
    "Chat with her":
        jump StoreChat 
    "Buy something":
        jump StoreBuy
    "Leave":
        jump Burbs02

label StoreChat:
menu:
    "I saw an ad in your window for a part-time job. Is it still available?" if (storework == False):
        scene store04
        fa "YES! Please take it, pretty please! It pays 5 dollars an hour and I only need you to work two-hour long shifts from 5pm till 7pm any day you choose."
        menu:
            "Mmh, that's not a lot. If you're so desperate, why don't you pay more?":
                fa "We can't afford it... But I'll make you a sweet deal. At the end of your two-hour shift, you can buy any item half price!"
                p "Interesting... And what items do you have for sale here?"
                scene store05
                fa "A fantastic assortment of various items that you can see displayed on your screen as I speak with their regular prices indicated."
                show storeitems
                menu:
                    "Na, still not worth it, sorry, I'm not interested.":
                        jump StoreNoDeal
                    "It's a deal!":
                        $ halfprice = True
                        jump StoreDeal
            "It's a deal!":
                jump StoreDeal
    "I have an inconvenience down my pants. Since this is a convenience store...":
        scene store03
        fa "I can barely contain my laughter."
        jump ClerkChoiceDay02
    
label StoreDeal:
scene store04 with dissolve
$ storework = True
fa "Oh, thank you so much! I'll see you at 5pm then... Today or some other day..."
window hide
$ lust_points[7] += 1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
if (hour == 18):
    fa "It's 6pm, so it's too late for you to start working today. Did you maybe want to buy anything?"
    menu:
        "Sure.":
            jump StoreBuy
        "No thanks.":
            fa "Alright, see you another day then."
            jump Burbs02
jump ClerkChoiceDay02


label StoreWork01:
fa "Alright! Let's start working for a meagre pay for our parent company \"Seven Square\"! Yippee!"
fa "I presume you speak French?"
p "What? Err... Oo-ne petite pew."
fa "Ah, you suck I see. We have to cater to the local community too, so you'll work in the storage room and filling up the shelves then."
fa "You seem like you have the muscles for such a job anyway..."
p "You bet! I'm like, super-strong!"
fa "Oh, really? Well, that's great because I've been having some back problems. My doctor can't figure out why..."
window hide
$ lust_points[7] += 1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
fa "Follow me, I'll show you the warehouse."
scene store06 with dissolve
$ renpy.pause(1.0, hard=True)
p "Wow, she's got such a tight waist and arse, and yet such huge boobies..."
stop music
scene store07 with dissolve
$ renpy.pause(1.0, hard=True)
fa "As you can see, it's rather a mess right now. So you'll have to clean it before working the shelves."
fa "I need to stack up some beers, people are ssoo thirsty on this island."
fa "I'll take the ladder and pass the boxes down to you, okay?"
scene storage with dissolve
$ renpy.pause(1.0, hard=True)
p "(Somehow, walking up a ladder in flip-flops sounds like a terrible idea...)"
fa "Almost there, they're right at the top for some reason..."
scene storagefall with dissolve
$ renpy.pause(1.0, hard=True)
fa "AH, I slipped!"
menu:
    "Catch Francine":
        jump CatchFrancine
    "Catch the beer":
        jump CatchBeer

label CatchFrancine:
scene storagecatchfrancine with dissolve
$ catchfrancine = True
$ renpy.pause(1.0, hard=True)
fa "Oh, thanks for catching me [name], I would have really hurt myself without your intervention!"
window hide
$ lust_points[7] += 2
$ score += 2
show lust02:
    xalign 0.75 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
fa "Unfortunately, the beer bottles broke in their fall. This will have to be taken out of our salaries..."
p "What? I saved you, this is not fair!"
fa "Seven Square policies.... Any breakage cost is shared by all employees... Except if you manage to find a way to replace them, I'm afraid I'll have to pay you only 5$ today..."
p "This job sucks! I'll find some beers to replace these, I don't want to lose 5 bucks."
fa "In the meantime, clean the storage room and then go and pack some shelves. I'll see you at 7pm."
scene storageclean with dissolve
$ renpy.pause(1.0, hard=True)
p "This job sucks! This job sucks!"
$ hour += 1
p "I'm done here, I should move into the store to pack the shelves..."
jump StoreTeagan01

label CatchBeer:
scene storagecatchbeer with dissolve
$ renpy.pause(1.0, hard=True)
$ catchbeer = True
fa "Ouch! I think I hurt myself badly in my fall... You could have tried to catch me instead of the beer!"
p "Beer is important, you said it yourself, people are really thirsty on this island!"
fa "I guess you're right, we should protect Seven Square products at all costs, that's the company's policy..."
fa "Hand me the beer boxes, I'll go and place them in the fridges. In the meantime, clean the storage room and then go and pack some shelves. I'll see you at 7pm."
scene storageclean with dissolve
$ renpy.pause(1.0, hard=True)
p "This job sucks! This job sucks!"
$ hour += 1
p "I'm done here, I should move into the store to pack the shelves..."
jump StoreTeagan01

label StoreTeagan01:
play music "Sounds/storemusic.mp3"
scene storeteagan01 with dissolve
$ renpy.pause(1.0, hard=True)
p "There's Miss Cocque doing her shopping, she hasn't noticed me yet."
menu:
    "Hide and hope she doesn't see you":
        jump StoreHide
    "Greet her and ask her if you can help with anything":
        jump StoreTeagan02

label StoreHide:
scene storeteaganhide with dissolve
$ renpy.pause(1.0, hard=True)
p "Phew, she almost saw me but I'm think I managed to avoid her... And she's on her way out."
p "At the same time, watching that arse... Maybe I should have greeted her..."
p "Oh well, only a few more minutes of hard labour and my shift ends. I'll just stack these bubble gums once she's out of the store."
jump StoreShiftEnd

label StoreTeagan02:
scene storeteagan02 with dissolve
$ renpy.pause(1.0, hard=True)
t "Oh, hello [name], I didn't know you worked here. It's good to see you don't shy away from hard work."
p "Well, I need a bit of pocket money and I'm strong enough to do that kind of job."
scene storeteagan06 with dissolve
$ renpy.pause(1.0, hard=True)
t "Yes, I can see that... Your outfit barely contains your bulging muscles..."
window hide
$ lust_points[22] += 1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
scene storeteagan03 with dissolve
$ renpy.pause(1.0, hard=True)
t "Well, I need to stock up on water bottles, and they are quite heavy, care to help young man?"
menu:
    "My manager told me to pack up the shelves, so I don't have time, sorry...":
        scene storeteagan04 with dissolve
        t "Fine, I understand... Seven Square is well known for its abysmal service anyway..."
        scene storeteagan05 with dissolve
        $ renpy.pause(1.0, hard=True)
        fa "What do I hear? [name], when a customer asks for your help, you MUST oblige! I'm sorry Ms Cocque, I will severely reprimand this new...employee."
        if (detention == True):
            t "Please don't, the poor boy already had detention today, it's my fault, I'm just in a foul mood today."            
        if (detention == False):
            p "Hey, I just did what you asked me to do, that's not fair!"
            fa "\"It's not fair, it's not fair\", That's all I hear you say since you arrived. Just help Ms Cocque and stop arguing with me!"
            window hide
            $ lust_points[7] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.1 yalign 0.3
                linear 1.0 yalign 0.5
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            jump StorePark
    "Sure Miss Cocque, let me help you with these heavy items, it'll be easy for me!":
        jump StoreTeagan05

label StoreTeagan05:
scene storeteagan03 with dissolve
t "Well, thanks [name], it's so much faster when a strong boy helps me carry all this..."
window hide
$ lust_points[22] += 1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
t "Please take two packs and follow me to my car outside..."
label StorePark:
stop music
play music "Sounds/gardensound.mp3"
scene storepark01 with dissolve
$ renpy.pause(1.0, hard=True)
t "My car is right over there. I'll open the trunk..."
scene storepark02 with dissolve
$ renpy.pause(1.0, hard=True)
p "(Wow, what a nice arse teach has!)"
t "There, all set. And now for your little reward..."
scene storepark03 with dissolve
$ renpy.pause(1.0, hard=True)
t "Here, five bucks for helping me carry those heavy grocery items."
$ money += 5
t "Maybe you can become my assigned grocery delivery boy and bring me home some orders I place online..."
menu:
    "Sure Miss Cocque!":
        t "Ooh, I have a new delivery boy... A really STRONG one too!"
        window hide
        $ lust_points[22] += 1
        $ score += 1
        show lust01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        t "Great, I'll let the store manager know... Have a nice evening [name], I'll see you tomorrow at class, 9am sharp!"
        window hide
        $ deliveryboy = True
        $ discoverteagan = True
        show addedlocation:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide addedlocation
        jump StoreShiftEnd
    "I don't know, I don't think I'll have time for that extra job...":
        t "Uh... OK, just think about it... Have a nice evening [name], I'll see you tomorrow at class, 9am sharp!"
        jump StoreShiftEnd

label StoreShiftEnd:
stop music
scene store01 with dissolve
$ hour += 1
$ renpy.pause(1.0, hard=True)
p "That's it, it's the end of my shift..."
fa "Yes, I am aware of that, it's 7pm, and therefore  \"Seven Square\" is now closed..."
if (catchbeer == True):
    fa "Here's ten dollars for your hard work [name]! I hope you come back again to work here. Goodbye."
    $ money += 10
    p "Yeah, maybe, I'll see..."
    jump StoreShiftEnd02
if (catchfrancine == True):
    fa "Here's five dollars for your hard work [name]! I hope you come back again to work here. Goodbye."
    $ money += 5
    p "Yeah, maybe, I'll see..."
    jump StoreShiftEnd02
    
label StoreShiftEnd02:
if (halfprice == True):
    p "Hey, I can buy something half-price remember?"
    fa "Ah yes, silly me for not remembering..."
    jump HalfPrice

label HalfPrice:
fa "So, what would you like to buy?"  
menu:
    "Buy wristband (2$) " if (money >= 2) and (wristband == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "I wonder who that is for, it's such a cheap gift..."        
        $ money -= 2
        $ wristband = True
        show wristband
        show square
        play sound "Sounds/found.mp3"
        "You acquired a glitzy wristband."
        hide square
        hide wristband
        jump StoreShiftEnd03
        
    "Buy mega-sized condoms (3$) " if (money >= 3) and (condoms == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "Wow, these condoms are for... really HUNG guys!"        
        window hide
        $ lust_points[7] += 1
        $ score += 1
        show lust01:
            xalign 0.35 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01                
        $ money -= 3
        $ condoms = True
        show megacondoms
        show square
        play sound "Sounds/found.mp3"
        "You acquired some mega-condoms."
        hide square
        hide megacondoms
        jump StoreShiftEnd03

    "Buy lubricant (4$) " if (money >= 4) and (wd69 == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "Great buy! This lubricant is so strong you can surf on it."        
        $ money -= 4
        $ wd69 = True
        show wd69
        show square
        play sound "Sounds/found.mp3"
        "You acquired some lubricant."
        hide square
        hide wd69
        jump StoreShiftEnd03

    "Buy energy drink (+2 stamina) (5$) " if (money >= 5) and (whitebull == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "Excellent choice! With that much energy, you could replace two coal-powered plants!"        
        $ money -= 5
        $ whitebull = True
        show whitebull
        show square
        play sound "Sounds/found.mp3"
        "You acquired an energy drink."
        hide square
        hide whitebull
        jump StoreShiftEnd03
    
    "Buy army knife (10$) " if (money >= 10) and (knife == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "It's Japanese, just like a mini samurai sword."        
        $ money -= 10
        $ knife = True
        show knife
        show square
        play sound "Sounds/found.mp3"
        "You acquired an army knife."
        hide square
        hide knife
        jump StoreShiftEnd03

    "Buy KokDik camera (40$) " if (money >= 40) and (camera == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "You want to become a paparazzi? This is the best camera on the market!"        
        $ money -= 40
        $ camera = True
        show camera
        show square
        play sound "Sounds/found.mp3"
        "You acquired a digital camera."
        hide square
        hide camera
        jump StoreShiftEnd03
    
    "Nothing actually...":
        jump StoreShiftEnd03
        
label StoreShiftEnd03:
scene store01 with dissolve
fa "That's it, you bought your item, now I have to close the store... Come back anytime to \"Seven Square\", your local shop that's opened from seven till... seven."
jump Burbs02
    
label StoreNoDeal:
scene store03 with dissolve
fa "That's a pity... Think about it, the job offer will be on all week."
jump ClerkChoiceDay02

label StoreBuy:
scene store01
menu:
    "Buy wristband (4$) " if (money >= 4) and (wristband == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "I wonder who that is for, it's such a cheap gift..."        
        $ money -= 4
        $ wristband = True
        show wristband
        show square
        play sound "Sounds/found.mp3"
        "You acquired a glitzy wristband."
        hide square
        hide wristband
        jump ClerkChoiceDay02

    "Buy mega-sized condoms (6$) " if (money >= 6) and (condoms == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "Wow, these condoms are for... really HUNG guys!"        
        window hide
        $ lust_points[7] += 1
        $ score += 1
        show lust01:
            xalign 0.35 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01                
        $ money -= 6
        $ condoms = True
        show megacondoms
        show square
        play sound "Sounds/found.mp3"
        "You acquired some mega-condoms."
        hide square
        hide megacondoms
        jump ClerkChoiceDay02

    "Buy lubricant (8$) " if (money >= 8) and (wd69 == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "Great buy! This lubricant is so strong you can surf on it."        
        $ money -= 8
        $ wd69 = True
        show wd69
        show square
        play sound "Sounds/found.mp3"
        "You acquired some lubricant."
        hide square
        hide wd69
        jump ClerkChoiceDay02

    "Buy energy drink (+2 stamina) (10$) " if (money >= 10) and (whitebull == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "Excellent choice! With that much energy, you could replace two coal-powered plants!"        
        $ money -= 10
        $ whitebull = True
        show whitebull
        show square
        play sound "Sounds/found.mp3"
        "You acquired an energy drink."
        hide square
        hide whitebull
        jump ClerkChoiceDay02
    
    "Buy army knife (20$) " if (money >= 20) and (knife == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "It's Japanese, just like a mini samurai sword."        
        $ money -= 20
        $ knife = True
        show knife
        show square
        play sound "Sounds/found.mp3"
        "You acquired an army knife."
        hide square
        hide knife
        jump ClerkChoiceDay02

    "Buy KokDik camera (80$) " if (money >= 80) and (camera == False):
        scene store02
        play sound "Sounds/cashregister.wav"
        fa "You want to become a paparazzi? This is the best camera on the market!"        
        $ money -= 80
        $ camera = True
        show camera
        show square
        play sound "Sounds/found.mp3"
        "You acquired a digital camera."
        hide square
        hide camera
        jump ClerkChoiceDay02
    "Nothing actually...":
        jump ClerkChoiceDay02

label AuntDebbyHouse:
stop music
scene debbyentrance with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/debbydoorbell.mp3"
p "Maybe I could ask Debby if I could wash her car for her and get a bit of money..."
if (hour >=18):
    scene debbyhouse01
    d "Well, look who came to visit me. What brings you here [name]?"
    $ auntdebbyseen = True
    jump AuntDebbyHouseMenu
if (hour <=17):
    p "She doesn't seem to be in at the moment."
    jump Burbs02

label AuntDebbyHouseMenu:
menu:
    "I wanted to see you model some more bikinis for me." if (debbybikini == False):
        d "Well, that's bold of you young man!"
        d "But you're in luck, I just received a new swimsuit which I haven't tested yet... Come on in..."
        $ debbybikini = True
        jump AuntDebbyInside
    "I was wondering if your car needed washing?" if (debbycarwashed == False) or (debbycarunwashed == False):
        d "Oh, I see, you want to make a bit of money do ya? Fair enough."
        d "I'll give you five dollars... But I want to be able to watch and you have to be bare-chested...(wink)"
        menu:
            "It's a deal!":
                jump AuntCarWash
            "Five dollars? It will take me at least one hour to wash it... Not interested.":
                d "Your choice mr I'm-too-important-to-wash-a-car-for-five-dollars!..."
                d "Anything else?"
                jump AuntDebbyHouseMenu
    "Nancy needs some...sugar." if (debbysugar == False):
        d "Oh, alright, come on in then."
        $ debbysugar = True
        jump AuntDebbyInside

label AuntDebbyNewBikini:
d "Where should I model this new bikini for you?"
menu:
    "Why not in your bedroom?":
        d "No, that's my special place. You can't go there ever, you hear me?"
        p "Alright, alright. How about the backyard then?"
        d "Yes, that will do, go and sit outside and wait for me, I'll be back in a minute."
        d "Get down to your underwear, I might need you... to do something for me."
        p "(Well, that's an unusual request... I hope it leads to something...)"
        jump DebbyHouseBikini01
    "The outside light will better reveal every detail of your hot bo...swimsuit.":
        d "Yes, you're right, you are a fine connoisseur. Go and sit outside then, I'll be back in a sec." 
        d "Get down to your underwear, I might need you... to do something for me."
        p "(Well, that's an unusual request... I hope it leads to something...)"
        jump DebbyHouseBikini01

label AuntCarWash:
scene debbycar01 with dissolve
$ renpy.pause(1.0, hard=True)
d "There it is, it's a bit dirty, I took it for a ride this weekend up the mountains... There's a bucket, a sponge and some soap for you."
d "Don't forget to take your top off, I want to see those muscles working hard to prove you're doing a good job!"
scene debbycar02 with dissolve    
play sound "Sounds/bucket.mp3"
$ renpy.pause(1.0, hard=True)
p "She's watching me like I'm some piece of meat... Which is pretty much what I am actually."
d "Keep going, I want the car to be spotless."
play sound "Sounds/auntphone.mp3"
scene debbycar03 with dissolve
$ renpy.pause(1.0, hard=True)
p "This is boring... And now she's on the phone and ignoring me..."
scene debbycar04 with dissolve
$ renpy.pause(1.0, hard=True)
d "Oh, I need to go... Just finish and take your five dollars from the side table in the living room, OK sweetie?"
p "She seems to be in a hurry all of a sudden..."
scene debbycar05 with dissolve
$ renpy.pause(1.0, hard=True)
p "Well that's just fucking great. First she wants to see me bare-chested and now she buggers off..."
menu:
    "Finish washing the car (+1 hr)":
        $ hour += 1
        $ debbycarwashed = True
        if (hour == 20):
            p "Shit, it's 8pm, I'd better quickly take the money and head back home for dinner or I'll be late!"
            $ money += 5
            jump Dinner02
        jump AuntDebbyMoney
    "Stop and sneak inside to get the money anyway":
        $ debbycarunwashed = True
        jump AuntDebbyMoney
    
label AuntDebbyInside:
scene debbyhouse02 with dissolve    
$ renpy.pause(1.0, hard=True)
play sound "Sounds/footsteps.mp3"
d "This way to the living room..."
p "Wow, Debby has such a huge house... And such a tight ass..."
jump AuntDebbyLivingRoom

label AuntDebbyLivingRoom:
scene debbyhouse03 with dissolve    
$ renpy.pause(1.0, hard=True)
if (debbysugar == True):
    d "I'll go and fetch some sugar from the kitchen. You can wait for me here. But don't touch anything, these sculptures are worth thousands of dollars!"
    p "Sure Debby. I won't move."
    play sound "Sounds/debbydooropenclose.mp3"
    jump DebbySnoop
if (debbybikini == True):
    jump AuntDebbyNewBikini
    
label DebbySnoop:
scene debbysnooping with dissolve    
$ renpy.pause(1.0, hard=True)
menu:
    "Snoop around":
        jump DebbySnooping
    "Wait patiently for Debby to return":
        jump DebbySugar

label DebbySnooping:
play music "Sounds/snooping.mp3"
$ d2rolldebby=renpy.random.randint(0, 1)
if (d2rolldebby == 0):
    call screen debbysnoop01
if (d2rolldebby == 1):
    call screen debbysnoop02
$ renpy.pause(1.0, hard=True)
stop music
"You were too slow and didn't find anything. Debby is coming back..."
jump DebbySugar

label FoundAudaciousPass:
scene debbysnooping
$ renpy.pause(1.0, hard=True)
stop music
show audaciouspass
show square
play sound "Sounds/found.mp3"
"You found a visitor's pass to Audacious Headquarters."
$ audaciouspass = True
hide square
hide audaciouspass

label DebbySugar:
scene debbyhouse04 with dissolve    
$ renpy.pause(1.0, hard=True)
d "Here you are. I hope Nancy does some nice cakes with it! Tell her to invite me when she's done."
p "Thanks Debby... I'll be sure to let her know..."
$ hour += 1
jump Burbs02
    
label DebbyHouseBikini01:
stop music
play music "Sounds/gardensound.mp3"
scene debbyhousebikini01 with dissolve    
$ renpy.pause(1.0, hard=True)
d "I'm thinking of calling this one \"Stud Tamer\". What do you think?"
p "Wow, Debby, it's really slu... I mean classy."
scene debbyhousebikini02 with dissolve    
$ renpy.pause(1.0, hard=True)
d "You need to see the back too. Does it fit well?"
p "Gggg.. Yeah, it hugs your curves perfectly fine..."
scene debbyhousebikini03 with dissolve    
$ renpy.pause(1.0, hard=True)
d "If you look closely, you will notice that it has a \"torn\" look to it, see?"
p "Oh yeah, I hadn't noticed at all..."
d "Now stand up, time for you to be useful..."
p "Erm... But... I can't really... I have a cramp between my legs suddenly..."
d "Is that what you call it? Never mind that hardening great big cock of yours, I need you to be in the picture for a poster campaign..."
p "Ah? Well, if you insist..."
scene debbyhousebikini04 with dissolve    
$ renpy.pause(1.0, hard=True)
d "Let's move over there, there's a camera set up in the wall and I can trigger it with my voice..."
p "That's high tech. But aren't you worried about this being a bit too... saucy for a poster?"
d "I want to call it \"Stud Tamer\" and... well, you'll do just fine as the \"stud\" aspect of it..."
scene debbyhousebikini05 with dissolve    
$ renpy.pause(1.0, hard=True)
p "I could like, flex my muscles for you if you want and you feel them up and pretend you're really impressed, that would be a cool photo, no?"
d "Oh [name], you sure have HUGE muscles everywhere, I wouldn't be pretending..."
window hide
$ lust_points[5] +=2
$ score += 2
show lust02:
    xalign 0.15 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
d "But that's not what I had in mind my \"stud\"... It's called \"Stud Tamer\", remember?"
scene debbyhousebikini06 with dissolve    
$ renpy.pause(1.0, hard=True)
p "Ah, I see, THAT's what you had in mind... I don't really want my friends at school to see me like that Debby, this is kinda humiliating..."
d "Don't worry, we'll cover your eyes with a black strip. This billboard campaign will have women screaming for this new model!"
p "Can't I get paid or something like normal models?"
d "Alright, I suppose I could give you ten dollars for your \"work\". But don't tell Nancy about this, it's between you and me alright?"
p "I sure hope it stays between you and me, I don't want the rest of the world to see me being tamed like I'm some kind of wild animal..."
$ money += 10
d "Now off you go, it's getting late... (wink)."
$ hour +=1
stop music
jump Burbs02

label AuntDebbyMoney:
stop music
scene debbymoney with dissolve    
$ renpy.pause(1.0, hard=True)
p "Here's the money."
play sound "Sounds/auntviolent.mp3"
p "What's that sound? It seems to be coming from upstairs where Debby's bedroom is..."
menu:
    "Go investigate":
        jump AuntDebbyStairs
    "Take the money and leave":
        $ money += 5
        jump Burbs02

label AuntDebbyStairs:
scene debbystairway with dissolve
play sound "Sounds/auntwhip01.mp3"
$ renpy.pause(1.0, hard=True)
p "Jeezus, this sounds violent, I'd better hurry up!"

label AuntDebbyBedroom:
scene debbybedroom01 with dissolve    
play sound "Sounds/auntwhip02.mp3"
$ renpy.pause(1.0, hard=True)
p "WTF? That masked naked guy is brutalizing Debby!"
menu:
    "Leave quietly and take the money on the way out":
        $ money += 5 
        jump Burbs02
    "Get involved":
        p "Hey you, stop this immediately or...I swear I'll beat you up!"
        jump AuntDebbyBondage01

label AuntDebbyBondage01:
scene debbybedroom02 with dissolve
$ renpy.pause(1.0, hard=True)
gi "Oh, shit, who's this boy... I'm outta here!"
scene debbybedroom03 with dissolve    
$ renpy.pause(1.0, hard=True)
"The masked man flees by the window..."
d "Mmmm....Phmmm..."
p "I'll chase after him Debby, don't worry!"
scene debbybedroom04 with dissolve
$ renpy.pause(1.0, hard=True)
d "Oh..[name].... I am so ashamed you had to see that...It wasn't...what it seemed..."
p "But...What do you mean?"
scene debbybedroom05 with dissolve
$ renpy.pause(1.0, hard=True)
d "I...I hired this guy to do that to me...I'm a sick person...I'm sorry..."
d "Please don't tell Nancy or anybody. I'll give you twenty dollars if you promise me to keep quiet."
menu:
    "So you're into bondage then? I like that...I like that a lot....":
        d "What? No, I'm not interested in doing such a vile thing with you and corrupting your fragile young mind...."
        d "You need to leave now...Take your carwash money and go."
        p "Hey! But..."
        d "Just GO!"
        $ money += 5
        jump Burbs02
    "You deserve a good cock slapping, get on your knees bitch!":
        d "Wh...what?..But..."
        p "You heard me. Remove your mask and ON YOUR KNEES BITCH!"
        d "Y..yes master..."        
        jump DebbyCockSlap
    "OK, I didn't see a thing. I won't say a word. I'll just erase everything from my memory.":
        d "Oh Thank you [name], I owe you big time. Here's your twenty bucks. Now get out of here and don't say a word to anyone!"
        $ money += 20
        jump Burbs02

label DebbyCockSlap:
scene debbycockslap01 with dissolve    
$ renpy.pause(1.0, hard=True)
p "Ready slave?"
d "Yes... Slap my filthy face with your massive dong master... I'm not worthy of it..."
scene debbycockslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene debbycockslap01  
$ renpy.pause(0.5, hard=True)
scene debbycockslap02 
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene debbycockslap01   
$ renpy.pause(0.5, hard=True)
scene debbycockslap02 
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene debbycockslap01 
$ renpy.pause(0.5, hard=True)
scene debbycockslap02 
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene debbycockslap01 
$ renpy.pause(0.5, hard=True)
scene debbycockslap02 
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene debbycockslap01 
$ renpy.pause(0.5, hard=True)
$ lust_points[5] +=1
$ score += 1
show lust01:
    xalign 0.6 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
p "You liked that didn't you Debby?"
d "Yes... But don't call me Debby... Call me \"filthy slut\"... That's what I am..."
menu:
    "Now time for you to suck my cock filthy slut!":
        d "What?... No! This is going too far... [name]... We had our fun... Let's leave it at that."
        p "Ah, uh, OK... sorry, I thought you were willing..."
        d "Did you see any \"Epic Lust\" icon appear over my head? No. So please put your... thingie back in your pants and leave..."
        d "Here's 10 dollars, don't say a word to Nancy and we might do something like that again (wink...)."
        p "F...fuck! I'm so hard and I can't even cum!"
        if (debbycarunwashed == True):
            $ hour +=1
        jump Burbs02
    "Now I'm gonna cock-slap that tight arse of yours filthy slut!":
        d "Oooh, yes master, I deserve it..."
        jump ArseCockSlap

label ArseCockSlap:
scene debbyarseslap01 with dissolve    
$ renpy.pause(1.0, hard=True)
p "Ready slave?"
d "Yes... Slap my slutty arse with your massive dong master... I'm not worthy of it..."
scene debbyarseslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene debbyarseslap01
$ renpy.pause(0.5, hard=True)
scene debbyarseslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene debbyarseslap01
$ renpy.pause(0.5, hard=True)
scene debbyarseslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene debbyarseslap01
$ renpy.pause(0.5, hard=True)
scene debbyarseslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene debbyarseslap01
$ renpy.pause(0.5, hard=True)
scene debbyarseslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene debbyarseslap01
$ renpy.pause(0.5, hard=True)
$ lust_points[5] +=2
$ score += 2
show lust02:
    xalign 0.6 yalign 0.5
    linear 1.0 yalign 0.3
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
d "It's enough for now [name], here's 10 dollars, don't say a word to Nancy and we might do something like that again (wink...)."
menu:
    "Sure, nice doing business with you Debby...":
        $ money += 10
        d "I feel so...cheap...so dirty...I love it, thank you [name]...Just go now..."
        p "I feel like...10 dollars worth apparently. See you another time Debby!"
        if (debbycarunwashed == True):
            $ hour +=1
        jump Burbs02
    "We ain't finished yet whore! Get back up on your knees and hop on the bed, I'm gonna stretch that pussy wide...":
        d "What?... No! This is going too far... [name]... We had our fun... Let's leave it at that."
        p "Ah, uh, OK... sorry, I thought you were willing..."
        d "Did you see any \"Epic Lust\" icon appear over my head? No. So please put your... thingie back in your pants and leave..."
        window hide
        $ lust_points[5] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.6 yalign 0.3
            linear 1.0 yalign 0.5
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        p "F...fuck! I'm so hard and I can't even cum!"
        if (debbycarunwashed == True):
            $ hour +=1
        jump Burbs02


label Downtown:
stop music
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"
$ renpy.pause(1.0, hard=True)
p "The bus left me right in front of the main downtown plaza."

if (hour >= 19):
    p "It's getting late, I should really take the bus and get home now."
    jump BusDowntownHome
else:
    jump DowntownChoiceb

label BusDowntownHome:
p "Ah, here's the bus heading to the Burbs, I'd better take it..."
$ hour += 1
jump Burbs02

label DowntownChoiceb:
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_14
    $ lustaddedB = 3
    call Challenger from _call_Challenger_15
    $ lustaddedB = 1
    call Challenger from _call_Challenger_16
    $ lustaddedB = 1
    call Challenger from _call_Challenger_17
    $ challengercalls += 2

if (hour >= 19):
    p "It's getting late, I should really take the bus and get home now."
    jump BusDowntownHome

p "Where should I go?"
menu:
    "Go to Audacious HQ" if (discoveraudacious == True):
        jump AudaciousHQ
    "Go shopping":
        jump Shop
    "Go to the massage parlour" if (discovermassage == True):
        jump Parlour01
    "Take the bus home":
        jump BusDowntownHome
    "Take the bus to the beach" if (hour <= 17):
        jump BusDowntownBeach

label BusDowntownBeach:
p "Ah, here's the bus heading for the beach, I'd better take it..."
$ hour += 1
jump Beach02

label AudaciousHQ:
scene downtownaudacious with dissolve
$ renpy.pause(1.0, hard=True)
p "Wow, this is where Nancy and Debby work? This building looks HUGE."

scene audaciousentrance with dissolve
$ renpy.pause(1.0, hard=True)
if (audacioustried == False):
    p "Here's the main entrance. I have to find a way to get in..."
    show security01
    se "Who dares trespass?"
    menu:
        "I work here, I'm a photographer. Here's my pass." if (audaciouspass == True):
            $ audacioustried = True
            hide security01
            show security01b
            se "Hmm, this pass looks fake. It says at the back \"Printed on the Cheat Console\" What does that mean?"
            p "What? Oh no, nothing, that's just a joke..."
            hide security01b
            show security02
            se "I don't think it's a joke. I think cheating is a serious offence. Bye bye cheat..."
            return

        "Let me through, my landlady's sister is the CEO of this company.":
            hide security01
            show security02
            se "And I'm the pope's daughter. Get out of here kid."
            $ audacioustried = True
            jump DowntownChoiceb

        "Out of my way oaf! I'm DA MAN! I will trample you!":
            if (strength >= 10):
                se "Normally, with your strength you would beat me and get inside this building. But you cheated with the console..."
                se "Bye bye cheat..."
                return
            if (strength <=9):
                hide security01
                show security03
                se "We'll see about that!"
                play sound "Sounds/punch.mp3"
                $ renpy.pause(1, hard=True)
                scene audaciousbeaten with dissolve
                $ renpy.pause(1.0, hard=True)
                play sound "Sounds/outofbreath.mp3"
                window hide
                $ stamina -=1
                show staminaminus01:
                    xalign 0.2 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/panting.mp3"
                $ renpy.pause(2, hard=True)
                hide staminaminus01
                p "The security guard beat the crap out of me. I'd better get stronger if I want to force my way into this building next time..."
                jump DowntownChoiceb

if (audacioustried == True):
    p "I already tried getting into this building today. And I failed miserably. I should probably leave."
    jump DowntownChoiceb
    
label AudaciousNO:
scene downtownaudacious with dissolve
$ renpy.pause(1.0, hard=True)
p "Looks like I can't get in today..."
jump DowntownChoiceb

label Shop:
if (evictedfromshop == True):
    "You are banned from entering this boutique until tomorrow. Bad boy. VERY bad boy."
    jump DowntownChoiceb
if (shoppingseen == True):
    "You already went shopping today. Looks like you might be a shopaholic..."
    jump DowntownChoiceb
else:
    stop music
    scene shop with dissolve
    play music "Sounds/shopmusic.mp3"
    $ renpy.pause(1.0, hard=True)
    p "This boutique looks very expensive..."
    p "There's a nice-looking clerk standing behind the counter and one customer looking at a skimpy swimsuit..."
    jump Shop01b

label Shop01:
$ shoppingseen = True
scene shop with dissolve
$ renpy.pause(1.0, hard=True)

label Shop01b:
menu:
    "Go talk to the clerk":
        jump ShopClerk
    "Go talk to the customer":
        jump ShopCustomer
    "Leave":
        stop music
        jump DowntownChoiceb

label ShopClerk:
scene shop01 with dissolve
sc "How may I help you?"
menu:
    "Talk to her":
        jump ShopTalk
    "Buy something":
        jump ShopBuy    
    "Leave the counter":
        jump Shop01

label ShopTalk:
 menu:
    "You know what would look good on you? Me.":
        scene shop03
        sc "Mmh, lemme think... Yes, it's the worse pick-up line ever."
        jump ShopClerk
    "What's the word on the street downtown?":
        if (downtowntipgiven == True):
            sc "I already gave you a tip today. Stop pestering me."
            jump ShopClerk
        scene shop03
        if (downtowntips == 0):
            sc "There's a new Chinese massage parlour that just opened up."
            sc "I hear you can get a FULL body massage, if you see what I mean (wink)!"
            window hide
            $ discovermassage = True
            show addedlocation:
                xalign 0.7 yalign 0.3
                linear 1.0 yalign 0.1
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide addedlocation
            $ downtowntips += 1
            $ downtowntipgiven = True
            jump ShopClerk

label ShopBuy:
menu:
    "Buy swimsuit for customer (40$ - pay 20$ from your own pocket)" if (money >= 20) and(seenhallebikini == True) and (boughthallebikini == False):
        scene shop02
        play sound "Sounds/cashregister.wav"
        sc "Here you are. That's for one lucky girl!"        
        $ money -= 20
        $ boughthallebikini = True
        jump HalleGift

    "Buy black tanktop (10$)" if (money >= 10) and (tanktop == False): 
        scene shop02
        play sound "Sounds/cashregister.wav"
        sc "You'll look different in this tank top... Like darker..."
        $ money -= 10
        $ tanktop = True
        show tanktop
        show square
        play sound "Sounds/found.mp3"
        "You purchased a black tanktop."
        hide tanktop
        hide square
        jump ShopClerk
    "Nothing actually":
        jump ShopClerk

    "I don't have enough money to buy anything here." if (money <=9):
        sc "We don't do credit. We don't trust poor people like you."
        p "I feel like... dirt..."
        jump ShopClerk

label ShopCustomer:
scene halleshop01 with dissolve
$ renpy.pause(1.0, hard=True)
if (boughthallebikini == True) and (seenhallebikini == True):
    p "Hey, Halle, why are you still here? I bought you this swimsuit already!"
    show halleshop01b
    ha "Yeah, I know, but the dev is too lazy to remove me from this image..."
    ha "Remember, I'm ACTUALLY at the beach."
    jump Shop01
elif (boughthallebikini == False) and (seenhallebikini == True):
    p "You're still staring at this swimsuit..."
    show halleshop01b
    ha "And I'll keep staring at it until you chip in 20 bucks to buy it for me!"
    jump Shop01

else:
    menu:
        "May I help you with anything miss? Would you like to try this item in one of our cabins?":
            show halleshop01b
            ha "Oh...hum.. Sorry, I didn't realize you worked here... Well, I don't know, it's quite expensive..."
            p "Well, try it on, that's free anyway..."
            ha "Yeah, I guess you're right, I might as well try it on..."
            $ pretendshop = True
            jump HalleChange
        "Hello there, wow, this swimsuit would look great on you I'm sure!":
            show halleshop01b
            ha "Oh...hi.. I don't have enough money to buy it unfortunately. I'm 20 dollars short..."
            menu:
                "Tell you what, I'll pay the difference if you try it on for me.":
                    ha "Really, you would do that? Em... OK, I'll try it on then."
                    window hide
                    $ lust_points[9] += 1
                    $ score += 1
                    show lust01:
                        xalign 0.75 yalign 0.4
                        linear 1.0 yalign 0.2
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lust01
                    jump HalleChange
                "That's too bad, cos I'm sure you would be a hit with that thing on...":
                    ha "(sigh)... Yes, it's too bad..."
                    jump Shop01

label HalleChange:
scene hallechange with dissolve
$ renpy.pause(1.0, hard=True)
p "Mmh, she's conveniently left the door slightly ajar..."
if (pretendshop == True):
    menu:
        "Do you need help in there miss? I can adjust the fit if you like...":
            ha "What? But...I'm still naked!"
            p "Well, I'm the only employee here so..."
            sc "What did I hear? Who are you pretending to be you pervert?"
            p "Sssh, she's falling for it, I'll give you 5 bucks to shut your mouth!"
            sc "This is a respectable establishment. I must ask you to leave at once!"
            $ evictedfromshop = True
            jump DowntownChoiceb
        "Wait for her to come out":
            jump HalleBikini01
else:
    ha "Hang on a minute, I'm almost ready..."

label HalleBikini01:
scene hallebikini01 with dissolve
$ renpy.pause(1.0, hard=True)
$ seenhallebikini = True
ha "So, what do you think? Does it hug my curves well?"
menu:
    "Spectacular! You were made for this bikini!":
        ha "Oh, thank you so much for the compliment!"
        window hide
        $ lust_points[9] += 1
        $ score += 1
        show lust01:
            xalign 0.7 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        ha "I'll show you the back to thank you..."
        jump HalleBikini02
    "Yeah, really hot... Turn around now...":
        ha "Like...that?"
        jump HalleBikini02

label HalleBikini02:
    scene hallebikini02 with dissolve
$ renpy.pause(1.0, hard=True)
if (pretendshop == True):
    p "Yes, that is a definitive perfect fit..."
    ha "Would...you..consider giving me a discount? I'm twenty bucks short to buy it and I really need a new bikini to go to the beach!"
    "The bikini is marked at 40 dollars..."
    menu:
        "Sure, for a girl like you, half-price! Give it to me and I'll make all the arrangements" if (money >= 20):
            ha "Oh, thank you sssoo much. My name is Halle by the way and I'll be wearing this at the beach if you ever fancy joining me (wink)!"
            jump ShopClerk
        "Mmh, you'll have to show me more to get such a discount price miss...":
            jump HalleTopOff
        "Oh, you thought I was an employee? Hah hah, no, no, I'm just your regular Joe!":
            ha "What??? But..."
            p "Ah, sorry, gotta go, busy busy...."
            window hide
            $ lust_points[9] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.7 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            jump Shop01

else:
    p "Wow, you look really hot...err..."
    ha "The name's Halle. So, since you like it so much, time to chip in 20 bucks like you promised so I can buy it!"
    menu:
        "Ah... About that.. I just realized I don't have enough money." if (money <= 19):
            ha "But..You promised me!"
            p "OK, OK, as soon as I get the money, I'll come back I swear!"
            ha "I'll be here every afternoon, lamenting as to why I can't own this lovely bikini!"
            "Well at least, I know where to find her..."
            jump Shop01
        "Ah...About that, I changed my mind. I don't want to spend 20 bucks for your bikini...":
            ha "But..You promised me!"
            window hide
            $ lust_points[9] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.7 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            p "Yeah, well, I changed my mind. Tough shit."
            jump Shop01
        "Well, sure...sure... But a little incentive wouldn't hurt... If you know what I mean...":
            ha "I know what you mean...You boys are all the same..."
            jump HalleTopOff
        "Of course, a beauty like you deserves the slutti...I mean... the best there is!":
            ha "Really, Oh, I'm so excited!!! By the way, my name is Halle."
            window hide
            $ lust_points[9] += 1
            $ score += 1
            show lust01:
                xalign 0.7 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
            jump ShopClerk
            
label HalleTopOff:
    scene halletopoff with dissolve
$ renpy.pause(1.0, hard=True)  
ha "So... Now that you've seen my big sumptuous tits... Time to cough up the money!"
p "Let me regain my breath first... WOW! I'll pay the difference for you baby!"
jump ShopClerk

label HalleGift:
scene hallegift with dissolve
$ renpy.pause(1.0, hard=True)
ha "OMG, you actually did it!"
window hide
$ lust_points[9] += 3
$ score += 3
show lust03:
    xalign 0.7 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust05
ha "I'll be wearing this at the beach every afternoon... Thank you ssso much!"
jump Shop01

label Parlour01:
scene parlour01
$ parlourseen = True
$ renpy.pause(1.0, hard=True)
play music "Sounds/parlourmusic.mp3"
ka "Welcome big American boy to \"Misohawny Massage Parlour\"! Me Katsumi, you want massage?"
menu:
    "I was told you did \"full-body massage\"...":
        ka "Yes, sucky sucky 50 dolla."
        p "Ah, I see. Sucky sucky indeed. That's quite expensive for just sucky sucky."
        ka "Me love you long time. For you, more than sucky sucky."
        p "Oh, the conversations we could have my dear..."
        jump ParlourChoice
    "Yes, how much is it?":
        ka "Normal massage? 10 dolla. More massage, 50 dolla."
        p "And what do I get for 50 dollars exactly?"
        ka "Sucky sucky 50 dolla."
        p "That's a lot of inflation since the Vietnam War..."
        jump ParlourChoice
    "Nope, not interested...":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceb

label ParlourChoice:
menu:
    "Get a normal massage (10 $)" if (money >=10):
        jump NormalMassage
    "Choose the \"full-body massage\" experience... (50 $)" if (money >=50) and (stamina >=1):
        jump FullMassage
    "Mmh...I don't seem to have enough money at the moment." if (money <=9):
        ka "You poor. Hah hah. Me not poor. Come back when you not poor."
        p "I certainly will, if just for the highly stimulating conversations."
        jump DowntownChoiceb
    "Mmh, I don't seem to have enough stamina at the moment." if(stamina == 0):
        ka "Ah! You not man enough. You leave and come back when you can cum."
        jump DowntownChoiceb
    "Actually, I don't want anything right now.":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceb

label NormalMassage:
$ money -= 10
ka "Big American boy! Put on towel. Me come back sexy for you."
p "This had better be worth it..."

scene parlour02
$ renpy.pause(1.0, hard=True)
ka "Ooh, big BIG bulge on American boy. I will sit on it when doing massage."
p "All....riiight-eee."
scene parlour03
$ renpy.pause(1.0, hard=True)
ka "You like massage? Big muscles very tense."
p "Y...yes."
scene parlour03b
ka "Oooh, cock getting VERY BIG. Bad boy. No sucky sucky 50 dolla, you not pay!"
menu:
    "It's your fault, you got me hard, you do something about it.":
        ka "No, you pay. I do it for 20 dolla more."
        menu:
            "Ok, I'll pay you 20 dolla for sucky sucky alright?" if (money >= 20) and (stamina >=1):
                ka katsumi "Yeah. Good price because you very big American boy."
                $ suckysucky = True
                $ fuckyfucky = True
                $ money -= 20
                jump Parlour05
            "Forget it. Just give me a normal massage.":
                ka katsumi "Ok, me gonna massage your cock because ssooo BIG."
                jump Parlour05
    "OK, OK, I'll pay the difference for a sucky sucky..." if (money >=40) and (stamina >=1):
        $ suckysucky = True
        $ fuckyfucky = True
        $ money -= 40
        jump Parlour05
    "Why don't you just massage it then like if it was one of my big tense muscles?...":
        ka "Oooh, boy very smart. OK, me gonna massage big American cock. But no sucky sucky, you not pay."
        jump Parlour05

label FullMassage:
$ money -= 50
$ renpy.pause(1.0, hard=True)
$ suckysucky = True
$ fuckyfucky = True
ka "Big American boy! Take clothes off. Me come back sexy for you."
p "Can't wait to get some sucky sucky from her... I'd better get my phone camera ready..."

scene parlour04
$ renpy.pause(1.0, hard=True)
ka "Ooh, cock ssooo big... Me never seen cock so big before."
menu:
    "It's still soft, it gets much bigger....":
        ka "Cock too big. Monster cock. Me only do sucky sucky."
        p "We'll make it fit."
        ka "No, you kill me with monster American boy cock!"
        p "I'll be gentle..."
        ka "Ok, me do sucky sucky and then me see if fucky fucky good."
        $ fuckyfucky = True
        jump Parlour05        
    "That's cos all Asian men have small penises.":
        ka "Not true. Some Asian men big penis. You like Trump, you racist."
        ka "Me only do sucky sucky. No fucky fucky. Because you bad boy."
        $ fuckyfucky = False
        jump Parlour05

label Parlour05:
scene parlour05 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Big American monster boycock so big and hard!"
p "Yeah, play with it Katsumi! It's all yours!"

label Parlour06:
scene parlour06a with dissolve
$ renpy.pause(1.0, hard=True)
ka "Me gonna massage huge monsterdick. You ready?"
p "Oh yeah, I'm ready!"
play sound "Sounds/parlourhandjob.mp3"
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06c
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06a
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06c
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06a
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06c
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06a
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06c
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06a
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06c
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06a
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06c
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06a
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06c
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06a
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06c
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06a
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06c
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06a
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06c
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06a
$ renpy.pause(0.2, hard=True)
scene parlour06b
$ renpy.pause(0.2, hard=True)
scene parlour06c
$ renpy.pause(0.2, hard=True)
p "Fuck, that was good, now suck me please Katsumi!"
if (suckysucky == False):
    ka "No, you pay. I do it for 20 dolla more."
    menu:
            "Ok, I'll pay you 20 dolla for sucky sucky alright?" if (money >= 20) and (stamina >=1):
                ka "Yeah. Good price because you very big American boy."
                $ suckysucky = True
                $ money -= 20
                jump Parlour07
            "Forget it. Just make me cum already." if (stamina >= 1):
                ka "Ok, me gonna massage your cock and you cum and leave."
                window hide
                $ lust_points[12] += 2
                $ score += 2
                show lust02:
                    xalign 0.3 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust02
                scene parlour06a
                $ renpy.pause(0.2, hard=True)
                scene parlour06b
                $ renpy.pause(0.2, hard=True)
                scene parlour06c
                $ renpy.pause(0.2, hard=True)
                scene parlour06b
                $ renpy.pause(0.2, hard=True)
                scene parlour06a
                $ renpy.pause(0.2, hard=True)
                scene parlour06b
                $ renpy.pause(0.2, hard=True)
                scene parlour06c
                $ renpy.pause(0.2, hard=True)
                scene parlour06cum with dissolve
                play sound "Sounds/ryancumming.mp3"
                $ renpy.pause(2.0, hard=True)
                window hide
                $ stamina -=1
                show staminaminus01:
                    xalign 0.6 yalign 0.4
                    linear 1.0 yalign 0.6
                play sound "Sounds/panting.mp3"
                $ renpy.pause(2, hard=True)
                hide staminaminus01
                ka "Good boy, you cum very big load. Now you leave. Me wait for next client."
                $ hour += 1
                jump DowntownChoiceb

    
label Parlour07:  
scene parlour07 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Me gonna lick huge balls first... Sssoo tasty and spicy, like chicken Sichuan."
window hide
$ lust_points[12] += 5
$ score += 5
show lust05:
    xalign 0.15 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust05
play sound "Sounds/lick.mp3"
p "Everything really DOES taste like chicken after all..."

label Parlour08:  
scene parlour08 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Reaching top of monstercock take me so long... Me love you long time!"
p "Keep going, you still have quite a few inches to go..."

label Parlour09:  
scene parlour09 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Oooh, lot of precum on monster boycock! You so virile!"
p "That's cos my balls are full... full of hot cum for you!"

if (fuckyfucky == False):
    ka "No fucky fucky for you."
    menu:
            "What??? You can't leave me like that! I paid good money for this!":
                ka "You pay for sucky sucky, I gave you sucky sucky."
                p "Shit! Alright, just make me cum already!"
                ka "Ok, me gonna massage your cock and you cum and leave."
                window hide
                $ lust_points[12] += 5
                $ score += 5
                show lust05:
                    xalign 0.2 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust05
                show epiclust:
                    xalign 0.4 yalign 0.2
                    zoom 0.5
                    linear 2.0 zoom 1.0
                play sound "Sounds/epiclust.mp3"
                $ renpy.pause(4.0, hard=True)
                hide epiclust
                if (katsumijosewin == False):
                    $ katsumiwin = True
                    p "Now's the time to take a pic and send it to José..."
                scene parlour06a
                $ renpy.pause(0.2, hard=True)
                scene parlour06b
                $ renpy.pause(0.2, hard=True)
                scene parlour06c
                $ renpy.pause(0.2, hard=True)
                scene parlour06b
                $ renpy.pause(0.2, hard=True)
                scene parlour06a
                $ renpy.pause(0.2, hard=True)
                scene parlour06b
                $ renpy.pause(0.2, hard=True)
                scene parlour06c
                $ renpy.pause(0.2, hard=True)
                scene parlour06cum with dissolve
                play sound "Sounds/ryancumming.mp3"
                $ renpy.pause(2.0, hard=True)
                $ stamina -=1
                show staminaminus01:
                    xalign 0.6 yalign 0.4
                    linear 1.0 yalign 0.6
                play sound "Sounds/panting.mp3"
                $ renpy.pause(2, hard=True)
                hide staminaminus01
                ka "Good boy, you cum very big load. Now you leave. Me wait for next client."
                $ hour += 1
                $ katsumifucked = True
                jump DowntownChoiceb

label Parlour10:  
scene parlour10 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Me take clothes off. Oooh, look at big American cock twitch!"
window hide
$ lust_points[12] += 5
$ score += 5
show lust05:
    xalign 0.2 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust05
show epiclust:
    xalign 0.4 yalign 0.2
    zoom 0.5
    linear 2.0 zoom 1.0
play sound "Sounds/epiclust.mp3"
$ renpy.pause(4.0, hard=True)
hide epiclust
if (katsumijosewin == False):
    $ katsumiwin = True
    p "Now's the time to take a pic and send it to José..."
        
label ParlourFuck:
stop music
play music "Sounds/katsumifuck.mp3"
show movieparlourfuck
show cum
call screen parlourfuckcum
screen parlourfuckcum:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("ParlourCum01")

label ParlourCum01:
stop music
hide movieparlourfuck
scene parlourcum01
stop music
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
ka "You filling me up with so much boyjuice! You so incredible!"

label ParlourCum02:
play sound "Sounds/ryancumming.mp3"
scene parlourcum02 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Look! Cum flowing from my Asian pussy ssooo much! Cum everywhere! Me need to get cleaned up for next client now!"
p "Fuck, you rode me like a wild bronco... I'm exhausted!"
$ katsumifucked = True
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.7 yalign 0.6
    linear 1.0 yalign 0.8
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ hour += 1
jump DowntownChoiceb


label Home02:
stop music
scene livingroom01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah, home sweet home..."

if (hour == 20):
    p "Just in time for dinner..."
    jump Dinner02

label Home02b:
stop music
scene livingroom01 with dissolve
if (hour == 20):
    p "Time for dinner..."
    jump Dinner02

p "What should I do?"
menu:
    "Go to my room":
       jump RyanBedroomDay02
    "Go to the bathroom":
        jump BathRoomDay02
    "Go to Nancy's room" if (momroomseen02 == False):
        jump MomRoomDay02
    "Go to the swimming pool" if (locswimmingpool == False):
        jump SwimmingPoolDay02
    "Leave the house":
        jump Burbs02

label SwimmingPoolDay02:
$ locswimmingpool = True
if (hour <= 18):
    scene poolempty with dissolve
    play music "Sounds/gardensound.mp3"
    $ renpy.pause(1.0, hard=True)
    p "There's no one around, I can't even, like, perv on Nancy or Nikki in a bikini right now. SAD."
    $ locswimmingpool = False
    jump Home02b
if (hour == 19):
    scene poolnikkiday02 with dissolve
    play music "Sounds/gardensound.mp3"
    $ renpy.pause(1.0, hard=True)
    p "Nikki is sunbathing... She has such huge muscles, it's making me horny..."
    s "What was that [name]? You're mumbling to yourself again?"
    p "No, nothing... Just admiring the...err... view from our garden."
    p "Well, I might as well swim a bit, dinner is soon..."
    scene poolryanday02 with dissolve
    play sound "Sounds/diving.mp3"
    $ renpy.pause(1.0, hard=True)
    p "This is fun, I think I'm going to enjoy our swimming pool a lot..."
    $ hour += 1
    $ locswimmingpool = False
    jump Dinner02

label RyanBedroomDay02:
stop music
$ locroom = True
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
if (hour >= 20):
    $ hour = 20
    p "Oh, it's time for dinner, I'd better hurry downstairs..."
    jump Dinner02

p "What to do, what to do..."
menu:
    "Turn the computer on":
        jump ComputerDay02
    "Do some heavy bodybuilding (+2hrs)" if (hour <= 18):
        if (workout == True):
            "You already trained today."
            jump RyanBedroomDay02
        else:
            play music "Sounds/workoutgroan.mp3"
            $ renpy.movie_cutscene("Day1/bedroomworkout.ogv", delay=-1, loops=-1, stop_music=False)
            stop music
            scene ryanworkout01
            play sound "Sounds/panting.mp3"
            $ renpy.pause(2, hard=True)
            p "That was great, I can feel my muscles getting bigger and stronger already..."
            window hide
            $ strength += 1
            show strengthplus01:
                xalign 0.6 yalign 0.6
                linear 1.0 yalign 0.4
            play sound "Sounds/more.mp3"
            $ renpy.pause(3, hard=True)
            hide strengthplus01
            $ workout = True
            $ hour += 2 
            jump RyanBedroomDay02        
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump RyanBedroomDay02
    "Go the living room":
        jump Home02b
    "Go to the bathroom" if (showerseen02 == False):
        jump BathRoomDay02
    "Go to Nancy's room" if (momroomseen02 == False):
        jump MomRoomDay02
    "Read the book Laura gave you (+1hr)" if (book == True) and (bookread == False):
        jump RyanReadingDay02b

label RyanReadingDay02b:
scene ryanreading with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump RyanBedroomDay02

label ComputerDay02:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label ComputerDay02b:
scene ryancomputerday
menu:
    "Check the map":
        jump MapDay02
    "Check the stats":
        jump StatsDay02
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump ComputerDay02b
    "Learn how to use the pendulum" if (pendulum == True) and (pendulumactive ==False):
        jump CompPendulumDay02
    "Play a smutty game (+1hr)":
        jump CompGameDay
    "Turn the computer off":
        jump RyanBedroomDay02

label CompPendulumDay02:
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump ComputerDay02b

label MapDay02:
play sound "Sounds/mouseclick.mp3"
hide screen statsbackground
hide screen inventorybutton
hide screen calendar
show islandmap with dissolve
$ renpy.pause(1.0, hard=True)
if (discoverrandybeach == True):
    show randybeachmap
if (discoveraunthouse == True):
    show aunthousemap
if (discovergym == True):
    show gymmap
if (discoverschool == True):
    show schoolmap
if (discovermassage == True):
    show parlourmap
if (discoveraudacious == True):
    show audaciousmap
if (discoverstore == True):
    show storemap
if (discovertanya == True):
    show tanyamap
p "This shows all the places I know so far on Veri-Bosti Island..."
show screen statsbackground
show screen inventorybutton
show screen calendar
jump ComputerDay02b

label StatsDay02:
play sound "Sounds/mouseclick.mp3"
scene stats
hide screen statsbackground
hide screen inventorybutton
hide screen calendar
show screen statsscreen
$ renpy.pause(1.0, hard=True)
p "Time to check my progress against José's..."
hide screen statsscreen
show screen statsbackground
show screen inventorybutton
show screen calendar
jump ComputerDay02b

label CompGameDay:
scene ryancomputergameday
$ renpy.pause(1.0, hard=True)
p "This game is tough. My fingers hurt like hell from so much clicking..."
$ hour += 1
jump ComputerDay02b 

label MomRoomDay02:
scene nancybedroomday with dissolve
$ renpy.pause(1.0, hard=True)
$ momroomseen02 = True
p "Nancy's room is so clean and tidy. Not like mine."
menu:
    "Snoop around":
        jump MomBedroomSnoop  
    "Go back to my room":
        jump RyanBedroomDay02

label MomBedroomSnoop:
p "There might be an interesting item hidden somewhere... Time to snoop around..."
p "But I have a limited amount of time to look for it, Nancy might come back from work anytime for all I know."
play music "Sounds/snooping.mp3"
call screen mombedroomsnoop
stop music
"You were too slow and didn't find anything."
jump RyanBedroomDay02

label FoundDildo:
scene mombedroomsnooping
$ renpy.pause(1.0, hard=True)
stop music
show dildo
show square
play sound "Sounds/found.mp3"
"You found a big black dildo. Mmh, why does Nancy have a big black dildo I wonder?..."
$ dildo = True
hide dildo
hide square
jump RyanBedroomDay02

label BathRoomDay02:
stop music
if (hour <= 17):
    jump EmptyBathRoomDay02
if (hour == 18) or (hour == 19):
    jump MomShowerDay02

label EmptyBathRoomDay02:
scene bathroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "No one is around right now, I could take a shower if I wanted to."
menu:
    "Take a shower":
        jump ShowerDay02
    "Leave":
        jump RyanBedroomDay02

label ShowerDay02:
scene shower with dissolve
stop music
play music "Sounds/shower.mp3"
$ renpy.pause(1.0, hard=True)
p "That's nice and relaxing..."
if (stamina <= 4) and (showerseen02 == False):
    window hide
    $ stamina += 1
    show stamina01:
        xalign 0.4 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide stamina01
    $ showerseen02 = True
$ showerseen02 = True
jump RyanBedroomDay02

label MomShowerDay02:
play music "Sounds/shower.mp3"
$ locroom = False
scene bathroomdoorclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "Someone's taking a shower..."
label MomBathroomDay02b:
menu:
    "Use lubricant on the door hinges" if (wd69 == True) and (squeakfixed == False):
        "The door should not squeak anymore."
        $ squeakfixed = True
        jump MomBathroomDay02b        
    "Have a peek":
        jump MomPeekBathroomDay02
    "Leave":
        jump RyanBedroomDay02

label MomPeekBathroomDay02:
if (squeakfixed == False):
    play sound "Sounds/doorsqueak.mp3"
    scene bathroomdooropen with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Shit, the door is squeaking..."
    m "I'm in the shower sweetie, don't get in!"
    p "Ah, sorry Nancy...I'm leaving..."
    p "Damn, I should try and find a way of stopping that door from squeaking if I want to spy on Nancy or Nikki in the shower like every other MC..."
    jump RyanBedroomDay02
if (squeakfixed == True):
    scene nancyshower01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Cool, she didn't hear me come in, I can see her naked in the shower now..."
    p "Fuck yeah, look at those huge titties... How I would love to rub my pud between them..."
menu:
        "Watch a little longer...":
            jump MomShower02
        "Leave before she turns round and catches me":
            jump RyanBedroomDay02
    
label MomShower02:
if (momshowerpeep == False):
    $ peeping += 1
$ momshowerpeep = True
scene nancyshower02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, her arse was made for fucking a great big cock. MY giant cock!"
menu:
        "Watch a little longer still...":
            jump MomShower03
        "Leave before she turns round and catches me":
            jump RyanBedroomDay02
 
label MomShower03:
scene nancyshower03 with dissolve
$ renpy.pause(1.0, hard=True)
m "OMG, my own tenant is spying on me in the shower! What kind of monster did I let into my house?"
$ lust_points[16] -=2
$ score -= 2
show lustminus02:
    xalign 0.3 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/less.mp3"
$ renpy.pause(2, hard=True)
hide lustminus02
p "No, it's not what you think... I just like... stumbled while in the hallway and ended up here!"
m "You are such a bad liar [name]! Get out of here IMMEDIATELY!"
jump RyanBedroomDay02


label Beach02:
stop music
play music "Sounds/oceanwaves.mp3"
scene beach with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah! Here's Tini-Wini-Bikini beach, as sunny as always... I should probably head for the beach bar first..."
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_18
    $ lustaddedB = 3
    call Challenger from _call_Challenger_19
    $ lustaddedB = 1
    call Challenger from _call_Challenger_20
    $ lustaddedB = 1
    call Challenger from _call_Challenger_21
    $ challengercalls += 2

label BeachBar01b:
play music "Sounds/tropicalmusic.mp3"
label BeachBar02b:
scene beachbar01 with dissolve
$ renpy.pause(1.0, hard=True)
bb "Aloha, welcome to Tini-Wini-Bikini Beach bar!"
menu:
    "Chat with her":
        jump ChatBeachBarb    
    "Leave":
        jump ExploreBeach02

label ChatBeachBarb:
bb "Have some free candy from our sponsor!"

menu:    
    "Thanks, I have a white chocolate stick to offer you in exchange...":
        scene beachbar03
        bb "Oh, that was sssooo subtle I almost fell for it."
        jump BeachBar02b
    "Who's your sponsor?":
        scene beachbar03
        bb "Audacious Bikinis. They have their headquarters right here on the island west of downtown."
        window hide
        $ discoveraudacious = True
        $ beachtipgiven +=1
        show addedlocation:
            xalign 0.3 yalign 0.3
            linear 1.0 yalign 0.1
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide addedlocation
        jump BeachBar02b
        
label ExploreBeach02:
p "Hum... Where should I go?"
menu:
    "Go to the beach bar":
        jump BeachBar01b
    "Walk along the beach" if (lollyseen == False):
        jump LollyBeach01
    "Go to Randy Beach" if ((discoverrandybeach == True) and (randybeachseen02 == False)):
        jump RandyBeach02
    "Take the Bus to town":
        jump BusBeachTown
    "Take the Bus back home":
        jump BusBeachHome

label BusBeachTown:
scene beach with dissolve
$ renpy.pause(1.0, hard=True)   
p "Bye bye Tini-Wini-Bikini beach!"
p "Ah, here's the bus going to town..."
$ hour += 1
jump Downtown
    
label BusBeachHome:
scene beach with dissolve
$ renpy.pause(1.0, hard=True)
p "Bye bye Tini-Wini-Bikini beach!"
p "Ah, here's the bus going to town..."
$ hour += 1
jump Burbs02

label LollyBeach01:
$ lollyseen = True
stop music
play music "Sounds/oceanwaves.mp3"
scene lollybeach01 with dissolve
$ renpy.pause(1.0, hard=True)
"There's a young girl standing with a ball on a secluded part of the beach..."
lo "Hey Mister, do you wanna play with me?"
label LollyChoice:
menu:
    "Are you all alone?":
        lo "Yes, I came here to play with my  big ball and I don't know where my mum went. But who cares. Let's play shall we?"
        jump LollyChoice
    "Do you want some candy?":
        scene lollybeach02
        lo "Oh, wow, thanks mister, I LOVE candy! Now let's play with that big ball shall we?"
        $ candygiven = True
        jump LollyChoice
    "What's your name little girl?":
        lo "Lolly... Lolly Kohn... Let's play with my big ball shall we?"
        jump LollyChoice
    "Sure, why not...":
        jump LollyBeach02

label LollyBeach02:
scene lollybeach03 with dissolve
$ renpy.pause(1.0, hard=True)
lo "Yeah, I'm playing with my big ball with a total stranger!"
menu:
    "I gave you some candy, it's only fair you give me your... swim bra." if (candygiven == True):
        lo "But they hold my big titties and keep naughty men from seeing them, that's what my mom says!"
        $ braasked = True
        jump LollyBeach03
    "I've got a big rock candy you could suck on if you want...":
        lo "Yeah, I LOVE candy! Show it to me, show it to me please!"
        $ rockcandy = True
        jump LollyBeach03
    "OK, enough pointless banter, where's you hot mom?":
        jump LollyBeach03
    "Why don't you play topless, it will be more fun." if (candygiven == False):
        lo "Mmh, I don't know, mommy says I shouldn't show my big titties to total strangers..."
        p "Oh, come on now..."
        $ braasked = True
        jump LollyBeach03

label LollyBeach03:
scene lollybeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Oh, there you are sweetheart, you gave me the fright of my life! Don't run away like that on a public beach!"
lo "I was playing with my big ball and this nice boy!"
if (candygiven == True):
    show lollybeach04b
    lo "He gave me some candy too!"
    ma "WHAT? I told you not to accept candy from strangers!" 
    scene lollybeachmariaangry01
    ma "Giving candy to little girls? You have some explaining to do young man!"
    if (rockcandy == True):
        scene lollybeach04
        show lollybeach04b
        lo "He also told me I could suck on his big rock candy..."
        p "No, I had a real rock candy I swear, it's like... Where is it again?"
        scene lollybeachmariaangry02
        ma "OH MY GOD! That's it, I'm calling the cops on you!"
        jump LollyBeachCop
    if (braasked == True):
        scene lollybeach04
        show lollybeach04b
        lo "He also told me I should show him my titties..."
        p "Show me her titties? No, that was just a joke, ha ha..."
        scene lollybeachmariaangry02
        ma "OH MY GOD! That's it, I'm calling the cops on you!"
        jump LollyBeachCop    
    else:
        p "They were distributing them for free at the beach bar! I just gave her some, nothing more..."
        ma "I'll give you the benefit of the doubt... THIS time."
        jump LollyBeachMaria
else:
    if (rockcandy == True):
        show lollybeach04b
        lo "He also told me I could suck on his big rock candy..."
        p "No, I had a real rock candy I swear, it's like... Where is it again?"
        scene lollybeachmariaangry02
        ma "OH MY GOD! That's it, I'm calling the cops on you!"
        jump LollyBeachCop
    if (braasked == True):
        scene lollybeach04
        show lollybeach04b
        lo "He also told me I should show him my titties..."
        p "Show me her titties? No, that was just a joke, ha ha..."
        scene lollybeachmariaangry02
        ma "OH MY GOD! That's it, I'm calling the cops on you!"
        jump LollyBeachCop    
    else:
        scene lollybeachmariaangry01 with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "I'm not sure I like the fact you were playing with my daughter..."
        jump MariaGood       
        

label MariaGood:
menu:
    "Well, YOU should look after your daughter a bit better... Good thing I was around.":
        scene mariasorry with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "Yes, you're right, it was my fault... Thank you..."
        window hide
        $ lust_points[15] += 1
        $ score += 1
        show lust01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01        
        jump LollyBeachMaria
    "I took good care of her, don't worry ma'am.":        
        scene mariagrateful with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "Still, you are a stranger after all... I always imagine the worst..."
        jump LollyBeachMaria
   
label LollyBeachMaria:
scene mariagrateful with dissolve
ma "I must apologize for my daughter's behavior, I hope she didn't cause you any trouble."
menu:
    "Not at all, I was hoping to get better acquainted with her mother actually...":
        scene mariahappy with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "And why would you want that?"
        menu:
            "Cos she has big tits for her age, so...":
                ma "What? You were looking at Lolly's tits???"
                p "Yes...I mean...no... I mean, well, you are a beautiful woman..."
                ma "Humpf... Leave us alone. Lolly, we are leaving, come with me."
                jump ExploreBeach02
            "I'm new in town and looking to meet like-minded people.":
                ma "And what exactly is this \"similar mind\" you are referring too?"
                p "I'm very open. What do you do for a living?"
                ma "I'm a single mother raising a kid, that's what I do! But to make ends meet, I'm also a part-time librarian at Hardcox High School."
                p "Oh, well I'm a new student there! And I...err... looove to study there!"
                ma "Ah? Err.. Then I guess I'll see you around at the library then... I'm Maria, nice to meet you...?"
                p "[name]. Yes, have a nice day Maria. And you too lolly."
                lo "Goodbye Mr muscle-stranger-boy!"    
                jump ExploreBeach02
    "Not at all, I was just walking along the beach when I saw her and realized she needed help.":
        scene mariagrateful with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "Well, thank you so much for keeping an eye on her. My name is Maria, a pleasure to meet you...?"
        p "[name] Johnson ma'am. The pleasure is all mine."        
        window hide
        $ lust_points[15] += 1
        $ score += 1
        show lust01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        ma "What school do you attend?"
        p "Hardcox High."
        scene mariahappy with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "Oh? I'm the part-time librarian there. I work on Tuesday, Thursday and Friday afternoons there!"
        p "Really? Then I will probably see you around, I like to use the library to... err.. study."
        ma "That's good. Well, I should leave now, Lolly say goodbye to [name] and come along..."
        lo "Goodbye Mr muscle-stranger-boy!"
        jump ExploreBeach02

label LollyBeachCop:
scene lollybeachcop01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "I'm telling you, this boy tried to entice my daughter into committing sexual acts on him!"
co "These are serious allegations ma'am, I need some proof!"
if (rockcandy == True):
    ma "Proof! He gave candy to my daughter and tried to get her to \"suck on his big rock candy\", that's what she told me!"
    co "Alright then, that's good enough for me!"
    jump LollyBeachCop02
if (braasked == True):
    ma "Proof! He gave candy to my daughter and tried to get her to strip naked for him, that's what she told me!"
    co "Alright then, that's good enough for me!"
    jump LollyBeachCop02

label LollyBeachCop02:
scene lollybeachcop02 with dissolve
$ renpy.pause(1.0, hard=True)
co "YOU, come with me, we have some talking to do... at the station!"
p "But...I ain't done nothing wrong I swear!"
co "We'll see about that..."

label Jail01:
stop music
scene jail01 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/policesound.mp3"
$ wenttojail = True
p "Hey, it hurts, what the fuck are you doing? This is police brutality at its worst!..."
co "That'll teach you a lesson you fucking pedo! Statutory rape attempt, you're done for!"
p "It can't be statutory rape cos I'm like... Shit, I can't say it here..."
scene jail02 with dissolve
play sound "Sounds/arserod.mp3"
$ renpy.pause(1.0, hard=True)
co "How do you like that? Having a big truncheon stuck up YOUR arse?"
p "I don't like it! I don't like it AT ALL! Please, stop it! AAAAH!"
scene black with dissolve
$ renpy.pause(1.0, hard=True)
p "She finally left... But I'm still in cuffs... When will this nightmare end?"
$ lustaddedB = 3
call Challenger from _call_Challenger_22
$ lustaddedB = 3
call Challenger from _call_Challenger_23
$ lustaddedB = 1
call Challenger from _call_Challenger_24
$ lustaddedB = 1
call Challenger from _call_Challenger_25
$ challengercalls += 2

scene jail03 with dissolve
$ hour = 22
$ renpy.pause(1.0, hard=True)
co "Ok, it turns out the charges are being dropped because the statutory rape thing doesn't apply here, for reasons we cannot discuss."
co "You're free to go, but not to try and rape young girls, you hear me?"
p "I'll start a movement called \"White Arses Matter\" I swear to God!"
co "Yeah, yeah, whatever. Now go back home. Your landlady is waiting for you in her car..."
scene jailmom01 with dissolve
play music "Sounds/caridle.mp3"
$ renpy.pause(1.0, hard=True)
m "My God, what happened [name]? This is so embarrassing!"
window hide
$ lust_points[16] -=1
$ score -= 1
show lustminus01:
    xalign 0.75 yalign 0.5
    linear 1.0 yalign 0.7
play sound "Sounds/less.mp3"
$ renpy.pause(2, hard=True)
hide lustminus01
menu:
    "I was set up! I'm innocent, this is a parody of justice!":
        show jailmom01b
        m "...Said every criminal ever. Now I don't want to hear another word from you mister. And no pocket money for you for two days!"        
        $ pocketmoney = True
        window hide
        $ lust_points[16] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.75 yalign 0.5
            linear 1.0 yalign 0.7
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        $ hour += 1
        stop music
        jump RyanRoomEveningDay02
    "They brutalized me Nancy, they probed my inner sanctum with a police club....sniff...":
        show jailmom01b
        m "Oh, sweetie, this is terrible... Let's go home and try and forget about this... Stay out of trouble and everything will be fine..."
        $ hour += 1
        stop music
        jump RyanRoomEveningDay02
 
label RandyBeach02:
stop music
$ seenparasolb01 = False
$ seenparasolb02 = False
$ seenparasolb03 = False
scene randybeach01 with dissolve
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
$ randybeachseen02 = True
if (randybeachseen == True):
    p "Finally back here again. I'd better take my speedos off."
else:
    p "I guess that's it. I'd better take my speedos off."
$ randybeachseen = True
window hide
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)

label RandyBeach02b:
p "I see three parasols but I can't see the people behind them...Which one should I go to?"
menu:
    "Go to the closest red parasol on the right" if (seenparasolb01 == False):
        jump RandyBeachParasolb01
    "Go to the middle orange parasol" if (seenparasolb02 == False):
        jump RandyBeachParasolb02
    "Go to the furthest red parasol on the left"if (seenparasolb03== False):
        jump RandyBeachParasolb03
    "Leave Randy Beach":
        if (seenparasolb01 == True) or (seenparasolb03 == True):
            $ hour += 1
        jump ExploreBeach02

label RandyBeachParasolb02:
$ seenparasolb02 = True
scene middleparasololdwoman
show randybeachparasol02
$ renpy.pause(2.0, hard=True)
p "Just a leg... This means a pussy not too far away..."
window hide
hide randybeachparasol02 with moveoutleft
$ renpy.pause(1.0, hard=True)
play sound "Sounds/oldmoaning.mp3"
ow "Ooh, I need a real cock! Come and replace my big friend, boy!"
if (seenparasol01 == True):
    p "NNNNOOO, not HER again! I'd better run away FAST!"
else:
    p "What the fuck? No way, run for your life, RUN FOR YOUR LIFE!"
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
p "That image will remain impregnated in my mind for a long time..."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.4 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ eyesore += 1
jump RandyBeach02b

label RandyBeachParasolb03:
$ seenparasolb03 = True
scene lesbians01
show randybeachparasol03
$ renpy.pause(1.0, hard=True)
p "What depravity will I find behind this parasol?..."
window hide
hide randybeachparasol03 with moveoutright
$ renpy.pause(1.0, hard=True)
play sound "Sounds/lesbians.mp3"
p "Nice, two hot chicks going at it..."
show lesbians01b
l01 "Hey, who do you think you are?"
menu:
    "God's gift to women.":
        l01 "Well, we're strictly lesbians. And you're not invited to the club."
        menu:
            "Good, cos I don't want to turn into a carpet-munching sissy! Ciao bella!":
                stop sound
                scene randybeach01 with dissolve
                show ryanrandybeach with dissolve
                jump RandyBeach02b
            "What if I show you my own club? He's called \"Billy\"...":
                l02 "You're kind of funny. We could let him watch..."
                jump Lesbians02
    "Just a pervert who likes to watch...":
        l02 "We're lesbians. So you can watch but you can't touch... Is that clear?"
        p "Can I jack off at least?"
        l01 "If you do, you can't fucking cum, we don't want a drop of your filthy male scum on us!"
        p "Gee, if we can't even shower dykes with cum these days... Feminism has just gone too far."
        jump Lesbians02
    "Your daddy. Who's your daddy? I'm your daddy!":
        l01 "Oh yeah? Cos I beat the crap out of my father after I told him I was a lesbian and he didn't agree!"
        l02 "Which means... You're going to get the beating of your lifetime boy! Let's grab him!"
        stop sound
        p "What? But... Help! Somebody, anybody!"
        jump LesbianBeating
    "Nobody. I shall bid you farewell my fair ladies.":
        stop sound
        scene randybeach01 with dissolve
        show ryanrandybeach with dissolve
        jump RandyBeach02b

label Lesbians02:
$ peeping += 1
scene lesbians02 with dissolve
$ renpy.pause(1.0, hard=True)
l01 "Fuck yeah, rub my pussy, just like that!"
l02 "AAh, so much better than a pathetic cock!"
p "I'm sure you would disagree if I stuck my massive weapon between your pussyfolds..."
scene lesbians03 with dissolve
$ renpy.pause(1.0, hard=True)
l01 "Watch in silence boy! We didn't ask for your useless opinion! Men are always wrong!"
l02 "Just like that... Oooh, I'm gonna cum!"
l01 "Lick my pussy, I need to get to the seventh heaven real FAST!"
scene lesbians04 with dissolve
$ renpy.pause(1.0, hard=True)
l01 "FUCK! You do that so well, I'm gonna CUM, cummmmmiiinng!"
p "So am I... Anytime soon now..."
l02 "Don't you dare fucking cum you filthy boy!"
menu:
    "Do as you're told by a bunch of lesbians":
        jump LesbiansNoCum
    "Cum anyway, you've got your male urges to satisfy":
        jump LesbiansCum

label LesbiansCum:
stop sound
scene lesbianscum with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "Oh boy, I'm spewing my load, RHHHAAA..."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.85 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
l01 "WTF? Aim that dong out of the way, my God, I can't believe he's doing this!"
l02 "Yikes, he's emptying his vile spunk all over our bodies, you're gonna pay for this kid!"
scene lesbianscum02 with dissolve
$ renpy.pause(1.0, hard=True)
l01 "Take that you arsehole! Hold his legs while I punch this little shit!"
play sound "Sounds/punch.mp3"
$ renpy.pause(1.0, hard=True)
p "No, please stop it, I just couldn't hold back, it's not my fault!"
play sound "Sounds/punch.mp3"
$ renpy.pause(1.0, hard=True)
l02 "We warned you boy, now let's get the fuck outta here Rosie!"
scene lesbiansbeaten with dissolve
$ renpy.pause(1.0, hard=True)
p "Finally, they left... I just took a right beating from a couple of dykes, but it was all worth it.... Aaaah..."
if (stamina >= 1):
    window hide
    $ stamina -=1
    show staminaminus01:
        xalign 0.3 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeach02b

label LesbiansNoCum:
stop sound
$ renpy.pause(1.0, hard=True)
p "Need...to...hold back... Pfeew, that was sssoo close."
show lesbian02happy
l02 "I'm impressed, usually our show makes every cock spew its filthy load in no time..."
show lesbian01happy
l01 "A man with self-control? That'll be a first. Now get the fuck out of here boy."
p "Sure... Such a pleasure meeting you lovely ladies..."
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeach02b

label LesbianBeating:
stop sound
scene lesbianscum02b with dissolve
$ renpy.pause(1.0, hard=True)
l01 "Take that you arsehole! Hold his legs while I punch this little shit!"
play sound "Sounds/punch.mp3"
$ renpy.pause(1.0, hard=True)
p "No, please stop it, I didn't mean it, I'm not your daddy!"
play sound "Sounds/punch.mp3"
$ renpy.pause(1.0, hard=True)
l02 "Too late boy, now let's get the fuck outta here Rosie!"
scene lesbiansbeaten with dissolve
$ renpy.pause(1.0, hard=True)
p "Finally, these crazy dykes left... Note to self: lesbians don't like daddies... Aaaah..."
if (stamina >= 1):
    window hide
    $ stamina -=1
    show staminaminus01:
        xalign 0.3 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeach02b


label RandyBeachParasolb01:
$ seenparasolb01 = True
scene randyanna01
show randybeachparasol03
$ renpy.pause(1.0, hard=True)
p "I hope it won't be another major disappointment..."
window hide
hide randybeachparasol03 with moveoutright
$ renpy.pause(1.0, hard=True)
p "Shit, that's Anna, José's mum!"
scene randyanna02
an "[name]! I didn't expect you to come to this beach, this is so embarrassing!"
menu:
    "Cover your dong with your hands":
        jump RandyAnna02
    "Let it hang out and get a semi":
        jump RandyAnna03
    "Apologize and leave her alone":
        an "Thank you [name]. Let's not mention this... incident to anyone."
        scene randybeach01 with dissolve
        show ryanrandybeach with dissolve
        $ renpy.pause(1.0, hard=True)
        jump RandyBeach02b

label RandyAnna02:
scene randyanna03 with dissolve
$ renpy.pause(1.0, hard=True)
p "And I didn't expect you to be here either, sorry to have exposed myself by mistake to you Ms Longrod..."
an "Well... It's not your fault... I didn't see a thing... Even though it was hard not to notice your... huge thingy..."
window hide
$ lust_points[0] +=1
$ score += 1
show lust01:
    xalign 0.2 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
menu:
    "It was hard not to notice your gorgeous breasts too Ms Longrod.":
        an "Please don't talk like that... Anyway, I didn't see any stirring down there when you saw them..."
        p "Ah, so you DID see a thing. A HUGE thingy as you rightfully call it."
        an "I meant... Damn, who am I kidding. Yes, I saw your massive pecker. You must be very proud of it I imagine..."
        p playersrite "Yes, it's the biggest dong on this island I'm sure of it."
        an "Well that's a rather bold statement for such a young boy..."
        jump RandyAnna05
    "Can't complain. Certainly does the trick with the ladies.":
        an "The trick? What do you mean? You're so young..."
        window hide
        $ lust_points[0] += 1
        $ score += 1
        show lust01:
            xalign 0.2 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        p "Sure, I've got tons of experience with chicks... And chicks have tons of experience with my big bad boy..."
        an "You talk like... you're some kind of sex god... And your penis... It looks enormous!"
        jump RandyAnna05

label RandyAnna03:
scene randyanna04 with dissolve
$ renpy.pause(1.0, hard=True)
an "My God [name], please cover yourself... Your...thingy...It's getting even BIGGER!"
menu:
    "It's hopeless, my cock is just too damn huge, even both my hands wouldn't begin to cover it Ms Longrod...":
        an "Yes, I can imagine, this thing is the biggest cock I've ever seen!"
        window hide
        $ lust_points[0] += 1
        $ score += 1
        show lust01:
            xalign 0.2 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump RandyAnna05
    "When it sees a hot lady like you, it always has to give a nod of approval...":
        an "I think it's best if you leave now, I don't want to be seen with a naked boy sporting a massive hardon in public."
        p "But..."
        an "Leave [name]!"
        scene randybeach01 with dissolve
        show ryanrandybeach with dissolve
        $ renpy.pause(1.0, hard=True)
        jump RandyBeach02b

label RandyAnna05:
an "Let me...see it a bit more... and a bit longer..."
menu:
    "I show you mine if you show me yours, it's only fair...":
        jump RandyAnna06
    "Let it swing":
        jump RandyAnna07

label RandyAnna06:
scene randyanna05 with dissolve
$ renpy.pause(1.0, hard=True)
an "That's what you want to see horny boy... My wet pussy... And my large breasts..."
p "Fuck yeah! How about you play with your tits?"
scene randyannatits01 with dissolve
$ renpy.pause(1.0, hard=True)
an "God, you're so naughty... I love it! Like that?"
scene randyannatits02
$ renpy.pause(0.3, hard=True)
scene randyannatits01
$ renpy.pause(0.3, hard=True)
scene randyannatits02
$ renpy.pause(0.3, hard=True)
scene randyannatits01
$ renpy.pause(0.3, hard=True)
scene randyannatits02
$ renpy.pause(0.3, hard=True)
scene randyannatits01
$ renpy.pause(0.3, hard=True)
scene randyannatits02
$ renpy.pause(0.3, hard=True)
scene randyannatits01
$ renpy.pause(0.3, hard=True)
scene randyannatits02
$ renpy.pause(0.3, hard=True)
scene randyannatits01
$ renpy.pause(0.3, hard=True)
an "Is that getting your massive dong ROCK-HARD?"
window hide
$ lust_points[0] += 2
$ score += 2
show lust02:
    xalign 0.2 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
scene randyannaryan01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Please let me fuck that tender pussy, I'm bursting at the seams!"
scene randyanna05 with dissolve
$ renpy.pause(1.0, hard=True)
an "No... I mean, it's a public place, we can't do that... Some more people are arriving, we've gone too far already..."
an "I think it's best you leave... I have to leave too... I'm too damn horny and I need to rub my pussy when I get home..."
scene randyannaryan01 with dissolve
$ renpy.pause(1.0, hard=True)
p "What? But look at how hard I am! Damn, it's not fair... What do you have to do to get good cervix these days?"
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeach02b

label RandyAnna07:
scene randyannaswing01 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyannaswing02 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyannaswing01 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyannaswing02 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyannaswing01 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyannaswing02 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyannaswing01 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyannaswing02 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyannaswing01 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyannaswing02 with dissolve
$ renpy.pause(0.3, hard=True)
an "Oh wow... It's not even hard and it looks already so... massive and heavy."
window hide
$ lust_points[0] += 1
$ score += 1
show lust01:
    xalign 0.1 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
p "Maybe it's time for you to show me yours..."
an "Yeah, I guess you deserve it..."
jump RandyAnna06


label Dinner02:
stop music
scene dinner01
show nikkinormal
$ renpy.pause(1.0, hard=True)

$ lustaddedB = 3
call Challenger from _call_Challenger_26
$ lustaddedB = 2
call Challenger from _call_Challenger_27
$ lustaddedB = 1
call Challenger from _call_Challenger_28
$ lustaddedB = 1
call Challenger from _call_Challenger_29
$ challengercalls += 2

m "So how was your first day at school [name]?"
menu:
    "I was sexually abused by the principal..." if (principalfootjob == True):
        show nancyshocked
        m "What? My poor, poor boy, that's terrible! But it's best you don't say a word about it, I hear she is running for a senate seat and no one will believe you."
        p "But... You DO believe me Nancy, right?"
        hide nancyshocked
        show nancyhappy
        m "Of course I do son! You're my sweet little innocent pumpkin!"
        window hide
        $ lust_points[16] +=1
        $ score += 1
        show lust01:
            xalign 0.8 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        hide nikkinormal
        show nikkihappy
        s "Humpf, you probably enjoyed it, she has the largest boobs on the island!"
        p "No! I am a sweet innocent pumpkin, didn't you hear what Nancy said?"
        hide nikkihappy
        show nikkinormal
        hide nancyhappy
        jump NikkiDinnerTalk
    "It was great, I met all my classmates and my teacher was really nice to me...":
        m "Oh, wonderful! Hopefully your grades will improve in this school.."
        jump NikkiDinnerTalk

label NikkiDinnerTalk:
s "And you mom? How was your day working in Debby's company?"
m "I was very busy from the start, having to organize photo shoots, pick some bikini design, do some advertisement work."
m "But I really like it and I'm very grateful for this wonderful opportunity. I think we will all settle down very well on this wonderful island, don't you think?"
s "Oh yeah, it's like a tropical paradise. I really like it too!"
show nancynikki
m "So, did you meet that nice boy José?"
show nikkimom
s "Yes... He was really nice to me..."
p "He was flirting with Brittany all day long, I saw him!"
hide nikkimom
show nikkiryan
s "That's not true, stop saying nasty stuff like that about him!"
if (seenlockerbrit == True):
    hide nancynikki
    p "It's true Nikki, I overheard them talking about the bikini pageant in the corridors and he was drooling all over her. I'm sorry..."
    hide nikkiryan
    hide nikkinormal
    show nikkicrying
    window hide
    $ lust_pointsB[17] -=2
    show challengerlustminus02:
        xalign 0.35 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide challengerlustminus02
    s "It...sniff...doesn't matter... He's nothing to me!"
    hide nikkicrying
    show nancynikki
    m "Oh, Nikki, don't worry, maybe he will change his mind? Or you will find an even nicer boy."    
    hide nancynikki
    jump EndDinner02
elif (seenlockerbrit == False):
    menu:    
        "Yeah..well... I can tell he's interested in her and not you, so there!":
            hide nikkinormal
            hide nikkiryan
            show nikkicrying
            window hide
            $ lust_points[17] -=2
            $ score -= 2
            show lustminus02:
                xalign 0.35 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus02    
            show nancyangry
            m "Now stop it, why do you say such things without any proof? You're hurting Nikki's feelings for no apparent reasons, that's just terrible!"    
            if (detention == True):
                s "And you...sniff...you got detention!"
                m "WHAT? Is that true [name]?"
                hide nikkicrying
                p "Y..yeah, but it wasn't my fault!"
                m "I SPECIFICALLY told you not to get into any kind of trouble and you do this to me, on your FIRST day of school!"
                window hide
                $ lust_points[16] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.35 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
                m "Now eat up and do the dishes TOGETHER after dinner."
                jump EndDinner02        
            elif (detention == False):
                s "You're just jealous because no one loves you!"
                m "Well said and well deserved..."
                hide nikkicrying
                p "Maybe I should start crying like a little girl so that everyone \"loves\" me... Grump.."
                m "Now eat up and do the dishes TOGETHER after dinner."
                jump EndDinner02
        "Well, I still think he's a douchebag... So there!":
            s "Well, that's YOUR opinion."
            m "And you should keep it to yourself! Now eat up both of you or the dinner is going to get cold."
            jump EndDinner02
        
label EndDinner02:
"You finish cleaning up the dishes with Nikki and head for your room."
$ hour += 1

label RyanRoomEveningDay02:
stop music
scene ryanbedroomnight with dissolve
$ locroom = True
$ renpy.pause(1.0, hard=True)
    
if (hour == 23) and (nightshowerseen02 == True) and (nightmomroomseen02 == True):
    $ hour += 1
if (hour >= 24):
    if (challengercalls <= 10):
        $ lustaddedB = 2
        call Challenger from _call_Challenger_30
        $ lustaddedB = 3
        call Challenger from _call_Challenger_31
        $ lustaddedB = 1
        call Challenger from _call_Challenger_32
        $ lustaddedB = 1
        call Challenger from _call_Challenger_33
        
    p "I should really go to sleep now, tomorrow is a school day..."
    jump SleepDay02
p "mmmh, what should I do?"
menu:
    "Go and help Nikki find her earrings" if (nikkihelp == True) and (hour <= 22) and (helpedsiswin == False):
        jump SisRoomEveningDay02
    "Do some heavy bodybuilding (+2hrs)" if (hour <= 22):    
        if (workout == True):
            "You already trained today."
            jump RyanRoomEveningDay02
        else:
            play music "Sounds/workoutgroan.mp3"
            $ renpy.movie_cutscene("Day1/bedroomworkout.ogv", delay=-1, loops=-1, stop_music=False)
            stop music
            scene ryanworkout01
            play sound "Sounds/panting.mp3"
            $ renpy.pause(2, hard=True)
            p "That was great, I can feel my muscles getting bigger and stronger already..."
            window hide
            $ strength += 1
            show strengthplus01:
                xalign 0.6 yalign 0.6
                linear 1.0 yalign 0.4
            play sound "Sounds/more.mp3"
            $ renpy.pause(3, hard=True)
            hide strengthplus01
            $ workout = True
            $ hour += 2 
            jump RyanRoomEveningDay02
    "Check the computer":
        jump ComputerEveningDay02
    "Admire my body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump RyanRoomEveningDay02
    "Read the book Laura gave you (+1hr)" if (book == True) and (bookread == False):
        jump RyanReadingEvening
    "Go somewhere else" if (hour >= 22):
        jump HouseChoiceEveningDay02
        
label ComputerEveningDay02:
scene ryancomputer with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label ComputerEveningDay02b:
scene ryancomputer
$ renpy.pause(1.0, hard=True)
menu:
    "Check the map":
        jump MapEveningDay02
    "Check the stats":
        jump StatsEveningDay02
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump ComputerEveningDay02b
    "Learn how to use the pendulum" if (pendulum == True) and (pendulumactive ==False):
        jump CompPendulumEveningDay02
    "Play a smutty game (+1hr)":
        jump CompGame
    "Turn the computer off":
        jump RyanRoomEveningDay02
    
label RyanReadingEvening:
scene ryanreading with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump RyanRoomEveningDay02

label CompPendulumEveningDay02:
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump ComputerEveningDay02b

label MapEveningDay02:
play sound "Sounds/mouseclick.mp3"
hide screen statsbackground
hide screen inventorybutton
hide screen calendar
show islandmap with dissolve
$ renpy.pause(1.0, hard=True)
if (discoverrandybeach == True):
    show randybeachmap
if (discoveraunthouse == True):
    show aunthousemap
if (discovergym == True):
    show gymmap
if (discoverschool == True):
    show schoolmap
if (discovermassage == True):
    show parlourmap
if (discoveraudacious == True):
    show audaciousmap
if (discoverstore == True):
    show storemap
if (discovertanya == True):
    show tanyamap
if (discoverteagan == True):
    show teaganmap
p "This shows all the places I know so far on Veri-Bosti Island..."
show screen statsbackground
show screen inventorybutton
show screen calendar
jump ComputerEveningDay02b

label StatsEveningDay02:
play sound "Sounds/mouseclick.mp3"
scene stats
hide screen statsbackground
hide screen inventorybutton
hide screen calendar
show screen statsscreen
$ renpy.pause(1.0, hard=True)
p "Time to check my progress against José's..."
hide screen statsscreen
show screen statsbackground
show screen inventorybutton
show screen calendar
jump ComputerEveningDay02b       

label CompGame:
scene ryancomputergame
$ renpy.pause(1.0, hard=True)
p "This game is tough. My fingers hurt like hell from so much clicking..."
$ hour +=1
jump ComputerEveningDay02b 
        
label SisRoomEveningDay02:
stop music
scene nikkibedroomhelp with dissolve
$ renpy.pause(1.0, hard=True)
$ locroom = False
$ nikkihelped = True
p "I came to help you find your earrings Nikki."
s "Oh goody! Are you going to lift that dresser then so we can have a look if they fell behind it?"
p "Sure, I'll try anyway: Be ready to sneak underneath and look for your earrings!"
p "Here we go..."
scene nikkibedroomhelpdresser with dissolve
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
if (strength <= 5):
    p "Damn...Too heavy...Can't...lift it!"
    s "You're not as strong as you think you are... I'll have to ask José to come and help me. You're just too weak...."
    window hide
    $ lust_points[17] -= 1
    $ score -= 1
    show lustminus01:
        xalign 0.05 yalign 0.4
        linear 1.0 yalign 0.6
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    p "This is so humiliating...I'll go back to my room."
    jump RyanRoomEveningDay02 
if (strength == 6) or (strength == 7):
    scene nikkibedroomhelpdresserwin with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Yes, I did it! Quick, look for your earrings Nikki, I don't know how long I can keep the dresser up in the air like that!"
    scene nikkibedroomearring with dissolve
    $ renpy.pause(1.0, hard=True)
    s "Oh, here they are! I found them, yippee!!!"
    p "Great, I can put the dresser back down again!"
    play sound "Sounds/workoutgroan.mp3"    
    $ renpy.pause(1.0, hard=True)
    $ helpedsiswin = True
    jump SisHappy
if (strength >= 8):
    scene nikkibedroomhelpdresserwin with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Yes, I did it! Quick, look for your earrings Nikki, I don't know how long I can keep the dresser up in the air like that!"
    s "Wow, I didn't realize you were so strong! Actually, a bit too strong... Have you been cheating by eating spinach again?"
    p "Don't be ridiculous, that's a cartoon trick, it doesn't work in real life!"
    s "Well, with the help of the Console, it might..."
    p "Come on, I would never use the Console. Cheating at a porn game is so LAME."
    s "Then, I have to say: Bye bye LAME CHEATER!"
    return

label SisHappy:
scene nikkibedroomhappy with dissolve
$ renpy.pause(1.0, hard=True)
s "Thank you, I found my earrings, I found my earrings!"
scene nikkibedroomkiss with dissolve
play sound "Sounds/kissing.mp3"
$ renpy.pause(1.0, hard=True)
window hide
$ lust_points[17] += 2
$ score += 2
show lust02:
    xalign 0.2 yalign 0.5
    linear 1.0 yalign 0.3
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
p "(Wow, she kissed me on the mouth... Time to make a move?)"
scene nikkibedroomsultry with dissolve
$ renpy.pause(1.0, hard=True)
s "Well, that was your reward... I think you liked it..."
label SisMenu:
menu:
    "Sure Nikki, your lips on my lips... It gave me a hardon.":
        s "I liked it too... But we can't do... it... We have a tenant-landlord relationship! And that is a definite no-no in any 3DCG game."
        s "And yew, you telling me about getting a hardon...."
        window hide
        $ lust_points[17] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.25 yalign 0.3
            linear 1.0 yalign 0.5
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump SisMenu        
    "Use the pendulum on her" if (pendulumactive == True) and (lust_points[17] >=8):
        jump SisPendulum
    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[17] >=8):
        play sound "Sounds/spray.mp3"
        $ renpy.pause(1.0, hard=True)
        jump SisPheromones
    "Wish her a good evening and leave":
        s "Bye [name], sweet dreams!"
        $ hour += 1
        jump RyanRoomEveningDay02   
        
label SisPendulum:
scene nikkibedroomhypno with dissolve
show pendulum03
$ renpy.pause(1.0, hard=True)
p "Just watch this pendulum as I wiggle it in front of your eyes Nikki..."
window hide
hide pendulum03
show pendulum02
$ renpy.pause(0.2, hard=True)
hide pendulum02
show pendulum01
$ renpy.pause(0.25, hard=True)
hide pendulum01
show pendulum02
$ renpy.pause(0.2, hard=True)
hide pendulum02
show pendulum03
$ renpy.pause(0.2, hard=True)
hide pendulum03
show pendulum04
$ renpy.pause(0.2, hard=True)
hide pendulum04
show pendulum05
$ renpy.pause(0.25, hard=True)
hide pendulum05
show pendulum04
$ renpy.pause(0.2, hard=True)
hide pendulum04
show pendulum03
$ renpy.pause(0.2, hard=True)
hide pendulum03
show pendulum02
$ renpy.pause(0.2, hard=True)
hide pendulum02
show pendulum01
$ renpy.pause(0.25, hard=True)
hide pendulum01
show pendulum02
$ renpy.pause(0.2, hard=True)
hide pendulum02
show pendulum03
$ renpy.pause(0.2, hard=True)
hide pendulum03
show pendulum04
$ renpy.pause(0.2, hard=True)
hide pendulum04
show pendulum05
$ renpy.pause(0.25, hard=True)
hide pendulum05
show pendulum04
$ renpy.pause(0.2, hard=True)
hide pendulum04
show pendulum03
p "You feel very sleepy... And you start dreaming... about fucking me..."
window hide
hide pendulum03
show pendulum02
$ renpy.pause(0.2, hard=True)
hide pendulum02
show pendulum01
$ renpy.pause(0.25, hard=True)
hide pendulum01
show pendulum02
$ renpy.pause(0.2, hard=True)
hide pendulum02
show pendulum03
$ renpy.pause(0.2, hard=True)
hide pendulum03
show pendulum04
$ renpy.pause(0.2, hard=True)
hide pendulum04
show pendulum05
$ renpy.pause(0.25, hard=True)
hide pendulum05
show pendulum04
$ renpy.pause(0.2, hard=True)
hide pendulum04
show pendulum03
$ renpy.pause(0.2, hard=True)
hide pendulum03
show pendulum02
$ renpy.pause(0.2, hard=True)
hide pendulum02
show pendulum01
$ renpy.pause(0.25, hard=True)
hide pendulum01
show pendulum02
$ renpy.pause(0.2, hard=True)
hide pendulum02
show pendulum03
$ renpy.pause(0.2, hard=True)
hide pendulum03
show pendulum04
$ renpy.pause(0.2, hard=True)
hide pendulum04
show pendulum05
$ renpy.pause(0.25, hard=True)
hide pendulum05
show pendulum04
$ renpy.pause(0.2, hard=True)
hide pendulum04
show pendulum03
hide pendulum03
play sound "Sounds/snap.mp3"
show pendulumsnapped
p "Shit, the pendulum snapped! I guess I won't be able to use it again..."
show pendulum
show square
play sound "Sounds/lost.mp3"
"You lost a hypnosis pendulum."
hide square
hide pendulum
$ pendulum = False
$ pendulumactive = False
if (lust_points[17] ==8):
    window hide
    $ lust_points[17] += 2
    $ score += 2
    show lust02:
        xalign 0.2 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    show epiclust:
        xalign 0.25 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    jump SisFuck
if (lust_points[17] ==9):
    window hide
    $ lust_points[17] += 1
    $ score += 1
    show lust01:
        xalign 0.2 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    show epiclust:
        xalign 0.25 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    jump SisFuck

label SisPheromones:
scene nikkibedroompheromone with dissolve
$ pheromone = False
play sound "Sounds/sniffing.mp3"
$ renpy.pause(1.0, hard=True)
s "Oh, it smells funny... And it's making me so horny at the same time..."
p "My spray is now empty... I guess I won't be able to use it again."
show pheromone
show square
play sound "Sounds/lost.mp3"
"You lost a pheromone spray."
hide square
hide pheromone
$ pheromone = False
if (lust_points[17] ==8):
    window hide
    $ lust_points[17] += 2
    $ score += 2
    show lust02:
        xalign 0.2 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    show epiclust:
        xalign 0.2 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    jump SisFuck
if (lust_points[17] ==9):
    window hide
    $ lust_points[17] += 1
    $ score += 1
    show lust01:
        xalign 0.2 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    show epiclust:
        xalign 0.2 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    jump SisFuck

label SisFuck:
stop music
scene nikkibedroomsultry with dissolve
$ renpy.pause(1.0, hard=True)
s "Maybe you deserve a bigger reward [name]... I've noticed how you... seem to lust after me..."
if (stamina <= 0) and (whitebull == False):
    p "Err, you know what, I'm like, having little, nothing to worry of course,... urinary problems right now, let's put this off until tomorrow."
    s "Eeew. I didn't want to know that! OK, go back to your room and sort that useless floppy wiener issue FAST!"
    $ hour += 1
    jump RyanRoomEveningDay02
if (stamina <= 0) and (whitebull == True):
    p "Definitely the right time to drink that energy drink, my libido is too low and it would be ssoo embarrassing if I couldn't perform..."
    show whitebull
    show square
    play sound "Sounds/lost.mp3"
    "You drank an energy drink. The bottle is now empty."
    hide square
    hide whitebull
    $ stamina += 2
    jump SisUndress01
label SisUndress01:    
scene nikkiundress01 with dissolve
$ renpy.pause(1.0, hard=True)
s "That's what you've been dying to see, my huge tits, haven't you? They've grown ssoo much in the last couple of years!"
p "Oh, Nikki, they are simply sumptuous, so large and round and firm..."
scene nikkiundress02 with dissolve
$ renpy.pause(1.0, hard=True)
s "Now it's your turn to show me that great big monster cock I know you're hiding down there..."
p "Sure, my hardon is about to tear a hole through my shorts! Let me carry you over to the bed Nikki..."
scene nikkiundress03 with dissolve
play sound "Sounds/sisomg.mp3"
$ renpy.pause(1.0, hard=True)
s "Mmmh, you're so strong... and hung... What are you going to do to poor little me?"
label SisFuckChoices:
menu:
    "Maybe we should start off with a gentle blowjob." if (sisblowjob == False):
        jump SisBlowjob
    "How about I lick your pussy to get it nice and wet?" if (sispussy == False):
        jump SisPussy
    "I'm gonna pound that arse of yours to oblivion!" if (sisanal == False):
        jump SisAnal
    "Let's fuck, like, for real!" if (sisall == 3):
        if (nikkijosewin == False):
            $ nikkiwin = True
        jump SisRealFuck

label SisPussy:
scene nikkilick01 with dissolve
$ sisall += 1
play music "Sounds/lick.mp3"
$ renpy.pause(1.0, hard=True)
$ sispussy = True
s "Oh, God, you're so good at this, I'm cumming!, AAAHH!"
s "Thanks [name], I really needed that... Now it's my turn to pleasure that rock-hard donkey-sized cock of yours!"
stop music
jump SisFuckChoices

label SisBlowjob:
scene nikkiblowjob01 with dissolve
$ sisall += 1
$ renpy.pause(1.0, hard=True)
$ sisblowjob = True
p "Ready to get your mouth stretched Nikki?"
s "gmmuumpfff..."
p "I'll take that as a yes."
play sound "Sounds/sisblowjob.mp3"
scene nikkiblowjob02
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.3, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob02
$ renpy.pause(0.2, hard=True)
scene nikkiblowjob01
$ renpy.pause(0.2, hard=True)
p "Fuck, I'm getting close to blowing my load!"
if (stamina >= 2):
    menu:
        "Blow your load":
            jump SisBlowjobCum
        "Don't blow your load":
            jump SisFuckChoices
else:
    s "Keep that hardon, I want you to fuck me with your huge cock!"
    p "Phew, that was ssoo close..."
    jump SisFuckChoices

label SisBlowjobCum:
scene nikkiblowjobcum01 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "Fuck, it's streaming out like a faucet!"
s "Mmmh, yes, cover my body in your hot sticky load [name]!"
scene nikkiblowjobcum02 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
window hide
$ stamina -=1
show staminaminus01:    
    xalign 0.2 yalign 0.2   
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
s "Wow, I've never seen that much cum in my life, I'm totally drenched in it! Will you be able to go again after such a massive load [name]???"
p "Sure, I'm still hard as rock, let's move on to the main course!"
jump SisFuckChoices

label SisAnal:
scene nikkianal01 with dissolve
$ sisall += 1
$ backdoor += 1
play sound "Sounds/threesomefuck.mp3"
$ renpy.pause(1.0, hard=True)
$ sisanal = True
s "Be gentle [name], you're too rough!"
p "Sorry, I got carried away, your arse is so warm and tight... Let's switch position."
stop sound
jump SisFuckChoices

label SisRealFuck:
stop music
play music "Sounds/sisfuck.mp3"
show movienikkifuck
show cum
call screen sisfuckcum
screen sisfuckcum:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("SisFuckCum01")

label SisFuckCum01:
stop music
hide movienikkifuck
scene nikkifuckcum01
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
s "OMG, you're filling my pussy to overcapacity! Pull it out and cover my body with your giant load!"
scene nikkifuckcum02 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "SSooo good... I really busted a nut there Nikki, you were great..."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
s "I'm gonna need to take a shower and clean my sheets without Nancy noticing all your sticky mess... Mmmh, it's so delicious..."
s "You'd better leave [name], we don't want to get caught by Nancy..."
$ nikkifucked = True
$ hour += 1
jump RyanRoomEveningDay02

label HouseChoiceEveningDay02:
stop music
p "Where should I go at this time of the evening?..."
menu:
    "Go to Nancy's room" if (nightmomroomseen02 == False):
        jump MomUndressing01
    "Go to Nikki's room" if (nightsisroomseen02 == False):
        jump SisRoomNightDay02 
    "Go to the bathroom" if (nightshowerseen02 == False):
        jump BathroomEveningDay02
    "Go back to my room" if (locroom == False):
        jump RyanRoomEveningDay02   

label SisRoomNightDay02:
scene nikkibedroomnight with dissolve
$ renpy.pause(1.0, hard=True)
$ locroom = False
p "Nikki isn't in her room... I wonder where she went..."
$ nightsisroomseen02 = True
jump HouseChoiceEveningDay02

label BathroomEveningDay02:
play music "Sounds/shower.mp3"
$ locroom = False
scene bathroomdoorclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "Someone's taking a shower..."
label BathroomEveningDay02b:
menu:
    "Use lubricant on the door hinges" if (wd69 == True) and (squeakfixed == False):
        "The door should not squeak anymore."
        $ squeakfixed = True
        jump BathroomEveningDay02b        
    "Have a peek":
        jump PeekBathroomEvening02
    "Leave":
        jump HouseChoiceEveningDay02

label PeekBathroomEvening02:
if (squeakfixed == False):
    play sound "Sounds/doorsqueak.mp3"
    scene bathroomdooropen with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Shit, the door is squeaking..."
    s "Hey, I'm in the shower, don't get in!"
    p "Ah, sorry Nikki...I'm leaving..."
    p "Damn, I should try and find a way of stopping that door from squeaking if I want to spy on Nancy or Nikki in the shower like every other MC..."
    jump HouseChoiceEveningDay02
if (squeakfixed == True):
    scene nikkishower01 with dissolve
    $ renpy.pause(1.0, hard=True)
    if (sisshowerpeep == False):
        $ peeping += 1
    $ sisshowerpeep = True
    p "Cool, she didn't hear me come in, I can see her naked in the shower now..."
    menu:
        "Get closer, it's dangerous but I'm crazy with lust for her!":
            jump SisShower02
        "Admire the view a little longer then leave":
            jump RyanRoomEveningDay02
    
label SisShower02:
scene nikkishower02 with dissolve
$ renpy.pause(1.0, hard=True)
if (nikkiwin == False):
    s "What the hell are you doing here, EEK!"
    $ lust_points[17] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.35 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01    
    p "Err... I didn't know there was someone in here, sorry... We really need to get a lock on that bathroom door I say!"
    s "Get out of here or I'll tell mom you're spying on me!"
    jump RyanRoomEveningDay02
if (nikkiwin == True): 
    s "[name]! It's not because we... did it, that you have the right to barge in on me taking a shower like that!"
    p "Oh, come on, how about we do it in the shower stall... Mmmh? wanna another taste of my massive cock?"
    s "Get the hell out of here! You're just a pervert, I knew it, I should never have allowed this to happen!"
    p "Pff, women! One moment they're bouncing up and down your hard shaft, the next minute they're all prude and shit... It's not fair."
    jump RyanRoomEveningDay02

label MomUndressing01:
stop music
$ nightmomroomseen02 = True
$ locroom = False
scene nancybedroomclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "The door is locked but I can see some light poking through the keyhole."
menu:
    "Look through the keyhole":
        jump MomUndressing01b
    "Leave and go back to my room":
        jump RyanRoomEveningDay02
        
label MomUndressing01b:
scene nancyundressing01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Nancy is sitting on her bed. She looks like she's thinking about doing something..."
p "More landlady blueballing on the way for you guys it seems... What should I do?"
menu:
    "Why do you even ask? Look on of course!":
        jump MomUndressing02
    "I feel dirty watching Nancy like that. Go back to my room and cry into my pillow":
        jump RyanRoomEveningDay02

label MomUndressing02:
play music "Sounds/sneaky.mp3"
scene nancyundressing02 with dissolve
$ renpy.pause(1.0, hard=True)
p "She's taking her silk gown off... Nice, she's about to change then."

scene nancyundressing03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oh yeah, she switched panties and now she's half naked, I can see her huge tits."

scene nancyundressing04 with dissolve
$ renpy.pause(1.0, hard=True)
p "She's putting on some sexy lingerie. I hope she's not waiting for a suitor."

scene nancyundressing05 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, I hope she doesn't just fall asleep and that's the end of it... Still, what an arse!"

scene nancyundressing06 with dissolve
$ renpy.pause(1.0, hard=True)
p "She's reaching into her drawer for something..."

if (dildo == True):
    scene nancyundressing06b with dissolve
    $ renpy.pause(1.0, hard=True)
    p "I guess she was looking for her dildo. Of course, she can't find it cos I took it and now she's perplexed and wondering where a huge black dildo could have disappeared..."
    scene nancyundressing06c with dissolve
    $ renpy.pause(1.0, hard=True)
    p "And now she turned the lights off and she's going to sleep, and I'm a fucking idiot for snooping around in her room... The show's over, time to leave."
    jump RyanRoomEveningDay02

scene nancyundressing07 with dissolve
$ renpy.pause(1.0, hard=True)
$ seenmomundressingfullday02 = True
p "Ah, I see, her \"suitor\" is called mr Big Black Dildo..."

scene nancyundressing08a with dissolve
$ renpy.pause(1.0, hard=True)
p "She's sticking it right up her poop chute..."
play sound "Sounds/katewank.ogg"
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene nancyundressing08a
$ renpy.pause(0.5, hard=True)
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene nancyundressing08a
$ renpy.pause(0.5, hard=True)
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene nancyundressing08a
$ renpy.pause(0.5, hard=True)
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene nancyundressing08a
$ renpy.pause(0.5, hard=True)
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene nancyundressing08a
$ renpy.pause(0.5, hard=True)
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene nancyundressing08a
$ renpy.pause(0.5, hard=True)
play sound "Sounds/womansigh.mp3"
scene nancyundressing08c with dissolve
$ renpy.pause(1.0, hard=True)
window hide
$ lust_points[16] +=1
$ score += 1
show lust01:
    xalign 0.6 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
p "I think I heard her say my name while she was creaming all over her huge dildo... Wish it was my cock instead."
p "Probably best to leave now, I don't want to be seen peeping through Nancy's keyhole like that."    
$ hour +=1
stop music
jump RyanRoomEveningDay02    

label SleepDay02:
scene ryansleeping with dissolve
play music "Sounds/ryansnoring.mp3"
$ renpy.pause(1.0, hard=True)
"You fall asleep and dream of your adventures to come..."
$ renpy.pause(2.0, hard=True)

"Your current score (not that it matters) is: {b}[score]{/b}"
if (score <=45):
    "Your ranking: {b}Douchebag{/b}"
elif (score <=52):
    "Your ranking: {b}Noob{/b}"
elif (score <=59):
    "Your ranking: {b}Average Joe{/b}"
elif (score <=66):
    "Your ranking: {b}Hunk{/b}"
else:
    "Your ranking: {b}Babe Magnet{/b}"
stop music
window hide

jump Day03








                
                
                
                
                
        
                
                                                      
        
        
    
            
    




