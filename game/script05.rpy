label Day05:
# reboot variables
$ day = 5
$ hour = 7
$ stamina = 5
$ wentforjog = False
$ longjog = False
$ shortjog = False
$ evictedfromstore = False
$ quentinnotfriends = False
$ locswimmingpool = False
$ audacioustried = False
$ evictedfromshop = False
$ shoppingseen = False
$ katephotoplanned05 = False
$ katephotoshoot05 = False
$ katephotoshootleft05 = False
$ downtowntipgiven = False
$ workout = False
$ pretendshop = False
$ challengercalls = 0
$ principaltits = False
$ principalback = False
$ friedaride = False
$ friedaarse = False
$ teaganpussy = False
$ teaganfeet = False
$ busbeach = False
$ bustown = False
$ bushome = False

stop music
play sound "Sounds/yawning.mp3"
scene ryanyawning with dissolve
$ renpy.pause(1.0, hard=True)
p "Yet another beautiful day... Filled with hot steamy sex hopefully!"
scene ryanbedroomday with dissolve
$ lustaddedB = 2
call Challenger from _call_Challenger_62
$ lustaddedB = 1
call Challenger from _call_Challenger_63
$ challengercalls += 2

label MorningDay05b:
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "What should I do?"
menu:
    "Put on a black tank top" if (tanktop == True):
        p "Yeah, I'm ready to be a goth. Or a rebel. Or just someone with terrible tastes."
        $ blacktop05 = True
        jump MorningDay05b
    "Take a shower":
        jump ShowerMorningDay05
    "Go for breakfast":
        jump BreakfastDay05
    "Check the computer":
        jump ComputerMorningDay05
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump MorningDay05b
        
label ComputerMorningDay05:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label ComputerMorningDay05b:
scene ryancomputerday
menu:
    "Check the map":
        jump MapMorningDay05
    "Check the stats":
        jump StatsMorningDay05
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump ComputerMorningDay05b
    "Turn the computer off":
        jump MorningDay05b

label MapMorningDay05:
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
if (discovergym == True):
    show gymmap
if (discovercabin == True):
    show cabinmap
if (discoverclinic == True):
    show clinicmap
if (discoverfalls == True):
    show waterfallsmap
p "This shows all the places I know so far on Veri-Bosti Island..."
show screen statsbackground
show screen inventorybutton
show screen calendar
jump ComputerMorningDay05b

label StatsMorningDay05:
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
jump ComputerMorningDay05b

label ShowerMorningDay05:
scene nikkishowermorning01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oops, Nikki is in the bathroom, but it's not my fault this time, she left the door open..."
if (nikkifucked == True):
    p "Let's have a bit of fun, I'll walk behind her and grab her funbags."
    scene sismorning01day05 with dissolve
    $ renpy.pause(1.0, hard=True)
    s "Hey! What are you doing [name]?"
    p "I think we have time for a bit of fun... don't you?"
    scene sismorning02day05 with dissolve
    $ renpy.pause(1.0, hard=True)
    s "I was about to take my shower, so we don't really have time... I guess you could shower with me though... I'll close the bathroom door..."
    scene sismorning03day05 with dissolve
    play music "Sounds/shower.mp3"
    $ renpy.pause(1.0, hard=True)
    p "Let's clean each other out, I'll clean your fat titties and you clean my hot rod..."
    s "This is so wrong... And so exciting at the same time... But let's not go too far, mom could hear us..."
    p "What if she does? Maybe it's time she knows the truth... That housematecest is best and that threesome housematecest is even better!"
    s "Not yet [name], not yet... Now play with my nipples... Mmmh..."
    jump BreakfastDay05b        
if (nikkifucked == False):
    p "Hi Nikki, good morning!"
    scene sismorning04day05 with dissolve
    $ renpy.pause(1.0, hard=True)
    s "What are you doing here? Can't you see I'm using the bathroom?..."
    p "Well... err... yeah, sure, but we could use it together at the same time to save time?"
    s "That's ridiculous! Get out of here and wait for your turn [name]."
    jump BreakfastDay05
    
label BreakfastDay05:
scene nancyyoga01 with dissolve
play music "Sounds/yoga.mp3"
$ renpy.pause(1.0, hard=True)
p "Nancy is doing her morning exercises... She hasn't seen me yet..."
scene nancyyoga02 with dissolve
$ renpy.pause(3.0, hard=True)
scene nancyyoga03 with dissolve
$ renpy.pause(3.0, hard=True)
scene nancyyoga04 with dissolve
$ renpy.pause(1.0, hard=True)
m "Oh, good morning sweetie. You're a bit early for breakfast,I'm still doing my yoga, maybe you'd like to join?"
p "Sure Nancy!"
m "Just watch me and do as I do then..."
scene momyoga05 with dissolve
$ renpy.pause(3.0, hard=True)
m "Good...Now a bit harder..."
scene momyoga06 with dissolve
$ renpy.pause(3.0, hard=True)
p "Wow, she's really flexible. I wish I had huge tits that I could just shove in my face like that...)"
m "And finally, can you do that?"
scene momyoga07 with dissolve
$ renpy.pause(3.0, hard=True)
p "Err.. Not really, I'm stuck."
m "Maybe your muscles are just too big for such a delicate art as yoga... Go and take a quick shower, I'll prepare breakfast."
p "OK Nancy. (Damn, my muscles are too huge now? Women, they never know what they want...)"

label BreakfastDay05b:
stop music
scene breakfastday03a
if (blacktop05 == True):
    show breakfastday03ablack
$ renpy.pause(1.0, hard=True)
$ hour += 1
m "Anna called me last night and we are invited to the Longrods tonight for dinner at 8pm."
show breakfastday03c
s "Will José be there too?"
show breakfastday03b
m "Of course, Nikki. And Anna told me we could relax in their indoor swimming pool after eating, so don't forget your swimsuits!"
window hide
$ discoveranna = True
show addedlocation:
    xalign 0.4 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide addedlocation
hide breakfastday03b
hide breakfastday03c
p "Umpf... I don't mind seeing Anna again, but that douchebag..."
m "You'd better behave yourself tonight, I'm warning you!"
if (pocketmoney2 == True):
    m "Here's some pocket money for the day Nikki, 5 dollars. For you [name], nothing, since you are still punished for what you did yesterday!"
    m "Now eat up so you two can get to school on time."
if (pocketmoney2 == False):
    m "Here's some pocket money for the day, five dollars each."
    $ money += 5
    show breakfastday03c
    s "Yeah, thanks mom!"
    p "Thanks Nancy!"
    m "Don't spend it on anything silly! Now eat up so you two can get to school on time."
    hide breakfastday03c
s "Sure mom, I'll leave a bit early, I'm going to Chantelle to pick her up and walk with her to school."
p "I know the way now, I'll be fine... I think."

label ClassRoomDay05:
scene classroomarrival with dissolve
$ renpy.pause(1.0, hard=True)
$ hour += 1
p "Uh, Uh, it seems I'm late... I can't hear the usual morning chatter."
if (maddysaved == True):
    scene classhappyday05 with dissolve
    $ renpy.pause(1.0, hard=True)
    t "Ah, here's our hero who saved Maddy!"
    play sound "Sounds/clapping.mp3"
    t "Unfortunately, Maddy is not here to celebrate with us today as she is being taken care of by social workers until she recovers from her ordeal."
    t "We expect her back tomorrow. Thanks to your bravery [name]!"
    if (lust_points[22] <= 8):
        $ score += 1
        $ lust_points[22] +=1
        show lust01:
            xalign 0.2 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
    fr "Thank you for saving meine best friend [name]!"
    if (lust_points[8] <= 8):
        $ score += 1
        $ lust_points[8] +=1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
    t "Now go and sit at your desk, we need to get on with the lesson."
    jump LessonDay05

if (maddysaved == False):
    scene classangryday05 with dissolve
    $ renpy.pause(1.0, hard=True)
    t "You're late [name]! And I do not tolerate students who are late! Detention for you today!"
    $ detention05 = True
    if (lust_points[22] <= 9):
        $ score -= 1
        $ lust_points[22] -=1
        show lustminus01:
            xalign 0.2 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
    p "(What? I just arrived, I followed the normal path to school, why am I late godamn dev?)"
    t "Stop mumbling to yourself and go and sit at your desk at once!"
    scene classpray05 with dissolve
    $ renpy.pause(1.0, hard=True)
    t "Unfortunately, Maddy is still missing. Let's stand and pray that our beloved police officers will soon find her safe and sound so she can rejoin us. Amen."
    p "(They'd better. I still haven't had a chance to fuck her...)"
    play sound "Sounds/sobbing.mp3"
    fr "I am zo worried...."
    t "Keep your spirits up Frieda. Veri-Bosti's police force is well trained in dealing with such cases. It seems our island attracts all sorts of weird perverts..."

label LessonDay05:
scene classroomday05 with dissolve
t "Let's get back to work. We'll continue the French lesson we started earlier this week."
t "Who can conjugate the verb \"to be\" in French for me?"
q "Me me me!"
p "What a nerd... This is boring. Let's daydream about naked MILFs instead shall we?"
menu:
    "Daydream about Teagan":
        jump DayDreamTeaganDay05
    "Daydream about Sophia":
        jump DayDreamSophiaDay05
    "Daydream about Viviane":
        jump DayDreamVivianeDay05
    "Daydream about Maria":
        jump DayDreamMariaDay05
        
label DayDreamTeaganDay05:
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
scene lesson01 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
p "Ah, fuck, right when she was about to virtually suck me..."
jump LessonEndDay05

label DayDreamSophiaDay05:
play sound "Sounds/dreaming.mp3"
scene dreamsophia01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
so "There's only one thing you can do to stop me from expelling you from this school [name]..."
p "Yeah? And what is that?"
scene dreamsophia02 with dissolve
$ renpy.pause(3.0, hard=True)
so "You need to FUCK ME HARD with your massive ramrod..."
p "I'm ready Ms Titstworthy! Just bend over some more and open wide..."
scene dreamsophia03 with dissolve
$ renpy.pause(3.0, hard=True)
so "And then I want you to FLOOD my holes with huge yummy loads of young cream, understood?"
p "I'll give it to you everyday Mrs Titswo..."
stop music
scene lesson01 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
p "Damn! Just as I was about to drench her with a virtual shower of spunk!..."
jump LessonEndDay05

label DayDreamVivianeDay05:
play sound "Sounds/dreaming.mp3"
scene dreamviviane01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
vi "It's so warm in here... I ABSOLUTELY need to take my bikini top off... Hope you don't mind?"
p "Of course not... I was actually wondering why you were wearing a bikini in the classroom..."
scene dreamviviane02 with dissolve
$ renpy.pause(3.0, hard=True)
vi "I just came out of the jacuzzi that's why... The hot water made me so.. HORNY!"
p "I'm getting horny too baby...Come and suck on my fat knob!"
scene dreamviviane03 with dissolve
$ renpy.pause(3.0, hard=True)
vi "Oooh, I can tell it's really HUGE [name]... The BIGGEST, most beautiful young FUCKMEAT I've ever seen!"
p "All for you Viviane, I'll fuck you so ha..."
stop music
scene lesson01 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
p "Why does the bell always ring right before I'm about to fuck my dreamgirl? Fucking sadistic dev..."
jump LessonEndDay05

label DayDreamMariaDay05:
play sound "Sounds/dreaming.mp3"
scene dreammaria01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
ma "I bet you're the type who likes library gals with glasses slowly undressing for you..."
p "You can read me like an open book Maria..."
scene dreammaria02 with dissolve
$ renpy.pause(3.0, hard=True)
ma "And that book is a very NAUGHTY book I can tell..."
p "Yes, with a very HARD cover!"
scene dreammaria03 with dissolve
$ renpy.pause(3.0, hard=True)
ma "I'd like an IN-DEPTH report on that book young man. RIGHT NOW!"
p "You bet, it will be REALLY in-dep..."
stop music
scene lesson01 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
p "Damn bell! This dream counts as educative, right?..."
jump LessonEndDay05

label LessonEndDay05:
$ hour += 1
t "Alright, we'll take a short break but be back in ten minutes everyone!"
if (deliveryboy == True):
    scene teacherenter with dissolve
    $ renpy.pause(1.0, hard=True)
    t "[name], I would need some groceries delivered this evening. Could you pick them up and bring them to my place at 7pm please?"
    menu:
        "Err... no, I have something planned at that time...":
            t "Hu. How disappointing."
            if (lust_points[22] <= 9):
                $ lust_points[22] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.5 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
        "Of course Miss Cocque, I'll make sure to bring them over.":
            $ teagangrocery05 = True
            t "That's a good boy."

stop music
play music "Sounds/lockersound.mp3"
scene locker with dissolve
$ renpy.pause(1.0, hard=True)
p "Quentin is there again, right in front of my locker..."
p "What's up Quentin? Any tips for me?"
q "I knew you were going to ask that! And that is precisely why I'm here. Again."
p "OK, well spill it out then!"
q "You want to beat José? Well, listen very carefully..."
if (quentintipfrancine == False):
    q "Ah ah! I know for a fact that Francine loves pole-dancing and practices it wherever and whenever she can."
    p "Mmh, interesting. Thanks for the tip Quentin."
    $ quentintipfrancine = True
scene fire01 with dissolve
stop music
play sound "Sounds/firealarm.mp3"
$ renpy.pause(1.0, hard=True)
p "Shit, what the hell is going on?"
scene fire01b with dissolve
play sound "Sounds/firealarm.mp3"
$ renpy.pause(1.0, hard=True)
q "It's the fire alarm, we need to leave the building immediately by following the emergency procedure delta-B-16! Quick, come with me!"
scene fire02 with dissolve
play sound "Sounds/firealarm.mp3"
$ renpy.pause(1.0, hard=True)
p "(People are panicking. Well, girls mostly. I can't die, I'm the MC, right?)"
menu:
    "Follow Quentin":
        jump FireQuentin
    "Talk to Frieda":
        jump FireFrieda
    "Talk to Kate":
        jump FireKate

label FireQuentin:
if (blacktop05 == True):
    scene firequentin01black with dissolve
else:
    scene firequentin01 with dissolve 
play music "Sounds/fire.mp3"
play sound "Sounds/firealarm.mp3"
$ renpy.pause(1.0, hard=True)
q "So... Err... Follow corridor H13 and turn left on corridor B3. Or is it right?"
p "Get your act together buddy, or we're both gonna DIE!"
q "Looks like the fire broke out at the back of the school. Then, it's procedure Echo-C-2! I know the way for this one!"
p "(Jeezus, what a tool. He took us right into the middle of the burning furnace!)"
stop music
if (blacktop05 == True):
    scene firequentin02black with dissolve
else:
    scene firequentin02 with dissolve    
play sound "Sounds/policesound.mp3"
$ renpy.pause(1.0, hard=True)
so "Where the hell did you two go? You got us all very worried of losing our best student and... err... you [name]."
q "I followed emergency procedure delta-B-16 Ms Titsworthy, but we soon encountered a snag, so I reverted to emergency procedure echo-C-2..."
t "Thank God you made it out alive!"
q "We discovered that the fire broke out at the back of the school..."
so "Is that so? Interesting... I know only of those filthy goths that hang out all the time at the back of our school..."
so "Where is this dreadful goth Damian? Anyone seen him? I need to talk to him IMMEDIATELY!"
jump FireDamian01

label FireFrieda:
scene firefrieda01 with dissolve
play sound "Sounds/firealarm.mp3"
$ renpy.pause(1.0, hard=True)
fr "ALARM! HILFE! ACHTUNG!"
p "Let me carry you to safety Frieda!"
play sound "Sounds/firealarm.mp3"
$ renpy.pause(1.0, hard=True)
fr "Run [name], I can smell the stench of burning bodies, the fire is real close!"
p "That's what your grandfather used to say..."
"On behalf of the development team, we would like to apologize for this terribly insensitive joke from the MC."
fr "Take us to the library, we'll be safe there, I know the way, I go there every day..."
scene firefrieda02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Phew, we made it. Thanks to me and my huge muscles."
fr "And your huge cock. I could feel it underneath me supporting my whole body weight. It's actually sticking out right now [name]."
p "Err. Ah, yes, I was having this dream earlier and..." 
if (lust_points[8] == 9):
    $ lust_points[8] +=1
    $ score += 1
    show lust01:
        xalign 0.2 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[8] == 8):
    $ lust_points[8] +=2
    $ score += 2
    show lust02:
        xalign 0.2 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02 
if (lust_points[8] <= 7):
    $ lust_points[8] +=3
    $ score += 3
    show lust03:
        xalign 0.2 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust03 
if (lust_points[8] == 10) and (friedafucked == False):
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    fr "This feuer has unleashed the fire within me! Come, follow me [name], I want you to FUCK ME!"
    jump FriedaFuckMorningDay05
fr "It is disgusting! Let me doww and let's go back to the entrance."
p "Alright, it's my fault for not being able to reach epiclust with you."
jump FireEnd

label FriedaFuckMorningDay05:
scene friedafuck01 with dissolve
$ renpy.pause(1.0, hard=True)
fr "Rrr, I'm like a pussycat! Follow me [name]! And take your clothes off, schnell!"
p "Sure, You too, take that top and your shorts off please, I'm so horny for you Frieda!"
scene friedafuck02 with dissolve
$ renpy.pause(1.0, hard=True)
fr "Hurry up, the librarian might come and I don't want to be expelled from this school. My parents vould kill me!"
p "I'm getting everything off as fast as I can! Let's go into the corner..."
scene friedafuck03 with dissolve
$ renpy.pause(1.0, hard=True)
fr "Was ist das, mein Gott! Are you rubbing your very BIG cock between my asscheeks naughty boy!"
p "Yeah I am, you're driving me crazy..."
scene friedafuck04 with dissolve
$ renpy.pause(1.0, hard=True)
fr "Rub it against mein arse, STUD! I want to feel how HUGE and HARD it is!"
label MorningFriedaCockRubDay05:
play sound "Sounds/friedaback.mp3"
scene friedafuck04b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04 with dissolve
$ renpy.pause(0.3, hard=True)
fr "Faster, SCHNELL! Ah, it's ssoo BIG!"
play sound "Sounds/friedaback.mp3"
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
menu:
    "Repeat":
        jump MorningFriedaCockRubDay05
    "Move on":
        pass
p "You liked that Frieda? My cock is like a bar of iron cos your hot bod is driving me insane!"

scene friedafuck05 with dissolve
$ renpy.pause(1.0, hard=True)
fr "I can see that, it's bigger than my arm! I don't know if mein poor pussy can take it, but I'm so wet and ready for you..."
p "Let's find out... Bend over and open wide..."
scene friedafuck06 with dissolve
$ renpy.pause(1.0, hard=True)
p "...I'm coming in! FUCK YEAH!"
fr "AAAH, ssooo wunderbar! Fuck me harder!"
scene friedafuck07 with dissolve
$ renpy.pause(1.0, hard=True)
p "Of course, I'm gonna pound you into the ground baby!"
fr "FUCK!!! AAAH! Too... too much! You're too deep!"
p "It's never too deep, your pussy can take it, but you have to stop screaming Frieda!"
scene friedafuck08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Like that, that's better..."
fr "Mm....mmmm....."
play sound "Sounds/friedafuck.mp3"
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
p "Just enjoy the feel of my massive teenage cock deep inside of you..."
menu:
    "Let her ride you" if (friedaride == False):
        jump MorningFriedaFuckRideDay05
    "Take her up the arse" if (friedaarse == False):
        jump MorningFriedaFuckArseDay05
    "Tell her to finish you off with a blowjob" if (friedaarse == True) and (friedaride == True):
        jump MorningFriedaFuckBlowjobDay05

label MorningFriedaFuckRideDay05:
scene friedaup with dissolve
$ renpy.pause(1.0, hard=True)
fr "Let me insert that cum-missile myself..."
p "Sure, do as you please Frieda, it's all yours!"
fr "OOOOh, it's zzooo big... (puff)... Ein bißchen mehr...."
scene friedafuck09 with dissolve
$ friedaride = True
$ renpy.pause(1.0, hard=True)
fr "Mein Gott! I can feel your huge cock so deep inside of me... I can touch it with my hands from outside!"
p "Well, it does have a certain volume..."
fr "It is ENORMOUS! (puff) I don't think I can take much more of it zat way..."
p "Let's switch position then..."
menu:
    "Take her up the arse" if (friedaarse == False):
        jump MorningFriedaFuckArseDay05
    "Tell her to finish you off with a blowjob" if (friedaarse == True) and (friedaride == True):
        jump MorningFriedaFuckBlowjobDay05

label MorningFriedaFuckArseDay05:
scene friedafuck10 with dissolve
$ friedaarse = True
$ renpy.pause(1.0, hard=True)
fr "You are stretching my poor little anus zo much! AAAAH!"
p "That's nothing, I'm not even halfway in. Let me stretch it a bit more..."
scene friedafuck10b with dissolve
$ renpy.pause(1.0, hard=True)
p "There. That's better. A solid ten inches of my ramrod up your arse!"
fr "Be caref.."
label MorningFriedaFuckArseDay05b:
play sound "Sounds/friedaarse.mp3"
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump MorningFriedaFuckArseDay05b        
    "Let her ride you" if (friedaride == False):
        jump MorningFriedaFuckRideDay05
    "Tell her to finish you off with a blowjob" if (friedaarse == True)and (friedaride == True):
        jump MorningFriedaFuckBlowjobDay05

label MorningFriedaFuckBlowjobDay05:
stop music
play music "Sounds/friedaslow.mp3"
show friedafuckslow
show faster
call screen morningfriedafuckslowday05
screen morningfriedafuckslowday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MorningFriedaFuckFastDay05")

label MorningFriedaFuckFastDay05:
hide faster
play music "Sounds/friedafast.mp3"
show friedafuckfast
show cum
call screen morningfriedafuckfastday05
screen morningfriedafuckfastday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MorningFriedaFuckCumDay05")

label MorningFriedaFuckCumDay05:
hide friedafuckfast
hide friedafuckslow
stop music
scene friedacum01
play sound "Sounds/imcumming.mp3"
$ renpy.pause(3.0, hard=True)
fr "Glurb... mmmh..."
scene friedacum02 with dissolve
play sound "Sounds/imcumming02.mp3"
$ renpy.pause(2.0, hard=True)
fr "You are coming ssooo much. Wunderbar!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
if (friedafucked == True):
    fr "But we need to get dressed. And cleaned up..."
    p "Yes, that is probably a good idea. They are probably looking for us."
    $ fuckedschoolgirlday05 = True
    $ hour += 1
    scene firefrieda03 with dissolve
    $ renpy.pause(1.0, hard=True)
    fi "Hey, I found them! They were... err... hiding in the library."
    jump FireEnd
$ friedafucked = True
$ backdoor += 1
if (katefucked == True) and (maddyfucked == True) and (laurafucked == True) and (achievement.has("classroom") == False):
    show achievement03:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement03
    $ achievement.grant("classroom")
fr "But we need to get dressed. And cleaned up..."
p "Yes, that is probably a good idea. They are probably looking for us."
if (friedajosewin == False):
    $ friedawin = True
    p "(José is going to be mightily pissed off when he gets the pic I'm sending him...)"
$ fuckedschoolgirlday05 = True
$ hour += 1
scene firefrieda03 with dissolve
$ renpy.pause(1.0, hard=True)
fi "Hey, I found them! They were... err... hiding in the library."
jump FireEnd

label FireKate:
scene firekate01 with dissolve
play sound "Sounds/firealarm.mp3"
$ renpy.pause(1.0, hard=True)
k "Oh my God, my hair is going to get all smoky and the pageant is TOMORROW!"
p "Get yourself together Kate! I'll take you to safety, follow me!"
if (blacktop05 == True):
    scene firekate02black with dissolve
else:
    scene firekate02 with dissolve 
play music "Sounds/fire.mp3"
play sound "Sounds/firealarm.mp3"
$ renpy.pause(1.0, hard=True)
p "Ah... That wasn't a good idea after all..."
k "Why did you take us to the back of the school [name]? Now we're gonna DIE because of you!!!"
if (lust_points[11] <= 9):
    $ lust_points[11] -= 1
    $ score -= 1
    show lustminus01:
        xalign 0.1 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01 
p "Don't worry, let's just go back and get to the front entrance then..."
stop music
if (blacktop05 == True):
    scene firekate03black with dissolve
else:
    scene firekate03 with dissolve    
play sound "Sounds/policesound.mp3"
so "There you are! We were looking for you two!"
if (detention05 == False):
    t "Thank God you're safe! But don't do this again to me. Detention for both of you today for not following the proper evacuation procedure!"
    $ detention05 = True
    jump FireDamian01
if (detention05 == True):
    t "Thank God you're safe! But don't do this again to me. Detention for you too Kate for not following the proper evacuation procedure!"
k "What? But... I was just following [name]! He took us to the back of the school where the fire was, so we had to come back!"
so "The fire broke out at the back of the school? Interesting..."
so "Where is this dreadful goth Damian? Anyone seen him? I need to talk to him IMMEDIATELY!"
jump FireDamian01

label FireDamian01:
$ hour += 1
if (blacktop05 == True):
    scene firedamian01black with dissolve
else:
    scene firedamian01 with dissolve 
$ renpy.pause(1.0, hard=True)
so "So. Mr pot-smoking arsonist... CONFESS! CONFESS! CONFESS!"
go "It was an accident, I swear! My... cigarette... Please, I beg you!"
so "You are hereby expelled from this school Damian! And now for your walk of shame out of the gates..."
$ damianexpelled = True
if (blacktop05 == True):
    scene firedamian02black with dissolve
else:
    scene firedamian02 with dissolve 
$ renpy.pause(1.0, hard=True)
play sound "Sounds/shame.mp3"
la "(muttering) Good riddance..."
scene firelaura01 with dissolve
$ renpy.pause(1.0, hard=True)
p "It's because I tried to evacuate through the back that the principal found out you know..."
la "Really? That was wicked!"
if (lust_points[13] <=8):
    $ lust_points[13] += 1
    $ score += 1
    show lust01:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01 
la "We can continue meeting at the campfire without him. I'm the only one who knows the incantation anyway!"
p "Yeah! Err.. Death to all but Metal, right?"
la "DEATH TO ALL BUT METAL!"

label FireEnd:
scene fireend with dissolve
$ renpy.pause(1.0, hard=True)
so "The fire brigade says the fire has been put out. It caused minor damage to an administrative wing near the back of the school. So everything will continue as per usual."
so "But the back of the school is now OFF-LIMITS, is that clear? Now, everyone off to lunch while we figure out how to best organize the school's activities for the coming days..."
jump LunchDay05

label LunchDay05:
scene lunchallday05 with dissolve
$ renpy.pause(1.0, hard=True)
$ hour += 1
stop music
play music "Sounds/lunchambience.mp3"
$ lustaddedB = 2
call Challenger from _call_Challenger_64
$ lustaddedB = 1
call Challenger from _call_Challenger_65
$ lustaddedB = 1
call Challenger from _call_Challenger_66
$ challengercalls += 2
p "Ah. The cafeteria is packed, as usual... Where should I sit...?"
menu:
    "Sit with your classmates":
        jump LunchClassDay05
    "Sit with Nikki":
        jump LunchSisterDay05   

label LunchClassDay05:
scene lunchclassday05 with dissolve
$ renpy.pause(1.0, hard=True)
p "I'll take that empty seat in front of Laura..."
label LunchChoiceDay05:
scene lunchclassday05
menu:
    "Talk to Laura" if (spokenlunchlaura05 == False):
        $ spokenlunchlaura05 = True
        menu:
            "Hey Laura, I read that book you gave me." if (bookread == True) and (toldlaurabook == False):                
                $ toldlaurabook = True
                show lunchlaurahappy with dissolve
                la "Oh really? And what did you think about it?"
                p "Fascinating. I didn't realize so many celebrities were goths."
                p "Ozzy Osbourne, Marilyn Manson, the Addams Family, Mike Pence... It opened my eyes." 
                la "Well, that's great! You're half-way to becoming a true goth then."
                $ lust_points[13] +=1
                $ score += 1
                show lust01:
                    xalign 0.35 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
                hide lunchlaurahappy
                jump LunchChoiceDay05
            "See, I'm wearing a black tank top today!" if (blacktop05 == True) and (lauratop == False):
                show lunchlaurahappy with dissolve
                la "Wicked, it suits you too [name]!"
                $ lust_points[13] +=2
                $ score += 2
                show lust02:
                    xalign 0.35 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust02 
                $ lauratop = True
                jump LunchChoiceDay05
            "What are you up to today Laura?":
                la "Well, I can't hang out with Damien anymore... I guess I'll just have to talk to Joséphine instead... (sigh)"
                jump LunchChoiceDay05
            "What are you up to this evening Laura?":
                if (blacktop05 == True) and (toldlaurabook == True) and (seencampfireday04 == False) and (seencampfireday03 == False):
                    la "We are performing a goth ritual, summoning demons and stuff. Meet us at the campfire on the local beach tonight if you're interested..."
                    $ lauraritual05 = True
                    jump LunchChoiceDay05
                if (blacktop05 == True) and ((seencampfireday04 == True) or (seencampfireday03 == True)):
                    la "I reckon we can meet at the campfire without Damian... Meet us tonight with Joséphine..."
                    $ lauraritual05 = True
                    jump LunchChoiceDay05
                if (blacktop05 == False) and (toldlaurabook == False):
                    la "None of your business! What a goth does at night is sacred knowledge that conformists like you do not deserve to hear!"
                    p "Wow. OK."
                    jump LunchChoiceDay05
                if (blacktop05 == False):
                    la "A goth ritual. But since you're wearing a pathetic and dirty white top, you're not invited."
                    jump LunchChoiceDay05
                if (blacktop05 == True):
                    la "A goth ritual. But sine you're not really a goth, you're not invited."                    
    "Talk to Kate" if (spokenlunchkate05 == False):
        $ spokenlunchkate05 = True
        show lunchkateunhappy
        if (detention05 == True):
            show lunchkateunhappy
            k "I've got detention again... And it's all your fault!..."
            p "Just think about what bikini you'll wear tomorrow during detention and forget about doing any work. The teacher will never know."
            show lunchkatehappy with dissolve
            k "Oooh, thanks for the advice [name]!"
            jump LunchChoiceDay05
        menu:
            "Hey Kate, you know what I found out? That scumbag José is totally backing Brittany for prom queen!" if ((seenlockerbrit == True) or (lust_pointsB[1] >= 8)) and (toldkatejose == False):
                $ toldkatejose = True
                k "What? Oooh, no... I need his vote to win... What a loser, what does he find in her?"
                if (lust_pointsB[11] == 1):
                    $ lust_pointsB[11] -=1
                    show challengerlustminus01:
                        xalign 0.1 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide challengerlustminus01
                if (lust_pointsB[11] >= 2):
                    $ lust_pointsB[11] -=2
                    show challengerlustminus02:
                        xalign 0.1 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide challengerlustminus02                    
                p "Who knows, that guy has shit for brains."
                jump LunchChoiceDay05
            "Since you will compete in the bikini pageant, I could maybe take pictures of you so you can better decide which bikini to choose?" if (katephotoasked == False) and (katefucked == False):
                show lunchkatehappy with dissolve
                k "Ooh, are you a photographer? I've been looking for someone who could show me what I look like, because I can't see myself."
                p "Yeah sure... I have a great camera, I'll let you know when I set everything up and you can come round to my place to try on some bikinis."
                k "Oooh, I can't wait! Hee hee!"
                window hide
                $ lust_points[11] += 1
                $ score += 1
                show lust01:
                    xalign 0.1 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
                p "(I'd better find a good camera real soon...)"
                $ katephotoasked = True
                jump LunchChoiceDay05
            "Maybe I could cheer you up with a photoshoot session this afternoon?" if (katephotoasked == True) and (katefucked == False):
                show lunchkatehappy with dissolve
                k "Oooh, yes! I have a couple of bikinis I would like to try on!"
                p "Come to my place at 5pm or 6pm then, I'll have everything set up!"
                k "Oh, really? That's so great, I'll be there!"
                $ katephotoplanned05 = True                
                if (camera == False):
                    p "I'd better find a camera TODAY or she'll be mighty disappointed..."
                    jump LunchChoiceDay05
                if (camera == True):
                    p "(I'd better make sure I'm back home by 5 or 6pm...)"
                    jump LunchChoiceDay05
            "Don't study and daydream about stuff instead. That's what I always do during detention.":
                show lunchkatehappy with dissolve
                k "Oooh, thanks for the advice [name]!"
                jump LunchChoiceDay05
    "Talk to Frieda" if (spokenlunchfrieda05 == False):
        $ spokenlunchfrieda05 = True
        scene lunchfriedaday05 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Hey Frieda, what are you doing this afternoon?"
        fr "I vill be studying in the school library. Again..."
        if (maddysaved == False):
            fr "And worrying about Maddy... She still hasn't been found..."
            p "Don't worry, I'll find her. Alive and well, I swear!"
            fr "I hope so... Otherwise, I hope another hero finds her this afternoon..."
            p "(What other hero is she talking about? I'm the only hero here!)"
            jump LunchChoiceDay05
        if (discoverlibrary == False):
            p "Oh? I didn't even know this school had a library..."
            fr "Yes, it is at the end of corridor F." 
            show addedlocation:
                xalign 0.7 yalign 0.3
                linear 1.0 yalign 0.1
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide addedlocation
        p "Ach, zo interesting."
        jump LunchChoiceDay05
    "Talk to Quentin" if (spokenlunchquentin05 == False):
        $ spokenlunchquentin05 = True
        scene lunchquentinhappy with dissolve
        if (discoverrooftop == False):
            q "I bet you're the kind of guy who loves astronomy, right?"
            menu:
                "No I'm not, it's for nerds.":
                    k "Hee hee."
                    play sound "Sounds/katehihi.mp3"
                    scene lunchquentinhappy with dissolve
                    q "Humpf, I guess I was wrong then. You're just a boring jock."
                    jump LunchChoiceDay05
                "Yeah, it's okay. I guess.":
                    q "Well guess what? I'm the president of the school astronomy club. I just finished installing a telescope on the school roof."
                    q "You can access the roof area through a ladder at the end of corridor K4. Don't thank me, thank the nebulaes, they are so beautiful!"
                    $ discoverrooftop = True
                    show addedlocation:
                        xalign 0.2 yalign 0.3
                        linear 1.0 yalign 0.1
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide addedlocation
                    p "(I can think of other uses for that telescope... During the day.)"
                    jump LunchChoiceDay05
        q "I almost died this morning. Makes you think about how important it is to enjoy life while you can."
        p "Sure buddy, sure. But I can't die. At least not before the end of the week!"
        jump LunchChoiceDay05
    "Just eat up already":
        jump LunchEndDay05
    
label LunchSisterDay05:
scene lunchsis01day05 with dissolve
$ renpy.pause(1.0, hard=True)
p "I think I'll join you guys."
if (lunchsister == True):
    j "I thought I already told you that, this table is for the SENIORS!"
    if (chantellejosewin == False):
        scene lunchsis02day05 with dissolve
        ch "And we already told you there is no such rule. You are starting to get VERY tiresome. Sit down next to us [name]..."
        window hide
        if (lust_pointsB[2] <= 9):
            $ lust_pointsB[2] -= 1 
            show challengerlustminus01:
                xalign 0.8 yalign 0.6
                linear 1.0 yalign 0.8
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide challengerlustminus01        
        jump LunchSister02Day05
    if (chantellejosewin == True):
        ch "Actually, I agree with José for once... He's been quite nice to me lately so I just have to agree with him."
        s "Looks like you're on your own [name]... I ain't getting involved for you, Chantelle is my best friend."
        p "She's only defending him because she opened her legs for him!"
        j "How dare you insult my darling Chantelle! Get out of here!"
        scene lunchsis03day05 with dissolve
        br "Hang on a minute, you did WHAT???"
        if (lust_pointsB[1] <=9):
            $ lust_pointsB[1] -= 2           
            show challengerlustminus02:
                xalign 0.2 yalign 0.6
                linear 1.0 yalign 0.8
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide challengerlustminus02        
        scene lunchsis04day05 with dissolve
        j "Well, I meant, of course, she's nothing compared to you babe, but..."
        scene lunchsis05day05 with dissolve
        s "Humpf, I thought you were a gentleman, but I see you are nothing but a heart-breaker..."
        if (lust_pointsB[17] <=9):
            $ lust_pointsB[17] -= 1           
            show challengerlustminus01:
                xalign 0.2 yalign 0.6
                linear 1.0 yalign 0.8
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide challengerlustminus01
        p "Fine, I'll go and sit with my classmates then. I'll leave you lot to your \"Senior\" bickerings."
        jump LunchClassDay05
if (lunchsister == False):
    j "Where do you think you're going? This table is for the SENIORS!"
    scene lunchsis02day05 with dissolve
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
            if (lust_points[17] >= 8):
                hide lunchbrittany01
                show lunchnikki01
                s "I want [name] to sit with me on his first week of school. Come [name], there's an empty seat next to me right here."
                jump LunchSister02Day05
            if (lust_points[17] <= 7):
                hide lunchbrittany01
                show lunchnikki01
                hide lunchjose02
                s "I don't know [name]... I think it's best not to piss José off. Go and sit with your classmates, they seem really nice. I'll see you at home tonight."
                hide lunchchantelle01
                p "Ok... I'll go and sit with my classmates then... Bye Chantelle..."
                ch "See you [name]... (sigh)"
                jump LunchClassDay05
        "Ok, I'll go and sit with my classmates then. They are nicer than you sorry lot of old farts.":
            jump LunchClassDay05

label LunchSister02Day05:
$ lunchsisterday05 = True
scene lunchsis03day05 with dissolve
show lunchbrittanyhappy
$ renpy.pause(1.0, hard=True)
label LunchSisterChoiceDay05:
menu:
    "Talk to Nikki":
        show lunchsistalk with dissolve
        p "I was looking for you this morning during the fire, I wanted to find you and save you."
        s "That's really cute [name], but I got out very easily. Our classroom is right by the front entrance. I was worried about you though..."
        p "I got out alright... I'm DA MAN!"
        hide lunchsistalk
        jump LunchSisterChoiceDay05
    "Talk to Chantelle" if (spokechantelleday05 == False):
        $ spokechantelleday05 = True
        p "I really think you should compete in tomorrow's Bikini Pageant Chantelle. You can win for sure!"
        show lunchchantellehappy with dissolve
        ch "Really, you think so? Honestly? That's really nice of you, but I'm still not sure yet..."
        $ lust_points[2] +=1
        $ score += 1
        show lust01:
            xalign 0.8 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01        
        show lunchbrittanyangry with dissolve
        br "WHAT? How dare you encourage other girls to compete with ME! I am the ultimate beauty Queen of this school!"
        $ lust_points[1] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        p "Uh Uh..."
        show lunchsistalk with dissolve
        s "I think you'd better shut up [name]..."
        hide lunchbrittanyangry
        hide lunchsistalk
        hide lunchchantellehappy
        jump LunchSisterChoiceDay05
    "Talk to Brittany" if (spokebrittanyday05 == False):
        $ spokebrittanyday05 = True 
        scene lunchsis03day05 with dissolve
        br "You're just a junior. I'm too important to be seen talking to a junior in public like that."
        p "Really, even one who might be on the jury in tomorrow's pageant?"
        show lunchjoseangry
        j "She doesn't need your vote, she'll win easily in any case! Right, babe?"
        show lunchbrittanyhappy
        br "Of course, I am the ultimate beauty Queen of this school!"
        if (lust_pointsB[1] <=8):
            $ lust_pointsB[1] += 1           
            show challengerlustplus01:
                xalign 0.25 yalign 0.6
                linear 1.0 yalign 0.4
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide challengerlustplus01        
        p "(Aargh, I shouldn't have spoken to her...)"
        hide lunchjoseangry
        jump LunchSisterChoiceDay05
    "Talk to José" if (spokejoseday05 == False):
        $ spokejoseday05 = True
        show lunchjoseangry with dissolve
        j "What do you want worm?"
        if (fuckedschoolgirl == True) or (fuckedschoolgirlday03 == True) or (fuckedschoolgirlday04 == True):
            p "You're cheating, you're snitching on me to the principal!"
            j "Yeah, so? What'ya gonna do about it? AH AH AH!"
            ch "I hate people who cheat..."
            window hide
            if (lust_pointsB[2] <= 9):
                $ lust_pointsB[2] -= 1 
                show challengerlustminus01:
                    xalign 0.8 yalign 0.6
                    linear 1.0 yalign 0.8
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide challengerlustminus01
            hide lunchjoseangry
            jump LunchSisterChoiceDay05
        p "You'll sing a different tune on Sunday! Then, you'll have to call me \"Master School Stud\"!"
        j "In your dreams! I AM and WILL REMAIN the school's stud! Everyone knows that here!"
        if (chantellejosewin == True):
            ch "It's true, I've heard people say that... Sorry [name], but José is DEFINITELY the school stud in this school..."
            p "Umpf..."
            jump LunchSisterChoiceDay05
        if (chantellejosewin == False):            
            ch "I never heard you being called that. So stop bragging."
            show lunchbrittanyangry with dissolve
            br "Umpf... You keep telling me everyone calls you a stud but I see that was a lie..."
            window hide
            if (lust_pointsB[1] <= 9):
                $ lust_pointsB[1] -= 1 
                show challengerlustminus01:
                    xalign 0.3 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide challengerlustminus01
            j "But... I AM the school stud, goddamit!"
            jump LunchSisterChoiceDay05
    "Just eat up already":
        jump LunchEndDay05

label LunchEndDay05:
stop music
scene lunchempty with dissolve
$ hour += 1
$ renpy.pause(1.0, hard=True)

if (fuckedschoolgirlday04 == True):
    play sound "Sounds/pasystem.mp3"
    ps "[name] Johnson, please report to the principal's office immediately."
    p "Why? What have I done this time I wonder... I guess I don't have a choice or I might be expelled in shame like Damian and Nancy would be mad... (sigh)."
    jump PrincipalGuidanceDay05

if (detention05 == True):
    p "I have to go to detention or I'm in trouble..."
    jump DetentionDay05
    
label SchoolChoiceDay05:
stop music
p "I've got the afternoon free. What should I do?"
menu:
    "Go to my locker" if (seenlocker05 == False):
        jump LockerDay05
    "Go to the school gym" if (seenschoolgym05 == False):
        jump SchoolGym01Day05
    "Go to the school library" if (seenlibrary05 == False):
        jump Library01Day05
    "Go on the school rooftop" if (discoverrooftop == True) and (seenrooftop05 == False)  and (seenrooftop04 == False):
        jump RooftopDay05
    "Go to the principal's office" if (seenwillie05 == False):
        jump WillieCorridorDay05
    "Go to the sports hall" if (seenhall05 == False) and (seenhall05v == False):
        jump SportsHallDay05
    "Go to the school bathroom" if (seenbathroom05 == False):
        jump SchoolBathroom01Day05
    "Go to the nurse's office" if (seennurse05 == False):
        jump NurseDay05
    "Leave the school and go the Burbs":
        jump BurbsDay05
        
label DetentionDay05:
scene detention01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Kate and [name], You both have detention for one hour. During that time, I want to see you studying hard, is that clear?"
p "Damn, this is going to be so boring... I wonder what I could do to pass the time?..."
p "Mmh, Kate is looking great in that schoolgirl outfit... But it would be better if she was naked..."
menu:
    "Daydream about Kate":
        jump KateDayDreamDay05
    "Daydream about Maddy and Frieda":
        jump MaddyDreamDay05
    "Daydream about Laura":
        jump LauraDreamDay05
    "Pretend you're studying":
        jump EndDetentionDay05

label LauraDreamDay05:
play sound "Sounds/dreaming.mp3"
scene dreaminglaura01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
la "Do you like seeing me in a naughty lace teddy [name]?"
p "Mmmh, yeah Laura, I do... Show me more..."
scene dreaminglaura02 with dissolve
$ renpy.pause(3.0, hard=True)
la "At your command [name], I will do ANYTHING for that GIANT COCK of yours..."
p "Yeah, I'm da man, I'm DA MAN! I'm gonna pound that pussy..."
scene dreaminglaura03 with dissolve
$ renpy.pause(3.0, hard=True)
la "AAAH, YES! Fuck me with that massive ramrod!"
p "NTR ALERT! NTR ALERT! AAAAARGH!..."
stop music
jump EndDetentionDay05

label MaddyDreamDay05:
play sound "Sounds/dreaming.mp3"
scene dreamingfriedamaddy01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
md "We're ready to worship you master [name]..."
p "Damn right, just like I love my girls... Prime those pussies for my huge cock babies..."
scene dreamingfriedamaddy02 with dissolve
$ renpy.pause(3.0, hard=True)
md "Of course, I'll finger Frieda so she's nice and wet for your pussy-pounder..."
fr "Ooh, JA! Das is so gut! Komm fick mich mit deinem riesenschwanz [name]!"
p "Wow, I can dream in German even though I can't speak it... JA, I'm coming for you baby!"
scene dreamingfriedamaddy03 with dissolve
$ renpy.pause(3.0, hard=True)
md "She's ready for you, you can take her from behind like that and pound her HARD and FAST!"
fr "I can't wait, please, please, feed my pussy with zat massive cock, JA!"
p "Alright! I'm da man, I'll do her from behind then I'll do Maddy... Mmh..."
stop music
jump EndDetentionDay05

label KateDayDreamDay05:
play sound "Sounds/dreaming.mp3"
scene katedreaming01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
k "Oops, I just dropped my top. Hee hee..."
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

label EndDetentionDay05:
play sound "Sounds/schoolrecess.mp3"
scene detention01 with dissolve
$ hour += 1
$ renpy.pause(1.0, hard=True)
t "That's it, you're both free to go now. I hope you learnt your lesson and I won't have to see you again in detention this week."
scene katedetentiondoor with dissolve
$ renpy.pause(1.0, hard=True)
p "I'm so glad this is over, I was getting ssooo bored."
k "Me too, I didn't do any work at all, I was just thinking about I would wear at the Bikini pageant on Friday...Hee hee."
if (katephotoasked == False):
    p "Tell you what, I could take pictures of you so you can better decide which bikini to choose?"
    k "Ooh, are you a photographer? I've been looking for someone who could show me what I look like, because I can't see myself."
    p "Yeah sure... I have a great camera, I'll let you know when I set everything up and you can come round to my place to try on some bikinis."
    k "Oooh, I can't wait! Hee hee!"
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
menu:
    "How about this afternoon at 5 or 6pm at my place for our photoshoot session?" if (katephotoasked == True):
        $ katephotoplanned05 = True
        k "Ooh, yeah, yippee! I'll DEFINITELY be there!"
        jump SchoolChoiceDay05
    "Ok, see you tomorrow Kate!":
        k "Ooh, yeah, see you tomorrow [name], hee hee!"
        play sound "Sounds/katehihi.mp3"
        jump SchoolChoiceDay05


label PrincipalGuidanceDay05:
stop music
scene guidance01 with dissolve
$ renpy.pause(1.0, hard=True)
so "Do you know why I called you in [name]?"
p "Err, no..."
so "Because despite my strict orders, you FUCKED ONE OF OUR GIRLS YESTERDAY!"
if (sophiafucked == True):
    so "However... Since you're such a stud who fucked me so good the other day, I will commute your guidance session..."
    so "...to a FUCK SESSION AGAIN!"
    if (posterup == True) and (postersaid == False):
        menu:
            "Alright!":
                jump PrincipalFuckDay05
            "Hang on a minute, I put some posters up for you, please let me go!":
                $ postersaid = True
                so "Fine, you wimp! I'd better get elected, I'm warning you!"
                jump SchoolChoiceDay05                
    jump PrincipalFuckDay05
menu:
    "Yeah, so? I'm DA MAN, I fuck whoever I want!":
        so "(sigh) Once again, you leave me no choice... Get undressed and get that cock of yours hard NOW!"
        jump PrincipalGuidance02Day05
    "This is FAKE NEWS! There was no collision between my cock and any schoolgirl's pussy, believe me.":
        so "Well, I DON'T believe you! My sources are reliable. You're a liar and you must pay for this. Get undressed and get that cock of yours hard NOW!"
        window hide
        $ lust_points[20] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.6 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump PrincipalGuidance02Day05
    "But I put some posters up for your senate campaign downtown!" if (posterup == True)  and (postersaid == False):
        $ postersaid = True
        scene principalposter with dissolve
        $ renpy.pause(1.0, hard=True)
        so "Oh, you did? Then, I waive your guidance session for the day. But only for today...."
        window hide
        $ lust_points[20] +=1
        $ score += 1
        show lust01:
            xalign 0.7 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        if (flower == True):
            $ plantsaid = True
            p "I also happen to have found a \"Bostiboobicus Gigantus\" in full bloom..."
            so "What? That is so sweet of you, do you have it on you?"
            p "Of course, but who says I'll give it you?"
            window hide
            $ lust_points[20] +=2
            $ score += 2
            show lust02:
                xalign 0.7 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust02            
            so "Don't try and play hardball with me young man. Give it to me or I'll expel you from this school!"
            menu:
                "Err...OK. Here it is.":
                    so "That's a good boy..."
                    show flower
                    show square
                    play sound "Sounds/lost.mp3"
                    "You offered a stinky flower to a woman. What a gentleman."
                    hide square
                    hide flower
                    $ flower = False
                    $ gaveflower = True
                    scene principalflower with dissolve
                    $ renpy.pause(1.0, hard=True)
                    so "It's so lovely... Even though it does stink a bit."
                    so "Well, you did good [name] for once... You might end up finishing the academic year in this school after all. IF YOU KEEP YOUR PANTS ZIPPED UP!"
                    menu:
                        "Use the pendulum on her" if (pendulumactive == True) and (lust_points[20] >=8):
                            jump PrincipalHypnoDay05
                        "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                            play sound "Sounds/spray.mp3"
                            $ renpy.pause(1.0, hard=True)
                            jump PrincipalPheromonesDay05
                        "Leave":
                            jump SchoolChoiceDay05
                        
                "That would be flimsy grounds, you don't scare me!":
                    so "I can come up with any excuse if I want to expel you, stop resisting me, I WANT this flower!"
                    window hide
                    $ lust_points[20] +=1
                    $ score += 1
                    show lust01:
                        xalign 0.7 yalign 0.4
                        linear 1.0 yalign 0.2
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lust01
                    p "OK, ok. (Gee, can't negociate with her, worse than an Iranian Ayatollah... Or an American president.)"
                    so "That's a good boy..."
                    show flower
                    show square
                    play sound "Sounds/lost.mp3"
                    "You offered a stinky flower to a woman. What a gentleman."
                    hide square
                    hide flower
                    $ flower = False 
                    $ gaveflower = True
                    scene principalflower with dissolve
                    $ renpy.pause(1.0, hard=True)
                    so "It's so lovely... Even though it does stink a bit."
                    so "Well, you did good [name] for once... You might end up finishing the academic year in this school. IF YOU KEEP YOUR PANTS ZIPPED UP!"
                    menu:
                        "Use the pendulum on her" if (pendulumactive == True) and (lust_points[20] >=8):
                            jump PrincipalHypnoDay05
                        "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                            play sound "Sounds/spray.mp3"
                            $ renpy.pause(1.0, hard=True)
                            jump PrincipalPheromonesDay05
                        "Leave":
                            jump SchoolChoiceDay05
        if (flower == False):
            so "So come on, shoot off. I'd better not see you again tomorrow because you fucked one of our girls YET AGAIN! Is that understood?"
            jump SchoolChoiceDay05
    "But I found a \"Bostiboobicus Gigantus\" in full bloom..." if (flower == True):
        so "What? That is so sweet of you, do you have it on you?"
        p "Of course, but who says I'll give it you?"
        window hide
        $ lust_points[20] +=2
        $ score += 2
        show lust02:
            xalign 0.7 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02            
        so "Don't try and play hardball with me young man. Give it to me or I'll expel you from this school!"
        menu:
            "Err...OK. Here it is.":
                so "That's a good boy..."
                show flower
                show square
                play sound "Sounds/lost.mp3"
                "You offered a stinky flower to a woman. What a gentleman."
                hide square
                hide flower
                $ flower = False
                $ gaveflower = True
                scene principalflower with dissolve
                $ renpy.pause(1.0, hard=True)
                so "It's so lovely... Even though it does stink a bit."
                so "Well, you did good [name] for once... You might end up finishing the academic year in this school after all. IF YOU KEEP YOUR PANTS ZIPPED UP!"
                menu:
                    "Use the pendulum on her" if (pendulumactive == True) and (lust_points[20] >=8):
                        jump PrincipalHypnoDay05
                    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                        play sound "Sounds/spray.mp3"
                        $ renpy.pause(1.0, hard=True)
                        jump PrincipalPheromonesDay05
                    "I also put some posters up for your senate campaign downtown!" if (posterup == True)  and (postersaid == False):
                        $ postersaid = True
                        scene principalposter with dissolve
                        $ renpy.pause(1.0, hard=True)
                        so "Oh, you did? Then, I waive your guidance session for the day. But only for today...."
                        window hide
                        $ lust_points[20] +=1
                        $ score += 1
                        show lust01:
                            xalign 0.7 yalign 0.4
                            linear 1.0 yalign 0.2
                        play sound "Sounds/more.mp3"
                        $ renpy.pause(2, hard=True)
                        hide lust01
                        if (lust_points[20] <=7):
                            so "So come on, shoot off. I'd better not see you again tomorrow because you fucked one of our girls YET AGAIN! Is that understood?"
                            jump SchoolChoiceDay05
                        menu:
                            "Use the pendulum on her" if (pendulumactive == True) and (lust_points[20] >=8):
                                jump PrincipalHypnoDay05
                            "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                                play sound "Sounds/spray.mp3"
                                $ renpy.pause(1.0, hard=True)
                                jump PrincipalPheromonesDay05
                            "Leave":
                                so "So come on, shoot off. I'd better not see you again tomorrow because you fucked one of our girls YET AGAIN! Is that understood?"
                                jump SchoolChoiceDay05

            "That would be flimsy grounds, you don't scare me!":
                so "I can come up with any excuse if I want to expel you, stop resisting me, I WANT this flower!"
                window hide
                $ lust_points[20] +=1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
                p "OK, ok. (Gee, can't negociate with her, worse than an Iranian Ayatollah... Or an American president.)"
                so "That's a good boy..."
                show flower
                show square
                play sound "Sounds/lost.mp3"
                "You offered a stinky flower to a woman. What a gentleman."
                hide square
                hide flower
                $ flower = False
                $ gaveflower = True
                scene principalflower with dissolve
                $ renpy.pause(1.0, hard=True)
                so "It's so lovely... Even though it does stink a bit."
                so "Well, you did good [name] for once... You might end up finishing the academic year in this school. IF YOU KEEP YOUR PANTS ZIPPED UP!"
                menu:
                    "Use the pendulum on her" if (pendulumactive == True) and (lust_points[20] >=8):
                        jump PrincipalHypnoDay05
                    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                        play sound "Sounds/spray.mp3"
                        $ renpy.pause(1.0, hard=True)
                        jump PrincipalPheromonesDay05
                    "Leave":
                        so "And where do you think you're going? You have a guidance session, remember?"
                        p "Oh, that thing..."
                        jump PrincipalGuidance02Day05
                    "I also put some posters up for your senate campaign downtown!" if (posterup == True)  and (postersaid == False):
                        $ postersaid = True
                        scene principalposter with dissolve
                        $ renpy.pause(1.0, hard=True)
                        so "Oh, you did? Then, I waive your guidance session for the day. But only for today...."
                        $ lust_points[20] +=1
                        $ score += 1
                        show lust01:
                            xalign 0.7 yalign 0.4
                            linear 1.0 yalign 0.2
                        play sound "Sounds/more.mp3"
                        $ renpy.pause(2, hard=True)
                        hide lust01
                        if (lust_points[20] <=7):
                            so "So come on, shoot off. I'd better not see you again tomorrow because you fucked one of our girls YET AGAIN! Is that understood?"
                            jump SchoolChoiceDay05
                        menu:
                            "Use the pendulum on her" if (pendulumactive == True) and (lust_points[20] >=8):
                                jump PrincipalHypnoDay05
                            "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                                play sound "Sounds/spray.mp3"
                                $ renpy.pause(1.0, hard=True)
                                jump PrincipalPheromonesDay05
                            "Leave":
                                so "So come on, shoot off. I'd better not see you again tomorrow because you fucked one of our girls YET AGAIN! Is that understood?"
                                jump SchoolChoiceDay05
  

label PrincipalGuidance02Day05:
scene guidance02 with dissolve
$ renpy.pause(1.0, hard=True)
so "Now lick my feet naughty boy! Before your GUIDANCE session!"
play sound "Sounds/sucking.mp3"
$ renpy.pause(1.0, hard=True)
scene guidance02 with dissolve
$ renpy.pause(1.0, hard=True)
so "Last time, you made a right mess on my feet with your filthy scum... This time, I took some precautions..."
so "See that table? Get under it and stick your cock through the hole..."
scene guidance04 with dissolve
$ renpy.pause(1.0, hard=True)
so "That's it... Now I can tame that hard beast without you spewing your vile load over me..."
if (lust_points[20] ==9):
    $ lust_points[20] +=1
    $ score += 1
    show lust01:
        xalign 0.1 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[20] <=8):
    $ lust_points[20] +=2
    $ score += 2
    show lust02:
        xalign 0.1 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
if (lust_points[20] >=10) and (sophiafucked == False):
    show epiclust:
        xalign 0.2 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    so "And after this footjob, the MAIN COURSE!"
    
stop music
play music "Sounds/principalslow02.mp3"
show guidanceslow
show faster
call screen principalfootjob05
screen principalfootjob05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("FootJobFast02Day05")

label FootJobFast02Day05:
stop movie
hide faster
play music "Sounds/principalfast02.mp3"
show guidancefast
show cum
call screen footjobfaster05
screen footjobfaster05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PrincipalCum02Day05")

label PrincipalCum02Day05:
hide guidancefast
hide guidanceslow
stop music
play sound "Sounds/ryancumming.mp3"
scene guidancecum01
$ renpy.pause(1.0, hard=True)
so "Yes, that's a good boy, empty those massive balls of all their filthy cum..."
play sound "Sounds/principalcum02.mp3"
scene guidancecum02 with dissolve
$ renpy.pause(8.0, hard=True)
$ stamina -=1
show staminaminus01:
    xalign 0.65 yalign 0.3
    linear 1.0 yalign 0.5
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ hour += 1
so "Every time you fuck one of our girls, you will get some guidance from me until you LEARN to control your fuckstick, understood?"
p "Yes Principal Titsworthy... I get it now."
if ((lust_points[20] ==8) or (lust_points[20] ==9)) and (sophiafucked == False) and (stamina >= 1):
    menu:
        "Use the pendulum on her" if (pendulumactive == True):
            jump PrincipalHypnoDay05
        "Spray yourself with some pheromones" if (pheromone == True):
            play sound "Sounds/spray.mp3"
            $ renpy.pause(1.0, hard=True)
            jump PrincipalPheromonesDay05
        "Leave":
            jump SchoolChoiceDay05

if (lust_points[20] >=10) and (sophiafucked == False) and (stamina >= 1):
    so "Now keep that horsedick HARD, I have much better than a guiding session in mind. A SEX SESSION!"
    jump PrincipalFuckDay05  
if (lust_points[20] >=10) and (sophiafucked == False) and (stamina <= 0) and (whitebull == False):
    so "Now what's wrong with your dick? It's all floppy and useless! Just when I wanted to have some REAL fun with it!"
    so "This is such a disappointment, I'm taking back my epiclust icon! It's like it never appeared!"
    $ lust_points[20] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.1 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    so "Now get out of my sight [name]!"
    jump SchoolChoiceDay05
if (lust_points[20] >=10) and (sophiafucked == False) and (stamina <= 0) and (whitebull == True):
    menu:
        "Maybe I should drink some White Bull...":
            show whitebull
            show square
            play sound "Sounds/lost.mp3"
            "You gulped down your White Bull energy drink."
            hide square
            hide whitebull
            $ whitebull = False
            $ stamina += 2
            so "Now keep that horsedick HARD, I have much better than a guiding session in mind. A SEX SESSION!"
            jump PrincipalFuckDay05
        "I can't be bothered drinking a White Bull, I'm exhausted...":
            so "Now what's wrong with your dick? It's all floppy and useless! Just when I wanted to have some REAL fun with it!"
            so "This is such a disappointment, I'm taking back my epiclust icon! It's like it never appeared!"
            $ lust_points[20] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.1 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            so "Now get out of my sight [name]!"
            jump SchoolChoiceDay05

if (principaldeal == False) and (postersaid == False):
    p "I heard you were looking for volunteers to help you in your senate seat election campaign."
    so "Yes, that is correct. A boy like you could put posters up downtown, are you interested in helping?"
    p "What do I get in return?"
    so "Humpf... Normally, people volunteer because they adhere to a political ideal! But fine, I will suspend your guidance session for a day if you spend an hour of your time putting posters up downtown."
    menu:
        "Deal!":
            so "Welcome aboard! The posters are in the corner over there. Take a stack of them on your way out."            
            $ principaldeal = True
            so "Now off you go, I need to call Willie our janitor to clean that mess you made... I'd better not see you again because you fucked yet ANOTHER of our girls!"
            jump SchoolChoiceDay05
        "Not interested, sorry, I'll be rooting for your opponent anyway!":
            so "Then you'll be on the losing side! Now get out of here, I need to call Willie our janitor to clean that mess you made!"
            jump SchoolChoiceDay05
jump SchoolChoiceDay05

label PrincipalHypnoDay05:
scene principalhypno with dissolve
$ renpy.pause(1.0, hard=True)
show pendulum03
$ renpy.pause(1.0, hard=True)
p "Just watch this pendulum as I wiggle it in front of your eyes Principal Titsworthy..."
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
if (lust_points[20] ==8):
    window hide
    $ lust_points[20] += 2
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
    jump PrincipalFuckDay05
if (lust_points[20] ==9):
    window hide
    $ lust_points[20] += 1
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
    jump PrincipalFuckDay05
    
label PrincipalPheromonesDay05:
scene principalhypno with dissolve
play sound "Sounds/sniffing.mp3"
$ renpy.pause(1.0, hard=True)
so "What is this smell... It's not the flower... It's... nice."
p "My spray is now empty... I guess I won't be able to use it again."
show pheromone
show square
play sound "Sounds/lost.mp3"
"You lost a pheromone spray."
hide square
hide pheromone
$ pheromone = False
if (lust_points[20] ==8):
    window hide
    $ lust_points[20] += 2
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
    jump PrincipalFuckDay05
if (lust_points[20] ==9):
    window hide
    $ lust_points[20] += 1
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
    jump PrincipalFuckDay05

label PrincipalFuckDay05:
stop music
scene principalfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
so "That's it young man, get undressed, I NEED to see that monster hard and ready on the spot!"
scene principalfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
so "And as treat, I'll show you my breasts. Aren't they just spectacular?"
p "Damn right, I'm getting a rock-hard boner just looking at them Principal Titsworthy!"
window hide
play sound "Sounds/sophia01.mp3"
$ renpy.pause(7.0, hard=True)
so "Well good, but you have to earn it... Get on your knees, you need to be punished for being a naughty boy who wants to fuck his principal!" 
scene principalfuck03 with dissolve
play sound "Sounds/slap.mp3"
$ renpy.pause(1.0, hard=True)
p "Hey, what the fuck? Stop it!"
so "Shut up and take it like a man! You are a man or are you a little boy?"
play sound "Sounds/slap.mp3"
$ renpy.pause(1.0, hard=True)
p "I'm a man, I'm a man! I'm DA MAN actually..."
so "Now get on your back and let me tease that massive rod till you can't bear it anymore!" 
scene principalfuck04 with dissolve
window hide
play sound "Sounds/sophia02.mp3"
$ renpy.pause(13.0, hard=True)
so "Mmmh, yeah, nice and hard, like a bar of steel... My giant knockers really are making you horny aren't they?"
p "Y..Yes Principal Titstworthy... Please, I want to feel them..."
so "Too soon, you have to learn to control yourself filthy horny boy! I want to see it grazing your face, it's big enough for you to suck yourself!"
p "What? But I don't want to suck myself!"
so "Shut up and do it!"
scene principalfuck05 with dissolve
window hide
play sound "Sounds/sophia03.mp3"
$ renpy.pause(11.0, hard=True)
so "That's it, don't resist, let the precum flow on your face, get a taste of your own filthy juices!"
p "No please... I've had enough of your teasing you fucking bitch! Stop it or I'll call the cops on you!"
scene principalfuck05b with dissolve
$ renpy.pause(1.0, hard=True)
so "Calm down [name], it's just a bit of fun..."
p "Get your disgusting feet off my face and get on the couch, I'm gonna pound your pussy till you're begging me to stop!"
so "Such manliness for a young boy who is at my mercy! Alright, I'll let you have a sniff of my sweet pussy then..."
scene principalfuck06 with dissolve
$ renpy.pause(1.0, hard=True)
so "Is that what you're after [name]... Come closer..."
scene principalfuck07 with dissolve
$ renpy.pause(1.0, hard=True)
p "Now we're talking, let me get these panties off... MY WAY!"
play sound "Sounds/rip.mp3"
$ renpy.pause(1.0, hard=True)
scene principalfuck08 with dissolve
$ renpy.pause(1.0, hard=True)
so "Oh, what are you doing, these are expensive panties!"
p "Shut up and get ready for my cock!"
scene principalfuck09 with dissolve
$ renpy.pause(1.0, hard=True)
so "Be careful, I've never had anything that big in me before!"
p "Too late to complain bitch!"
scene principalfuck09b with dissolve
window hide
play sound "Sounds/sophia04.mp3"
$ renpy.pause(13.0, hard=True)
so "AAAAH, it's like a telephone pole! I'm so... Rhaa.... full of young virile cock!"
label PrincipalStartFuckDay05:
window hide
play sound "Sounds/sophia05.mp3"
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09 with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09 with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09 with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09 with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09c
$ renpy.pause(0.2, hard=True)
scene principalfuck09b
$ renpy.pause(0.2, hard=True)
scene principalfuck09
$ renpy.pause(0.2, hard=True)
scene principalfuck09b
$ renpy.pause(0.2, hard=True)
scene principalfuck09c
$ renpy.pause(0.2, hard=True)
scene principalfuck09b
$ renpy.pause(0.2, hard=True)
scene principalfuck09
$ renpy.pause(0.2, hard=True)
scene principalfuck09b
$ renpy.pause(0.2, hard=True)
scene principalfuck09c
$ renpy.pause(0.2, hard=True)
scene principalfuck09b
$ renpy.pause(0.2, hard=True)
scene principalfuck09
$ renpy.pause(0.2, hard=True)
scene principalfuck09b
$ renpy.pause(0.2, hard=True)
scene principalfuck09c
$ renpy.pause(0.2, hard=True)
scene principalfuck09b
$ renpy.pause(0.2, hard=True)
scene principalfuck09
$ renpy.pause(0.2, hard=True)
scene principalfuck09b
$ renpy.pause(0.2, hard=True)
scene principalfuck09c
$ renpy.pause(0.2, hard=True)
scene principalfuck09b
$ renpy.pause(0.2, hard=True)
scene principalfuck09
$ renpy.pause(0.2, hard=True)
scene principalfuck09b
$ renpy.pause(0.2, hard=True)
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
play sound "Sounds/sophia06.mp3"
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09c with dissolve
$ renpy.pause(0.1, hard=True)
scene principalfuck09b with dissolve
$ renpy.pause(0.1, hard=True)
menu:
    "Repeat":
        jump PrincipalStartFuckDay05
    "Move on":
        pass
so "NNOO! too... too much.... I can't take it anymore, AAAAHH!"
p "Giving up already principal? You're gonna screw the people as a senator, now it's time for the people to screw YOU!"
label PrincipalFuckChoiceDay05:
menu:
    "I want to stick my cock between your huge jugs..." if (principaltits == False):
        jump PrincipalTitfuckDay05
    "Let's switch position, get on your back!" if (principalback == False):
        jump PrincipalBackFuckDay05
    "Time to finish me off with your arse muscles!" if ((principaltits == True) and (principalback == True)):
        jump PrincipalArseFuckDay05
    
label PrincipalTitfuckDay05:
scene principaltits01 with dissolve
window hide
play sound "Sounds/sophiatitfuck01.mp3"
$ renpy.pause(8.0, hard=True)
so "Mmh, that's a first. Yours is the only cock to ever make it through my tunnel of titflesh!"
p "Well put it to good use and wank me off with your massive funbags!"
scene principaltits02 with dissolve
window hide
play sound "Sounds/sophiatitfuck02.mp3"
$ renpy.pause(10.0, hard=True)
so "Mmh, like that studboy? You love the feel of tons of soft titmeat wrapped around that giant fuckstick of yours?"
p "Fuck YEAH! Do it faster, now!"
label PrincipalTitFuckDay05b:
play sound "Sounds/sophiatitfuck03.mp3"
scene principaltits01 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits01 with dissolve
$ renpy.pause(0.1, hard=True)
scene principaltits02 with dissolve
$ renpy.pause(0.1, hard=True)
$ principaltits = True
menu:
    "Repeat":
        jump PrincipalTitFuckDay05b
    "Move on":
        pass
jump PrincipalFuckChoiceDay05

label PrincipalBackFuckDay05:
scene principalback02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready for a good pussy pounding principal?..."
so "Oh yeah, you've made me addicted to that monster cock of yours [name], fuck me hard, as hard as you want!"
label PrincipalBackFuckDay05b:
play sound "Sounds/sophiaback.mp3"
scene principalback03 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback03 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback03 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback03 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback03 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback03 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback03 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback03 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback03 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback03 with dissolve
$ renpy.pause(0.3, hard=True)
scene principalback02
$ renpy.pause(0.3, hard=True)
scene principalback03
$ renpy.pause(0.3, hard=True)
scene principalback02
$ renpy.pause(0.3, hard=True)
scene principalback03
$ renpy.pause(0.3, hard=True)
scene principalback02
$ renpy.pause(0.3, hard=True)
scene principalback03
$ renpy.pause(0.3, hard=True)
scene principalback02
$ renpy.pause(0.3, hard=True)
scene principalback03
$ renpy.pause(0.3, hard=True)
scene principalback02
$ renpy.pause(0.3, hard=True)
scene principalback03
$ renpy.pause(0.3, hard=True)
scene principalback02
$ renpy.pause(0.3, hard=True)
scene principalback03
$ renpy.pause(0.3, hard=True)
scene principalback02
$ renpy.pause(0.3, hard=True)
scene principalback03
$ renpy.pause(0.3, hard=True)
scene principalback02
$ renpy.pause(0.3, hard=True)
scene principalback03
$ renpy.pause(0.3, hard=True)
scene principalback02
$ renpy.pause(0.3, hard=True)
scene principalback03
$ renpy.pause(0.3, hard=True)
scene principalback02
$ renpy.pause(0.3, hard=True)
scene principalback03
$ renpy.pause(0.3, hard=True)
$ principalback = True
menu:
    "Repeat":
        jump PrincipalBackFuckDay05b
    "Move on":
        pass
so "Oooh, my poor pussy! I'll never recover from such a pounding.... (puff)"
p "Then it's time to try something else..."
jump PrincipalFuckChoiceDay05

label PrincipalArseFuckDay05:
scene principalarse01 with dissolve
$ renpy.pause(1.0, hard=True)
so "You can't be serious! My arse is too tiny for your massive piece of teenage meat!"
p "We're about to find out..."
scene principalarse02 with dissolve
$ renpy.pause(1.0, hard=True)
so "Oh my God, you're stretching me ssooo much!"
p "Just hang in there, there's quite a few more inches to go..."
so "What? Wait...AAAH!"

label PrincipalMainFuckDay05:
play music "Sounds/sophiaslowfuck.mp3"
show sophiafuckslow
show faster
call screen sophiafuckslowday05
screen sophiafuckslowday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("SophiaFuckFastDay05")
label SophiaFuckFastDay05:
hide faster
stop music
play music "Sounds/sophiafastfuck.mp3"
show sophiafuckfast
show cum
call screen sophiafuckfastday05
screen sophiafuckfastday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("SophiaFuckCumDay05")

label SophiaFuckCumDay05:
hide sophiafuckfast
hide sophiafuckslow
stop music
scene principalcum01
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
play sound "Sounds/sophiacum01.mp3"
$ renpy.pause(10.0, hard=True)
stop music
scene principalcum02 with dissolve
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
play sound "Sounds/sophiacum02.mp3"            
$ renpy.pause(16.0, hard=True)
so "Damn boy, you're STILL cumming like a firehose? Cover my huge jugs, I want to be bathing in your tasty spunk, more, more, AAAH!"
scene principalcum03 with dissolve
so "What a SPECTACULAR load [name]! My massive breasts are TOTALLY covered in your red-hot spunk!"
$ hour +=1
$ stamina -=1
show staminaminus01:
    xalign 0.3 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
so "I don't think I'll call Willie this time, I prefer to clean up your mess myself... with my MOUTH!"
so "Hopefully, you have emptied your giant balls and our girls are safe for the day..."
so "It will take me a while so get dressed and get back to your studies! Not a word to anyone about this..."
p "Of course Principal Titsworthy, my lips are sealed! And my balls are drained..."
if (sophiafucked == True):
    jump SchoolChoiceDay05
if (sophiajosewin == False):
    p "(She didn't notice I took a picture of her being filled by my dick... Now I'll send it to José)."
    $ sophiawin = True
if (sophiajosewin == True):
    p "(I hate sloppy seconds, especially after that dickhead José already ploughed their insides... But it was worth it, what a pair of tits!)"
$ backdoor += 1
$ sophiafucked = True
jump SchoolChoiceDay05

label RooftopDay05:
$ seenrooftop05 = True
scene rooftop01 with dissolve
play music "Sounds/wind.mp3"
$ renpy.pause(1.0, hard=True)
p "Ah, here's Quentin's telescope..."
if (blacktop05 == True):
    scene rooftop02black with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop02Day05
else:
    scene rooftop02 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop02Day05

label Rooftop02Day05:
p "Let's see what the neighbors are up to..."
$ renpy.pause(1.0, hard=True)
p "Mr Anderson is doing some gardening... BORING!"
p "Hang on a minute, his wife and daughter are on the upper deck jacuzzi..."
scene voyeur01 with dissolve
$ renpy.pause(1.0, hard=True)
p "And there's some muscular redhead boy proudly displaying his massive dong to them. That could become interesting..."
menu:
    "Continue watching (+1 stamina and +1hr)":
        jump Rooftop03Day05
    "Leave, this is bordering on NTR and my fragile ego can't take it!":
        jump SchoolChoiceDay05

label Rooftop03Day05:
scene voyeur02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Mrs Anderson is really going to town on his giant fuckstick." 
p "Her daughter is fisting herself silly watching her being throatfucked by that stud."
scene voyeur03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Now he's moving on to her tender fuckhole, ramming his pole into her in foot-long strokes." 
p "And the daughter can't help but play with her pussy, hoping her turn will come soon."
scene voyeur04 with dissolve
$ renpy.pause(1.0, hard=True)
p "Finally, he can't take it anymore. and after pumping her full of boycum, he's now plastering his cockwhores with massive streamers of spunk!"
p "Mr Anderson is going to be mighty pissed off if he sees those huge puddles of cum on his deck... Hang on, the young stallion is STILL hard and is now moving onto the daughter..."
scene voyeur05 with dissolve
$ renpy.pause(1.0, hard=True)
p "He's lifting her up in his strong arms and impaling her on his giant shaft. Ouch, that must hurt."
p "Mrs Anderson doesn't want to miss out on the action and is licking his massive dong and flowing precum to coax another load from him."
scene voyeur06 with dissolve
$ renpy.pause(1.0, hard=True)
p "And of course, the Grand Finale, he's covering their faces and bodies in giant pellets of scalding boyspunk. A classic."
p "Well, that sure was hot and got me horny like hell..."
$ peeping += 1
if (blacktop05 == True):
    scene rooftop02black with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop04Day05
else:
    scene rooftop02 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop04Day05

label Rooftop04Day05:
$ hour += 1
$ stamina += 1
show stamina01:
    xalign 0.7 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide stamina01
jump SchoolChoiceDay05

label SchoolBathroom01Day05:
$ seenbathroom05 = True
if (seenbathroom03 == True):
    if (d2rollbath == 0):
        jump SchoolBathroom01Day05b     
    if (d2rollbath == 1):
        jump SchoolBathroom01Day05c       
$ d2rollbathDay05=renpy.random.randint(0, 1)
if (d2rollbathDay05 == 0):
    jump SchoolBathroom01Day05b      
if (d2rollbathDay05 == 1):
    jump SchoolBathroom01Day05c   

label SchoolBathroom01Day05b:
scene schoolbathroombrittany01 with dissolve
$ renpy.pause(1.0, hard=True)
$ seenbrittanybathroom = True
"Brittany is here but she didn't see me come in. She's too engrossed in putting on her makeup..."
br "Yes, you look fabulous as always."
menu:
    "Are you talking to me?":
        scene schoolbathroombrittany02 with dissolve
        $ renpy.pause(1.0, hard=True)        
        br "What? No, I was talking...to myself."
        menu:
            "That's kind of sad...":
                scene schoolbathroombrittany03 with dissolve
                $ renpy.pause(1.0, hard=True)  
                br "I'm... (sniff)...lonely... (sniff)."  
                if (blacktop05 == True):
                    scene brittanycrying01b with dissolve
                    $ renpy.pause(1.0, hard=True)
                else:
                    scene brittanycrying01 with dissolve
                    $ renpy.pause(1.0, hard=True)
                p "There, there, everything will be alright..."
                scene schoolbathroombrittany04 with dissolve
                $ renpy.pause(1.0, hard=True)
                br "Thanks for lifting my spirits up... I've been so stressed lately with the pageant coming up..."
                $ lust_points[1] += 2
                $ score += 2
                show lust02:
                    xalign 0.3 yalign 0.6
                    linear 1.0 yalign 0.4
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust02
                p "You'll win for sure, don't worry..."
                scene schoolbathroombrittany03 with dissolve
                $ renpy.pause(1.0, hard=True)
                br "You haven't seen me crying, is that clear?"
                p "Crystal clear. My lips are sealed."
                br "I should go now..."
                jump SchoolChoiceDay05
            "It's a sign you need company. Male company preferably...":
                scene schoolbathroombrittany02b with dissolve
                $ renpy.pause(1.0, hard=True)
                br "No I don't! I'm perfectly fine being single, thank you very much. Now shoo, shoo little boy!"
                if (lust_points[1] >=1):
                    $ lust_points[1] -=1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.6 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                if (lust_points[1] ==0):
                    pass
                if (lust_pointsB[1] >=1):
                    $ lust_points[1] -=1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.6 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                if (lust_pointsB[1] ==0):
                    pass
            "Yeah, I do that too. I stare at the mirror and admire my huge muscles and say \"I'm da man, I'm DA MAN!\".":
                if (blacktop05 == True):
                    scene schoolbathroombrittany06black with dissolve
                    $ renpy.pause(1.0, hard=True)
                else:
                    scene schoolbathroombrittany06 with dissolve
                    $ renpy.pause(1.0, hard=True)
                br "Pff, pathetic! Now leave me alone little boy, I need to pamper myself."
                jump SchoolChoiceDay05


    "Yes, I agree your Magnificent Fabulousness.":
        scene schoolbathroombrittany02 with dissolve
        $ renpy.pause(1.0, hard=True)        
        br "What? Ah, it's you. Another admirer of my great beauty I presume?"
        p "How could anyone not be your most devoted admirer?"
        $ lust_points[1] += 1
        $ score += 1
        show lust01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        br "You're right, it boggles the mind. But I'll prove my detractors wrong Friday evening when I retain my crown!" 
        br "Now be gone loyal subject, your Queen needs to finish putting her make-up on!"
        jump SchoolChoiceDay05

    "I have a present for you Brittany." if (wristband == True):
        scene schoolbathroombrittany02 with dissolve
        $ renpy.pause(1.0, hard=True)        
        br "Oh really? What is it? It'd better be a present that befits a princess like me!"
        p "Yes it is, look!"
        scene schoolbathroombrittany02c with dissolve
        br "Oh my God, it's beautiful, it must have cost ssoo much too since it's golden!"
        $ lust_points[1] += 3
        $ score += 3
        show lust03:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust03
        show wristband
        show square
        play sound "Sounds/lost.mp3"
        "You gave away a wristband."
        hide square
        hide wristband
        $ wristband = False
        p "Yes, I spent all my money on this for you, but it was worth it your Magnificient Beautifulness."
        br "Well, thank you [name]? Is that right? I might see you around and grant you another audience. Now be gone, I need to finish putting my make-up on!"
        jump SchoolChoiceDay05
    "Walk past her and ignore her":
        if (blacktop05 == True):
            scene schoolbathroombrittany05black with dissolve
            $ renpy.pause(1.0, hard=True)
        else:
            scene schoolbathroombrittany05 with dissolve
            $ renpy.pause(1.0, hard=True)
        br "Hey you, look at me!"
        if (blacktop05 == True):
            scene schoolbathroombrittany06black with dissolve
            $ renpy.pause(1.0, hard=True)
        else:
            scene schoolbathroombrittany06 with dissolve
            $ renpy.pause(1.0, hard=True)
        p "Why? I prefer to look at myself. Yeah, I'm da man, I'm DA MAN!"
        br "Pff, pathetic! Now leave me alone little boy, I need to pamper myself."
        jump SchoolChoiceDay05

    "Hey Brittany, José slept with Kate. It's clear he's going to vote for her Friday night." if (katejosewin == True) and (brittanyjosewin == False):
        scene schoolbathroombrittany02 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What? How could he... This is a crime of lese-majesty that shall not go unpunished!"
        scene schoolbathroombrittany04 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Don't cry, the guy's a loser anyway..."
        if (lust_pointsB[1] >= 2):
            $ lust_pointsB[1] -=2
            show challengerlustminus02:
                xalign 0.2 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide challengerlustminus02
        if (lust_pointsB[1] == 1):
            $ lust_pointsB[1] -=1
            show challengerlustminus01:
                xalign 0.2 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide challengerlustminus01
        if (lust_pointsB[1] == 0):
            pass
        scene schoolbathroombrittany03 with dissolve
        $ renpy.pause(1.0, hard=True)        
        br "I need... to go... Thanks for letting me know [name]."
        $ lust_points[1] +=1
        show lust01:
            xalign 0.2 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        p "Alright...Maybe you and I? One day..."    
        jump SchoolChoiceDay05

    "Hey Brittany, José is getting real close to Kate. I wonder why..." if (lust_pointsB[1] >=6) and (lust_pointsB[1] <=9) and (brittanyjosewin == False):
        scene schoolbathroombrittany02c with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What? How could he... This is a crime of lese-majesty that shall not go unpunished!"
        $ lust_pointsB[1] -=1
        show challengerlustminus01:
            xalign 0.2 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus01
        scene schoolbathroombrittany02b with dissolve
        $ renpy.pause(1.0, hard=True)        
        br "I am going to talk to him and reason this knucklehead!"
        jump SchoolChoiceDay05
        
label SchoolBathroom01Day05c:
scene schoolbathroom01 with dissolve
$ renpy.pause(1.0, hard=True)
p "No one seems to be around..."
p "I might as well go for a pee while I'm here..."
scene schoolbathroom02 with dissolve
$ renpy.pause(1.0, hard=True)
p "One of the stalls seem different from the others... Let's investigate."
scene schoolbathroom03 with dissolve
$ renpy.pause(1.0, hard=True)
p "I see, it seems to be the gloryhole stall. Every private school in America has one of them, it's a sign that the school pampers its students." 
menu:
    "Stick your cock through the outside wall and wait.":
        jump GloryholeDay05
    "Have a piss and leave.":
        play sound "Sounds/peeing.mp3"
        $ renpy.pause(10.0, hard=True)
        p "Aaah, I needed that."
        jump SchoolChoiceDay05

label GloryholeDay05:
$ seengloryhole05 = True
if (seengloryhole03 == True):
    if (d2rollglory == 0):
        jump GloryholeDay05c     
    if (d2rollglory == 1):
        jump GloryholeDay05b       

$ d2rollglory05=renpy.random.randint(0, 1)
if (d2rollglory05 == 0):
    jump GloryholeDay05b      
if (d2rollglory05 == 1):
    jump GloryholeDay05c 

label GloryholeDay05b:
if (blacktop05 == True):
    scene gloryhole01black with dissolve
    $ renpy.pause(1.0, hard=True)
else:
    scene gloryhole01 with dissolve
    $ renpy.pause(1.0, hard=True)
$ hour += 1
"I waited long enough. Nobody came to take the bait, I'm out of here."
scene schoolbathroom01 with dissolve
$ renpy.pause(1.0, hard=True)
jump SchoolChoiceDay05

label GloryholeDay05c:
if (blacktop05 == True):
    scene gloryhole01black with dissolve
    $ renpy.pause(1.0, hard=True)
else:
    scene gloryhole01 with dissolve
    $ renpy.pause(1.0, hard=True)
play sound "Sounds/footsteps.mp3"
$ renpy.pause(1.0, hard=True)
p "Oh, oh, I think I hear someone coming along."
scene gloryholebrit01 with dissolve
play sound "Sounds/surprise.mp3"
$ renpy.pause(1.0, hard=True)
p "Bingo, they've seen my monster dong sticking straight at them... Pity I can't see who it is..."
br "What a big cock mister! I don't know if my little mouth could take it... But it's so tempting..."
scene gloryholebrit02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Now she's taking a hold of it with one hand and... AAAH... nice... It feels so warm on my cock..."
label GloryHoleSuckDay05:
play sound "Sounds/gloryhole.mp3"
scene gloryholebrit03
$ renpy.pause(0.3, hard=True)
scene gloryholebrit04
$ renpy.pause(0.3, hard=True)
scene gloryholebrit03
$ renpy.pause(0.3, hard=True)
scene gloryholebrit02
$ renpy.pause(0.3, hard=True)
scene gloryholebrit03
$ renpy.pause(0.3, hard=True)
scene gloryholebrit04
$ renpy.pause(0.3, hard=True)
scene gloryholebrit03
$ renpy.pause(0.3, hard=True)
scene gloryholebrit02
$ renpy.pause(0.3, hard=True)
scene gloryholebrit03
$ renpy.pause(0.3, hard=True)
scene gloryholebrit04
$ renpy.pause(0.3, hard=True)
scene gloryholebrit03
$ renpy.pause(0.3, hard=True)
scene gloryholebrit02
$ renpy.pause(0.3, hard=True)
scene gloryholebrit03
$ renpy.pause(0.3, hard=True)
scene gloryholebrit04
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump GloryHoleSuckDay05
    "Cum":
        pass
p "Haa... She's sucking me sssoo good, I'm gonna blow my load!"
play sound "Sounds/ryancumming.mp3"
scene gloryholebrit05 with dissolve
$ renpy.pause(1.0, hard=True)
br "Glurb... (swallow).... mmmpf... (swallow)...."
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
p "Pfeeeww... She sucked me dry... Whoever she is, she's a pro..."
if (lust_pointsB[1] ==1):
    $ lust_pointsB[1] -=1
    show challengerlustminus01:
        xalign 0.7 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide challengerlustminus01
if (lust_pointsB[1] >=2):
    $ lust_pointsB[1] -=2
    show challengerlustminus02:
        xalign 0.7 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide challengerlustminus02
if (brittanyjosewin == True):
    br "That definitely isn't José's cock. It's much bigger than his, now I regret letting him fuck me..."
    p "(It sounded like Brittany... The fucking slut already fucked José before me though...)"
$ hour += 1
if (blacktop05 == True):
    scene gloryholebrit06black with dissolve
    $ renpy.pause(1.0, hard=True)
else:
    scene gloryholebrit06 with dissolve
    $ renpy.pause(1.0, hard=True)
play sound "Sounds/footsteps.mp3"
p "Oooh, it was Brittany! What a slut! Then again, I'm a he-slut too..."
menu:
    "Call her and let her know it was you":
        jump GloryHoleEnd01Day05
    "Stay put and wait for her to leave":
        jump GloryHoleEnd02Day05
        
label GloryHoleEnd01Day05:
scene gloryholebrit07 with dissolve
$ renpy.pause(1.0, hard=True)
p "Hey Brittany, that giant cock you sucked... It was mine! Ta-daa!"
br "Eek, you broke the unwritten rule that you should never reveal yourself to your gloryhole partner you moron!"
if (lust_points[1] >=1):
    $ lust_points[1] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.6 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
if (lust_points[1] ==0):
    pass
p "But, I thought..."
$ gloryholetold = True
br "Shut up already twerp! Get out of my sight!"
scene gloryholend with dissolve
$ renpy.pause(1.0, hard=True)
p "She's gone. Good thing I didn't mention she had some of my cum dripping out of her mouth..."
jump SchoolChoiceDay05
    
label GloryHoleEnd02Day05:
scene gloryholend with dissolve
$ renpy.pause(1.0, hard=True)
p "She's gone. Now I can do other stuff..."
jump SchoolChoiceDay05

label WillieCorridorDay05:
if (williequestdone == True):
    $ seenwillie05 = True
    jump PrincipalOfficeBackDay05
stop music
scene williecorridor with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/Willie.wav"
$ seenwillie05 = True
wi "Where do you think you're going lad?..."

if (vivianepic == True) and (cantgoback == False) and (williequest == True):
    jump PrincipalBackDay05b
menu:
    "None of your business.":
        wi "I've got me eyes on ya lad. I know you're trying to sneak into Principal Titsworthy's office..."
        scene willie02 with dissolve
        $ renpy.pause(1.0, hard=True)
        play sound "Sounds/keyswrangling.mp3"
        wi "But oh look, Willie has the keys. And only Willie."
        p "Alright. What do you want?"
        wi "Smart boy. Willie will open the door IF you get Willie a naked picture of... Viviane, your sports instructor."
        wi "She's the love of me life. Oh, Viviane, come to Willie, Willie will make you happy!"
        if (vivianejosewin == True):
            p "As it turns out, I already have a picture of her naked. Getting fucked by that douchebag José..."
            show willie02b with dissolve
            $ renpy.pause(1.0, hard=True)
            wi "What? Why did you let this little rascal get to you Viviane?"
            hide willie02b
            show willie02c with dissolve
            $ renpy.pause(1.0, hard=True)
            wi "I swear to God, I'll get him for that! Willie will not have his lass taken away from him!"
            scene willie03 with dissolve
            $ renpy.pause(1.0, hard=True)
            wi "I suppose I'll unlock the door for ya lad. But you have only five minutes, Willie is not getting into trouble for ya!"
            $ williequestdone = True
            jump PrincipalSnoopingDay05
        if (vivianejosewin == False):
            p "OK, I'll get you your picture you fucking pervert! But I strongly condemn your immorality."
            wi "So says the lad who wants to sneak into Principal Titsworthy's office! Take a hike! And come back with a sexy picture of my Viviane..."
            $ williequest = True
            jump SchoolChoiceDay05
    "I have an appointment with Principal Titsworthy.":
        wi "Oh yeah? Well, she ain't there, so that's a wee bit suspicious."
        p "I'll wait for her then."
        wi "No you won't. Move it lad or Willie will report you to the Principal. And you wouldn't want to cross her, I tell ya!"
        jump SchoolChoiceDay05

label PrincipalSnoopingDay05:
scene principalsnooping with dissolve
play music "Sounds/snooping.mp3"
$ d2rollofficeDay05=renpy.random.randint(0, 1)
if (d2rollofficeDay05 == 0):
    call screen officesnoop01day05
if (d2rollofficeDay05 == 1):
    call screen officesnoop02day05
$ renpy.pause(1.0, hard=True)
stop music
"I was too slow and didn't find the right folder... Now I have to leave or Willie will lock me up..."
jump SchoolChoiceDay05

label FoundFriedaGradeDay05:
scene principalsnooping
$ renpy.pause(1.0, hard=True)
stop music
p "Frieda...Frieda....Ah, there it is, now I'll change the F grade for an A. Piece of cake, I'm DA MAN!"
play sound "Sounds/Willie02.wav"
$ renpy.pause(2.0, hard=True)
$ friedachangedgrade = True
p "Let's get the hell out of here before the principal comes back..."
jump SchoolChoiceDay05

label LockerDay05:
$ seenlocker05 = True

if (seenlockerkate == False):
    jump LockerKate01Day05  
if (seenlockerbrit == False):
    jump BritLockerDay05  
 
label LockerEmpty02Day05:
scene lockerempty with dissolve
$ renpy.pause(1.0, hard=True)
$ seenlockerempty = True
p "There's no one around... Like everyone left school or something. And I'm here, wasting my time in empty corridors like an idiot."
jump SchoolChoiceDay05

label LockerKate01Day05:
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
        jump LockerKate08Day05
    "Well pick it up then.":
        k "Uh...oh...OK."
        scene lockerkate02
        $ renpy.pause(1.0, hard=True)
        k "Oooh, it's too far, I can't reach it...Uuh..."
        menu:
            "Well, bend over some more...":
                jump LockerKate03Day05
            "Offer to help":
                k "No, I'm...OK....Ooh, I hope my panties aren't...like... showing.... Are they?"
                menu: 
                    "Not at all, I can't see a thing. You can bend more.":
                        jump LockerKate03Day05
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
                        jump LockerKate03Day05
 
label LockerKate03Day05:
scene lockerkate03 with dissolve
$ renpy.pause(1.0, hard=True)
k "Like that?... I still can't find my pen...Oooh, Where is it?"
menu:
    "It's right in front of you, you dumb bimbo.":
        k "Oooh, yes, I see it now...Hee...hee..."
        play sound "Sounds/katehihi.mp3"
        jump LockerKate07Day05
    "Look some more, meanwhile, I'll probe behind you, it might be stuck somewhere...":
        k "Ooh, OK...hee...hee..."
        play sound "Sounds/katehihi.mp3"
        if (blacktop05 == True):
            scene lockerkate04black with dissolve
            $ renpy.pause(1.0, hard=True)        
        else:
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
                jump LockerKate08Day05
            "Don't mind me, I'm in control of the situation...":
                jump LockerKate07Day05

label LockerKate07Day05:
scene lockerkate06 with dissolve
$ renpy.pause(1.0, hard=True)
k "Uh...OK...I'll continue looking... Oh, look, I found my pen!"
label LockerKate08Day05:
scene lockerkate07 with dissolve
$ renpy.pause(1.0, hard=True)
p "Well done, you're such a smart girl! By the way, it's actually a pencil, not a pen."
label KateLockerEndDay05:
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
    jump SchoolChoiceDay05
menu:
    "How about this afternoon at 5 or 6pm at my place for our photoshoot session?" if (katephotoasked == True):
        $ katephotoplanned05 = True
        k "Ooh, yeah, yippee! I'll DEFINITELY be there!"
        jump SchoolChoiceDay05
    "Ok, see you tomorrow Kate!":
        k "Ooh, yeah, see you tomorrow [name], hee hee!"
        play sound "Sounds/katehihi.mp3"
        jump SchoolChoiceDay05
        
label BritLockerDay05:
scene
stop music
play sound "Sounds/footsteps.mp3"
$ renpy.movie_cutscene("Day2/britlocker.ogv")
scene lockerbritmovie
show slowmo
call screen britslowmoDay05
screen britslowmoDay05:
    modal True
    button:
        xpos .82
        ypos .9
        xysize(120, 50)
        action Jump ("BritSlowMoDay05")
label BritSlowMoDay05:
play sound "Sounds/britlockerslowmo.mp3"
$ renpy.movie_cutscene("Day2/britlockerslowmo.ogv")
scene lockerbritmovie
$ renpy.pause(1.0, hard=True)

label LockerBrit01Day05:
$ seenlockerbrit = True
scene lockerbrit01 with dissolve
$ renpy.pause(1.0, hard=True)
j "Hey babe, how are you doing?"
br "Fabulous, I just got this new outfit on the weekend, do you like?"
j "Fuck yeah, you look so hot in it, you're sure to win the pageant on Friday babe..."
if (brittanyjosewin == False):
    $ lust_pointsB[1] +=1
    show challengerlustplus01:
        xalign 0.3 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide challengerlustplus01

menu:
    "Continue eavesdropping on the conversation":
        jump LockerBritEavesdropDay05
    "Barge in on the conversation":
        jump LockerBrit02Day05
        
label LockerBrit02Day05:
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
        jump SchoolChoiceDay05
    "I might be a junior student, but I'm a senior in bed.":
        show lockerbrit02b
        br "So boring, another wannabe stud. I only date REAL studs."
        j "Yeah, like ME. Do you hear that [name]?"
        br "I don't recall saying YOU were a REAL stud either..."
        show lockerbrit02c
        j "But, babe, everyone knows I'm the school stud..."
        br "Well, maybe I should look OUTSIDE of this school... A goddess like me deserves the BEST..."
        jump BritLocker03Day05
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
        jump BritLocker03Day05

label BritLocker03Day05:
scene lockerbrit02 with dissolve
$ renpy.pause(1.0, hard=True)
br "I've wasted enough time talking to you. A true princess like me needs to spend more time pampering herself."
br "Do not disturb me until I grant you permission."
menu:
    "Sure ma'am, at your cervix your Magnificent Beautifulness! (snickers)":
        show lockerbrit02b
        br "Be gone!"
        jump SchoolChoiceDay05
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
        jump SchoolChoiceDay05
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
            jump SchoolChoiceDay05
        menu: 
            "José is lying. It was actually 4 dollars.":
                br "Oh my God, that's even worse!!! Be gone and keep your cheap wristband!"
                jump SchoolChoiceDay05
            "Oh, hang on a minute, I seem to have given you the wrong one. My bad, this one was meant for...err.. Kate.":
                br "That would indeed suit that cheap bimbo... Who dares try to claim my throne as bikini pageant queen this year again!"
                br "Come back with your \"proper\" present tomorrow then. Or else..."
                p "Yeah... Of course... Ahem... Thank you, your...err.. majesty."
                $ britpresentfail = True
                jump SchoolChoiceDay05

label LockerBritEavesdropDay05:
scene lockerbrit01 with dissolve
if (brittanyjosewin == False):
    j "Listen babe, why don't we meet tonight at my place?"
    if (lust_pointsB[1]>=8):
        br "To do what exactly?"
        j "Talk about how beautiful you are and how hot you look in those expensive outfits you wear..."
        br "Oh, yes, I love that topic of conversation!"
        window hide
        if (brittanyjosewin == False):
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
        jump LockerBrit02Day05
    "Leave, you are defeated, what's the point in arguing...":
        jump SchoolChoiceDay05

label SportsHallDay05:
stop music

if (williequest == True) and (williequestdone == False):
    jump SportsHallDay05b
if (williequest == True) and (williequestdone == True):
    jump SportsHallDay05c

label SportsHallDay05c:
scene vivianewillie01 with dissolve
$ renpy.pause(1.0, hard=True)
$ seenhall05v = True
vi "Wh... What are you doing here Willie?"
wi "Come on lass, ya know you want Willie, take off yer clothes now!"
menu:
    "Yeah, I wanna see that too!":
        scene vivianewillie02 with dissolve
        $ renpy.pause(1.0, hard=True)
        wi "She's mine lad, get lost! Willie will not share her, you can fuck one of your cheap lasses!"
        scene vivianewillie04 with dissolve
        $ renpy.pause(1.0, hard=True)
        vi "Who the hell do you think I am??? Now YOU fuck OFF Willie before I beat you into a pulp!..."
        scene vivianewillie05 with dissolve
        $ renpy.pause(1.0, hard=True)
        vi "...And YOU, you little shit, I'll remember your cowardice! Get out of here! And you'd better be ready for tommorow's swimming practice!"
        $ lust_points[23] -= 2
        $ score -= 2
        show lustminus02:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus02 
        jump SchoolChoiceDay05
    "Leave her alone you Scottish inbred!":
        scene vivianewillie02 with dissolve
        $ renpy.pause(1.0, hard=True)        
        wi "Or else what lad? You have a deal with Willie remember..."
        jump SportsHall02Day05c
    "Quietly leave and let them sort it out.":
        jump SchoolChoiceDay05

label SportsHall02Day05c:
menu:
    "Err.. OK, I'll leave you two to it then.":
        scene vivianewillie04 with dissolve
        $ renpy.pause(1.0, hard=True)
        vi "Well, what a gentleman! Now YOU fuck OFF Willie before I beat you into a pulp..."
        wi "Willie didn't do nothing wrong..."         
        p "I would have done something, I swear! But it was quite clear you can take care of yourself..."
        scene vivianewillie05 with dissolve
        $ renpy.pause(1.0, hard=True)
        vi "...And YOU, you little shit, I'll remember your cowardice! Get out of here! And you'd better be ready for tommorow's swimming practice!"
        $ lust_points[23] -= 2
        $ score -= 2
        show lustminus02:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus02 
        jump SchoolChoiceDay05
    "We have no such thing as a deal!":
        wi "Now now, lad...I think you'd better remember what you did for me... Should I tell Viviane?" 
        vi "What is he talking about???"
        menu:
            "Nothing... He's just a pervert! I'll beat him up for you Viviane!":
                scene vivianewillie03 with dissolve
                $ renpy.pause(1.0, hard=True)
                wi "Willie will show ya, lad!"
                if (strength >= 9):
                    show williebeaten
                    p "I warned you, take that!"
                    play sound "Sounds/punch.mp3"
                    $ renpy.pause(1.0, hard=True)
                    scene vivianewillie02 with dissolve
                    $ renpy.pause(1.0, hard=True)
                    wi "Have mercy on Willie! Willie will leave!"                        
                    p "That's right, get the hell out of here!"
                    jump VivianeGratefulDay05
                if (strength <= 8):
                    show williebeat
                    wi "I warned ya, take that!"
                    play sound "Sounds/punch.mp3"
                    $ renpy.pause(1.0, hard=True)
                    p "I'm out of here, this crazy Scottish freak is actually STRONGER than me!"
                    scene vivianewillie05 with dissolve
                    $ renpy.pause(1.0, hard=True)
                    vi "You're such a weakling, it's embarrassing! Now get outta here! You'd better be ready for tomorrow's swimming practice!"
                    $ lust_points[23] -= 1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.3 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01 
                    jump SchoolChoiceDay05
            "Ah yes, I think I'll leave you to to it then... Bye Viviane!":
                scene vivianewillie05 with dissolve
                $ renpy.pause(1.0, hard=True)
                vi "I'll remember your cowardice! Get out of here! And you'd better be ready for tommorow's swimming practice!"
                $ lust_points[23] -= 1
                $ score -= 1
                show lustminus01:
                    xalign 0.3 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01 
                jump SchoolChoiceDay05
            "Pff, that was nothing! And anyway, it was YOUR idea!":
                wi "[name] here took a picture of you naked Viviane! What a wee weasel!"
                scene vivianewillie05 with dissolve
                $ renpy.pause(1.0, hard=True)
                vi "WHAT??? Get out of here you sick pervert!"
                $ lust_points[23] -= 2
                $ score -= 2
                show lustminus02:
                    xalign 0.3 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus02 
                jump SchoolChoiceDay05

label VivianeGratefulDay05:
scene vivianegrateful with dissolve
$ renpy.pause(1.0, hard=True)
vi "Well, thanks for helping me get rid of this vile pesky creature [name]!"
if (lust_points[23] ==9):
    window hide
    $ lust_points[23] += 1
    $ score += 1
    show lust01:
        xalign 0.3 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    vi "I see you for what you are now... A SEX GOD to ravish my body!"
    jump VivianeFuckDay05
if (lust_points[23] <=8):
    window hide
    $ lust_points[23] += 2
    $ score += 2
    show lust02:
        xalign 0.3 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    if (lust_points[23] >= 10):
        show epiclust:
            xalign 0.3 yalign 0.2
            zoom 0.5
            linear 2.0 zoom 1.0
        play sound "Sounds/epiclust.mp3"
        $ renpy.pause(4.0, hard=True)
        hide epiclust
        vi "I see you for what you are now... A SEX GOD to ravish my body!"
        jump VivianeFuckDay05
    if (lust_points[23] <= 7):        
        p "You're welcome, it was a piece of cake for me, I'm so strong!"
        vi "Yeah, yeah... Quit the bragging and concentrate on your swimming. We have practice tomorrow! I'll see you there [name]..."
        p "Sure Viviane..."
        jump SchoolChoiceDay05

menu:
    "Use pendulum on her" if (pendulumactive == True):
        jump VivianeHypnoDay05
    "Spray yourself with pheromones" if (pheromone == True):
        jump VivianePheromonesDay05
    "You're welcome, it was a piece of cake for me, I'm so strong!":
        vi "Yeah, yeah... Quit the bragging and concentrate on your swimming. We have practice tomorrow! I'll see you there [name]..."
        p "Sure Viviane..."
        jump SchoolChoiceDay05
        

label VivianeHypnoDay05:
scene vivianehypno with dissolve
$ renpy.pause(1.0, hard=True)
show pendulum03
$ renpy.pause(1.0, hard=True)
p "Just watch this pendulum as I wiggle it in front of your eyes Viviane..."
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
if (lust_points[23] ==8):
    window hide
    $ lust_points[23] += 2
    $ score += 2
    show lust02:
        xalign 0.3 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    vi "I see you for what you are now... A SEX GOD to ravish my body!"
    jump VivianeFuckDay05
if (lust_points[23] ==9):
    window hide
    $ lust_points[23] += 1
    $ score += 1
    show lust01:
        xalign 0.3 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    vi "I see you for what you are now... A SEX GOD to ravish my body!"
    jump VivianeFuckDay05
    
label VivianePheromonesDay05:
scene vivianesmell with dissolve
play sound "Sounds/sniffing.mp3"
$ renpy.pause(1.0, hard=True)
vi "What is this smell... It's not the chlorine from the pool... It's... amazing. ANd it's making me ssoo. horny too..."
p "My spray is now empty... I guess I won't be able to use it again."
show pheromone
show square
play sound "Sounds/lost.mp3"
"You lost a pheromone spray."
hide square
hide pheromone
$ pheromone = False
if (lust_points[23] ==8):
    window hide
    $ lust_points[23] += 2
    $ score += 2
    show lust02:
        xalign 0.3 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    vi "I see you for what you are now... A SEX GOD to ravish my body!"
    jump VivianeFuckDay05
if (lust_points[23] ==9):
    window hide
    $ lust_points[23] += 1
    $ score += 1
    show lust01:
        xalign 0.3 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    vi "I see you for what you are now... A SEX GOD to ravish my body!"
    jump VivianeFuckDay05

label VivianeFuckDay05:
scene vivianefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Maybe I should take this off, what do you reckon [name]?"
p "It certainly would be more convenient..."
scene vivianefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
vi "No haste tiger... I've locked the door, no one will disturb us..."
p "Well, it's a matter of my cock tearing my pants apart real soon..."
scene vivianefuck03 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Well then, take it out, what are you waiting for?..."
vi "And come closer to me...."

label VivianeFuckChoiceDay05:
scene vivianechoice with dissolve
$ renpy.pause(1.0, hard=True)
vi "So... What are you going to do to me now [name]?"
menu:
    "I want to take you up the arse and work my hip muscles!" if (vivianeanal == False):
        vi "Great idea! They really help improve the speed of your legs underwater..."
        jump VivianeAnalDay05
    "I'll hold you up while I pummel my great pile-driver in your mouth!" if (vivianeblow == False):
        vi "Mmh, that sounds so hot! Lift me up in your muscular arms and lick my pussy!"
        jump VivianeBlowDay05
    "Let's get on the floor so you can ride my huge dong!" if (vivianepussy == False):
        vi "So I'll be doing all the work? I guess you deserve it STUD!"
        jump VivianePussyDay05
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (vivianepussy == True) and (vivianeblow == True) and (vivianeanal == True):
        vi "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump VivianeMovieDay05

label VivianeAnalDay05:
$ vivianeanal = True
p "First, I'll lick that bunghole to warm it up..."
vi "A rimjob? Mmh, you really are a DIRTY boy aren't you [name]?"
scene vivianelick01 with dissolve
$ renpy.pause(1.0, hard=True)
scene vivianelick02 with dissolve
play sound "Sounds/womansigh.mp3"
$ renpy.pause(1.0, hard=True)
vi "YYYES! Your tongue is making me tingle all over!"
scene vivianelick03 with dissolve
play sound "Sounds/womansigh.mp3"
$ renpy.pause(1.0, hard=True)
vi "You do that so well! But don't kiss me afterwards if you don't mind..."
play sound "Sounds/vivianelick.mp3"
scene vivianelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianelick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianelick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianelick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianelick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianelick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianelick03 with dissolve
$ renpy.pause(0.3, hard=True)
vi "Oooh, my little backdoor is now moist and ready for your massive teenage fuckmeat [name]!"
p "Then it's time to turn in into a wide gaping hole..."
scene vivianeanal01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "FUCK! You're sssooo BIG! I feel like I'm getting impaled on a giant spike!"
p "Hang on in there, I'm gonna spike your arse some more..."
scene vivianeanal02 with dissolve
$ renpy.pause(0.3, hard=True)
vi "YES! Fuck my arse [name]! FUCK ME HARD!"
label VivianeAnalDay05b:
play sound "Sounds/vivianeanal.mp3"
scene vivianeanal01 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeanal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeanal01 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeanal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeanal01
$ renpy.pause(0.3, hard=True)
scene vivianeanal02
$ renpy.pause(0.3, hard=True)
scene vivianeanal01
$ renpy.pause(0.3, hard=True)
scene vivianeanal02
$ renpy.pause(0.3, hard=True)
scene vivianeanal01
$ renpy.pause(0.3, hard=True)
scene vivianeanal02
$ renpy.pause(0.3, hard=True)
scene vivianeanal01
$ renpy.pause(0.3, hard=True)
scene vivianeanal02
$ renpy.pause(0.3, hard=True)
scene vivianeanal01
$ renpy.pause(0.3, hard=True)
scene vivianeanal02
$ renpy.pause(0.3, hard=True)
scene vivianeanal01
$ renpy.pause(0.3, hard=True)
scene vivianeanal02
$ renpy.pause(0.3, hard=True)
scene vivianeanal01
$ renpy.pause(0.3, hard=True)
scene vivianeanal02
$ renpy.pause(0.3, hard=True)
scene vivianeanal01
$ renpy.pause(0.3, hard=True)
scene vivianeanal02
$ renpy.pause(0.3, hard=True)
scene vivianeanal01
$ renpy.pause(0.3, hard=True)
scene vivianeanal02
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump VivianeAnalDay05b
    "Move on":
        pass
scene vivianeanal03 with dissolve
$ renpy.pause(1.0, hard=True)
vi "My God, it feels like my arse is nothing more than a gaping hole now..."
p "It sure looks like it from where I'm standing..." 
jump VivianeFuckChoiceDay05

label VivianeBlowDay05:
$ vivianeblow = True
scene vivianeoral01 with dissolve
play sound "Sounds/vivianeblow01.mp3"
$ renpy.pause(10.0, hard=True)
vi "Mmh, you're so strong holding me like that!"
p "That's cos I need to lick that tasty pussy of yours!"
vi "While I suck on that giant shaft of yours! It's a deal!"
label VivianeBlowDay05b:
scene vivianeoral02 with dissolve
play sound "Sounds/vivianeblow02.mp3"
$ renpy.pause(0.3, hard=True)
scene vivianeoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianeoral02 with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump VivianeBlowDay05b
    "Move on":
        pass    
vi "I think I dislocated my jaw..."
p "It happens...Let's move on to something else." 
jump VivianeFuckChoiceDay05    

label VivianePussyDay05:
$ vivianepussy = True
scene vivianecowgirl01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Keep steady mustang! This cowgirl is going to ride you into submission!"
p "Oh fuck, I think I'm in for a wild ride!" 
label VivianePussyDay05b:
scene vivianecowgirl02 with dissolve
play sound "Sounds/vivianecowgirl.mp3"
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene vivianecowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump VivianePussyDay05b
    "Move on":
        pass    
vi "How was it for you stallion?"
p "Damn, I feel like I rode all the way to California..." 
jump VivianeFuckChoiceDay05    

label VivianeMovieDay05:
scene vivianeprefuck with dissolve
p "I've pinned you down against the lockers... Time to smash the padlock on your uterus with my sledgehammer!"
vi "OOOh, you have the worst lines [name], but I forgive you because you're about to give me what I want, that fat young bullcock of yours! FUCK ME!"
play music "Sounds/vivianefuck.mp3"
show vivianefuck
show cum
call screen vivianefuckday05
screen vivianefuckday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("VivianeFuckCumDay05")

label VivianeFuckCumDay05:
hide vivianefuck
stop music
scene vivianecum01
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
vi "YES! Fill me up like a sperm tank!"
p "So strong! I'm cumming non-stop!"
vi "Mmmh, yes stallion, I can feel it sloshing around inside me! Pull out and dump the rest on my body please!"
scene vivianecum02 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "Oh, Fuck, still spraying, still ssoo good!"
vi "Damn boy, my pussy really got those great big cum factories of yours working overtime didn't they?"
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
scene vivianecum03 with dissolve
play sound "Sounds/kissing.mp3" 
$ renpy.pause(1.0, hard=True)
vi "Now kiss me stud! And come with me in the showers so we can get cleaned up!"
scene vivianecum04 with dissolve
play music "Sounds/shower.mp3"
$ renpy.pause(1.0, hard=True)
vi "Mmh, I love your body... And that MONSTERCOCK! Can you get hard again and fuck me?"
p "Sure I could, but I'm afraid I have to go Viviane. You know, training and getting ready for the swimming competition..."
vi "I understand stud... I wouldn't want to drain all your energy this week! (wink)"
$ vivianefucked = True
$ hour += 1
$ backdoor += 1
if (vivianejosewin == False):
    p "(She didn't notice I took a picture of her boobs plastered in my cum... Now I'll send it to José)."
    $ vivianewin = True 
if (teaganfucked == True) and (sophiafucked == True) and (achievement.has("faculty") == False):
    show achievement10:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement10
    $ achievement.grant("faculty")
stop music
jump SchoolChoiceDay05

label SportsHallDay05b:
$ seenhall05 = True
scene sportshall01 with dissolve
$ renpy.pause(1.0, hard=True)
p "The lockers are empty... But I can hear some sound coming from the girls shower area..."
menu:
    "Go and have a peek":
        jump SportsHall02Day05
    "Don't do it, you might get caught...":
        jump SchoolChoiceDay05

label SportsHall02Day05:
scene sportshall02 with dissolve
play music "Sounds/shower.mp3"
$ renpy.pause(1.0, hard=True)
p "It's Viviane, she's taking a shower, totally in the nude!"
p "Seems like the ideal opportunity to take a pic for Willie..."
p "I'll hide behind these lockers and use the zoom on my phone..."
scene sportshall03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Mmh, nice arse...We can't really see her face on that one though, I'll take another one or Willie might complain..."
scene sportshall04 with dissolve
$ renpy.pause(1.0, hard=True)
p "Look at those abs, she's so fit... And those tits..."
p "Willie is bound to be happy with those shots. It's time to quietly leave before Viviane notices me."
$ vivianepic = True
menu:
    "Go back to the Principal's office (+1hr because it's far)":
        $ hour += 1
        jump PrincipalBackDay05
    "Do something else":
        $ cantgoback = True
        jump SchoolChoiceDay05

label PrincipalBackDay05:
$ d2principalback05=renpy.random.randint(0,1)  
if (d2principalback05 == 0):
    scene williecorridor with dissolve
    $ renpy.pause(1.0, hard=True)
    label PrincipalBackDay05b:
    p "I got your pics... Now let me in."
    wi "Willie will check them first. Hand me that phone lad."
    scene willie04 with dissolve
    $ renpy.pause(1.0, hard=True)
    wi "Rhooo. Yeah, my Viviane, you were made for Willie. Mmh..."
    p "Are you... like touching yourself you sick perv?"
    wi "Shut your gob lad. Let Willie be. And you'd better not tell anyone about our little secret."
    scene willie03 with dissolve
    $ renpy.pause(1.0, hard=True)
    $ williequestdone = True
    wi "I suppose I'll unlock the door for ya lad. But you have only five minutes, Willie is not getting into trouble for ya!"
    jump PrincipalSnoopingDay05

if (d2principalback05 == 1):
    jump PrincipalOfficeBackDay05

label PrincipalOfficeBackDay05:
scene principalback01 with dissolve
$ renpy.pause(1.0, hard=True)
so "What are you doing here? Can't you see I'm busy?"
menu:
    "Ah. Yes, I got the wrong door sorry.":
        so "Apparently, you can't read. It says \"Principal's Office\" in huge letters on the door. Now get out!"
        jump SchoolChoiceDay05  
    "I'm interested in joining your campaign as a volunteer." if (principaldeal == False) and (postersaid == False):
        so "That's great, I can always use some extra help in putting posters up! Welcome on board!"
        so "I need some posters to be put up downtown. The posters are in the corner over there. Take a stack of them on your way out." 
        p "Will do Senator Titsworthy!"
        $ principaldeal = True
        jump SchoolChoiceDay05
   

label SchoolGym01Day05:
$ seenschoolgym05 = True
if (schoolgymchantelle == False):
    jump SchoolGymChantelleDay05
if (schoolgymchantelle == True):
    jump SchoolGymEmptyDay05

label SchoolGymEmptyDay05:
scene schoolgymempty with dissolve
$ renpy.pause(1.0, hard=True)
p "There's no one around, I could use this gym to train and get stronger..."
menu:
    "Do some heavy training, better equipment means I can cut on my routine time (+1hr)" if (workout == False):
        jump SchoolGymWorkoutDay05
    "Leave":
        jump SchoolChoiceDay05

label SchoolGymChantelleDay05:
    $ schoolgymchantelle = True
    play music "Sounds/gymmusic.mp3"
    scene chantellegym01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Chantelle is doing some curls... She hasn't seen me come in."
    menu:
        "Do some heavy training, better equipment means I can cut on my routine time (+1hr)":
            p "I hope you don't mind if I do some heavy training with barbells in my jockstrap?"
            ch "What?.. No, it's fine...Be my guest..."
            jump ChantelleRyanWorkoutDay05
        "Watch her for a while":
            jump SchoolGymChantelle02Day05

label ChantelleRyanWorkoutDay05:
stop music
scene
play music "Sounds/workoutgroan.mp3"
$ renpy.movie_cutscene("Day2/schoolgymworkout.ogv", delay=-1, loops=-1, stop_music=False)
stop music
scene schoolgymworkout01
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
p "That was great, I can feel my muscles getting bigger and stronger already..."
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
$ muscleman += 1
p "What next?"
ch "This..is going too fast...maybe... I don't want to lose Nikki's friendship...sorry...I shouldn't have..."
p "But...What did I do wrong? It's not fair!"
ch "Another time maybe [name]... Let's leave it at that for now...I...should go now..."
jump SchoolChoiceDay05

label SchoolGymChantelle02Day05:
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
        jump SchoolGymChantelle03Day05
    "Of course, I only use the biggest weights around all the time, piece of cake for me!":
        ch "Mmh, I want to see that..."
        jump SchoolGymChantelle04Day05
    "Actually, I was planning on a serious routine with barbells, but I need to concentrate...(+1hr)":
        ch "Sure, I'll continue my exercises and I'll leave you alone, don't worry..."
        p "Also, I like to train with my shorts and tank top off, hope you don't mind..."
        ch "Ooh? No... I don't mind..."
        jump ChantelleRyanWorkoutDay05
        
label SchoolGymChantelle03Day05:
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
if (lust_points[2] >= 8) and (nikkifucked == True):
    menu:
        "There's another muscle I'd like to work out...":
            ch "Well I'm not taking care of it here!... Not today anyway...! Bye bye [name]!"
            $ hour += 1
            scene schoolgymempty with dissolve
            $ renpy.pause(1.0, hard=True)
            p "Jeezus, what a tease!"
            p "Now I lost an hour and this routine was not enough to build up my strength."
            menu:
                "Do some further proper heavy training (+1hr)":
                    jump SchoolGymWorkoutDay05   
                "Leave": 
                    jump SchoolChoiceDay05
            
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
        jump SchoolGymWorkoutDay05   
    "Leave": 
        jump SchoolChoiceDay05
 
label SchoolGymChantelle04Day05:
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
            jump SchoolGymWorkoutDay05
        "Leave":
            jump SchoolChoiceDay05
         
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
if (lust_points[2] >= 8) and (nikkifucked == True):
    menu:
        "There's another muscle I'd like to work out...":
            ch "Well I'm not taking care of it here!... Not today anyway...! Bye bye [name]!"
            $ hour += 1
            scene schoolgymempty with dissolve
            $ renpy.pause(1.0, hard=True)
            p "Jeezus, what a tease!"
            p "Now I lost an hour and this routine was not enough to build up my strength."
            menu:
                "Do some further proper heavy training (+1hr)":
                    jump SchoolGymWorkoutDay05   
                "Leave": 
                    jump SchoolChoiceDay05
p "You almost got me, and now I've got a massive tent in my strap..."
ch "Well I'm not taking care of it here!... Not today anyway...! Bye bye [name]!"
$ hour += 1
p "Jeezus, what a tease!"
p "Now I lost an hour and this routine was not enough to build up my strength."
menu:
    "Do some further proper heavy training (+1hr)":
        jump SchoolGymWorkoutDay05
    "Leave":
        jump SchoolChoiceDay05
   
label SchoolGymWorkoutDay05:
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
jump SchoolChoiceDay05


label NurseDay05:
if (discoverclinic == False):
    jump NurseDay05b

scene clinic01 with dissolve
$ seennurse05 = True
$ renpy.pause(1.0, hard=True)
je "Oh, hello [name]. I'm still waiting for your test results from the latest sample that was... err... collected."
je "And I'm afraid I'm rather busy this afternoon."
menu:
    "I actually just came for my big friend: my massive shaft would like a nice sloppy handjob...":
        scene nurseangry with dissolve
        $ renpy.pause(1.0, hard=True)
        je "I beg you pardon??? What kind of cheap whore do you think I am? Get out of here immediately!"
        window hide
        $ lust_points[10] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.2 yalign 0.6
            linear 1.0 yalign 0.8
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        p "Gee, calm down, I was just kidding..."
        jump SchoolChoiceDay05
    "I injured my leg a bit. Right near my groin area.":
        scene nurseangry with dissolve
        $ renpy.pause(1.0, hard=True)
        je "How stupid do you think I am? Get out of here, I'm too busy to listen to your puerile ramblings."
        jump SchoolChoiceDay05

label NurseDay05b:
scene clinic01 with dissolve
$ seennurse05 = True
$ renpy.pause(1.0, hard=True)
if (seennurse04 == False):
    je "Oh, hello [name]. The... hum... test results for your sperm sample came back and the clinic says they would like to extract some more for further analysis..."
    menu:
        "What does that mean exactly?":
            je "They wouldn't elaborate but they claimed it was very important... I could take you there by car, it's not far away and we would get there in no time at all!"
            je "And you'll be next to the beach if you wanted to get there afterwards..."
            menu:
                "Ok, why not.":
                    je "Great! I'll get dressed and we can be on our way."
                    jump ClinicDay05
                "No way, I am not a number, I am a free man! DA MAN actually.":
                    scene clinic02 with dissolve
                    $ renpy.pause(1.0, hard=True)
                    je "Mmh, that's disappointing, I was really looking forward to making a fortune exploiting... I mean really looking forward to finding out the quality of your sperm."
                    $ lust_points[10] -=1
                    $ score -=1
                    show lustminus01:
                        xalign 0.2 yalign 0.4
                        linear 1.0 yalign 0.6
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                    jump SchoolChoiceDay05
        "What's in it for me?":
            je "I'll give you 5 dollars if you come with me to the clinic right now."
            je "It's not far, we'll get there in no time by car. And you'll be next to the beach if you wanted to get there."
            menu:
                "Ok, why not.":
                    $ money += 5
                    je "Great! I'll get dressed and we can be on our way."
                    jump ClinicDay05
                "Not interested, I have other plans for the day.":
                    scene clinic02 with dissolve
                    $ renpy.pause(1.0, hard=True)
                    jump SchoolChoiceDay05
        "I'm too busy this afternoon, another time.":
            je "I hope you decide to take them up on their offer soon. Like tomorrow..."
            scene clinic02 with dissolve
            $ renpy.pause(1.0, hard=True)
            jump SchoolChoiceDay05
        
label ClinicDay05:
scene clinic03 with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
$ discoverclinic = True
show addedlocation:
    xalign 0.4 yalign 0.3
    linear 1.0 yalign 0.1
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide addedlocation
je "Come on, Doctor Stains is waiting for us."
stop music
scene clinic04 with dissolve
$ renpy.pause(1.0, hard=True)
dr "Ah, welcome Jennifer, I was eagerly awaiting both of you. And I presume this is our \"patient\", correct?"
je "Yes doctor. [name], I would like you to meet Dr Stains, a world expert on male fertility."
dr "I will call nurse Racque immediately, she will assist in the procedure."
p "What \"procedure\"?"
dr "The semen extraction of course. Please get undressed and sit on the exam table. Don't worry, the procedure is painless. Quite the opposite in fact."
scene clinic05 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, that nurse has indeed a nice \"rack\". Instant boner material."
ra "Oh Doctor Stains, another horse-hung boy for me to play with? You are really spoiling me! And this one looks EXTRA-LARGE too!"
dr "Please remain professionnal nurse Racque. The patient needs a semen extraction. A LARGE semen extraction. Set the machine to maximum power if you please."
scene clinic06 with dissolve
$ renpy.pause(1.0, hard=True)
ra "My pleasure doctor. Please lay down and relax, I will first get your cock hard and ready for extraction... I'm sure showing you my tits will do the trick."
je "Doctor, this sounds highly inappropriate!"
dr "Standard procedures nurse Bigguns. I suggest you also strip down for the boy, he needs maximal sexual stimulation in order to deliver the largest possible load."
je "But... Doctor! I am a married woman!"
dr "Your husband will never know, we take doctor confidentiality very seriously in our clinic. Now do as you're told and show us ya tits for Christ's sake!"
scene clinic07 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Or maybe you are an ass man. In that case, my big fake bum implants will be more to your liking..."
dr "Now move over to the other side of the patient and assist nurse Racque in helping that boy achieve the hardest possible erection..."
je "I... did not expect the procedure to follow such a protocol."
dr "Standard protocol nurse Bigguns, I wrote it myself, I should know. Now move along, I think a titjob is in order."
scene clinic08 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Ooh, YES! A DOUBLE-TITFUCK! What do you say Jennifer? Wanna rub your big boobies against mine and this boy's fuckstick?"
je "Do we really need to? He seems to be getting bigger and harder already..."
ra "Of course we do, Dr Stains said so. And anyways, why wouldn't you want to rub your tits against such a massive pecker? Really..."
je "Well... Fine, I suppose so, if it's for science..."
scene clinic09 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Just do as I do. See? He's so big, his cock sticks way past our giant racks. He seems to like it a lot too, since he's pouring precum all over them..."
je "This is... so lewd... And yet so thrilling at the same time..."
window hide
$ lust_points[10] +=1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
scene clinic10 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Now is the time to really pump his rod with our big tits..."
play sound "Sounds/doubletitfuck.mp3"
scene clinic11 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic10 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic11 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic10 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic11 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic10 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic11 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic10 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic11 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic10 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic11 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic10 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic11 with dissolve
$ renpy.pause(0.3, hard=True)
scene clinic10 with dissolve
$ renpy.pause(0.1, hard=True)
scene clinic11 with dissolve
$ renpy.pause(0.1, hard=True)
scene clinic10 with dissolve
$ renpy.pause(0.1, hard=True)
scene clinic11 with dissolve
$ renpy.pause(0.1, hard=True)
scene clinic10 with dissolve
$ renpy.pause(0.1, hard=True)
scene clinic11 with dissolve
$ renpy.pause(0.1, hard=True)
scene clinic10 with dissolve
$ renpy.pause(0.1, hard=True)
scene clinic11 with dissolve
$ renpy.pause(0.1, hard=True)
scene clinic10 with dissolve
$ renpy.pause(0.1, hard=True)
scene clinic11 with dissolve
$ renpy.pause(0.1, hard=True)
p "Oh God, this is so good, I'm about to bust my nut!"
ra "Not so fast cowboy, the extractor needs to be placed over your glans... Jennifer, please insert his cockhead into the extractor's opening while I set the computer up...."
scene clinic12 with dissolve
play music "Sounds/extractor.mp3"
$ renpy.pause(1.0, hard=True)
ra "Hurry up, we don't want to spill one drop of his genetically-superior juices!"
je "I'm trying to do my best... But his shaft is so thick!"
window hide
$ lust_points[10] +=1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
scene clinic13 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Maximum power! Hear that? that's the semen extractor working full time... It will suck up all his cum when he ejaculates and deliver it directly into the receptacle..."
p "SHIT! This thing is rubbing against my helmet... Sssooo good.... AAAAH"
play sound "Sounds/cumming.mp3"
$ renpy.pause(3.0, hard=True)
ra "That's good stud! Keep cumming, don't ever stop until your giant balls are TOTALLY DRAINED!"
scene clinic14 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
je "I'm having trouble keeping the extractor steady, his cock is blasting so powerfully! And I'm afraid we are losing some, it's trickling in thick rivulets down his shaft!"
scene clinic15 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
ra "It's fine, we already have over a quart of his tasty spunk in the receptacle and there's still cum pouring into it!"
ra "What a GIGANTIC load boy, this is the BIGGEST one I ever pumped out of a patient!"
je "Wow... Such a huge load... I didn't even know it was possible for a human being to cum that much...! It's so much more than my hubby..."
window hide
$ lust_points[10] +=1
$ score += 1
show lust01:
    xalign 0.1 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
dr "That is indeed an exceptional load... Please bring the receptacle over to the lab for analysis once the boy is done cumming like a firehose into the extractor nurse Racque..."
ra "Of course doctor, I believe he is almost done now..."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.7 yalign 0.6
    linear 1.0 yalign 0.8
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
p "Oh fuck! My balls.... Hurts so much... I'm drained... FUCK!"
$ hour += 1
stop music
scene clinic04 with dissolve
$ renpy.pause(1.0, hard=True)
dr "Well done boy. You gave us a large enough quantity of sperm to finish our analysis. You can come back anytime to make a sperm donation..."
menu:
    "What? I'm not getting paid for that?":
        dr "Err... No, this is a... err... charitable organization. You did it FOR SCIENCE, get it?"
        dr "Now off you go, I have some patients with tiny useless noodle dicks to attend to."
        jump ClinicEndDay05
    "My pleasure doctor. Can I have nurse Racque's phone number?":
        dr "That bimbo? Trust me, you don't want to get anywhere near her, she's got more venereal diseases than a president who fucks pornstars for a living."
        je "I am very disappointed by your non-commitment to this scientific endeavor!"
        window hide
        $ lust_points[10] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.1 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
        dr "Now off you go, I have some patients with tiny useless noodle dicks to attend to."
        jump ClinicEndDay05
    "I'll think about it. I am totally drained...":
        dr "And that is why you should come back. With just one load, you can give us enough sperm to impregn... I mean perform lots and lots of scientific tests."
        dr "Now off you go, I have some patients with tiny useless noodle dicks to attend to."
        jump ClinicEndDay05        

label ClinicEndDay05:
scene clinicentrance with dissolve
$ renpy.pause(1.0, hard=True)
p "It seems this place is like a shortcut between the Burbs and Tini-Wini Bikini Beach... I can go to either way in no time."
menu:
    "Go to the Burbs":
        jump BurbsDay05
    "Go to the beach":
        jump Beach01Day05

label Library01Day05:
$ seenlibrary05 = True
stop music
play music "Sounds/coughing.mp3"
if (seenjosemarialibrary == False):
    scene mariajoselibrary01 with dissolve
    $ renpy.pause(1.0, hard=True)
    $ seenjosemarialibrary = True
    $ spokemaria05 = True
    p "That fucking arsehole of José is chatting Maria up..."
    if (mariawin == True):
        p "But the dumb ass is too late, I already nailed her fine pussy.... he...he..."
    if (mariajosewin == True) and (mariafucked == False):
        p "He's rubbing it in, since he already fucked her and I didn't... What a douchebag!"
    if (mariajosewin == True) and (mariafucked == True):
        p "He's rubbing it in, since he already fucked her before I did... What a douchebag!"
    j "Talking to you is so fascinating, you really are the best librarian a school could ever wish for!"
    if (lust_pointsB[15] <= 9):
        ma "Oooh, thank you José, that's so kind of you... You are going to make me blush..."
        $ lust_pointsB[15] += 1
        show challengerlustplus01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustplus01
    menu:
        "Ignore them and find Frieda":
            jump Library04Day05
        "Barge in on the conversation":
            jump Library02Day05
        "Wait for José to leave and talk to Maria":
            jump Library03Day05
        "Leave the library and go elsewhere":
            jump SchoolChoiceDay05
        
if (seenjosemarialibrary == True):
    jump Library03Day05

label Library02Day05:
scene mariajoselibrary02 with dissolve
$ renpy.pause(1.0, hard=True)
j "What do you want worm?"
menu:
    "Your head on a spike":
        show mariajoselibrary02b with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "Stop it you two! I will not have two students fighting in my library!"
        $ lust_points[15] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        ma "Now disperse! In OPPOSITE directions..."
        jump LibraryChoiceDay05
    "I need to speak to Maria about some important stuff...":
        if (mariafucked == True):
            ma "Yes, it's best if you leave José... [name] and I have to... ahem... look for some books..."
            j "Fine, I'll leave then. But only because you asked Maria."
            scene marialibrary04 with dissolve
            $ renpy.pause(1.0, hard=True)
            ma "What's that important stuff you mentioned?"
            p "You really shouldn't let that creep talk to you. He's only trying to get into your panties."
            p "And his cock is tiny compared to my monster dong... (cockblock José)"
            ma "Fine, I'll follow your advice then..."
            "You cockblocked José."
            $ josemariacockblocked = True
            jump Library03Day05
        if (mariafucked == False):
            j "Oh really? How fascinating. I was just talking myself about important stuff to Maria... Fancy that..."
            show mariajoselibrary02b
            ma "And you literally barged in on the conversation. Which is very rude."
            $ lust_points[15] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.3 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            show mariajoselibrary02c
            j "Ha Ha... LOSER! I'm laughing so hard, I have to leave or I'll disturb the whole library... HA HA HA!"
            p "(Fucking arsehole...)"
            jump Library03Day05
            
label Library03Day05:
scene marialibraryb04 with dissolve
$ renpy.pause(1.0, hard=True)
$ spokemaria05 = True
ma "Hello [name]. What can I do for you today?"
menu:
    "I'm looking for a book on... how to have sex with a huge cock without hurting girls." if (mariafucked == False):
        scene marialibraryb03 with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "Oh, that is sssoo subtle..."
        jump LibraryChoiceDay05
    "Thanks for coming with us on the schooltrip yesterday. And the in-depth knowledge of Bigdong Falls you provided..." if (spokenbigdongteagan == True):
        if (savedlolly == True) and (mariafucked == False):
            ma "And thank you for saving Lolly... I never had the chance to properly thank you for it."
            if (lust_points[15] == 9):
                $ lust_points[15] +=1
                $ score += 1
                show lust01:
                    xalign 0.6 yalign 0.5
                    linear 1.0 yalign 0.3
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
            if (lust_points[15] <= 8):
                $ lust_points[15] +=2
                $ score += 2
                show lust02:
                    xalign 0.6 yalign 0.5
                    linear 1.0 yalign 0.3
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust02           
            if (lust_points[15] >= 10):
                show epiclust:
                    xalign 0.25 yalign 0.2
                    zoom 0.5
                    linear 2.0 zoom 1.0
                play sound "Sounds/epiclust.mp3"
                $ renpy.pause(4.0, hard=True)
                hide epiclust
                jump MariaFuckDay05  
        elif (savedlolly == True) and (mariafucked == True):
            ma "Your \"in-depth\" dwelling on the subject wasn't bad either... Actually, it was really... amazing..."
            ma "Ever since I left my husband, I have been rather lonely, and you have ignited a fire of lust within me... I'm so horny for you [name]..."
            ma "I can close the library early and let everyone leave so we can be left alone... What do you say?"
            menu:
                "Alright! Let's do it Maria! I'm horny too!":
                    ma "Wait for me here and get that cock hard then..."
                    jump MariaFuckDay05
                "I'd love to but I'm rather busy this afternoon I'm afraid...":
                    ma "Oh, why are you doing this to me? I hope you'll have more spare time tomorrow to quench my lust for your giant cock!"
                    p "Sure, I promise... See you Maria..."
                    jump LibraryChoiceDay05        
        ma "Yes... err... Let's not talk about this too much in a public space..."            
        jump LibraryChoiceDay05

label MariaFuckDay05:
stop music
scene mariapre01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "That's it, everyone left now... It's just you and me STUD!"
scene mariapre02 with dissolve
play sound "Sounds/maria01.mp3"
$ renpy.pause(6.0, hard=True)
ma "Do you like my large sumptuous tits? I bet you do... I can see a MASSIVE tent forming in your pants right now."
p "You bet!"
scene mariapre03 with dissolve
play sound "Sounds/maria02.mp3"
$ renpy.pause(1.0, hard=True)
ma "And what about my arse? Does it make you HARD stud?"
p "The massive tent in my pants says YES!"
scene mariapre04 with dissolve
$ renpy.pause(1.0, hard=True)
ma "And my pussy... It's been ssso long since it's been licked good by a pro... I hope YOU are a PRO!"
p "Oh yeah! Don't worry, I've got my muff-diving license!"
    
label MariaFuckChoiceDay05:
scene mariapre05 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Well, that's all good... But what are you going to do now STUD?"
menu:
    "Your pussy looks so tasty... I wanna have a scoop. Or two scoops, cos I'm bigly the best!" if (mariapussy05 == False):
        ma "Right, as long as you don't pretend to be an orang-utan..."            
        jump MariaPussyDay05
    "I'm gonna show how strong I am! Get ready for lift-off!" if (mariastanding == False):
        ma "Ooh, yes, I've also noticed your giant MUSCLES..."            
        jump MariaStandingDay05
    "Let's make sweet love on the floor." if (mariablow05 == False):
        ma "Good thing the floor was cleaned this morning by Willie then..."            
        jump MariaBlowDay05
    "I want to fuck that tender pussy of yours till I blow my load!" if (mariablow05 == True) and (mariastanding == True) and (mariapussy05 == True):
        jump MariaMovieDay05

label MariaPussyDay05:
$ mariapussy05 = True
scene mariapussylick with dissolve
play sound "Sounds/mariapussylick01.mp3"
$ renpy.pause(6.0, hard=True)
ma "Does my pussy taste good? Mmmh, I can feel your balls tightening already, they feel so heavy..."            
p "Get on the desk, I'm really going to dive into the abyss this time!"
scene mariadesk01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Are you good with tongue-twisters Maria?"
ma "Mmh, I don't know, but I bet YOU are! Show me STUD!"
label MariaPussyLickDay05b:
play sound "Sounds/mariapussydesk.mp3"
scene mariadesk02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariadesk01 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariadesk02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariadesk01 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariadesk02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariadesk01 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariadesk02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariadesk01 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariadesk02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariadesk01 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariadesk02
$ renpy.pause(0.3, hard=True)
scene mariadesk01
$ renpy.pause(0.3, hard=True)
scene mariadesk02
$ renpy.pause(0.3, hard=True)
scene mariadesk01
$ renpy.pause(0.3, hard=True)
scene mariadesk02
$ renpy.pause(0.3, hard=True)
scene mariadesk01
$ renpy.pause(0.3, hard=True)
scene mariadesk02
$ renpy.pause(0.3, hard=True)
scene mariadesk01
$ renpy.pause(0.3, hard=True)
scene mariadesk02
$ renpy.pause(0.3, hard=True)
scene mariadesk01
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump MariaPussyLickDay05b
    "Move on":
        pass
ma "I'll give you a stellar report for your work [name]..."
p "Alright! Let me show something else then..."
jump MariaFuckChoiceDay05

label MariaStandingDay05:
$ mariastanding = True
scene mariastanding01 with dissolve
play sound "Sounds/mariastanding01.mp3"
$ renpy.pause(12.0, hard=True)
ma "Ooh, I love it in that position, your massive tool gets so deep! AAAH! Yes, plunge it as far it will go!"
scene mariastanding02 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Ouch, let me adjust my pussy... to this giant... intruder... Yeah, that's better now..."
label MariaStandingDay05b:
scene mariastanding01 with dissolve
play sound "Sounds/mariastanding02.mp3"
$ renpy.pause(0.3, hard=True)
scene mariastanding02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding01 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding01 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding01 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding01 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding01 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding01 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariastanding02
$ renpy.pause(0.3, hard=True)
scene mariastanding01
$ renpy.pause(0.3, hard=True)
scene mariastanding02
$ renpy.pause(0.3, hard=True)
scene mariastanding01
$ renpy.pause(0.3, hard=True)
scene mariastanding02
$ renpy.pause(0.3, hard=True)
scene mariastanding01
$ renpy.pause(0.3, hard=True)
scene mariastanding02
$ renpy.pause(0.3, hard=True)
scene mariastanding01
$ renpy.pause(0.3, hard=True)
scene mariastanding02
$ renpy.pause(0.3, hard=True)
scene mariastanding01
$ renpy.pause(0.3, hard=True)
scene mariastanding02
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump MariaStandingDay05b
    "Move on":
        pass    
ma "Damn boy, you really know how to ful-FILL a woman's deepest desires!"
p "Yep, that's me, the biggest stud on the island! Let me show something else now."
jump MariaFuckChoiceDay05    

label MariaBlowDay05:
$ mariablow05 = True
scene mariasuckb01 with dissolve
play sound "Sounds/mariapreblow.mp3"
$ renpy.pause(9.0, hard=True)
ma "Oh my, what do we have here? That's the biggest cock I've ever seen, it's gonna take me forever to lick... all the way to the tip ..."
p "Take your time... But not too long!"
scene mariasuckb02 with dissolve
$ renpy.pause(1.0, hard=True)
ma "I'm sure you... gggllr... prefer to have my... warm mouth... mmmh... around it..."
p "Damn, you've got the whole apple-sized head in already!"
scene mariasuckb03 with dissolve
$ renpy.pause(1.0, hard=True)
label MariaBlowDay05b:
scene mariasuckb02 with dissolve
play music "Sounds/hallesuck02.mp3"
$ renpy.pause(0.3, hard=True)
scene mariasuckb03 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariasuckb02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariasuckb03 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariasuckb02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariasuckb03 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariasuckb02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariasuckb03 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariasuckb02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariasuckb03 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariasuckb02 with dissolve
$ renpy.pause(0.3, hard=True)
scene mariasuckb03
$ renpy.pause(0.3, hard=True)
scene mariasuckb02
$ renpy.pause(0.3, hard=True)
scene mariasuckb03
$ renpy.pause(0.3, hard=True)
scene mariasuckb02
$ renpy.pause(0.3, hard=True)
scene mariasuckb03
$ renpy.pause(0.3, hard=True)
scene mariasuckb02
$ renpy.pause(0.3, hard=True)
scene mariasuckb03
$ renpy.pause(0.3, hard=True)
scene mariasuckb02
$ renpy.pause(0.3, hard=True)
scene mariasuckb03
$ renpy.pause(0.3, hard=True)
scene mariasuckb02
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        jump MariaBlowDay05b
    "Move on":
        pass    
scene mariasuckb01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "I think your cock liked that... It's twitching in my hands..."
p "WOW! Is all I can say. And let's do something else too." 
jump MariaFuckChoiceDay05    

label MariaMovieDay05:
ma "I'm ready to get impaled by your huge dong and plastered in cum [name]!"
p "Well, that's good, cos it's exactly what's going to happen." 
play music "Sounds/mariafuckslow02.mp3"
show mariafuckslow02
show faster
call screen mariafuckslow02day05
screen mariafuckslow02day05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MariaFastFuckDay05")

label MariaFastFuckDay05:
stop music
hide faster
play music "Sounds/mariafuckfast02.mp3"
show mariafuckfast02
show cum
call screen mariafuckfast02day05
screen mariafuckfast02day05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MariaCumDay05")

label MariaCumDay05:
hide mariafuckslow02
hide mariafuckfast02
stop music
scene mariacumb01
window hide
play sound "Sounds/marialibrarycum01.mp3" 
$ renpy.pause(8.0, hard=True)
ma "Dump your seed all over my chest! Wow, there's so much of it in a single shot! Yes, cum for me baby!"
scene mariacumb02 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
scene mariacumb03 with dissolve
play sound "Sounds/marialibrarycum02.mp3" 
$ renpy.pause(7.0, hard=True)
ma "Damn, you're like a firehose! You've totally covered my tits in your cream... Mmmh, it's going to take me a while to clean up, you'd better leave before anyone catches us..."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.6 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ mariafucked = True
if (mariajosewin == False):
    p "(She didn't notice I took a picture of her boobs plastered in my cum... Now I'll send it to José)."
    $ mariawin = True 
$ hour += 1
jump LibraryChoiceDay05

label LibraryChoiceDay05:
menu:
    "Talk to Maria" if (spokemaria05 == False):
        jump Library03Day05
    "Look for Frieda" if (spokefriedalibraryday05 == False):
        jump Library04Day05
    "Learn how to use the hypnosis pendulum" if (pendulum == True) and (pendulumactive == False):
        jump LibraryPendulumDay05
    "Read the book about Goths that Laura gave you" if (book == True) and (bookread == False):
        jump LibraryGothDay05
    "Leave the library":
        jump SchoolChoiceDay05

label Library04Day05:
scene friedalibrary01day03 with dissolve
$ renpy.pause(1.0, hard=True)
$ spokefriedalibraryDay05 = True
p "Hi Frieda, what's up? You seem to be studying hard... Again."
fr "I can think a bit more clearly now with those new clothes... But it's still tough.... I really need an A or my parents vill kill me."
label FriedaChoiceDay05:
scene friedalibrary01day03 with dissolve
menu:
    "That's too bad. They sound like real Nazis." if (friedanazis == False):
        scene friedalibrary02day03 with dissolve
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
        jump FriedaChoiceDay05
    "Well, guess what? I switched your grades! You now have an A!" if (friedachangedgrade == True) and (friedatoldgrades == False):
        scene friedalibrary03day03 with dissolve
        fr "Mein Gott, you did it! Sank you sssooo much..."
        window hide
        $ lust_points[8] += 3
        $ score += 3
        show lust03:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        $ friedachangedgrade = False
        $ friedatoldgrades = True
        hide lust03
        if (lust_points[8] >= 10):
            show epiclust:
                xalign 0.25 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust
            jump FriedaFuckDay05  
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (lust_points[8] >=8):
                jump FriedaPendulumDay05
            "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[8] >=8):
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump FriedaPheromonesDay05
        p "You're welcome. Hopefully, this will lead to a growing relationship between us. Mine is definitely growing right now."
        jump FriedaChoiceDay05
    "I haven't managed to sneak into the principal's office but I'm planning on it..." if (friedahelped == True) and (friedachangedgrade == False) and (friedtoldgrades == False):
        scene friedalibrary02day03 with dissolve
        fr "Please hurry up. The reports are mailed on Thursday... And then, my parents vill see I had an F and they vill kill me..."
        window hide
        $ lust_points[8] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
        p "Right, right... I'll... do my best."
        fr "I need more than ze best! I need an übermensch!"
        jump FriedaChoiceDay05
    "OK, I'll leave you alone to study then...":
        jump Library03Day05

label FriedaPendulumDay05:
scene friedalibrary02day03 with dissolve
show pendulum03
$ renpy.pause(1.0, hard=True)
p "Just watch this pendulum as I wiggle it in front of your eyes Frieda..."
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
if (lust_points[8] ==8):
    window hide
    $ lust_points[8] += 2
    $ score += 2
    show lust02:
        xalign 0.2 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
if (lust_points[8] ==9):
    window hide
    $ lust_points[8] += 1
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
jump FriedaFuckDay05
    
label FriedaPheromonesDay05:
scene friedalibrary02day03 with dissolve
play sound "Sounds/sniffing.mp3"
$ renpy.pause(1.0, hard=True)
fr "Oh, it smells funny... And it's making me so horny at the same time..."
p "My spray is now empty... I guess I won't be able to use it again."
show pheromone
show square
play sound "Sounds/lost.mp3"
"You lost a pheromone spray."
hide square
hide pheromone
$ pheromone = False
if (lust_points[8] ==8):
    window hide
    $ lust_points[8] += 2
    $ score += 2
    show lust02:
        xalign 0.2 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
if (lust_points[8] ==9):
    window hide
    $ lust_points[8] += 1
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
jump FriedaFuckDay05

label FriedaFuckDay05:
scene friedalibrary03day03 with dissolve
$ renpy.pause(1.0, hard=True)
fr "FRISS MEINE SCHEISSE DU SCHWEIN!"
p "Wh... What the hell was that?"
fr "Ach, sorry, I just blurted this out. Let's go behind those bookshelves over there, no one vill bother us..."
p "Alright! Now we're talking!"
scene friedafuck01 with dissolve
$ renpy.pause(1.0, hard=True)
fr "Rrr, I'm like a pussycat! Follow me [name]! And take your clothes off, schnell!"
p "Sure, You too, take that top and your shorts off please, I'm so horny for you Frieda!"
scene friedafuck02 with dissolve
$ renpy.pause(1.0, hard=True)
fr "Hurry up, the librarian might come and I don't want to be expelled from this school. My parents vould kill me!"
p "I'm getting everything off as fast as I can! Let's go into the corner..."
scene friedafuck03 with dissolve
$ renpy.pause(1.0, hard=True)
fr "Was ist das, mein Gott! Are you rubbing your very BIG cock between my asscheeks naughty boy!"
p "Yeah I am, you're driving me crazy..."
scene friedafuck04 with dissolve
$ renpy.pause(1.0, hard=True)
fr "Rub it against mein arse, STUD! I want to feel how HUGE and HARD it is!"
label FriedaCockRubDay05:
play sound "Sounds/friedaback.mp3"
scene friedafuck04b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck04 with dissolve
$ renpy.pause(0.3, hard=True)
fr "Faster, SCHNELL! Ah, it's ssoo BIG!"
play sound "Sounds/friedaback.mp3"
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
scene friedafuck04b
$ renpy.pause(0.4, hard=True)
scene friedafuck04
$ renpy.pause(0.4, hard=True)
menu:
    "Repeat":
        jump FriedaCockRubDay05
    "Move on":
        pass
p "You liked that Frieda? My cock is like a bar of iron cos your hot bod is driving me insane!"

scene friedafuck05 with dissolve
$ renpy.pause(1.0, hard=True)
fr "I can see that, it's bigger than my arm! I don't know if mein poor pussy can take it, but I'm so wet and ready for you..."
p "Let's find out... Bend over and open wide..."
scene friedafuck06 with dissolve
$ renpy.pause(1.0, hard=True)
p "...I'm coming in! FUCK YEAH!"
fr "AAAH, ssooo wunderbar! Fuck me harder!"
scene friedafuck07 with dissolve
$ renpy.pause(1.0, hard=True)
p "Of course, I'm gonna pound you into the ground baby!"
fr "FUCK!!! AAAH! Too... too much! You're too deep!"
p "It's never too deep, your pussy can take it, but you have to stop screaming Frieda!"
scene friedafuck08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Like that, that's better..."
fr "Mm....mmmm....."
play sound "Sounds/friedafuck.mp3"
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08b with dissolve
$ renpy.pause(.2, hard=True)
scene friedafuck08 with dissolve
$ renpy.pause(.2, hard=True)
p "Just enjoy the feel of my massive teenage cock deep inside of you..."
label FriedaFuckChoiceDay05:
menu:
    "Let her ride you" if (friedaride == False):
        jump FriedaFuckRideDay05
    "Take her up the arse" if (friedaarse == False):
        jump FriedaFuckArseDay05
    "Tell her to finish you off with a blowjob" if (friedaarse == True) and (friedaride == True):
        jump FriedaFuckBlowjobDay05


label FriedaFuckRideDay05:
scene friedaup with dissolve
$ renpy.pause(1.0, hard=True)
fr "Let me insert that cum-missile myself..."
p "Sure, do as you please Frieda, it's all yours!"
fr "OOOOh, it's zzooo big... (puff)... Ein bißchen mehr...."
scene friedafuck09 with dissolve
$ friedaride = True
$ renpy.pause(1.0, hard=True)
fr "Mein Gott! I can feel your huge cock so deep inside of me... I can touch it with my hands from outside!"
p "Well, it does have a certain volume..."
fr "It is ENORMOUS! (puff) I don't think I can take much more of it zat way..."
p "Let's switch position then..."
menu:
    "Take her up the arse" if (friedaarse == False):
        jump FriedaFuckArseDay05
    "Tell her to finish you off with a blowjob" if (friedaarse == True) and (friedaride == True):
        jump FriedaFuckBlowjobDay05

label FriedaFuckArseDay05:
scene friedafuck10 with dissolve
$ friedaarse = True
$ renpy.pause(1.0, hard=True)
fr "You are stretching my poor little anus zo much! AAAAH!"
p "That's nothing, I'm not even halfway in. Let me stretch it a bit more..."
scene friedafuck10b with dissolve
$ renpy.pause(1.0, hard=True)
p "There. That's better. A solid ten inches of my ramrod up your arse!"
fr "Be caref.."
label FriedaFuckArseDay05b:
play sound "Sounds/friedaarse.mp3"
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10 with dissolve
$ renpy.pause(0.3, hard=True)
scene friedafuck10b with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump FriedaFuckArseDay05b        
    "Let her ride you" if (friedaride == False):
        jump FriedaFuckRideDay05
    "Tell her to finish you off with a blowjob" if (friedaarse == True)and (friedaride == True):
        jump FriedaFuckBlowjobDay05

label FriedaFuckBlowjobDay05:
stop music
play music "Sounds/friedaslow.mp3"
show friedafuckslow
show faster
call screen friedafuckslowday05
screen friedafuckslowday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("FriedaFuckFastDay05")

label FriedaFuckFastDay05:
hide faster
play music "Sounds/friedafast.mp3"
show friedafuckfast
show cum
call screen friedafuckfastday05
screen friedafuckfastday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FriedaFuckCumDay05")

label FriedaFuckCumDay05:
hide friedafuckfast
hide friedafuckslow
stop music
scene friedacum01
play sound "Sounds/imcumming.mp3"
$ renpy.pause(3.0, hard=True)
fr "Glurb... mmmh..."
scene friedacum02 with dissolve
play sound "Sounds/imcumming02.mp3"
$ renpy.pause(2.0, hard=True)
fr "You are coming ssooo much. Wunderbar!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ friedafucked = True
$ backdoor += 1
if (katefucked == True) and (maddyfucked == True) and (laurafucked == True) and (achievement.grant("classroom") == False):
    show achievement03:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement03
    $ achievement.grant("classroom")
fr "But we need to get dressed. And cleaned up..."
p "Yes, that is probably a good idea. I mean, some people DO use the library sometimes."
if (friedajosewin == False):
    $ friedawin = True
    p "(José is going to be mightily pissed off when he gets the pic I'm sending him...)"
$ fuckedschoolgirlDay05 = True
$ hour += 1
jump LibraryChoiceDay05

label LibraryPendulumDay05:
if (blacktop05 == True):
    scene ryanlibraryinternetblack with dissolve
else:
    scene ryanlibraryinternet with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/keyboard.ogg"
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump LibraryChoiceDay05

label LibraryGothDay05:
if (blacktop05 == True):
    scene ryanreadinglibraryblack with dissolve
else:
    scene ryanreadinglibraryinternet with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump LibraryChoiceDay05

label BurbsDay05:
stop music
scene burbsday with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_67
    $ lustaddedB = 1
    call Challenger from _call_Challenger_68
    $ challengercalls += 2
if (hour >= 16) and (maddysaved == False) and (maddysaved05 == False) and (josemaddysaved == False):
    $ lust_pointsB[14] = 10
    play sound "Sounds/phonevibrate.mp3"
    $ renpy.pause(1.0, hard=True)
    show josemaddy at center:
        yalign 0.0
        linear 1.0 yalign 0.5
    j "Guess who's the island's hero who saved Maddy?"
    j "It's ME, loser! And she was VERY grateful as you can see! HA HA HA!"
    p "I'll show him who's the REAL hero by the end of the week!"
    hide josemaddy
    if (maddyjosewin == False):
        $ girlsfucked += 1
    $ josemaddysaved = True
    $ maddyjosewin = True

if (hour == 20):
    p "Just in time to head to the Longrods for dinner!"
    jump DinnerDay05
if (hour == 18 or hour == 19):
    p "I don't have time for much at this time of the day... Dinner is at 8pm."
    jump BurbsChoiceDay05

p "The burbs are so quiet during the day. I guess everyone is at work. Except me!"

label BurbsChoiceDay05:
if (hour == 20):
    p "Damn, it's 8pm already, I should really head back home for dinner..."
    jump DinnerDay05
p "What should I do?"
menu:
    "Explore the Burbs" if (discoverstore == False):
        jump BurbsExploreDay05
    "Go to the convenience store" if (discoverstore == True) and (evictedfromstore == False):
        jump StoreDay05
    "Go back home":
        jump HomeDay05
    "Go to Debby's house" if (auntdebbyseen05 == False) and ((debbycarwashed == False) or ((debbysugar == False) and (debbysugar03 == False)  and (debbysugar04 == False)) or ((debbybikini == False) and (debbybikini03 == False) and (debbybikini04 == False))):
        jump AuntDebbyHouseDay05
    "Take the bus to the beach" if (hour <= 17):
        $ busbeach = True
        jump BusDriveDay05
    "Take the bus heading downtown" if (hour <= 17):
        $ bustown = True
        jump BusDriveDay05
    "Go to the school" if (hour <= 15):
        scene lockerempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump SchoolChoiceDay05
    "Take the shortcut to the Beach" if (hour <= 19) and (discoverclinic == True):
        stop music
        scene clinicentrance with dissolve
        play music "Sounds/gardensound.mp3"
        $ renpy.pause(1.0, hard=True)
        p "I wish I had discovered this shortcut earlier, it is really helpful in cutting my travel time between the burbs and the beach..."
        jump Beach01Day05
    "Go to the clinic" if (hour <= 18) and (discoverclinic == True) and (seenclinic05 == False):
        jump Insemination01Day05

label BurbsExploreDay05:
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
jump BurbsChoiceDay05

label BusDriveDay05:
stop music
scene busdrive with dissolve
play music "Sounds/busidle.mp3"
$ renpy.pause(1.0, hard=True)
p "Here's the bus. Let's get on."

label BusDriveDayb05:
if (shadyguyseen05 == True) or (maddysaved == True) or (josemaddysaved == True) or (maddysaved05 == True):
    jump BusEndDay05

if (maddylead == True) and (maddysaved == False) and (josemaddysaved == False) and (maddysaved05 == False):
    jump ShadyGuySecondDay

label ShadyGuyFirstDay:
scene shadybus01 with dissolve
$ shadyguyseen05 = True
$ renpy.pause(1.0, hard=True)
p "This guy looks shady..."
sg"Oy, who you're looking at?"
p "Are you talking to me? Are you talking to me?"
scene shadybus02 with dissolve
$ renpy.pause(1.0, hard=True)
sg"You wanna taste some blade boy?"
menu:
    "Oh, sorry sir, my apologies. I'll be on my merry way.":
        sg"You're lucky I'm getting off at the next stop boy!"
        jump EscapeShadyGuyDay05
    "You don't scare me, I'm da man, I'm DA MAN!":
        jump FightShadyGuyDay05

label ShadyGuySecondDay:
scene shadybus01 with dissolve
$ shadyguyseen05 = True
$ renpy.pause(1.0, hard=True)
p "It's that shady guy again... I should confront him."
sg"You again boy?"
p "Yeah, me again dipshit, and I'm ready to KICK YOUR ARSE!"
scene shadybus02 with dissolve
$ renpy.pause(1.0, hard=True)
sg"So am I!"
jump FightShadyGuyDay05

label EscapeShadyGuyDay05:
$ escapeshadyguy = True
scene shadyguyleft with dissolve
$ renpy.pause(1.0, hard=True)
p "Phew, that was close, that guy's crazy!"
if (maddylead == False):
    "The man leaves at the next stop. He seems to have dropped something."
    window hide
    show maddyphoto with dissolve
    $ renpy.pause(1.0, hard=True)
    p "OMG, it's a picture of Maddy! The bastard must have kidnapped her!"
    p "Damn, I don't know where he went or where that picture was taken... Next time I meet him, I should confront him."
jump BusEndDay05

label EscapeShadyGuyDay05b:
$ escapeshadyguy = True
scene shadyguyleft with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, that hurts! I can't run after him, I can barely breathe..."
if (maddylead == False):
    "The man leaves at the next stop. He seems to have dropped something."
    window hide
    show maddyphoto with dissolve
    $ renpy.pause(1.0, hard=True)
    p "OMG, it's a picture of Maddy! The bastard must have kidnapped her!"
    p "Next time I cross paths with this cunt, I'd better be stronger and prepared."
    $ maddylead = True
jump BusEndDay05

label FightShadyGuyDay05:
scene shadybus03 with dissolve
$ renpy.pause(1.0, hard=True)
sg"You asked for it! Get ready to BLEED!"
if (knife == True) and (blacktop05 == False):
    scene shadybus04whiteknife with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Ah, ah, you didn't see that coming did you, shady guy?"
    sg"Pff! A Japanese army knife? Look at my blade! It's as big as Rambo's! Now enough talk, let's FIGHT!"
    if (strength >=8):
        play sound "Sounds/punch.mp3"
        scene shadyguyfall with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Take that you scumbag!"
        "You deliver a mighty kick to your foe who falls unconscious to the ground."
        jump ShadyGuyDownDay05
    jump ShadyGuyLoseDay05

if (knife == True) and (blacktop05 == True):
    scene shadybus04blackknife with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Ah, ah, you didn't see that coming did you, shady guy?"
    sg"Pff! A Japanese army knife? Look at my blade! It's as big as Rambo's! Now enough talk, let's FIGHT!"
    if (strength >=8):
        play sound "Sounds/punch.mp3"
        scene shadyguyfallblack with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Take that you scumbag!"
        "You deliver a mighty kick to your foe who falls unconscious to the ground."
        jump ShadyGuyDownDay05
    jump ShadyGuyLoseDay05

if (knife == False) and (blacktop05 == False):
    scene shadybus04white with dissolve
    $ renpy.pause(1.0, hard=True)
    p "(If only I had a knife like him...)"
    sg"Enough thinking to yourself in your head, let's FIGHT!"
    if (strength >=10):
        play sound "Sounds/punch.mp3"
        scene shadyguyfall with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Take that you scumbag!"
        "You deliver a mighty kick to your foe who falls unconscious to the ground."
        jump ShadyGuyDownDay05
    jump ShadyGuyLoseDay05

if (knife == False) and (blacktop05 == True):
    scene shadybus04black with dissolve
    $ renpy.pause(1.0, hard=True)
    p "(If only I had a knife like him...)"
    sg"Enough thinking to yourself in your head, let's FIGHT!"
    
    if (strength >=10):
        play sound "Sounds/punch.mp3"
        scene shadyguyfallblack with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Take that you scumbag!"
        "You deliver a mighty kick to your foe who falls unconscious to the ground."
        jump ShadyGuyDownDay05
    jump ShadyGuyLoseDay05

label ShadyGuyLoseDay05:
if (blacktop05 == True):
    scene shadyguyinjuredblack with dissolve
if (blacktop05 == False):
    scene shadyguyinjured with dissolve
sg"You're no match for my Ninja moves kid!"
play sound "Sounds/ryanpain.mp3"
$ renpy.pause(1.0, hard=True)
"You feel a stinging pain in your abdomen as the shady guy lashes at you."
$ stamina -= 1
show staminaminus01:
    xalign 0.5 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
p "Good thing I have a solid eight-pack that stopped the blade from piercing through my stomach and killing me..."
sg"You're lucky I'm getting off at this stop or I would have finished you off boy!"
jump EscapeShadyGuyDay05b

label ShadyGuyDownDay05:
scene shadyguyground with dissolve
$ renpy.pause(1.0, hard=True)
p "I win, I'm da man, I'm DA MAN!"

"You search his pockets and find 5 dollars and a photograph."
$ money += 5
window hide
show maddyphoto with dissolve
$ renpy.pause(1.0, hard=True)
p "OMG, it's a picture of Maddy! The bastard must have kidnapped her!"
"There is also a bill with an address."
window hide
show billphoto with dissolve
$ renpy.pause(1.0, hard=True)
p "Interesting, this place seems to be close to Tini-Wini-Bikini Beach. Maybe it's where Maddy is...."
show addedlocation:
    xalign 0.4 yalign 0.3
    linear 1.0 yalign 0.1
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide addedlocation
$ discovercabin = True
$ maddylead = True
jump BusEndDay05

label BusEndDay05:
if (busbeach == True):
    $ hour += 1
    $ busbeach = False
    jump Beach01Day05
elif (bustown == True):
    $ hour += 1
    $ bustown = False
    jump DowntownDay05
elif (bushome == True):
    $ hour += 1
    $ bushome = False
    jump BurbsDay05

label StoreDay05:
stop music
scene store01 with dissolve
play music "Sounds/storemusic.mp3"
$ renpy.pause(1.0, hard=True)

label StoreClerkDay05:
scene store01
if (workedseconddaystore == True) and (hour == 17):
    fa "Oh hi [name]. I guess you came to work here again?"
    fa "I'm really sorry but you can't. I took another boy for the work today, since you already worked here twice already."
    fa "He was desperate for money, I couldn't really say no. He's a nice boy called José."
    p "WHAT???? AAARGH! This is not fair!"
    fa "Oh, moan, moan, moan, that's all I ever hear from you..."
    jump ClerkChoiceDay05    
if ((catchfrancine == True) or (catchbeer == True)) and (hour == 17):
    fa "Are you ready to start another shift today?"
    menu:
        "Yes, I'm ready.":
            jump StoreSecondWork01Day05
        "No, I'm too busy right now.":
            fa "Well, that's unfortunate... I could have really used your help again today..."
            jump ClerkChoiceDay05    
if (storework == True) and (hour == 17) and (catchfrancine == False) and (catchbeer == False):
    fa "Are you ready to start your shift today?"
    menu:
        "Yes, I'm ready.":
            jump StoreWork01Day05
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
            jump ClerkChoiceDay05
elif (storework == True) and (hour == 18):
    fa "You're late for your shift! Although you're lucky cos you don't have one today. I gave the job to someone else."
    fa "Come back tomorrow. At 5pm, not 6pm."
    jump ClerkChoiceDay05   
elif (hour == 19) and (teagangrocery05 == True) and (seenteaganhouseday05 == False):
    fa "Oh, you're just in time to pick up Miss Cocque's groceries. I was about to close."
    p "I'll get them to her right away!"
    jump TeaganHouse02Day05
elif (hour == 19):
    fa "Welcome to \"Seven Square\", your local shop that's opened from seven till... seven."
    fa "I'm sorry, but it is seven o'clock. The second seven. So we are closing."
    fa "Please come back tomorrow to your local convenience store \"Seven Square\" between 7am and... 7pm!"
    jump BurbsDay05    
else:
    fa "Welcome to \"Seven Square\", your local shop that's opened from seven till... seven."

label ClerkChoiceDay05:
if (catchfrancine == True) or (catchbeer == True):
    fa "So, how may I help you?"
else:
    fa "My name is Francine, how may I help you?"
menu:
    "Chat with her":
        jump StoreChatDay05 
    "Buy something":
        jump StoreBuyDay05
    "Invite her to the gym" if (gymmember == True):
        p "Hey, would you like to come to the gym with me today?"
        fa "Ooh, yes! Please let me know when you get there, thanks!"
        $ invitedfrancine05 = True
        jump ClerkChoiceDay05
    "Leave":
        jump BurbsDay05

label StoreChatDay05:
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
                        jump StoreNoDealDay05
                    "It's a deal!":
                        $ halfprice = True
                        jump StoreDealDay05
            "It's a deal!":
                jump StoreDealDay05
    "Just thought I’d check a few things out, you being one of them...":
        scene store03
        fa "I can barely contain my laughter."
        jump ClerkChoiceDay05
    
label StoreDealDay05:
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
            jump StoreBuyDay05
        "No thanks.":
            fa "Alright, see you another day then."
            jump BurbsDay05
jump StoreClerkDay05

label StoreWork01Day05:
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
        jump CatchFrancineDay05
    "Catch the beer":
        jump CatchBeerDay05

label CatchFrancineDay05:
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
jump StoreTeagan01Day05

label CatchBeerDay05:
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
jump StoreTeagan01Day05

label StoreTeagan01Day05:
play music "Sounds/storemusic.mp3"
scene storeteagan01 with dissolve
$ renpy.pause(1.0, hard=True)
p "There's Miss Cocque doing her shopping, she hasn't noticed me yet."
menu:
    "Hide and hope she doesn't see you":
        jump StoreHideDay05
    "Greet her and ask her if you can help with anything":
        jump StoreTeagan02Day05

label StoreHideDay05:
scene storeteaganhide with dissolve
$ renpy.pause(1.0, hard=True)
p "Phew, she almost saw me but I'm think I managed to avoid her... And she's on her way out."
p "At the same time, watching that arse... Maybe I should have greeted her..."
p "Oh well, only a few more minutes of hard labour and my shift ends. I'll just stack these bubble gums once she's out of the store."
jump StoreShiftEndDay05

label StoreTeagan02Day05:
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
        if (detention05 == True):
            t "Please don't, the poor boy already had detention today, it's my fault, I'm just in a foul mood today."            
        if (detention05 == False):
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
            jump StoreParkDay05
    "Sure Miss Cocque, let me help you with these heavy items, it'll be easy for me!":
        jump StoreTeagan05Day05

label StoreTeagan05Day05:
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

label StoreParkDay05:
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
        jump StoreShiftEndDay05
    "I don't know, I don't think I'll have time for that extra job...":
        t "Uh... OK, just think about it... Have a nice evening [name], I'll see you tomorrow at class, 9am sharp!"
        jump StoreShiftEndDay05

label StoreSecondWork01Day05:
$ workedseconddaystore = True
fa "Alright! Let's start working for a meagre pay for our parent company \"Seven Square\" once again! Yippee!"
if (beercase == True):
    p "I'm replacing the broken beer pack with this one which err...fell from the back of a truck."
    fa "That's fantastic! That way, I don't have to report it broken and we can get paid properly for yesterday's work, yippee!"
    $ lust_points[7] += 2
    $ score += 2
    show lust02:
        xalign 0.35 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    show beercase
    show square
    play sound "Sounds/lost.mp3"
    "You gave away a beercase."
    hide square
    hide beercase
    $ beercase = False
    $ money += 5

fa "The storage room is filthy again. I don't know how this happens. But you need to clean it."
p "My pleasure (snickers)."
menu:
    "Clean the storage room":
        jump CleanStorageDay05
    "Build a pole-dancing platform with all the shit lying around" if (quentintipfrancine == True):
        jump PoleDancingDay05

label CleanStorageDay05:
scene storageclean with dissolve
$ renpy.pause(1.0, hard=True)
p "This job sucks! This job sucks!"
$ hour += 1
scene store07 with dissolve
$ renpy.pause(1.0, hard=True)
fa "Oh wow, it's squeaky clean! Seven Square is proud of you!"
$ lust_points[7] += 1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
fa "Now let's go and pack some shelves in the front room!"
p "Sure thing, boss! (anything to get me out of this sordid place)"
scene storepacking with dissolve
play music "Sounds/storemusic.mp3"
$ renpy.pause(1.0, hard=True)
fa "Isn't that fun [name]? Us working together for our parent company \"Seven Square\"!"
p "(She's fucking nuts. But she's got big tits...)"
jump StoreShiftEndSecondDay05

label PoleDancingDay05:
scene polebuild01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Heigh-ho, Heigh-ho, it's home from work we go..."
$ hour += 1
scene polebuild02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Well, that looks OK, complete with a spotlight. I hope she'll like it. I can hear her steps, I'll find out soon enough..."
scene pole01 with dissolve
$ renpy.pause(1.0, hard=True)
fa "What have you done to our storage room? It's even dirtier than before!"
$ lust_points[7] -= 1
$ score -= 1
show lustminus01:
    xalign 0.6 yalign 0.4
    linear 1.0 yalign 0.6
play sound "Sounds/less.mp3"
$ renpy.pause(2, hard=True)
hide lustminus01
scene pole02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Not this corner, it's squeaky clean and I thought it might be a relaxing way to end the day..."
fa "A pole-dance! That's... unusual for a work place... But I must admit I am tempted to try it out."
$ lust_points[7] += 2
$ score += 2
show lust02:
    xalign 0.6 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
fa "Why don't you man the till for a while? If a French-speaker comes along, tell them to come back later or something..."
p "Sure boss!"
scene pole03 with dissolve
play music "Sounds/storemusic.mp3"
$ renpy.pause(1.0, hard=True)
p "Shit, there's a customer. I hope she leaves soon... Although she's pretty damn hot."
scene pole04 with dissolve
$ renpy.pause(1.0, hard=True)
re "Vous vendez de la poudre de lessive? Je n'en trouve pas."
menu:
    "Fuck off Frenchie.":
        scene pole04b with dissolve
        $ renpy.pause(1.0, hard=True)
        re "What? Je... I will complain to the highest autorité!"
        $ shopcomplaint = True
        p "Well, at least I got rid of her. That's what I was supposed to do right?"
        p "I can finally go and check out on Francine..."        
        jump PoleDance01Day05
    "Me no parl-ay Froggie. Sorry.":
        re "But you are supposed to! All shops must cater to French-speakers on Veri-Bosti island, it's the law!"
        p "Well clearly you speak English. So what are you moaning about?"
        re "Humpf, yes I do, but it is not my first language. I am looking for.. how do you say?... Washing powder?"
        p "Ah, let me show you, we have all the big brands and also the cheap ones that are exactly the same shit."
        jump StoreCustomerDay05
    "Vou-lay-vous couch-ay avec moi ce soir?":
        re "Hein? Mais ça va pas la tête? C'est un scandale!"
        p "Calm down now lady, I was just kidding... Why don't we speak English for a change, you speak English right?"
        re "Humpf, yes I do, but it is not my first language. I am looking for.. how do you say?... Washing powder?"
        p "Ah, let me show you, we have all the big brands and also the cheap ones that are exactly the same shit."
        jump StoreCustomerDay05

label StoreCustomerDay05:
scene pole05 with dissolve
$ renpy.pause(1.0, hard=True)
p "There they are. Right next to the dog food."
re "I see... Merci."
scene pole06 with dissolve
$ renpy.pause(1.0, hard=True)
re "Which one to choose... Mr White... Dax... Homo... Homo? Is that a brand? Oh, I don't know which one is the best..."
menu:
    "They're all the same for crying out loud!":
        scene pole05 with dissolve
        $ renpy.pause(1.0, hard=True)
        re "Don't pressure me, this is an important decision."
        p "I don't have all day lady..."
        re "I'm the customer! That's it, I'm leaving this store, the service here is deplorable."
        p "(Good riddance)"
        $ shopcomplaint = True
        jump PoleDance01Day05
    "Imagine her naked":
        scene pole06b with dissolve
        play sound "Sounds/dreaming.mp3"
        $ renpy.pause(2.0, hard=True)
        p "Fuck yeah, nice tight arse..."
        re "Hello? HELLO!"
        scene pole05 with dissolve
        $ renpy.pause(1.0, hard=True)
        re "I want to buy the one in the pink box."
        p "Sure, sure... Great choice. Let's go to the check-out counter... (phew, finally got rid of her...)"
        scene pole04 with dissolve
        p "That will be 78,350 Veri-Bosti Liras. (Gee, the currency in this country is pure madness...)"
        re "Here you are. Bonne journée à vous."
        play sound "Sounds/cashregister.wav"
        p "I can finally go and check out on Francine..."
        
        jump PoleDance01Day05

label PoleDance01Day05:
scene pole07 with dissolve
play music "Sounds/haton.mp3"
$ renpy.pause(1.0, hard=True)
p "Ooh, she's using the pole and she even put on some sexy music..."
scene pole08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Let's get closer, she didn't hear me come in..."
scene pole09 with dissolve
$ renpy.pause(1.0, hard=True)
p "Uh uh, now she saw me..."
scene pole10 with dissolve
stop music
$ renpy.pause(1.0, hard=True)
fa "I... couldn't resist doing a bit of pole-dancing... Don't tell anyone please!"
p "Don't worry Francine. My lips are sealed (and yours will be soon on my cock!)"
fa "How did it go at the till?"
p "Err... Fine, only satisfied customers, but it's empty now, so I came to check on you..."
scene pole11 with dissolve
$ renpy.pause(1.0, hard=True)
fa "Well, that's nice of you... Did you enjoy the show?"
p "Of course! Although it was cut short too fast..."
$ lust_points[7] += 1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
fa "Well, maybe I could continue for a while, I didn't finish my moves..."
scene pole12 with dissolve
play music "Sounds/haton.mp3"
$ renpy.pause(3.0, hard=True)
scene pole13 with dissolve
$ renpy.pause(3.0, hard=True)
p "Wow, she's very flexible..."
scene pole14 with dissolve
stop music
$ renpy.pause(2.0, hard=True)
fa "That's it for now... We'd better get back to the store front..."
if (gymmember == True):
    menu:
        "Invite her as a guest to the downtown gym as your guest":
            p "You know, as an eminent member of the downtown gym, I can invite you as a guest for free."
            p "Apparently, they have a fully-equipped pole-dancing room ...."
            fa "Really? That's amazing, thank you so much for inviting me!"
            p "We could go there tomorrow, I'll call you when I get there..."
            $ invitedfrancine05 = True
        "Don't say anything":
            pass

scene storepacking with dissolve
play music "Sounds/storemusic.mp3"
$ renpy.pause(1.0, hard=True)
fa "Isn't that fun [name]? Us working together for our parent company \"Seven Square\"!"
p "(She's fucking nuts. But she's got big tits...)"
if (shopcomplaint == True):
    play sound "Sounds/phonering.mp3"
    fa "Oh, the store phone is ringing, let me get it, it must be headquarters..."
    scene storephone with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Uh uh, I hope it's not about that stupid French-speaking lady..."
    fa "[name]!, Come over here immediately!"
    scene store03 with dissolve
    stop music
    stop sound
    $ renpy.pause(1.0, hard=True)
    fa "I just got a call from Seven Square's headquarters. Someone complained about our store..."
    p "What? But it's the best convenience store on the island!"
    fa "That person complained about a young, blond shop clerk who was rude to her. It was YOU clearly! While I was in the storage room..."
    fa "I am very disappointed in you [name]..."
    $ lust_points[7] -= 1
    $ score -= 1
    show lustminus01:
        xalign 0.3 yalign 0.4
        linear 1.0 yalign 0.6
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01 
    p "It's not my fault, she was babbling in French, I didn't understand a word she was saying!"
    fa "The headquarters are fining us. Meaning, YOU won't get paid today as a punishment!"
    p "What? It's not fair..."
    fa "Stop moaning, now close the front door, we are done for the day here!"
    p "Do I get to buy an item half-price at least?"
    fa "Certainly not! Go home now!"
    $ hour += 1
    jump BurbsChoiceDay05

label StoreShiftEndSecondDay05:
stop music
scene store01 with dissolve
$ hour += 1
$ renpy.pause(1.0, hard=True)
fa "That's it, the end of the shift. Since you didn't break anything today for a change, you will be paid a whopping ten dollars!"
$ money += 10
p "And... I still get a choice of an item half-price right?"
scene store01 with dissolve
fa "Ah yes, I'm so sorry, I almost forgot. Again."
scene store03 with dissolve
jump HalfPriceDay05

label StoreShiftEndDay05:
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
    jump StoreShiftEnd02Day05
if (catchfrancine == True):
    fa "Here's five dollars for your hard work [name]! I hope you come back again to work here. Goodbye."
    $ money += 5
    p "Yeah, maybe, I'll see..."
    jump StoreShiftEnd02Day05
    
label StoreShiftEnd02Day05:
if (halfprice == True):
    p "Hey, I can buy something half-price remember?"
    fa "Ah yes, silly me for not remembering..."
    jump HalfPriceDay05

label HalfPriceDay05:
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
        jump StoreShiftEnd03Day05
        
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
        jump StoreShiftEnd03Day05

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
        jump StoreShiftEnd03Day05

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
        jump StoreShiftEnd03Day05
    
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
        jump StoreShiftEnd03Day05

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
        jump StoreShiftEnd03Day05
    
    "Nothing actually...":
        jump StoreShiftEnd03Day05
        
label StoreShiftEnd03Day05:
scene store01 with dissolve
fa "That's it, you bought your item, now I have to close the store... Come back anytime to \"Seven Square\", your local shop that's opened from seven till... seven."
jump BurbsDay05
    
label StoreNoDealDay05:
scene store03 with dissolve
fa "That's a pity... Think about it, the job offer will be on all week."
jump StoreClerkDay05

label StoreBuyDay05:
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
        jump ClerkChoiceDay05

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
        jump ClerkChoiceDay05

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
        jump ClerkChoiceDay05

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
        jump ClerkChoiceDay05
    
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
        jump ClerkChoiceDay05

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
        jump ClerkChoiceDay05
    "Nothing actually...":
        jump ClerkChoiceDay05

label AuntDebbyHouseDay05:
stop music
if (blacktop05 == True):
    scene debbyentranceblack with dissolve
else:
    scene debbyentrance with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/debbydoorbell.mp3"
p "Maybe I could ask Debby if I could wash her car for her and get a bit of money..."
if (hour >=18):
    scene debbyhouse01 with dissolve
    d "Well, look who came to visit me. What brings you here [name]?"
    $ auntdebbyseen05 = True
    if (debbycarunwashed == True):
        scene debbyhouseangry with dissolve
        d "Hang on, now I remember... I paid you 5 bucks to wash my car yesterday and it's still as filthy as ever, but the five bucks are gone!"
        d "Are you trying to rip me off? Give me back my five bucks [name]!"
        $ money -= 5
        if (debbyfucked == False):
            $ lust_points[5] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.4 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
        d "That's better... So what brings you here?"
        $ debbycarunwashed = False
        scene debbyhouse01 with dissolve
    jump AuntDebbyHouseMenuDay05
if (hour <=17):
    p "She doesn't seem to be in at the moment."
    jump BurbsDay05

label AuntDebbyHouseMenuDay05:
menu:
    "I wanted to see you model some more bikinis for me." if (debbybikini04 == False) and (debbybikini == False) and (debbybikini03 == False):
        d "Well, that's bold of you young man!"
        d "But you're in luck, I just received a new swimsuit which I haven't tested yet... Come on in..."
        $ debbybikini05 = True
        jump AuntDebbyInsideDay05
    "I was wondering if your car needed washing?" if (debbycarwashed == False):
        d "Oh, I see, you want to make a bit of money do ya? Fair enough."
        d "I'll give you five dollars... But I want to be able to watch and you have to be bare-chested...(wink)"
        menu:
            "It's a deal!":
                jump AuntCarWashDay05
            "Five dollars? It will take me at least one hour to wash it... Not interested.":
                d "Your choice mr I'm-too-important-to-wash-a-car-for-five-dollars!..."
                d "Anything else?"
                jump AuntDebbyHouseMenuDay05
    "Nancy needs some...sugar." if (debbysugar == False) and (debbysugar03 == False) and (debbysugar04 == False):
        d "Oh, alright, come on in then."
        $ debbysugar05 = True
        jump AuntDebbyInsideDay05
    "How about you get down on your knees and worship your Master's cock again?" if (debbyfuckedoffice == True):
        d "Well... I don't know [name], I..."
        p "Your Master ir ORDERING YOU bitch!"
        d "Of course Master, come in and your slave will get ready for you."
        jump DebbyCockSlapDay05
    
label AuntDebbyNewBikiniDay05:
d "Where should I model this new bikini for you?"
menu:
    "Why not in your bedroom?":
        d "No, that's my special place. You can't go there ever, you hear me?"
        p "Alright, alright. How about the backyard then?"
        d "Yes, that will do, go and sit outside and wait for me, I'll be back in a minute."
        d "Get down to your underwear, I might need you... to do something for me."
        p "(Well, that's an unusual request... I hope it leads to something...)"
        jump DebbyHouseBikini01Day05
    "The outside light will better reveal every detail of your hot bo...swimsuit.":
        d "Yes, you're right, you are a fine connoisseur. Go and sit outside then, I'll be back in a sec." 
        d "Get down to your underwear, I might need you... to do something for me."
        p "(Well, that's an unusual request... I hope it leads to something...)"
        jump DebbyHouseBikini01Day05

label AuntCarWashDay05:
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
            jump DinnerDay05
        jump AuntDebbyMoneyDay05
    "Stop and sneak inside to get the money anyway":
        $ debbycarunwashed = True
        jump AuntDebbyMoneyDay05
    
label AuntDebbyInsideDay05:
scene debbyhouse02 with dissolve    
$ renpy.pause(1.0, hard=True)
play sound "Sounds/footsteps.mp3"
d "This way to the living room..."
p "Wow, Debby has such a huge house... And such a tight ass..."
jump AuntDebbyLivingRoomDay05

label AuntDebbyLivingRoomDay05:
scene debbyhouse03 with dissolve    
$ renpy.pause(1.0, hard=True)
if (debbysugar05 == True):
    d "I'll go and fetch some sugar from the kitchen. You can wait for me here. But don't touch anything, these sculptures are worth thousands of dollars!"
    p "Sure Debby. I won't move."
    play sound "Sounds/debbydooropenclose.mp3"
    jump DebbySnoopDay05
if (debbybikini05 == True):
    jump AuntDebbyNewBikiniDay05
    
label DebbySnoopDay05:
scene debbysnooping with dissolve    
$ renpy.pause(1.0, hard=True)
menu:
    "Snoop around":
        jump DebbySnoopingDay05
    "Wait patiently for Debby to return":
        jump DebbySugarDay05

label DebbySnoopingDay05:
play music "Sounds/snooping.mp3"
$ d2rolldebby=renpy.random.randint(0, 1)
if (d2rolldebby == 0):
    call screen debbysnoop01Day05
if (d2rolldebby == 1):
    call screen debbysnoop02Day05
$ renpy.pause(1.0, hard=True)
stop music
"You were too slow and didn't find anything. Debby is coming back..."
jump DebbySugarDay05

label FoundAudaciousPassDay05:
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

label DebbySugarDay05:
scene debbyhouse04 with dissolve    
$ renpy.pause(1.0, hard=True)
d "Here you are. I hope your landlady does some nice cakes with it! Tell her to invite me when she's done."
p "Thanks Debby... I'll be sure to let her know..."
$ hour += 1
jump BurbsDay05
    
label DebbyHouseBikini01Day05:
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
if (lust_points[5] >= 10):
    show epiclust:
        xalign 0.2 yalign 0.3
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    jump DebbyBikiniPrefuck01Day05
d "But that's not what I had in mind \"stud\"... It's called \"Stud Tamer\", remember?"
scene debbyhousebikini06 with dissolve    
$ renpy.pause(1.0, hard=True)
p "Ah, I see, THAT's what you had in mind... I don't really want my friends at school to see me like that Debby, this is kinda humiliating..."
d "Don't worry, we'll cover your eyes with a black strip. This billboard campaign will have women screaming for this new model!"
p "Can't I get paid or something like normal models?"
d "Alright, I suppose I could give you ten dollars for your \"work\". But don't tell your landlady about this, it's between you and me alright?"
p "I sure hope it stays between you and me, I don't want the rest of the world to see me being tamed like I'm some kind of wild animal..."
$ money += 10
d "Now off you go, it's getting late... (wink)."
$ hour +=1
stop music
jump BurbsDay05

label DebbyBikiniPrefuck01Day05:
d "Oh, who am I kidding [name]? I want to see it, please, show me your great big slave-tamer Master!"
p "Mmh, that's better Debby... Show me your arse and your tits first... SLAVE!"
scene debbyhousebikini09 with dissolve
$ renpy.pause(1.0, hard=True)
d "My goodness Master, your bulge... It's just GIGANTIC! Please fuck me like filthy trash, use my body as your cumdump!"
p "First show me the goods slave, and I'll decide if you're worthy of my godlike scepter!"
scene debbyhousebikini07 with dissolve
$ renpy.pause(1.0, hard=True)
d "Of course Master, your slave will do ANYTHING for you! I hope my tight arse is to your liking... You can pound it as hard as you like..."
p "Not bad. I wanna see those tits now."
scene debbyhousebikini08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, what a rack aun... I mean SLAVE!"
d "You can call me dirty whore, cos I'm just a filthy cock-slut. A slut for your big, fat, donkey-dick Master!"
d "Let me take you to my fuckroom Master... Where you can ravish me and cover my slutty face in your cum!"
scene debbystairs02 with dissolve
$ renpy.pause(1.0, hard=True)
d "Oh Master, I'm crawling for you like a whore, because I'm just a filthy slave to your huge cock!"
p "(Wow, she's really getting turned on by pretending to be my slave...)"
p "Err.. Yeah, that's good slave, now show Master the way so he can give a good pounding!"
d "This way Master... To the master bedroom... YOUR fuckroom!"
jump DebbyFuckChoiceDay05

label AuntDebbyMoneyDay05:
stop music
scene debbymoney with dissolve    
$ renpy.pause(1.0, hard=True)
p "Here's the money."
play sound "Sounds/auntviolent.mp3"
p "What's that sound? It seems to be coming from upstairs where Debby's bedroom is..."
menu:
    "Go investigate":
        jump AuntDebbyStairsDay05
    "Take the money and leave":
        $ money += 5
        jump BurbsDay05

label AuntDebbyStairsDay05:
scene debbystairway with dissolve
play sound "Sounds/auntwhip01.mp3"
$ renpy.pause(1.0, hard=True)
p "Jeezus, this sounds violent, I'd better hurry up!"

label AuntDebbyBedroomDay05:
scene debbybedroom01 with dissolve    
play sound "Sounds/auntwhip02.mp3"
$ renpy.pause(1.0, hard=True)
p "WTF? That masked naked guy is brutalizing Debby!"
menu:
    "Leave quietly and take the money on the way out":
        $ money += 5 
        jump BurbsDay05
    "Get involved":
        p "Hey you, stop this immediately or...I swear I'll beat you up!"
        jump AuntDebbyBondage01Day05

label AuntDebbyBondage01Day05:
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
d "Please don't tell your landlady or anybody. I'll give you twenty dollars if you promise me to keep quiet."
menu:
    "So you're into bondage then? I like that...I like that a lot....":
        d "What? No, I'm not interested in doing such a vile thing with you and corrupting your fragile young mind...."
        d "You need to leave now...Take your carwash money and go."
        p "Hey! But..."
        d "Just GO!"
        $ money += 5
        jump BurbsDay05
    "You deserve a good cock slapping, get on your knees bitch!":
        d "Wh...what?..But..."
        p "You heard me. Remove your mask and ON YOUR KNEES BITCH!"
        d "Y..yes master..."        
        jump DebbyCockSlapDay05
    "OK, I didn't see a thing. I won't say a word. I'll just erase everything from my memory.":
        d "Oh Thank you [name], I owe you big time. Here's your twenty bucks. Now get out of here and don't say a word to anyone!"
        $ money += 20
        jump BurbsDay05

label DebbyCockSlapDay05:
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
        d "Here's 10 dollars, don't say a word to your landlady and we might do something like that again (wink...)."
        p "F...fuck! I'm so hard and I can't even cum!"
        if (debbycarunwashed == True):
            $ hour +=1
        jump BurbsDay05
    "Now I'm gonna cock-slap that tight arse of yours filthy slut!":
        d "Oooh, yes master, I deserve it..."
        jump ArseCockSlapDay05

label ArseCockSlapDay05:
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
if (lust_points[5] == 9):
    $ lust_points[5] +=1
    $ score += 1
    show lust01:
        xalign 0.6 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[5] <= 8):
    $ lust_points[5] +=2
    $ score += 2
    show lust02:
        xalign 0.6 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
if (lust_points[5] >= 10):
    show epiclust:
        xalign 0.6 yalign 0.3
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    d "I'm such a dirty whore for your great big cock Master... Please, do whatever you want with my filthy body!"
    jump DebbyFuckChoiceDay05
d "It's enough for now [name], here's 10 dollars, don't say a word to your landlady and we might do something like that again (wink...)."
menu:
    "Sure, nice doing business with you Debby...":
        $ money += 10
        d "I feel so...cheap...so dirty...I love it, thank you [name]...Just go now..."
        p "I feel like...10 dollars worth apparently. See you another time Debby!"
        if (debbycarunwashed == True):
            $ hour +=1
        jump BurbsDay05
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
        jump BurbsDay05

label DebbyFuckChoiceDay05:
scene debbybed01 with dissolve
play sound "Sounds/debbyprefuck01.mp3"
$ renpy.pause(10.0, hard=True)
d "I am ready to be treated like the cheap whore that I am Master..."
if (stamina <= 0) and (whitebull == True):
    p "I'd better drink some White Bull if I want to be able to perform...."
    menu:
        "Drink white bull (+2 stamina)":
            show whitebull
            show square
            play sound "Sounds/lost.mp3"
            "You gulped down your White Bull energy drink."
            hide square
            hide whitebull
            $ whitebull = False
            $ stamina += 2
            jump DebbyFuckChoiceDay05b
        "Don't drink white bull and keep it for another time":
            pass
    p "Well, this is all good clean fun Debby, but it's late, I have to go to home for dinner..."
    d "What? Is this some kind of sick joke? Get out of my house you useless pervert!"
    window hide
    $ lust_points[5] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.7 yalign 0.3
        linear 1.0 yalign 0.5
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01    
    jump BurbsDay05        
if (stamina <= 0):
    p "Well, this is all good clean fun Debby, but it's late, I have to go to home for dinner..."
    d "What? Is this some kind of sick joke? Get out of my house you useless pervert!"
    window hide
    $ lust_points[5] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.7 yalign 0.3
        linear 1.0 yalign 0.5
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    jump BurbsDay05        

label DebbyFuckChoiceDay05b:
scene debbybed01 with dissolve
menu:
    "Let me titfuck your massive tits filthy slut!" if (debbytitfuck == False):
        jump DebbyTitfuckDay05
    "On the bed on your back slave!" if (debbyback == False):
        jump DebbyBackFuckDay05
    "I want to lick your hard nipples and maul your tits!":
        jump DebbyNippleDay05
    "A cheap whore like you deserves a good pussy-pounding!" if (debbyfrontfuck == False):
        jump DebbyFrontFuckDay05
    "Be a good bitch and get on all fours for this horny dog!" if (debbydoggy01 == False):
        jump DebbyDoggyFuckDay05        
    "Time to finish me off slave!" if (debbydoggy01 == True) and (debbyfrontfuck == True) and (debbyback == True) and (debbytitfuck == True):
        jump DebbyBedMovie05

label DebbyDoggyFuckDay05:
$ debbydoggy01 = True
scene debbydoggy01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Open wide for your Master's cock, bitch!"
d "Yes, I'm a bitch... IN HEAT!"
scene debbydoggy02 with dissolve
window hide
play sound "Sounds/debbydoggy01.mp3"
$ renpy.pause(2.0, hard=True)
d "Oh, FUCK, master's cock is ssoo HUGE!"
label DebbyDoggyFuckDay05b:
play sound "Sounds/debbyfuck02.mp3"
scene debbydoggy01 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbydoggy02 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbydoggy01 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbydoggy02 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbydoggy01 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbydoggy02 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbydoggy01 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbydoggy02 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbydoggy01
$ renpy.pause(0.2, hard=True)
scene debbydoggy02
$ renpy.pause(0.2, hard=True)
scene debbydoggy01
$ renpy.pause(0.2, hard=True)
scene debbydoggy02
$ renpy.pause(0.2, hard=True)
scene debbydoggy01
$ renpy.pause(0.2, hard=True)
scene debbydoggy02
$ renpy.pause(0.2, hard=True)
scene debbydoggy01
$ renpy.pause(0.2, hard=True)
scene debbydoggy02
$ renpy.pause(0.2, hard=True)
scene debbydoggy01
$ renpy.pause(0.2, hard=True)
scene debbydoggy02
$ renpy.pause(0.2, hard=True)
scene debbydoggy01
$ renpy.pause(0.2, hard=True)
scene debbydoggy02
$ renpy.pause(0.2, hard=True)
scene debbydoggy01
$ renpy.pause(0.2, hard=True)
scene debbydoggy02
$ renpy.pause(0.2, hard=True)
menu:
    "Repeat":
        p "Let's do that again bitch, I haven't quenched the heat in my dong!"
        jump DebbyDoggyFuckDay05b
    "Move on":
        p "You did good slave, it's now time to move on to something else..."
        jump DebbyFuckChoiceDay05b
        
label DebbyTitfuckDay05:
$ debbytitfuck = True
scene debbytitfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
d "Let me lick your bull-sized balls while you pleasure yourself between my tits Master!"
p "Fuck yeah! That's a good little slut! I want my heavy seedmakers to be shiny with your filthy spit you hear me?"
d "Of course Master..."
scene debbytitfuck02 with dissolve
window hide
play sound "Sounds/debbytitfuck01.mp3"
$ renpy.pause(6.0, hard=True)
d "Of course Master... Are my tits good enough for your giant fuckstick?"
p "Mmh, yes, but I'm gonna pummel them faster now! SO keep up with your ball-licking slave!"
label DebbyTitFuckDay05b:
play sound "Sounds/debbytitfuck02.mp3"
scene debbytitfuck01 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbytitfuck02 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbytitfuck03 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbytitfuck02 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbytitfuck01 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbytitfuck02 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbytitfuck03 with dissolve
$ renpy.pause(0.2, hard=True)
scene debbytitfuck02
$ renpy.pause(0.2, hard=True)
scene debbytitfuck01
$ renpy.pause(0.2, hard=True)
scene debbytitfuck02
$ renpy.pause(0.3, hard=True)
scene debbytitfuck03
$ renpy.pause(0.3, hard=True)
scene debbytitfuck02
$ renpy.pause(0.3, hard=True)
scene debbytitfuck01
$ renpy.pause(0.3, hard=True)
scene debbytitfuck02
$ renpy.pause(0.3, hard=True)
scene debbytitfuck03
$ renpy.pause(0.3, hard=True)
scene debbytitfuck02
$ renpy.pause(0.3, hard=True)
scene debbytitfuck01
$ renpy.pause(0.3, hard=True)
scene debbytitfuck02
$ renpy.pause(0.3, hard=True)
scene debbytitfuck03
$ renpy.pause(0.3, hard=True)
scene debbytitfuck02
$ renpy.pause(0.3, hard=True)
scene debbytitfuck01
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        p "Let's do that again whore, I want more drool on my balls!"
        jump DebbyTitFuckDay05b
    "Move on":
        p "You did good slave, it's now time to move on to something else..."
        jump DebbyFuckChoiceDay05b

label DebbyBackFuckDay05:
$ debbyback = True
scene debbyback01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Offer your gaping slut-hole to my massive teenage cock slave!"
d "My filthy hole belongs to you Master... Do as you please with it!"
label DebbyBackFuckDay05b:
play sound "Sounds/debbyfuck01.mp3"
scene debbyback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyback01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyback01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyback01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyback02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyback01
$ renpy.pause(0.5, hard=True)
scene debbyback02
$ renpy.pause(0.5, hard=True)
scene debbyback01
$ renpy.pause(0.5, hard=True)
scene debbyback02
$ renpy.pause(0.5, hard=True)
scene debbyback01
$ renpy.pause(0.5, hard=True)
scene debbyback02
$ renpy.pause(0.5, hard=True)
scene debbyback01
$ renpy.pause(0.5, hard=True)
scene debbyback02
$ renpy.pause(0.5, hard=True)
scene debbyback01
$ renpy.pause(0.5, hard=True)
scene debbyback02
$ renpy.pause(0.5, hard=True)
scene debbyback01
$ renpy.pause(0.5, hard=True)
scene debbyback02
$ renpy.pause(0.5, hard=True)
$ debbyback = True
menu:
    "Repeat":
        p "Your pussy needs some more destroying!"
        jump DebbyBackFuckDay05b
    "Move on":
        p "I've punished your dirty hole enough for the moment slave... I'm giving you a respite..."
        d "Thank you Master, I am not worthy of such generosity..."
        jump DebbyFuckChoiceDay05b

label DebbyNippleDay05:
scene debbybed02 with dissolve
play sound "Sounds/sucking.mp3"
$ renpy.pause(2.0, hard=True)
d "Ooh, you suck on my nipples ssoo good! Maul my tits Master!"
p "They look red and erect now, it's time for something else slave..."
jump DebbyFuckChoiceDay05b

label DebbyFrontFuckDay05:
$ debbyfrontfuck = True
scene debbybed03 with dissolve
$ renpy.pause(1.0, hard=True)
d "Oh my God, your cock is stretching me wide open Master!"
p "Not wide enough yet..."
scene debbybed04a with dissolve
$ renpy.pause(1.0, hard=True)
d "AAAH! I don't deserve your giant teenage piece of meat!"
p "What? You want me to stop?"
d "Of course not, fuck me deeper please Master!"
p "That's what I like to hear slave!"
label DebbyFrontFuckDay05b:
scene debbybed04b with dissolve
play sound "Sounds/debbyfuck03.mp3"
$ renpy.pause(0.3, hard=True)
scene debbybed04a with dissolve
$ renpy.pause(0.3, hard=True)
scene debbybed04b with dissolve
$ renpy.pause(0.3, hard=True)
scene debbybed04a with dissolve
$ renpy.pause(0.3, hard=True)
scene debbybed04b with dissolve
$ renpy.pause(0.3, hard=True)
scene debbybed04a with dissolve
$ renpy.pause(0.3, hard=True)
scene debbybed04b with dissolve
$ renpy.pause(0.3, hard=True)
scene debbybed04a
$ renpy.pause(0.3, hard=True)
scene debbybed04b
$ renpy.pause(0.3, hard=True)
scene debbybed04a
$ renpy.pause(0.3, hard=True)
scene debbybed04b
$ renpy.pause(0.3, hard=True)
scene debbybed04a
$ renpy.pause(0.3, hard=True)
scene debbybed04b
$ renpy.pause(0.3, hard=True)
scene debbybed04a
$ renpy.pause(0.3, hard=True)
scene debbybed04b
$ renpy.pause(0.3, hard=True)
scene debbybed04a
$ renpy.pause(0.3, hard=True)
scene debbybed04b
$ renpy.pause(0.3, hard=True)
scene debbybed04a
$ renpy.pause(0.3, hard=True)
scene debbybed04b
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump DebbyFrontFuckDay05b
    "Move on":
        p "Your dirty hole is creaming all over the place, let's switch position whore!"
        jump DebbyFuckChoiceDay05b

label DebbyBedMovie05:
scene debbyballs with dissolve
$ renpy.pause(1.0, hard=True)
d "I can feel your balls are ready to unleash their massive store of pent-up young and yummy cum Master!"
p "Fuck yeah! I'm close to bursting a nut, finish me off slave!"
play music "Sounds/debbybedslow.mp3"
show debbybedslow
show faster
call screen debbyfuckslowDay05
screen debbyfuckslowDay05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("DebbyFuckFastDay05")
label DebbyFuckFastDay05:
hide faster
stop music
play music "Sounds/debbybedfast.mp3"
show debbybedfast
show cum
call screen debbyfuckfastDay05
screen debbyfuckfastDay05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("DebbyFuckCumDay05")

label DebbyFuckCumDay05:
hide debbybedslow
hide debbybedfast
stop music
scene debbybedcum01
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(1.0, hard=True)
d "Ooh Master, such a BIG load for your slave! Let me swallow the rest of it!"
play sound "Sounds/debbycum02.mp3" 
$ renpy.pause(4.0, hard=True)
scene debbybedcum02 with dissolve
window hide
play sound "Sounds/cumming.mp3" 
$ renpy.pause(3.0, hard=True)
d "Your slave will pull your giant cock out of her poor little destroyed pussy so you can cover her filthy whore body in your cream!"
scene debbybedcum03 with dissolve
play sound "Sounds/cumming.mp3" 
$ renpy.pause(3.0, hard=True)
d "Yes, more, empty those massive balls Master!"
play sound "Sounds/debbycum01.mp3" 
$ renpy.pause(8.0, hard=True)
d "Mmh, this is the biggest load I ever had.... Thank you for your generous cummy offering Master!"
$ hour +=1
$ stamina -=1
show staminaminus01:
    xalign 0.3 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01    
if (debbyjosewin == False) and (debbywin == False):
    p "(She didn't notice I took a picture of her being filled by my dick... Now I'll send it to José)."
    $ debbywin = True
if (debbyjosewin == True):
    p "(I hate sloppy seconds, especially after that dickhead José already ploughed their insides... But it was worth it, Debby is such a filthy whore!)"
$ debbyfucked = True
$ debbyfuckedhome = True
$ debbycarwashed = True
$ debbycarunwashed = False
if (nikkifucked == True) and (nancyfucked == True) and (achievement.has("homesteader") == False):
    show achievement07:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement07
    $ achievement.grant("homesteader")
if (tanyafucked == True) and (francinefucked == True) and (teaganfucked == True) and (achievement.has("king") == False):
    show achievement13:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement13
    $ achievement.grant("king")
if (hour == 20):
    p "I'd better get going, it's dinner time and I'm late!"
    d "Don't tell anyone about this, okay?"
    if (debbyjosewin == True):
        p "Umpf, coming from a whore who fucked José, that's grand!"
        scene debbybedcum03b
        d "What? But... How do you know? That little shit!"
        p "That's right, he's a fucking douchebag and you screwed him! That makes YOU a FILTHY WHORE!"
        d "I'm so ashamed of myself... I'm just a dirty slut... You'd better go home and leave your whore of a slave alone..."
        jump DinnerDay05
    menu:
        "Fine, but don't you dare get anywhere near that arsehole José, you hear me slave? (Cockblock José)":
            d "Yes, Master."
            $ josedebbycockblocked = True
            jump DinnerDay05
        "Alright, but I want 5 bucks for my silence...SLAVE!":
            d "There you are, you greedy little pig! Now get out of my house!"
            $ money += 5
            jump DinnerDay05

if (hour <= 19):
    p "I'd better get going now.... You drained my nuts..."
    d "Don't tell anyone about this, okay?"
    if (debbyjosewin == True):
        p "Umpf, coming from a whore who fucked José, that's grand!"
        scene debbybedcum02b
        d "What? But... How do you know? That little shit!"
        p "That's right, he's a fucking douchebag and you screwed him! That makes YOU a FILTHY WHORE!"
        d "I'm so ashamed of myself... I'm just a dirty slut... You'd better go home and leave your whore of a slave alone..."
        jump BurbsDay05
    menu:
        "Fine, but don't you dare get anywhere near that arsehole José, you hear me slave? (Cockblock José)":
            d "Yes, Master."
            $ josedebbycockblocked = True
            jump BurbsDay05
        "Alright, but I want 5 bucks for my silence...SLAVE!":
            d "There you are, you greedy little pig! Now get out of my house!"
            $ money += 5
            jump BurbsDay05

label HomeDay05:
stop music
scene livingroom01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah, home sweet home..."

if (hour == 17 or hour == 18) and (katephotoplanned05 == True) and (katephotoshoot05 == False) and (katephotoshootleft05 == False):
    p "I think Kate should arrive anytime now for our little photoshoot session... I hope it gets steamy fast..."
    jump KateShoot01Day05  
    
if (hour == 20):
    p "Just in time for dinner..."
    jump DinnerDay05

label Home02Day05:
stop music
scene livingroom01 with dissolve
if (hour == 20):
    p "Time for dinner..."
    jump DinnerDay05

p "What should I do?"
menu:
    "Go to my room":
       jump RyanBedroomDay05
    "Go to the bathroom":
        jump BathRoomDay05
    "Go to Nancy's room" if (momroomseen05 == False):
        jump MomRoomDay05
    "Go to the swimming pool" if (locswimmingpool == False):
        jump SwimmingPoolDay05
    "Leave the house":
        jump BurbsDay05

label SwimmingPoolDay05:
$ locswimmingpool = True
if (hour <= 18):
    scene poolempty with dissolve
    play music "Sounds/gardensound.mp3"
    $ renpy.pause(1.0, hard=True)
    p "There's no one around, I can't even, like, perv on Nancy or Nikki in a bikini right now. SAD."
    $ locswimmingpool = False
    jump Home02Day05
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
    jump DinnerDay05

label RyanBedroomDay05:
stop music
$ locroom = True
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
if (hour >= 20):
    $ hour = 20
    p "Oh, it's time for dinner, I'd better hurry downstairs..."
    jump DinnerDay05
if (hour == 17 or hour == 18) and (katephotoplanned05 == True) and (katephotoshoot05 == False) and (katephotoshootleft05 == False):
    p "I think Kate should arrive anytime now for our little photoshoot session... I hope it gets steamy fast..."
    jump KateShoot01Day05  

p "What to do, what to do..."
menu:
    "Turn the computer on":
        jump ComputerDay05
    "Do some heavy bodybuilding (+2hrs)" if (hour <= 18):
        if (workout == True):
            "You already trained today."
            jump RyanBedroomDay05
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
            jump RyanBedroomDay05        
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump RyanBedroomDay05
    "Go the living room":
        jump Home02Day05
    "Go to the bathroom" if (showerseen05 == False):
        jump BathRoomDay05
    "Go to Nancy's room" if (momroomseen05 == False):
        jump MomRoomDay05
    "Read the book Laura gave you (+1hr)" if (book == True) and (bookread == False):
        jump RyanReadingDay05

label RyanReadingDay05:
scene ryanreading with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump RyanBedroomDay05

label ComputerDay05:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label Computer02Day05:
scene ryancomputerday
menu:
    "Check the map":
        jump MapDay05
    "Check the stats":
        jump StatsDay05
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump Computer02Day05
    "Learn how to use the pendulum" if (pendulum == True) and (pendulumactive ==False):
        jump CompPendulumDay05
    "Play a smutty game (+1hr)":
        jump CompGameDay05
    "Turn the computer off":
        jump RyanBedroomDay05

label CompPendulumDay05:
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump Computer02Day05

label MapDay05:
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
if (discoverclinic == True):
    show clinicmap
if (discovercabin == True):
    show cabinmap
if (discoverfalls == True):
    show waterfallsmap
if (discoveranna == True):
    show annamap    
p "This shows all the places I know so far on Veri-Bosti Island..."
show screen statsbackground
show screen inventorybutton
show screen calendar
jump Computer02Day05

label StatsDay05:
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
jump Computer02Day05

label CompGameDay05:
scene ryancomputergameday
$ renpy.pause(1.0, hard=True)
p "This game is tough. My fingers hurt like hell from so much clicking..."
$ hour += 1
jump Computer02Day05

label MomRoomDay05:
scene nancybedroomday with dissolve
$ renpy.pause(1.0, hard=True)
$ momroomseen05 = True
p "Nancy's room is so clean and tidy. Not like mine."
menu:
    "Snoop around" if (dildo == False):
        jump MomBedroomSnoopDay05  
    "Go back to my room":
        jump RyanBedroomDay05
    "Put the dildo back in its drawer" if (dildo == True):
        show dildo
        show square
        play sound "Sounds/lost.mp3"
        "You relinquish a giant black dildo. Yes, that's right, \"relinquish\". Look it up in the dictionary."
        hide square
        hide dildo
        $ dildo = False
        jump RyanBedroomDay05

label MomBedroomSnoopDay05:
p "There might be an interesting item hidden somewhere... Time to snoop around..."
p "But I have a limited amount of time to look for it, Nancy might come back from work anytime for all I know."
play music "Sounds/snooping.mp3"
call screen mombedroomsnoopDay05
stop music
"You were too slow and didn't find anything."
jump RyanBedroomDay05

label FoundDildoDay05:
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
jump RyanBedroomDay05

label BathRoomDay05:
stop music
if (hour <= 17):
    jump EmptyBathRoomDay05
if (hour == 18) or (hour == 19):
    jump MomShowerDay05

label EmptyBathRoomDay05:
scene bathroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "No one is around right now, I could take a shower if I wanted to."
menu:
    "Take a shower":
        jump ShowerDay05
    "Leave":
        jump RyanBedroomDay05

label ShowerDay05:

scene shower with dissolve
stop music
play music "Sounds/shower.mp3"
$ renpy.pause(1.0, hard=True)
p "That's nice and relaxing..."
if (stamina <= 4) and (showerseen05 == False):
    window hide
    $ stamina += 1
    show stamina01:
        xalign 0.4 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide stamina01
$ showerseen05 = True
jump RyanBedroomDay05

label MomShowerDay05:
play music "Sounds/shower.mp3"
$ locroom = False
scene bathroomdoorclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "Someone's taking a shower..."
menu:
    "Use lubricant on the door hinges" if (wd69 == True) and (squeakfixed == False):
        "The door should not squeak anymore."
        $ squeakfixed = True
        jump MomShowerDay05        
    "Have a peek":
        jump MomPeekBathroomDay05
    "Leave":
        jump RyanBedroomDay05

label MomPeekBathroomDay05:
if (squeakfixed == False):
    play sound "Sounds/doorsqueak.mp3"
    scene bathroomdooropen with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Shit, the door is squeaking..."
    m "I'm in the shower sweetie, don't get in!"
    p "Ah, sorry Nancy...I'm leaving..."
    p "Damn, I should try and find a way of stopping that door from squeaking if I want to spy on Nancy or Nikki in the shower like every other MC..."
    jump RyanBedroomDay05
if (squeakfixed == True):
    scene nancyshower01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Cool, she didn't hear me come in, I can see her naked in the shower now..."
    p "Fuck yeah, look at those huge titties... How I would love to rub my pud between them..."
menu:
        "Watch a little longer...":
            jump MomShower02Day05
        "Leave before she turns round and catches me":
            jump RyanBedroomDay05
    
label MomShower02Day05:
if (momshowerpeep == False):
    $ peeping += 1
$ momshowerpeep = True
scene nancyshower02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, her arse was made for fucking a great big cock. MY giant cock!"
menu:
        "Watch a little longer still...":
            jump MomShower03Day05
        "Leave before she turns round and catches me":
            jump RyanBedroomDay05
 
label MomShower03Day05:
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
jump RyanBedroomDay05

label KateShoot01Day05:
play sound "Sounds/doorbell.mp3"
scene katehouse01 with dissolve
$ renpy.pause(1.0, hard=True)
k "Hi, it's meeee! I came for our photo shoot!"
window hide
play sound "Sounds/katehihi.mp3"                     
$ renpy.pause(1.0, hard=True)
if (camera == False):
    p "Hi Kate, err, there's a small problem, my camera is broken, I need to get it fixed..."
    scene katehouse02 with dissolve
    $ renpy.pause(1.0, hard=True)
    k "Oooh, but you promised me and I came all the way from my house... You let me down [name] and I wasted my afternoon..."
    $ lust_points[11] -=2
    $ score -= 2
    show lustminus02:
        xalign 0.4 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus02
    p "I'm really sorry, it will be fixed tomorrow, I promise..."
    "Kate leaves, looking very disappointed..."
    $ katephotoshootleft05 = True
    scene livingroom01 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Home02Day05

if (camera == True):
    p "Hi Kate, alright, everything is set up and we are ready to roll...the roll."
    scene katehouse03 with dissolve
    $ renpy.pause(1.0, hard=True)
    k "Oooh, I'm so excited! I'm gonna get to see myself in a bikini!"
    p "Yeah, that's right, the wonders of modern technology... Why don't you change into your first outfit and come by the pool, I'll be waiting for you."
    jump KateShoot02Day05

label KateShoot02Day05:
play music "Sounds/gardensound.mp3"
scene katepool01 with dissolve
$ renpy.pause(1.0, hard=True)
k "I decided for this blue bikini first. Does it look good on me?"
p "Fabulous, now let me take a picture..."
scene katepool01 with flash
play sound "Sounds/flash.mp3"
p "Turn round, that way I'll be able to show you your lovely butt..."
scene katepool02 with dissolve
play sound "Sounds/katehihi.mp3"
$ renpy.pause(1.0, hard=True)
k "You're so naughthy... I'll get another bikini... The one I was thinking of wearing at the pageant..."
scene katepool02 with flash
play sound "Sounds/flash.mp3"
p "Sure, I'll wait and make sure there is enough roll..."
scene katepool03 with dissolve
$ renpy.pause(1.0, hard=True)
k "This one... What do you think?"
p "Wow, I think it's a great choice!"
scene katepool03 with flash
play sound "Sounds/flash.mp3"
scene katepool04 with dissolve
$ renpy.pause(1.0, hard=True)
k "And the back. It doesn't cover much, I feel almost naked..."
scene katepool04 with flash
play sound "Sounds/flash.mp3"
p "Maybe pose on the deck, look at the camera..."
scene katepool05 with dissolve
$ renpy.pause(1.0, hard=True)
k "Like that?..."
scene katepool05 with flash
play sound "Sounds/flash.mp3"
p "Yeah, perfect... Stand up and look naughty for the camera Kate..."
scene katepool06 with dissolve
play sound "Sounds/katehihi.mp3"
$ renpy.pause(1.0, hard=True)
k "I like being naughty... for you..."
scene katepool06 with flash
play sound "Sounds/flash.mp3"
p "I'll show you the photos if you want..."
k "Oh goodie!"
$ katephotoshoot05 = True

scene katepool07 with dissolve
$ renpy.pause(1.0, hard=True)
k "Oh, this is what I look like? I didn't realize my boobies were so...BIG!"
p "Yeah, and you're so fit, we could make some money sending these shots to \"Fitness Babes and Studs Illustrated\"..."
k "Don't they have both a girl and a man in those shoots?"
p "I can set up the camera on a tripod with a timer and be the \"stud\" if you want..."
scene katepool07b with dissolve
k "It sure looks like you could... You're so muscular... OK, let's do it! Hee hee!"
play sound "Sounds/katehihi.mp3"
$ renpy.pause(1.0, hard=True)
p "Ok, I'll change into my speedos then and be right back!"

scene katepool08 with dissolve
$ renpy.pause(1.0, hard=True)
k "Oh, wow [name]..."
$ lust_points[11] += 2
$ score += 2
show lust02:
    xalign 0.2 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
if (lust_points[11] >= 10):
    show epiclust:
        xalign 0.2 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust

p "How about I pose like He-man and you look at me from below?"
k "Uuh... Ok."
scene katepool09 with dissolve
$ renpy.pause(1.0, hard=True)
k "Can I touch it? I've never seen anything that big before!"
p "Sure, I'll let a pint of blood flow into it so it's even bigger for you..."
play sound "Sounds/katehihi.mp3"
$ renpy.pause(1.0, hard=True)
scene katepool10 with dissolve
if (lust_points[11] == 9):
    $ lust_points[11] += 1
    $ score += 1
    show lust01:
        xalign 0.2 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[11] <= 8):
    $ lust_points[11] += 2
    $ score += 2
    show lust02:
        xalign 0.2 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
if (lust_points[11] == 10):
    show epiclust:
        xalign 0.2 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
k "Oh fuck [name], it's so big..."
window hide
play sound "Sounds/kate01.mp3"
$ renpy.pause(4.0, hard=True)
p "Of course Kate. It's all for you..."
if (lust_points[11] <= 9):
    k "I think it's too big. I'm scared, I want to go home..."
    p "But, I've got like a massive semi for you!"
    k "Another time maybe [name], I'm not used to this..."
    jump RyanBedroomDay05

if (stamina <= 0) and (whitebull == True):
    p "I'd better drink some White Bull if I want to be able to perform...."
    menu:
        "Drink white bull (+2 stamina)":
            show whitebull
            show square
            play sound "Sounds/lost.mp3"
            "You gulped down your White Bull energy drink."
            hide square
            hide whitebull
            $ whitebull = False
            $ stamina += 2
            jump KatePool11Day05
        "Don't drink white bull and keep it for another time":
            p "Actually, we really shouldn't... I mean, the neighbors might see us and all that..."
            k "What? But... I don't understand... Why did you bring me here?"
            p "For a photoshoot remember? Come on, off you go Kate. I'll see you tomorrow at school."
            k "Uh, oh... Okay."
            $ hour += 1
            jump RyanBedroomDay05

label KatePool11Day05:
scene katepool11 with dissolve
$ renpy.pause(1.0, hard=True)
k "It's so incredibly thick! I'm having trouble taking it out..."
p "I'll help you, I'll just drop the speedos altogether... Why don't you drop your top too?"
k "Hee hee... That is so NAUGHTY!"
scene katepool12 with dissolve
$ renpy.pause(1.0, hard=True)
k "Look at you, those bulging rock-hard muscles... and that COCK! I can't even get my hand all the way around it and it's not even fully hard!"
window hide
play sound "Sounds/kate01.mp3"
$ renpy.pause(3.0, hard=True)
p "Keep wanking it like that and it will be rock-hard very soon!"
menu:
    "Stick your pud between her legs from behind":
        jump KateBehindDay05
    "Push her down and place the head near her pussy":
        jump KatePussyDay05
    "Push her down and stick your rod between her tits":
        jump KateTitsDay05

label KateBehindDay05:
stop music
scene katepool13 with dissolve
$ katelegs = True
$ renpy.pause(1.0, hard=True)
k "Oooh... It's sticking straight out way past my tummy. It's like I have a huge cock of my own, hee hee!"
p "And what would you do if it was yours?..."
k "Uuuh... I'd probably...."
scene katepool18 with dissolve
$ renpy.pause(1.0, hard=True)
k "Hold it like that and tug hard on it like I was wanking my big hard shaft..."
scene katepoolwank01 with dissolve
$ renpy.pause(1.0, hard=True)
label KateBehindDay05b:
play sound "Sounds/wanking.mp3"
scene katepoolwank01b with dissolve
$ renpy.pause(0,3, hard=True)
scene katepoolwank01 with dissolve
$ renpy.pause(0.3, hard=True)
scene katepoolwank01b with dissolve
$ renpy.pause(0,3, hard=True)
scene katepoolwank01 with dissolve
$ renpy.pause(0.3, hard=True)
scene katepoolwank01b with dissolve
$ renpy.pause(0,3, hard=True)
scene katepoolwank01 with dissolve
$ renpy.pause(0.3, hard=True)
scene katepoolwank01b with dissolve
$ renpy.pause(0,3, hard=True)
scene katepoolwank01 with dissolve
$ renpy.pause(0.3, hard=True)
k "God, this is so hot, hi hi!"
scene katepoolwank01b
play sound "Sounds/wanking.mp3"
$ renpy.pause(0.4, hard=True)
scene katepoolwank01
$ renpy.pause(0.4, hard=True)
scene katepoolwank01b
$ renpy.pause(0.4, hard=True)
scene katepoolwank01
$ renpy.pause(0.4, hard=True)
scene katepoolwank01b
$ renpy.pause(0.4, hard=True)
scene katepoolwank01
$ renpy.pause(0.4, hard=True)
scene katepoolwank01b
$ renpy.pause(0.4, hard=True)
scene katepoolwank01
$ renpy.pause(0.4, hard=True)
scene katepoolwank01b
$ renpy.pause(0.4, hard=True)
scene katepoolwank01
$ renpy.pause(0.4, hard=True)
scene katepoolwank01b
$ renpy.pause(0.4, hard=True)
scene katepoolwank01
$ renpy.pause(0.4, hard=True)

menu:
    "Repeat":
        jump KateBehindDay05b
    "Move on":
        pass
p "Oh, you're going too fast, I'm... gonna..."
scene katepool19
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
k "Oh, look, I'm cumming huge wads everywhere!"
p "Please...stop it... I don't want to empty my balls... just yet!"
k "Oooh, I hope you have some more for meeee!"
p "Yeah, don't worry, it was just a small load... I came quickly but it didn't affect my mammoth erection!"
menu:
    "Push her down and place the head near her pussy" if (katepussy == False):
        jump KatePussyDay05
    "Push her down and stick your rod between her tits" if (katetits == False):
        jump KateTitsDay05
    "Lift her up and fuck her sweet hole" if (katelegs == True) and (katepussy == True) and (katetits == True):
        jump KateLiftDay05

label KatePussyDay05:
scene katepool14 with dissolve
$ katepussy = True
$ renpy.pause(1.0, hard=True)
k "Oooh, you're so forceful [name]! What are you going to do to poor little me?"
p "I'm going to give you what you came for, that's what!"
k "Your...your giant cock? hee...hee..."
window hide
play sound "Sounds/katehihi.mp3"
scene katepool15 with dissolve
$ renpy.pause(1.0, hard=True)
p "Yeah, that's right!"
$ renpy.pause(1.0, hard=True)
k "OOoh (puff) Aaah... It's really stretching me!"
p "The pain will pass once I pound it harder into you... like that!"
scene katepool16a with dissolve
$ renpy.pause(1.0, hard=True)
label KatePussyDay05b:
scene katepool16b with dissolve
play sound "Sounds/kate03.mp3"
$ renpy.pause(0.3, hard=True)
scene katepool16a with dissolve
$ renpy.pause(0.3, hard=True)
scene katepool16b with dissolve
$ renpy.pause(0.3, hard=True)
scene katepool16a with dissolve
$ renpy.pause(0.3, hard=True)
scene katepool16b with dissolve
$ renpy.pause(0.3, hard=True)
scene katepool16a with dissolve
$ renpy.pause(0.3, hard=True)
scene katepool16b with dissolve
$ renpy.pause(0.3, hard=True)
scene katepool16a with dissolve
$ renpy.pause(0.3, hard=True)
scene katepool16b with dissolve
$ renpy.pause(0.3, hard=True)
scene katepool16a with dissolve
$ renpy.pause(0.3, hard=True)
scene katepool16b with dissolve
$ renpy.pause(0.2, hard=True)
scene katepool16a with dissolve
$ renpy.pause(0.2, hard=True)
scene katepool16b with dissolve
$ renpy.pause(0.2, hard=True)
scene katepool16a with dissolve
$ renpy.pause(0.2, hard=True)
scene katepool16b with dissolve
$ renpy.pause(0.2, hard=True)
scene katepool16a with dissolve
$ renpy.pause(0.2, hard=True)
scene katepool16b with dissolve
$ renpy.pause(0.2, hard=True)
scene katepool16a with dissolve
$ renpy.pause(0.2, hard=True)
menu:
    "Repeat":
        jump KatePussyDay05b
    "Stick your pud between her legs from behind" if (katelegs == False):
        jump KateBehindDay05
    "Push her down and stick your rod between her tits" if (katetits == False):
        jump KateTitsDay05
    "Lift her up and fuck her sweet hole" if (katelegs == True) and (katepussy == True) and (katetits == True):
        jump KateLiftDay05

label KateTitsDay05:
scene katepool20 with dissolve
$ katetits = True
$ renpy.pause(1.0, hard=True)
p "I think those big jugs of yours are a perfect match for my massive erection!"
k "Uuhh, oooh, you think so?"
p "For sure, I'm dripping precum all over the place cos they make me so horny!"
k "Oooh, I'm so glad you like them..."
menu:
    "Stick your pud between her legs from behind" if (katelegs == False):
        jump KateBehindDay05
    "Push her down and place the head near her pussy" if (katepussy == False):
        jump KatePussyDay05
    "Lift her up and fuck her sweet hole" if (katelegs == True) and (katepussy == True) and (katetits == True):
        jump KateLiftDay05

label KateLiftDay05:
scene katepool17 with dissolve
$ renpy.pause(1.0, hard=True)
k "Uuhh, what? You're lifting me up on your COCK? God, it's ssooo powerful!"
p "Ready for a wild ride Kate?"

stop music
play music "Sounds/kateslow.mp3"
show katefuckslow
show faster
call screen katefuckscreen05
screen katefuckscreen05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("KateFuckFastDay05")

label KateFuckFastDay05:
stop movie
hide faster
play music "Sounds/kate04.mp3"
show katefuckfast
show cum
call screen katefuckscreen05b
screen katefuckscreen05b:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("KateFuckCumDay05")

label KateFuckCumDay05:
hide katefuckslow
hide katefuckfast
stop music
play music "Sounds/gardensound.mp3"
scene katepoolcum01
play sound "Sounds/cumming.mp3"
$ renpy.pause(3.0, hard=True)
k "Oooh, you're spraying your huge load everywhere! On the deck, on my tits, on my face.... I love it! More, more [name]!"
scene katepoolcum02 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
p "I can't stop cumming! AAAHH, this is so good!"
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
if (katejosewin == False):
    $ katewin = True
$ katefucked = True
$ fuckedschoolgirlDay05 = True
$ hour += 1
if (maddyfucked == True) and (laurafucked == True) and (friedafucked == True) and (achievement.has("classroom") == False):
    show achievement03:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement03
    $ achievement.grant("classroom")

if (hour == 18):
    k "We should take a dip in the pool to clean ourselves of all this cum you've unloaded everywhere! Hee hee!"
    p "I'd better clean the deck, you go in the pool."
    k "Oooh, OK."
    scene katepoolend with dissolve
    $ renpy.pause(1.0, hard=True)
    k "The pool water is so great..."
    p "(It's so nice to see poor Kate so happy. Especially after she got detention again today.)"
    k "I'm clean now, I'd better get going. See you tomorrow [name]!"
    p "Yep, see you at school tomorrow Kate!"
    jump RyanBedroomDay05    
if (hour == 19):
    scene katepoolcum03 with dissolve
    $ renpy.pause(1.0, hard=True)
    m "What on earth is going on here? [name], who is this girl you're fucking in MY house?"
    if (nancyfucked == False):
        $ lust_points[16] -=2
        $ score -= 2
        show lustminus02:
            xalign 0.1 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus02
    s "God, you're such a perv, I can't believe you're doing this in broad daylight in our garden..."
    if (nikkifucked == False):
        $ lust_points[17] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.4 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
    menu:
        "Hum... It's not what it looks like! She assaulted me, she's a total nympho!":
            k "What? Oooh, that's mean, that's not true!"
            m "My God, on top of that, you lie to me! Now get dressed and let go of this poor girl!"
            $ lust_points[16] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.1 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            jump RyanBedroomDay05
        "Ah... Let me introduce you to my new classmate Kate. Kate, my landlady and her daughter.":
            m "Who the hell do you think you're kidding? Get dressed and get this \"Kate\" girl out of here!"
            jump RyanBedroomDay05
        "Well, a man's got to do what a man's got to do, right?":
            m "Not HERE in our garden! Now get dressed both of you, I don't want to see such a lewd display in MY house any longer!"
            jump RyanBedroomDay05

label TeaganHouse02Day05:
$ seenteaganhouseday05 = True
scene teagan01day05 with dissolve
play music "Sounds/gardensound.mp3"
play sound "Sounds/swimming.mp3"
$ renpy.pause(1.0, hard=True)
p "Oh, there she is, swimming in a different outfit this time... Nice."
t "Oh, Hello [name], you brought my groceries again? How nice of you! Put them in the kitchen my dear, I'd rather stay in the pool, it's so hot..."
p "Sure Ms Cocque... I'll be right back."
stop sound
scene teagankitchenempty with dissolve
$ renpy.pause(1.0, hard=True)
p "I'll just put them here on the counter. And go back to join the teacher. Hoping I'll get a nice reward for that..."
scene teagan02day05 with dissolve
play sound "Sounds/swimming.mp3"
$ renpy.pause(1.0, hard=True)
t "Why don't you join me in the pool to cool down a bit after carrying such heavy grocery bags?"
menu:
    "Sure, thanks for the offer Ms Cocque!":
        jump TeaganPool01Day05
    "I'm kinda busy right now, I'm already late for...err... some other stuff.":
        t "Fine, I'll see you tomorrow at school then [name]... 9 am sharp!"
        t "Here's five bucks for bringing my groceries over."
        $ money += 5
        jump BurbsDay05

label TeaganPool01Day05:
scene teagan03day05 with dissolve
$ renpy.pause(1.0, hard=True)
p "I can see her ogling my bulge... Good thing I got a semi while admiring her, it must look even bigger than usual..."
window hide
if (teaganfucked == True):
    t "Just as big as I remember it yesterday..."
    p "I'm not even hard yet teach, it will grow even bigger!"
    t "I know... YOu are so MASSIVE when you are rock-hard... Come in the pool with me stud!"
    jump TeaganPool02Day05
if (lust_points[22] <= 9):
    $ lust_points[22] += 1
    $ score += 1
    show lust01:
        xalign 0.2 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[22] == 10):
    show epiclust:
        xalign 0.3 yalign 0.4
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
t "Wow... [name], you really have an incredible body for such a young boy..."
p "And you have an incredible body too Ms Cocque for...err... a schoolteacher."
t "Come into the pool clumsy boy. I'll let you get a closer look at it if you like it so much..."

label TeaganPool02Day05:
scene teagan04day05 with dissolve
$ renpy.pause(1.0, hard=True)
t "You know, it's highly inappropriate for a teacher to be spending time like this with a student..."
t "So let's just pretend you are only my delivery boy today... and not a boy in the class I teach."
p "Sure Ms Cocque, I don't mind role-playing!"
t "So... What do you have for me Mr grocery boy? (wink)"
label TeaganPool02Day05b:
menu:
    "I picked up an extra-large zucchini for you ma'am!":
        if (lust_points[22] == 10):
            t "That is so corny [name]... Try again."
            jump TeaganPool02Day05b
        t "That is so corny [name]... I don't want to play anymore. Please go home. (sigh)"
        p "But... What about my zucchini? Don't you want to see my big zucchini?"
        jump BurbsChoiceDay05
    "I do pick-ups and deliveries. Right now, I'm picking you up...":        
        t "Ooh? And when will the delivery be?"
        scene teagan05day05 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "In a while... I first need to unpack those heavy bags..."
        if (teaganfucked == True):
            t "You like them don't you... And I KNOW you liked fucking them with your huge, young, hard COCK!"
            p "What can I say, I can't resist such lovely MILF knockers..."
            t "Let's move out of the pool, I want to see that monstercock of yours again!"
            jump TeaganFuckChoicePreDay05
        if (lust_points[22] <= 9):
            $ lust_points[22] += 1
            $ score += 1
            show lust01:
                xalign 0.6 yalign 0.5
                linear 1.0 yalign 0.3
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
            if (lust_points[22] == 10) and (teaganfucked == False):
                show epiclust:
                    xalign 0.7 yalign 0.4
                    zoom 0.5
                    linear 2.0 zoom 1.0
                play sound "Sounds/epiclust.mp3"
                $ renpy.pause(4.0, hard=True)
                hide epiclust
        if (lust_points[22] == 10) and (teaganfucked == False):
            t "You like them don't you, naughty boy?"
            p "What can I say, I can't resist such lovely MILF knockers..."
            t "Let's move out of the pool, I want to see that monstercock of yours!"
            jump TeaganFuckChoicePreDay05
        t "Oh... I like it... But I think this is going too far young man..."
        p "What do you mean?"
        t "I'm your teacher... I can't... let a student fondle my big breasts like that. What if a nosy neighbor reported on us?"
        t "It's best that you leave [name]. I'll see you tomorrow at school..."
        p "But I'm not your student, you said it! I'm just your delivery boy, it's not fair!"
        jump BurbsChoiceDay05

label TeaganFuckChoicePreDay05:
if (stamina <= 0) and (whitebull == True):
    p "I'd better drink some White Bull if I want to be able to perform...."
    menu:
        "Drink white bull (+2 stamina)":
            show whitebull
            show square
            play sound "Sounds/lost.mp3"
            "You gulped down your White Bull energy drink."
            hide square
            hide whitebull
            $ whitebull = False
            $ stamina += 2
            jump TeaganFuckChoiceDay05
        "Don't drink white bull and keep it for another time":
            p "Teagan, I'm having second thoughts. I read so many stories of teachers going to jail because they fucked their student..."
            p "I wouldn't want that to happen to you..."
            t "What? You're fondling my tits and then you don't want to fuck me? Get out of my house at once [name]!"
            jump BurbsChoiceDay05

label TeaganFuckChoiceDay05:
stop music
scene teaganchoiceday05 with dissolve
$ renpy.pause(1.0, hard=True)
t "So, now that you are here, proudly displaying your gigantic erection to your schoolteacher, what would you like us to do [name]?"
menu:
    "I think anal is in order. Yes, anal." if (teagananalday05 == False):
        t "That massive fuckstick up my arse? You can't be serious..."
        p "I am serious and I'll prove it!"        
        jump TeaganAnalDay05
    "My studcock is sore from so much fucking. It needs a nice foot massage." if (teaganfeet == False):
        t "Mmh, you're a footboy are you? Then get ready for the best footjob in town stud!"
        jump TeaganFeetDay05
    "Get in the lounge chair, I'm gonna pound that sweet teacher pussy of yours!" if (teaganpussy == False):
        t "It's ready to receive your massive teenage pussy-pleaser!"
        jump TeaganPussyDay05
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (teaganpussy == True) and (teaganfeet == True) and (teagananalday05 == True):
        t "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump TeaganMovieDay05

label TeaganAnalDay05:
$ teagananalday05 = True
scene teagananal01 with dissolve
$ renpy.pause(1.0, hard=True)
p "How do you like your student's cock up your fuckhole teach?"
t "I'm such a dirty slut... Pound me with your massive fuckstick I beg you!"
scene teagananal02 with dissolve
$ renpy.pause(1.0, hard=True)
t "AAAH, it's so fucking deep!"
label TeaganAnalDay05b:
play sound "Sounds/teagananal.mp3"
scene teagananal01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagananal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagananal01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagananal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagananal01
$ renpy.pause(0.3, hard=True)
scene teagananal02
$ renpy.pause(0.3, hard=True)
scene teagananal01
$ renpy.pause(0.3, hard=True)
scene teagananal02
$ renpy.pause(0.3, hard=True)
scene teagananal01
$ renpy.pause(0.3, hard=True)
scene teagananal02
$ renpy.pause(0.3, hard=True)
scene teagananal01
$ renpy.pause(0.3, hard=True)
scene teagananal02
$ renpy.pause(0.3, hard=True)
scene teagananal01
$ renpy.pause(0.3, hard=True)
scene teagananal02
$ renpy.pause(0.3, hard=True)
scene teagananal01
$ renpy.pause(0.3, hard=True)
scene teagananal02
$ renpy.pause(0.3, hard=True)
scene teagananal01
$ renpy.pause(0.3, hard=True)
scene teagananal02
$ renpy.pause(0.3, hard=True)
scene teagananal01
$ renpy.pause(0.3, hard=True)
scene teagananal02
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump TeaganAnalDay05b
    "Move on":
        t "Have mercy on my poor arse [name]!"
        p "Ok Teagan, I'll give you a respite. FOR NOW."
        jump TeaganFuckChoiceDay05

label TeaganFeetDay05:
$ teaganfeet = True
scene teaganfeet01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Ready? Cos my feet are going to make your dick extra-hard and extra-HUGE, guaranteed!"
p "Let's see if you're better than Sophia then shall we?"
t "Oh? A competition with the principal? I'm in!"
label TeaganFeetDay05b:
scene teaganfeet02 with dissolve
play sound "Sounds/teaganfeet.mp3"
$ renpy.pause(0.3, hard=True)
scene teaganfeet01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teaganfeet02 with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump TeaganFeetDay05b
    "Move on":
        pass    
t "Ooh, look at all that precum flowing from your tip...You're ready to pop aren't you? So, was it better than Sophia's footjobs?"
p "Y...Yes... So it's best if we move on to something else." 
jump TeaganFuckChoiceDay05    

label TeaganPussyDay05:
$ teaganpussy = True
scene teaganpussylick01 with dissolve
$ renpy.pause(1.0, hard=True)
p "First, I'm gonna lick your pussy..." 
scene teaganpussylick02 with dissolve
play sound "Sounds/lick.mp3"
$ renpy.pause(1.0, hard=True)
t "Mmh, yes, that's a good boy, licking your teacher's nasty fuckhole like that!"
t "I feel all tingly down there..."
p "I could tell, you were convulsing around my expert tongue..." 
p "Now it's time for you to convulse around my expert megadong..." 
t "Mmmh, I can't wait [name]..."
scene teagandoggy01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Split me in half with your giant fuckstick!"
label TeaganPussyDay05b:
scene teagandoggy02 with dissolve
play sound "Sounds/teagandoggy.mp3"
$ renpy.pause(0.3, hard=True)
scene teagandoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene teagandoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump TeaganPussyDay05b
    "Move on":
        pass    

jump TeaganFuckChoiceDay05    

label TeaganMovieDay05:
scene teaganfuckmovieday05 with dissolve
p "Bounce up and down on my dong teach! I want to be buried balls-deep inside you!"
t "OOOh, I don't know if I can take that much cock [name], but I sure as hell will try!"
play music "Sounds/teaganfuckslow02.mp3"
show teaganfuckslow02
show faster
call screen teaganfuckslowday05
screen teaganfuckslowday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TeaganFuckFastDay05")

label TeaganFuckFastDay05:
stop music
hide faster
play music "Sounds/teaganfuckfast02.mp3"
show teaganfuckfast02
show cum
call screen teaganfuckfastday05
screen teaganfuckfastday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TeaganFuckCumDay05")

label TeaganFuckCumDay05:
hide teaganfuckfast02
hide teaganfuckslow02
stop music
scene teaganfuckcumb01
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
t "YES! Come inside me [name]! Your hot teacher wants her favorite student's cum sloshing inside her tonight!"
p "I'll fill you up Teagan, don't worry, your stomach will be bloated like a balloon with the amount I'm dumping inside you!"
t "YES, I can feel those heavy bursts of semen flooding my fuckhole! Don't forget to cover my tits too please!"
scene teaganfuckcumb02 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "Fuck yeah, I'm still going strong teach! Get ready for some heavy showers of spunk!!"
t "I am ready and I AM getting plastered in them! I can feel your balls expanding..."
scene teaganfuckcumb03 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "Your hot body is making my cock explode teach! AAAH!"
t "I've never had my huge knockers covered in so much cum before... And you're still cumming buckets!"
scene teaganfuckcumb04 with dissolve
$ renpy.pause(2.0, hard=True)
t "Let me milk the last huge dollops of cream from that cum-cannon....Mmh, just that is more than a normal guy comes in a full orgasm!..."
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
t "Jeezus! How long ago was it that you busted a nut [name]? You came sssooo much!"
p "Not that long ago Teagan... I just replenish my balls super-fast..."
t "Wow, that's incredible... A true alpha teen-stud!"
t "While I would love to have another go on that still rock-hard donkey-dick of yours, I have a faculty appointment with Principal Titsworthy I can't miss..."
t "So off you go, I'll see you tomorrow and don't say a word about this to anyone [name]!"
p "What about some money for bringing your groceries?"
t "You're kidding right? Tell me you're kidding..."
p "Err.. I guess so..."
$ teaganfucked = True
$ hour += 1
$ backdoor += 1
if (teaganjosewin == False):
    p "(She didn't notice I took a picture of her with her tits plastered in my cum... Now I'll send it to José)."
    $ teaganwin = True    
if (vivianefucked == True) and (sophiafucked == True) and (achievement.has("faculty") == False):
    show achievement10:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement10
    $ achievement.grant("faculty")
if (tanyafucked == True) and (debbyfucked == True) and (francinefucked == True) and (achievement.has("king") == False):
    show achievement13:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement13
    $ achievement.grant("king")
jump BurbsChoiceDay05

label Insemination01Day05:
stop music
scene clinic04 with dissolve
$ renpy.pause(1.0, hard=True)
dr "Ah, welcome back [name], are you ready to use your \"talents\" to help a poor wife whose husband is shooting blanks?"
p "What do you mean exactly?"
dr "Well, while most insemination programs use artificial means, some of our clients prefer the more \"traditional\" method of insemination."
dr "And there's 10 shiny dollars for you if you unleash one of your spectacular loads inside one of our customers who is here and awaiting insemination to get pregnant."
label Insemination01Day05b:
menu:
    "Na, not today doc.":
        dr "What a waste of a stud's life. Don't forget there are ten shiny dollars in it for you if you ever come back!"
        jump ClinicOutDay05
    "Your establishment is nothing but a depraved whorehouse exploiting men!":
        dr "Yes. And the problem is?"
        p "Well, err... Nothing."
        jump Insemination01Day05b
    "Alright, I'm in! Is she hot?":
        dr "She is indeed \"hot\" as you put it. We doctors prefer the legal term \"rapable\"."
        dr "However, I am not at liberty to disclose her identity and the deed shall be done anonymously through a specially-designed aperture in the wall."
        p "You mean a gloryhole."
        dr "While it is my inclination to refrain from using such vulgar terms, yes, it's just a gloryhole."
        dr "Nurse Racque will show you the way to the insemination room and get you prepared. Please follow her."
        jump Insemination02Day05    

label Insemination02Day05:
$ seenclinic05 = True
scene insemination01 with dissolve
$ renpy.pause(1.0, hard=True)
ra "So here we are, horse-hung boy, this is the prep room. Get undressed and take a shower."
ra "You have to prime that huge meatlog, so don't hesitate to pump it wildly and ask for help if you need it (wink)."
scene insemination02 with dissolve
play music "Sounds/shower.mp3"
$ renpy.pause(1.0, hard=True)
p "Fuck! Think about horny things, think about horny things... AAAH!"
scene insemination03 with dissolve
$ renpy.pause(1.0, hard=True)
ra "How are we doing in there? Don't cum yet, we need an extra-big load from you to be delivered directly into that customer's womb..."
ra "I know just the way to bring you over the edge without making you cum..."
scene insemination04 with dissolve
$ renpy.pause(1.0, hard=True)
ra "First, I'll gently massage your massive seedmakers... Mmmmh, they are so BIG!"
p "Yeah, that's good nurse Racque, I like how you play with them... Oooh..."
ra "Now hold off from blowing your load young man... I have another idea..."
scene insemination05 with dissolve
$ renpy.pause(1.0, hard=True)
ra "How about I gently lick your rock-hard shaft and tease it with my tongue..."
ra "Up and down.. Ever so slowly.... Licking the flowing precum as my tongue swirls over the vast expanse of your mighty fuckpole..."
p "Jeeezus nurse Racque, I'm ready to blow any time!"
ra "Then you are ready... Dry off and I'll take you to the insemination room. Just stick your pud through the hole and ram it up the customer's hungry twat on the other side, OK?"
p "O..OK, whatever you say!..."
ra "I won't dry off, I like the feeling of that oily soap on my skin..."
stop music
scene insemination06 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Let me help you position yourself Jenn... I mean Mrs Anonymous."
je "I hope you found a stud who can really deliver a big load. My hubby is such a wimp, he barely manages a dribble. That's why I don't get pregnant..."
ra "Don't worry, we managed to find a stud who cums so much your ovaries will be drowning in young virile seed!"
je "Oh goodie! I still have in mind the incredible amount of cum that [name] blasted in the jar the other day... But he's a student in my school, it would be so wrong..."
ra "I can assure you today's stud will come just as much as him! (wink)"
menu:
    "Hey, it's ME Jennifer, on the other side of the wall!":
        scene insemination07 with dissolve
        $ renpy.pause(1.0, hard=True)
        je "What? Oh my God, I can't agree to that! What if people find out? I'd lose my job!"
        ra "You idiot! Why did you tell her your name? Now she's gone! Now you won't get any money at all and you can leave the clinic at once!"
        jump InseminationNOTDay05
    "Don't say a word":
        ra "I'll show you how to get the best out of that huge dick. By having a go on it myself for a while..."
        je "Don't make him cum, his sperm belongs to me!"
        ra "Don't worry Mrs Anonymous. I know how to control my pussy muscles to bring men to the edge and maintain them there..."
        jump Insemination03Day05

label Insemination03Day05:
scene insemination09 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Like that is a very good position. The sperm will be ejected directly into your womb..."
scene insemination09a with dissolve
$ renpy.pause(1.0, hard=True)
ra "Just place the apple-sized tip near your pussylips..."
scene insemination09b with dissolve
$ renpy.pause(1.0, hard=True)
ra "And push back really hard to get as many inches as possible in one swift go."
je "You didn't get all of it Nurse Racque, I can see several inches still sticking out."
ra "Yes indeed, but you need to take your breath first before really relaxing your vagina and letting it stretch to accomodate the massive girth of that giant cock before..."
scene insemination09c with dissolve
play sound "Sounds/womansigh.mp3"
$ renpy.pause(1.0, hard=True)
ra "Pushing back even harder! AAAH! Like so! See? I got all of it!"
je "Wow, where does it even go?"
ra "Don't ask silly questions, a woman's body is perfectly capable of taking 20 inches of cock. I just proved it, so the naysayers at f95zone.com are all wrong."
je "Doesn't it hurt a bit though? It looks extremely painful to be impaled that way..."
ra "Of course not, it's immensely pleasurable. So much so that I can't help myself but have a go on that horsedick for a while if you don't mind..."
play music "Sounds/nursefuck.mp3"
scene insemination09b with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09a with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09b with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09c with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09b with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09a with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09b with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09c with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09b with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09a with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09b with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09c with dissolve
$ renpy.pause(0.1, hard=True)
scene insemination09b
$ renpy.pause(0.3, hard=True)
scene insemination09a
$ renpy.pause(0.3, hard=True)
scene insemination09b
$ renpy.pause(0.3, hard=True)
scene insemination09c
$ renpy.pause(0.3, hard=True)
scene insemination09b
$ renpy.pause(0.3, hard=True)
scene insemination09a
$ renpy.pause(0.3, hard=True)
scene insemination09b
$ renpy.pause(0.3, hard=True)
scene insemination09c
$ renpy.pause(0.3, hard=True)
scene insemination09b
$ renpy.pause(0.3, hard=True)
scene insemination09c
$ renpy.pause(0.3, hard=True)
scene insemination09b
$ renpy.pause(0.3, hard=True)
scene insemination09c
$ renpy.pause(0.3, hard=True)
scene insemination09b
$ renpy.pause(0.3, hard=True)
scene insemination09c
$ renpy.pause(0.3, hard=True)
scene insemination09b
$ renpy.pause(0.3, hard=True)
scene insemination09c
$ renpy.pause(0.3, hard=True)
scene insemination09b
$ renpy.pause(0.3, hard=True)
scene insemination09c
$ renpy.pause(0.3, hard=True)
scene insemination09b
$ renpy.pause(0.3, hard=True)
scene insemination09c
$ renpy.pause(1.0, hard=True)
stop music
if (sophiafucked == True) and (achievement.has("bosom") == False):
    show achievement14:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement14
    $ achievement.grant("bosom")
$ nursefucked05 = True
$ extras += 1
ra "Ah, it's ssoo deep in me!"
je "Get off MY stud! You'll make him cum!"
scene insemination09 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Phew, that was a good workout. And the boy... I mean young man behind the wall didn't cum, see?"
scene insemination08 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Why don't you come closer and admire that  magnificient fuckstick that's about to drown your womb in thick virile semen Jennifer?"
je "It sure looks yummy... But just a taste then... I came here purely for fertility reasons, not to blow off cocks, that is reserved for my darling hubby."
ra "Of course, your marital vows are super-important (cough)..."
scene insemination10a with dissolve
$ renpy.pause(1.0, hard=True)
ra "Here, I'll hold it for you. Just taste the pre-cum and see what you think of it..."                                                            
je "O..Okay."
scene insemination10b with dissolve
play sound "Sounds/hallesuck01.mp3"
$ renpy.pause(1.0, hard=True)
ra "That's it... Now spread your lips and take that monstrous helmet in... Mmh, doesn't it taste wonderful Jennifer?"
scene insemination10c with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/gulp.mp3"
ra "Well done girl! You took it all! Only proficient cocksuckers can manage such a huge cockhead in their tiny mouths!"
scene insemination10a with dissolve
$ renpy.pause(1.0, hard=True)
je "This cock really looks familiar..."
ra "Never mind that, just bring the stud to the edge one more time..."
play sound "Sounds/hardsucking.mp3"
scene insemination10b
$ renpy.pause(0.3, hard=True)
scene insemination10c
$ renpy.pause(0.3, hard=True)
scene insemination10b
$ renpy.pause(0.3, hard=True)
scene insemination10c
$ renpy.pause(0.3, hard=True)
scene insemination10b
$ renpy.pause(0.3, hard=True)
scene insemination10c
$ renpy.pause(0.3, hard=True)
scene insemination10b
$ renpy.pause(0.3, hard=True)
scene insemination10c
$ renpy.pause(0.3, hard=True)
scene insemination10b
$ renpy.pause(0.3, hard=True)
scene insemination10c
$ renpy.pause(0.3, hard=True)
scene insemination10b
$ renpy.pause(0.3, hard=True)
scene insemination10c
$ renpy.pause(0.3, hard=True)
scene insemination10b
$ renpy.pause(0.3, hard=True)
scene insemination10c
$ renpy.pause(0.3, hard=True)
stop sound
je "(gargle) Ggg..."
scene insemination07
$ renpy.pause(1.0, hard=True)
p "(Damn...It's so good!)"
ra "Now, maybe you should test the girth in your pussy..."
je "...Okay... I'll try..."
p "(But I can't take a picture from behind this wall!)"
scene insemination10d
$ renpy.pause(0.3, hard=True)
scene insemination10e
$ renpy.pause(0.3, hard=True)
scene insemination10d
$ renpy.pause(0.3, hard=True)
scene insemination10e
$ renpy.pause(0.3, hard=True)
scene insemination10d
$ renpy.pause(0.3, hard=True)
scene insemination10e
$ renpy.pause(0.3, hard=True)
scene insemination10d
$ renpy.pause(0.3, hard=True)
scene insemination10e
$ renpy.pause(0.3, hard=True)
scene insemination10d
$ renpy.pause(0.3, hard=True)
scene insemination10e
$ renpy.pause(0.3, hard=True)
scene insemination10d
$ renpy.pause(0.3, hard=True)
scene insemination10e
$ renpy.pause(0.3, hard=True)
scene insemination10d
$ renpy.pause(0.3, hard=True)
scene insemination10e
$ renpy.pause(0.3, hard=True)
scene insemination07
$ renpy.pause(1.0, hard=True)
p "FUCK! THIS IS SO GOOD!!!"
je "What? I recognize this voice!"
ra "Well, you wanted a huge load of virile spunk, he's a stud who can deliver just that. Who cares he's a student of yours, no one will ever know."
je "But... It's so wrong!"
ra "I think you can come out now [name]: Show Jennifer your full muscled body to convince her, she's already horny as hell."
je "Well... Yes, actually, my pussy is soaking wet but.."
window hide
$ lust_points[10] +=2
$ score += 2
show lust02:
    xalign 0.2 yalign 0.8
    linear 1.0 yalign 0.6
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
scene insemination10g
$ renpy.pause(1.0, hard=True)
ra "Now look at him! You want a physically-superior baby? His seed will give you one Jennifer..."
menu:
    "Come on, I'll be gentle and I won't tell anyone, I promise!":
        je "You'd better... I can't let my husband know I sucked off a student..."
        window hide
        $ lust_points[10] +=2
        $ score += 2
        show lust02:
            xalign 0.2 yalign 0.8
            linear 1.0 yalign 0.6
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
        if (lust_points[10] >= 10):
            show epiclust:
                xalign 0.25 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            je "OK, fuck me [name]! Fill me with your nasty teenage cum, I don't care anymore, I'm too horny!"
            ra "That's my girl.."
            jump JenniferFuckChoiceDay05
        je "But I just can't... It's so wrong... I want out of this deal!"
        if (jenniferjosewin == True):
            p "You've already sucked one off, that douchebag José. But I'm more potent than him, you know it..."
            je "It's true that your... thing... is bigger than his..."
            window hide
            $ lust_points[10] +=1
            $ score += 1
            show lust01:
                xalign 0.2 yalign 0.8
                linear 1.0 yalign 0.6
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
            if (lust_points[10] >= 10):
                show epiclust:
                    xalign 0.25 yalign 0.2
                    zoom 0.5
                    linear 2.0 zoom 1.0
                play sound "Sounds/epiclust.mp3"
                je "OK, fuck me [name]! Fill me with your nasty teenage cum, I don't care anymore, I'm too horny!"
                ra "That's my girl.."
                jump JenniferFuckChoiceDay05
            je "But I just can't... It's so wrong... I want out of this deal!"
            ra "What a disappointment (sigh). But you're the customer..."
            ra "[name], tuck that monstrous rod back in your pants and leave, we'll call you again if we need you..."
            p "WHAT? Like that? Dismissed like a cheap he-whore? Pfff!"
            jump InseminationNOTDay05 
        ra "What a disappointment (sigh). But you're the customer..."
        ra "[name], tuck that monstrous rod back in your pants and leave, we'll call you again if we need you..."
        p "WHAT? Like that? Dismissed like a cheap he-whore? Pfff!"
        jump InseminationNOTDay05
    "What are you waiting for, my cock demands attention!":
        je "How insulting! I will not tolerate being treated with so much disregard!"
        ra "Don't talk to her like that, she's the customer and she's paying us tons of money for the procedure!"
        p "I thought she might like it. Like, you know, dominant male and all that..."
        ra "Well now, you can tuck that monstrous rod back in your pants and leave, we'll call you again if we need you..."
        p "WHAT? Like that? Dismissed like a cheap he-whore? Pfff!"
        window hide
        $ lust_points[10] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.2 yalign 0.6
            linear 1.0 yalign 0.8
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump InseminationNOTDay05
        
label JenniferFuckChoiceDay05:
scene insemination13 with dissolve
$ renpy.pause(1.0, hard=True)
je "Get on with it, I need your sweet cum!"
menu:
    "Get on your back, I'll drill you slowly to stretch your fuckhole!" if (jenniferpussy == False):
        je "Yes, I think that's in order. Since you're so big..."
        jump JenniferPussyDay05
    "Spread those legs, I'm gonna pound you from behind!" if (jenniferdoggy == False):
        je  "Of course, pummel me like a ragdoll [name]!"
        jump JenniferDoggyDay05
    "Yeah, OK, but I want your sweet arse!" if (jenniferanal == False):
        je "What? But you can't impregnate me that way!"
        p "It's to get my cock really hard and ready to explode in your other hole. Come on, you know you want it!"
        je "I definitely DON'T want it, but if it's for a good cause..."
        jump JenniferAnalDay05
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (jenniferpussy == True) and (jenniferdoggy == True) and (jenniferanal == True):
        je  "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump JenniferMovieDay05

label JenniferPussyDay05:
$ jenniferpussy = True
scene insemination11 with dissolve
$ renpy.pause(1.0, hard=True)
p "Nice and slow at first..."
window hide
play sound "Sounds/jennifer01.mp3"
$ renpy.pause(3.0, hard=True)
je  "You're so much bigger than my husband..."
scene insemination11b with dissolve
$ renpy.pause(1.0, hard=True)
p "And in it goes..."
je "Fuck! This teenage monstercock feels so good in my tight cunt!"
label JenniferPussyDay05b:
play sound "Sounds/jenniferpussy.mp3"
scene insemination11 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination11b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination11 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination11b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination11 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination11b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination11 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination11b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination11 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination11b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination11
$ renpy.pause(0.3, hard=True)
scene insemination11b
$ renpy.pause(0.3, hard=True)
scene insemination11
$ renpy.pause(0.3, hard=True)
scene insemination11b
$ renpy.pause(0.3, hard=True)
scene insemination11
$ renpy.pause(0.3, hard=True)
scene insemination11b
$ renpy.pause(0.3, hard=True)
scene insemination11
$ renpy.pause(0.3, hard=True)
scene insemination11b
$ renpy.pause(0.3, hard=True)
scene insemination11
$ renpy.pause(0.3, hard=True)
scene insemination11b
$ renpy.pause(0.3, hard=True)
scene insemination11
$ renpy.pause(0.3, hard=True)
scene insemination11b
$ renpy.pause(0.3, hard=True)
scene insemination11
$ renpy.pause(0.3, hard=True)
scene insemination11b
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump JenniferPussyDay05b
    "Move on":
        pass
je "Now I'm totally stretched out!"
ra "I can see that, your hole is gaping wide open Jennifer!"
p "Good, so we can move on to another position then..."
jump JenniferFuckChoiceDay05

label JenniferDoggyDay05:
$ jenniferdoggy = True
scene insemination12 with dissolve
play sound "Sounds/jennifer02.mp3"
$ renpy.pause(12.0, hard=True)
je "Oh God, oh God! I'm gonna take the biggest fattest cock I've ever seen! I'm dripping wet, shove it in [name] I beg you!"
p "Sure, Here I come, ten inches in one swift go!"
scene insemination12b with dissolve
$ renpy.pause(1.0, hard=True)
je "Damn it, you're so fucking deep!"
label JenniferDoggyDay05b:
scene insemination12 with dissolve
play music "Sounds/jenniferdoggy.mp3"
$ renpy.pause(0.3, hard=True)
scene insemination12b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination12b
$ renpy.pause(0.3, hard=True)
scene insemination12
$ renpy.pause(0.3, hard=True)
scene insemination12b
$ renpy.pause(0.3, hard=True)
scene insemination12
$ renpy.pause(0.3, hard=True)
scene insemination12b
$ renpy.pause(0.3, hard=True)
scene insemination12
$ renpy.pause(0.3, hard=True)
scene insemination12b
$ renpy.pause(0.3, hard=True)
scene insemination12
$ renpy.pause(0.3, hard=True)
scene insemination12b
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        jump JenniferDoggyDay05b
    "Move on":
        pass    
je "I feel like a hog on a spitfire!"
p "My dick sure took some heat, I'm red-hot and ready for more action!"
jump JenniferFuckChoiceDay05    

label JenniferAnalDay05:
$ jenniferanal = True
scene insemination18 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Show the naysayers that a woman is also perfectly capable of taking well over a foot of fat hosepipe up her backside [name]!"
je "What? No, please, show instead some restraint when you plunge that massive pole int....!"
scene insemination18b with dissolve
play sound "Sounds/jenniferanal01.mp3"
$ renpy.pause(1.0, hard=True)
je "... MEEEE! FUCK! AAAH!"
label JenniferAnalDay05b:
scene insemination18 with dissolve
play sound "Sounds/jenniferanal02.mp3"
$ renpy.pause(0.3, hard=True)
scene insemination18b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination18 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination18b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination18 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination18b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination18 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination18b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination18 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination18b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination18 with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination18b with dissolve
$ renpy.pause(0.3, hard=True)
scene insemination18
$ renpy.pause(0.3, hard=True)
scene insemination18b
$ renpy.pause(0.3, hard=True)
scene insemination18
$ renpy.pause(0.3, hard=True)
scene insemination18b
$ renpy.pause(0.3, hard=True)
scene insemination18
$ renpy.pause(0.3, hard=True)
scene insemination18b
$ renpy.pause(0.3, hard=True)
scene insemination18
$ renpy.pause(0.3, hard=True)
scene insemination18b
$ renpy.pause(0.3, hard=True)
scene insemination18
$ renpy.pause(0.3, hard=True)
scene insemination18b
$ renpy.pause(0.3, hard=True)
scene insemination18
$ renpy.pause(0.3, hard=True)
scene insemination18b
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump JenniferAnalDay05b
    "Move on":
        pass    
je "Thank God you didn't waste your virile spunk in that hole..."
p "I know where to aim... Let me show you." 
jump JenniferFuckChoiceDay05    

label JenniferMovieDay05:
scene insemination14 with dissolve
p "Ok, you want my sperm Jennifer? I want to hear you SAY IT!"
je "YES! Breed me [name], I want to have your baby!"
play music "Sounds/jenniferfuckslow.mp3"
show jenniferslowfuck
show faster
call screen jenniferslowfuckday05
screen jenniferslowfuckday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("JenniferFastFuckDay05")

label JenniferFastFuckDay05:
stop music
hide faster
play music "Sounds/jenniferfuckfast.mp3"
show jenniferfastfuck
show cum
call screen jenniferfastfuckday05
screen jenniferfastfuckday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("JenniferCumDay05")

label JenniferCumDay05:
hide jenniferfastfuck
hide jenniferslowfuck
stop music
scene inseminationcum01
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
je "YES! Give me your seed! Put a baby in me!"
p "I'm doing it, I'm filling you up!"
scene inseminationcum02 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
je "That's it, fill me up to the brim with your warm spunk! I can feel every massive pellet hitting my cervix! Fuck, you cum ssoo much more than my husband!"
play sound "Sounds/jennifercum.mp3" 
$ renpy.pause(8.0, hard=True)
je "I think you've cum enough inside of me , pull out and give some to nurse Racque, she's a hungry cumwhore!"
ra "I sure am, gimme, gimme, gimme please!"
scene insemination15 with dissolve
play sound "Sounds/cumming.mp3" 
$ renpy.pause(1.0, hard=True)
p "There you go, take those heavy shots nurse Racque!"
ra "Mmh, yes, it's shooting so powerfully out of that donkey-sized cum cannon!"
scene insemination16 with dissolve
$ renpy.pause(1.0, hard=True)
ra "I can't believe how much cum you produced once again... Probably over a quart even this time!"
p "I think I'm done ladies, I'm exhausted and my balls hurt like hell..."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
ra "I'd better go and collect all that virile spunk into a jar for Dr.Stains before it goes off... I'll leave you two lovebirds to it."
p "(Shit, I didn't have time to take a pic of her!)"
scene insemination20a with dissolve
$ renpy.pause(1.0, hard=True)
if (jenniferjosewin == False):
    $ jenniferwin = True
    p "(Jennifer looks so fulfilled and contented. The perfect time to take a picture of her at least and send it to José... I wonder what she's thinking about right now...)"
else:
    p "(Jennifer looks so fulfilled and contented. I wonder what she's thinking about right now...)"
scene insemination20b with dissolve
play sound "Sounds/dreaming.mp3"
$ renpy.pause(1.0, hard=True)
je "Can you feel the baby kicking inside me honey? He seems to be so vigorous already!"
scene insemination20c with dissolve
$ renpy.pause(1.0, hard=True)
je "Ooh, there he goes again, giving great big kicks with his tiny feet... So cute!"
$ jenniferfucked = True
$ hour += 1
$ backdoor += 1
if (tanyafucked == True) and (achievement.has("cuckmaker") == False):
    show achievement12:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement12
    $ achievement.grant("cuckmaker")

p "I should get cleaned up and leave this hall of utter depravity..."

scene clinic04 with dissolve
$ renpy.pause(1.0, hard=True)
dr "So, how did it go [name]? Did you give it to her good?"
p "I sure did doc, I sure did..."
scene clinic04b with dissolve
$ renpy.pause(1.0, hard=True)
dr "Tell me about it, how did her hole feel stretched around that giant log you're carrying?"
p "Err, I know it's offscreen, but it definitely looks like you're touching yourself doc..."
dr "Me? How preposterous! I'm just showing a keen interest in my clients' welfare is all..."
p "Right... Right... Well, I don't have all day, so ask that bimbo nurse of yours, she saw everything."
dr "Umpf... Here's your money. NURSE RACQUE? COME HERE DARLING, I WANT A FULL REPORT!"
$ money += 10
p "(What a weirdo, I'm out of here...)"
scene clinicentrance
$ renpy.pause(1.0, hard=True)
p "Where should I go?"
menu:
    "Go to the beach":
        jump Beach01Day05
    "Go to the Burbs":
        jump BurbsDay05
    
label InseminationNOTDay05:
$ inseminationfail05 = True
scene clinic04 with dissolve
$ renpy.pause(1.0, hard=True)
dr "So, how did it go [name]? Did you give it to her good?"
p "No, she bailed out, it's not fair..."
dr "In that case, I won't give you a penny, lousy stud! And get out of my clinic and only come back when you can perform!"
p "I COULD perform, she chickened out, it ain't my fault!"
dr "Whatever, I'm a busy man and time is money."
scene clinicentrance
$ renpy.pause(1.0, hard=True)
p "Where should I go?"
menu:
    "Go to the beach":
        jump Beach01Day05
    "Go to the Burbs":
        jump BurbsDay05    

label ClinicOutDay05:
scene clinicentrance
$ renpy.pause(1.0, hard=True)
p "Where should I go?"
menu:
    "Go to the beach":
        jump Beach01Day05
    "Go to the Burbs":
        jump BurbsDay05    

label DinnerDay05:
scene annapredinner with dissolve
$ renpy.pause(1.0, hard=True)
m "Ah, there you are! We're late! Go and quickly change your clothes , we've got to head for the Longrods as soon as possible!"
p "Sure mom, I'll be down in a sec!"
scene blackscreen with dissolve
$ renpy.pause(1.0, hard=True)
jump EveningAnna01Day05

label Beach01Day05:
$ seenbeach05 = True
stop music
play music "Sounds/oceanwaves.mp3"
scene beach with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah! Here's Tini-Wini-Bikini beach, as sunny as always... I should probably head for the beach bar first..."
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_69
    $ lustaddedB = 1
    call Challenger from _call_Challenger_70
    $ challengercalls += 2

label BeachBar01e:
$ beachbarseen05 = True
stop music
play music "Sounds/tropicalmusic.mp3"
scene beachbar01 with dissolve
$ renpy.pause(1.0, hard=True)
bb "Aloha, welcome to Tini-Wini-Bikini Beach bar! Again..."
label BeachBar02e:
scene beachbar01
menu:
    "Chat with her":
        jump ChatBeachBarDay05    
    "Leave":
        jump ExploreBeachDay05

label ChatBeachBarDay05:
if (discoveraudacious == False):
    scene beachbar03 with dissolve
    bb "Are you aware that our beach is sponsored by Audacious Bikinis? And that they have their headquarters right here on the island west of downtown?"
    p "No, I did not know that. Now I do know that."
    $ discoveraudacious = True
    show addedlocation:
        xalign 0.3 yalign 0.3
        linear 1.0 yalign 0.1
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide addedlocation 
if (lifeguarddiscovered == False):
    scene beachbar01 with dissolve
    bb "The Tini-Wini Beach Lifeguard Corps is recruiting. Preferably good swimmers. And muscular to boot, so they can more easily carry fat tourists."
    bb "Seeing how muscular you are, you might be interested? The lifeguard tower is just behind you..."
    p "Yeah, I sure am super-muscled. ALL OVER. I'm da man!"
    scene beachbar03 with dissolve
    bb "Too much information. Just too much information..."
    $ lifeguarddiscovered = True
    show addedlocation:
        xalign 0.3 yalign 0.3
        linear 1.0 yalign 0.1
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide addedlocation 
if (hour <= 18):
    p "What horny news will you tell me today to brighten up my day?"
    scene beachbar01 with dissolve
    bb "Well, you'll be happy to know that today is \"Topless Thursday\". Most girls take advantage of that to get rid of their tanlines."
    p "Ooh! Now that lifted my spirits up, as well as something else... Excuse me while I readjust my bulge."
    bb "I hope you do realize you're just a sick pervert, right?"
    p "Maybe... Pray tell me, where are the topless girls, I haven't seen any on my way here?"
    bb "Well, for your perverse information, they usually hang out by the beach pier..."
    p "Thank you, kind lady! I shall bid you farewell and go on my adventurous quest."    

label ExploreBeachDay05:
stop music
play music "Sounds/oceanwaves.mp3"
if (hour >= 19) and (discoverclinic == False):
    p "It's getting late, I should really take the bus and get home now."
    $ bushome = True
    jump BusBeachHomeDay05
if (hour >= 20) and (discoverclinic == True):
    p "It's getting late, I should really take the shortcut through the clinic to get home in time for dinner..."
    stop music
    scene clinicentrance with dissolve
    play music "Sounds/gardensound.mp3"
    $ renpy.pause(1.0, hard=True)   
    p "I wish I had discovered this shortcut earlier, it is really helpful in cutting my travel time between the burbs and the beach..."
    jump DinnerDay05

p "Hum... Where should I go?"
menu:
    "Go to the beach bar" if (beachbarseen05 == False):
        jump BeachBar01e
    "Walk along the beach" if (walkbeachseen05 == False):
        jump BeachWalkDay05
    "Go to Randy Beach" if (randybeachseen05 == False):
        jump RandyBeachDay05
    "Go to the lifeguard tower" if (lifeguarddiscovered == True) and (seenlifeguard05 == False):
        jump Lifeguard01Day05
    "Go to the address on the shady guy's card" if (discovercabin == True) and (maddysaved == False) and (maddysaved05 == False):
        jump Cabin01Day05
    "Head for the beach pier" if (hour <= 18) and (pierseen05 == False):
        jump PierDay05
    "Take the Bus to town" if (hour <= 18):
        $ bustown = True
        jump BusBeachTownDay05
    "Take the Bus back home" if (discoverclinic == False):
        $ bushome = True
        jump BusBeachHomeDay05
    "Take the shortcut back to the Burbs" if (discoverclinic == True):
        stop music
        scene clinicentrance with dissolve
        play music "Sounds/gardensound.mp3"
        $ renpy.pause(1.0, hard=True)   
        p "I wish I had discovered this shortcut earlier, it is really helpful in cutting my travel time between the burbs and the beach..."
        jump BurbsDay05

label BusBeachTownDay05:
scene beach with dissolve
$ renpy.pause(1.0, hard=True)   
p "Bye bye Tini-Wini-Bikini beach!"
p "Ah, here's the bus going to town..."
jump BusDriveDayb05

label BusBeachHomeDay05:
scene beach with dissolve
$ renpy.pause(1.0, hard=True)   
p "Bye bye Tini-Wini-Bikini beach!"
p "Ah, here's the bus going to the burbs..."
jump BusDriveDayb05

label BeachWalkDay05:
$ walkbeachseen05 = True    
if (boughthallebikini == True) and ((walkbeachseen == False) or (beachswimday03 == True)) and ((walkbeachseen04 == False) or (beachswimday04 == True)) and (hallefucked == False):
    jump HalleBeachDay05

else:
    scene beachempty with dissolve
    $ renpy.pause(1.0, hard=True)  
    if (beachswimday04 == False) and (beachswimday03 == False):
        "This secluded part of the beach is empty... I could always go for a swim I guess."
        menu:
            "Go for a swim" if (beachswimday05 == False) and (beachswimday04 == False) and (beachswimday03 == False):
                jump BeachSwimDay05
            "Don't go for a swim":
                jump ExploreBeachDay05
    "This secluded part of the beach is empty today. BORING!"
    jump ExploreBeachDay05

label PierDay05:
$ pierseen05 = True
scene pier01 with dissolve
$ renpy.pause(1.0, hard=True)
p "There's a few hot fit topless babes around here indeed, just like the beach bar lady told me. Nice."
scene pier02 with dissolve
$ renpy.pause(1.0, hard=True)
re "Yuck! What are you doing here? This place is supposed to be off-limits to men!"
menu:
    "Why? A place with boobies exposed for the world to see IS the perfect place for men to be!":
        re "What a pervert! I'm getting out of here, this place is no longer safe for us women!"
        p "(Pfff, what did I say wrong?)"
        jump Pier02Day05
    "Well, I'm just a boy, you have nothing to fear from me. I'm just here to learn about the bees and the boo-bees.":
        re "Umpf. I think that it is highly inappropriate. Your mother is the one who is supposed to teach you about that, not me!"
        p "She's doing it, she's doing it, don't worry..."
        re "Come Isabelle, we'll leave, I don't want to have anything to do with this!"
        p "(Pfff, what did I say wrong?)"
        jump Pier02Day05        
        
label Pier02Day05:
scene pier03 with dissolve
$ renpy.pause(1.0, hard=True)
p "I'd better be more discreet, I'm making them flee like... fleas."
scene pier04 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ho Ho Ho! What do we have here? Nikki and Chantelle sunbathing topless!"
menu:
    "Approach them quietly":
        jump NikkiChantellePier01
    "Call out Nikki's name":
        jump NikkiChantellePier02
    "Call out Chantelle's name":
        jump NikkiChantellePier03

label NikkiChantellePier01:
scene pier05 with dissolve
$ renpy.pause(1.0, hard=True)
p "(boobies... Boobies... BOOBIES!)"
scene pier06 with dissolve
$ renpy.pause(1.0, hard=True)
s "Oh, I should have known it was you. The only boy who can't keep his mouth shut when he's thinking."
ch "What was he saying exactly? \"Boobies\" repeatedly, if I recall correctly."
menu:
    "Err... It was just a song that was in my head.":
        ch "Right, it had nothing to do with Nikki and me being topless... I'm starting to think [name] is a serial liar... and pervert."
        window hide
        $ lust_points[2] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.8 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        s "Anyway, what do you want, apart from ogling our big tits [name]?"
        jump NikkiChantelleChoice
    "Well, your boobies are indeed so nice that they messed with my mind. It's a compliment really!":
        ch "I see... So you like what you see then naughty boy?"
        s "You really shouldn't encourage him. He's a total pervert..."
        if (sisshowerpeep == True):
            s "The other day, he even barged in on me taking a shower!"
            ch "What? That's gross!"
            window hide
            $ lust_points[2] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.8 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            s "Anyway, what do you want, apart from ogling our big tits [name]?"
            jump NikkiChantelleChoice

label NikkiChantelleChoice:
menu:
    "Chantelle, I was wondering if you were getting tanned for tomorrow's beauty pageant? I really think you should compete, I'd vote for you for sure!":
        ch "Hum, I don't know. Maybe. But it's nice of you to encourage me..."
        $ chantellecompete = True
        window hide
        $ lust_points[2] += 1
        $ score += 1
        show lust01:
            xalign 0.8 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01 
        p "Well, I hope you do. See you around tomorrow maybe Chantelle. Bye."
        ch "Goodbye [name]. Thanks for stopping by."
        s "Umpf..."
        jump ExploreBeachDay05
    "Chantelle, I was wondering if you wanted to accompany me to the downtown gym, I'm a member and I can invite you for free..." if (gymmember == True) and (invitedchantelle == False):
        ch "Ooh, that would be wonderful, thank you. I need to train, I'm feeling too fat lately."
        window hide
        $ lust_points[2] += 1
        $ score += 1
        show lust01:
            xalign 0.8 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01 
        $ invitedchantelle05 = True
        p "Well, I'll call you when I get there so you can join me then. See you around Chantelle!"
        ch "Goodbye [name]. Thanks for stopping by."
        s "Umpf..."
        jump ExploreBeachDay05
    "Not really. I was just coming by to say hi. I'll leave you two alone then.":
        ch "Yes, please don't disturb us again when we're sunbathing. Girls need to concentrate to get the perfect tan."
        p "Right... Of course."
        jump ExploreBeachDay05
    "Nikki, do we REALLY have to go to the Longrod's tonight? I can't stand that arsehole José...":
        s "Mom said we should and that YOU should behave. So stop complaining and be nice to him tonight, Okay?"
        if (chantellejosewin == True):
            ch "What do you have against José? He's been very nice lately..."
            window hide
            $ lust_points[2] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.8 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            p "I know why YOU would say that... I'll leave you too to work on your suntan then. See you tonight Nikki!"
            jump ExploreBeachDay05

label NikkiChantellePier02:
scene pier06 with dissolve
$ renpy.pause(1.0, hard=True)
s "Oh, it's you [name]. You almost scared me. I was wondering who might know me here..."
p "Just enjoying the beach, I was wandering around and I thought I had seen you so I called your name."
ch "And you didn't recognize me?"
window hide
$ lust_points[2] -= 1
$ score -= 1
show lustminus01:
    xalign 0.8 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/less.mp3"
$ renpy.pause(2, hard=True)
hide lustminus01 
p "Err... Of course I did Chantelle!"
ch "Because you didn't call MY name."
p "The dev didn't give me the option of calling both your names, it's not my fault!"
s "So, apart from coming by to say hi, do you have anything you wanted to talk about or can we go back to working on our tan?..."
jump NikkiChantelleChoice
  
label NikkiChantellePier03:
scene pier07 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Yes? Oh, it's you, [name]. What are you doing here?"
p "Just enjoying the beach, I was wandering around and I thought I had seen you so I called your name."
s "Umpf, and do you have anything interesting to talk about with Chantelle or you just wanted to see us topless?"
if (lust_points[17] <= 9):
    window hide
    $ lust_points[17] -= 1
    $ score - 1
    show lustminus01:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01        
menu:
    "Actually yes. Are you getting tanned for tomorrow's beauty pageant Chantelle? I really think you should compete, I'd vote for you for sure!":
        ch "Hum, I don't know. Maybe. But it's nice of you to encourage me..."
        $ chantellecompete = True
        window hide
        $ lust_points[2] += 1
        $ score += 1
        show lust01:
            xalign 0.8 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01 
        p "Well, I hope you do. See you around tomorrow maybe Chantelle. Bye."
        ch "Goodbye [name]. Thanks for stopping by."
        s "Umpf..."
        jump ExploreBeachDay05
    "Actually yes. I was wondering if you wanted to accompany me to the downtown gym, I'm a member and I can invite you for free..." if (gymmember == True):
        ch "Ooh, that would be wonderful, thank you. I need to train, I'm feeling too fat lately."
        $ invitedchantelle05 = True
        window hide
        $ lust_points[2] += 1
        $ score += 1
        show lust01:
            xalign 0.8 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01 
        p "Well, I'll call you when I get there so you can join me then. See you around Chantelle!"
        ch "Goodbye [name]. Thanks for stopping by."
        s "Umpf..."
        jump ExploreBeachDay05
    "Not really. I was just coming by to say hi. I'll leave you two alone then.":
        ch "Yes, please don't disturb us again when we're sunbathing. Girls need to concentrate to get the perfect tan."
        p "Right... Of course."
        jump ExploreBeachDay05

label BeachSwimDay05:
$ beachswimday05 = True
play music "Sounds/randybeachsound.mp3"
scene beachswim01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I can see some coral reefs below. Let's dive and have a look!"        
scene beachswim02 with dissolve
play music "Sounds/underwater.mp3"
$ renpy.pause(1.0, hard=True)
p "What the hell is that thing swimming towards me?"
jump Mermaid01Day05

label HalleBeachDay05:
$ walkbeachseen05 = True 
stop music
play music "Sounds/oceanwaves.mp3"
scene hallebeach01 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Oh, hello [name]! I looove this new bikini, look, it even has straps so I can undo them and sunbathe topless..."
p "Very sexy indeed..."
scene hallebeach02 with dissolve
$ renpy.pause(1.0, hard=True)
ha "I was thinking of testing it by going diving. The coral reefs around here are really beautiful. Fancy tagging along?"
menu:
    "Sure, sounds like great fun!":
        ha "Alright! Hope you can keep your breath for a very long time because once you're down there, you simply won't want to come back up to the surface, it's so beautiful!"
        p "Sure, I can hold on for like minutes, piece of cake for me, I'm DA MAN!"
        $ lust_points[9] +=1
        $ score += 1
        show lust01:
            xalign 0.15 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        ha "Ha ha, then let's go Mr DA MAN!"
        jump Underwater01bDay05
    "Why don't we spend some special time together sunbathing on the beach?":
        ha "This is boring! I thought you were the adventurous type of guy..."
        $ lust_points[9] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        p "No, no, I'm adventurous. Where do we dive then?"
        jump Underwater01bDay05

label Underwater01bDay05:
scene hallebeach03 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Come on, this way! You'll see, it's gonna be ssoo much fun!"

label Underwater02Day05:
scene hallesea01 with dissolve
stop music
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
ha "Here's a good spot. Breathe in and...let's dive!"        
scene underwater01 with dissolve
play music "Sounds/underwater.mp3"
$ renpy.pause(1.0, hard=True)
p "Wow, this coral reef is amazing... And swimming with Halle is such a turn-on..."
menu:
    "Swim next to her":
        scene underwater02 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "She really seems to be enjoying herself... Me too..."
        p "Maybe time to make a move..."        
        scene underwater05 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Mmh, an underwater kiss...Kind of salty but I like it nevertheless..."
        $ lust_points[9] +=1
        $ score += 1
        show lust01:
            xalign 0.15 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        scene underwater03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "She's smiling at me...What next?..."
        scene underwater03b with dissolve
        p "What's wrong, she seems to be scared of something..."
        scene underwater04 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "She's darting off... OMG, what the fuck is that?..."
        jump Mermaid01Day05
    "Sneak under her":
        scene underwater03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Bingo, she's smiling at me... I wonder what a kiss underwater feels like..."
        scene underwater03b with dissolve
        p "What's wrong, she seems to be scared of something..."
        scene underwater04 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "She's darting off... OMG, what the fuck is that?..."
        jump Mermaid01Day05

label Mermaid01Day05:
scene mermaid01 with dissolve
$ renpy.pause(1.0, hard=True)
p "This mermaid is captivating... OK, she has a fish tail and all that but... Mmmh, those tits..."
scene mermaid02 with dissolve
$ renpy.pause(1.0, hard=True)
p "She seems to be signalling me to follow her..."
menu:
    "Follow her":
        jump Mermaid02Day05
    "Get the hell out of here and re-join Halle" if (beachswimday05 == False):
        $ underwaterleft = True
        jump Underwater03Day05
    "Get the hell out of here" if (beachswimday05 == True):
        scene beachswim01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Phew, that was close!I'm still shaking. Better go back to the beach..." 
        scene beachempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ExploreBeachDay05

label Mermaid02Day05:
scene mermaid03 with dissolve
$ renpy.pause(1.0, hard=True)
p "She's taking me to a giant clam... Is this where she lives?..."
scene mermaid05 with dissolve
$ renpy.pause(1.0, hard=True)
p "Now what?... Since we can't speak, it's hard to tell what she wants from me."
scene mermaid05 with dissolve
$ renpy.pause(1.0, hard=True)
p "Wow, lady, come on, a bit of courtship never hurts... Although it's clear what she wants now..."
scene mermaid06 with dissolve
$ renpy.pause(1.0, hard=True)
p "Wow, these mermaids are full-on... Hang on, I can feel some oxygen filling my lungs... Now I understand why she kissed me."
scene mermaid07 with dissolve
$ renpy.pause(1.0, hard=True)
p "Don't tell me she's pointing at her fuckhole..."
menu:
    "A hole is a hole, let's fuck!":
        jump Mermaid03Day05
    "Get the hell out of here and re-join Halle" if (beachswimday05 == False):
        jump Underwater03Day05
    "Get the hell out of here" if (beachswimday05 == True):
        scene beachswim01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Phew, that was close!I'm still shaking. Better go back to the beach..." 
        scene beachempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ExploreBeachDay05
        
label Mermaid03Day05:
scene mermaid08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Here we go, it's tough to aim underwater but once I'm in, it shouldn't move too much..."
show mermaidfuckslow
show faster
call screen mermaidfuckslowday05
screen mermaidfuckslowday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MermaidFuckFastday05")
label MermaidFuckFastday05:
hide faster
show mermaidfuckfast
show cum
call screen mermaidfuckfastday05
screen mermaidfuckfastday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MermaidFuckCumday05")
label MermaidFuckCumday05:
hide mermaidfuckfast
hide mermaidfuckslow
scene mermaid09
$ renpy.pause(1.0, hard=True)
p "Damn, I'm really filling her up with my cum...! But now I'm feeling dizzy and running out of air..."
scene mermaid10 with dissolve
$ renpy.pause(1.0, hard=True)
p "She's thanking me with a kiss... I can feel some oxygen filling my lungs... Phew, this kiss might have saved my life."
scene mermaid11 with dissolve
$ renpy.pause(1.0, hard=True)
p "She's offering me something. Looks like some old coin. Wow, thank you little mermaid!"
$ goldcoin = True
show goldcoin
show square
play sound "Sounds/found.mp3"
"You acquired an ancient gold coin."
hide goldcoin
hide square
p "I'd better get back to the surface before I run out of air again..."
scene mermaid12 with dissolve
$ renpy.pause(1.0, hard=True)
p "Shame I couldn't take a picture with my phone and send it to José... Then again, it might be best that way since this was bordering on bestiality..."
if mermaidfuck == False:
    $ extras += 1
$ mermaidfuck = True
if (beachswimday05 == False):
    jump Underwater03Day05
if (beachswimday05 == True):
    scene beachswim01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "The sea is getting rough. I'd better go back to the beach..." 
    scene beachempty with dissolve
    $ renpy.pause(1.0, hard=True)
    jump ExploreBeachDay05

label Underwater03Day05:
stop music
play music "Sounds/randybeachsound.mp3"
scene hallesea02 with dissolve
$ renpy.pause(1.0, hard=True)
if (mermaidfuck == True):
    ha "What took you so long? I was scared you drowned or got eaten by that repulsive creature! They are supposed to be evil you know?"
else:
    ha "Did you see that thing? I thought they didn't exist, that was scary. They are supposed to be evil you know?"
menu:
    "Evil? Come on, it's just a fish with nice big tits.":
        if (mermaidfuck == True):
            scene hallesea03 with dissolve
            $ renpy.pause(1.0, hard=True)
            ha "Somehow, I have the feeling you spent a lot of time with her... How can you prefer a repulsive creature to me?"
            $ lust_points[9] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.7 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01  
            ha "Let's get back to the beach, the sea is getting rough..."
            p "Great idea..."
            jump HalleBackBeach01Day05
        else:
            scene hallesea04 with dissolve
            $ renpy.pause(1.0, hard=True)
            ha "Ha ha! You boys really are all the same... A pair of tits, that's all that counts!"
            ha "Let's get back to the beach, the sea is getting rough..."
            p "Great idea..."
            jump HalleBackBeach01Day05
    "Yeah, that's why I came straight after you, to protect you..." if (underwaterleft == True):
        scene hallesea04 with dissolve
        $ renpy.pause(1.0, hard=True)
        ha "You're so sweet... So young and yet so...bold and confident..."
        $ lust_points[9] +=1
        $ score += 1
        show lust01:
            xalign 0.7 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        ha "Let's get back to the beach, the sea is getting rough..."
        p "Great idea..."
        jump HalleBackBeach01Day05        
    "We should report this amazing discovery to the police, we might become famous...":
        scene hallesea03 with dissolve
        $ renpy.pause(1.0, hard=True)
        ha "Hum... No, I'd rather not get in touch with the pi.., I mean cops... Let's forget about all that..."
        $ lust_points[9] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        p "Ah...Okay, sorry for suggesting that..."        
        ha "Let's get back to the beach, the sea is getting rough..."
        p "Great idea..."
        jump HalleBackBeach01Day05
        
label HalleBackBeach01Day05:
stop music
play music "Sounds/oceanwaves.mp3"
scene hallebeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Well, that was fun, apart from this vile creature... I think I'd better head back to the university, I need to study."
menu:
    "Okay, I hope to see you again Halle...":
        ha "You will, don't worry... If you come back to the beach, I'll be here..."
        jump ExploreBeachDay05
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True) and (lust_points[9] >=8):
        jump HallePendulumDay05
    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[9] >=8):
        play sound "Sounds/spray.mp3"
        $ renpy.pause(1.0, hard=True)
        ha "Why did you spray yourself with perfume? I can't smell a thing with that sea breeze silly! You're so cute..."
        p "(Ah, shit, didn't think of that...)"
        show pheromone
        show square
        play sound "Sounds/lost.mp3"
        "You lost a pheromone spray."
        hide square
        hide pheromone
        $ pheromone = False
        p "Err, okay, I hope to see you again Halle..."
        ha "You will, don't worry..."
        jump ExploreBeachDay05

label HallePendulumDay05:
scene hallebeachhypno with dissolve
show pendulum03
$ renpy.pause(1.0, hard=True)
p "Just watch this pendulum as I wiggle it in front of your eyes Halle..."
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
if (lust_points[9] ==8):
    window hide
    $ lust_points[9] += 2
    $ score += 2
    show lust02:
        xalign 0.25 yalign 0.5
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
    jump HalleFuckDay05
if (lust_points[9] ==9):
    window hide
    $ lust_points[9] += 1
    $ score += 1
    show lust01:
        xalign 0.25 yalign 0.5
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
    jump HalleFuckDay05   

label HalleFuckDay05:
scene hallebeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "I think I changed my mind... I would rather spend some \"quality\" time with you after all..."
ha "And by \"quality\", I mean some hot, steamy SEX!"
p "Alright, I'm in baby!"
label HalleFuckDay05b:
ha "I hope that MASSIVE bulge of yours hides a MASSIVE cunt-splitter, because I need to be stretched WIDE and GOOD!"
p "Well, why don't you find out for yourself..."
ha "Mmmh, I can't wait to see it... Get out of these swimtrunks NOW!"
scene hallesuck01 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Oh fuck [name], it's so fucking BIG! And that precum of yours is so tasty!"
p "Drink as much as you like, there's an endless supply of it in my sperm factories..."
ha "God, you're so manly and confident, I love it! Fucking RAPE my mouth with your giant cock!"
scene hallesuck02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Well, since you ask so politely... First, a good stretching exercise..."
play sound "Sounds/hallesuck01.mp3"
ha "Gllur---mmmm!"
p "And then..."
scene hallesuck03 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/hallesuck02.mp3"
p "The main course! RHHAAA, Open that throat if you want to take it!"
play sound "Sounds/hallesuck02.mp3"
$ renpy.pause(3.0, hard=True)
p "Yeah... That's a good girl... You said you could hold your breath for a very long time, now prove it, AAHHH!"
play sound "Sounds/hallesuck02.mp3"
$ renpy.pause(3.0, hard=True)
scene hallesuck04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "(cough)... Wow, I've never been throat-fucked that hard... (sputter)...before in my life!"
ha "Let's get behind those rocks, I want to feel that monster up my pussy!"
scene hallefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Oh you're making me so damn horny! I can't stand it, I NEED that giant teenage cock NOW!"
scene hallefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
ha "AAH, AAAH, you're pounding me so hard! And you're so strong, fuck me harder!"
scene hallefuck03 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Now be careful with that monster... My pussy has never taken something that big inside..."
scene hallefuck04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "AAAH, be more gentle, your cock is the size of a tree trunk!"
label HallePrefuckDay05:
play sound "Sounds/halleprefuck.mp3"
scene hallefuck05 with dissolve
$ renpy.pause(0.3, hard=True)
scene hallefuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene hallefuck05 with dissolve
$ renpy.pause(0.3, hard=True)
scene hallefuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene hallefuck05 with dissolve
$ renpy.pause(0.3, hard=True)
scene hallefuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene hallefuck05
$ renpy.pause(0.5, hard=True)
scene hallefuck04
$ renpy.pause(0.5, hard=True)
scene hallefuck05
$ renpy.pause(0.5, hard=True)
scene hallefuck04
$ renpy.pause(0.5, hard=True)
scene hallefuck05
$ renpy.pause(0.4, hard=True)
scene hallefuck04
$ renpy.pause(0.5, hard=True)
scene hallefuck05
$ renpy.pause(0.5, hard=True)
scene hallefuck04
$ renpy.pause(0.5, hard=True)
scene hallefuck05
$ renpy.pause(0.5, hard=True)
scene hallefuck04
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        jump HallePrefuckDay05
    "Spread her legs and fuck her pussy slowly":
        ha "You want to fuck me some more stud? Yeah, I 'm ready for your great big horsecock, come and ram that monstercock home!"
        jump HalleFuckMovieDay05

label HalleFuckMovieDay05:
stop music
play sound "Sounds/oceanwaves.mp3"
play music "Sounds/hallefuckslow.mp3"
show hallefuckslow
show faster
call screen hallefuckslowday05
screen hallefuckslowday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("HalleFuckFastday05")
label HalleFuckFastday05:
hide faster
play music "Sounds/hallefuckfast.mp3"
show hallefuckfast
show cum
call screen hallefuckfastday05
screen hallefuckfastday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("HalleFuckCumday05")

label HalleFuckCumday05:
hide hallefuckfast
hide hallefuckslow
stop sound
stop music
play music "Sounds/oceanwaves.mp3"
scene hallefuckcum01
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "OOOH, I'm cumming....AAAH"
ha "Wow, that's what I call a fucking GEYSER of cum! Keep spewing [name], show me what a superstud you are!"
scene hallefuckcum02 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
ha "Damn, you're filling me up to bursting point, pull it out, pull it out!"
scene hallefuckcum03 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
ha "Mmmh, yeah, cover my big titties with your splooge... Sssoo, so much of it!"
p "That's it Halle, your amazing pussy totally drained me... Phew!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
ha "Well you did REAL good [name]... Now I have to go back into the ocean to clean myself of the tons of cum you've covered me with!"
ha "Don't wait for me, I'll be a WHILE cos you came SSSOOO MUCH!"
p "See you Halle, thanks for that hot steamy sex!"
$ hour += 1
$ hallefucked = True
if (hallejosewin == False):
    p "(She didn't notice I took a picture of us... Now I'll send it to José)."
    $ hallewin = True
if (tanyafucked == True) and (achievement.has("colonizer") == False):
    show achievement05:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement05
    $ achievement.grant("colonizer")
if (sandyfucked == True) and (achievement.has("student") == False):
    show achievement06:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement06
    $ achievement.grant("student")
    
jump ExploreBeachDay05

label Lifeguard01Day05:
stop music
scene tower01 with dissolve
$ renpy.pause(1.0, hard=True)

if (hour == 16) and (workedseconddaylifeguard == True):
    pa "Oh, hi there [name]: I'm afraid the beach is quite empty today for some reason..."
    pa "We won't be needing your lifesaving skills, I need to watch my budget. It mainly goes into alcohol too!"
    p "What? But I'm HERE, ready to save lives! That's so unfair..."
    pa "You're so cute when you're sad..."
    window hide
    $ lust_points[18] += 1
    $ score += 1
    show lust01:
        xalign 0.5 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    $ seenlifeguard05 = True
    jump ExploreBeachDay05
    

if (hour == 16) and (wonarmwrestling == True):
    pa "Hi again [name]. So, you wanna start working today?"
    menu:
        "Sure, I'm in!":
            jump LifeGuardWorkDay05
        "Maybe another day...":
            pa "Fine, your choice, hope to see you back here at 4pm another day..."
            jump ExploreBeachDay05
if (hour >=17) and (wonarmwrestling == True):
    pa "It's a bit late to start a workshift. We're almost done here. Come back tomorrow at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay05
if (hour <=15) and (wonarmwrestling == True):
    pa "It's a bit early to start a workshift. Come back at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay05

mb "What do you want kid? You lost your mommy?"
pa "Ha ha, nice one Mitch!"
p "Is making fun of people part of your job?"
pa "Calm down boy, it was just in jest... I'm Pamela, the head lifeguard, this dufus is Mitch, how may we help you?"
p "I'd like to become a lifeguard, I'm strong and I can swim well."
scene tower02 with dissolve
$ renpy.pause(1.0, hard=True)
mb "Ooh! Is that so? Look Pam, David Hasselhof! Ha ha!"
p "(I'm really starting to dislike this jerk...)"
pa "Well, we could use some additional help at peak time, between 4pm and 6pm, but how can I be sure you're really as good as you claim?"
scene tower03 with dissolve
$ renpy.pause(1.0, hard=True)
mb "Tell you what kid, you beat me at arm wrestling, and then you can become a lifeguard. I beat you, you get the hell out of my sight!"
menu:
    "Deal!":
        scene tower04 with dissolve
        $ renpy.pause(1.0, hard=True)
        mb "Get ready to feel the PAIN! No one can beat Mitch Bigcannon's huge muscles, right Pam?"
        pa "I've never seen you lose Mitch, but we'll see... This boy is... very muscular."
        $ lust_points[18] += 1
        $ score += 1
        show lust01:
            xalign 0.5 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump ArmWrestlingDay05

    "This guy looks too strong, bail out":
        p "Err... Maybe another time... I need to...train."
        scene tower05 with dissolve
        $ renpy.pause(1.0, hard=True)
        mb "Oooooh! Little boy scared... Once again, Mitch Bigcannon is the winner! Choo-chooo!"
        $ lifeguardbail = True
        jump ExploreBeachDay05


label ArmWrestlingDay05:
$ clicked = True
$ points=20
if (strength <= 7):
    jump WrestlingStrength07Day05
if (strength == 8):
    jump WrestlingStrength08Day05
if (strength >= 9):
    jump WrestlingStrength09Day05

label WrestlingStrength07Day05:
$ plus=0
$ max_point=40
scene arm01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Ready guys? On your marks...set.. and go!"
play music "Sounds/grunt.mp3"
scene arm01b with dissolve
centered "Click on the hand!{w=1}{nw}"
call screen clicker7day05
screen clicker7day05:
    modal True
    timer .2 repeat True action [If(points <= 0, true=Jump("LostwrestlingDay05"), false=SetVariable("points", points - 1))]
    button:
        xpos .35
        ypos .3
        xysize(200, 200)
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("WonwrestlingDay05"), false=SetVariable("points", points + plus))]
    bar value StaticValue(points, max_point):
        xalign 0.45 yalign 0.0
        xmaximum 400 
        ymaximum 15

label WrestlingStrength08Day05:
$ plus=1
$ max_point=40
scene arm01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Ready guys? On your marks...set.. and go!"
play music "Sounds/grunt.mp3"
scene arm01b with dissolve
centered "Click on the hand!{w=1}{nw}"
call screen clicker8day05
screen clicker8day05:
    modal True
    timer .3 repeat True action [If(points <= 0, true=Jump("LostwrestlingDay05"), false=SetVariable("points", points - plus))]
    button:
        xpos .35
        ypos .3
        xysize(200, 200)
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("WonwrestlingDay05"), false=SetVariable("points", points + plus))]
    bar value StaticValue(points, max_point):
        xalign 0.45 yalign 0.0
        xmaximum 400 
        ymaximum 15

label WrestlingStrength09Day05:
$ plus=2
$ max_point=40
scene arm01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Ready guys? On your marks...set.. and go!"
play music "Sounds/grunt.mp3"
scene arm01b with dissolve
centered "Click on the hand!{w=1}{nw}"
call screen clicker9day05
screen clicker9day05:
    modal True
    timer .5 repeat True action [If(points <= 0, true=Jump("LostwrestlingDay05"), false=SetVariable("points", points - plus))]
    button:
        xpos .35
        ypos .3
        xysize(200, 200)
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("WonwrestlingDay05"), false=SetVariable("points", points + plus))]
    bar value StaticValue(points, max_point):
        xalign 0.45 yalign 0.0
        xmaximum 400 
        ymaximum 15

label LostwrestlingDay05:
stop music
play music "Sounds/oceanwaves.mp3"
play sound "Sounds/thump.mp3"
scene armlost with dissolve
$ renpy.pause(1.0, hard=True)
mb "Once again, Mitch Bigcannon is the winner!"
scene tower05 with dissolve
$ renpy.pause(1.0, hard=True)
mb "Nobody can beat the ultimate arm wrestling champion Mitch Bigcannon! Choo-choo!"

p "How humiliating... I'd better train to get stronger if I want to beat that jerk..."
$ lust_points[18] -= 1
$ score -= 1
show lustminus01:
    xalign 0.5 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/less.mp3"
$ renpy.pause(2, hard=True)
hide lustminus01
jump ExploreBeachDay05

label WonwrestlingDay05:
stop music
play music "Sounds/oceanwaves.mp3"
play sound "Sounds/thump.mp3"
scene armwon with dissolve
$ renpy.pause(1.0, hard=True)
p "I win JERK! I'm da man, I'm DA MAN!"
scene tower06 with dissolve
$ renpy.pause(1.0, hard=True)
if  (strength >=11):
    mb "Pam, don't listen to him, I'm sure he cheated! It was way too easy for him..."
    pa "Did you use the console [name]?"
    p "The what? Na, I would never cheat at a ren'py porn game, that's preposterous!"
    mb "Yes he did! I'm certain of it! he's a CHEAT, kick him out of the game, Pam!"
    pa "I'm afraid you leave me no choice.... Bye bye [name]..."
    return

mb "Pam, don't listen to him, I'm sure he cheated! Mitch Bigcannon CANNOT lose!"
pa "Give it up Mitch, this boy won fair and square..."
$ wonarmwrestling = True
$ lust_points[18] += 2
$ score += 2
show lust02:
    xalign 0.6 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
scene tower07 with dissolve
$ renpy.pause(1.0, hard=True)
pa "What's your name?"
p "[name] Johnson. So, when can I start working as a lifeguard then?"
pa "Such eagerness! At 4pm, that's peak time for beachgoers. And we need you for two hours, pay is 10 dollars an hour."
if (hour == 16):
    pa "And as it turns out, it's 4pm. So, you wanna start working today?"
    menu:
        "Sure, I'm in!":
            jump LifeGuardWorkDay05
        "Maybe another day...":
            pa "Fine, your choice, hope to see you back here at 4pm another day..."
            jump ExploreBeachDay05
if (hour >=17) and (wonarmwrestling == True):
    pa "It's a bit late to start a workshift. We're almost done here. Come back tomorrow at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay05
if (hour <=15) and (wonarmwrestling == True):
    pa "It's a bit early to start a workshift. Come back at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay05

label LifeGuardWorkDay05:
if (workedfirsdaylifeguard == True):
    jump LifeGuardSecondWorkDay05
$ workedfirsdaylifeguard = True
scene tower08 with dissolve
$ renpy.pause(1.0, hard=True)
pa "We have to take turns looking out for swimmers in distress. Mitch, get me a beer."
mb "Sure boss!"
menu:
    "You shouldn't be drinking on the job...":
        pa "Says who? Just a beer here and there, no big deal!"
        $ lust_points[18] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump LifeGuardWork02Day05
    "Oh yeah, I'll get one too!":
        pa "No you won't, you're too young. Your turn on the binoculars anyway."
        jump LifeGuardWork02Day05
    "None for me, I'm fully concentrated on the job.":
        pa "Nice, so I can drink my beer and not worry then..."
        $ lust_points[18] += 1
        $ score += 1
        show lust01:
            xalign 0.7 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump LifeGuardWork02Day05    

label LifeGuardWork02Day05:
$ hour +=1
scene tower09 with dissolve
$ renpy.pause(1.0, hard=True)
p "Err, I've spotted some swimmers who seem to be having trouble."
pa "Let me see!"
scene tower10 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Shit, they're caught in a rip current. We need to go and get them and coordinate. Tell me on the way which woman you will go for!"
menu:
    "The small girl on the left. (Lolly)":
        jump LifeguardSmall01Day05
    "The tall woman on the right. (Sandy)":
        jump LifeguardsBig01Day05


label LifeguardSmall01Day05:
$ savedlolly = True
scene pamelarun
play sound "Sounds/baywatch.mp3"
$ renpy.movie_cutscene("Day3/pamelarun.ogv")
scene pamelarun
stop sound
$ renpy.pause(1.0, hard=True)
p "Nope, I ain't running like that... Just nope."
scene tower11 with dissolve
stop music
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
lo "Help mister! (gl--glurb...)"
p "I'm coming, don't worry. (shit, these currents are strong...)"
scene towerlolly01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Phew, I managed to make it and get her out in time before she drowned..."
ma "Oh my God, my poor baby! Save her, please!"
scene towerlolly02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Don't worry, I'll perform CPR on her right away, I'm...err.. fully-qualified..."
ma "She's not breathing, she's gonna die!"
scene towerlolly03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Come on, wake up little girl!"
lo "(cough) (spurt)... Eew, mommy, this boy is feeling up my boobies!"
menu:
    "Oh come on now! What next, I go to jail again?" if (wenttojail == True):
        pa "Why are you saying that???"
        p "Err... No particular reason..."
        ma "Of course not, I'm ever so thankful to you for saving my little girl's life..."
        if (lust_points[15] <= 8):
            $ lust_points[15] += 1
            $ score += 1
            show lust01:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        if (lust_points[15] <= 7):
            $ lust_points[15] += 2
            $ score += 2
            show lust02:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust02
        if (lust_points[15] <= 6):
            $ lust_points[15] += 3
            $ score += 3
            show lust03:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust03
        pa "Yeah, you did good... I'm proud of you. I've reanimated the other woman and she's on her merry way now, so we can go back to the watch tower."
        $ lust_points[18] += 1
        $ score += 1
        show lust01:
            xalign 0.85 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump TowerEndDay05
    "Hey, I saved your life you ungrateful little bitch!":
        pa "Calm down [name], she's confused, she didn't mean it!"
        ma "But YOU meant it and you insulted my little girl. Thank you for NOTHING! Lolly, get up, we're leaving!"
        pa "Oh oh, seems like you pissed her off big time. But you did good on your CPR... I'm proud of you."
        $ lust_points[18] += 1
        $ score += 1
        show lust01:
            xalign 0.85 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        pa "I've reanimated the other woman and she's on her merry way now, so we can go back to the watch tower."
        jump TowerEndDay05
    "This is standard procedures for reanimating an unconscious swimmer.":
        pa "Wow, [name], you might be a new lifeguard but you did everything by the books, I'm so proud of you..."
        $ lust_points[18] += 2
        $ score += 2
        show lust02:
            xalign 0.85 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
        ma "I am ever so thankful to you for saving my little girl's life..."
        $ lust_points[15] += 3
        $ score += 3
        show lust03:
            xalign 0.2 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust03
        pa "I've reanimated the other woman and she's on her merry way now, so we can go back to the watch tower."
        jump TowerEndDay05

label LifeguardsBig01Day05:
$ savedsandy = True
scene pamelarun
play sound "Sounds/baywatch.mp3"
$ renpy.movie_cutscene("Day3/pamelarun.ogv")
scene pamelarun
stop sound
$ renpy.pause(1.0, hard=True)
p "Nope, I ain't running like that... Just nope."
scene tower11b with dissolve
stop music
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
p "Puff... (grunt) She's...too...heavy...with these currents... And I'm not strong enough...Pamela, help!"
pa "Maintain her head above the water, I'll come back once I'm done with this little girl..."
p "Shit... I should have picked her, looks much easier... But when you have a dick for a brain..."
$ stamina -= 1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
scene towersandy01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Quick, place her on the sand, I'll practice CPR on her straight away..."
menu: 
    "Hey, I want to practice mouth-to-m.. I mean CPR on her!":
        pa "I can't trust you, you weren't even capable of bringing her back by yourself!"
        $ lust_points[18] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.1 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
    "Sure boss, I'll put her down over there.":
        pass

scene towersandy02 with dissolve
$ renpy.pause(1.0, hard=True)
sa "(cough) (spurt)... Wh...what happened?"
menu:
    "You were drowning, I saved you Sandy...":
        scene towersandy03 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "Oooh, my Prince Charming... Thank you..."
        pa "Prince Charming hey? Well, your \"Prince Charming\" here couldn't save you on his own, he wasn't strong enough. And I practiced CPR, not him!"
        $ lust_points[18] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.5 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
        p "Come on, don't spoil the moment! I maintained her head above water, I saved her!"
        sa "I... kind of believe you, my Prince Charming..."
        $ lust_points[19] += 2
        $ score += 2
        show lust02:
            xalign 0.35 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
        p "How about we go some place quiet... Like Randy Beach?"
        pa "She's in no state for your shenanigans! She almost drowned, Mitch is arriving with the medics and you should leave them alone!"
        p "But... I know her, she's like... my Princess Charming..."
        pa "Oh, gimme a break and go back to the watch tower!"
        sa "(cough) I'll see you around my Prince Charming..."                
        jump TowerEndDay05
    "Don't say a word, let Pamela speak":
        pa "You were caught in a strong rip current ma'am. But thanks to the intervention of the trusted Tini-Wini-Bikini Beach Lifeguard Corps, you are now safe..."
        scene towersandy03 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "Oooh, thank you sssoo much... Both of you..."
        $ lust_points[19] += 1
        $ score += 1
        show lust01:
            xalign 0.35 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        p "How about we go some place quiet... Like Randy Beach?"
        pa "She's in no state for your shenanigans! She almost drowned, Mitch is arriving with the medics and you should leave them alone!"
        p "But... I know her, she's like... my Princess Charming..."
        pa "Oh, gimme a break and go back to the watch tower!"
        sa "(cough) I'll see you around my Pricne Charming..."                
        jump TowerEndDay05

label LifeGuardSecondWorkDay05:
$ workedseconddaylifeguard = True
scene tower08 with dissolve
$ renpy.pause(1.0, hard=True)
pa "We have to take turns looking out for swimmers in distress. Mitch, get me a beer."
mb "Sure boss!"
if (beercase == True):
    mb "Err, boss! There aren't any left!"
    pa "What? I was sure there was a full case left last night!... [name], did you steal our beer?"
    p "Me? Of course not, I resent this accusation, I would never do that!"
    pa "Ugh... I'm left with no beer to drink... That puts me in a foul mood!"
    $ lust_points[18] -= 1
    $ score -= 1
    show lustminus01:
        xalign 0.7 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    mb "I found one bottle in the emergency kit boss!"
    pa "Give it to me then, I don't care if it's still warm, I NEED TO DRINK!"
menu:
    "You shouldn't be drinking on the job...":
        pa "Says who? Just a beer here and there, no big deal!"
        $ lust_points[18] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump LifeGuardWorkSecond02Day05
    "Oh yeah, I'll get one too!":
        pa "No you won't, you're too young. Your turn on the binoculars anyway."
        jump LifeGuardWorkSecond02Day05
    "None for me, I'm fully concentrated on the job.":
        pa "Nice, so I can drink my beer and not worry then..."
        $ lust_points[18] += 1
        $ score += 1
        show lust01:
            xalign 0.7 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump LifeGuardWorkSecond02Day05

label LifeGuardWorkSecond02Day05:
$ hour +=1
scene tower09 with dissolve
$ renpy.pause(1.0, hard=True)
p "Err, I've spotted some swimmers who seem to be having trouble. Again."
pa "Let me see!"
if (savedlolly == True):
    scene tower10b with dissolve
if (savedsandy == True):
    scene tower10c with dissolve
$ renpy.pause(1.0, hard=True)
pa "Shit, they're caught in a rip current (again). We need to go and get them... Now let me guess. You're going for the girl, right?"
p "One chance out of two but yes, you are correct!"
pa "Umpf. Another fat slob for me it is then..."
if (savedsandy == True):
    jump SavedLollySecondDay05
if (savedlolly == True):
    jump SavedSandySecondDay05
    
label SavedLollySecondDay05:
$ savedlolly02 = True
scene pamelarun
play sound "Sounds/baywatch.mp3"
$ renpy.movie_cutscene("Day3/pamelarun.ogv")
scene pamelarun
stop sound
$ renpy.pause(1.0, hard=True)
p "Nope, I ain't running like that... Just nope."
scene tower11 with dissolve
stop music
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
lo "Help mister! (gl--glurb...)"
p "I'm coming, don't worry. (shit, these currents are strong...)"
scene towerlolly01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Phew, I managed to make it and get her out in time before she drowned..."
ma "Oh my God, my poor baby! Save her, please!"
scene towerlolly02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Don't worry, I'll perform CPR on her right away, I'm...err.. fully-qualified..."
ma "She's not breathing, she's gonna die!"
scene towerlolly03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Come on, wake up little girl!"
lo "(cough) (spurt)... Eew, mommy, this boy is feeling up my boobies!"
menu:
    "Oh come on now! What next, I go to jail again?" if (wenttojail == True):
        pa "Why are you saying that???"
        p "Err... No particular reason..."
        ma "Of course not, I'm ever so thankful to you for saving my little girl's life..."
        if (lust_points[15] <= 8):
            $ lust_points[15] += 1
            $ score += 1
            show lust01:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        if (lust_points[15] <= 7):
            $ lust_points[15] += 2
            $ score += 2
            show lust02:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust02
        if (lust_points[15] <= 6):
            $ lust_points[15] += 3
            $ score += 3
            show lust03:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust03
        pa "Yeah, you did good... I'm proud of you. I've reanimated the other woman and she's on her merry way now, so we can go back to the watch tower."
        $ lust_points[18] += 1
        $ score += 1
        show lust01:
            xalign 0.85 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump TowerEndDay05
    "Hey, I saved your life you ungrateful little bitch!":
        pa "Calm down [name], she's confused, she didn't mean it!"
        ma "But YOU meant it and you insulted my little girl. Thank you for NOTHING! Lolly, get up, we're leaving!"
        pa "Oh oh, seems like you pissed her off big time. But you did good on your CPR... I'm proud of you."
        $ lust_points[18] += 1
        $ score += 1
        show lust01:
            xalign 0.85 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        pa "I've reanimated the other woman and she's on her merry way now, so we can go back to the watch tower."
        jump TowerEndDay05
    "This is standard procedures for reanimating an unconscious swimmer.":
        pa "Wow, [name], you might be a new lifeguard but you did everything by the books, I'm so proud of you..."
        $ lust_points[18] += 2
        $ score += 2
        show lust02:
            xalign 0.85 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
        ma "I am ever so thankful to you for saving my little girl's life..."
        if (lust_points[15] <= 8):
            $ lust_points[15] += 1
            $ score += 1
            show lust01:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        if (lust_points[15] <= 7):
            $ lust_points[15] += 2
            $ score += 2
            show lust02:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust02
        if (lust_points[15] <= 6):
            $ lust_points[15] += 3
            $ score += 3
            show lust03:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust03
        pa "I've reanimated the fat slob and he's on his merry way now, so we can go back to the watch tower."
        jump TowerEndDay05

label SavedSandySecondDay05:
$ savedsandy02 = True
scene pamelarun
play sound "Sounds/baywatch.mp3"
$ renpy.movie_cutscene("Day3/pamelarun.ogv")
scene pamelarun
stop sound
$ renpy.pause(1.0, hard=True)
p "Nope, I ain't running like that... Just nope."
scene tower11b with dissolve
stop music
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
if (strength <= 8):
    jump SavedSandyLowStrength05
if (strength >= 9):
    jump SavedSandyHighStrength05

label SavedSandyLowStrength05:
p "Puff... (grunt) She's...too...heavy...with these currents... And I'm not strong enough...Pamela, help!"
pa "Maintain her head above the water, I'll come back once I'm done with this little girl..."
p "Shit... I should have picked her, looks much easier... But when you have a dick for a brain..."
$ stamina -= 1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
scene towersandy01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Quick, place her on the sand, I'll practice CPR on her straight away..."
menu: 
    "Hey, I want to practice mouth-to-m.. I mean CPR on her!":
        pa "I can't trust you, you weren't even capable of bringing her back by yourself!"
        $ lust_points[18] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.1 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
    "Sure boss, I'll put her down over there.":
        pass

scene towersandy02 with dissolve
$ renpy.pause(1.0, hard=True)
sa "(cough) (spurt)... Wh...what happened?"
menu:
    "You were drowning, I saved you Sandy...":
        scene towersandy03 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "Oooh, my Prince Charming... Thank you..."
        pa "Prince Charming hey? Well, your \"Prince Charming\" here couldn't save you on his own, he wasn't strong enough. And I practiced CPR, not him!"
        $ lust_points[18] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.5 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
        p "Come on, don't spoil the moment! I maintained her head above water, I saved her!"
        sa "I... kind of believe you, my Prince Charming..."
        if (lust_points[19] == 9):
            $ lust_points[19] += 1
            $ score += 1
            show lust01:
                xalign 0.35 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        if (lust_points[19] <= 8):                    
            $ lust_points[19] += 2
            $ score += 2
            show lust02:
                xalign 0.35 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust02        
        p "How about we go some place quiet... Like Randy Beach?"
        pa "She's in no state for your shenanigans! She almost drowned, Mitch is arriving with the medics and you should leave them alone!"
        p "But... I know her, she's like... my Princess Charming..."
        pa "Oh, gimme a break and go back to the watch tower!"
        sa "(cough) I'll see you around my Prince Charming..."                
        jump TowerEndDay05
    "Don't say a word, let Pamela speak":
        pa "You were caught in a strong rip current ma'am. But thanks to the intervention of the trusted Tini-Wini-Bikini Beach Lifeguard Corps, you are now safe..."
        scene towersandy03 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "Oooh, thank you sssoo much... Both of you..."
        $ lust_points[19] += 1
        $ score += 1
        show lust01:
            xalign 0.35 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        p "How about we go some place quiet... Like Randy Beach?"
        pa "She's in no state for your shenanigans! She almost drowned, Mitch is arriving with the medics and you should leave them alone!"
        p "But... I know her, she's like... my Princess Charming..."
        pa "Oh, gimme a break and go back to the watch tower!"
        sa "(cough) I'll see you around my Prince Charming..."                
        jump TowerEndDay05

label SavedSandyHighStrength05:
p "Puff... (grunt) She's...pretty...heavy... But I'm strong enough... I can do it, I'm DA MAN!"
scene towersandy01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Quick, place her on the sand, I'll practice CPR on her straight away..."
menu: 
    "Hey, I want to practice mouth-to-m.. I mean CPR on her!":
        pa "Alright, but you'd better do it properly!"
        scene sandycpr with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "I see, you're doing it the old-fashioned way. Mouth-to-mouth. What a surprise..."
        $ sandycpr = True        
    "Sure boss, I'll put her down over there.":
        pass

scene towersandy02 with dissolve
$ renpy.pause(1.0, hard=True)
sa "(cough) (spurt)... Wh...what happened?"
menu:
    "You were drowning, I saved you Sandy...":
        scene towersandy03 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "Oooh, my Prince Charming... Thank you..."
        if (sandycpr == False):
            pa "Prince Charming hey? Well, your \"Prince Charming\" here isn't the one who practiced the kiss of life, I performed the CPR, not him!"
            $ lust_points[18] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.5 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01        
            p "Come on, don't spoil the moment! I carried her back from the brink of death, I saved her!"
            sa "I... believe you, my Prince Charming..."
        if (lust_points[19] == 9):
            $ lust_points[19] += 1
            $ score += 1
            show lust01:
                xalign 0.35 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        if (lust_points[19] == 8):                    
            $ lust_points[19] += 2
            $ score += 2
            show lust02:
                xalign 0.35 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust02        
        if (lust_points[19] <= 7):                    
            $ lust_points[19] += 3
            $ score += 3
            show lust03:
                xalign 0.35 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust03
        if (lust_points[19] == 10):                    
            show epiclust:
                xalign 0.3 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust 
        p "How about we go some place quiet... my Princess Charming."
        sa "Yes, I know just the place...my Prince Charming."
        pa "Yuck, I think I'm gonna puke..."
        $ sandyfuckedlifeguard = True
        $ hour +=1
        jump SandyFuckDay05a     
    "Don't say a word, let Pamela speak":
        pa "You were caught in a strong rip current ma'am. But thanks to the intervention of the trusted Tini-Wini-Bikini Beach Lifeguard Corps, you are now safe..."
        pa "Our new recruit here carried you safely onto the beach..."
        scene towersandy03 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "Oooh, thank you sssoo much... Both of you..."
        if (lust_points[19] == 9):
            $ lust_points[19] += 1
            $ score += 1
            show lust01:
                xalign 0.35 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        if (lust_points[19] == 8):                    
            $ lust_points[19] += 2
            $ score += 2
            show lust02:
                xalign 0.35 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust02        
        if (lust_points[19] == 10):                    
            show epiclust:
                xalign 0.3 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust 
        p "How about we go some place quiet... my Princess Charming."
        sa "Yes, I know just the place...my Prince Charming."
        pa "Yuck, I think I'm gonna puke..."
        $ sandyfuckedlifeguard = True
        $ hour +=1
        jump SandyFuckDay05a

label SandyFuckDay05a:
stop music
play music "Sounds/oceanwaves.mp3"
scene sandybeach01b with dissolve
$ renpy.pause(1.0, hard=True)
sa "Oh, my Prince Charming, what a beautifully romantic place you found, far from the madding crowd!"
menu:
    "Yes, it's the perfect spot for us to get...more intimate..." if (lust_points[19] ==10):
        scene sandybeach02a with dissolve
        sa "And to get back to our natural human state without constraints by being naked...In total communion with Mother Nature."
        jump SandyFuckDay05
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True) and (lust_points[19] >=8) and (lust_points[19] <=9):
        jump SandyPendulumDay05
    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[19] >=8) and (lust_points[19] <=9):
        play sound "Sounds/spray.mp3"
        $ renpy.pause(1.0, hard=True)
        jump SandyPheromoneDay05
    "Leave, I don't have time for hanky-panky right now.":
        scene sandybeach02b with dissolve
        sa "What? Are you f*cking bl**dy kidding me???"
        p "Well, that's not very poetic language if I may say so..."
        p "(I should go back to Pamela, I haven't been paid yet...)"
        jump BeachPamela01Day05

label SandyPheromoneDay05:
scene sandybeach03b with dissolve
$ renpy.pause(1.0, hard=True)
sa "You are making sure you smell nice my Prince Charming? That is such a nice touch, even though I can't smell a thing with the sea breeze..."
show pheromone
show square
play sound "Sounds/lost.mp3"
"You used up your pheromone spray."
hide square
hide pheromone
$ pheromone = False
p "Yes, only the best for you my princess..."
if (lust_points[19] ==8):
    window hide
    $ lust_points[19] += 2
    $ score += 2
    show lust02:
        xalign 0.25 yalign 0.5
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
    sa "Let's get naked, I want to be in total communion with Mother Nature... And you!" 
    jump SandyFuckDay05
if (lust_points[19] ==9):
    window hide
    $ lust_points[19] += 1
    $ score += 1
    show lust01:
        xalign 0.25 yalign 0.5
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
    sa "Let's get naked, I want to be in total communion with Mother Nature... and you!"
    jump SandyFuckDay05   

label SandyPendulumDay05:
scene sandybeachhypnob with dissolve
show pendulum03
$ renpy.pause(1.0, hard=True)
p "Just watch this pendulum as I wiggle it in front of your eyes Sandy..."
sa "What is this? Are you trying to trick me by attempting to hypnotize me [name]...?"
window hide
$ lust_points[19] -= 2
$ score -= 2
show lustminus02:
    xalign 0.25 yalign 0.3
    linear 1.0 yalign 0.5
play sound "Sounds/less.mp3"
$ renpy.pause(2, hard=True)
hide lustminus02
sa "I've majored in social abuse science, you can't trick me... My prince Disappointing... I'm leaving."
scene beachempty with dissolve
$ renpy.pause(1.0, hard=True)
p "No, wait! I was just kidding... Ah, ah, it was just a joke... Sandy?"
jump ExploreBeachDay05

label SandyFuckDay05:
scene sandyfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
sa "First, my top, so you can admire my large, firm and TOTALLY NATURAL breasts."
p "Yep, entirely believable, especially in a 3D game."
scene sandyfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
sa "And then, the bottom, so you can admire my toned legs and firm buttocks..."
p "Your body is spectacular Sandy, you must really take good care of it..."
sa "Your turn lover, show me the humongous cock that will soon ravish my body..."
scene sandyfuck03 with dissolve
$ renpy.pause(1.0, hard=True)
sa "Yes, just as I remember it... Rock-hard and fully engorged with lust... Clearly in need of some luscious lips to love it and worship it..."
scene sandyfuck04 with dissolve
play sound "Sounds/sandysuck01.mp3"
$ renpy.pause(1.0, hard=True)
p "You can read its mind my Prin..."
scene sandyfuck04b with dissolve
play sound "Sounds/ryanmoan.mp3"
$ renpy.pause(3.0, hard=True)
p "AAAH...cess!"
label SandyBlowDay05:
play music "Sounds/hardsucking.mp3"
scene sandyfuck04c with dissolve
$ renpy.pause(0.3, hard=True)
scene sandyfuck04d with dissolve
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c with dissolve
$ renpy.pause(0.3, hard=True)
scene sandyfuck04b with dissolve
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c with dissolve
$ renpy.pause(0.3, hard=True)
scene sandyfuck04d with dissolve
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c with dissolve
$ renpy.pause(0.3, hard=True)
scene sandyfuck04b
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c
$ renpy.pause(0.3, hard=True)
scene sandyfuck04d
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c
$ renpy.pause(0.3, hard=True)
scene sandyfuck04b
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c
$ renpy.pause(0.3, hard=True)
scene sandyfuck04d
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c
$ renpy.pause(0.3, hard=True)
scene sandyfuck04b
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c
$ renpy.pause(0.3, hard=True)
scene sandyfuck04d
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c
$ renpy.pause(0.3, hard=True)
scene sandyfuck04b
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c
$ renpy.pause(0.3, hard=True)
scene sandyfuck04d
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c
$ renpy.pause(0.3, hard=True)
scene sandyfuck04b
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c
$ renpy.pause(0.3, hard=True)
scene sandyfuck04d
$ renpy.pause(0.3, hard=True)
scene sandyfuck04c
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        jump SandyBlowDay05
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay05

label SandyFuckChoiceDay05:
menu:
    "Spoon her from the side" if (sandyside == False):
        jump SandySideDay05
    "Stick your cock between her huge jugs" if (sandytits == False):
        jump SandyTitsDay05
    "Take her from behind like a bitch in heat" if (sandydoggy == False):
        jump SandyDoggyDay05
    "Watch her bounce up and down your giant crank" if (sandyside == True) and (sandytits == True) and (sandydoggy == True):
        jump SandyFinalDay05

label SandySideDay05:
$ sandyside = True
scene sandyside01 with dissolve
play sound "Sounds/sandyside01.mp3"
$ renpy.pause(4.0, hard=True)
sa "Oooh... You're so muscular. And that cock... It's so fucking big..."
p "It's not even half-way in yet..."
scene sandyside02 with dissolve
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
p "Now it is..."
label SandySideDay05b:
scene sandyside01 with dissolve
play sound "Sounds/sandyside02.mp3"
$ renpy.pause(0.5, hard=True)
scene sandyside02 with dissolve
$ renpy.pause(0.5, hard=True)
scene sandyside01 with dissolve
$ renpy.pause(0.5, hard=True)
scene sandyside02 with dissolve
$ renpy.pause(0.5, hard=True)
scene sandyside01 with dissolve
$ renpy.pause(0.5, hard=True)
scene sandyside02 with dissolve
$ renpy.pause(0.5, hard=True)
scene sandyside01 with dissolve
$ renpy.pause(0.5, hard=True)
scene sandyside02 with dissolve
$ renpy.pause(0.5, hard=True)
scene sandyside01 with dissolve
$ renpy.pause(0.2, hard=True)
scene sandyside02 with dissolve
$ renpy.pause(0.2, hard=True)
scene sandyside01 with dissolve
$ renpy.pause(0.2, hard=True)
scene sandyside02 with dissolve
$ renpy.pause(0.2, hard=True)
scene sandyside01 with dissolve
$ renpy.pause(0.2, hard=True)
scene sandyside02 with dissolve
$ renpy.pause(0.2, hard=True)
scene sandyside01 with dissolve
$ renpy.pause(0.2, hard=True)
scene sandyside02 with dissolve
$ renpy.pause(0.2, hard=True)
scene sandyside01 with dissolve
$ renpy.pause(0.2, hard=True)
scene sandyside02 with dissolve
$ renpy.pause(0.2, hard=True)
stop sound
menu:
    "Repeat":
        jump SandySideDay05b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay05

label SandyTitsDay05:
$ sandytits = True
scene sandytits01 with dissolve
play sound "Sounds/sandytitfuck01.mp3"
$ renpy.pause(2.0, hard=True)
sa "OOoh, my Prince Charming, my huge tits can't even bury that massive fuckstick, the head is sticking out..."
p "It will be sticking out way more once I do this..."
scene sandytits02 with dissolve
sa "It's so fucking big... Ssooo fucking big..."
label SandyTitsDay05b:
play sound "Sounds/sandytitfuck02.mp3"
scene sandytits01
$ renpy.pause(0.5, hard=True)
scene sandytits02
$ renpy.pause(0.5, hard=True)
scene sandytits01
$ renpy.pause(0.5, hard=True)
scene sandytits02
$ renpy.pause(0.5, hard=True)
scene sandytits01
$ renpy.pause(0.5, hard=True)
scene sandytits02
$ renpy.pause(0.5, hard=True)
scene sandytits01
$ renpy.pause(0.5, hard=True)
scene sandytits02
$ renpy.pause(0.5, hard=True)
scene sandytits01
$ renpy.pause(0.5, hard=True)
scene sandytits02
$ renpy.pause(0.5, hard=True)
scene sandytits01
$ renpy.pause(0.5, hard=True)
scene sandytits02
$ renpy.pause(0.5, hard=True)
scene sandytits01
$ renpy.pause(0.5, hard=True)
scene sandytits02
$ renpy.pause(0.5, hard=True)
scene sandytits01
$ renpy.pause(0.5, hard=True)
scene sandytits02
$ renpy.pause(0.5, hard=True)
stop sound
menu:
    "Repeat":
        jump SandyTitsDay05b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay05

label SandyDoggyDay05:
$ sandydoggy = True
scene sandydoggy01 with dissolve
$ renpy.pause(1.0, hard=True)
sa "My hole is all yours my Prince! Ram it in as deep as you like!"
p "Sure will do!"
scene sandydoggy01 with dissolve
play sound "Sounds/sandydoggy01.mp3"
$ renpy.pause(3.0, hard=True)
sa "AAAAH, it's so good feeling your giant teenage cock stretching my tiny fuckhole!"
label SandyDoggyDay05b:
play sound "Sounds/sandydoggy02.mp3"
scene sandydoggy01
$ renpy.pause(0.5, hard=True)
scene sandydoggy02
$ renpy.pause(0.5, hard=True)
scene sandydoggy01
$ renpy.pause(0.5, hard=True)
scene sandydoggy02
$ renpy.pause(0.5, hard=True)
scene sandydoggy01
$ renpy.pause(0.5, hard=True)
scene sandydoggy02
$ renpy.pause(0.5, hard=True)
scene sandydoggy01
$ renpy.pause(0.5, hard=True)
scene sandydoggy02
$ renpy.pause(0.5, hard=True)
scene sandydoggy01
$ renpy.pause(0.5, hard=True)
scene sandydoggy02
$ renpy.pause(0.5, hard=True)
scene sandydoggy01
$ renpy.pause(0.5, hard=True)
scene sandydoggy02
$ renpy.pause(0.5, hard=True)
scene sandydoggy01
$ renpy.pause(0.3, hard=True)
scene sandydoggy02
$ renpy.pause(0.3, hard=True)
scene sandydoggy01
$ renpy.pause(0.3, hard=True)
scene sandydoggy02
$ renpy.pause(0.3, hard=True)
scene sandydoggy01
$ renpy.pause(0.3, hard=True)
scene sandydoggy02
$ renpy.pause(0.3, hard=True)
scene sandydoggy01
$ renpy.pause(0.3, hard=True)
scene sandydoggy02
$ renpy.pause(0.3, hard=True)
scene sandydoggy01
$ renpy.pause(0.3, hard=True)
scene sandydoggy02
$ renpy.pause(0.3, hard=True)
scene sandydoggy01
$ renpy.pause(0.3, hard=True)
scene sandydoggy02
$ renpy.pause(0.3, hard=True)
scene sandydoggy01
$ renpy.pause(0.3, hard=True)
scene sandydoggy02
$ renpy.pause(0.3, hard=True)
stop sound
menu:
    "Repeat":
        jump SandyDoggyDay05b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay05

label SandyFinalDay05:
scene sandybeachkiss with dissolve
play sound "Sounds/sandyslut.mp3"
$ renpy.pause(3.0, hard=True)
sa "I'm going to bounce up and down your shaft and make you feel sssoo good my Prince... You'll pop in no time!"
stop music
play sound "Sounds/oceanwaves.mp3"
play music "Sounds/sandyfuckslow.mp3"
show sandyfuckslow
show faster
call screen sandyfuckslowday05
screen sandyfuckslowday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("SandyFuckFastday05")
label SandyFuckFastday05:
hide faster
play music "Sounds/sandyfuckfast.mp3"
show sandyfuckfast
show cum
call screen sandyfuckfastday05
screen sandyfuckfastday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("SandyFuckCumday05")

label SandyFuckCumday05:
hide sandyfuckslow
hide sandyfuckfast
stop music
play music "Sounds/oceanwaves.mp3"
scene sandycum01
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "FUUUCKK! Your bouncing arse is making me cum so HARD!"
sa "Yes, YES, I can feel it filling up my hole! SSSOO much cum for your Princess baby!"
sa "Damn, you're filling me up to bursting point, pull it out, pull it out!"
scene sandycum02 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
sa "Let me get hold of that cum-cannon! I want you to keep cumming like a stallion and cover my tits!"
scene sandycum03 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
sa "Mmmh, yeah, that's it, keep cumming and cover my big titties with your splooge... Sssoo, so much of it!"
p "You're making me cum buckets, AAAH!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
sa "Well you did REAL good [name]... Now I have to go back into the ocean to clean myself of the tons of cum you've covered me with!"
sa "Don't wait for me, I'll be a WHILE cos you came SSSOOO MUCH!"
p "See you Princess, I'll come back to... err... save you anytime!"
$ hour += 1
$ sandyfucked = True
if (sandyjosewin == False):
    p "(She didn't notice I took a picture of us... Now I'll send it to José)."
    $ sandywin = True
if (hallefucked == True) and (achievement.has("student") == False):
    show achievement06:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement06
    $ achievement.grant("student")    
jump ExploreBeachDay05

label TowerEndDay05:
scene tower01 with dissolve
stop music
play music "Sounds/oceanwaves.mp3"
$ renpy.pause(1.0, hard=True)
if (workedseconddaylifeguard == True):
    pa "Ok, you did well for your second day [name]. It's almost 6pm so I'll pay you now cos... we're heading for the beach bar."
if (workedseconddaylifeguard == False):
    pa "Ok, you did well for your first day [name]. It's almost 6pm so I'll pay you now cos... we're heading for the beach bar."
$ money += 20
pa "Use your remaining time to clean up this filthy place!"
scene towerend with dissolve
$ renpy.pause(1.0, hard=True)
p "More goddam cleaning to do..."
$ hour +=1
label TowerEndChoiceDay05:
menu: 
    "Snoop around the watch tower" if (beercase == False):
        $ beercase = True
        show beercase
        show square
        play sound "Sounds/found.mp3"
        "You find a case of beer."
        hide beercase
        hide square
        p "Cool, I found some booze..."
        jump TowerEndChoiceDay05        
    "Go and meet Pamela at the beach bar":
        jump BeachPamela01Day05  
    "Leave":
        jump ExploreBeachDay05       
        
label BeachPamela01Day05:
stop music
play music "Sounds/tropicalmusic.mp3"
scene beachbarpamela01 with dissolve
$ renpy.pause(1.0, hard=True)
if (workedseconddaylifeguard == True):
    mb "...And then, Pamela had to carry that old dude who weighs a ton, and she tripped...And the guy's cock was, like, hanging out..."
    pa "Shut up Mitch (hips)! You've already told this filthy story! Or was it another story (hips)?"
if (workedseconddaylifeguard == False):
    mb "...And then, the medics had to check her heart and I got to see her huge boobs, he he..."
    pa "Ha ha! You're such a (hips)... perv Mitch!"
if (sandyfuckedlifeguard == True):
    p "I don't want to bother you, but I wasn't actually paid today..."
    mb "Yeah, well you buggered off before the end of your shift you lazy sod, that's why!"
    pa "I'll give you (hips)... Ten bucks. Now you can buy me a drink, AH AH!"
    $ money += 10
    mb "Sssoo funny boss, HO HO HA HA!"
    p "What? Ten bucks? I was supposed to get paid 20 dollars! What a ripoff!"
menu:
    "Buy Pamela a non-alcoholic beverage (3$)":
        $ money -= 3
        scene beachbarpamela02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "Mmh, thanks [name]..."
        pa "Hang on a minute, what the fuck is that, there's no alcohol in it!"
        $ lust_points[18] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.1 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01 
        mb "Get out of here boy! This place is for drinking adults only, ha ha!"
        jump ExploreBeachDay05        
    "Buy Pamela an alcoholic beverage (6$)":
        $ money -= 6
        scene beachbarpamela02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "Mmh, thanks [name]... That's a lovely... (hips)... cocktail."
        $ lust_points[18] + 1
        $ score += 1
        show lust01:
            xalign 0.1 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01 
        pa "You can come back anytime to work for us..."
        jump ExploreBeachDay05        
    "Talk to Pamela about working some more as a lifeguard":
        scene beachbarpamela02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "Yeah, I guess we could use your help some more. You can come back anytime to work for us..."
        mb "Humpf..."
        jump ExploreBeachDay05
    
        
label RandyBeachDay05:
stop music
scene randybeach01 with dissolve
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
$ randybeachseen05 = True
if (randybeachseen == True) or (randybeachseen02 == True) or (randybeachseen03 == True) or (randybeachseen04 == True):
    p "Finally back here again. I'd better take my speedos off."
else:
    p "I guess that's it. I'd better take my speedos off."
window hide
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)

label RandyBeachDay05b:
p "I see three parasols but I can't see the people behind them...Which one should I go to?"
menu:
    "Go to the closest red parasol on the right" if (seenparasole01 == False):
        jump RandyBeachParasole01
    "Go to the middle orange parasol" if (seenparasole02 == False):
        jump RandyBeachParasole02
    "Go to the furthest red parasol on the left" if (seenparasole03== False):
        jump RandyBeachParasole03
    "Leave Randy Beach":
        if (seenparasole03 == True):
            $ hour += 1
        jump ExploreBeachDay05

label RandyBeachParasole01:
$ seenparasole01 = True
scene sweden01
show randybeachparasol01
$ renpy.pause(2.0, hard=True)
p "TWO pairs of legs... Now that's interesting..."
window hide
hide randybeachparasol01 with moveoutright
$ renpy.pause(1.0, hard=True)
p "Well, hello there girls, what are you doing on this beach?"
scene sweden02 with dissolve
$ renpy.pause(1.0, hard=True)
sw01 "We got told off for being tøpless on the other beach so my sister Hilde and I came here."
scene sweden03 with dissolve
sw02 "This beach is perfect, a nudist beach just like all beaches in Sweden!"
p "Oh, you're twins from Sweden hey? Interesting... (never fucked twins before...)"
scene sweden02 with dissolve
sw01 "Jå, we are here on holidays visiting the island, it's so sunny, not like Sweden..."
scene sweden03 with dissolve
sw02 "Vhere is the nearest Ikea?"
p "The nearest what? Listen, I could be your guide, I'll give you an \"in-depth\" tour of the island... (wink)"
scene sweden02 with dissolve
sw01 "Oh, thank you, but we already met someone who offered us a tour."
scene sweden03 with dissolve
sw02 "He said he vould make us eat some local meatballs. I love meatballs."
scene sweden02 with dissolve
sw02 "Do you like our tits? We can play with our bøøbies for you."
menu:
    "Err, yeah, I like them, I'd like to see that.":
        jump SwedenTitsDay05
    "You fucking European liberals make me sick. American Tits First!":
        sw02 "What a prude! Cøme Ingrid, ve will play with our titties somewhere else!"
        jump Parasol01eout
        
label SwedenTitsDay05:
scene sweden04 with dissolve
play sound "Sounds/sweden.mp3"
$ renpy.pause(3.0, hard=True)
$ peeping += 1
sw02 "Ooh, jå, Ingrid, suck on my big titties!"
sw01 "Mmh, they taste like sweet rollmøps Hilde!"
sw02 "My turn Ingrid. I love rubbing my bøøbies against yours!"
scene sweden05 with dissolve
play sound "Sounds/sweden.mp3"
$ renpy.pause(5.0, hard=True)
sw01 "Jå, Jå, JÅ!!! I think this boy likes it too, he has a big hardøn!"
p "Fuck yeah! I need to go to Sweden on holidays next year!"
sw02 "If you do, come and visit us, we will play with your monster boycøck!"
jump Parasol01eout

label Parasol01eout:
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeachDay05b

label RandyBeachParasole02:
$ seenparasole02 = True
scene randyoldcouple01
show randybeachparasol02
$ renpy.pause(2.0, hard=True)
p "I can't wait to see what's behind that parasol...Or maybe I could have, once I find out..."
window hide
hide randybeachparasol02 with moveoutleft
$ renpy.pause(1.0, hard=True)
p "By the holy Heavens, this scene is unbearable! My eyes hurt, MY EYES HURT!"
scene randyoldcouple02 with dissolve
$ renpy.pause(1.0, hard=True)
om "She's horny, I'm giving her what she wants since apparently, you're a wimp who keeps walking out on her..."
p "I'm walking out on her because she is repulsive! AAARGH! Run, run for your life!"
om "Pfff, I'm giving some of this game's viewers what they were clamoring for, unlike you..."
$ eyesore += 1
jump Parasol02eout

label Parasol02eout:
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
$ renpy.pause(1.0, hard=True)
jump RandyBeachDay05b
 
label RandyBeachParasole03:
$ seenparasole03 = True
scene randydoris01
show randybeachparasol03
$ renpy.pause(1.0, hard=True)
p "Mmh, what a weird foot position..."
window hide
hide randybeachparasol03 with moveoutright
$ renpy.pause(1.0, hard=True)
p "Oh, it's Doris! She's doing push-ups NAKED! Yummy..."
do "Ah, it's you... Good timing, I was about to finish my reps."
scene randydoris02 with dissolve
$ renpy.pause(1.0, hard=True)
do "Now for a few more stretching exercises... Get that cock hard and ready in the meantime boy!"
p "Err... OK, what's the plan?"
scene randydoris03 with dissolve
$ renpy.pause(1.0, hard=True)
do "The plan is more training for you to get you ready for Saturday's competition."
do "Now do some push-ups as an appetizer."
scene randydoris04 with dissolve
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
do "Of course, simple push-ups are too easy, so I'll push DOWN on your back while you do them..."
do "Good. Now, as part of your training... I want to test your cock strength!"
p "Wh.. what do you mean by that?"
do "I mean I'll attach some weights to it to see how much you can lift with that mighty love muscle..."
menu:
    "That's crazy, you'll break my cock, I'm outta here!":
        do "How do you expect to win the Muscle Stud competition if you are scared of lifting a few hundred pounds on your cock?"
        p "Well, that's a LOT! I don't want to break my schlong in half, my cock is my Master!"
        do "Pathetic! I can lift that much with my little finger! You're not up to my standards boy..."
        $ lust_points[6] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.8 yalign 0.3
            linear 1.0 yalign 0.5
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump Parasol03eout
    "Yeah, I'll show you, I'm da man, I'm DA MAN!":
        do "Good, I like your spirits! We'll start with an easy weight, just 100 pounds..."
        jump RandyCock01Day05

label RandyCock01Day05:
scene randydoris05 with dissolve
do "Now flex that mighty rock-hard dong and lift up the weight with it..."
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
scene randydoris06 with dissolve
play sound "Sounds/workoutgroan.mp3"
do "Now keep it flexed and hold it..."
if (strength <= 8):
    scene randydoris06b with dissolve
    p "Ah... Shit, can't hold it..."
    do "Well that was piss weak..."
    $ lust_points[6] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.8 yalign 0.3
        linear 1.0 yalign 0.5
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    do "You're clearly not ready yet... How disappointing. You'd better leave now, I have better things to do than waste my time with a weak boy like you..."        
    jump Parasol03eout
do "Hold it... Good. Well done, we can try a heavier weight now."
play sound "Sounds/panting.mp3"
$ renpy.pause(1.0, hard=True)
menu:
    "Try 200 pounds":
        do "Oooh, nice, that's a LOT... I wanna see that..."
        $ lust_points[6] +=1
        $ score += 1
        show lust01:
            xalign 0.8 yalign 0.5
            linear 1.0 yalign 0.3
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump RandyCock02Day05
    "Give up, it's too dangerous...":
        do "Well, I'm sure the biggest stud on Saturday will manage a few hundred pounds more... So you'd better work out some more name!"
        jump Parasol03eout
        
label RandyCock02Day05:
show randydoris07
play sound "Sounds/workoutgroan.mp3"
do "Now keep it flexed and hold it..."
scene randydoris06b
show randydoris07b
p "Ah... Shit, can't hold it..."
do "Well, you still managed to hold it for a while... So train some more and I think you might get there boy!"

label Parasol03eout:
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeachDay05b


label Cabin01Day05:
scene cabin01 with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
p "I guess it must be here. God, this place looks dingy."
menu:
    "Enter the cabin":
        jump Cabin02Day05
    "Leave, it looks too dangerous.":
        jump ExploreBeachDay05

label Cabin02Day05:
scene cabin02 with dissolve
stop music
$ renpy.pause(1.0, hard=True)
md "Help me [name]! I'm all tied up, I was kidnapped!"
p "Of course Maddy, I'm here to save you."
scene cabin03 with dissolve
p "Here, let me untie you... Were you... raped?"

md "No, but he was about to, he threatened me, it was horrible..."
menu:
    "You're safe now, let's get out of here before he comes back.":
        md "Thank you so much, you saved my life! You are my hero..."
        if (lust_points[14] <=6):
            window hide
            $ lust_points[14] += 3
            $ score += 3
            show lust03:
                xalign 0.3 yalign 0.5
                linear 1.0 yalign 0.3
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust03
            jump Cabin03Day05
        if (lust_points[14] ==7):
            window hide
            $ lust_points[14] += 3
            $ score += 3
            show lust03:
                xalign 0.3 yalign 0.5
                linear 1.0 yalign 0.3
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust03
            show epiclust:
                xalign 0.3 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust
            jump Cabin03Day05
        if (lust_points[14] ==8):
            window hide
            $ lust_points[14] += 2
            $ score += 2
            show lust02:
                xalign 0.3 yalign 0.5
                linear 1.0 yalign 0.3
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust02
            show epiclust:
                xalign 0.3 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust
            jump Cabin03Day05
        if (lust_points[14] ==9):
            window hide
            $ lust_points[14] += 1
            $ score += 1
            show lust01:
                xalign 0.3 yalign 0.5
                linear 1.0 yalign 0.3
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
            show epiclust:
                xalign 0.3 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust
            jump Cabin03Day05
    "Oh good. Cos I hate sloppy seconds after a rape.":
        md "What? That's disgusting, you're such a FREAK!"
        $ lust_points[14] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.3 yalign 0.3
            linear 1.0 yalign 0.5
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        p "Err, OK, let's just get out of here before he comes back."      
        jump Cabin03Day05
        
label Cabin03Day05:
scene cabin04 with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
$ maddysaved05 = True
md "How did you find me?..."
p "I ran into your rapi... I mean kidnapper and fought with him. And I beat him, he was no match for my strength! I'm DA MAN!"
md "You sure are... And I can see why you beat him, your muscles are so... AWESOME!"
if (lust_points[14] >= 10) and (stamina <= 0) and (whitebull == True):
    p "I'd better drink some White Bull if I want to be able to perform...."
    menu:
        "Drink white bull (+2 stamina)":
            show whitebull
            show square
            play sound "Sounds/lost.mp3"
            "You gulped down your White Bull energy drink."
            hide square
            hide whitebull
            $ whitebull = False
            $ stamina += 2
            jump MaddyPrefuckDay05
        "Don't drink white bull and keep it for another time":
            pass
    md "What? But... I was thinking we could... you know..."
    p "Ah. Yeah, about that. It's just that I feel really tired you know, after fighting with your kidnapper and all that..."
    md "OK, I understand [name], I hope you'll be in better \"shape\" tomorrow (wink)."
    scene beach with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Maddy is in safe hands now. But not in MY safe hands. (sigh)"
    jump ExploreBeachDay05
if (lust_points[14] >=10) and (stamina <= 0):
    p "I'll take you over to the lifeguards so they can take care of you Maddy."
    md "What? But... I was thinking we could... you know..."
    p "Ah. Yeah, about that. It's just that I feel really tired you know, after fighting with your kidnapper and all that..."
    md "OK, I understand [name], I hope you'll be in better \"shape\" tomorrow (wink)."
    scene beach with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Maddy is in safe hands now. But not in MY safe hands. (sigh)"
    jump ExploreBeachDay05 
label MaddyPrefuckDay05:
if (lust_points[14] >=10):
    p "I've got another muscle that's huge and hard... You wanna feel its awesome power?"
    md "Yes, I'm ready! Fuck me with that giant love muscle of yours [name]!"
    p "I spotted a small secluded bay on the way here, let's go there, I'm so horny, I can't wait!"
    jump MaddyFuckDay05

if (lust_points[14] <=9):
    p "I've got another muscle that's huge and hard... You wanna feel its awesome power?"
    md "Err... I just got out of being bound and abused by a filthy pervert, I'm not in the mood right now you FREAK!"
    p "Well, I thought... it might do you good. Like a therapy."
    md "No, I just want to go home... Take me home please [name]..."
    p "OK, I'll carry you to the beach and call the lifeguards so they can take care of you."
    scene beach with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Maddy is in safe hands now. But not in MY safe hands. (sigh)"
    jump ExploreBeachDay05
   
label MaddyFuckDay05:
stop music
play music "Sounds/oceanwaveslow.mp3"
scene maddybeach01 with dissolve
$ renpy.pause(1.0, hard=True)
md "It's so nice feeling some fresh air again after being locked up in this disgusting cabin... My clothes are all dirty..."
p "Maybe you should take them off then and like... feel the fresh air on your tits..."
md "You're a pervert just like that guy, but a funny clumsy one..."
scene maddybeach02 with dissolve
$ renpy.pause(1.0, hard=True)
md "But I can be dirty too. VERY dirty... And I am VERY horny right now!"
p "Alright! Let me get my swimming trunks off then, I'm getting a massive boner watching you play with your little pussy like that!"
scene maddybeach03 with dissolve
$ renpy.pause(1.0, hard=True)
md "That's what you were after right? My nice firm breasts...And that tender pussy..."
p "Damn right Maddy! Look how hard you got me!"
md "Yeah, I can see that... It's as big as the rest of your over-muscular teenage body... Bring it over between my feet..."
scene maddyfoot01 with dissolve
play sound "Sounds/ryanmoan.mp3"
$ renpy.pause(1.0, hard=True)
p "Squeeze as hard as you can with your feet Maddy and jerk my rockhard dong please!"
scene maddyfoot02 with dissolve
$ renpy.pause(1.0, hard=True)
md "Damn [name], you're drooling precum all over the place, you must be very excited?"
p "For sure, I'm as hard as a bar of titanium and ready to pop real soon!"
md "Is it the rush you felt when you beat that horrible man! Mmmh? The knowledge you're such a muscled stud gets your rocks off, right [name]?"
p "Oh, AAAH, your words are stirring me into getting even harder!"
md "Well, let's do something about that monstrous fuckpole then shall we?"
label MaddyFootDay05b:
play sound "Sounds/wanking.mp3"
scene maddyfoot01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfoot02 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfoot01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfoot02 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfoot01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfoot02 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfoot01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfoot02 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfoot01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfoot02 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfoot01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfoot02
$ renpy.pause(0.3, hard=True)
scene maddyfoot01
$ renpy.pause(0.3, hard=True)
scene maddyfoot02
$ renpy.pause(0.3, hard=True)
scene maddyfoot01
$ renpy.pause(0.3, hard=True)
scene maddyfoot02
$ renpy.pause(0.3, hard=True)
scene maddyfoot01
$ renpy.pause(0.3, hard=True)
scene maddyfoot02
$ renpy.pause(0.3, hard=True)
scene maddyfoot01
$ renpy.pause(0.3, hard=True)
scene maddyfoot02
$ renpy.pause(0.3, hard=True)
stop sound
menu:
    "Repeat":
        jump MaddyFootDay05b
    "Cum quickly (no stamina penalty)":
        scene maddyfoot03 with dissolve
        play sound "Sounds/ryancumming.mp3"
        $ renpy.pause(2.0, hard=True)
        p "Fuck, your feet are so good on my knob, RHHAAA!"
        md "Wow, I didn't expect you to cum like a stallion so soon [name]...."
        p "Don't worry, it was just a tiny premature load, let's move on to the main dish of the day!"
        jump MaddyFuckChoiceDay05

label MaddyFuckChoiceDay05:
scene maddybeach04 with dissolve
$ renpy.pause(1.0, hard=True)
md "I'm ready for anything, what are you ready for...?"
menu:
    "How about some anal to really get our juices going?" if (maddyarse == False):
        jump MaddyArseDay05
    "How about a blowjob, and I'll lick your pussy at the same time?" if (maddyblowjob == False):
        jump MaddyBlowjobDay05
        
label MaddyArseDay05:
$ maddyarse = True
scene maddyfuck04 with dissolve
$ renpy.pause(1.0, hard=True)
md "If you're gonna stick that massive pud up my arse, let me at least stretch it a bit with my hands..."
window hide
play sound "Sounds/katewank.ogg"    
$ renpy.pause(2.0, hard=True)
play sound "Sounds/maddyarse01.mp3"    
$ renpy.pause(4.0, hard=True)
md "Now you can come and stick that giant boymeat in my backside [name]!"
scene maddyarse02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Is it alright like that? It seems to fit..."
md "It...it hurts a little, you're so big!"
scene maddyfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
md "FUCK! Just a little bit more..."
scene maddyfuck02 with dissolve
play sound "Sounds/maddyarse02.mp3"    
$ renpy.pause(3.0, hard=True)
md "Oh my God, be careful! You're ripping my arsehole apart!"
p "Just relax, it will be easier..."
label MaddyArseDay05b:
play sound "Sounds/maddyarse03.mp3"    
scene maddyfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump MaddyArseDay05b
    "Move on":
        scene maddyarse02 with dissolve
        $ renpy.pause(1.0, hard=True)
        md "This is too much, my stomach is so full of cock! Please let's switch position!"
        menu:
            "Alright, how about a blowjob, and I'll lick your pussy at the same time?" if (maddyblowjob == False):
                jump MaddyBlowjobDay05
            "Fuck her sweet pussy" if ((maddyarse == True) and (maddyblowjob == True)):
                jump MaddyEndFuckDay05

label MaddyBlowjobDay05:
$ maddyblowjob = True
scene maddyfuck05 with dissolve
$ renpy.pause(1.0, hard=True)

scene maddyfuck05b with dissolve
play sound "Sounds/maddyblow01.mp3"
$ renpy.pause(5.0, hard=True)
md "I've never sucked a cock this huge before... But I don't care, I want to choke on it!"
label MaddyBlowjobDay05b:
play sound "Sounds/maddyblow02.mp3"
scene maddyfuck05 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck05b with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck05 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck05b with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck05 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck05b with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck05 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck05b with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck05 with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck05b with dissolve
$ renpy.pause(0.3, hard=True)
scene maddyfuck05
play sound "Sounds/hardsucking.mp3"
$ renpy.pause(0.3, hard=True)
scene maddyfuck05b
$ renpy.pause(0.3, hard=True)
scene maddyfuck05
$ renpy.pause(0.3, hard=True)
scene maddyfuck05b
$ renpy.pause(0.3, hard=True)
scene maddyfuck05
$ renpy.pause(0.3, hard=True)
scene maddyfuck05b
$ renpy.pause(0.3, hard=True)
scene maddyfuck05
$ renpy.pause(0.3, hard=True)
scene maddyfuck05b
$ renpy.pause(0.3, hard=True)
scene maddyfuck05
$ renpy.pause(0.3, hard=True)
scene maddyfuck05b
$ renpy.pause(0.3, hard=True)
scene maddyfuck05
$ renpy.pause(0.3, hard=True)
scene maddyfuck05b
$ renpy.pause(0.3, hard=True)
stop sound
menu:
    "Repeat":
        jump MaddyBlowjobDay05b
    "Move on":
        scene maddybeach04 with dissolve
        $ renpy.pause(1.0, hard=True)
        md "My jaws are starting to tire, your cock is just too gigantic! Please let's switch position!"
        menu:
            "Alright, how about some anal to real get our juices going?" if (maddyarse == False):
                jump MaddyArseDay05
            "Fuck her sweet pussy" if ((maddyarse == True) and (maddyblowjob == True)):
                jump MaddyEndFuckDay05

label MaddyEndFuckDay05:
scene maddyfuck03b with dissolve
play sound "Sounds/maddyfuck01b.mp3"
$ renpy.pause(3.0, hard=True)
p "Slow and easy..."
md "Good thing I do lots of stretching exercises..."
scene maddyfuck03 with dissolve
$ renpy.pause(1.0, hard=True)
p "And in it goes... We just need to get a good rhythm."
md "Mmmh, yes, fuck me slowly at first... And harder afterwards!"

play music "Sounds/maddyfuckslow.mp3"
show maddyfuckslow
show faster
call screen maddyfuckslow05
screen maddyfuckslow05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MaddyFuckFast05")
label MaddyFuckFast05:
hide faster
play music "Sounds/maddyfuckfast.mp3"
show maddyfuckfast
show cum
call screen maddyfuckfast05
screen maddyfuckfast05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MaddyFuckCum05")

label MaddyFuckCum05:
hide maddyfuckslow
hide maddyfuckfast
stop music
play music "Sounds/oceanwaveslow.mp3"
scene maddyfuckcum01
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "OOOH, FUCK, I'm dumping my load deep inside of you, RHAAAA!"
md "Damn it [name], there's too much of it, you're bloating me, pull out, pull out!"
scene maddyfuck03c with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
md "That's better, now I can also admire that magnificent fuckstick spewing its red-hot spunk all over me! Keep cumming [name]"
scene maddycum04a
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(0.5, hard=True)
scene maddycum04b
$ renpy.pause(1.0, hard=True)
scene maddycum04c
$ renpy.pause(0.5, hard=True)
scene maddycum04d
$ renpy.pause(1.0, hard=True)
md "Sssoo much cum! Yes, keep wanking that cum-cannon [name]!"
scene maddycum04e
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(0.5, hard=True)
scene maddycum04f
$ renpy.pause(1.0, hard=True)
scene maddycum04g
play sound "Sounds/cumming.mp3"
$ renpy.pause(3.0, hard=True)
scene maddycum05
$ renpy.pause(1.0, hard=True)
md "My God, you cum so much, what a stallion! Look at me, I'm caked in your hot spunk!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ backdoor += 1
if (katefucked == True) and (laurafucked == True) and (friedafucked == True) and (achievement.has("classroom") == False):
    show achievement03:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement03
    $ achievement.grant("classroom")

md "Good thing this cove is secluded, I can go and clean myself in the sea. Fancy coming along [name]?"
p "Phew, yeah, a nice cooling-off in the ocean would be good!"
$ maddyfucked = True

$ fuckedschoolgirlday05 = True
if (maddyjosewin == False):
    p "(She didn't notice I took a picture of us... Now I'll send it to José)."
    $ maddywin = True

scene maddyafterfuck with dissolve
$ renpy.pause(1.0, hard=True)
md "Don't tell Frieda you had sex with me, she looks up to me, I don't want to disappoint her..."
p "Sure, absolutely nobody will ever know, I swear... (fingers crossed)."
$ hour += 1
jump ExploreBeachDay05

label DowntownDay05:
stop music
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"
$ renpy.pause(1.0, hard=True)
p "The bus left me right in front of the main downtown plaza."
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_71
    $ lustaddedB = 1
    call Challenger from _call_Challenger_72
    $ lustaddedB = 1
    call Challenger from _call_Challenger_73
    $ challengercalls += 2

if (hour >= 19):
    p "It's getting late, I should really take the bus and get home now."
    $ bushome = True
    jump BusDowntownHomeDay05
else:
    jump DowntownChoiceDay05b

label BusDowntownHomeDay05:
p "Ah, here's the bus heading to the Burbs, I'd better take it..."
$ bushome = True
jump BusDriveDayb05

label DowntownChoiceDay05b:
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"

if (hour >= 19):
    p "It's getting late, I should really take the bus and get home now."
    jump BusDowntownHomeDay05

p "Where should I go?"
menu:
    "Go to Audacious HQ" if (discoveraudacious == True):
        jump AudaciousHQDay05
    "Go shopping":
        jump ShopDay05
    "Go to the massage parlour" if (discovermassage == True) and (parlourseen05 == False):
        jump Parlour01Day05
    "Take the bus home":
        $ bushome = True
        jump BusDowntownHomeDay05
    "Take the bus to the beach" if (hour <= 17):
        $ busbeach = True
        jump BusDowntownBeachDay05
    "Go to the downtown gym" if (discovergym == True) and (seengym05 == False):
        jump Gym01Day05
    "Put some posters up for Miss Titsworthy's campaign (+1hr)" if (principaldeal == True) and (posterup == False)  and (postersaid == False):
        jump PosterDay05
    "Go to Old Joe's Emporium" if (discoveremporium == True):
        jump PawnShop01Day05
    "Go to the main plaza" if (discoverplaza == True) and (redpill <= 1) and (bluepill <=1):
        jump PlazaDay05

label PlazaDay05:
scene dealer01 with dissolve
$ renpy.pause(1.0, hard=True)
p "There's a dodgy guy over there. He looks Mexican, he must be either a drug-dealer or a rapist, right?"
menu:
    "Approach the dodgy guy":
        jump DrugDay05
    "Leave":
        jump DowntownChoiceDay05b
   
label DrugDay05:
mx "Hola gringo! You looka for some-fingo?"
p "(Phew, he's not a rapist) Yeah, I'm feeling down lately, if you know-a what I mean-o..."
mx "I have justa what you're after. Fresho from MERICO!!! Twenty dollars for two of the samo for you my gringo friend!"
scene dealer02 with dissolve
$ renpy.pause(1.0, hard=True)
p "And what do they do?"
mx "I don't know, I just work for the cartel \"Los Trumpos\". They told me some-fingo like..."
mx "If you take a rojo pill, you go down the rabbit-hole, and if you take a bluo pill, a rabbit goes up your hole."
mx "Or some-fingo like that gringo. Choose quickly, the copos are not far from here."
if (money <= 19):
    p "I don't have the money anyway. So fuck off back to Mexico and wait in line in Tijuana like everyone else!"
    mx "I came to Veri-Bosti legally gringo arsehole! You fuck offo back to Merica!!!"
    scene dealer03 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Oh well, it was probably some dodgy shit anyways. Drugs are bad, m'kay?"
    jump DowntownChoiceDay05b    
call screen drugday05
stop music
"You were too slow and the drug dealer leaves in a hurry."
scene dealer03 with dissolve
$ renpy.pause(1.0, hard=True)
mx "I gotta go. The copos are on me...."
p "Oh well, it was probably some dodgy shit anyways. Drugs are bad, m'kay?"
play music "Sounds/downtown.mp3"
jump DowntownChoiceDay05b

label DrugRedDay05:
stop music
play music "Sounds/downtown.mp3"
$ money -= 20
mx "Nice doing business with you gringo!"
show redpills
show square
play sound "Sounds/found.mp3"
"You acquired two red pills. With unknown effects..."
$ redpill = 2
hide redpills
hide square
scene dealer03 with dissolve
$ renpy.pause(1.0, hard=True)
mx "Hasta la vista, I gotta go."
jump DowntownChoiceDay05b

label DrugBlueDay05:
stop music
play music "Sounds/downtown.mp3"
$ money -= 20
mx "Nice doing business with you gringo!"
show bluepills
show square
play sound "Sounds/found.mp3"
"You acquired two blue pills. With unknown effects..."
$ bluepill = 2
hide bluepills
hide square
scene dealer03 with dissolve
$ renpy.pause(1.0, hard=True)
mx "Hasta la vista, I gotta go."
jump DowntownChoiceDay05b

label PosterDay05:
scene downtownposter with dissolve
$ renpy.pause(1.0, hard=True)
$ hour += 1
p "That's done. I almost feel ashamed, this slogan is so cheesy..."
$ posterup = True
jump DowntownChoiceDay05b

label BusDowntownBeachDay05:
p "Ah, here's the bus heading for the beach, I'd better take it..."
jump BusDriveDayb05

label PawnShop01Day05:
scene emporium01 with dissolve
$ renpy.pause(1.0, hard=True)
oj "Hello young man. Welcome to Old Joe's Emporium. We buy and sell all sorts of wares."
label PawnShop01Day05b:
menu:
    "I have an ancient gold coin I'd like to sell." if (goldcoin == True):
        oj "Well let's have a look at it then."
        scene emporium02 with dissolve
        $ renpy.pause(1.0, hard=True)
        oj "I see... It's genuine, seems to be 17th century Spanish gold, probably sunk with a galleon."
        scene emporium03 with dissolve
        $ renpy.pause(1.0, hard=True)
        oj "I'll give you 30 dollars."
        menu:
            "Deal!":
                $ money += 30
                show goldcoin
                show square
                play sound "Sounds/lost.mp3"
                "You sold your gold coin."
                hide square
                hide goldcoin
                $ goldcoin = False
                oj "Nice doing business with you sir, come back any time."
                jump DowntownChoiceDay05b
            "50 dollars.":
                oj "40 dollars."
                menu:
                    "Deal!":
                        $ money += 40
                        show goldcoin
                        show square
                        play sound "Sounds/lost.mp3"
                        "You sold your gold coin."
                        hide square
                        hide goldcoin
                        $ goldcoin = False
                        oj "Nice doing business with you sir, come back any time."
                        jump DowntownChoiceDay05b
                    "No, 50 dollars.":
                        oj "30 dollars."
                        menu:
                            "Deal!":
                                $ money += 30
                                show goldcoin
                                show square
                                play sound "Sounds/lost.mp3"
                                "You sold your gold coin."
                                hide square
                                hide goldcoin
                                $ goldcoin = False
                                oj "Nice doing business with you sir, come back any time."
                                jump DowntownChoiceDay05b
                            "Hang on, I'm confused...":
                                $ money += 30
                                show goldcoin
                                show square
                                play sound "Sounds/lost.mp3"
                                "You sold your gold coin."
                                hide square
                                hide goldcoin
                                $ goldcoin = False
                                oj "30 dollars it is then. Nice doing business with you sir, come back any time."
                                p "Err... Right. (I think I was conned but I'm not even sure....)"
                                jump DowntownChoiceDay05b
                    "Mmmm, I don't know, it was given to me by a mermaid, maybe I want to keep it as a souvenir.":
                        oj "Ah, ah, you're a funny boy. A mermaid... What a laugh! Tell you what, I'll give you 30 dollars and that's my final word. Ah, ah, a mermaid!"
                        $ money += 30
                        show goldcoin
                        show square
                        play sound "Sounds/lost.mp3"
                        "You sold your gold coin."
                        hide square
                        hide goldcoin
                        $ goldcoin = False
                        p "Err... Right. (I'm confused, I thought I said I wanted to keep it....)"
                        jump DowntownChoiceDay05b
    "What's this place?":
        oj "I just told you boy, are you deaf?"
        jump PawnShop01Day05b
    "Leave":
        jump DowntownChoiceDay05b

label AudaciousHQDay05:
scene downtownaudacious with dissolve
$ renpy.pause(1.0, hard=True)
p "Wow, this is where mom and aunt Debby work? This building looks HUGE."

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
            se "Hmm, OK, everything seems to be in order Mr...Visitor."
            jump AudaciousOffice01Day05

        "Let me through, my aunt is the CEO of this company.":
            hide security01
            show security02
            se "And I'm the pope's daughter. Get out of here kid."
            $ audacioustried = True
            jump DowntownChoiceDay05b

        "Out of my way oaf! I'm DA MAN! I will trample you!":
            $ audacioustried = True
            if (strength >= 9):
                se "We'll see about that!"
                hide security01                
                show security04
                p "I warned you, take that!"
                play sound "Sounds/punch.mp3"
                $ renpy.pause(1.0, hard=True)
                p "Ha, ha, now the coast is clear to enter the building..."
                jump AudaciousOffice01Day05
            if (strength <=8):
                hide security01
                show security03
                se "We'll see about that!"
                play sound "Sounds/punch.mp3"
                $ renpy.pause(1, hard=True)
                if (blacktop05 == True):
                    scene audaciousbeatenblack with dissolve
                    $ renpy.pause(1.0, hard=True)
                else:
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
                jump DowntownChoiceDay05b

if (audacioustried == True):
    p "I already tried getting into this building today. I should probably leave."
    jump DowntownChoiceDay05b

label ShopDay05:
if (evictedfromshop == True):
    "You are banned from entering this boutique until tomorrow. Bad boy. VERY bad boy."
    jump DowntownChoiceDay05b
if (shoppingseen05 == True):
    "You already went shopping today. Looks like you might be a shopaholic..."
    jump DowntownChoiceDay05b
if (shoppingseen04 == True):
    jump Shop01Day05
if (shoppingseen04 == False):
    jump ShopAltDay05

label ShopAltDay05:
$ shoppingseen05 = True
$ altshop = True
stop music
scene shopday04 with dissolve
play music "Sounds/shopmusic.mp3"
$ renpy.pause(1.0, hard=True)
p "This boutique looks very expensive..."
p "There's a nice-looking clerk standing behind the counter and several customers looking at skimpy swimsuits...The shop seems to be very busy today..."

label Shop01AltDay05b:
scene shopday04 with dissolve
menu:
    "Go talk to the clerk":
        jump ShopClerkDay05
    "Go talk to the black girl on the left":
        jump ShopCustomerDay05
    "Go talk to the redhead in the middle":
        jump ShopCustomerRedDay05
    "Go talk to the blonde on the right":
        jump ShopCustomerBlondeDay05
    "Go to the changing rooms" if (foundcabins == True) and (rightcabinseen05 == False):
        jump ShopCabinChoiceAltDay05
    "Leave":
        stop music
        jump DowntownChoiceDay05b    

label Shop01Day05:
$ shoppingseen05 = True
stop music
scene shop with dissolve
play music "Sounds/shopmusic.mp3"
$ renpy.pause(1.0, hard=True)
p "This boutique looks very expensive..."
p "There's a nice-looking clerk standing behind the counter and one customer looking at a skimpy swimsuit..."

label Shop01Day05b:
scene shop with dissolve
menu:
    "Go talk to the clerk":
        jump ShopClerkDay05
    "Go talk to the customer":
        jump ShopCustomerDay05
    "Go to the changing rooms" if (foundcabins == True):
        jump ShopCabinChoiceDay05
    "Leave":
        stop music
        jump DowntownChoiceDay05b

label ShopCustomerRedDay05:
scene shopred01 with dissolve
$ renpy.pause(1.0, hard=True)
re "Oh, you're a man, give me your advice. Should I choose the red or the green bikini?"
menu:
    "The red bikini, it will match your hair.":
        re "Yes, you're right, thank you!"
        jump Shop01AltDay05b    
    "The green bikini, it will match your eyes.":
        re "Yes, you're right, thank you!"
        jump Shop01AltDay05b
    "Imagine her naked":
        scene shopred01b with dissolve
        play sound "Sounds/dreaming.mp3"
        $ renpy.pause(2.0, hard=True)
        re "Err... Hello? Are you ogling my breasts? What a pervert!"
        sc "Stop disturbing the customers! This is a respectable establishment. I must ask you to leave at once!"
        $ evictedfromshop = True
        jump DowntownChoiceDay05b

label ShopCustomerBlondeDay05:
scene shopblonde01 with dissolve
$ renpy.pause(1.0, hard=True)
bl "Can't you see I'm busy thinking? There's too many new bikinis to choose from in this store!"
sc "Stop disturbing the customers!"
jump Shop01AltDay05b

label ShopClerkDay05:
scene shop01 with dissolve
sc "How may I help you?"
menu:
    "Talk to her":
        jump ShopTalkDay05
    "Buy something":
        jump ShopBuyDay05  
    "Leave the counter":
        if (altshop == True):
            jump Shop01AltDay05b
        jump Shop01Day05b

label ShopTalkDay05:
menu:
    "You know what would look good on you? Me.":
        scene shop03
        sc "Mmh, lemme think... Yes, it's the worst pick-up line ever."
        jump ShopClerkDay05
    "What's the word on the street downtown?":
        if (downtowntipgiven == True):
            sc "I already gave you a tip today. Stop pestering me."
            jump ShopClerkDay05
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
            jump ShopClerkDay05
        if (downtowntips == 1):
            sc "The downtown gym holds a major weightlifting competition this weekend."
            sc "I hear you have to be like super-strong to win. Also super-virile. Maybe you can try..."
            $ downtowntipgiven = True
            $ downtowntips += 1
            show addedlocation:
                xalign 0.7 yalign 0.3
                linear 1.0 yalign 0.1
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide addedlocation
            $ discovergym = True
            jump ShopClerkDay05
        if (downtowntips == 2):
            sc "If you ever have some valuable items clustering your attic, you can always try and sell them at \"Old Joe's Emporium\"."
            sc "It's 100 yards away in a small alley called \"Dirty Street\"..."
            $ downtowntipgiven = True
            $ downtowntips += 1
            show addedlocation:
                xalign 0.7 yalign 0.3
                linear 1.0 yalign 0.1
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide addedlocation
            $ discoveremporium = True
            jump ShopClerkDay05
        if (downtowntips == 3):
            sc "The town hall is concerned about an increase in drug dealing on the main plaza downtown."
            sc "There's a new hard drug hitting the streets apparently, I would avoid that area if I were you."
            p "Of course, sound advice (in your dreams...)."
            $ downtowntipgiven = True
            $ downtowntips += 1
            show addedlocation:
                xalign 0.7 yalign 0.3
                linear 1.0 yalign 0.1
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide addedlocation
            $ discoverplaza = True
            jump ShopClerkDay05
    "What's going on today? It seems unusually busy..." if (altshop == True):
        sc "We have just received the new summer line of \"Audacious Bikinis\". People are going crazy for them."
        sc "We've also received the new \"Mega-sized Audacious Briefs for Boys\". But not many people seem interested in them unfortunately..."
        p "Err... I might be interested, I want to try one."
        sc "Oh great!, you can pick one from the shelf for your size and try it in one of the changing rooms, if you can find one that's empty..."
        $ foundcabins = True
        jump ShopClerkDay05
        
label ShopBuyDay05:
menu:
    "Buy swimsuit for customer (40$ - pay 20$ from your own pocket)" if (money >= 20) and (seenhallebikini == True) and (boughthallebikini == False):
        scene shop02
        play sound "Sounds/cashregister.wav"
        sc "Here you are. That's for one lucky girl!"        
        $ money -= 20
        $ boughthallebikini = True
        jump HalleGiftDay05

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
        jump ShopClerkDay05

    "Nothing actually":
        jump ShopClerkDay05

    "I don't have enough money to buy anything here." if (money <=9):
        sc "We don't do credit. We don't trust poor people like you."
        p "I feel like... dirt..."
        jump ShopClerkDay05

label ShopCustomerDay05:
scene halleshop01 with dissolve
$ renpy.pause(1.0, hard=True)
if (boughthallebikini == True) and (seenhallebikini == True):
    p "Hey, Halle, why are you still here? I bought you this swimsuit already!"
    show halleshop01b
    ha "Yeah, I know, but the dev is too lazy to remove me from this image..."
    ha "Remember, I'm ACTUALLY at the beach."
    jump Shop01Day05
elif (boughthallebikini == False) and (seenhallebikini == True):
    p "You're still staring at this swimsuit..."
    show halleshop01b
    ha "And I'll keep staring at it until you chip in 20 bucks to buy it for me!"
    if (altshop == True):
        jump Shop01AltDay05b
    jump Shop01Day05b

else:
    menu:
        "May I help you with anything miss? Would you like to try this item in one of our cabins?":
            show halleshop01b
            ha "Oh...hum.. Sorry, I didn't realize you worked here... Well, I don't know, it's quite expensive..."
            p "Well, try it on, that's free anyway..."
            ha "Yeah, I guess you're right, I might as well try it on..."
            $ pretendshop = True
            jump HalleChangeDay05
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
                    jump HalleChangeDay05
                "That's too bad, cos I'm sure you would be a hit with that thing on...":
                    ha "(sigh)... Yes, it's too bad..."
                    if (altshop == True):
                        jump Shop01AltDay05b
                    jump Shop01Day05b


label HalleChangeDay05:
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
            jump DowntownChoiceDay05b
        "Wait for her to come out":
            jump HalleBikini01Day05
else:
    ha "Hang on a minute, I'm almost ready..."

label HalleBikini01Day05:
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
        jump HalleBikini02Day05
    "Yeah, really hot... Turn around now...":
        ha "Like...that?"
        jump HalleBikini02Day05

label HalleBikini02Day05:
    scene hallebikini02 with dissolve
$ renpy.pause(1.0, hard=True)
if (pretendshop == True):
    p "Yes, that is a definitive perfect fit..."
    ha "Would...you..consider giving me a discount? I'm twenty bucks short to buy it and I really need a new bikini to go to the beach!"
    "The bikini is marked at 40 dollars..."
    menu:
        "Sure, for a girl like you, half-price! Give it to me and I'll make all the arrangements" if (money >= 20):
            ha "Oh, thank you sssoo much. My name is Halle by the way and I'll be wearing this at the beach if you ever fancy joining me (wink)!"
            if (altshop == True):
                jump Shop01AltDay05b
            jump Shop01Day05b
        "Mmh, you'll have to show me more to get such a discount price miss...":
            jump HalleTopOffDay05
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
            if (altshop == True):
                jump Shop01AltDay05b
            jump Shop01Day05b

else:
    p "Wow, you look really hot...err..."
    ha "The name's Halle. So, since you like it so much, time to chip in 20 bucks like you promised so I can buy it!"
    menu:
        "Ah... About that.. I just realized I don't have enough money." if (money <= 19):
            ha "But..You promised me!"
            p "OK, OK, as soon as I get the money, I'll come back I swear!"
            ha "I'll be here every afternoon, lamenting as to why I can't own this lovely bikini!"
            "Well at least, I know where to find her..."
            if (altshop == True):
                jump Shop01AltDay05b
            jump Shop01Day05b
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
            if (altshop == True):
                jump Shop01AltDay05b
            jump Shop01Day05b
        "Well, sure...sure... But a little incentive wouldn't hurt... If you know what I mean...":
            ha "I know what you mean...You boys are all the same..."
            jump HalleTopOffDay05
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
            jump ShopClerkDay05
            
label HalleTopOffDay05:
scene halletopoff with dissolve
$ renpy.pause(1.0, hard=True)  
ha "So... Now that you've seen my big sumptuous tits... Time to cough up the money!"
p "Let me regain my breath first... WOW! I'll pay the difference for you baby!"
jump ShopClerkDay05

label HalleGiftDay05:
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
if (altshop == True):
    jump Shop01AltDay05b
jump Shop01Day05b

label ShopCabinChoiceDay05:
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
if (chiyofucked == False) and (rightcabinseen == True):
    p "Now let's see, I hope Chiyo is here again... I haven't fucked her yet."
    jump NewChiyoDay05
if (chiyofucked == False) and (rightcabinseen == False):
    jump ShopCabinChoiceAltDay05
if (chiyofucked == True):
    p "No need to waste time checking if Chiyo is here, I've already fucked her and I need to keep my stamina."
    p "Let's check the cabin on the left instead then."
    scene redcabin02 with dissolve
    $ renpy.pause(1.0, hard=True)    
    re "Oui?"
    p "Oui! OUI!"
    re "And NON. Get out of here or I'm calling the police!"
    p "Alright, alright. I guess there's a reason she's not on the list of 24 in-game girls..."
    jump DowntownChoiceDay05b
    
    
label NewChiyoDay05:
stop music
play sound "Sounds/dooropen.mp3"
$ renpy.pause(1.0, hard=True)
scene chiyo01day05 with dissolve
$ rightcabinseen05 = True
cy " You again! Barging in on me while I'm trying on a skimpy lingerie set..."
p "The call of duty Chiyo, the call of duty..."
cy "Well, in that case, it is YOUR duty to tell me what you think about this set..."
scene chiyo02day05 with dissolve
$ renpy.pause(1.0, hard=True)
cy "Is it the right color? Does it hug my big firm breasts well enough?"
p "Mmh, Yes it does... Turn around so I can see if the thong is well positioned between your asscheeks..."
cy "That's cheeky! Let me get rid of that lace top so you can get get a better look then..."
window hide
$ lust_points[3] += 1
$ score += 1
show lust01:
    xalign 0.5 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
scene chiyo03day05 with dissolve
$ renpy.pause(1.0, hard=True)
cy "So... I hope you brought a big fat dildo this time..."
if (dildo == True):
    p "I sure did!"
    cy "Oh, very good! Give it to me then I want to stick it up my arse!"
    scene chiyodildo01 with dissolve
    $ renpy.pause(1.0, hard=True)
    cy "Just jerk that fat donkey-dick and watch, naughty boy."
    scene chiyodildo02 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Wow, she's sticking it so far up her backside..."
    play sound "Sounds/chiyodildo.mp3"
    scene chiyodildo01
    $ renpy.pause(0.5, hard=True)
    scene chiyodildo02
    $ renpy.pause(0.5, hard=True)
    scene chiyodildo01
    $ renpy.pause(0.5, hard=True)
    scene chiyodildo02
    $ renpy.pause(0.5, hard=True)
    scene chiyodildo01
    $ renpy.pause(0.5, hard=True)
    scene chiyodildo02
    $ renpy.pause(0.5, hard=True)
    scene chiyodildo01
    $ renpy.pause(0.5, hard=True)
    scene chiyodildo02
    $ renpy.pause(0.5, hard=True)
    scene chiyodildo01
    $ renpy.pause(0.5, hard=True)
    scene chiyodildo02
    $ renpy.pause(0.5, hard=True)
    cy "Ooh, it's so good... It stretches my little arsehole so much... AAAH..."
    scene chiyofuck02 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Come on, enough of that, I've got the real thing right here!"
    $ lust_points[3] += 2
    $ score += 2
    show lust02:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    if (lust_points[3] == 10):
        show epiclust:
            xalign 0.8 yalign 0.2
            zoom 0.5
            linear 2.0 zoom 1.0
        play sound "Sounds/epiclust.mp3"
        $ renpy.pause(4.0, hard=True)
        hide epiclust
        cy "Mmh, you might deserve a reward after all... You're such a filthy pervert... And that cock looks so tasty..."
        jump ChiyoNewFuckREALDay05
    if (lust_points[3] >= 8) and (((pendulumactive == True) and (pendulum == True)) or (pheromone == True)):
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
                jump ChiyoPendulumDay05           
            "Spray yourself with pheromones" if (pheromone == True):
                window hide
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump ChiyoPheromoneDay05
            "Don't use anything":
                jump ChiyoNoFuckDay05
    else:
        jump ChiyoNoFuckDay05
    
if (dildo == False):
    p "I don't have a dildo, I have a REAL cock."
    cy "Too bad then that you don't have one.... I was really horny... But I'm not anymore, you spoilt the mood."
    p "What? But..."
    cy "Now shoot little boy. Hee hee."
    play sound "Sounds/doorclosing.mp3"
    scene shopcabin01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "I might as well check the door on the left then while I'm here..."
    scene redcabin02 with dissolve
    $ renpy.pause(1.0, hard=True)    
    re "Oui?"
    p "Oui! OUI!"
    re "And NON. Get out of here or I'm calling the police!"
    p "Alright, alright. I guess there's a reason she's not on the list of 24 in-game girls..."
    jump DowntownChoiceDay05b

label ShopCabinChoiceAltDay05:
stop music

scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
label ShopCabinChoiceDay05b:
p "Mmh, which cabin should I choose?"
menu:
    "The cabin on the left" if (leftcabinseen05 == False):
        jump ShopCabin01Day05
    "The cabin in the middle":
        jump ShopCabin02Day05
    "The cabin on the right" if (rightcabinseen05 == False):
        jump ShopCabin03Day05
    "Leave":
        scene shop01 with dissolve
        sc "So, did they fit you big boy? Are you ready to buy a pair?"
        p "Err... No, they're soiled actually, don't know how it happened really..."
        scene shop04 with dissolve
        sc "What? You're soiling my products? Get out of my shop immediately!"
        $ evictedfromshop = True
        jump DowntownChoiceDay05b

label ShopCabin01Day05:
play sound "Sounds/dooropen.mp3"
scene randyshop01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oh, it's that couple I saw on the beach on the first day I arrived!"
rc "Mmmh, I can see that got you horny!"
rb "Fuck yeah baby, let's do it right here... Hey, there's someone watching us!"
$ leftcabinseen05 = True
scene randyshop02 with dissolve
$ renpy.pause(1.0, hard=True)
rb "What are you looking at? Never seen a huge thick pre-teen monstercock before or what?"
rc "I doubt it honey, your young giant penis is the biggest ever! I bet he wants to watch, isn't that right boy?"
menu:
    "I don't have time for this lewd display!":
        rc "Pff, such a prude! Get outta here then, while I get my pussy wet to take my boyfriend's behemoth!"
        rb "Too bad for you buddy, you could have learnt a thing or two... I'm gonna pound her sweet pussy till she's begging for me to stop!"
        play sound "Sounds/doorclosing.mp3"
        jump ShopCabinChoiceDay05b
    "Ok, why not, I'm bored anyway. (50\%\ chance of +1 stamina)":
        rc "First, I'll get my pussy wet to take my boyfriend's behemoth! It's important since he's so gigantic..."
        rb "Watch this buddy. I'm gonna pound her sweet pussy till she's begging for me to stop!"
        jump RandyShop02Day05
        
label RandyShop02Day05:
scene randyshop03 with dissolve
$ renpy.pause(1.0, hard=True)
rc "Oh fuck baby, you're stretching me ssoo good... And you're so deep inside me!"
rb "I'm not even half-way in, open wide to take in another ten inches!"
scene randyshop04 with dissolve
$ renpy.pause(0.3, hard=True)
rc "AAAH! Such a fucking megadong! Give me more baby!"
rb "Watch buddy, she's already creaming all over my huge cock!"
play music "Sounds/randybeachchickmoaning.mp3"
scene randyshop03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyshop04 with dissolve
$ renpy.pause(0.3, hard=True)
rc "Cum inside me baby, I want to feel my stomach bloat with your tenth giant load of the day!"
scene randyshop05 with dissolve
stop music
play sound "Sounds/randyboycumming.mp3"
$ renpy.pause(1.0, hard=True)
rb "RHHAAA, yes, I 'm cumming.... AAAH!"
rc "Oh, my stomach is about to burst from being overfilled with your young spunk! Come all over me baby!"
scene randyshop06 with dissolve
play sound "Sounds/randyboycumming02.mp3"
$ renpy.pause(1.0, hard=True)
rc "Look at all those massive cumshots flying everywhere after he totally filled me with ounces of boycream already!"
scene randyshop07 with dissolve
play sound "Sounds/randyboycumming.mp3"
$ renpy.pause(1.0, hard=True)
rc "That's it, you've seen enough, we're far from done but this is our special arse time now."
rb "Oh yeah, I'm gonna stretch that arse nice and good, let me just finish unloading and I'll stay rock-hard for you! Hope you learnt a thing or two buddy, now leave us alone."
$ d2randycabin05=renpy.random.randint(0, 1)
if (d2randycabin05 == 0):
    $ stamina +=1
    show stamina01:    
        xalign 0.2 yalign 0.4   
        linear 1.0 yalign 0.2
    $ renpy.pause(2, hard=True)
    play sound "Sounds/more.mp3"
    hide stamina01
if (d2randycabin05 == 1):
    pass
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
jump ShopCabinChoiceDay05b

label ShopCabin02Day05:
play sound "Sounds/dooropen.mp3"
scene shopcabin02 with dissolve
$ renpy.pause(1.0, hard=True)
ow "Mmh, what do you think boy? I think this bikini hugs my curves perfectly."
p "Oh no, it's her again! Let's close the door and erase this from my memory..."
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
$ stamina -=1
show staminaminus01:    
    xalign 0.2 yalign 0.2   
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ eyesore += 1
jump ShopCabinChoiceDay05b

label ShopCabin03Day05:
stop music
play sound "Sounds/dooropen.mp3"
scene shopcabin03 with dissolve
$ rightcabinseen05 = True
label ShopCabin03Day05b:
cy "How rude, I'm all naked and you barge in here just as I was about to put on this bikini..."
p "Sorry but all the stalls are taken and I wanted to try on these new mega-sized briefs."
cy "Mega-sized briefs? Well maybe I could make some room for you in here then... But no touching naughty boy..."
cy "But first, let me put on this bikini..."
scene shopcabin03b with dissolve
$ renpy.pause(1.0, hard=True)
cy "What do you think? Will you be having problems putting on your briefs over that hardening rod, hee hee..."
menu:
    "I'll...try anyway if you don't mind...":
        jump ShopCabin03bDay05
    "You're right, let's just go straight to business then shall we?":
        cy "What business? You have no business being in here to start with you randy pervert! Now get out of my stall, you've seen too much already!"
        $ lust_points[3] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.6 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        play sound "Sounds/doorclosing.mp3"
        scene shopcabin01 with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ShopCabinChoiceDay05b

label ShopCabin03bDay05:
scene shopcabin03c with dissolve
$ renpy.pause(1.0, hard=True)
cy "Oh my... They might be mega-sized briefs but they clearly are no match for that massive package of yours..."
cy "I want to hear your cock thump hard against your pecs you naughty boy as I undress slightly for you..."
scene shopcabin03d with dissolve
play sound "Sounds/thud.mp3"
$ renpy.pause(1.0, hard=True)
cy "That is so nasty... and hot... Yeah, flex that mighty fuckstick studboy!"
scene shopcabin03c with dissolve
$ renpy.pause(0.3, hard=True)
scene shopcabin03d with dissolve
play sound "Sounds/thud.mp3"
$ renpy.pause(0.3, hard=True)
scene shopcabin03c with dissolve
$ renpy.pause(0.3, hard=True)
scene shopcabin03d with dissolve
play sound "Sounds/thud.mp3"
$ renpy.pause(0.3, hard=True)
scene shopcabin03c with dissolve
$ renpy.pause(0.3, hard=True)
scene shopcabin03d with dissolve
play sound "Sounds/thud.mp3"
$ renpy.pause(0.3, hard=True)
$ lust_points[3] += 1
$ score += 1
show lust01:
    xalign 0.7 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
scene chiyofuck01 with dissolve
$ renpy.pause(1.0, hard=True)
cy "What would get me really horny now is a big dildo so I could play with my little arsehole and stretch it out for... that giant thing."
if (dildo == True):
    p "How about this one lady? Big enough for you?"
    cy "Yes! And black too... My favorite color... Gimme me that, boy, and watch while you jerk your fat donkey-dick!"
    $ lust_points[3] += 2
    $ score += 2
    show lust02:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    show dildo
    show square
    play sound "Sounds/lost.mp3"
    "You gave away a huge black dildo."
    hide square
    hide dildo
    $ dildo = False
    if (lust_points[3] == 10):
        show epiclust:
            xalign 0.4 yalign 0.2
            zoom 0.5
            linear 2.0 zoom 1.0
        play sound "Sounds/epiclust.mp3"
        $ renpy.pause(4.0, hard=True)
        hide epiclust
        jump ChiyoFuck01Day05
    if (lust_points[3] >= 8) and (((pendulumactive == True) and (pendulum == True)) or (pheromone == True)):
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
                jump ChiyoPendulumDay05           
            "Spray yourself with pheromones" if (pheromone == True):
                window hide
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump ChiyoPheromoneDay05
            "Don't use anything":
                jump ChiyoFuck01Day05
    if (lust_points[3] <= 7):
        jump ChiyoFuck01Day05
    
if (dildo == False):
    p "I don't have a dildo, I have a REAL cock."
    cy "Too bad then that you don't have one.... I was really horny... But I'm not anymore, you spoilt the mood. Shoot little boy. Hee hee."
    p "What? But you can't leave me in such a state!"
    cy "Of course I can. You shouldn't be in the same stall as me anyway. The woman in the stall next door is horny, you can get that fat cock serviced by her."
    p "AAARGH!"
    play sound "Sounds/doorclosing.mp3"
    scene shopcabin01 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump ShopCabinChoiceAltDay05
    
        
label ChiyoPendulumDay05:
scene chiyopendulum with dissolve
show pendulum03
$ renpy.pause(1.0, hard=True)
p "Just watch this pendulum as I wiggle it in front of your eyes lady..."
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
if (lust_points[3] ==8):
    window hide
    $ lust_points[3] += 2
    $ score += 2
    show lust02:
        xalign 0.3 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    cy "I can't help but feel the need to jump that fat young cock of yours! Even though I just want to tease you all day!"
    if (altshop == True):
        jump ChiyoFuck01Day05
    jump ChiyoNewFuckREALDay05
if (lust_points[3] ==9):
    window hide
    $ lust_points[3] += 1
    $ score += 1
    show lust01:
        xalign 0.3 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    cy "I can't help but feel the need to jump that fat young cock of yours! Even though I just want to tease you all day!"
    if (altshop == True):
        jump ChiyoFuck01Day05
    jump ChiyoNewFuckREALDay05


label ChiyoPheromoneDay05:
scene chiyopendulum with dissolve
$ renpy.pause(1.0, hard=True)
$ pheromone = False
play sound "Sounds/sniffing.mp3"
$ renpy.pause(1.0, hard=True)
cy "What is that weird naughty and enticing smell...?"
p "My spray is now empty... I guess I won't be able to use it again."
show pheromone
show square
play sound "Sounds/lost.mp3"
"You lost a pheromone spray."
hide square
hide pheromone
$ pheromone = False
if (lust_points[3] ==8):
    window hide
    $ lust_points[3] += 2
    $ score += 2
    show lust02:
        xalign 0.6 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    show epiclust:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    jump ChiyoFuck01Day05
if (lust_points[3] ==9):
    window hide
    $ lust_points[3] += 1
    $ score += 1
    show lust01:
        xalign 0.6 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    show epiclust:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    if (altshop == True):
        jump ChiyoFuck01Day05
    jump ChiyoNewFuckREALDay05

label ChiyoFuck01Day05:
scene chiyofuck01 with dissolve
$ renpy.pause(1.0, hard=True)
cy "Get out of those skivvies.... I want to see that monster cock in all its glory!"
p "Alright! Yeah, now we're talking, I'm rock-hard for you lady..."
cy "My name's Chiyo, you don't need to tell me yours. Your cock is making me so horny and naughty that I need to play with my arse... and that huge dildo!"
scene chiyodildo01 with dissolve
$ renpy.pause(1.0, hard=True)
cy "Just jerk that fat donkey-dick and watch, naughty boy."
scene chiyodildo02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Wow, she's sticking it so far up her backside..."
play sound "Sounds/chiyodildo.mp3"
scene chiyodildo01
$ renpy.pause(0.5, hard=True)
scene chiyodildo02
$ renpy.pause(0.5, hard=True)
scene chiyodildo01
$ renpy.pause(0.5, hard=True)
scene chiyodildo02
$ renpy.pause(0.5, hard=True)
scene chiyodildo01
$ renpy.pause(0.5, hard=True)
scene chiyodildo02
$ renpy.pause(0.5, hard=True)
scene chiyodildo01
$ renpy.pause(0.5, hard=True)
scene chiyodildo02
$ renpy.pause(0.5, hard=True)
scene chiyodildo01
$ renpy.pause(0.5, hard=True)
scene chiyodildo02
$ renpy.pause(0.5, hard=True)
cy "Ooh, it's so good... It stretches my little arsehole so much... AAAH..."
label ChiyoFuckALTDay05:
scene chiyofuck02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Come on, enough of that, I've got the real thing right here!"

label ChiyoNewFuckREALDay05:
if (lust_points[3] == 10):
    cy "Mmh, I know and it DOES look tasty... What would you want to do with it naughty naughty boy?"
    menu:
        "If it looks tasty, then give me a blowjob!":
            jump ChiyoBlowjobDay05
        "Your pussy looks tasty... And ready for a good pounding!":
            jump ChiyoPussyDay05

cy "I think you've seen enough naughtiness for the day. I came here to buy a bikini, not to get fucked by some random horse-hung boy. So you can leave now..."
p "AAARGH! She's doing it to me again!"
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
jump ShopCabinChoiceAltDay05
            
label ChiyoBlowjobDay05:
$ chiyoblowjob = True
scene chiyoblowjob01 with dissolve
play sound "Sounds/chiyoblowjob01.mp3"
$ renpy.pause(8.0, hard=True)
cy "Mmh, yeah, I've never sucked a cock that big before but I'm willing to try since you're such a naughty boy...."
scene chiyoblowjob02 with dissolve
play sound "Sounds/chiyoblowjob02.mp3"
$ renpy.pause(2.5, hard=True)
p "Oh fuck! You're doing great Chiyo, just take a few more inches and I'll be in heavens!"
scene chiyoblowjob03 with dissolve
play sound "Sounds/chiyoblowjob03.mp3"
$ renpy.pause(3.0, hard=True)
p "Yeah, just like th..."
label ChiyoBlowjobDay05b:
play sound "Sounds/hardsucking.mp3"
scene chiyoblowjob02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyoblowjob03 with dissolve
$ renpy.pause(0.3, hard=True)
$ chiyoblowjob = True
stop sound
menu:
    "Repeat":
        jump ChiyoBlowjobDay05b
    "Your pussy looks tasty... And ready for a good pounding!" if (chiyopussy == False):
         jump ChiyoPussyDay05
    "It's time to stretch that gaping anus even more than that puny dildo you used!" if (chiyoblowjob == True) and (chiyopussy == True):
        jump ChiyoArseDay05

label ChiyoPussyDay05:
scene chiyopussy01 with dissolve
play sound "Sounds/chiyopussy01.mp3"
$ renpy.pause(7.0, hard=True)
p "That's nothing, I'm not even half-way in!"
scene chiyopussy02 with dissolve
play sound "Sounds/chiyopussy02.mp3"
$ renpy.pause(11.0, hard=True)
cy "Oh my God, you're so deep!"
label ChiyoPussyDay05b:
play sound "Sounds/chiyopussy03.mp3"
scene chiyopussy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chiyopussy02 with dissolve
$ renpy.pause(0.3, hard=True)
$ chiyopussy = True
stop sound
menu:
    "Repeat":
        jump ChiyoPussyDay05b
    "If it looks tasty, then give me a blowjob!" if (chiyoblowjob == False):
        jump ChiyoBlowjobDay05
    "It's time to stretch that gaping anus even more than that puny dildo you used!" if (chiyoblowjob == True) and (chiyopussy == True):
        jump ChiyoArseDay05

label ChiyoArseDay05:
scene chiyoarse01 with dissolve
$ renpy.pause(0.3, hard=True)
cy "I'm ready to have my little arsehole stretched by your naughty prick!"
play music "Sounds/chiyofuckslow.mp3"
show chiyofuckslow
show faster
call screen chiyofuckslow05
screen chiyofuckslow05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("ChiyoFuckFast05")
label ChiyoFuckFast05:
hide faster
play music "Sounds/chiyofuckfast.mp3"
show chiyofuckfast
show cum
call screen chiyofuckfast05
screen chiyofuckfast05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("ChiyoFuckCum05")

label ChiyoFuckCum05:
hide chiyofuckfast
hide chiyofuckslow
stop music
scene chiyocum01
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "OOOH, I'm cumming so hard....AAAH"
cy "Fill my arse, bloat me! AAAH, I can feel each massive streamer of cum pummelling my insides!"
scene chiyocum02 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
cy "Look at all that cum spewing everywhere naughty boy! The shop clerk is going to have to work extra-hard to get rid of all of it."
scene chiyocum03 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
cy "I'm dumping rivers of cum all over the place and I still feel pregnant with your virile seed!"
p "I don't think I ever came that much in my life... Phew!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01

cy "I'm gonna stay here for a while... I need to empty the ounces of cum you dumped inside me!"
cy "I think the whole shop will smell of your seed for the rest of the afternoon, hee hee!"
p "I love filthy girls like you Chiyo, but I have to get going!"
$ hour += 1
$ chiyofucked = True
$ backdoor += 1
if (katsumifucked == True) and (achievement.has("asian") == False):
    show achievement04:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement04
    $ achievement.grant("asian")
if (chiyojosewin == False):
    p "(She didn't notice I took a picture of us... Now I'll send it to José)."
    $ chiyowin = True
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I'd better leave this place quietly before anyone notices me..."
jump DowntownChoiceDay05b

label ChiyoNoFuckDay05:
cy "Looks like you won't be getting any Asian poontang from me today... Now shoot little boy, hee hee..."
p "Damn lustmeter! AARGH!"
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
if (altshop == True):
    jump ShopCabinChoiceDay05b
if (altshop == False):
    scene shopcabin01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "I might as well check the door on the left then while I'm here..."
    scene redcabin02 with dissolve
    $ renpy.pause(1.0, hard=True)    
    re "Oui?"
    p "Oui! OUI!"
    re "And NON. Get out of here or I'm calling the police!"
    p "Alright, alright. I guess there's a reason she's not on the list of 24 in-game girls..."
    jump DowntownChoiceDay05b


label Parlour01Day05:
scene parlour01
$ parlourseen05 = True
$ renpy.pause(1.0, hard=True)
play music "Sounds/parlourmusic.mp3"
ka "Welcome big American boy to \"Misohawny Massage Parlour\"! Me Katsumi, you want massage?"
menu:
    "I was told you did \"full-body massage\"...":
        ka "Yes, sucky sucky 50 dolla."
        p "Ah, I see. Sucky sucky indeed. That's quite expensive for just sucky sucky."
        ka "Me love you long time. For you, more than sucky sucky."
        p "Oh, the conversations we could have my dear..."
        jump ParlourChoiceDay05
    "Yes, how much is it?":
        ka "Normal massage? 10 dolla. More massage, 50 dolla."
        p "And what do I get for 50 dollars exactly?"
        ka "Sucky sucky 50 dolla."
        p "That's a lot of inflation since the Vietnam War..."
        jump ParlourChoiceDay05
    "Nope, not interested...":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceDay05b

label ParlourChoiceDay05:
menu:
    "Get a normal massage (10 $)" if (money >=10):
        jump NormalMassageDay05
    "Choose the \"full-body massage\" experience... (50 $)" if (money >=50) and (stamina >=1):
        jump FullMassageDay05
    "Mmh...I don't seem to have enough money at the moment." if (money <=9):
        ka "You poor. Hah hah. Me not poor. Come back when you not poor."
        p "I certainly will, if just for the highly stimulating conversations."
        jump DowntownChoiceDay05b
    "Mmh, I don't seem to have enough stamina at the moment." if(stamina == 0):
        ka "Ah! You not man enough. You leave and come back when you can cum."
        jump DowntownChoiceDay05b
    "Actually, I don't want anything right now.":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceDay05b

label NormalMassageDay05:
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
                jump Parlour05Day05
            "Forget it. Just give me a normal massage.":
                ka katsumi "Ok, me gonna massage your cock because ssooo BIG."
                jump Parlour05Day05
    "OK, OK, I'll pay the difference for a sucky sucky..." if (money >=40) and (stamina >=1):
        $ suckysucky = True
        $ fuckyfucky = True
        $ money -= 40
        jump Parlour05Day05
    "Why don't you just massage it then like if it was one of my big tense muscles?...":
        ka "Oooh, boy very smart. OK, me gonna massage big American cock. But no sucky sucky, you not pay."
        jump Parlour05Day05

label FullMassageDay05:
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
        jump Parlour05Day05        
    "That's cos all Asian men have small penises.":
        ka "Not true. Some Asian men big penis. You like Trump, you racist."
        ka "Me only do sucky sucky. No fucky fucky. Because you bad boy."
        $ fuckyfucky = False
        jump Parlour05Day05

label Parlour05Day05:
scene parlour05 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Big American monster boycock so big and hard!"
p "Yeah, play with it Katsumi! It's all yours!"

label Parlour06Day05:
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
                jump Parlour07Day05
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
                jump DowntownChoiceDay05b
    
label Parlour07Day05:  
scene parlour07 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Me gonna lick huge balls first... Sssoo tasty and spicy, like chicken Sichuan."
window hide
if (katsumiwin == False):
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

label Parlour08Day05:  
scene parlour08 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Reaching top of monstercock take me so long... Me love you long time!"
p "Keep going, you still have quite a few inches to go..."

label Parlour09Day05:  
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
                if (katsumiwin == False):
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
                $ katsumifucked = True
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
                $ katsumifucked = True
                $ hour += 1
                if (chiyofucked == True) and (achievement.has("asian") == False):
                    show achievement04:
                        xalign 0.5 yalign 0.2
                        zoom 0.5
                        linear 2.0 zoom 1.0
                    play sound "Sounds/achievement.mp3"
                    $ renpy.pause(4.0, hard=True)
                    hide achievement04
                    $ achievement.grant("asian")
                jump DowntownChoiceDay05b

label Parlour10Day05:  
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
        
label ParlourFuckDay05:
stop music
play music "Sounds/katsumifuck.mp3"
show movieparlourfuck
show cum
call screen parlourfuckcumday05
screen parlourfuckcumday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("ParlourCumDay05")

label ParlourCumDay05:
stop music
hide movieparlourfuck
scene parlourcum01
stop music
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
ka "You filling me up with so much boyjuice! You so incredible!"
play sound "Sounds/ryancumming.mp3"
scene parlourcum02 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Look! Cum flowing from my Asian pussy ssooo much! Cum everywhere! Me need to get cleaned up for next client now!"
p "Fuck, you rode me like a wild bronco... I'm exhausted!"
window hide
$ katsumifucked = True
if (chiyofucked == True) and (achievement.has("asian") == False):
    show achievement04:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement04
    $ achievement.grant("asian")
$ stamina -=1
show staminaminus01:
    xalign 0.7 yalign 0.6
    linear 1.0 yalign 0.8
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ hour += 1
jump DowntownChoiceDay05b

label Gym01Day05:
$ seengym05 = True
stop music
scene gym01 with dissolve
play music "Sounds/gymreception.mp3"
$ renpy.pause(1.0, hard=True)
if (wenttogymday03 == False) and (seengym04 == False):
    jump GymFirstDay05
if ((seengym04 == True) and (wenttogymday03 == False)) or ((seengym04 == False) and (wenttogymday03 == True)):
    jump GymSecondDay05
if (seengym04 == True) and (wenttogymday03 == True):
    jump GymThirdDay05

label GymFirstDay05:
da "Welcome to \"Jerk n' Clean Fitness Club \". My name is Daniella, how may I help you?"
label Gym01bDay05:
scene gym01 with dissolve
menu:
    "How do I become a member?":
        da "It's five dollars per session. Or you can buy a monthly pass for 50 dollars and you can invite a friend twice."
        p "Mmh, I'm interested in the monthly pass but it's quite steep, I'd like to try it out first. For free."
        da "Well you can't. Five dollars to try it out or nothing."
        menu:
            "Alright then, here's five bucks." if (money >= 5):
                scene gym03 with dissolve
                da "Excellent! You now have access to the gym for the day! Enjoy your workout."
                $ money -= 5
                jump Gym03Day05
            "Mmh, I'll think about it.":
                jump Gym01bDay05
    "I'm a member already. A LONG-STANDING \"member\" if you catch my drift...":
        show gym02 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "I tried to catch it but then it flew away..."
        jump Gym01bDay05
    "Why should I pay to join your gym when there are free gyms around the island?":
        da "Because our gym has the best equipment you can find on the island, that's why."
        p "I'm not convinced. You need to prove it."
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Alright Mr-Big-Shot. Follow me and I'll prove it!"
        jump Gym02Day05
    "Leave the gym":
        jump DowntownChoiceDay05b

label Gym02Day05:
scene gym04 with dissolve
$ renpy.pause(1.0, hard=True)
da "First of all, we have some tanning beds. For those who want to get ready for a competition. Do other gyms have this? I think not."
p "Yeah ok, but I prefer my tan natural..."
da "You've clearly never been in a bodybuilding competition before..."
scene gym05 with dissolve
stop music
play music "Sounds/gymabience.mp3"
$ renpy.pause(1.0, hard=True)
da "There's our main gym room. Notice that we have all the latest workout equipments...Benches, squat racks, exercise bikes, EVERYTHING!"
p "Nice... What else you got?"
da "Oh, that's not enough? Mister is a fine connoisseur I see. The next room will finish to convince you."
stop music
scene gym06 with dissolve
$ renpy.pause(1.0, hard=True)
da "...The sauna room. For relaxing after a heavy workout. Oh and by the way, it's MIXED (wink). How many other gyms on the island have one? NONE, that's how many!"
da "And finally, not that it concerns you, we have a pole dancing room, it's a new urban trend for women."
menu:
    "OK, I'm sold, here's five bucks." if (money >=5):
        da "Alright! You are free to use any room today then... Except the women's locker room that is."
        jump Gym03Day05
    "OK, I'm sold here's 50 bucks for a monthly pass." if (money >=50):
        if (money >= 200):
            da "Mmmh, I wonder how a boy your age managed to accumulate that much money..."
            da "Perhaps you robbed a bank? The Console Bank of Cheats?..."
            p "Err... No, I can explain!"
            da "Bye bye cheat..."
            return
        da "Alright, new member it is!... And don't forget you can invite a friend twice..."
        $ money -= 50
        $ gymmember = True
        $ lust_points[4] +=1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump Gym03Day05
    "Great, I'll try out the equipment straight away then. See you in a bit.":
        da "Err...Sure... I think..."
        jump Gym03Day05
    "Not convinced, I'll give it a pass for today.":
        da "Your choice, but you're missing out on some great fitness fun!"
        jump DowntownChoiceDay05b

label Gym03Day05:
scene dorisgym01 with dissolve
play music "Sounds/gymabience.mp3"
$ renpy.pause(1.0, hard=True)
"There's only one \"interesting\" customer in the gym at this time."
menu:
    "Do some heavy training (+1hr)" if (workout == False):
        jump GymWorkoutDay05
    "Approach the woman":
        jump GymDorisDay05

label GymWorkoutDay05:
scene
play music "Sounds/workoutgroan.mp3"
$ renpy.movie_cutscene("Day3/downtownworkout.ogv", delay=-1, loops=-1, stop_music=False)
stop music
scene gymworkout with dissolve
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
$ hour += 1
$ muscleman += 1
scene dorisryangym01 with dissolve
$ renpy.pause(1.0, hard=True)
do "Not bad boy... Will you be entering the Mister Muscle Stud competition this Saturday?"
menu:
    "What's to win?":
        do "100 dollar prize money. But more importantly, the admiration of MANY female fans..."
        $ lust_points[6] +=1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01        
    "Do you think I might have a chance?":
        do "The competition is fierce. You definitely need to train hard and get stronger..."
        do "But your huge muscles and the strength you just displayed already show promising signs..."
        do "Not to mention that massive bulge in your pants..."
        $ lust_points[6] +=2
        $ score += 2
        show lust02:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
p "How is that supposed to count?"
do "Well, it's not called \"Muscle STUD\" competition for nothing... But why don't you join me in the sauna, I'll tell you all about it..."
menu:
    "Sure, I want to know! (+1hr)" if (hour <=18):
        jump SaunaDorisDay05
    "I don't have time right now I'm afraid, it's getting late...":
        do "Too bad boy, we could have had some good time..."
        jump DowntownChoiceDay05b

label SaunaDorisDay05:
stop music
$ seendorissauna = True
scene dorissauna01 with dissolve
$ renpy.pause(1.0, hard=True)
do "Ah, there you are finally, I was starting to wonder if you would ever turn up..."
do "Don't be a prude and take that towel off. There's no one else around but us... And I need to check if that bulge is REAL!"
p "Sure, if you do too..."
scene dorissauna02 with dissolve
$ renpy.pause(1.0, hard=True)
do "Are you satisfied young man? Your turn now... I can't wait to see that giant love muscle you're hiding down there."
scene dorissauna03 with dissolve
$ renpy.pause(1.0, hard=True)
do "Damn boy, that's what I call a potential winner!"
$ lust_points[6] +=1
$ score += 1
show lust01:
    xalign 0.55 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
p "Potential?"
do "Well, the competition takes more into account than just the size of your soft dangling manhood..."
scene dorissauna04 with dissolve
$ renpy.pause(1.0, hard=True)
do "You will need to get ROCK-HARD for the jury... They will measure its dimensions."
do "And you will also need to deliver a MASSIVE load of cum into a measuring jar!"
scene dorissauna05 with dissolve
$ renpy.pause(1.0, hard=True)
do "You think you'll be able to rise up to the challenge boy? This hardening fuckstick tells me yes... Let's check shall we?"
play music "Sounds/wanksound.mp3"
play sound "Sounds/doriswank.mp3"
scene dorissauna05b with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.3, hard=True)    
scene dorissauna05b with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.3, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05 with dissolve
$ renpy.pause(0.1, hard=True)
scene dorissauna05b with dissolve
$ renpy.pause(0.1, hard=True)
stop sound
scene dorissaunacum01 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
do "That's it, plaster me with your hot load! Show me you have what it takes to win that competition boy!"
scene dorissaunacum02 with dissolve
stop music
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
do "Wow, you sure do! You keep cumming like a firehose even after drenching me in ounces of cum!"
scene dorissaunacum03 with dissolve
$ renpy.pause(1.0, hard=True)
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.6
    linear 1.0 yalign 0.8
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
do "Well, that was pretty amazing kid... But you still have some more training to do if you want to win. I'll be happy to help... Right now, I need a hot shower."
$ lust_points[6] +=2
$ score += 2
show lust02:
    xalign 0.7 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
p "(pant)... Thanks for that, your hands were amazing.... I'm pretty sure I'll be coming back for MORE!"
$ hour += 1
jump DowntownChoiceDay05b

label GymDorisDay05:
$ seendorisgym01 = True
scene dorisgym02 with dissolve
$ renpy.pause(1.0, hard=True)
scene dorisgym03 with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(1.0, hard=True)
scene dorisgym02 with dissolve
$ renpy.pause(1.0, hard=True)
scene dorisgym03 with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(1.0, hard=True)
p "The woman seems rather focused on her workout..."
label DorisGymTrainDay05:
menu:
    "Continue watching":
        scene dorisgym02 with dissolve
        $ renpy.pause(1.0, hard=True)
        scene dorisgym03 with dissolve
        play sound "Sounds/womangroan.mp3"
        $ renpy.pause(1.0, hard=True)
        scene dorisgym02 with dissolve
        $ renpy.pause(1.0, hard=True)
        scene dorisgym03 with dissolve
        play sound "Sounds/womangroan.mp3"
        $ renpy.pause(1.0, hard=True)
        scene dorisgym04 with dissolve
        do "Hey, stop disturbing me like that boy!"
        jump DorisGymTrainDay05
    "Leave and do some heavy training (+1hr)" if (workout == False):
        jump GymWorkoutDay05    
    "Leave the gym":
        jump DowntownChoiceDay05b

label GymSecondDay05:
da "Welcome back to \"Jerk n' Clean Fitness Club \". Are you planning on using the gym again today?"
scene gym01 with dissolve
menu:
    "Yes, I am a fully-fledged member so it's free right?" if (gymmember == True):
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Of course, just make yourself at home [name]! I can go and get a tan now finally..."
        jump GymSecond01Day05        
    "Yes, here's five bucks to use it for the day...(pay $5)" if (money >= 5):
        $ money -= 5
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Perfect, the gym is all yours... I can go and get a tan now finally..."
        jump GymSecond01Day05
    "Yes, on becoming a fully fledged member." if (money >= 50) and (gymmember == False): 
        $ money -= 50
        $ gymmember = True
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Perfect, the gym is all yours... I can go and get a tan now finally..."
        jump GymSecond01Day05        
    "No, not really, just came to say \"Hi\".":
        show gym02 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Well, \"Hi\" and now \"Goodbye\"..."
        jump DowntownChoiceDay05b

label GymSecond01Day05:
$ wenttogym05 = True
scene gymanna01 with dissolve
play music "Sounds/gymabience.mp3"
$ renpy.pause(1.0, hard=True)
p "There's Anna in a tight outfit..."
if (seendorisgym01 == False) and (seendorissauna == False):
        p "And a muscular lady doing curls."
if (seendorissauna == True) or (seendorisgym01 == True):
        p "And Doris lifting a heavy barbell."
label GymChoiceDay05:
if (hour >= 19):
    p "Damn, it's getting late. Let's go back home..."
    jump DowntownChoiceDay05b
menu:
    "Do some heavy training (+1hr)" if (workout == False):
        jump GymWorkoutSecondDay05
    "Approach Anna" if (talkedannagym05 == False):
        jump GymAnnaDay05
    "Approach the muscular woman" if (seendorissauna == False) and (seendorisgym05 == False) and (seendorisgym01 == False):
        jump GymDorisDay05
    "Approach Doris" if ((seendorissauna == True) or (seendorisgym01 == True)) and (seendorisgym05 == False):
        jump GymDorisBellDay05
    "Go to the tanning rooms" if (seentanningbed05 == False):
        jump TanningDay05
    "Leave the gym":
        jump DowntownChoiceDay05b

label TanningDay05:
$ seentanningbed05 = True
scene tanning01 with dissolve
play sound "Sounds/banging.mp3"
$ renpy.pause(2.0, hard=True)
p "Oooh ooh... There's some weird noise coming from that room..."
p "Seems like someone got stuck under the tanning bed.[name] to the rescue!"
scene tanning02 with dissolve
$ renpy.pause(1.0, hard=True)
da "Thanks for saving me, I was getting burnt in here!"
$ lust_points[4] +=3
$ score += 3
show lust03:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust03
p "What happened? How did you end up stuck inside?"
scene tanning03 with dissolve
$ renpy.pause(1.0, hard=True)
da "This is so embarassing, it's the first time it happens... REALLY."
da "And I'm all naked in front of a customer..."
p "My only concern was to rescue you Daniella."
scene tanning03 with dissolve
$ renpy.pause(1.0, hard=True)
da "Well, how can I thank you... I'll give you a free pass to the gym for tomorrow, how does that sound?"
$ freegym06 = True
p "Sounds like a $5 dollar reward for saving your life..."
da "Yeah, well, the gym is heavily in debt. I hope that the Muscle Stud competition on Saturday will attract many new female customers..."
p "I'll be in it!"
da "I have no doubt. Seeing how muscular and... big down there you are..."
da "Now I need to put on some fake untan lotion so I don't look like a lobster. Thanks again for saving me [name]!"
jump GymChoiceDay05


label GymAnnaDay05:
scene gymanna02 with dissolve
$ renpy.pause(1.0, hard=True)
an "Oh, hello [name]... I'm glad you're here, I don't really know what to do with this machine and the gym owner is not around..."
$ talkedannagym05 = True
menu:
    "Help her":
        jump GymAnnaHelpDay05
    "Tell her you don't have time but she can watch you train":
        scene gymanna02b with dissolve
        $ renpy.pause(1.0, hard=True)
        an "Humpf, I didn't come here to watch other people train, but to do a workout!"
        window hide
        $ lust_points[0] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.2 yalign 0.4
            linear 1.0 yalign 0.6
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump GymChoiceDay05
    "Ask her if she wants to join you in the sauna":
        scene gymanna02b with dissolve
        $ renpy.pause(1.0, hard=True)
        an "I just arrived here, I haven't even worked out yet!"
        an "So no, I am not interested in wasting my time in the sauna with you...Goodbye [name]."
        jump GymChoiceDay05

label GymWorkoutSecondDay05:
scene
play music "Sounds/workoutgroan.mp3"
$ renpy.movie_cutscene("Day3/downtownworkout.ogv", delay=-1, loops=-1, stop_music=False)
stop music
scene gymworkout with dissolve
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
$ hour += 1
jump GymChoiceDay05

label GymAnnaHelpDay05:
$ helpedannagym05 = True
p "Just sit on the bench with your head down, and then do crunches. I'll hold your legs for you if you want."
an "Oh, that's what this machine is for? I hope it works, I would really like to get better abs..."
menu:
    "Your abs are already pretty damn fit Ms Longrod...":
        an "Well, thank you for the compliment, but I have seen the gym owner and hers are like a wall of bricks!"
        an "So let's get to crunching then!"
        jump GymAnnaCrunchDay05
    "That's how I got my rock-hard abs, see?":
        scene gymanna03 with dissolve
        $ renpy.pause(1.0, hard=True)
        an "Damn, they really are rock-HARD! You sure are a strapping muscle boy [name]..."
        window hide
        $ lust_points[0] +=1
        $ score += 1
        show lust01:
            xalign 0.2 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        an "Well, let's get to crunching then!"
        jump GymAnnaCrunchDay05
        
label GymAnnaCrunchDay05:
scene gymanna04 with dissolve
$ renpy.pause(1.0, hard=True)
an "Like that? Is that a good starting position?"
p "Yeah, but put your arms behind your head and then start raising your bod using your abs..."
scene gymanna04b with dissolve
$ renpy.pause(1.0, hard=True)
scene gymanna04c with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(1.0, hard=True)
scene gymanna04d with dissolve
$ renpy.pause(1.0, hard=True)
p "Now turn your neck to the right and then to the left...."
scene gymanna04e with dissolve
$ renpy.pause(1.0, hard=True)
scene gymanna04f with dissolve
$ renpy.pause(1.0, hard=True)
an "It's quite tough! I can feel my abs really straining..."
p "That's good, it means you are doing it right, do a few more, at least 10 of them..."
an "Okay, I'll try..."
scene gymanna04d with dissolve
$ renpy.pause(1.0, hard=True)
scene gymanna04c with dissolve
$ renpy.pause(1.0, hard=True)
scene gymanna04b with dissolve
$ renpy.pause(1.0, hard=True)
scene gymanna04c with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(1.0, hard=True)
scene gymanna04d with dissolve
$ renpy.pause(1.0, hard=True)
scene gymanna04e with dissolve
$ renpy.pause(1.0, hard=True)
scene gymanna04f with dissolve
$ renpy.pause(1.0, hard=True)
p "A bit faster now..."
scene gymanna04d with dissolve
$ renpy.pause(0.5, hard=True)
scene gymanna04c with dissolve
$ renpy.pause(0.5, hard=True)
scene gymanna04b with dissolve
$ renpy.pause(0.5, hard=True)
scene gymanna04c with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.5, hard=True)
scene gymanna04d with dissolve
$ renpy.pause(0.5, hard=True)
scene gymanna04e with dissolve
$ renpy.pause(0.5, hard=True)
scene gymanna04f with dissolve
$ renpy.pause(0.5, hard=True)
p "Nice, I get to check out her huge funbags at the same time..."
scene gymanna04d with dissolve
$ renpy.pause(0.3, hard=True)
scene gymanna04c with dissolve
$ renpy.pause(0.3, hard=True)
scene gymanna04b with dissolve
$ renpy.pause(0.3, hard=True)
scene gymanna04c with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.3, hard=True)
scene gymanna04d with dissolve
$ renpy.pause(0.3, hard=True)
scene gymanna04e with dissolve
$ renpy.pause(0.3, hard=True)
scene gymanna04f with dissolve
$ renpy.pause(0.3, hard=True)
p "Okay, you did 10 reps!"
scene gymannaend with dissolve
$ renpy.pause(1.0, hard=True)
an "Thank you for showing me how to use the crunch bench [name]."
an "I won't keep you any longer away from YOUR workout, I'm sure it must be very LONG and HARD..."
window hide
$ lust_points[0] +=1
$ score += 1
show lust01:
    xalign 0.2 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
jump GymChoiceDay05

label GymDorisBellDay05:
scene dorisbell01 with dissolve
$ renpy.pause(1.0, hard=True)
if (seendorisgym01 == True) or (seendorissauna == True):
    p "There's Doris training with what looks like a pretty heavy barbell..."
if (seendorisgym01 == False) and (seendorissauna == False):
    p "There's a muscular lady training with what looks like a pretty heavy barbell..."
$ seendorisgym05 = True
scene dorisbell02
play sound "Sounds/womangroan.mp3"
$ renpy.pause(1.0, hard=True)
scene dorisbell03
play sound "Sounds/panting.mp3"
$ renpy.pause(2.0, hard=True)
scene dorisbell02 with dissolve
$ renpy.pause(0.5, hard=True)
scene dorisbell01 with dissolve
play sound "Sounds/panting.mp3"
$ renpy.pause(2.0, hard=True)
scene dorisbell02
play sound "Sounds/womangroan.mp3"
$ renpy.pause(1.0, hard=True)
scene dorisbell03
play sound "Sounds/panting.mp3"
$ renpy.pause(2.0, hard=True)
scene dorisbell02 with dissolve
$ renpy.pause(0.5, hard=True)
scene dorisbell01 with dissolve
play sound "Sounds/panting.mp3"
$ renpy.pause(2.0, hard=True)
scene dorisbell02
play sound "Sounds/womangroan.mp3"
$ renpy.pause(1.0, hard=True)
scene dorisbell03
play sound "Sounds/panting.mp3"
$ renpy.pause(2.0, hard=True)
scene dorisbell02 with dissolve
$ renpy.pause(0.5, hard=True)
scene dorisbell01 with dissolve
play sound "Sounds/panting.mp3"
$ renpy.pause(2.0, hard=True)
menu: 
    "Hi Doris, are you training hard again today?":
        do "Every day is training day, I didn't get those muscles doing nothing boy!"
        p "Yeah, same here, I train every day to maintain my super-huge muscles!"
        do "Well, look who's bragging... You're gonna prove to me they are strong enough?"
        p "Err... What do you mean?"
        do "I bet you can't do 3 reps with this barbell without breaking a sweat."
        p "Pff, piece of cake for me, I'm DA MAN, I'll show you!"
        jump GymDorisBell03Day05
    "Now I get why you are so muscular, this barbell is super-heavy!":
        do "Yeah, I'm the strongest woman on the island, wanna spot me?"
        p "Sure, I'll spot you Doris."
        jump GymDorisBell02Day05    
    "Let me handle this barbell, it's clearly too heavy for you.":        
        do "Is that what you think? That's so typical of men. Of LOUSY men."
        window hide
        $ lust_points[6] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.2 yalign 0.4
            linear 1.0 yalign 0.6
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
        do "I bet you can't do 3 reps with it without breaking a sweat."
        p "Pff, piece of cake for me, I'm DA MAN, I'll show you!"
        jump GymDorisBell03Day05

label GymDorisBell02Day05:
scene dorisbell04 with dissolve
$ renpy.pause(2.0, hard=True)
do "I'll go faster this time so keep up!"
scene dorisbell05 with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.5, hard=True)
scene dorisbell05b with dissolve
$ renpy.pause(1.0, hard=True)
scene dorisbell05 with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.3, hard=True)
scene dorisbell05b with dissolve
$ renpy.pause(1.0, hard=True)
scene dorisbell05 with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.5, hard=True)
scene dorisbell05b with dissolve
$ renpy.pause(1.0, hard=True)
scene dorisbell05 with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.3, hard=True)
scene dorisbell05b with dissolve
$ renpy.pause(1.0, hard=True)
scene dorisbell05 with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.5, hard=True)
scene dorisbell05b with dissolve
$ renpy.pause(1.0, hard=True)
scene dorisbell05 with dissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.3, hard=True)
scene dorisbell05b with dissolve
$ renpy.pause(1.0, hard=True)
do "I can't... concentrate with that monstrous bulge right in my face!"
scene dorisbell05 with dissolve
$ renpy.pause(0.3, hard=True)
scene dorisbell06 with dissolve
$ renpy.pause(1.0, hard=True)
do "Shit!"
p "I caught it, no worries!"
do "Puff, thanks, without you, that 500kg barbell could have crushed me..."
$ lust_points[6] +=1
$ score += 1
show lust01:
    xalign 0.4 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01        
scene dorisbell07 with dissolve
$ renpy.pause(1.0, hard=True)
do "Now it's your turn to show me what you can do with this barbell..."
menu:
    "I'm not ready, I'd rather not...":
        if (seendorissauna == False):
            do "Are you at least ready to join me in the sauna so we can talk some more about that competition?"
            menu:
                "Sure, I want to know more about it (+1hr)" if (hour <=18):
                    jump SaunaDorisDay05                    
                "Na, no time, busy busy...":
                    do "You clearly don't have what it takes to become the island's Muscle Stud..."
                    jump GymChoiceDay05
        if (seendorisgym01 == True):
            do "Bailing out are we? How do you expect to win the Muscle Stud competition Saturday if you don't train?"
            p "I train every day! You'll see, I'll be ready on Saturday, I'm da man, I'm DA MAN!"
            do "Well go and play with your tiny toys boy, I'm gonna add some more weights to this barbell, I'm not done with my training yet."
            jump GymChoiceDay05
        if (seendorisgym01 == False):
            do "Too bad, I was looking for a muscle stud to take under my wing for the upcoming Muscle Stud Competition..."
            p "No, I'm a muscle stud, I swear! What's that competition about?"
            do "About more than muscles... Hence the stud part... You'll find out on Saturday. If you don't chicken out."
            jump GymChoiceDay05
        do "I should find myself another muscle stud to take under my wing. Good thing I spotted a few young stallions around the island already..."
        window hide
        $ lust_points[6] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.2 yalign 0.4
            linear 1.0 yalign 0.6
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01  
        do "So go and play with your tiny toys boy, I'm gonna add some more weights to this barbell, I'm not done with my training yet."
        jump GymChoiceDay05
    "Pff, piece of cake for me, I'm DA MAN, I'll show you!":
        jump GymDorisBell03Day05
  
label GymDorisBell03Day05:
scene dorisbell08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Alright, here we go..."
scene dorisbell09
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
scene dorisbell08
$ renpy.pause(1.0, hard=True)
scene dorisbell09
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
scene dorisbell08
$ renpy.pause(1.0, hard=True)
scene dorisbell09
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
scene dorisbell10
play sound "Sounds/dumbbell.mp3"
$ renpy.pause(1.0, hard=True)
p "No! I dropped it! But I almost did three reps, right?"
do "Almost. But not quite. You need to train some more kid. Maybe with smaller weights to begin with. (sigh)"
do "So go and play with your tiny toys, I'm gonna add some more weights to this barbell, I'm not done with my training yet."
jump GymChoiceDay05

label GymThirdDay05:
da "Welcome back to \"Jerk n' Clean Fitness Club \". Are you planning on using the gym again today?"
scene gym01 with dissolve
menu:
    "Yes, I am a fully-fledged member so it's free right?" if (gymmember == True):
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Of course, just make yourself at home [name]! I was about to start my training myself..."
        jump GymThird01Day05
    "I've got a free pass today for saving your life yesterday remember?" if (freegym05 == True):
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Of course, I didn't forget [name]! Just make yourself at home. I can go and get a tan now finally..."
        jump GymThird01Day05
    "Yes, here's five bucks to use it for the day...(pay $5)" if (money >= 5):
        $ money -= 5
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Perfect, the gym is all yours... I was about to start my training myself..."
        jump GymThird01Day05
    "Yes, and on becoming a fully-fledged member (pay $50)" if (money >= 50) and (gymmember == False): 
        $ money -= 50
        $ gymmember = True
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Perfect, the gym is all yours... I was about to start my training myself..."
        jump GymThird01Day05        
    "No, not really, just came to say \"Hi\".":
        show gym02 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Well, \"Hi\" and now \"Goodbye\"..."
        jump DowntownChoiceDay05b

label GymThird01Day05:
$ wenttogym05 = True
if (invitedchantelle == True) or (invitedfrancine == True) or (invitedchantelle05 == True) or (invitedfrancine05 == True):
    menu:
        "Call Francine to join you here" if ((gymmember == True) and ((invitedfrancine == True) or (invitedfrancine05 == True))) and (hour <= 17):
            $ francinegym05 = True
            p "I guess it will take her a while to get there, I might as well enjoy the gym until then."
            jump GymThird01Day05b
        "Call Chantelle to join you here" if ((gymmember == True) and ((invitedchantelle == True) or (invitedchantelle05 == True))) and (hour <= 17):
            $ chantellegym05 = True
            p "I guess it will take her a while to get there, I might as well enjoy the gym until then."
            jump GymThird01Day05b
        "Don't invite anyone and enter the gym":
            jump GymThird01Day05b
            
label GymThird01Day05b:
scene gymdaniella01 with dissolve
play music "Sounds/gymabience.mp3"
$ renpy.pause(1.0, hard=True)
p "There's Daniella doing some curls..."
menu:
    "Approach Daniella":
        jump DaniellaGym01Day05
    "Go to the locker room":
        jump GymBoyDay05
        
label DaniellaGym01Day05:
scene gymdaniella02 with dissolve
$ renpy.pause(1.0, hard=True)
da "Hello there, do you need any help with our wonderful state-of-the-art equipment?"
menu:
    "Na, I'm good, I know everything, I train a lot.":
        scene gymdaniella03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Well, good for you. Now if you'll excuse me..."
        jump GymChoiceThirdDay05
    "I was wondering, how do I join the \"Muscle Stud Competition\"?":
        scene gymdaniella03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "You just turn up on Saturday at 2pm."
        da "But are you sure you want to do that? It's very competitive, and you might get humiliated..."
        p "Me, humiliated? No way, I'll win for sure!"
        scene gymdaniella04 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Let me be the judge of that... I'm gonna check how well you're faring so far..."
        da "Take your shirt off and get on that machine over there in the corner..."
        jump DaniellaGym02Day05
        
label DaniellaGym02Day05:
stop music
scene gymdaniella05 with dissolve
$ renpy.pause(1.0, hard=True)
da "So, Mr big shot, let's see you lifting up 800kg... That's the minimum requirement for being allowed to compete..."
p "Rhaaa, no worries, I'm da man , I'm DA MAN!"
scene gymdaniella06 with dissolve
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
da "Not bad, but what about if I tease you a bit... Can you hold onto that heavy barbell?"
scene gymdaniella07 with dissolve
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
p "What...What are you doing? Your foot... I'm getting a hardon... All the blood pumping to my dick... AAAH!"
da "See, a REAL winner will have to be able to sustain some heavy sexual teasing, the competition is not just about MUSCLES..."
scene gymdaniella08 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
p "RHAAA! I'm cumming uncontrollably!"
$ stamina -=1
show staminaminus01:
    xalign 0.6 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
da "And from the looks of things, you get teased quite easily... You'd better work on that kiddo..."
da "But I'll allow you into the competition, you sure are strong enough for it..."
da "And you also seem to have a great big whopper of a cock... Mmmh..."
$ lust_points[4] +=2
$ score += 2
show lust02:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
$ enteredcompetition = True
$ gymdaniellacum = True
jump GymChoiceThirdDay05

label GymChoiceThirdDay05:
stop music
if (chantellegym05 == True):
    if (gymdaniellacum == True):
        scene chantellegymb
    else:
        scene chantellegym        
    ch "Hi [name], I've arrived!"
    p "Oh, hey Chantelle, I'm glad you came. Isn't this gym great or what?"
    ch "Yeah, I saw they have amazing tanning beds near the entrance."
    if (gymdaniellacum == True):        
        ch "Oh, you look very \"sweaty\"... Maybe you should go and take a shower... (wink). I'll go and work on my tan. See you [name]"
        if (lust_points[2] <= 8):
            $ lust_points[2] +=1
            $ score += 1
            show lust01:
                xalign 0.35 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01                        
        jump GymChoiceThirdbDay05
    ch "I'll actually go and work on my tan now. See you [name]"
    jump GymChoiceThirdbDay05
if (francinegym05 == True):
    scene francinegym
    fa "Hello [name], I've finally made it! I can't wait to see the pole-dancing room!"
    p "Hi Francine, yeah, it's at the back over there. But apparently, men are not allowed in there..."
    fa "Well, if there's no one else around, I might let you in (wink). Enjoy your training, I'm off to work on some dance moves!"
    jump GymChoiceThirdbDay05

label GymChoiceThirdbDay05:
if (hour >= 19):
    p "Damn, it's getting late! I'd better leave and head back home or I'll miss dinner at Anna's place..."
    jump DowntownChoiceDay05b
menu:
    "Go to the lockers" if (gymlockers05 == False):
        jump GymBoyDay05
    "Go to the tanning beds" if ((chantellegym05 == True) or (seentanningbed04 == False)) and (seenchantelletanning == False) and (seentanningbed05 == False):
        jump TanningBedThirdDay05
    "Go to the pole-dancing studio" if (francinegym05 == True) and (seenfrancinegym05 == False):
        jump FrancineGymDay05
    "Leave the gym":
        jump DowntownChoiceDay05b


label TanningBedThirdDay05:
if (chantellegym05 == True):
    $ seenchantelletanning = True
    scene chantelletan01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "(Ooh... Chantelle is about to get on the tanning bed and she conveniently left the door slightly open...)"
    p "(It's amazing how many people forget to close doors on this island really...)"
    menu:
        "Leave, you don't want to get caught":
            p "(While I have a nice view of her sumptuous rump, I should probably leave before she sees me...)"
            jump GymChoiceThirdbDay05
        "Hang around, what could possibly go wrong?":
            jump ChantelleTanning02Day05            
if (seentanningbed04 == False):
    $ seentanningbed05 = True
    scene tanning01 with dissolve
    play sound "Sounds/banging.mp3"
    $ renpy.pause(2.0, hard=True)
    p "Oooh ooh... There's some weird noise coming from that room..."
    p "Seems like someone got stuck under the tanning bed.[name] to the rescue!"
    scene tanning02 with dissolve
    $ renpy.pause(1.0, hard=True)
    da "Thanks for saving me, I was getting burnt in here!"
    $ lust_points[4] +=3
    $ score += 3
    show lust03:
        xalign 0.3 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust03
    p "What happened? How did you end up stuck inside?"
    scene tanning03 with dissolve
    $ renpy.pause(1.0, hard=True)
    da "This is so embarassing, it's the first time it happens... REALLY."
    da "And I'm all naked in front of a customer..."
    p "My only concern was to rescue you Daniella."
    scene tanning03 with dissolve
    $ renpy.pause(1.0, hard=True)
    da "Well, how can I thank you... I'll give you a free pass to the gym for tomorrow, how does that sound?"
    $ freegym06 = True
    p "Sounds like a $5 dollar reward for saving your life..."
    da "Yeah, well, the gym is heavily in debt. I hope that the Muscle Stud competition on Saturday will attract many new female customers..."
    p "I'll be in it!"
    da "I have no doubt. Seeing how muscular and... big down there you are..."
    da "Now I need to put on some fake untan lotion so I don't look like a lobster. Thanks again for saving me [name]!"
    jump GymChoiceThirdbDay05

label ChantelleTanning02Day05:
scene chantelletan02 with dissolve
$ renpy.pause(1.0, hard=True)
p "(Oh yeah, strip for me baby, take that top off!)"
scene chantelletan02b with dissolve
$ renpy.pause(1.0, hard=True)
p "(And now the bottom, please!)"
scene chantelletan03 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Do you realize I could hear everything you said [name]?"
p "(Oh my God, she's a witch, just like Nikki!)"
ch "While I appreciate your insight into my physique, I would really like to have a tanning session... Without being disturbed if you don't mind..."
p "Ah...err... Sure Chantelle, I was only checking on you, the other day, something terrible happened in those tanning beds..."
ch "How thoughtful of you... (wink)"
if (lust_points[2] <=8):
    $ lust_points[2] +=1
    $ score += 1
    show lust01:
        xalign 0.4 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01                
jump GymChoiceThirdbDay05

label GymBoyDay05:
stop music
scene gymboy01 with dissolve
$ renpy.pause(1.0, hard=True)
$ gymlockers05 = True
p "What is going on here? Looks like a young horse-hung muscle stud being serviced by a couple of dykes..."
menu:
    "Leave, this looks like it's going to be NTR-ish and I don't like that one bit!":
        scene gymboy02
        l01 "Yeah, leave us, you're not invited to the party anyway!"
        jump GymChoiceThirdbDay05
    "What the hell, just watch and hope I can join this time (unlikely...)":
        jump GymBoy02Day05

label GymBoy02Day05:
scene gymboy02 with dissolve
$ renpy.pause(1.0, hard=True)
rb "Came to watch how a real stud fucks again?"
menu:
    "Fuck you arsehole! I can have any girl I want too!":
        rb "What do you say girls?"
        l01 "In his dreams! He can watch, but our pussies belong to you daddy!"
        l02 "We can't wait to get rammed by that massive horsecock of yours and covered in ounces of your virile seed!"
        p "Well gee, thanks for the warm welcome girls..."
        menu:
            "Leave, you are not wanted clearly...":
                jump GymChoiceThirdbDay05
            "Stay on, you might get an opportunity somehow...":
                jump GymBoy03Day05
    "No, I'm just bored, that's all.":
        rb "Ha Ha, right, yeah... Well, watch and learn boy. This is part of my training to retain my title as Muscle Stud saturday." 
        rb "I heard you might be competing too, although you have no chance against me, I've been winning this competition three years in a row already!"
        p "Well, you're about to lose your crown dumbass!"
        l01 "Why don't you shut the hell up and make yourself useful by fisting me, I need to have my pussy loosened up for this young stud's monstercock!"
        menu:
            "I'm in for some good old-fashioned fist-fucking!":
                jump GymBoy03Day05
            "Leave, it's starting to sound more and more NTR-ish.":
                jump GymChoiceThirdbDay05
    "And what if I told your girlfriend you fuck behind her back all the time?":
        rb "She knows and she doesn't care. I give it to her a dozen times a day and then she can't take it anymore."
        rb "She understands I need to unload my bloated nuts some more every day...."
        p "(Damn, it does look like this guy is serious competition... I hope he's not going to enter the Muscle Stud challenge.)"
        rb "And anyway, this is part of my training to retain my title as Muscle Stud saturday."
        rb "I heard you might be competing too, although you have no chance against me, I've been winning this competition three years in a row already!"
        p "Well, you're about to lose your crown dumbass!"
        l01 "Why don't you shut the hell up and make yourself useful by fisting me, I need to have my pussy loosened up for this young stud's monstercock!"
        menu:
            "I'm in for some good old-fashioned fist-fucking!":
                jump GymBoy03Day05
            "Leave, it's starting to sound more and more NTR-ish.":
                jump GymChoiceThirdbDay05

label GymBoy03Day05:
$ peeping += 1
scene gymboy03 with dissolve
$ renpy.pause(1.0, hard=True)
l01 "Yeah, that's good, but stick it way up, our stallion's cock is much bigger than simply your fist!"
l02 "Oh fuck, your cock is so big! AAAH, I can't believe I've been missing out on this all these years! Fuck me daddy!"
scene gymboy03b with dissolve
$ renpy.pause(1.0, hard=True)
p "Gee, I can't believe my whole arm is inside her, her hole is a godamn cave! I hope there aren't any thai boys inside..."
l01 "AAAAH! Just keep it there (puff)! Let me get used to it... AAAH!"
l02 "DADDYYYY! You fuck me so good, you're the best! I hope I can take enough inches of your mega-cock to please you daddy!"
p "(Why the fuck are they calling him daddy? I thought they hated daddies...)"
label GymBoy03Day05b:
play sound "Sounds/gymorgy01.mp3"
scene gymboy03 with dissolve
$ renpy.pause(0.3, hard=True)
scene gymboy03b with dissolve
$ renpy.pause(0.3, hard=True)
scene gymboy03 with dissolve
$ renpy.pause(0.3, hard=True)
scene gymboy03b with dissolve
$ renpy.pause(0.3, hard=True)
scene gymboy03 with dissolve
$ renpy.pause(0.3, hard=True)
scene gymboy03b with dissolve
$ renpy.pause(0.3, hard=True)
scene gymboy03 with dissolve
$ renpy.pause(0.3, hard=True)
scene gymboy03b with dissolve
$ renpy.pause(0.3, hard=True)
scene gymboy03
$ renpy.pause(0.5, hard=True)
scene gymboy03b
$ renpy.pause(0.5, hard=True)
scene gymboy03
$ renpy.pause(0.5, hard=True)
scene gymboy03b
$ renpy.pause(0.5, hard=True)
scene gymboy03
$ renpy.pause(0.5, hard=True)
scene gymboy03b
$ renpy.pause(0.5, hard=True)
scene gymboy03
$ renpy.pause(0.5, hard=True)
scene gymboy03b
$ renpy.pause(0.5, hard=True)
scene gymboy03
$ renpy.pause(0.5, hard=True)
scene gymboy03b
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        jump GymBoy03Day05b
    "Move on":
        rb "I'm gonna blow my load again! Get ready to be filled up!"
        scene gymboy03cum with dissolve    
        play sound "Sounds/randyboycumming.mp3"
        $ renpy.pause(3.0, hard=True)
        l02 "Oh my God, it's incredible Rosie, I can feel every massive cumshot hosing my insides!"
        l01 "I can't wait for my turn, I want some of daddy's sweet cum too!"
        p "Why don't you take mine instead, it's even sweeter..."
        l01 "Shut up useless boy! Just keep wriggling your fist inside of me to warm me up for daddy's giant dong!"
        scene gymboy03d with dissolve    
        play sound "Sounds/randyboycumming.mp3"
        $ renpy.pause(3.0, hard=True)
        l01 "Sweet Ellen de Generes! He's covering her in ounces of scalding spunk! I wanna taste it Daddy, please!"
        window hide
        play sound "Sounds/randyboycumming.mp3"
        $ renpy.pause(3.0, hard=True)
        rb "No problem, a dozen massive streamers coming your way! AAH!"
        l01 "Thank you daddy! Now come and fuck my gaping pussy, I need that monster dong in me now, I can't stand it daddy!"
        l02 "Yeah, do it stud, she deserves it, she's been a good girl, just like me!"
        rb "Of course, get on your back and stick your arse up, daddy is coming home!"
        jump GymBoy04Day05

label GymBoy04Day05:
scene gymboy04 with dissolve    
$ renpy.pause(1.0, hard=True)
p "Hey, what about you, how about you give me a blowjob or something?"
scene gymboy04b with dissolve    
$ renpy.pause(1.0, hard=True)
l02 "How about you go fuck yourself? I'm busy gulping down the huge amount of nutjuice this super-stud plastered me with, I have no time for you boy!"
l01 "Oh damn, daddy! Your thingie is so massive! I'm gonna cum in no time! AAAAH!"
rb "There's more where that came from!"
label GymBoy04Day05b:
play sound "Sounds/gymorgy02.mp3"   
scene gymboy05 with dissolve    
$ renpy.pause(0.3, hard=True)
scene gymboy05b with dissolve    
$ renpy.pause(0.3, hard=True)
scene gymboy05 with dissolve    
$ renpy.pause(0.3, hard=True)
scene gymboy05b with dissolve    
$ renpy.pause(0.3, hard=True)
scene gymboy05 with dissolve    
$ renpy.pause(0.3, hard=True)
scene gymboy05b with dissolve    
$ renpy.pause(0.3, hard=True)
scene gymboy05 with dissolve    
$ renpy.pause(0.3, hard=True)
scene gymboy05b with dissolve    
$ renpy.pause(0.3, hard=True)
scene gymboy05 with dissolve    
$ renpy.pause(0.3, hard=True)
scene gymboy05b with dissolve    
$ renpy.pause(0.3, hard=True)
scene gymboy05
$ renpy.pause(0.3, hard=True)
scene gymboy05b
$ renpy.pause(0.3, hard=True)
scene gymboy05
$ renpy.pause(0.3, hard=True)
scene gymboy05b
$ renpy.pause(0.3, hard=True)
scene gymboy05
$ renpy.pause(0.3, hard=True)
scene gymboy05b
$ renpy.pause(0.3, hard=True)

menu:
    "Repeat":
        jump GymBoy04Day05b
    "Move on":
        scene gymboy05c with dissolve
        play sound "Sounds/randyboycumming.mp3"
        $ renpy.pause(2.0, hard=True)
        l01 "Yes, YES, fill me up a like a sperm tank Daddy!!!!"
        window hide
        play sound "Sounds/randyboycumming.mp3"
        $ renpy.pause(2.0, hard=True)
        rb "I am, I'm spewing my sauce non-stop inside your gaping hole!"
        l02 "It's already starting to leak out like a fire hydrant at full blast! What a mega-load!"
        p "Pff, I can come just as much..."
        l01 "Watch and shut your mouth! AAAH, cover us with the rest of your massive pellets of seed daddy!"
        rb "No problems, get on your knees and open your mouths REAL wide! Dinner is being served!"
        scene gymboy06 with dissolve
        play sound "Sounds/randyboycumming.mp3"
        $ renpy.pause(2.0, hard=True)
        l02 "Oh my God daddy, you're drowning us in your thick cream! I want to drink your cum for the rest of my life!"
        l01 "Me too, me too daddy, I NEED that sweet slush inside my stomach 24 hours a day!"
        rb "I'll give you enough to keep you bloated with it for days, don't worry! Now get back on the bench, I'm gonna pummel your arses for another hour or so..."
        p "While I would love to watch, I've got more important things to do... Like actually fucking girls. So I shall bid you farewell lezzies... errr, I mean ladies!"
        $ hour +=1
        $ stamina += 1
        window hide
        show stamina01:
            xalign 0.4 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide stamina01
        jump GymChoiceThirdbDay05
        
label FrancineGymDay05:
$ seenfrancinegym05 = True
scene francinepole04 with dissolve
play music "Sounds/haton.mp3"
$ renpy.pause(1.0, hard=True)
fa "Oh, there you are! You've decided to come and see my pole-dancing moves..."
p "Sure, you're the best pole-dancer I've ever seen!"
fa "That's nice of you to say... I'm not finished yet... Watch carefully..."
scene francinepole01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn..."
scene francinepole02 with dissolve
$ renpy.pause(1.0, hard=True)
menu:
    "I've got a big pole you could dance with right now Francine!":
        scene francinepole07 with dissolve
        $ renpy.pause(1.0, hard=True)
        fa "What? That's disgusting! Pole-dancing is an ART, not SMUT! Now get out of here!"        
        $ lust_points[7] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.5 yalign 0.4
            linear 1.0 yalign 0.6
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        p "Apparently, my witty humor doesn't work on everyone..."
        jump GymChoiceThirdbDay05
    "You turn pole-dancing into an art!":
        fa "Well, it IS an art actually..."
        p "Of course, but you elevate it to something subliminal... Since your body is a work of art itself..."
        $ lust_points[7] += 1
        $ score += 1
        show lust01:
            xalign 0.5 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        if (lust_points[7] >=10):
            stop music
            window hide
            show epiclust:
                xalign 0.5 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust
            jump FrancineGym02Day05
        fa "Thank you for such a nice compliment [name]!"
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (lust_points[7] >=8):
                jump FrancinePendulumDay05
            "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[7] >=8):
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump FrancinePheromonesDay05
            "Well, I'd better leave you finish off your dance routine and get back to the gym...":
                fa "Bye [name], thanks again for inviting me!"
                $ hour += 1
                jump GymChoiceDay05  
            "I've got a big pole you could dance with right now Francine!":
                scene francinepole07 with dissolve
                $ renpy.pause(1.0, hard=True)
                fa "What? That's disgusting! Pole-dancing is an ART, not SMUT! Now get out of here!"        
                $ lust_points[7] -= 1
                $ score -= 1
                show lustminus01:
                    xalign 0.5 yalign 0.4
                    linear 1.0 yalign 0.6
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
                p "Apparently, my witty humor doesn't work on everyone..."
                jump GymChoiceThirdbDay05
        
label FrancinePendulumDay05:
stop music
scene francinehypno with dissolve
show pendulum03
$ renpy.pause(1.0, hard=True)
p "Just watch this pendulum as I wiggle it in front of your eyes Francine..."
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
if (lust_points[7] ==8):
    window hide
    $ lust_points[7] += 2
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
    jump FrancineGym02Day05
if (lust_points[7] ==9):
    window hide
    $ lust_points[7] += 1
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
    jump FrancineGym02Day05

label FrancinePheromonesDay05:
stop music
scene francinepheromone with dissolve
$ pheromone = False
play sound "Sounds/sniffing.mp3"
$ renpy.pause(1.0, hard=True)
fa "What's that enticing smell?... That's turning me into a primal beast of lust..."
p "Bingo, it worked! But my spray is now empty... I guess I won't be able to use it again."
show pheromone
show square
play sound "Sounds/lost.mp3"
"You lost a pheromone spray."
hide square
hide pheromone
$ pheromone = False
if (lust_points[7] ==8):
    window hide
    $ lust_points[7] += 2
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
    jump FrancineGym02Day05
if (lust_points[7] ==9):
    window hide
    $ lust_points[7] += 1
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
    jump FrancineGym02Day05

label FrancineGym02Day05:
stop music
fa "Tell me what you think of THIS art!"
scene francinepole05 with dissolve
$ renpy.pause(1.0, hard=True)
fa "Like so..."
p "Damn, she's doing it half-naked now!"
scene francinepole05 with dissolve
$ renpy.pause(1.0, hard=True)
fa "I LOVE holding onto big POLES like that... Do you have one for me [name]?"
p "Fuck yeah! Let me show you MY pole!"
scene francinepole06 with dissolve
play sound "Sounds/francinefuck01.mp3"
$ renpy.pause(3.0, hard=True)
fa "Oh my, that pole is even thicker than a pole-dancing pole! I can't wait for you to FUCK me!"

label FrancineFuckChoiceDay05:
scene francineprefuck with dissolve
$ renpy.pause(1.0, hard=True)
fa "I'm ready when you are!"
menu:
    "Well, I'm ready to facefuck your mouth then! Get on your knees." if (francineblow == False):
        fa "I hope my mouth can stretch enough to take on THAT monster..."
        jump FrancineBlowDay05
    "Hold on to the pole, I'm gonna fuck you from behind!" if (francinedoggy == False):
        fa  "Ooh, I LOVE that idea!"
        jump FrancineDoggyDay05
    "Let's make sweet love on the floor." if (francineground == False):
        fa "I hope not TOO sweet... My pussy wants a good pounding (wink)."
        p "Yeah, don't worry about it, just get on board for starters..."
        jump FrancineGroundDay05
    "I'm ready to blow anytime now, do something Francine!" if (francineblow == True) and (francinedoggy == True) and (francineground == True):
        fa  "I know exactly what to do... Double-handed monstercock handjob it is!"
        jump FrancineMovieDay05

label FrancineBlowDay05:
$ francineblow = True
scene francineblow01 with dissolve
play sound "Sounds/francinefuck02.mp3"
$ renpy.pause(3.0, hard=True)
p "Easy...Open wide..."
fa "Mmmm, ggglll..."
scene francineblow02 with dissolve
$ renpy.pause(1.0, hard=True)
p "And your throat now... Wider, wider! Aah, this feels good!"
label FrancineBlowDay05b:
play music "Sounds/hallesuck02.mp3"
scene francineblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene francineblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene francineblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene francineblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene francineblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene francineblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene francineblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene francineblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene francineblow01
$ renpy.pause(0.3, hard=True)
scene francineblow02
$ renpy.pause(0.3, hard=True)
scene francineblow01
$ renpy.pause(0.3, hard=True)
scene francineblow02
$ renpy.pause(0.3, hard=True)
scene francineblow01
$ renpy.pause(0.3, hard=True)
scene francineblow02
$ renpy.pause(0.3, hard=True)
scene francineblow01
$ renpy.pause(0.3, hard=True)
scene francineblow02
$ renpy.pause(0.3, hard=True)
scene francineblow01
$ renpy.pause(0.3, hard=True)
scene francineblow02
$ renpy.pause(0.3, hard=True)
scene francineblow01
$ renpy.pause(0.3, hard=True)
scene francineblow02
$ renpy.pause(0.3, hard=True)
scene francineblow01
$ renpy.pause(0.3, hard=True)
scene francineblow02
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        jump FrancineBlowDay05b
    "Move on":
        pass
fa "Gaaa gaaa, I think... my jaw... is dislocated..."
p "Never mind that, it will get back to normal soon, let's switch position!"
jump FrancineFuckChoiceDay05

label FrancineDoggyDay05:
$ francinedoggy = True
scene francinefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
fa "Oh fuck, FUCK! Give it to me [name]"
p "No problemo. Get ready, set, GO!"
scene francinefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
fa "AAAOUUW, FUCK it hurts! But it's so good! Do it again, please!"
label FrancineDoggyDay05b:
scene francinefuck02 with dissolve
play music "Sounds/francinefuck04.mp3"
$ renpy.pause(0.3, hard=True)
scene francinefuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck01
$ renpy.pause(0.3, hard=True)
scene francinefuck02
$ renpy.pause(0.3, hard=True)
scene francinefuck01
$ renpy.pause(0.3, hard=True)
scene francinefuck02
$ renpy.pause(0.3, hard=True)
scene francinefuck01
$ renpy.pause(0.3, hard=True)
scene francinefuck02
$ renpy.pause(0.3, hard=True)
scene francinefuck01
$ renpy.pause(0.3, hard=True)
scene francinefuck02
$ renpy.pause(0.3, hard=True)
scene francinefuck01
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        jump FrancineDoggyDay05b
    "Move on":
        pass    
fa "That was the best pole-dancing workout I ever got!"
p "My pole sure did give you a workout! Let's do something else now."
jump FrancineFuckChoiceDay05    

label FrancineGroundDay05:
$ francineground = True
scene francinefuck05 with dissolve
play sound "Sounds/francinefuck03.mp3"
$ renpy.pause(1.0, hard=True)
fa "My God, look at that log, it's distending my belly! I can't sit up anymore, it's just...too...good..."
p "Ok, I'm gonna spoon you from the side then, get on the floor and spread those fine tanned legs for me..."
scene francinefuck03 with dissolve
$ renpy.pause(1.0, hard=True)
fa "Oh yeah, that's better... Does your cock feel snug and warm inside my little pussy [name]!"
p "It sure does Francine...  But there are too many inches exposed to the cold outside air..."
scene francinefuck04 with dissolve
play sound "Sounds/francinefuck06.mp3"
$ renpy.pause(3.0, hard=True)
fa "...AAH! YES! AAAH!"
label FrancineGroundbDay05b:
scene francinefuck03 with dissolve
play sound "Sounds/francinefuck05.mp3"
$ renpy.pause(0.3, hard=True)
scene francinefuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck03 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck03 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck03 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck03 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck03 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck04 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck03 with dissolve
$ renpy.pause(0.3, hard=True)
scene francinefuck04
$ renpy.pause(0.3, hard=True)
scene francinefuck03
$ renpy.pause(0.3, hard=True)
scene francinefuck04
$ renpy.pause(0.3, hard=True)
scene francinefuck03
$ renpy.pause(0.3, hard=True)
scene francinefuck04
$ renpy.pause(0.3, hard=True)
scene francinefuck03
$ renpy.pause(0.3, hard=True)
scene francinefuck04
$ renpy.pause(0.3, hard=True)
scene francinefuck03
$ renpy.pause(0.3, hard=True)
scene francinefuck04
$ renpy.pause(0.3, hard=True)
scene francinefuck03
$ renpy.pause(0.3, hard=True)
scene francinefuck04
$ renpy.pause(0.3, hard=True)
scene francinefuck03
$ renpy.pause(0.3, hard=True)
stop sound
menu:
    "Repeat":
        jump FrancineGroundbDay05b
    "Move on":
        pass    
fa "My pussy is creaming all over the place..."
p "My cock needs a good cleaning then, let's think of another position shall we?" 
jump FrancineFuckChoiceDay05    

label FrancineMovieDay05:
fa "You'll see, my hands will milk a huge load straight out of that cum-cannon!"
play music "Sounds/francinefuckmovie.mp3"
show francinefuckslow
show faster
call screen francineslowfuckday05
screen francineslowfuckday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FrancineFastFuckDay05")

label FrancineFastFuckDay05:
stop music
hide faster
play music "Sounds/francinefuckmovie.mp3"
show francinefuckfast
show cum
call screen francinefastfuckday05
screen francinefastfuckday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FrancineCumDay05")

label FrancineCumDay05:
hide francinefuckfast
hide francinefuckslow
stop music
scene francinecum01
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
fa "There you go... Shoot it all out [name]!"
p "Fuck, don't stop tugging on it, there's more coming out!"
scene francinecum02 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
fa "Ooh, you're right, my soft hands are really draining your nuts, aren't they?"
scene francinecum01 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
fa "Look at all those fat ropes of semen spewing out of your horsecock! Wow!"
p "God, you sure give the best handjobs around Francine..."
if (tanyafucked == True) and (debbyfucked == True) and (teaganfucked == True) and (achievement.has("king") == False):
    show achievement13:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement13
    $ achievement.grant("king")
fa "I'm always happy to lend a hand... Now, let's get cleaned up before someone else arrives..."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.6 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
if (francinejosewin == False):
    p "(She didn't notice I took a picture of us fucking earlier on... Now I'll send it to José)."
    $ francinewin = True 
$ francinefucked = True
$ hour += 1
jump GymChoiceThirdbDay05

label AudaciousOffice01Day05:
$ seenaudaciousday05 = True
stop music
play sound "Sounds/liftsound.mp3"
if (stolecamera == True):
    scene secretaryangry with dissolve
    $ renpy.pause(1.0, hard=True)
    st "Hey, YOU! You stole a camera that was property of this company! Give it back immediately or I'm calling the cops!"
    menu:
        "Give her the camera":
            p "I simply forgot to give it back the other day, no big deal..."
            st "Humpf, I find that hard to believe but I'll give you the benefit of the doubt."
            show camera
            show square
            play sound "Sounds/lost.mp3"
            "You relinquish a digital camera. Yes, that's right, \"relinquish\". Look it up in the dictionary."
            hide square
            hide camera
            $ stolecamera = False
            $ camera = False            
            jump AudaciousOffice01Day05b
        "Yeah, go ahead, I'm not scared, I ain't done nuffin wrong!":
            $ stolecamera = False
            st "That's it, you're done for mister!"
            jump AudaciousCopDay05
if (stolecamera == False):
    jump AudaciousNoCopDay05

label AudaciousCopDay05:
$ audacioustried = True
scene audaciouscop01 with dissolve
$ renpy.pause(1.0, hard=True)
co"What seems to be the matter?"
st "This boy stole a camera from us! He tricked me into believing he was a photographer!"
co"That's it, follow me to the police station immediately!"
if (wenttojail == True):
    p "What? Not AGAIN! Damn, it's pretty easy to accuse people in this country and get them arrested. Good thing I'm not black."
    jump AudaciousCop02Day05
p "What for? This accusation is grotesque, why don't you search me?"
"The cop searches you and finds the camera."
p "Aaaah, THAT camera! You guys should have said it earlier..."
show camera
show square
play sound "Sounds/lost.mp3"
"You lost a digital camera."
hide square
hide camera
$ camera = False    
co"You're not fooling anybody, follow me NOW!"

label AudaciousCop02Day05:
stop music
play music "Sounds/policesound.mp3"
$ hour +=1 
$ wenttojail02 = True

scene audaciouscop02 with dissolve
$ renpy.pause(1.0, hard=True)
co"So, into \"photography\" are we?"
p "Yeah. Is there a law against that?"
co"Shut up and get undressed NOW!"
p "What???"
co"You heard me! You're into photography, let's see how YOU like to get photographed NAKED IN A JAIL!"
p "This is outrageous, I want it to be entered into the record that I am showing you my giant schlong under duress!"
co"Quit the bragging and quit the pants!"
scene audaciouscop03 with dissolve
$ renpy.pause(1.0, hard=True)
co"Damn boy, quite the truncheon you're carrying there... I... didn't expect this."
menu:
    "I always carry a loaded weapon on me.":
        co"Is that so, funny boy? Let's see how much ammunition you've got there then..."
        co"I'll open the door, don't do anything silly or I'll tase you..."
        jump CopFuckBlowDay05
    "Let me out of here or I'll report you for police brutality!":
        co"And you really think anyone will believe you? We can either do this MY way or we'll do this the HARD way!"
        co"Now I'll open the door, don't do anything silly or I'll tase you..."
        jump CopFuckDay05
    "Now that you've seen my massive dong, get on your knees and suck it bitch!":
        co"I don't take orders from a BOY! Even if he's carrying more meat than any man I've ever seen... As a punishment, I'll let you rot in this cell a while longer!"
        jump CopNoFuckDay05
        
        
label CopNoFuckDay05:
scene black with dissolve
$ renpy.pause(1.0, hard=True)
p "Noooo! I need to fuck girls to win and I can't fuck any here!... When will this nightmare end?"
$ lustaddedB = 2
call Challenger from _call_Challenger_74
$ lustaddedB = 2
call Challenger from _call_Challenger_75
$ lustaddedB = 2
call Challenger from _call_Challenger_76
$ lustaddedB = 2
call Challenger from _call_Challenger_77
$ challengercalls += 4
$ hour = 21
scene audaciouscop02 with dissolve
$ renpy.pause(1.0, hard=True)
co"So, have you calmed down now, BOY?"
p "Let me out of here, I beg you!"
co"Alright, but I'd better not see you again EVER!"
co"Oh, and your landlady is waiting for you outside in her car... Good luck explaining to her why you ended up in jail, HA HA!"
stop music
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
        $ pocketmoney2 = True
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
        jump EveningChoiceDay05
    "They brutalized me mommy, and they threw me in a dirty cell for hours....sniff...":
        show jailmom01b
        m "Oh, sweetie, this is terrible... Let's go home and try and forget about this... Stay out of trouble and everything will be fine..."
        $ hour += 1
        stop music
        jump EveningChoiceDay05

label CopFuckBlowDay05:
scene copblow01 with dissolve
$ renpy.pause(1.0, hard=True)
co"First, you are going to unload that weapon down my throat! And you'd better be quick!"
if (stamina <= 0) and (whitebull == True):
    co"What's wrong? You can't deliver?"
    p "Err... I'm kind of tired, you know, busy busy day and all that...(Shit, she took all my belongings and I can't even drink a White Bull...)"
    co"Is that so? Then, I'll make your day less busy by locking you up in this cell until this evening, limp dick!"
    jump CopNoFuckDay05

if (stamina <= 0):
    co"What's wrong? YOu can't deliver?"
    p "Err... I'm kind of tired, you know, busy busy day and all that..."
    co"Is that so? Then, I'll make your day less busy by locking you up in this cell until this evening, limp dick!"
    jump CopNoFuckDay05

label CopFuckBlowDay05b:
scene copblow02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Alright! (Although I have the feeling I'm gonna lose a lot of stamina here today...)"
play sound "Sounds/hardsucking.mp3"
scene copblow03
$ renpy.pause(0.5, hard=True)
scene copblow02
$ renpy.pause(0.5, hard=True)
scene copblow03
$ renpy.pause(0.5, hard=True)
scene copblow02
$ renpy.pause(0.5, hard=True)
scene copblow03
$ renpy.pause(0.5, hard=True)
scene copblow02
$ renpy.pause(0.5, hard=True)
scene copblow03
$ renpy.pause(0.5, hard=True)
scene copblow02
$ renpy.pause(0.5, hard=True)
scene copblow03
$ renpy.pause(0.5, hard=True)
scene copblow02
$ renpy.pause(0.5, hard=True)
scene copblow03
$ renpy.pause(0.5, hard=True)
scene copblow02
$ renpy.pause(0.5, hard=True)
p "FUUUUCK! Her lips are sucking the life out of me, I'm gonna CUUUMM!"
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
scene copblowcum with dissolve
$ renpy.pause(1.0, hard=True)
if (stamina >= 2):
    window hide
    $ stamina -= 1
    show staminaminus01:
        xalign 0.4 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01

co"That was good, my belly is full and my tits are covered in your sticky cum..."
co"Now you'd better stay hard so I can get a ride on that fat truncheon."
p "No worries officer, spread your legs and my mighty lovepole will deliver!"
label CopFuckDay05:
scene copfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
co"That's it, MY way, nice and slow, I want it DEEP!"
scene copfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
p "My God, her pussy is so tight, she's gonna milk me in no time!"
co"That's right, I want a nice big fat load sloshing around inside me, get it boy?"
play music "Sounds/randybeachchickmoaning.mp3"
scene copfuck01
$ renpy.pause(0.5, hard=True)
scene copfuck02
$ renpy.pause(0.5, hard=True)
scene copfuck01
$ renpy.pause(0.5, hard=True)
scene copfuck02
$ renpy.pause(0.5, hard=True)
scene copfuck01
$ renpy.pause(0.5, hard=True)
scene copfuck02
$ renpy.pause(0.5, hard=True)
scene copfuck01
$ renpy.pause(0.5, hard=True)
scene copfuck02
$ renpy.pause(0.5, hard=True)
scene copfuck01
$ renpy.pause(0.5, hard=True)
scene copfuck02
$ renpy.pause(0.5, hard=True)
scene copfuck01
$ renpy.pause(0.5, hard=True)
scene copfuck02
$ renpy.pause(0.5, hard=True)
scene copfuck01
$ renpy.pause(0.5, hard=True)
scene copfuck02
$ renpy.pause(0.5, hard=True)
stop music
scene copfuckcum01 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
co"Yeah, dump that load inside me, give me everything you've got stud!"
p "Fuck, I'm getting totally drained! AAAH"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
scene copfuckcum02 with dissolve
play sound "Sounds/ryancumming.mp3"
$ hour += 1
co"You did good, my legs are numb, now you can go..."
p "This looks like a crime scene. A SEX crime scene... I'd better get the hell out of here..."
$ extras +=1
if (wenttojail == True):
    show achievement08:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement08
    $ achievement.grant("lawbreaker")
jump DowntownChoiceDay05b

label AudaciousNoCopDay05:
scene secretary01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I think I'm on the corporate floor..."
label AudaciousOffice01Day05b:
scene secretary01 with dissolve
st "How may I help you?"
menu:
    "Where's the CEO's office?" if (debbyofficeseen == False) and (debbyofficeseen05 == False):
        st "Do you have an appointment?"
        p "Err... Yeah, sure, I'm a big time swimwear buyer, I need to sign a contract with her."
        scene secretary04 with dissolve
        $ renpy.pause(1.0, hard=True)
        st "Alright, it's down the hallway on your right..."
        p "Well thank you. (That was easy...)"
        jump DebbyOffice01Day05
    "I'm a photographer. Nudge nudge, wink wink." if (hour <=18) and (seenshoot03 == False) and (seenshoot05 == False):
        scene secretary03 with dissolve
        $ renpy.pause(1.0, hard=True)
        st "Oh, yes, we were expecting you mr... let's see... Hank? You're late!"
        st "Take this camera and go to modelling room 4B, Angelina Jolly is waiting for you!"
        p "(Angelina Jolly? The famous pornstar? Wow, cool...) Sure ma'am, I'm on my way."
        $ camera = True
        show camera
        show square
        play sound "Sounds/found.mp3"
        "You acquired a digital camera."
        hide camera
        hide square
        jump Shoot01Day05
    "A receptionist needs good oral skills. Let me test yours...":
        scene secretary02 with dissolve
        $ renpy.pause(1.0, hard=True)
        st "Quit it cowboy, I ain't falling for that...."
        jump AudaciousOffice01Day05b
    "Leave the building":
        jump DowntownChoiceDay05b
    "Look for mom's office" if (seenmomofficeday05 == False):
        jump MomOffice01Day05

label Shoot01Day05:
$ seenshoot05 = True
scene preshoot01 with dissolve
$ renpy.pause(1.0, hard=True)
aj "Ah, there you are, you're late! I HATE waiting!"
p "Sorry Ms Jolly. Traffic..."
scene preshoot03 with dissolve
$ renpy.pause(1.0, hard=True)
aj "That's a lousy excuse! Don't you have a chauffeur to drive you around?"
p "Of course, but he called in sick this morning. Now let's get the show rolling shall we?"
aj "Well since you were late, I already put on the swimwear I'm supposed to use for the shoot."
p "Perfect, now let's move to the studio area, the lights are all set and my camera is ready!"

label Shoot02Day05:
scene shoot01 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/flash.mp3"
scene shoot01 with flash
aj "Hey, wait for me to pose before taking pictures!"
p "Ah, sorry, I pressed the button by mistake."
aj "You really don't seem professional at all. And very young to boot..."

scene shoot02 with dissolve
$ renpy.pause(1.0, hard=True)
aj "Now you can take a picture..."
play sound "Sounds/flash.mp3"
scene shoot02 with flash
aj "So what should I do next?..."
menu:
    "Hold that big banana.":
        aj "Oh, I see, that's the plan then hey?..."
        jump Shoot03Day05
    "Show us ya tits.":
        aj "That was fast... Well, you're the photographer, you know what to do."
        scene shoot03 with dissolve
        $ renpy.pause(1.0, hard=True)
        aj "Like that?..."
        p "Yeah, hold it..."
        play sound "Sounds/flash.mp3"
        scene shoot03 with flash
        p "Now there's a need for a big fat cock in the picture... You know, to sell more bikinis to horny women."
        aj "What? Are you out of your mind? I'm paid for a bikini shoot, not a porn scene! I'm outta here!"
        p "But... You're a pornstar!"
        aj "It doesn't mean I'm a cheap whore! Who the fuck do you think you are, Harvey Weinstein?"
        p "Shit... Apparently, you can also come on too strong on a pornstar... I'd better get out of here before she tells everyone what a tool I am."
        jump AudaciousEscapeDay05

label Shoot03Day05:
scene shoot04 with dissolve
$ renpy.pause(1.0, hard=True)
p "Yes, that's nice, let me take a few photos..."
play sound "Sounds/flash.mp3"
scene shoot04 with flash
aj "OOh, look at my big banana... Ha ha , this photoshoot is so much fun. You're full of surprises Mr Hank..."
p "Err, yeah, thanks Miss Jolly. Now sit on the inflatable island and straddle the banana."
aj "OMG, who are you trying to sell this bikini to, this is ssoo risqué! (wink)"
scene shoot05 with dissolve
$ renpy.pause(1.0, hard=True)
p "Yeah, perfect Miss Jolly."
play sound "Sounds/flash.mp3"
scene shoot05 with flash
aj "You can call me Angelina ...mister... photographer..."
p "The name's Hank. Nicknamed Hank the Crank."
aj "Ooh, and why is that?..."
p "You'll find out soon enough..."
aj "I can't wait... I'm so horny right now..."
p "Then why don't you pretend that you're sucking on the tip of that banana..."
aj "What a devilish idea Hank..."
scene shoot06 with dissolve
$ renpy.pause(1.0, hard=True)
aj "God, I can't stand it, you make me do such naughty things..."
play sound "Sounds/flash.mp3"
scene shoot06 with flash
p "How about you show some nipples?"
aj "That sounds very raunchy for a billboard campaign Mr Hank-the-Crank..."
p "It's for my personal collection..."


scene shoot07 with dissolve
$ renpy.pause(1.0, hard=True)
aj "You're a dirty boy aren't you?"
p "Oh yeah... I've seen your movies, you're a dirty girl too..."
play sound "Sounds/flash.mp3"
scene shoot07 with flash
aj "Ooh, and what particular scene caught your attention Hank?"
menu:
    "The anal scene with that horse-hung pornstar.":
        aj "Mmh, yeah, Mandingo really pounded my arse that day... I was butt-sore for three days after that..."
        p "I can pound that arse ten times harder with my massive pole..."
        aj "Well, if that's true, it doesn't sound like something I'm willing to experience young man..."
        aj "Let's wrap up this photoshoot, you can jerk off to those photos afterwards filthy boy."
        p "What? But... I'm like totally bursting through my pants!"
        aj "Too bad, I'm paid for a bikini photoshoot, not for sucking your cock..."
        jump EndShootDay05

    "The gangbang scene with ten men.":
        aj "Nothing like a bukkake session with tons of cum plastering my huge breasts..."
        p "Well I'm a bukkake machine all by myself..."
        scene shoot08 with dissolve
        $ renpy.pause(1.0, hard=True)
        aj "Is that so? I demand some proof Mr Hank..."
        p " Sure thing, I'll offer you ounces of proof...."
        aj "Mmh, such devotion to your job mr photographer... Bring that crank over here then..."
        jump ShootFuckDay05

    "The scene with the amateur fan.":
        aj "Yes, that was tons of fun. The poor sod was so worried at first, but he gained confidence and then pounded me just as hard as a veteran pornstar."
        scene shoot08 with dissolve
        $ renpy.pause(1.0, hard=True)
        aj "Too bad there isn't someone like him right here... I'm so horny..."
        p "I can volunteer... I'm a major fan myself..."
        aj "Mmh, such devotion to your job mr photographer... Bring that crank over here then..."
        jump ShootFuckDay05


label ShootFuckDay05:
stop music
scene shoot09 with dissolve
$ renpy.pause(1.0, hard=True)
aj "Damn kid, that's the biggest \"crank\" I've ever seen and I've seen hundreds of pornstar dongs!"
p "Enough talking, put that mouth to good use and gobble my shaft as deep as you can!"
aj "I'll try..."
label ShootFuckMouthDay05:
scene shoot10 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/hardsucking.mp3"
scene shoot11 with dissolve
$ renpy.pause(0.2, hard=True)
scene shoot10 with dissolve
$ renpy.pause(0.2, hard=True)
scene shoot11 with dissolve
$ renpy.pause(0.2, hard=True)
scene shoot10 with dissolve
$ renpy.pause(0.2, hard=True)
scene shoot11 with dissolve
$ renpy.pause(0.2, hard=True)
scene shoot10 with dissolve
$ renpy.pause(0.2, hard=True)
scene shoot11 with dissolve
$ renpy.pause(0.2, hard=True)
scene shoot10 with dissolve
$ renpy.pause(0.3, hard=True)
scene shoot10
$ renpy.pause(0.3, hard=True)
scene shoot11
$ renpy.pause(0.3, hard=True)
scene shoot10
$ renpy.pause(0.3, hard=True)
scene shoot11
$ renpy.pause(0.3, hard=True)
scene shoot10
$ renpy.pause(0.3, hard=True)
scene shoot11
$ renpy.pause(0.3, hard=True)
scene shoot10
$ renpy.pause(0.3, hard=True)
scene shoot11
$ renpy.pause(0.3, hard=True)
scene shoot10
$ renpy.pause(0.3, hard=True)
scene shoot11
$ renpy.pause(0.3, hard=True)
scene shoot10
$ renpy.pause(0.3, hard=True)
scene shoot11
$ renpy.pause(0.3, hard=True)
scene shoot10
$ renpy.pause(0.3, hard=True)
scene shoot11
$ renpy.pause(0.3, hard=True)

stop sound
menu:
    "Repeat":
        jump ShootFuckMouthDay05
    "Move on":
        pass

label ShootFuckPussyDay05:
p "You're doing good. Not many girls can gobble up my monster dong like that!"
aj "I'm not the winner of \"Pornstar Mouth of the Year\" five years in a row for nothing Mr Hank!"
p "Let's test your \"Pornstar Pussy of the Year\" then..."
aj "Ok, but be caref....."
scene shoot12 with dissolve
$ renpy.pause(1.0, hard=True)
aj "AAAH, You're going ssooo deep! Yes, I want more, pound that pussy, I'm creaming all over that giant cock!!!"
label ShootFuckPussyDay05b:
play music "Sounds/angelinafuck.mp3"
scene shoot13 with dissolve
$ renpy.pause(0.3, hard=True)
scene shoot12 with dissolve
$ renpy.pause(0.3, hard=True)
scene shoot13 with dissolve
$ renpy.pause(0.3, hard=True)
scene shoot12 with dissolve
$ renpy.pause(0.3, hard=True)
scene shoot13 with dissolve
$ renpy.pause(0.3, hard=True)
scene shoot12 with dissolve
$ renpy.pause(0.3, hard=True)
scene shoot13 with dissolve
$ renpy.pause(0.3, hard=True)
scene shoot12 with dissolve
$ renpy.pause(0.3, hard=True)
scene shoot12
$ renpy.pause(0.3, hard=True)
scene shoot13
$ renpy.pause(0.3, hard=True)
scene shoot12
$ renpy.pause(0.3, hard=True)
scene shoot13
$ renpy.pause(0.3, hard=True)
scene shoot12
$ renpy.pause(0.3, hard=True)
scene shoot13
$ renpy.pause(0.3, hard=True)
scene shoot12
$ renpy.pause(0.3, hard=True)
scene shoot13
$ renpy.pause(0.3, hard=True)
scene shoot12
$ renpy.pause(0.3, hard=True)
scene shoot13
$ renpy.pause(0.3, hard=True)
scene shoot12
$ renpy.pause(0.3, hard=True)
scene shoot13
$ renpy.pause(0.3, hard=True)
scene shoot12
$ renpy.pause(0.3, hard=True)
scene shoot13
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        jump ShootFuckPussyDay05b
    "Move on":
        pass
p "I'm cumming! RHAAA!"
scene shoot14 with dissolve
play sound "Sounds/angelinaend.wav"
$ renpy.pause(2.0, hard=True)
aj "YES! Keep pumping that load, I want OUNCES of your red-hot boycum!"
scene shoot15 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(3.0, hard=True)
$ extras += 1
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.4
    linear 1.0 yalign 0.6
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ hour += 1
aj "Damn boy, you truly are a bukkake machine! Now I have to get cleaned up, I'm caked in semen..."
scene shootend with dissolve
$ renpy.pause(1.0, hard=True)
aj "I have a porn shoot this afternoon and I'm not sure I'll be able to feel my partner's rod this time... You've stretched me so much...."
p "Hank the Crank at your service ma'am!"
p "SHHHIIIT, I forgot to put the timer on! I can't send José any pic of the deed... What a missed opportunity..."

label EndShootDay05:
$ stolecamera = True
scene secretary06 with dissolve
$ renpy.pause(1.0, hard=True)
p "Let's just walk nonchalantly past the receptionist, I want to keep that camera to myself, it could be handy..."
play sound "Sounds/whistling.mp3"
$ renpy.pause(2.0, hard=True)
scene downtownaudacious with dissolve
play music "Sounds/downtown.mp3"
$ renpy.pause(1.0, hard=True)
p "Pfew, I managed to get out of the building..."
jump DowntownChoiceDay05b

label AudaciousEscapeDay05:
scene secretary05 with dissolve
$ renpy.pause(1.0, hard=True)
st "And where exactly do you think you're going Mr \"Hank\", if that is your real name, which I highly doubt!"
p "Err... I forgot some shooting equipment in my car, I'll be back in a minute."
st "Enough with the bullshit. Give me the camera back, it's property of \"Audacious Inc.\" and get the hell out of this building or I'll call security!"
show camera
show square
play sound "Sounds/lost.mp3"
"You give the camera back to its rightful owner."
hide square
hide camera
$ camera = False
p "Gee, she must be on her period or something..."
jump DowntownChoiceDay05b

label DebbyOffice01Day05:

if (hour <= 18):
    jump DebbyOffice01bDay05
if (hour > 18):
    scene debbyoffice02 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Looks like Debby isn't in her office. She must have gone home, it's getting quite late actually... I should leave too."
    jump DowntownChoiceDay05b

label DebbyOffice01bDay05:    
scene debbyoffice01 with dissolve
$ renpy.pause(1.0, hard=True)
$ debbyofficeseen05 = True
d "Well, if it isn't my favorite nephew! What brings you here?"
menu:
    "Thought I could score with some of your hot models. Where are the chicks?":
        show debbyofficeangry
        d "I'm running a respectable business here, not a whorehouse! Get out of my building at once!"
        $ lust_points[5] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.6 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01        
        scene downtownaudacious with dissolve
        p "I don't think I'm gonna be allowed back in today. I really pissed her off..."
        jump DowntownChoiceDay05b
    "I just wanted to see where you and mom work.":
        show debbyofficeneutral
        d "How quaint. And what do you think?"
        p "It's an amazing place, a testament to your success Debby!"
        scene debbyoffice01 with dissolve
        d "Oooh, thank you [name], you're going to be make me blush..."
        $ lust_points[5] +=1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        d "But you should leave now... I'm very busy with work, I'm running a very LARGE corporation now!"        
        jump AudaciousOffice01Day05b
    "I would like to offer my services as a critic of your lovely swimsuits.":
        show debbyofficeneutral
        d "That's a bit bold young man... But as it turns out, I have just received this new bikini from our R&D department..."
        show debbyofficedevious
        d "Perhaps you would like to see me wearing it and give your \"professional\" opinion?"
        menu:
            "Sure Debby!":
                d "Such eagerness... Well go and wait in the corridor and I'll call you back in once I'm ready..."
                $ lust_points[5] +=1
                $ score += 1
                show lust01:
                    xalign 0.6 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
                jump DebbyOffice02Day05
            "I wouldn't want to intrude. Maybe you have a hot.. I mean a model for this kind of work?":
                show debbyofficeneutral
                d "Of course, but I always beta-test the new swimsuits first... since I'm the CEO. So take it or lose it!"
                p "I'll take it of course!"
                d "Then go and wait in the corridor and I'll call you back in once I'm ready..."
                jump DebbyOffice02Day05

label DebbyOffice02Day05:
scene debbyoffice02 with dissolve
$ renpy.pause(2.0, hard=True)
d "Ready! You can open the door now [name]..."
scene debbyoffice03 with dissolve
$ renpy.pause(1.0, hard=True)
p "(Damn, she looks so fine in that micro-bikini)"
d "So...What do you think? Maybe I should turn round first so you can inspect it in more details..."
scene debbyoffice04 with dissolve
$ renpy.pause(1.0, hard=True)
menu:
    "Yes, yes I see... Interesting design, innovative... May I feel the fabric?":
        d "Yes of course, the fabric quality is indeed very important..."
        jump DebbyOffice04Day05
    "Wow, Debby, you look fabulous in it!":
        d "Well, that's very nice of you to say, but you're supposed to be a critic for the BIKINI, not me..."
        d "I guess you don't have what it takes to be a swimsuit critique, you are too easily distracted by the person wearing in it... (sigh)"
        p "Well...err... I didn't mean to..."
        d "It's best if you leave the building now [name], since your services are not required, you have now become \"unauthorized\" personnel..."
        scene downtownaudacious with dissolve
        p "I don't think I'm gonna be allowed back in today. I really pissed her off..."
        jump DowntownChoiceDay05b
    "Feel up her breasts":
        if (blacktop05 == True):
            scene debbyoffice06black with dissolve
        else:
            scene debbyoffice06 with dissolve            
        $ renpy.pause(1.0, hard=True)
        d "Come on [name], I know you're a horny boy but this is too bold!"
        p "Sorry, I got carried away by those...err...funbags."
        d "I guess you don't have what it takes to be a swimsuit critique, you are too easily distracted by the person wearing in it... (sigh)"
        p "Well...err... I didn't mean to..."
        d "It's best if you leave the building now [name], since your services are not required, you have now become \"unauthorized\" personnel..."
        scene downtownaudacious with dissolve
        p "I don't think I'm gonna be allowed back in today. I really pissed her off..."
        jump DowntownChoiceDay05b

label DebbyOffice04Day05:
scene debbyoffice07 with dissolve
$ renpy.pause(2.0, hard=True)
p "Mmm.... It feels soft yet sturdy..."
d "I'm impressed, you really sound like you know what you're talking about [name]..."
window hide
if (lust_points[5] <= 9):
    $ renpy.pause(1.0, hard=True)
    $ lust_points[5] +=1
    $ score += 1
    show lust01:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[5] >= 10):
    $ renpy.pause(1.0, hard=True)        
    show epiclust:
        xalign 0.6 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    d "Why don't you pull the string up and see my big old titties?"
    if (blacktop05 == True):
        scene debbyoffice08black with dissolve
    else:
        scene debbyoffice08 with dissolve            
    $ renpy.pause(2.0, hard=True)
    d "Oops... See what a dirty whore I am... I guess I have no choice but to pull my bottom down too now... So you can FUCK ME MY STUD NEPHEW!"
    jump OfficeDebbyFuckChoiceDay05
    
menu:
    "pull the string up":
        if (blacktop05 == True):
            scene debbyoffice08black with dissolve
        else:
            scene debbyoffice08 with dissolve            
        $ renpy.pause(2.0, hard=True)
        if (lust_points[5] <= 9):
            $ renpy.pause(1.0, hard=True)
            $ lust_points[5] +=1
            $ score += 1
            show lust01:
                xalign 0.8 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        if (lust_points[5] >= 10):
            $ renpy.pause(1.0, hard=True)        
            show epiclust:
                xalign 0.6 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust
            d "Oops... See what a dirty whore I am... I guess I have no choice but to pull my bottom down too now... So you can FUCK ME MY STUD NEPHEW!"
            jump OfficeDebbyFuckChoiceDay05
        d "Oops, pull it down now [name], you've \"inspected\" the fabric enough now..."
        d "Thanks for your help [name], but now I have a lot of work to do..."
        p "Sure Debby, I'll leave you to it then."
        jump AudaciousOffice01Day05b        
    "Feel up her breasts":
        if (blacktop05 == True):
            scene debbyoffice06black with dissolve
        else:
            scene debbyoffice06 with dissolve            
        $ renpy.pause(2.0, hard=True)
        d "Come on [name], I know you're a horny boy but this is too bold!"
        p "Sorry, I got carried away by those...err...funbags."
        d "I guess you don't have what it takes to be a swimsuit critique, you are too easily distracted by the person wearing in it... (sigh)"
        p "Well...err... I didn't mean to..."
        d "It's best if you leave the building now [name], since your services are not required, you have now become \"unauthorized\" personnel..."
        scene downtownaudacious with dissolve
        p "I don't think I'm gonna be allowed back in today. I really pissed her off..."
        jump DowntownChoiceDay05b

label OfficeDebbyFuckChoiceDay05:
scene debbyofficeprefuck01 with dissolve
play sound "Sounds/debbyprefuck01.mp3"
$ renpy.pause(10.0, hard=True)
d "I am ready to be treated like the cheap whore that I am Master..."
if (stamina <= 0) and (whitebull == True):
    p "I'd better drink some White Bull if I want to be able to perform...."
    menu:
        "Drink white bull (+2 stamina)":
            show whitebull
            show square
            play sound "Sounds/lost.mp3"
            "You gulped down your White Bull energy drink."
            hide square
            hide whitebull
            $ whitebull = False
            $ stamina += 2
            jump DebbyFuckChoiceDay05b
        "Don't drink white bull and keep it for another time":
            p "Well, this is all good clean fun Debby, but it's late, I have to go to home for dinner..."
            d "What? Is this some kind of sick joke? Get out of my office you useless pervert!"
            window hide
            $ lust_points[5] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.7 yalign 0.3
                linear 1.0 yalign 0.5
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01    
            jump DowntownChoiceDay05b        
if (stamina <= 0):
    p "Well, this is all good clean fun Debby, but it's late, I have to go to home for dinner..."
    d "What? Is this some kind of sick joke? Get out of my office you useless pervert!"
    window hide
    $ lust_points[5] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.7 yalign 0.3
        linear 1.0 yalign 0.5
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    jump DowntownChoiceDay05b        

label OfficeDebbyFuckChoiceDay05b:
scene debbyofficeprefuck01 with dissolve
menu:
    "Let me fuck your dirty hole nice and slow!" if (debbychair == False):
        jump OfficeDebbyChairFuckDay05
    "Give me a nice sloppy blowjob slave!" if (debbyblow == False):
        jump OfficeDebbyBlowDay05
    "I want to maul your hard nipples with my teeth!" if (debbymaul == False):
        jump OfficeDebbyNippleDay05
    "A cheap whore like you deserves a good pussy-pounding!" if (debbydoggy == False):
        jump OfficeDebbyDoggyDay05
    "Time to finish me off slave!" if (debbymaul == True) and (debbydoggy == True) and (debbyblow == True) and (debbychair == True):
        jump OfficeDebbyMovie05
    
label OfficeDebbyBlowDay05:
$ debbyblow = True
scene debbyblowoffice01 with dissolve
$ renpy.pause(1.0, hard=True)
d "Let me lick your bull-sized balls while you pleasure yourself between my tits Master!"
scene debbyblowoffice02 with dissolve
$ renpy.pause(1.0, hard=True)
label OfficeDebbyBlowDay05b:
play sound "Sounds/debbyblow01.mp3"
scene debbyblowoffice01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyblowoffice02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyblowoffice01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyblowoffice02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyblowoffice01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyblowoffice02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyblowoffice01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyblowoffice02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyblowoffice01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyblowoffice02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyblowoffice01
$ renpy.pause(0.5, hard=True)
scene debbyblowoffice02
$ renpy.pause(0.5, hard=True)
scene debbyblowoffice01
$ renpy.pause(0.5, hard=True)
scene debbyblowoffice02
$ renpy.pause(0.5, hard=True)
scene debbyblowoffice01
$ renpy.pause(0.5, hard=True)
scene debbyblowoffice02
$ renpy.pause(0.5, hard=True)
scene debbyblowoffice01
$ renpy.pause(0.5, hard=True)
scene debbyblowoffice02
$ renpy.pause(0.5, hard=True)
scene debbyblowoffice01
$ renpy.pause(0.5, hard=True)
scene debbyblowoffice02
$ renpy.pause(0.5, hard=True)
scene debbyblowoffice01
$ renpy.pause(0.5, hard=True)
scene debbyblowoffice03
$ renpy.pause(1.0, hard=True)
menu:
    "Repeat":
        p "Let's do that again whore, I want more drool on my balls!"
        jump OfficeDebbyBlowDay05b
    "Move on":
        p "You did good slave, it's now time to move on to something else..."
        jump OfficeDebbyFuckChoiceDay05b

label OfficeDebbyChairFuckDay05:
$ debbychair = True
scene debbyofficefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Offer your gaping slut-hole to my massive teenage cock slave!"
d "My filthy hole belongs to you Master... Do as you please with it!"
label OfficeDebbyChairFuckDay05b:
play sound "Sounds/debbyfuck01.mp3"
scene debbyofficefuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyofficefuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyofficefuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyofficefuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyofficefuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyofficefuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyofficefuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyofficefuck01
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck02
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck01
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck02
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck01
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck02
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck01
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck02
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck01
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck02
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck01
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck02
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck01
$ renpy.pause(0.5, hard=True)
scene debbyofficefuck02
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        p "Your pussy needs some more destroying!"
        jump OfficeDebbyChairFuckDay05b
    "Move on":
        p "I've punished your dirty hole enough for the moment slave... I'm giving you a respite..."
        d "Thank you Master, I am not worthy of such generosity..."
        jump OfficeDebbyFuckChoiceDay05b

label OfficeDebbyNippleDay05:
if (blacktop05 == True):
    scene debbyofficenippleblack with dissolve
else:
    scene debbyofficenipple with dissolve      
play sound "Sounds/sucking.mp3"
$ renpy.pause(1.0, hard=True)
d "Ooh, you suck on my nipples ssoo good! Maul my tits Master!"
p "They look red and erect now, it's time for something else slave..."
$ debbymaul = True
jump OfficeDebbyFuckChoiceDay05b

label OfficeDebbyDoggyDay05:
$ debbydoggy = True
scene debbyhardfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
d "Oh my God, your cock is stretching me wide open Master!"
p "Not wide enough yet..."
scene debbyhardfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
d "AAAH! I don't deserve your giant teenage piece of meat!"
p "What? You want me to stop?"
d "Of course not, fuck me deeper please Master!"
p "That's what I like to hear slave!"
scene debbyhardfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
label OfficeDebbyDoggyDay05b:
scene debbyhardfuck02 with dissolve
play sound "Sounds/debbyfuck02.mp3"
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck01
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck02
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck01
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck02
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck01
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck02
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck01
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck02
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck01
$ renpy.pause(0.3, hard=True)
scene debbyhardfuck02
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump OfficeDebbyDoggyDay05b
    "Move on":
        p "Your dirty hole is creaming all over the place, let's switch position whore!"
        jump OfficeDebbyFuckChoiceDay05b


label OfficeDebbyMovie05:
stop music
play music "Sounds/debbyslow.mp3"
show debbyofficeslow
show faster
call screen officedebbyfuckslowday05
screen officedebbyfuckslowday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("OfficeDebbyFuckFastDay05")

label OfficeDebbyFuckFastDay05:
stop movie
hide faster
play music "Sounds/debbyfast.mp3"
show debbyofficefast
show cum
call screen officedebbyfuckfastday05
screen officedebbyfuckfastday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("OfficeDebbyFuckCumDay05")

label OfficeDebbyFuckCumDay05:
hide debbyofficefast
hide debbyofficeslow
stop music
scene debbyofficecum01
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(1.0, hard=True)
d "I'm filled up with your cum and you're still spurting everywhere, I can feel heavy streamers hitting my dirty tits! AAH!"
window hide
scene debbyofficecum02 with dissolve
play sound "Sounds/cumming.mp3" 
$ renpy.pause(3.0, hard=True)
d "Oh my God Master, look at all that cum flying everywhere! Yes, cover my filthy whore body with your cream [name]!"
scene debbyofficecum03 with dissolve
play sound "Sounds/debbycum01.mp3" 
$ renpy.pause(8.0, hard=True)
d "This is the biggest load I've ever had in my life... What a stud nephew you are Master!"
$ hour +=1
$ stamina -=1
show staminaminus01:
    xalign 0.3 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
p "I'd better get going, it's getting quite late!"
if (debbyjosewin == False) and (debbywin == False):
    p "(She didn't notice I took a picture of her being filled by my dick... Now I'll send it to José)."
    $ debbywin = True
if (debbyjosewin == True):
    p "(I hate sloppy seconds, especially after that dickhead José already ploughed their insides... But it was worth it, Debby is such a filthy whore!)"
$ debbyfucked = True
$ debbyfuckedoffice = True
if (nikkifucked == True) and (nancyfucked == True) and (achievement.has("homesteader") == False):
    show achievement07:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement07
    $ achievement.grant("homesteader")
if (tanyafucked == True) and (francinefucked == True) and (teaganfucked == True) and (achievement.has("king") == False):
    show achievement13:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement13
    $ achievement.grant("king")
jump DowntownChoiceDay05b

label MomOffice01Day05:
$ seenmomofficeday05 = True
if (hour <= 17) and (seenmomofficeday03 == False):
    scene momwork01 with dissolve
    $ renpy.pause(1.0, hard=True)
    m "[name]! How the hell did you get in here??? You should really leave sweetie, I'm busy with work."
    p "I just wanted to see where you work Nancy!"
    m "Well now you've seen. Get back home before a security guard finds you, I don't want any trouble from you here!"
    p "Ok Nancy, I'm sorry... (I'd better leave)."
    $ seenmomofficeday05 = True
    jump AudaciousOffice01Day05b

if (hour <= 17) and (seenmomofficeday03 == True):
    scene momwork01 with dissolve
    $ renpy.pause(1.0, hard=True)
    m "Oh, hello sweetie! YOu came to see your hard-working landlady again? I'm sorry, but I'm very busy... Debby is really pushing me, I'm exhausted..."
    menu:
        "Ok mom, I'll see you tonight then... (I'd better leave).":
            jump AudaciousOffice01Day05b
        "Maybe I could give you a massage?":
            m "Mmh, why not, I could certainly do with a footrub at least..."
            $ gavemommassage05 = True
            jump MomMassageDay05

if (hour >= 18):
    scene momofficeempty with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Looks like Nancy isn't in her office. She must have gone home, it's getting quite late actually... I should leave too."
    jump DowntownChoiceDay05b

label MomMassageDay05:
if (blacktop05 == True):
    scene mommassage01black with dissolve
if (blacktop05 == False):
    scene mommassage01 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/womansigh.mp3"
m "Thank you my sweet tenant, I feels more relaxed now..."
if (lust_points[16] <= 8):
    $ lust_points[16] +=1
    $ score += 1
    show lust01:
        xalign 0.35 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (blacktop05 == True):
    scene mommassage02black with dissolve
if (blacktop05 == False):
    scene mommassage02 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/kissing.mp3"
m "You'd better leave now [name], you really shouldn't be coming to mommy's workplace, you might get her in trouble..."
p "Alright mom, see you tonight at dinner!"
jump AudaciousOffice01Day05b

label EveningAnna01Day05:
scene annaentrance01 with dissolve
play sound "Sounds/debbydoorbell.mp3"
$ renpy.pause(1.0, hard=True)
an "Welcome to our home! Please come in and make yourselves comfortable."
m "Thank you Anna, and thanks for inviting us, it's so nice to have such welcoming neighbors!"
p "(Well, except for her son who's a complete dickhead that is...)"
scene annaentrance02 with dissolve
$ renpy.pause(1.0, hard=True)
j "Hi Nikki, nice to see you again! In MY house..."
s "Hi José! (peck on the cheek)"
p "Humpf..."
m "Oh, Anna, your house is beautiful! I really like the decoration."
an "There are some excellent designer furniture shops downtown. Have you heard about \"Luxury Houses\" on Main Street?"
j "Hey worm, what are you doing standing there like an idiot? Do come in..."
p "I'll come in if I want to! OK, I just decided I want to."
scene annaentrance03 with dissolve
$ renpy.pause(1.0, hard=True)
an "Please sit down and make yourselves comfortable. The dinner is still simmering but we can all get to know each other better beforehand."
m "That is an excellent idea Anna. [name], why don't you sit next to me? So I can keep an eye on you..."
if (maddysaved == True) or (maddysaved05 == True):
    scene annadinner01 with dissolve
    $ renpy.pause(1.0, hard=True)
    an "I heard that you saved a girl that had been kidnapped [name]. Everyone is calling you a hero on the island."
    $ lust_points[0] +=1
    $ score += 1
    show lust01:
        xalign 0.8 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01     
    scene annadinner02 with dissolve
    j "Not everyone. Some people are saying he was lucky, that's all."
    p "You're just jealous because I saved her and not you!"
    scene annadinner01 with dissolve
    an "Now please calm down boys. We're sure both of you are very brave." 
    p "Well at least we know I am..."
    jump EveningAnna02Day05
if (maddysaved == False) and (maddysaved05 == False):
    scene annadinner02 with dissolve
    $ renpy.pause(1.0, hard=True)    
    m "I heard that you saved a girl that had been kidnapped José. Everyone is calling you a hero on the island."
    if (lust_pointsB[16] <= 9):
        $ lust_pointsB[16] +=1
        show challengerlustplus01:
            xalign 0.2 yalign 0.5
            linear 1.0 yalign 0.3
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustplus01     
    s "Yeah, that was amazing of you... I heard you had to beat up her kidnapper real bad too! He deserved it."
    if (lust_pointsB[17] <= 9):
        $ lust_pointsB[17] +=1
        show challengerlustplus01:
            xalign 0.7 yalign 0.5
            linear 1.0 yalign 0.3
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustplus01         
    p "I was on the verge of finding her myself today, so I deserve credit too."
    j "Credit for what? I'm the one who saved Maddy, I'm the HERO, you're nothing WORM!"
    scene annadinner01 with dissolve
    an "Now please calm down boys. We're sure both of you are very brave."
    j "Well at least we know I am..."

label EveningAnna02Day05:
an "I'll go and check on the roast, I think it might be ready."
m "I'll come with you and help Anna."
scene annadinnerjosenikki01 with dissolve
$ renpy.pause(1.0, hard=True)
s "My mom said there was an indoor pool in the house?"
j "Yes Nikki, I hope you brought a swimsuit because we might go for a dip after dinner. You'll see, it's so nice to swim after dark, the setting is more... romantic."
s "Oooh, that's nice! I can't wait."
menu:
    "I'll be there too, I brought my speedo, the one that really shows off my massive package.":
        j "Pff! Everyone knows you're just stuffing it with socks!"
        p "No, I'm not! How can you say that after all the pics I sent you? You KNOW I'm hung like a horse!"
        s "What pics are you talking about?"
        j "[name] is a pervert, he's sending dick pics to people on crapchat all the time..."
        scene annadinnerjosenikki02 with dissolve
        s "Ewww, that's disgusting! I knew you were a pervert [name]!"
        if (nikkifucked == False):
            $ lust_points[17] -=1
            $ score -= 1
            show lustinus01:
                xalign 0.7 yalign 0.3
                linear 1.0 yalign 0.5
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
    "I'm in, your mother is going to see how much more muscular I am than you!":
        j "You've got nothing on me WORM!"
        p "We'll see about, I'm da man, I'm DA MAN!"
        s "Oh, not AGAIN! Will you two stop arguing all the time?"        

an "Dinner is ready! Bring out your plates so I can serve everyone!"
j "We're coming mom!"
scene annadinner04 with dissolve
$ renpy.pause(1.0, hard=True)
an "So, how are you all settling into your new life on the island?"
s "I really like our school and all the beautiful beaches that are on the island!"
j "I know all of the best beaches, I'll take you there sometimes, I'm sure there are some that you haven't seen yet."
s "Oh, thank you José, that would be awesome! Perhaps this weekend?"
p "There's the Muscle Stud competition this weekend, José will be too busy there, losing to ME!"
j "We'll see about that! I'll beat you by a mile, I've been training hard for it!"
an "Give it a rest boys, we've had enough! I was asking a question to NANCY."
j "Sorry mom..."
m "Thank you Anna. Well, I've started my new job, it's quite demanding, but I'm starting to really get the hang of it."
an "I actually bought a new bikini from the latest \"Audacious\" collection, I'm really looking forward to wearing it. They are really the best swimwear company in the world, keep up the good work!"
$ hour += 1
"Time passes and food gets eaten."
scene annadinner05  with dissolve
$ renpy.pause(1.0, hard=True)
an "I propose that we all change into our swimwears to enjoy an evening dip in our indoors swimming pool!"
m "That's a wonderful idea!"
an "[name], you can change in the bathroom, Nancy and Nikki can change in the spare bedroom. Let's meet back up here in five minutes!"
"You change into your speedos and leave the bathroom...."
scene annadinner06  with dissolve
$ renpy.pause(1.0, hard=True)
m "Now, I want you to BEHAVE [name], is that understood? And try and keep that bulge to reasonable proportions if you know what I mean..."
s "I doubt he'll manage, he keeps getting hardons all the time for no reasons (giggles)"
p "I assure you there is always a valid reason..."
scene annadinner07  with dissolve
$ renpy.pause(1.0, hard=True)
an "Ah, everyone is ready, let me show you to our indoor swimming pool then. This way..."
p "(Mmmh, Anna sure is going for a rather \"Audacious\" look tonight... I hope it's for me...)"
scene annapool01 with dissolve
$ renpy.pause(1.0, hard=True)
p "(I must admit their pool is really nice... There's mom and Anna chatting....)"
scene annapoolnikki01 with dissolve
$ renpy.pause(1.0, hard=True)
p "(And that douchebag trying his luck with Nikki... Pfff!)"
label AnnaPoolChoice01:
menu:
    "Talk to mom" if (spokenmompool == False):
        $ spokenmompool = True
        scene annapool02 with dissolve
        $ renpy.pause(1.0, hard=True)        
        p "Hey Nancy, do you fancy a dip in the pool with me?"
        m "Can't you see I'm having a conversation with Anna? Go and play with Nikki and José sweetie."
        if (nancyfucked == False):
            $ lust_points[17] -=1
            $ score -= 1
            show lustinus01:
                xalign 0.7 yalign 0.3
                linear 1.0 yalign 0.5
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
        p "Ah. That was apparently the wrong choice..."
        jump AnnaPoolChoice01
    "Talk to Anna" if (spokenannapool == False):
        $ spokenannapool = True
        scene annapool03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "I love your pool. I wish we had an indoors pool at our house, it's so cool!"
        an "I'm glad you like it. Why don't you dive in and enjoy the water, which is kept at 25C all year round!"
        scene annapool01 with dissolve
        $ renpy.pause(1.0, hard=True)
        m "That's impressive. But the weather is so nice all year round here, I think our outdoor pool is the same!"
        an "I guess you're right... I ALSO bought it to stop our prying neighbors from being too curious..."
        m "I see what you mean..."
        p "(Well, that conversation is BORING. And I didn't get her to swim with me...)"
        m "Sweetie, why don't go and play with Nikki and José? It would be nice for you three to bond together."
        p "Err... Sure Nancy."        
        jump AnnaPoolChoice01
    "Talk to Nikki":
        scene annapoolnikki01b with dissolve
        $ renpy.pause(1.0, hard=True) 
        p "Hey Nikki, fancy a dip with me?"
        s "Sure [name]. The water is really warm, you'll see..."
        j "Well, I'm off, I have some homework left to do. SInce I had to HELP my mom prepare the dinner for YOU guys."
        if (maddysaved == False) and (maddysaved05 == False):
            s "A hero like you sure deserves a break José! Next time, you're the one who'll be invited to our house..."
            j "By Nikki, see you tomorrow at school then."
            jump AnnaPool02            
        if (maddysaved == True) or (maddysaved05 == True):
            s "Well, next time, you're the one who'll be invited to our house José..."
            p "(I bloody well hope not...)"
            jump AnnaPool02
    
label AnnaPool02:
scene annapoolnikki02 with dissolve
play sound "Sounds/swimming.mp3"
$ renpy.pause(1.0, hard=True)
menu:
    "Swim around nonchalantly":
        s "Isn't the pool wonderful [name]? Too bad José left..."
        p "Good riddance I say!"
        jump AnnaPool03
    "Swim behind her and get REAL close" if (nikkifucked == True):
        jump AnnaPool02b

label AnnaPool02b:
scene annapoolnikki03 with dissolve
play music "Sounds/swimming.mp3"
$ renpy.pause(1.0, hard=True)
p "Why don't you rub your arse on my bulge Nikki... No one can see us..."
s "Are you crazy?... Are.. you getting a hardon?"
scene annapoolnikki04 with dissolve
$ renpy.pause(1.0, hard=True)
p "Yep! And it's sticking between your legs well past your pussy... Can you feel how hard and big it is Nikki?"
s "Oh my God, I can't believe you're doing that. Stop it!"
p "Not before you tell me you won't get anywhere near that arsehole José... (cockblock José)"
scene annapoolnikki05 with dissolve
$ renpy.pause(1.0, hard=True)
s "But he's such a nice boy... But your cock... OK, you win! Now get off me with that monstercock before Anna or mom sees us!"
"You cockblocked José."
$ josenikkicockblocked = True
if (josedebbycockblocked == True) and (josemariacockblocked == True) and (achievement.has("cockblocker") == False):
    show achievement11:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement11
    $ achievement.grant("cockblocker")

label AnnaPool03:
scene annapool04 with dissolve
play sound "Sounds/diving.mp3"
$ renpy.pause(1.0, hard=True) 
an "A quick dip in the pool for me!"
m "I'll leave you to it, I'd better get dressed, we should go soon..."
scene annapool05 with dissolve
$ renpy.pause(1.0, hard=True) 
p "Where the hell did she go?"
scene annapool06 with dissolve
$ renpy.pause(1.0, hard=True) 
an "Surprise! I had a... nice view from under the water... (wink)"
p "Well, you can always get a closer look..."
$ lust_points[0] +=1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.5
    linear 1.0 yalign 0.3
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
an "Maybe I do, Maybe I don't... Up to you to find out... I'll be waiting at my window later on..."
an "Right now though, you'd better leave or your mom might get suspicious... See you maybe later [name]! (wink)"
jump AnnaEveningOutDay05

label AnnaEveningOutDay05:
$ hour += 1
scene annaentrance01 with dissolve
$ renpy.pause(1.0, hard=True)
m "Well, thank you for a wonderful evening Anna!"
an "You're welcome, it is my duty to make every new family feel welcome on our wonderful island!"
s "Good night Josè, I'll see tomorrow in class!"
scene blackscreen with dissolve
$ renpy.pause(1.0, hard=True)
scene annapredinner with dissolve
$ renpy.pause(1.0, hard=True)
m "Well, it's getting late, I think I'll head to my room... I'm a bit tipsy... (blush)"
jump EveningChoiceDay05

label AnnaRoomDay05:
scene annaroom01 with dissolve
$ renpy.pause(1.0, hard=True)
$ seenannaevening05 = True
an "Who is that? Oh, it's you..."
if (stamina <=0) and (whitebull == False):
    an "I was expecting you. Come in, naughty boy..."
    p "You know what? This is getting a bit too saucy for me. I'm like, real tired, you know, school, homework, stuff like that."
    an "Oh my God, I can't believe I'm hearing that! What a massive let-down!"
    $ lust_points[0] -=2
    show lustminus02:
        xalign 0.6 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus02
    if (annajosewin == False):
        an "At least, I have my son who is also hung like a horse and not a tired little wimp like you..."
        $ lust_pointsB[0] +=1
        show challengerlustplus01:
            xalign 0.2 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustplus01
        an "Now get out of my house!"
        $ hour += 1
        jump EveningChoiceDay05
    if (annajosewin == True):
        an "My son wasn't tired like you when he rammed his giant pole up all my holes the other day! I guess I'll just have to fuck him again tonight..."
        an "Now get out of my house!"
        $ hour += 1
        jump EveningChoiceDay05
if (stamina <=0) and (whitebull == True):
    an "I was expecting you. Come in, naughty boy..."
    p "(Now is definitely the time to take some White Bull, it looks like it's going to get interesting real fast...)"
    menu:
        "Drink some White Bull (+2 stamina)":
            show whitebull
            show square
            play sound "Sounds/lost.mp3"
            "You gulped down your White Bull energy drink."
            hide square
            hide whitebull
            $ whitebull = False
            $ stamina += 2
            jump AnnaRoom02PreDay05
        "Keep your energy drink for another time":
            p "You know what? This is getting a bit too saucy for me. I'm like, real tired, you know, school, homework, stuff like that."
            an "Oh my God, I can't believe I'm hearing that! What a massive let-down!"
            $ lust_points[0] -=2            
            show lustminus02:
                xalign 0.6 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus02
            if (annajosewin == False):
                an "At least, I have my son who is also hung like a horse and not a tired little wimp like you..."
                $ lust_pointsB[0] +=1
                show challengerlustplus01:
                    xalign 0.2 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide challengerlustplus01
                an "Now get out of my house!"
                $ hour += 1
                jump EveningChoiceDay05
            if (annajosewin == True):
                an "My son wasn't tired like you when he rammed his giant pole up all my holes the other day! I guess I'll just have to fuck him again tonight..."
                an "Now get out of my house!"
                $ hour += 1
                jump EveningChoiceDay05

label AnnaRoom02PreDay05:            
if (lust_points[0] == 8):
    $ lust_points[0] +=2
    $ score += 2
    show lust02:
        xalign 0.6 yalign 0.3
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02     
if (lust_points[0] == 9):
    $ lust_points[0] +=1
    $ score += 1
    show lust01:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01 
if (lust_points[0] >= 10):
    show epiclust:
        xalign 0.4 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    an "I was expecting you... Come in, naughty boy."
    jump AnnaRoom02Day05
if (lust_points[0] <= 9):
    an "Well, you're too late. I'm not in the mood anymore. Next time, try and hurry up and don't make women wait..."
    p "What? But I ran as fast as I could!!! It's not fair!"
    $ hour += 1
    jump EveningChoiceDay05

label AnnaRoom02Day05:
scene annaroom02 with dissolve
$ renpy.pause(1.0, hard=True)
an "Let me first get more comfortable by getting rid of this bathrobe. So you can admire my curves..."
if (stamina <=0) and (whitebull == False):
    p "YOu know what? This is getting a bit too saucy for me. I'm like, real tired, you know, school, homework, stuff like that."
    scene annaroom01 with dissolve
    $ renpy.pause(1.0, hard=True)
    an "Oh my God, I can't believe I'm hearing that! What a massive let-down!"
    if (annajosewin == False):
        an "At least, I have my son who is also hung like a horse and not a tired little wimp like you..."
        show challengerlustplus01:
            xalign 0.2 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustplus01
        an "Now get out of my house!"
        jump EveningChoiceDay05
    if (annajosewin == True):
        an "My son wasn't tired like you when he rammed his giant pole up all my holes! I guess I'll just have to fuck him again tonight..."
        an "Now get out of my house!"
        jump EveningChoiceDay05
if (stamina <=0) and (whitebull == True):
    p "Now is definitely the time to take some white bull, it looks like it's going to get interesting real fast..."
    show whitebull
    show square
    play sound "Sounds/lost.mp3"
    "You gulped down your White Bull energy drink."
    hide square
    hide whitebull
    $ whitebull = False
    $ stamina += 2
    
p "Alright! Now we're talking!"
scene annaroom03 with dissolve
$ renpy.pause(1.0, hard=True)
an "So, what do you think?"
p "These are dangerous curves but I'm cruising full speed ahead!"
an "There's also a dangerous curve starting to form in your pants..."
scene annaroom04 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn Anna, now my pants are starting to get real uncomfortable!"
an "Well, get out of them and get more comfortable by sitting down so I can give it a gentle rub... With my arse!"
scene annaroom05 with dissolve
$ renpy.pause(1.0, hard=True)
an "Relax and enjoy the show [name], I worked as a stripper in my youth, my specialty was arse-grinding."
p "I can't wait to feel it against my growing shaft Anna!"
an "Most customers would blow their load in their trousers in under two minutes...Let's see how YOU fare!"
scene annaroom06 with dissolve
$ renpy.pause(1.0, hard=True)
an "Oooh, I can feel a really BIG log of meat right between my asscheeks... What could it be?"
p "Gggg...MMmb..."
an "God, I can't stand it, it's just so HUGE and feels so POWERFUL! Please take it out [name]!"
scene annaroom07 with dissolve
$ renpy.pause(1.0, hard=True)
an "Sweet Mother of God, what did I let myself into? You are going to PULVERIZE my holes with that monster dong!"
p "Don't worry, I'll be careful..."
an "Al..right... What would you like to do first?"
label AnnaFuckChoiceDay05:
menu:
    "Let me lift you up on my crank!" if (annacrank == False):
        jump AnnaCrankDay05
    "How about giving me a nice blowjob?" if (annablow == False):
        jump AnnaBlowDay05
    "Your boobs seem ideal for a titfuck..." if (annatits == False):
        jump AnnaTitfuckDay05
    "Let's get on the bed and fuck like wild animals!" if (annabed == False):
        jump AnnaBedDay05
    "I need to get my rocks off SOON! In YOUR ARSE!" if (annacrank == True) and (annablow == True) and (annatits == True) and (annabed == True):
        an "What? But... You're way too big for that! On the other hand, you're my guest so I'll let you do it, naughty boy!"
        jump AnnaMovieDay05

label AnnaCrankDay05:
$ annacrank = True
scene annaroom11 with dissolve
play sound "Sounds/annacrank01.mp3"
$ renpy.pause(4.0, hard=True)
an "Mmh, I like how POWERFUL that giant tool feels! Please IMPALE me on it [name]!"
scene annaroom12b with dissolve
$ renpy.pause(1.0, hard=True)
an "OOOH, FUCK! It's so fucking thick and DEEP!"
p "Hang on, I'll drill even deeper!"
label AnnaCrankDay05b:
play sound "Sounds/annacrank02.mp3"
scene annaroom12 with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12 with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12 with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12 with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12 with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12 with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12 with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12 with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12 with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12 with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12 with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom12b with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        p "Let's do some more of that workout!"
        if (annajosewin == True):
            an "Ooh, yes please, STUD! YOu go way DEEPER than my son too!"
        if (annajosewin == False):
            an "Ooh, yes please, STUD!"        
        jump AnnaCrankDay05b
    "Move on":
        p "That was a nice workout. Let's do something else..."
        an "The best workout my fuckhole ever got... Phew... What would you like to do next [name]?"        
        jump AnnaFuckChoiceDay05

label AnnaBlowDay05:
$ annablow = True
scene annaroom13 with dissolve
play sound "Sounds/annablow01.mp3"
$ renpy.pause(7.0, hard=True)
an "Let me lick it first... God, it's so fucking big and beautiful!"
label AnnaBlowDay05b:
scene annaroom14a with dissolve
$ renpy.pause(0.3, hard=True)
play sound "Sounds/annablow02.mp3"
scene annaroom14a with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14a with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14a with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14a with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14a with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14a with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom14a with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        p "Suck me some more!"
        if (annajosewin == True):
            an "Of course, your massive cock tastes so good. There's way more precum flowing from it than José..."
        if (annajosewin == False):
            an "Of course, your massive cock tastes so good. There's so much precum flowing from it..."        
        jump AnnaBlowDay05b
    "Move on":
        scene annaroom13 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "That's good, now my cock is nice and shiny with your spit..."
        an "I was choking on it, it's so massive!"
        jump AnnaFuckChoiceDay05

label AnnaTitfuckDay05:
$ annatits = True
scene annaroom10 with dissolve
$ renpy.pause(1.0, hard=True)
an "Kiss me first [name]... Before you plough that fat dong between my big firm funbags!"
play sound "Sounds/kissing.mp3"
scene annatitfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready? Try and keep up, I'm so huge I'll pummel your chin otherwise..."
an "Yes, I'm ready, fuck my tits as hard as you like [name]!"
scene annatitfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
p "As you wish Anna..."
an "Mmh, I'll lick it on each upstroke like that.."
label AnnaTitfuckDay05b:
scene annatitfuck01 with dissolve
play sound "Sounds/annatitfuck.mp3"
$ renpy.pause(0.3, hard=True)
scene annatitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene annatitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        p "Your huge tits feel so good around my shaft..."
        if (annajosewin == True):
            an "And your horsecock feels so good pummelling between them...More so than my son..."
        if (annajosewin == False):
            an "And your horsecock feels so good pummelling between them..."        
        jump AnnaTitfuckDay05b
    "Move on":
        p "I've creamed my precum all over your tits, so that's marked, let's do something else!"
        jump AnnaFuckChoiceDay05

label AnnaBedDay05:
$ annabed = True
scene annaroom08 with dissolve
play sound "Sounds/annabed01.mp3"
$ renpy.pause(5.0, hard=True)
an "Mmh, I can't wait to feel this big dick in my tight little pussy..."
scene annaroom08b with dissolve
$ renpy.pause(1.0, hard=True)
an "AAh, you're stretching me wide open!"
label AnnaBedDay05b:
scene annaroom08c with dissolve
play sound "Sounds/annabed02.mp3"
$ renpy.pause(0.3, hard=True)
scene annaroom08b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom08c with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom08b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom08c with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom08b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom08c with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom08b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom08c with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom08b with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom08c with dissolve
$ renpy.pause(0.3, hard=True)
scene annaroom08b
$ renpy.pause(0.5, hard=True)
scene annaroom08c
$ renpy.pause(0.5, hard=True)
scene annaroom08b
$ renpy.pause(0.5, hard=True)
scene annaroom08c
$ renpy.pause(0.5, hard=True)
scene annaroom08b
$ renpy.pause(0.5, hard=True)
scene annaroom08c
$ renpy.pause(0.5, hard=True)
scene annaroom08b
$ renpy.pause(0.5, hard=True)
scene annaroom08c
$ renpy.pause(0.5, hard=True)
scene annaroom08b
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        p "I like fucking your MILF hole in that position, let's do it again!"
        if (annajosewin == True):
            an "Ooh, yes please! You fuck me so much better than my son I have to admit..."
        if (annajosewin == False):
            an "Ooh, yes please! I want more of that donkey-dick!"        
        jump AnnaBedDay05b
    "Move on":
        p "Let's do something else!"
        jump AnnaFuckChoiceDay05


label AnnaMovieDay05:
scene annafuckmovie with dissolve
p "As I said, I'll finish off by ramming my pole up your tight arse!"
an "I'm ready, just be gentle will you? No one has ever gone up my backside before... Even my ex-husband."
p "Cool, I'll take your arse virginity then!"
play music "Sounds/annafuckslow.mp3"
show annafuckslow
show faster
call screen annaslowfuckday05
screen annaslowfuckday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("AnnaFastFuckDay05")

label AnnaFastFuckDay05:
stop music
hide faster
play music "Sounds/annafuckfast.mp3"
show annafuckfast
show cum
call screen annafastfuckday05
screen annafastfuckday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("AnnaCumDay05")

label AnnaCumDay05:
hide annafuckfast
hide annafuckslow
stop music
scene annacum01
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
an "SHIT! I can feel your red-hot pellets of cum filling up my backside!"
p "And I can feel your tight arse gripping my cock like a vice! RHAAA! Take another cumshot Anna!"
scene annacum02 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "I've got some more creamy offerings for you! I'll cover your back with my seed! UUUGHH, AAAH!"
if (annajosewin == True):
    an "Damn, you're cumming so much! Way more sperm than my son! Yes, give it to me [name]!"
if (annajosewin == False):
    an "Damn, you're cumming so much! Yes, give it to me [name]!"        
$ renpy.pause(2.0, hard=True)
scene annacum03 with dissolve
play sound "Sounds/cumming.mp3" 
$ renpy.pause(1.0, hard=True)
p "Damn! That was an intense orgasm! Phew!"
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
an "My MILF arse was that good, hey?"
if (mariafucked == True) and (nancyfucked == True) and (achievement.has("hunter") == False):
    show achievement09:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement09
    $ achievement.grant("hunter")
$ backdoor += 1
p "It sure was Anna, it sure was... Now you're not a virgin back there anymore, thanks to me! I'm DA MAN!"
if (annajosewin == True):
    an "Well, my son is also DA MAN and he fucked me good and hard earlier this week... Before you...(wink)"
    p "Yeah, thanks for reminding me..."
if (annajosewin == False):
    an "You sure are... Now you'd better leave, Mr DA MAN, cos I need to clean my bedsheets... You totally covered them with your unending streams of thick pearly cum..."        
p "OK, I'd better go back home anyway now..."
if (annajosewin == False):
    $ annawin = True
    p "(Oh, I can't wait to imagine José's shocked face when I send him a pic of his mom covered in my seed...)"
else:
    p "(I got my rocks off with Anna, but she's gonna count towards that arsehole's tally... What a waste of good MILF pussy.) (sigh)"
$ annafucked = True
$ hour += 1
jump EveningChoiceDay05

label EveningChoiceDay05:
stop music
scene ryanbedroomnight with dissolve
$ locroom = True
$ renpy.pause(1.0, hard=True)

if (hour >= 24):
    if (challengercalls <= 10):
        $ lustaddedB = 2
        call Challenger from _call_Challenger_78
        $ lustaddedB = 1
        call Challenger from _call_Challenger_79
        $ challengercalls += 2        
    p "I should really go to sleep now, tomorrow is a school day..."
    jump SleepDay05
p "mmmh, what should I do?"
menu:
    "Do some heavy bodybuilding (+2hrs)" if (hour <= 22):    
        if (workout == True):
            "You already trained today."
            jump EveningChoiceDay05
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
            jump EveningChoiceDay05
    "Check the computer":
        jump ComputerEveningDay05
    "Admire my body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump EveningChoiceDay05
    "Read the book Laura gave you (+1hr)" if (book == True) and (bookread == False):
        jump RyanReadingEveningDay05
    "Go to Nikki's room" if (nikkifucked == False) and (nightsisroomseen05 == False):
        jump SisRoomEveningDay05
    "Go to Tanya's House" if (discovertanya == True) and (seentanyaday05 == False) and (tanyafucked == False) and (hour<=23):
        jump TanyaHouseDay05
    "Go and join Laura at the campsite on the beach" if (lauraritual05 == True) and (seencampfireday05 == False) and (hour<=22):
        jump Campfire01Day05
    "Go to Nancy's room" if (nightmomroomseen02 == False) and (seenmomundressingfullday03  == False) and (seenmomundressingfullday04  == False) and (nightmomroomseen05 == False) and (hour >=22):
        jump MomUndressingDay05
    "Go back to Anna's house" if (seenannaevening05 == False) and (hour<=23):
        jump AnnaRoomDay05
        
label ComputerEveningDay05:
scene ryancomputer with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label ComputerEveningDay05b:
scene ryancomputer
$ renpy.pause(1.0, hard=True)
menu:
    "Check the map":
        jump MapEveningDay05
    "Check the stats":
        jump StatsEveningDay05
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump ComputerEveningDay05b
    "Learn how to use the pendulum" if (pendulum == True) and (pendulumactive ==False):
        jump CompPendulumEveningDay05
    "Play a smutty game (+1hr)":
        jump CompGameEveningDay05
    "Turn the computer off":
        jump EveningChoiceDay05
    
label RyanReadingEveningDay05:
scene ryanreading with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump EveningChoiceDay05

label CompPendulumEveningDay05:
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump ComputerEveningDay05b

label SisRoomEveningDay05:
stop music
$ nightsisroomseen05 = True
if ((lust_points[17] == 10) and (sisanal == False)):
    jump SisRoomEveningDay05b
elif ((lust_points[17] <= 9) and (nikkijosewin == True)):
    jump SisRoomEveningDay05c
else:
    jump SisRoomEveningDay05d

label SisRoomEveningDay05b:
scene sisbed01b with dissolve
$ renpy.pause(1.0, hard=True)
$ locroom = False
s "Hi [name], what's up? You came to finish off what you tried to start but failed miserably to finish?"
if (stamina >= 1):
    p "Yeah, my problem is solved! My huge cock is now ready to rumble!"
    scene sisbed03b with dissolve
    $ renpy.pause(1.0, hard=True)
    s "Alright, finally! I was starting to think you were a wimp or something... Come and kiss me then..."
    jump SisUndress01Day05
if (stamina <= 0) and (whitebull == False):
    p "Err, no actually, I still have some problems with my... err.. thingie."
    scene sisbed01c with dissolve
    s "You should really go and see a doctor about that, it sounds terrible..."    
    p "Hum, well, I hope it will get better tomorrow. Have a good night Nikki, see you in the morning."
    jump EveningChoiceDay05
if (stamina <= 0) and (whitebull == True):
    p "Definitely the right time to drink that energy drink, my libido is too low and it would be ssoo embarrassing if I couldn't perform..."
    show whitebull
    show square
    play sound "Sounds/lost.mp3"
    "You drank an energy drink. The bottle is now empty."
    hide square
    hide whitebull
    $ stamina += 2
    p "Yeah, my problem is solved! My huge cock is now ready to rumble!"
    scene sisbed03b with dissolve
    $ renpy.pause(1.0, hard=True)
    s "Alright, finally! I was starting to think you were a wimp or something... Come and kiss me then..."
    jump SisUndress01Day05

label SisRoomEveningDay05c:
scene sisbed01b with dissolve
$ renpy.pause(1.0, hard=True)
$ locroom = False
s "Hi [name], what's up?"
p "I can't believe you actually fucked that douchebag José, Nikki! You're supposed to be a role-model for me..."
scene sisbed01c with dissolve
s "Well... I do what I want in my private life [name]! How do you even know that anyway?"
p "The arsehole actually sent me a pic of you two having sex to taunt me, that's how!"
s "Oh my God, he really did that? You were right all along, he is a douchebag, I won't ever talk to him again!"
if (lust_points[17] == 9):
    window hide
    $ lust_points[17] += 1
    $ score += 1
    show lust01:
        xalign 0.2 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[17] <= 8):
    window hide
    $ lust_points[17] += 2
    $ score += 2
    show lust02:
        xalign 0.2 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
if (lust_points[17] >= 10):
    window hide
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    p "You're much better off hanging out with nice people like me who would never do such a horrible thing as take a picture of someone naked..."
    scene sisbed01 with dissolve
    s "I'm sorry I didn't trust you... Let me kiss you to make up for it..."
    jump SisFuckday05
p "You're much better off hanging out with nice people like me who would never do such a horrible thing as take a picture of someone naked..."
scene sisbed01 with dissolve
s "I'm sorry I didn't trust you... I'll bear that in mind in the future...But right now, I'm feeling really tired. Have a good night [name]!"
jump EveningChoiceDay05

label SisRoomEveningDay05d:
scene sisbed01 with dissolve
$ renpy.pause(1.0, hard=True)
$ locroom = False
s "Hi [name], what's up?"
p "Err, I don't want to alarm you but there's actually a huge spider crawling on your head..."
scene sisbed02 with dissolve
s "What? AAAH? Get rid of it please! I love animals but not on my head!"
menu:
    "I ain't touching this thing, I might get bitten.":
        s "I can't believe this! MOM, MOM, HELP! And YOU, get out of here useless coward!"
        if (lust_points[17] <= 9):
            window hide
            $ lust_points[17] -= 2
            $ score -= 2
            show lustminus02:
                xalign 0.2 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus02
        jump EveningChoiceDay05
    "Flick it with your hand":
        scene sisbed03 with dissolve
        "The spider scurries along the floor and hides under the bed."
        s "Where is it, where is it? AAAH, It's still in my room!"
        p "Yeah, but it's not on your head anymore at least. Thanks to me."
        s "Thanks to you I won't be able to sleep in my bed tonight, I'm too scared..."
        s "I'll have to go and sleep with mom now!"
        p "I've got a better idea..."
        s "Don't even try [name]. I'm off to mom's room. The only place where I'll feel safe."
        p "But... I did my best! It's not fair!"
        jump EveningChoiceDay05
    "Pick it up carefully and throw it out of the window":
        scene sisbed04 with dissolve
        play sound "Sounds/ouch.mp3"
        $ renpy.pause(1.0, hard=True)
        "The spider bites you but you manage to get rid of it and quickly close the window."
        p "Shit, this godamn spider bit me!"
        window hide
        $ stamina -=1
        show staminaminus01:
            xalign 0.1 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/panting.mp3"
        $ renpy.pause(2, hard=True)
        hide staminaminus01        
        scene sisbed03b with dissolve
        s "But you managed to get rid of it without hurting it... Thank you [name]..."
        if (lust_points[17] == 9):
            window hide
            $ lust_points[17] += 1
            $ score += 1
            show lust01:
                xalign 0.3 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        if (lust_points[17] <= 8):
            window hide
            $ lust_points[17] += 2
            $ score += 2
            show lust02:
                xalign 0.3 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust02
        if (sisanal == False) and (lust_points[17] == 10):                        
            show epiclust:
                xalign 0.3 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust 
            s "Let me kiss the pain away [name]..."
            scene sisbed05 with dissolve
            play sound "Sounds/kissing.mp3"
            $ renpy.pause(2.0, hard=True)
            s "Mmh, I can't feel your HUGE bulge against my thighs..."
            s "Maybe you deserve a bigger reward [name]... I've noticed how you... seem to lust after me..."
            scene sisbed06 with dissolve
            $ renpy.pause(1.0, hard=True)
            jump SisFuckday05        
        s "Let me kiss the pain away [name]..."
        scene sisbed05 with dissolve
        $ renpy.pause(1.0, hard=True)
        s "Mmh, I can't feel your HUGE bulge against my thighs... But it's not right It's not right, right?"
        p "It IS right! It IS right!"
        s "Another day perhaps [name]. When it will feel righter. Have a good night (kiss)."
        jump EveningChoiceDay05

label SisFuckday05:            
if (stamina <= 0) and (whitebull == False):
    p "Err, you know what, I'm like, having little, nothing to worry of course,... urinary problems right now, let's put this off until tomorrow."
    s "Eeew. I didn't want to know that! OK, go back to your room and sort that useless floppy wiener issue FAST!"
    $ hour += 1
    jump EveningChoiceDay05
if (stamina <= 0) and (whitebull == True):
    p "Definitely the right time to drink that energy drink, my libido is too low and it would be ssoo embarrassing if I couldn't perform..."
    show whitebull
    show square
    play sound "Sounds/lost.mp3"
    "You drank an energy drink. The bottle is now empty."
    hide square
    hide whitebull
    $ whitebull = False
    $ stamina += 2
    jump SisUndress01Day05
label SisUndress01Day05:    
scene sisbed06 with dissolve
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
label SisFuckChoicesDay05:
menu:
    "Maybe we should start off with a gentle blowjob." if (sisblowjob == False):
        jump SisBlowjobDay05
    "How about I lick your pussy to get it nice and wet?" if (sispussy == False):
        jump SisPussyDay05
    "I'm gonna pound that arse of yours to oblivion!" if (sisanal == False):
        jump SisAnalDay05
    "Let's fuck, like, for real!" if (sisall == 3):
        jump SisRealFuckDay05

label SisPussyDay05:
scene nikkilick01 with dissolve
$ sisall += 1
play music "Sounds/lick.mp3"
$ renpy.pause(1.0, hard=True)
$ sispussy = True
s "Oh, God, you're so good at this, I'm cumming!, AAAHH!"
s "Thanks [name], I really needed that... Now it's my turn to pleasure that rock-hard donkey-sized cock of yours!"
stop music
jump SisFuckChoicesDay05

label SisBlowjobDay05:
scene nikkiblowjob01 with dissolve
$ sisall += 1
$ renpy.pause(1.0, hard=True)
$ sisblowjob = True
p "Ready to get your mouth stretched sis?"
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
            jump SisBlowjobCumDay05
        "Don't blow your load":
            jump SisFuckChoicesDay05
else:
    s "Keep that hardon, I want you to fuck me with your huge cock!"
    p "Phew, that was ssoo close..."
    jump SisFuckChoicesDay05

label SisBlowjobCumDay05:
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
jump SisFuckChoicesDay05

label SisAnalDay05:
scene nikkianal01 with dissolve
$ sisall += 1
$ backdoor += 1
play sound "Sounds/threesomefuck.mp3"
$ renpy.pause(1.0, hard=True)
$ sisanal = True
s "Be gentle [name], you're too rough!"
p "Sorry, I got carried away, your arse is so warm and tight... Let's switch position."
stop sound
jump SisFuckChoicesDay05

label SisRealFuckDay05:
stop music
play music "Sounds/sisfuck.mp3"
show movienikkifuck
show cum
call screen sisfuckcumday05
screen sisfuckcumday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("SisFuckCum01day05")

label SisFuckCum01day05:
stop music
hide movienikkifuck
scene nikkifuckcum01
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
s "OMG, you're filling my pussy to overcapacity! Pull it out and cover my body with your giant load!"
scene nikkifuckcum02 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "Sssooo good... I really busted a nut there Nikki, you were great..."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
if (nikkijosewin == False):
    $ nikkiwin = True
$ fuckedschoolgirlday05 = True
$ nikkifucked = True
$ hour += 1
if (debbyfucked == True) and (nancyfucked == True) and (achievement.has("homesteader") == False):
    show achievement07:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement07
    $ achievement.grant("homesteader")
s "I'm gonna need to take a shower and clean my sheets without mom noticing all your sticky mess... Mmmh, it's so delicious..."
s "You'd better leave [name], we don't want to get caught by Nancy..."
jump EveningChoiceDay05

label MapEveningDay05:
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
if (discovercabin == True):
    show cabinmap
if (discoverclinic == True):
    show clinicmap
if (discoverfalls == True):
    show waterfallsmap
if (discoveranna == True):
    show annamap

p "This shows all the places I know so far on Veri-Bosti Island..."
show screen statsbackground
show screen inventorybutton
show screen calendar
jump ComputerEveningDay05b

label StatsEveningDay05:
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
jump ComputerEveningDay05b       

label CompGameEveningDay05:
scene ryancomputergame with dissolve
$ renpy.pause(1.0, hard=True)
p "This game is tough. My fingers hurt like hell from so much clicking..."
$ hour +=1
jump ComputerEveningDay05b 
        
label MomUndressingDay05:
stop music
$ nightmomroomseen05 = True
$ locroom = False
scene nancybedroomclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "The door is locked but I can see some light poking through the keyhole."
menu:
    "Look through the keyhole":
        jump MomUndressingDay05b
    "Leave and go back to my room":
        jump EveningChoiceDay05
        
label MomUndressingDay05b:
scene nancyundressing01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Nancy is sitting on her bed. She looks like she's thinking about doing something..."
p "More landlady blueballing on the way for you guys it seems... What should I do?"
menu:
    "Why do you even ask? Look on of course!":
        jump MomUndressing02Day05
    "I feel dirty watching Nancy like that. Go back to my room and cry into my pillow":
        jump EveningChoiceDay05

label MomUndressing02Day05:
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
    jump EveningChoiceDay05

scene nancyundressing07 with dissolve
$ seenmomundressingfullDay05 = True
$ renpy.pause(1.0, hard=True)
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
jump EveningChoiceDay05   


label TanyaHouseDay05:
if (seentanyaday03 == False) and (seentanyaday04 == False):
    jump TanyaHouse01Day05

if (seentanyaday03 == True) or (seentanyaday04 == True):
    jump TanyaBed01Day05
    
label TanyaHouse01Day05:
$ seentanyaday05 = True
stop music
play sound "Sounds/debbydoorbell.mp3"
scene tanyahouse01 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Oh, it's you, you decided to come... And have fun with \"Webcam Tanya\"..."
dl "Who's he? What the hell is he doing here, we're about to start our show, our viewers are waiting!"
ta "I met him on the beach... We need to spice up our shows, we are losing viewers..."
scene tanyahouse02 with dissolve
$ renpy.pause(1.0, hard=True)
dl "No fucking way! I ain't doing it, you never spoke to me about this!"
ta "What are you afraid of honey? We'll just have him stand next to you so that you can humiliate him with your MASSIVE BLACK COCK..."
ta "Viewers have been clamouring for that kind of kink, we'll deliver, so what do you say?"
dl "Hummm... OK, I'll do it. Come in white cuck boy."
menu:
    "Hey, don't I have my say in this shit?":
        ta "Stop it boys! I'm in charge here. [name], get your arse in here, Darryl, go and get ready."
        scene tanyahouse03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "So, what's the deal Tanya?"
        ta "The deal is you want some fun, that's why you came... You'll get your fun... "
        ta "My husband Darryl thinks he's a stud, but I think you might be a bigger stud than him... You want to prove me right or chicken out?"
        menu:
            "Ok, I'll do it! I'm da man, I'm DA MAN!":
                jump TanyaHouse02Day05
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay05
    "I'm out of here, you guys are crazy!":
        ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
        jump EveningChoiceDay05
    "My name is [name] and I ain't playing the cuck you'll find out..." if (stamina >= 1):
        window hide
        $ lust_points[21] += 1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        dl "What? What is he on about?"
        ta "Don't mind him, go and get ready, wear your sexy jungle briefs, I want them to be overpacked with your meat..."
        scene tanyahouse03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "So, what's the deal Tanya?"
        ta "The deal is you want some fun, that's why you came... You'll get your fun..."
        ta "My husband Darryl thinks he's a stud, but I think you might be a bigger stud than him... You want to prove me right or chicken out?"
        menu:
            "Ok, I'm in!":
                jump TanyaHouse02Day05
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay05
    "Err, I wasn't expecting anything sexual and I'm not ready... I'm... exhausted." if (stamina <= 0):
        ta "That's pathetic! A young man like you should always be ready to perform!"
        $ lust_points[21] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.6 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        dl "Ha ha. Come back when your dick isn't a useless noodle kid!"
        jump EveningChoiceDay05
    "My name is [name] and I ain't playing the cuck you'll find out... (+ drink some White Bull)" if (stamina <= 0) and (whitebull == True):
        window hide
        $ lust_points[21] += 1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        dl "What? What is he on about?"
        ta "Don't mind him, go and get ready, wear your sexy jungle briefs, I want them to be overpacked with your meat..."
        scene tanyahouse03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "So, what's the deal Tanya?"
        ta "The deal is you want some fun, that's why you came... You'll get your fun..."
        ta "My husband Darryl thinks he's a stud, but I think you might be a bigger stud than him... You want to prove me right or chicken out?"
        menu:
            "Ok, I'm in!":
                show whitebull
                show square
                play sound "Sounds/lost.mp3"
                "You gulped down your White Bull energy drink."
                hide square
                hide whitebull
                $ whitebull = False
                $ stamina += 2
                jump TanyaHouse02Day05
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay05

label TanyaHouse02Day05:
$ tanyawebcamday03 = True
play music "Sounds/tanyamusic.mp3"
scene webcam01 with dissolve
$ renpy.pause(1.0, hard=True)    
ta "Just stand on either side of the bed boys, the show is about to start... We are live in 3...2...1..."
scene webcam02 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Well hello my horny viewers, it's Webcam Tanya, your favorite goddess..."
ta "Today, Darryl and I have decided to spice up our sex life... We invited a white boy to join in on the fun..."
ta "Will he measure up or will he end up being humiliated by Darryl's massive black cock, you decide!"
ta "Now bring Tanya's fat packages over here boys, I want to feel up what's on offer..."
scene webcam03 with dissolve
$ renpy.pause(1.0, hard=True)
ta "First, my beloved husband, Webcam Black Stallion... Well, you guys already know how HUNG he is... Look at that fat bulge..."
scene webcam04 with dissolve
$ renpy.pause(1.0, hard=True)
ta "And now let's turn to the newbie. Oh my, what do we have here? Either this white boy is stuffing his underwear or he's sporting a dong of TITANIC proportions..."
window hide
play sound "Sounds/beep.mp3"
$ renpy.pause(1.0, hard=True)
ta "Oh, RogerCuck33 here thinks the white boy is cheating... He wants me to compare cock sizes... What a great idea Roger!"
scene webcam05 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Now let's fish out Darryl's anaconda... Mmmh, already so big and throbbing, a full twelve-inch weapon of ass destruction I'd say!"
ta "What will come out when I pull our newbie's jockstrap down I wonder? A banana and two pairs of oranges? Now THAT would be embarrassing!"
scene webcam06 with dissolve
play sound "Sounds/thud.mp3"
$ renpy.pause(1.0, hard=True)
ta "What a magnificent fuckstick! Now Roger will have to apologize for doubting this wonder stud's equipment... Is he bigger than Darryl you may ask?"
window hide
$ lust_points[21] += 1
$ score += 1
show lust01:
    xalign 0.6 yalign 0.5
    linear 1.0 yalign 0.3
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
scene webcam07 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Bring those fat fucksticks closer boys and let's put them side by side to compare their sizes..."
dl "I don't like where this is going Tanya..."
scene webcam08 with dissolve
$ renpy.pause(1.0, hard=True)
ta "OMG! I'm sorry Darryl, but that white boy has you beaten by a mile, what a giant piece of boymeat!"
dl "What? How can that be? Normally, the black guy is always bigger, this totally goes against established game conventions! Where is Slonique when you need him?!"
ta "Oh, stop crying, maybe he cums just a few trickles of slimy sterile drops, while YOU, our viewers already know, can deliver MASSIVE loads of virile juice!"
ta "So let's find out. Bring those meatclubs closer, I'm gonna wank you both together until you cover my body in your sticky cum!"
play sound "Sounds/tanyawank.mp3"
show tanyawankslow
show faster
call screen tanyawankslowday05
screen tanyawankslowday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("TanyaWankFastday05")
label TanyaWankFastday05:
hide faster
show tanyawankfast
show cum
call screen tanyawankfastday05
screen tanyawankfastday05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TanyaWankCumday05")

label TanyaWankCumday05:
stop sound
hide tanyawankfast
hide tanyawankslow
scene webcam09
$ renpy.pause(1.0, hard=True)
dl "I'm...almost there, get closer Tanya!"
ta "Yes Darryl, that's it, pump that big load all over your filthy wife's face..."
scene webcam10 with dissolve
play sound "Sounds/darrylcumming.mp3"
$ renpy.pause(1.0, hard=True)
dl "FUUUCK! That's it, take this you cum-hungry size-queen whore!"
ta "MMh, so delicious! And so MUCH of it too hubby!"
ta "I think white boy is ready to pop too... I'd better take care of him now that you're done..."
scene webcam11 with dissolve
$ renpy.pause(1.0, hard=True)
ta "That's it stud, let's see how much cream you've got stored in those giant balls of yours!"
scene webcam12 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
ta "OMG, it's like a firehose! Sssoooo much cum! Look at the size and force of that single streamer!"
scene webcam13 with dissolve
$ renpy.pause(1.0, hard=True)
ta "He's dousing me in ounces of boycum! But I want MORE! Yes, that's it, keep pumping that massive shaft and shooting that red-hot spunk all over me for our viewers!"
window hide
$ lust_points[21] += 1
$ score += 1
show lust01:
    xalign 0.7 yalign 0.5
    linear 1.0 yalign 0.3
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
scene webcam14 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Damn, I'm caked in your cream... Well, what do you think guys? Who came the most between hubby and the newbie?"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
play sound "Sounds/beep.mp3"
$ renpy.pause(1.0, hard=True)
ta "DanSubmissive79 claims hubby's load wasn't even a tenth of the mega-spunk shower the white boy delivered... I think he might be right."
dl "This is going too far Tanya, I'm being humiliated! I'm gonna beat the crap out of this kid you brought in!"
menu:
    "So who's the cuck now? I'm da man, I'm DA MAN!":
        scene webcam15 with dissolve
        $ renpy.pause(1.0, hard=True)
        dl "That's it, get out of my house, there is no way I'm letting you fuck my wife!"
        ta "Oh well, it seems our live show is over for tonight my horny viewers, I have to deal with some... domestic issues."
        play sound "Sounds/endcall.mp3" 
        stop music
        ta "Come on Darryl, calm down, our viewership doubled for this show alone, we're on the right track..."
        ta "Of course, I won't fuck this boy, you can trust your wife, right? [name], go home now, I think it was enough fun for tonight..."
        dl "I don't want to see your ugly face in here ever again you hear me?"
        p "Yeah, yeah, whatever cuck boy.... (chuckle)"
        scene webcamend with dissolve
        $ renpy.pause(1.0, hard=True)
        ta "Don't worry, I'll calm him down... You're welcome to come back another evening for some more fun [name]... (wink)"
        $ hour += 1
        jump EveningChoiceDay05

    "It was never my intention to humiliate you, your wife is fucking crazy!":
        scene webcam16 with dissolve
        $ renpy.pause(1.0, hard=True)
        ta "Hey, watch what you're saying!"
        window hide
        $ lust_points[21] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.6 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        scene webcam15 with dissolve
        $ renpy.pause(1.0, hard=True)
        dl "How dare you talk about my wife like that!"
        p "You just called her a whore live on cam a couple of minutes ago!"
        dl "That was different! Now get out of my house or I'll beat the crap out of you!"
        ta "Oh well, it seems our live show is over for tonight my horny viewers, I have to deal with some... domestic issues."
        play sound "Sounds/endcall.mp3" 
        stop music
        ta "Come on Darryl, calm down, our viewership doubled for this show alone, we're on the right track..."
        ta "As for you [name], you'd better leave and go back home now. It was enough fun for tonight."
        dl "I don't want to see your ugly face in here ever again you hear me?"
        p "Yeah, yeah, whatever you fucking weirdo.... (chuckle)"        
        scene webcamend with dissolve
        $ renpy.pause(1.0, hard=True)
        ta "Don't worry, I'll calm him down... You're welcome to come back another evening for some more fun [name]... (wink)"
        $ hour += 1
        menu:
            "Go back home":
                jump EveningChoiceDay05
            "Meet Laura on the beach" if (lauraritual05 == True) and (seencampfireday05 == False)  and (hour<=22):
                jump Campfire01Day05
            "Go back to Anna's house" if (seenannaevening05 == False) and (hour<=23):
                jump AnnaRoomDay05
                
label TanyaBed01Day05:
$ seentanyaday05 = True
if (tanyawebcamday03 == False):
    stop music
    play sound "Sounds/debbydoorbell.mp3"
    scene tanyahouse01 with dissolve
    $ renpy.pause(1.0, hard=True)
    ta "Oh, it's you again... I hope this time you won't chicken out..."
    dl "We don't need him, he's clearly useless to us!"
    ta "Let's just give him another chance... So, are you in boy for a bit of fun?"
    if (stamina <= 0) and (whitebull == True):
        menu:
            "Drink white bull (+2 stamina)":
                show whitebull
                show square
                play sound "Sounds/lost.mp3"
                "You gulped down your White Bull energy drink."
                hide square
                hide whitebull
                $ whitebull = False
                $ stamina += 2
                p "Ok, I'll do it! I'm da man, I'm DA MAN!"
                jump TanyaHouse02Day05
            "Bail out anyway":
                p "Err... Actually, I was just coming by to say hello, but I can't indulge in any sexual activities. You know, moral high ground and all that."
                ta "Pathetic! Get out of here and NEVER come back!"
                window hide
                $ lust_points[21] -= 1
                $ score -= 1
                show lustminus01:
                    xalign 0.6 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
                jump EveningChoiceDay05            
    if (stamina <= 0):
        p "Err... Actually, I was just coming by to say hello, but I can't indulge in any sexual activities. You know, moral high ground and all that."
        ta "Pathetic! Get out of here and NEVER come back!"
        window hide
        $ tanyanever = True
        $ lust_points[21] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.6 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump EveningChoiceDay05
    menu:
        "Ok, I'll do it! I'm da man, I'm DA MAN!":
            jump TanyaHouse02Day05
        "I'm out of here, you guys are crazy!":
            ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
            jump EveningChoiceDay05

if (tanyawebcamday03 == True):
    jump TanyaBed02Day05
    
label TanyaBed02Day05:
$ tanyawebcamday05 = True
stop music
play sound "Sounds/debbydoorbell.mp3"
scene tanyahouse05 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Oh, it's you again [name]... I'm so glad you came... Hubby is handcuffed to the bed. Which means... we can do whatever we like! (wink)"
if (stamina <= 0) and (whitebull == True):
    menu:
        "Drink white bull (+2 stamina)":
            show whitebull
            show square
            play sound "Sounds/lost.mp3"
            "You gulped down your White Bull energy drink."
            hide square
            hide whitebull
            $ whitebull = False
            $ stamina += 2
            p "Ok, I'll do it! I'm da man, I'm DA MAN!"
            jump TanyaCondomsDay05
        "Bail out anyway":
            p "Err... Actually, I was just coming by to say hello, but I can't indulge in any sexual activities. You know, moral high ground and all that."
            ta "Pathetic! Get out of here!"
            window hide
            $ lust_points[21] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.6 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            jump EveningChoiceDay05            
if (stamina <= 0):
    p "Err... Actually, I was just coming by to say hello, but I can't indulge in any sexual activities. You know, moral high ground and all that."
    ta "Pathetic! Get out of here!"
    window hide
    $ lust_points[21] -= 1
    $ score -= 1
    show lustminus01:
        xalign 0.6 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    jump EveningChoiceDay05
p "Alright! Let's do it then, I'm getting a massive boner just thinking about it!"
label TanyaCondomsDay05:
ta "I hope you brought some condoms. I am not letting that monstercock anywhere near my pussy if you're not wearing any..."
ta "And I doubt my hubby's \"Trojan Magnum XXL condoms\" will be big enough for that donkey-dick of yours."
if (condoms == True):
    p "Yeah, I'm equipped! I've got the biggest mega-condoms in the world! Made for super-studs like me..."
    ta "Oh fuck, that's so hot... Come in, I was about to turn the webcam on and start the show, I can't wait to feel that huge fuckstick!"
    window hide
    $ lust_points[21] += 2
    $ score += 2
    show lust02:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02    
    jump TanyaBed03Day05
if (condoms == False):
    p "Say again? Con... what?..."
    scene tanyahouse06 with dissolve
    $ renpy.pause(1.0, hard=True)
    ta "I can't believe this! What do they teach you at school? ALWAYS wear condoms!"
    p "Well, it's worked for me bareback so far... OK, I'll get some and come back tomorrow then... (sigh)"
    ta "You've just ruined my evening, now I'm gonna have to play with hubby's inadequate 12-incher. BORING! Get out of here!"
    window hide
    $ lust_points[21] -= 1
    $ score -= 1
    show lustminus01:
        xalign 0.6 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    $ tanyanocondoms = True
    jump EveningChoiceDay05
        
label TanyaBed03Day05:   
scene tanyabed01 with dissolve
play music "Sounds/tanyamusic.mp3"
$ renpy.pause(1.0, hard=True)
ta "Oh, look at poor little Darryl... All tied up and with his cock constrained in his tight briefs..."
dl "Untie me for fuck's sake Tanya! Wh... Why is this boy here again? I told you I never wanted to see him again in MY house!"
ta "He's here to get us lots of money... I'm sorry honeypot, but I read our viewers' requests last night on twatter and they all wanted to see me handle his young monster cock!"
dl "No please, don't do this to me, I'm all tied up, this is so humiliating!"
ta "Well that's the idea darling... Now hush, showtime is in a few seconds, [name], can you go and turn the webcam on please?"
p "Sure Tanya!"
$ tanyabedday05 = True
scene tanyabed02 with dissolve
$ renpy.pause(1.0, hard=True)    
ta "Just point the camera at me [name]... We are live in 3...2...1..."
ta "Hello, I'm back again my horny viewers... And as you can see, there have been some changes in the household since yesterday's visit by a young over-hung muscle stud...."
scene tanyabed03 with dissolve
$ renpy.pause(1.0, hard=True)    
ta "Poor hubby is handcuffed to the bed and he can't do anything... And our mystery guest is back!"
window hide
play sound "Sounds/beep.mp3"
$ renpy.pause(1.0, hard=True)
ta "Yes, RogerCuck33, this time it's going to be the real thing... Come over here [name], show our viewers your muscled body next to my incredible figure..."
scene tanyabed04 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Mmh, you're not wasting any time boy... Going straight for Tanya's big firm tits! And I can see that bulge getting even BIGGER!"
$ lust_points[21] += 1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01    
p "Yeah, let me show you while you play with your pussy and get it moist and ready for my massive ramrod."
scene tanyabed05 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Oh yes, I can see it trying to free itself and distending your mega-sized jockstrap to bursting point! Show it to our viewers in all its glory!"
p "That's right, over 18 inches of virile teenage fuckmeat, your husband is a pindick compared to me!"
dl "Hey! Untie me Tanya, I'm gonna kill that son of a bitch!"
ta "Let it go honey, there's nothing you can do except watch... Watch how a REAL stud fucks your wife!"
scene tanyabed06 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Damn, look at that giant pussy-pleaser my horny viewers! It's drooling pre-cum all over my corset. Maybe it's time to take it off then!"
$ lust_points[21] += 1
$ score += 1
show lust01:
    xalign 0.2 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
if (lust_points[21] >= 10):
    window hide
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust    
p "Oh yeah, let the viewers (and me) see those firm globes Tanya!"
ta "Of course, meanwhile, pop one of your mega-sized condoms on that beast!"
scene tanyabed07 with dissolve
$ renpy.pause(1.0, hard=True)
ta "My God, will you look at that hubby? I didn't even know they made condoms that size!"
play sound "Sounds/tanya01.mp3"
$ renpy.pause(3.0, hard=True)
p "It's a tight fit but it will hold, it says they are made from extra-strong latex."
if (lust_points[21] >= 10):
    jump TanyaBed04Day05
if (lust_points[21] <= 9):
    window hide
    $ lust_points[21] += 1
    $ score += 1
    show lust01:
        xalign 0.3 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01    
if (lust_points[21] >= 10):
    window hide
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust    

label TanyaBed04Day05:
$ tanyablow = False
$ tanyaride = False
scene tanyabed09 with dissolve
$ renpy.pause(1.0, hard=True)
ta "First, I want you to loosen my anus with that monster dong. Anal isn't cheating, right hubby?"
dl "What the fuck are you talking about? Of course it's cheating!"
ta "Too late darling, I can feel it plunging into my backside. AAAH!"
scene tanyabed09b with dissolve
$ renpy.pause(1.0, hard=True)
ta "Oh fuck, he's so rough, he's really giving it to me hubby, sssooo good!"
dl "Why are you doing this to me Tanya? This is so humiliating!"
ta "Oh, stop moaning. Here, you can suckle on my big fat titties like the baby you are while this boy wonderstud gives me the anal fucking of a lifetime!"
scene tanyabed08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready for my big cock Tanya?"
ta "Oh, yeah stud, fuck me hard with your young, virile fuckstick, give it to me please!"
label TanyaBed04Day05b:
play sound "Sounds/tanya02.mp3"
scene tanyabed08b with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed08 with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed08b with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed08 with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed08b with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed08 with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed08b with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed08 with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed08b with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed08 with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed08b with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed08 with dissolve
$ renpy.pause(0.3, hard=True)
ta "Oh my God hubby, this boy is giving me orgasms like you never could! AAAH!"
menu:
    "Repeat":
        jump TanyaBed04Day05b
    "Move on":
        pass
p "Your arse is so tight, I think I'm gonna blow, I can't stop it, AAAH!"
play sound "Sounds/ryancumming.mp3"
ta "So soon? But we still have over half an hour of showtime!"
p "Don't worry, it was just a tiny load, it happens sometimes when I'm super excited, but I'm still rock-hard and ready for more!"
ta "Damn kid, hubby here never manages to stay hard after cumming. Bring that giant pole over here boy!"
scene tanyabed10 with dissolve
$ renpy.pause(1.0, hard=True)
ta "You call THAT a \"tiny load\"? It's gigantic! I hope our viewers can see it..."
ta "Look hubby, how heavy it feels, there must be like twenty of your loads sloshing around in there!"
play sound "Sounds/beep.mp3"
$ renpy.pause(1.0, hard=True)
ta "DanSubmissive79 says it might be even more... And he suggests you drink it..."
dl "No fucking way! That is totally gay!"
ta "Alright, alright, I'll just keep that filled condom for later then... I sure want a taste of it!"
p "I'm warning you I don't have any more condoms though..."
ta "The hell with condoms anyway, I want to ride that monster bareback from now on! Just take me, my body belongs to you stud!"
menu:
    "Get a blowjob" if (tanyablow == False):
        ta "Good idea, and let's do it right in front of Darryl's face, you don't mind do you hubby?"
        dl "Of course I fucking mind! Don't do this to me!"
        ta "Sorry, but that's what our viewers want and that's what we'll give them..."
        jump TanyaBlowjobDay05
    "Fuck her above Darryl" if (tanyaride == False):
        jump TanyaRideDay05
    
label TanyaBlowjobDay05:
$ tanyablow = True
scene tanyabed11 with dissolve    
$ renpy.pause(1.0, hard=True)
ta "Just the tip is filling up my mouth entirely. Can you see that hubby?"
dl "Stop it Tanya, you're torturing me!"
scene tanyabed11b with dissolve    
$ renpy.pause(1.0, hard=True)
ta "It's so big Darryl, I can barely take a third of his young monster dong! And I can deepthroat you easily..."
dl "I beg you to stop comparing me to this stu... I mean little prick!"
ta "Just watch me blow this STUD! That's what you were going to say hubby, right?"
label TanyaBlowjobDay05b:
play sound "Sounds/tanyasuck.mp3"
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11 with dissolve    
$ renpy.pause(0.3, hard=True)
scene tanyabed11b with dissolve    
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump TanyaBlowjobDay05b
    "Get her to take MORE of your cock!":
        p "I think you can take more Tanya, come on, do it! AAAH!"
        scene tanyabed11c with dissolve    
        play sound "Sounds/hallesuck02.mp3"
        $ renpy.pause(3.0, hard=True)
        dl "I can't watch this! This is too humiliating!"
        jump TanyaBlowjobDay05b
    "Fuck her above Darryl" if (tanyaride == False):
        jump TanyaAboveDay05
    "Let her ride you like a wild bronco" if (tanyaride == True) and (tanyablow == True):
        jump TanyaRideDay05
        
label TanyaAboveDay05:
$ tanyaride = True
scene tanyabed12 with dissolve
play sound "Sounds/tanya04.mp3"
$ renpy.pause(3.0, hard=True)
ta "Come and stick that big fucking cock in me!"
scene tanyabed13 with dissolve
$ renpy.pause(3.0, hard=True)
p "Ready to have your pussy ruined for your hubby by a way bigger cock than his?"
ta "Ooh, fuck yeah!"
label TanyaAboveDay05b:
scene tanyabed14 with dissolve
play sound "Sounds/tanya05.mp3"
$ renpy.pause(1.0, hard=True)
scene tanyabed14b with dissolve
$ renpy.pause(1.0, hard=True)
scene tanyabed14 with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed14b with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed14 with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed14b with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed14 with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed14b with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed14 with dissolve
$ renpy.pause(0.3, hard=True)
scene tanyabed14b with dissolve
$ renpy.pause(0.3, hard=True)
ta "Fa-aaster! Destroy my marital cunt!"
play sound "Sounds/tanya05.mp3"
scene tanyabed14
$ renpy.pause(0.5, hard=True)
scene tanyabed14b
$ renpy.pause(0.5, hard=True)
scene tanyabed14
$ renpy.pause(0.5, hard=True)
scene tanyabed14b
$ renpy.pause(0.5, hard=True)
scene tanyabed14
$ renpy.pause(0.5, hard=True)
scene tanyabed14b
$ renpy.pause(0.5, hard=True)
scene tanyabed14
$ renpy.pause(0.5, hard=True)
scene tanyabed14b
$ renpy.pause(0.5, hard=True)
scene tanyabed14
$ renpy.pause(0.5, hard=True)
scene tanyabed14b
$ renpy.pause(0.5, hard=True)
scene tanyabed14
$ renpy.pause(0.5, hard=True)
scene tanyabed14b
$ renpy.pause(0.5, hard=True)
scene tanyabed14
$ renpy.pause(0.5, hard=True)
scene tanyabed14b
$ renpy.pause(0.5, hard=True)
scene tanyabed14
$ renpy.pause(0.5, hard=True)
scene tanyabed14b
$ renpy.pause(0.5, hard=True)
scene tanyabed14
$ renpy.pause(0.5, hard=True)
scene tanyabed14b
$ renpy.pause(0.5, hard=True)
scene tanyabed14
$ renpy.pause(0.5, hard=True)
scene tanyabed14b
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        jump TanyaAboveDay05b
    "Get a blowjob" if (tanyablow == False):
        ta "Good idea, and let's do it right in front of Darryl's face, you don't mind do you hubby?"
        dl "Of course I fucking mind! Don't do this to me!"
        ta "Sorry, but that's what our viewers want and that's what we'll give them..."
        jump TanyaBlowjobDay05
    "Let her ride you like a wild bronco" if (tanyaride == True) and (tanyablow == True):
        jump TanyaRideDay05
    

label TanyaRideDay05:
scene tanyabed15 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Let me ride that donkey-dick stud! I can't wait to feel that monstrous rock-hard member deep inside of me while my helpless hubby watches on!"
dl "No, don't fuck him please Tanya!"
ta "Stop pretending you don't like it honey, I can see your erection distending your tight briefs... Just watch and enjoy the ride, I sure will!"
play music "Sounds/tanyafuckslow.mp3"
show tanyafuckslow
show faster
call screen tanyafuckslow05
screen tanyafuckslow05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("TanyaFuckFast05")
label TanyaFuckFast05:
hide faster
play music "Sounds/tanyafuckfast.mp3"
show tanyafuckfast
show cum
call screen tanyafuckfast05b
screen tanyafuckfast05b:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TanyaFuckCum05")

label TanyaFuckCum05:
hide tanyafuckfast
hide tanyafuckslow
stop music
scene tanyacum01
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "OOOH, I'm cumming so hard....AAAH"
ta "Honey, this boy is cumming like a breeding stallion inside your wife's pussy! There's just sssooo much of it, pull out boy, you're bloating me!"
scene tanyacum02 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/cumming.mp3"
$ renpy.pause(2.0, hard=True)
ta "You're STILL cumming? Damn, what a spunk machine [name]! Yeah, cover my marital bedsheets with your sweet cream!"
scene tanyacum03 with dissolve
$ renpy.pause(1.0, hard=True)
ta "That's it, hose that cream all over the place, all over my body! Look at that load hubby, nothing like yours, right?"
dl "Get him to stop, I'm getting sprayed by his filthy cum!"
play sound "Sounds/cumming.mp3"
$ renpy.pause(2.0, hard=True)
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
scene tanyacum04 with dissolve
ta "Damn boy, what a fucking load! I'm covered in spunk.... Darryl is too, and I can tell he came in his tight briefs...."
dl "I DID NOT! I... thought this was disgusting! I'm gonna kill that son of a bitch, untie me Tanya!"
ta "Shhush honey, let this boy go home now and... I'll let you lick his creampie out of me."
dl "What? What makes you think I want to do such a filthy thing?"
ta "Your spoilt briefs don't lie, you enjoyed it, I can tell... Let the show go on!"
p "I don't think I ever came that much in my life... Phew! I'd better get going now..."
$ renpy.pause(1.0, hard=True)
$ backdoor += 1
if (hallefucked == True) and (achievement.has("colonizer") == False):
    show achievement05:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement05
    $ achievement.grant("colonizer")
ta "Well, my horny viewers, I hope you enjoyed the show tonight, I did for sure, I came ssooo many times on that massive love muscle..."
ta "Say goodbye to our viewers hubby, I'll get your handcuffs off so you can help me clean those semen-stained sheets... My way!"
if (jenniferfucked == True) and (achievement.has("cuckmaker") == False):
    show achievement12:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement12
    $ achievement.grant("cuckmaker")
if (francinefucked == True) and (debbyfucked == True) and (teaganfucked == True) and (achievement.has("king") == False):
    show achievement13:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement13
    $ achievement.grant("king")
$ hour += 1
$ tanyafucked = True
if (tanyajosewin == False):
    p "(She didn't notice I took a picture of us... Now I'll send it to José)."
    $ tanyawin = True

menu:
    "Go back home":
        jump EveningChoiceDay05
    "Meet Laura on the beach" if (lauraritual05 == True) and (seencampfireday05 == False) and (hour <= 22):
        jump Campfire01Day05
    "Go back to Anna's house" if (seenannaevening05 == False) and (hour<=23):
        jump AnnaRoomDay05


label Campfire01Day05:
$ seencampfireday05 = True

if (damianexpelled == False):
    if (seencampfireday03 == False) and (seencampfireday04 == False):
        jump Campfire01Day05First
    if (ritualwords == True):
        if (((seencampfireday03 == True) and (seencampfireday04 == False)) or ((seencampfireday03 == False) and (seencampfireday04 == True))):
            jump Campfire01Day05Second
        if (seencampfireday03 == True) and (seencampfireday04 == True):
            $ MCturn = True
            jump Campfire01Day05First
    if (ritualwords == False):
            jump Campfire01Day05First
if (damianexpelled == True):
    jump Campfire01Day05ThirdNoDamian

label Campfire01Day05ThirdNoDamian:
scene campfire01b with dissolve
play music "Sounds/campfire.mp3"
$ renpy.pause(1.0, hard=True)
la "Oh, there you are, good timing, we were just about to begin the ritual...Without Damian."
p "Why didn't he show up?"
la "His parents grounded him for having been expelled from our school. Good riddance I say. I just need you to perform the ritual."
scene campfire03b with dissolve
$ renpy.pause(1.0, hard=True)
la "(whispering) Evil, live, live, evil... Evil, live, live, evil..."
fc "Hein? Qu'est-ce-qu'il se passe?"
p "Evil, live, live, evil... Evil, live, live, evil..."
la "Te avio päläfertiilam. Éntölam kuulua, avio päläfertiilam!"
window hide
play sound "Sounds/magic.mp3"
$ renpy.pause(1.0, hard=True)
scene campfire04bb with dissolve
$ renpy.pause(1.0, hard=True)
la "I curse you mother, I curse you father!"
play sound "Sounds/magic.mp3"
$ renpy.pause(1.0, hard=True)
show campfire04c with dissolve
la "Your turn [name]. Curse anyone you like..."
p "I curse thee, José!"
"Choose a girl to go with José's curse (-3 challenger lust points for her):"
menu:
    "Remind me of the stats first...":
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
        scene campfire04
        show campfire04c
        jump ChooseGirlCurseDay05
    "Brittany":
        show brittanysprite at CampfirePosition
        $ lust_pointsB[1] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        hide brittanysprite
        jump CampFireEndNoDamianDay05
    "Anna":
        show annasprite at CampfirePosition
        $ lust_pointsB[0] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndNoDamianDay05        
    "Viviane":
        show vivianesprite at CampfirePosition
        $ lust_pointsB[23] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndNoDamianDay05
    "Daniella":
        show daniellasprite at CampfirePosition
        $ lust_pointsB[4] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndNoDamianDay05
    "Doris":
        show dorissprite at CampfirePosition
        $ lust_pointsB[6] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndNoDamianDay05
    "Pamela":
        show pamelasprite at CampfirePosition
        $ lust_pointsB[18] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndNoDamianDay05

label CampFireEndNoDamianDay05:
scene campfire09bb with dissolve
$ renpy.pause(1.0, hard=True)
la "The fireball is getting smaller and smaller..."
p "But my fireballs are getting fuller and fuller right now..."
if (laurafucked == True):
    la "That is so corny... And anyway, Joséphine is still here, we can't do anything in front of her..."
    p "Yeah, I guess not. Well, I'd better get going, I'll see you tomorrow Laura!"
    la "Have a good night. Not full of nightmares like mine."
    $ hour += 1
    jump EveningChoiceDay05

if (laurafucked == False):
    la "That is so corny... And anyway, Joséphine is still here, we can't do anything in front of her..."
    p "Maybe we can get rid of her..."
    la "I like your thinking. I'll talk to her."
    scene campfire09bc with dissolve
    $ renpy.pause(1.0, hard=True)
    la "Joséphine, tu peux nous laisser seuls s'il te plaît? J'ai besoin de parler avec [name]..."
    fc "D'accord. Je vais rentrer chez moi, il se fait tard."
    scene campfire07 with dissolve
    $ renpy.pause(1.0, hard=True)
    la "There you go... Now it's just you and me..."
    $ lust_points[13] +=1
    $ score += 1
    show lust01:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    la "Why don't you sit next to me for a little while... I'm starting to get a bit cold..."
    jump CampfireLaura01Day05

label Campfire01Day05First:
scene campfire01 with dissolve
play music "Sounds/campfire.mp3"
$ renpy.pause(1.0, hard=True)
la "Oh, there you are, good timing, we were just about to begin the ritual..."
scene campfire02 with dissolve
$ renpy.pause(1.0, hard=True)
go "Now be careful Laura, it can be very dangerous, we don't want this to get out of hands..."
la "Let me do this my way Damian, I know perfectly well what I'm doing, it is time for the world to pay. DEATH TO ALL BUT METAL!"
scene campfire03 with dissolve
$ renpy.pause(1.0, hard=True)
la "(whispering) Evil, live, live, evil... Evil, live, live, evil..."
go "(whispering) Evil, live, live, evil... Evil, live, live, evil..."
fc "Hein? Qu'est-ce-qu'il se passe?"
menu:
    "Get the hell out of here":
        jump CampfireLeftDay05
    "Whisper the words":
        p "Evil, live, live, evil... Evil, live, live, evil..."
        $ ritualwords = True
        jump Campfire02Day05
    "Just continue watching":
        $ ritualwords = False
        jump Campfire02Day05

label Campfire02Day05:
scene campfire03 with dissolve
$ renpy.pause(1.0, hard=True)
la "Te avio päläfertiilam. Éntölam kuulua, avio päläfertiilam!"
window hide
play sound "Sounds/magic.mp3"
$ renpy.pause(1.0, hard=True)
scene campfire04 with dissolve
$ renpy.pause(1.0, hard=True)
go "Wicked!"
show campfire04b with dissolve
la "I curse you mother, I curse you father!"
play sound "Sounds/magic.mp3"
$ renpy.pause(1.0, hard=True)
if (ritualwords == True):
    show campfire04c with dissolve
    la "Your turn [name]. Curse anyone you like..."
    menu:
        "Curse Damian":
            jump DamianCurseDay05
        "Curse José":
            jump JoseCurseDay05
        "Don't curse anyone, this is too satanic":
            jump NoCurseDay05

if (ritualwords == False):
    la "Your turn Damian..."
    go "I curse you WORLD... DEATH TO ALL BUT METAL!"
    la "DEATH TO ALL BUT METAL!"
    scene campfire05 with dissolve
    $ renpy.pause(1.0, hard=True)
    "You feel a stinging pain in your body..."
    if (stamina >=1):
            scene campfire05b with flash
            $ stamina -=1
            show staminaminus01:
                xalign 0.2 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/panting.mp3"
            $ renpy.pause(2, hard=True)
            hide staminaminus01
    scene campfire05c with dissolve
    $ renpy.pause(1.0, hard=True)
    la "Looks like your curse worked Damian! [name] is aching and the black girl left fleeing..."
    p "I...need to go home..."
    show campfire05d with dissolve
    la "Sorry [name], you're clearly not strong enough inside your mind to deal with this ritual..."
    $ hour += 1
    stop music
    menu:
        "Go back home":
            jump EveningChoiceDay05
        "Go to Tanya's House" if (discovertanya == True) and (tanyafucked == False) and (seentanyaday05 == False) and (hour <= 23):
            jump TanyaHouseDay05
    
label DamianCurseDay05:
p "I curse thee, Damian!"
scene campfire06 with dissolve
window hide
play sound "Sounds/magic.mp3"
$ renpy.pause(1.0, hard=True)
go "What the fuck? Hey, what's going on?... This thing is following me, AAAHH!"
scene campfire07 with dissolve
$ renpy.pause(1.0, hard=True)
la "Wow, [name], that was so evil of you... I liked it, it was awesome..."
window hide
if (lust_points[13] ==9):
    $ lust_points[13] +=1
    $ score += 1
    show lust01:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[13] <=8):
    $ lust_points[13] +=2
    $ score += 2
    show lust02:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
la "Why don't you sit next to me for a little while... I'm starting to get a bit cold..."
jump CampfireLaura01Day05

label JoseCurseDay05:
p "I curse thee, José!"
"Choose a girl to go with José's curse (-3 challenger lust points for her):"
label ChooseGirlCurseDay05:
menu:
    "Remind me of the stats first...":
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
        scene campfire04
        show campfire04c
        jump ChooseGirlCurseDay05
    "Brittany":
        show brittanysprite at CampfirePosition
        $ lust_pointsB[1] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        hide brittanysprite
        jump CampFireEndDay05
    "Maddy":
        show maddysprite at CampfirePosition
        $ lust_pointsB[14] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay05        
    "Nikki":
        show nikkisprite at CampfirePosition
        $ lust_pointsB[17] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay05
    "Frieda":
        show friedasprite at CampfirePosition
        $ lust_pointsB[8] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay05
    "Kate":
        show katesprite at CampfirePosition
        $ lust_pointsB[11] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay05
    "Laura":
        show laurasprite at CampfirePosition
        $ lust_pointsB[13] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        la "God I hate José... Such a douchebag..."
        jump CampFireEndDay05


label NoCurseDay05:
p "I'm good, no need to curse anyone."
scene campfire07b with dissolve
$ renpy.pause(1.0, hard=True)
la "Humpf. How disappointing of you... Get out of here, you're not welcome to stay anymore."
$ lust_points[13] -=1
$ score -= 1
show lustminus01:
    xalign 0.6 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/less.mp3"
$ renpy.pause(2, hard=True)
hide lustminus01
go "Chicken shit loser!"
$ hour += 1
stop music
jump EveningChoiceDay05

label CampFireEndDay05:
scene campfire09 with dissolve
$ renpy.pause(1.0, hard=True)
la "The fireball is getting smaller and smaller..."
go "Hey, I didn't get to curse anyone, that's not fair! Why did you choose [name] to go first, I'm a REAL goth, not a wannabe one like him!"
menu:
    "You got a problem with that dipshit?":
        scene campfire09b with dissolve
        $ renpy.pause(1.0, hard=True)
        la "Hey hey, calm down boys! Next time, Damian will go first. It's true that he's  the founder of our movement..."
        go "That's it, it's finished for tonight, everyone go back home, I'll decide what we do tomorrow."
        la "Of course Damian. We'll see how YOU manage to summon demons tomorrow..."
        go "Well, err... yeah, we'll see..."
        scene campfire09c with dissolve
        $ renpy.pause(1.0, hard=True)        
        la "Goodnight [name], I hope you enjoyed this ritual... Remember, not a word to anyone. We need to keep this secret."
        p "Of course Laura, my lips are sealed... Well, until they end up next to yours..."
        go "Oh, P--lease! That's so corny..."
        jump EveningChoiceDay05        
    "Laura is in charge, how dare you criticize her?":
        scene campfire09c with dissolve
        $ renpy.pause(1.0, hard=True)
        go "I see, I'm disbanding the Hardcox Goth Club then, I'm outta here, you guys suck!"
        "Damian leaves, fuming."
        scene campfire07 with dissolve
        $ renpy.pause(1.0, hard=True)
        la "I think you really pissed him off [name]... Oh well, he was too controlling anyway. A real goth is the Master of his own destiny!"
        $ lust_points[13] +=1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        la "Why don't you sit next to me for a little while... I'm starting to get a bit cold..."
        jump CampfireLaura01Day05
                
label CampfireLaura01Day05:
scene campfire10 with dissolve
$ renpy.pause(1.0, hard=True)
la "I feel strange, like I enjoy your company. Isn't that weird... Mmh, screw it, kiss me!"
scene campfire11 with dissolve
play sound "Sounds/kissing.mp3"
$ renpy.pause(1.0, hard=True)
if (lust_points[13] <= 9):
    $ renpy.pause(1.0, hard=True)
    $ lust_points[13] +=1
    $ score += 1
    show lust01:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[13] >= 10):
    $ renpy.pause(1.0, hard=True)        
    show epiclust:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust 
    la "I... really like you... Even though I'm supposed to hate everyone in the world..."
    jump LauraFuck01Day05

label LauraCampFireChoiceDay05:
scene campfire12 with dissolve
$ renpy.pause(1.0, hard=True)
la "That was...just a one-off thing, okay? Even if... I did enjoy it."
menu:
    "I respect your goth-like decision...":
        la "Good... Because goths don't like to be pushed around... It's getting late [name], I have to go home, even if I hate my parents..."
        p "Sure, same here. Gotta go back to my lousy family and all... See you tomorrow Laura!"
        $ hour += 1
        menu:
            "Go back home":
                jump EveningChoiceDay05
            "Go to Tanya's House" if (discovertanya == True) and (tanyafucked == False) and (seentanyaday05 == False) and (hour <= 23):
                jump TanyaHouseDay05
    "Kiss her again forcefully":
        scene campfireforcedkiss with dissolve
        $ renpy.pause(1.0, hard=True)
        la "Hey! Who do you think you are! Get off me and get the hell out of here [name]!"
        $ lust_points[13] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.6 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        $ hour += 1
        menu:
            "Go back home":
                jump EveningChoiceDay05
            "Go to Tanya's House" if (discovertanya == True) and (tanyafucked == False) and (seentanyaday05 == False)  and (hour <= 23):
                jump TanyaHouse01Day05
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
        jump LauraPendulumDay05
    "Spray yourself with pheromones" if (pheromone == True):
        scene campfirehypno with dissolve
        $ renpy.pause(1.0, hard=True)
        play sound "Sounds/spray.mp3"
        $ renpy.pause(1.0, hard=True)
        la "Why did you spray yourself with perfume? I can't smell a thing with that sea breeze..."
        p "(Ah, shit, didn't think of that...)"
        show pheromone
        show square
        play sound "Sounds/lost.mp3"
        "You lost a pheromone spray."
        hide square
        hide pheromone
        $ pheromone = False
        jump LauraCampFireChoiceDay05

label LauraPendulumDay05:
scene campfirehypno with dissolve
show pendulum03
$ renpy.pause(1.0, hard=True)
p "Just watch this pendulum as I wiggle it in front of your eyes Laura..."
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
if (lust_points[13] ==8):
    window hide
    $ lust_points[13] += 2
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
    jump LauraFuck01Day05
if (lust_points[13] ==9):
    window hide
    $ lust_points[13] += 1
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
    jump LauraFuck01Day05  

label LauraFuck01Day05:
stop music
scene campfire13 with dissolve
$ renpy.pause(1.0, hard=True)
la "I... have an uncontrollable urge to... get close to you... Don't resist, it's futile..."
if (stamina <= 0) and (whitebull == False):
    p "(Shit, my stamina is too low...  I need to find an excuse)"
    p "You know what... I'm a goth, right? Then I decide not to have sex with you. How's that for being a goth, hey?"
    la "Wh... What the fuck??? That's not what I meant by being a goth! God, I HATE YOU, you've ruined my evening, get outta here!"
    menu:
        "Go back home":
            jump EveningChoiceDay05
        "Go to Tanya's House" if (discovertanya == True) and (tanyafucked == False) and (seentanyaday05 == False)  and (hour <= 23):
            jump TanyaHouseDay05
if (stamina <= 0) and (whitebull == True):
    p "Now is the time to drink some White Bull..."
    show whitebull
    show square
    play sound "Sounds/lost.mp3"
    "You drank an energy drink. The bottle is now empty."
    hide square
    hide whitebull
    $ whitebull = False
    $ stamina += 2
p "Oh, I won't resist, don't worry Laura! (Bingo!)"
la "Take those shorts off... I want to see your demonic pillar of lust!"
scene campfire14 with dissolve
$ renpy.pause(1.0, hard=True)
la "Sweet Belzebuth! This thing is HUGE, like... out of this world!"
p "Yes, do something about it Laura, I am possessed by a satanic desire to fuck you so hard!"
la "Alright [name], let me take care of that bad boy..."
label LauraFuck01Day05b:
scene campfire16 with dissolve
play sound "Sounds/lauratitfuck.mp3"    
$ renpy.pause(1.0, hard=True)
scene campfire16b with dissolve
$ renpy.pause(0.3, hard=True)
scene campfire16 with dissolve
$ renpy.pause(0.3, hard=True)
scene campfire16b with dissolve
$ renpy.pause(0.3, hard=True)
scene campfire16 with dissolve
$ renpy.pause(0.3, hard=True)
scene campfire16b with dissolve
$ renpy.pause(0.3, hard=True)
scene campfire16 with dissolve
$ renpy.pause(0.3, hard=True)
scene campfire16b with dissolve
$ renpy.pause(0.3, hard=True)
scene campfire16 with dissolve
$ renpy.pause(0.3, hard=True)
p "Faster please, the demon in me demands it!"  
play sound "Sounds/lauratitfuck.mp3"    
scene campfire16b with dissolve
$ renpy.pause(0.2, hard=True)
scene campfire16 with dissolve
$ renpy.pause(0.2, hard=True)
scene campfire16b with dissolve
$ renpy.pause(0.2, hard=True)
scene campfire16 with dissolve
$ renpy.pause(0.2, hard=True)
scene campfire16b with dissolve
$ renpy.pause(0.2, hard=True)
scene campfire16 with dissolve
$ renpy.pause(0.2, hard=True)
scene campfire16b with dissolve
$ renpy.pause(0.2, hard=True)
scene campfire16 with dissolve
$ renpy.pause(0.2, hard=True)
scene campfire16b with dissolve
$ renpy.pause(0.2, hard=True)
scene campfire16 with dissolve
$ renpy.pause(0.2, hard=True)
$ renpy.pause(0.2, hard=True)
scene campfire16 with dissolve
$ renpy.pause(0.2, hard=True)

menu:
    "Repeat":
        jump LauraFuck01Day05b
    "Move on":
        pass

scene campfire15 with dissolve
play sound "Sounds/laura01.mp3"    
$ renpy.pause(8.0, hard=True)
la "You seem to have liked that... Your cock has turned into a steel-hard pole!"
menu:
    "Make it spew its evil load with your hands!" if (stamina >=2):
        jump LauraFuck03Day05
    "I need to put it into something soft and warm!":
        jump LauraFuck02Day05
    "Tease it with your fingernails!" if (stamina ==1):
        jump LauraFuck03Day05

label LauraFuck03Day05:
$ lauratease = True
scene campfiretease01 with dissolve
$ renpy.pause(1.0, hard=True)
la "How about I scratch it like that.... all the way up..."
play sound "Sounds/lauratease01.mp3"
scene campfiretease02 with dissolve
$ renpy.pause(2.0, hard=True)
scene campfiretease01 with dissolve
$ renpy.pause(2.0, hard=True)
la "And down again... Yes, you like that, your cock is trembling..."
label LauraFuck03Day05b:
play sound "Sounds/lauratease02.mp3"
scene campfiretease02 with dissolve
$ renpy.pause(1.0, hard=True)
scene campfiretease01 with dissolve
$ renpy.pause(1.0, hard=True)
scene campfiretease02 with dissolve
$ renpy.pause(1.0, hard=True)
scene campfiretease01 with dissolve
$ renpy.pause(1.0, hard=True)
scene campfiretease02 with dissolve
$ renpy.pause(1.0, hard=True)
scene campfiretease01 with dissolve
$ renpy.pause(1.0, hard=True)
scene campfiretease02 with dissolve
$ renpy.pause(1.0, hard=True)
scene campfiretease01 with dissolve
$ renpy.pause(1.0, hard=True)
scene campfiretease02 with dissolve
$ renpy.pause(1.0, hard=True)
scene campfiretease01 with dissolve
$ renpy.pause(1.0, hard=True)
scene campfiretease02 with dissolve
$ renpy.pause(1.0, hard=True)
scene campfiretease01 with dissolve
$ renpy.pause(1.0, hard=True)
menu:
    "Repeat":
        jump LauraFuck03Day05b
    "Move on":
        pass
if (stamina >= 2):
    scene campfiretease03 with dissolve
    play sound "Sounds/ryancumming.mp3"
    $ renpy.pause(2.0, hard=True)
    la "Wow, that's a huge amount of cum... You truly are possessed... Possessed by the Demon of Sex!"
    scene campfiretease04 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "I've got some more for you, get your mouth over the tip... RHAAAA! Fondle my balls at the same time to coax a massive load out of me!"
    play sound "Sounds/cumming.mp3"
    la "Glubb... too...tooo much!"
    scene campfiretease05 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Never too much cum, here have some more, get the whole head in! OOOOH, I'm cumming so fucking HARD!"
    scene campfiretease06 with dissolve
    $ renpy.pause(1.0, hard=True)
    la "Oh [name], you came SSOOO MUCH! I can't believe the incredible amount of baby-batter you can produce! You're a horny little devil!"    
    $ stamina -=1
    show staminaminus01:
        xalign 0.2 yalign 0.3
        linear 1.0 yalign 0.5
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
    p "I hope you are too, because I'm still rock-hard and needing a soft and warm pussy!"
    la "My pussy is ready for that demonic pole of yours... Let me ride it!"
    jump LauraFuck02Day05b
if (stamina == 1):
    p "Enough, I can't take much more of that teasing, I need to put my cock into something soft and warm! And very deep preferably..."    
    la "Such eagerness... Alright, I will ride that horsecock cowboy!"
    jump LauraFuck02Day05b
label LauraFuck02Day05:
if (lauratease == False):
    la "I think I should first tease that throbbing cock with my fingernails..."
    p "Ah, err. Ok."
    jump LauraFuck03Day05
    
label LauraFuck02Day05b:
stop music
play sound "Sounds/campfire.mp3"
play music "Sounds/laurafuckslow.mp3"
show laurafuckslow
show faster
call screen laurafuckslowDay05
screen laurafuckslowDay05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("LauraFuckFastDay05")

label LauraFuckFastDay05:
stop movie
hide faster
play music "Sounds/laurafuckfast.mp3"
show laurafuckfast
show cum
call screen laurafuckfastDay05
screen laurafuckfastDay05:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("LauraFuckCumDay05")
    
label LauraFuckCumDay05:
hide laurafuckslow
hide laurafuckfast
stop music
play music "Sounds/campfire.mp3"
scene campfirefuckcum01
play sound "Sounds/cumming.mp3"
$ renpy.pause(2.0, hard=True)
la "Go on [name], spew that demonic load inside me!"
window hide
$ renpy.pause(2.0, hard=True)
la "Take it out and cover my back with your hot cream!"
scene campfirefuckcum02 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
la "My God, my pussy is overfilled with cum and you're still shooting massive wads up in the air!!! More, MORE!"
scene campfirefuckcum03 with dissolve
$ renpy.pause(1.0, hard=True)
$ stamina -=1
show staminaminus01:
    xalign 0.3 yalign 0.3
    linear 1.0 yalign 0.5
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ laurafucked = True
if (katefucked == True) and (maddyfucked == True)and (friedafucked == True) and (achievement.has("classroom") == False):
    show achievement03:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement03
    $ achievement.grant("classroom")
la "Kiss me while I'm covered in your sticky spunk... This was so amazing [name]!"
play sound "Sounds/kissing.mp3"
$ renpy.pause(1.0, hard=True)
if (laurajosewin == False):
    $ laurawin = True
$ fuckedschoolgirlDay05 = True
$ hour += 1
la "I should go back home now, after an evening dip in the sea to clean myself of your MASSIVE load (giggles). See you tomorrow [name]!"
p "Good night Laura, see you tomorrow!"
menu:
    "Go back home":
        jump EveningChoiceDay05
    "Go to Tanya's House" if (discovertanya == True) and (tanyafucked == False) and (seentanyaday05 == False)  and (hour <= 23):
        jump TanyaHouseDay05
        
label Campfire01Day05Second:
scene campfire01 with dissolve
play music "Sounds/campfire.mp3"
$ renpy.pause(1.0, hard=True)
la "Oh, there you are, good timing, we were just about to begin the ritual..."
scene campfire02 with dissolve
$ renpy.pause(1.0, hard=True)
go "Remember, it's my turn to start the curse this time, not this goth wannabe..."
la "Sure Damian, be ready for it once I finish the incantation. DEATH TO ALL BUT METAL!"
scene campfire03 with dissolve
$ renpy.pause(1.0, hard=True)
la "(whispering) Evil, live, live, evil... Evil, live, live, evil..."
go "(whispering) Evil, live, live, evil... Evil, live, live, evil..."
fc "Hein? Qu'est-ce-qu'il se passe?"
p "Evil, live, live, evil... Evil, live, live, evil..."
scene campfire03 with dissolve
$ renpy.pause(1.0, hard=True)
la "Te avio päläfertiilam. Éntölam kuulua, avio päläfertiilam!"
window hide
play sound "Sounds/magic.mp3"
$ renpy.pause(1.0, hard=True)
scene campfire04 with dissolve
$ renpy.pause(1.0, hard=True)
go "Wicked!"
show campfire04b with dissolve
la "I curse you mother, I curse you father!"
play sound "Sounds/magic.mp3"
$ renpy.pause(1.0, hard=True)
la "Your turn Damian..."
go "I curse you WORLD... DEATH TO ALL BUT METAL!"
la "DEATH TO ALL BUT METAL!"
scene campfire05 with dissolve
$ renpy.pause(1.0, hard=True)
"You feel a stinging pain in your body..."
if (stamina >=1):
    scene campfire05b with flash
    $ stamina -=1
    show staminaminus01:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
scene campfire05c with dissolve
$ renpy.pause(1.0, hard=True)
la "Looks like your curse worked Damian! [name] is aching and the black girl left fleeing..."
p "I...need to go home..."
show campfire05d with dissolve
la "Sorry [name], you're clearly not strong enough inside your mind to deal with this ritual..."
$ hour += 1
stop music
menu:
    "Go back home":
        jump EveningChoiceDay05
    "Go to Tanya's House" if (discovertanya == True) and (tanyafucked == False) and (seentanyaday05 == False) and (hour <=23):
        jump TanyaHouseDay05
    "Go to Anna's house" if (seenannaevening05 == False) and (hour<=23):
        jump AnnaRoomDay05


label SleepDay05:
scene ryansleeping with dissolve
play music "Sounds/ryansnoring.mp3"
$ renpy.pause(1.0, hard=True)
"You fall asleep and dream of your adventures to come..."
$ renpy.pause(2.0, hard=True)

"Your current score (not that it matters) is: {b}[score]{/b}"
if (score <=110):
    "Your ranking: {b}Douchebag{/b}"
elif (score <=130):
    "Your ranking: {b}Noob{/b}"
elif (score <=150):
    "Your ranking: {b}Average Joe{/b}"
elif (score <=170):
    "Your ranking: {b}Hunk{/b}"
else:
    "Your ranking: {b}Babe Magnet{/b}"
stop music
window hide

jump Day06

    
    

    