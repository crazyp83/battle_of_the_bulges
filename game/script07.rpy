label Day07:
# reboot variables
$ day = 7
$ hour = 8
$ stamina = 5
$ wentforjog = False
$ evictedfromstore = False
$ locswimmingpool = False
$ audacioustried = False
$ evictedfromshop = False
$ shoppingseen = False
$ downtowntipgiven = False
$ workout = False
$ pretendshop = False
$ challengercalls = 0

# new variables

$ saunaoral = False
$ saunaplay = False
$ saunadoris = False
$ saunadanialla = False
$ saunaup = False
$ dorisfirst = False
$ busbeach = False
$ bustown = False
$ bushome = False
$ debbytitfuck = False
$ debbyback = False
$ debbyfrontfuck = False
$ debbydoggy01 = False
$ daysgymseen = 0

stop music
play sound "Sounds/yawning.mp3"
scene ryanyawning with dissolve
$ renpy.pause(1.0, hard=True)
p "Yet another beautiful day... Filled with hot steamy sex hopefully! And I got an extra hour sleep too because it's the weekend!"
if (nursefucked06 == True):
    scene ryanache with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Shit, my dick hurts this morning! I must have caught an STD from that filthy bimbo nurse..."
    window hide
    $ stamina -=1
    show staminaminus01:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.6
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
        
scene ryanbedroomday with dissolve
$ lustaddedB = 2
call Challenger from _call_Challenger_98
$ lustaddedB = 1
call Challenger from _call_Challenger_99
$ challengercalls += 2

label MorningDay07b:
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "What should I do?"
menu:
    "Take a shower":
        jump ShowerMorningDay07
    "Go for a jog":
        jump JogMorningDay07
    "Check the computer":
        jump ComputerMorningDay07
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump MorningDay07b
        
label JogMorningDay07:
scene ryanjog01 with dissolve
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
"You enjoy the fresh sea breeze as you jog along the beach..."
window hide
$ stamina += 1
show stamina01:
    xalign 0.4 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide stamina01
"After running ten miles, you head back home in time for breakfast."
jump BreakfastDay07

label ComputerMorningDay07:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label ComputerMorningDay07b:
scene ryancomputerday
menu:
    "Check the map":
        jump MapMorningDay07
    "Check the stats":
        jump StatsMorningDay07
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump ComputerMorningDay07b
    "Turn the computer off":
        jump MorningDay07b

label MapMorningDay07:
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
if (discoveranna == True):
    show annamap
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
jump ComputerMorningDay07b

label StatsMorningDay07:
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
jump ComputerMorningDay07b

label ShowerMorningDay07:
scene bothshowermorning01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oooh... Both Nikki AND Nancy are in the shower, with the door wide open and their fine arses in lingerie staring at me..."
menu:
    "Having said that... I might need to save some stamina for later today... I'd better leave quietly.":
        jump MorningDay07b
    "To hell with the game's objectives, I want some poontang NOW!" if (nikkifucked == True) and (nancyfucked == True):
        jump ShowerMorningDay07b
    "This is going to be tough. I've fucked Nancy, but not Nikki yet..." if (nikkifucked == False) and (nancyfucked == True):
        jump ShowerMorningDay07b
    "This is going to be tough. I've fucked Nikki, but not Nancy yet..." if (nikkifucked == True) and (nancyfucked == False):
        jump ShowerMorningDay07b
    "This is going to be tough. I didn't fuck either of them yet..." if (nikkifucked == False) and (nancyfucked == False):
        jump ShowerMorningDay07b

label ShowerMorningDay07b:
if (nikkifucked == True) and (nancyfucked == True):
    p "Hi Nancy, hi Nikki! Can I come in?"
    scene bothshowermorning02 with dissolve
    $ renpy.pause(1.0, hard=True)
    s "Sure, we were about to leave, I just finished my shower and mom just came to pick up some hand cream."
    p "Oh yeah? Well, I've got some cream for both of you if you like."
    scene bothshowermorning03 with dissolve
    m "Oh... Honey, you really shouldn't talk like that..."
    p "Why not? I already nailed both of you, and as the saying goes: \"Housematecest is best!\". And housematecest threesome is ...err... awesome!"
    m "Well... This is just so wrong!"
    show bothshowernikki with dissolve
    s "MOM! You let [name] fuck you???"
    show bothshowernancy with dissolve
    m "I was... so lonely... And he was so..."
    p "Hung and muscular? I think that's what you said... Well, I'm still hung and muscular... Look at how hard I am right now..."
    scene bothshowermorning05 with dissolve
    m "Oh my God, it looks even bigger than I remember..."
    s "It sure is... I think it's time to let him do us both at once, then he'll stop being obsessed about it and we can finally have some peace!"
    p "I like your way of thinking Nikki..."
    window hide
    show doubledelight:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/delight.mp3"
    $ renpy.pause(4.0, hard=True)
    hide doubledelight
    jump MorningThreesomeDay07
if (nancyfucked == False) and (nikkifucked == True):
    p "Hi Nancy, hi Nikki! Can I come in?"
    scene bothshowermorning02 with dissolve
    $ renpy.pause(1.0, hard=True)
    s "Sure, we were about to leave, I just finished my shower and mom just came to pick up some hand cream."
    p "Oh yeah? Well, I've got some cream for both of you if you like."
    scene bothshowermorning03 with dissolve
    m "Oh... Honey, you really shouldn't talk like that. It's... disgusting."
    p "Come on Nancy. I already nailed Nikki, and as the saying goes: \"Housematecest is best!\". And housematecest threesome is ...err... awesome!"
    show bothshowernancy with dissolve
    m "What? You had sex with my own DAUGHTER??? This is just so wrong!"
    show bothshowernikki with dissolve
    s "It's him,  he took advantage of me in a time of weakness mom!"
    hide bothshowernancy with dissolve    
    m "I can imagine. Sex is all he thinks about. Now I do NOT approve of such behavior young man!"    
    window hide
    $ lust_points[16] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.6 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01    
    m "Now off you go, we have to finish cleaning ourselves. We'll see you for breakfast."
    jump BreakfastDay07            
if (nancyfucked == True) and (nikkifucked == False):
    p "Hi Nancy, hi Nikki! Can I come in?"
    scene bothshowermorning02 with dissolve
    $ renpy.pause(1.0, hard=True)
    s "Sure, we were about to leave, I just finished my shower and mom just came to pick up some hand cream."
    p "Oh yeah? Well, I've got some cream for both of you if you like."
    scene bothshowermorning03 with dissolve
    m "Oh... Honey, you really shouldn't talk like that..."
    p "Why not? I already nailed you, and as the saying goes: \"Housematecest is best!\". And housematecest threesome is ...err... awesome!"
    show bothshowernancy
    m "What? How dare you reveal... I mean, LIE and say such a vile thing in front of Nikki!"
    s "José is a much better gentleman than you, that's for sure. He is so... romantic."
    window hide
    $ lust_points[17] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01    
    p "I can be romantic! Just show me and I'll be romantic!"
    scene bothshowermorning04 with dissolve
    $ renpy.pause(1.0, hard=True)
    m "Now off you go, we have to finish cleaning ourselves. We'll see you for breakfast."    
    jump BreakfastDay07       
if (nancyfucked == False) and (nikkifucked == False):
    p "Hi Nancy, hi Nikki! Can I come in?"
    scene bothshowermorning02 with dissolve
    $ renpy.pause(1.0, hard=True)
    s "Sure, we were about to leave, I just finished my shower and mom just came to pick up some hand cream."
    p "Oh yeah? Well, I've got some cream for both of you if you like."
    show bothshowernancy with dissolve
    m "Oh... Honey, you really shouldn't talk like that. It's disgusting."
    window hide
    $ lust_points[16] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.6 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01        
    s "More than disgusting. PERVY!"
    window hide
    $ lust_points[17] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01    
    m "Now off you go, we have to finish cleaning ourselves. We'll see you for breakfast."
    jump BreakfastDay07            

label MorningThreesomeDay07:
scene morningfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
m "Since we all agree, what would you like to do for morning fun [name]?" 
label MorningChoiceDay07:
menu:
    "My cock is rock-hard and ready to burst, cool it down please!" if (morningfeet == False):
        s "My feet are exactly what you need..."
        m "And my tits will help too..."
        jump MorningFeetDay07
    "How about some lesbian fun... I'll watch." if (morningplay == False):
        s "Great idea... I've always wanted to play with your fat funbags mom!"
        jump MorningPlayDay07
    "A household that sucks together is a household that sticks together!" if (morningblow == False):
        s "I volunteer to blow you first!"
        m "But don't make him pop too soon Nikki, I want him to fuck my mouth next..."
        jump MorningBlowDay07
    "I can't decide which pussy to fuck!" if (morningdp == False):
        s "Then we should let you test-drive both."
        jump MorningDoubleDay07
    "I'm about to burst a nut!" if (morningplay == True) and (morningblow == True) and (morningdp == True) and (morningfeet == True):
        jump MorningCumDay07

label MorningFeetDay07:
$ morningfeet = True
scene morningfeet01 with dissolve
$ renpy.pause(1.0, hard=True)
m "That's it, lick my feet...."
s "... while I rub this great big hard dong of yours!"
scene morningfeet02 with dissolve
play sound "Sounds/morningsisbig.mp3"
$ renpy.pause(2.0, hard=True)
s "Are you ready to get teased [name]?"
p "Y... yeah..."
label MorningFeetDay07b:
play music "Sounds/wanking.mp3"
scene morningfeet03 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet03 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet03 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet03 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet03 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet03 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet03 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet03 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet03 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet03 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet03 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningfeet02 with dissolve
$ renpy.pause(0.1, hard=True)
stop music
menu:
    "Repeat":
        p "Yeah, keep going Nikki, I'm close..."
        s "Oooh, you're gonna give us a great big load of pearly white cum [name]?"
        m "I can't wait to get my tits covered in your spunk [name]!"
        jump MorningFeetDay07b
    "Cum (no stamina penalty)":
        stop music
        scene morningfeet04 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "FUCK, I'm bursting! AAAH!"
        m "Wow, that was a HUGE shot of cum [name]..."
        scene morningfeet05 with dissolve
        $ renpy.pause(1.0, hard=True)
        m "Damn, you've covered my breasts with a TON of cum! I'm so proud of my tenant!"
        s "But you're still ROCK-HARD and ready for more, aren't you [name]?"
        scene morningfuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        m "Indeed, so what would you like to do next [name]?"
        jump MorningChoiceDay07

label MorningPlayDay07:
$ morningplay = True
scene morningbothplay01 with dissolve
$ renpy.pause(1.0, hard=True)
s "Mom... Your tits are so big and soft...."
m "You were always tugging at them when you were a suckling baby. Do it again... I have some milk for you my sweet child."
p "Fuck yeah!"
label MorningPlayDay07b:
scene morningbothplay02 with dissolve
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
p "Yeah, Nikki, twist those nipples and get some milk out!"
scene morningbothplay03 with dissolve
$ renpy.pause(1.0, hard=True)
s "Mmmh, it tastes delicious mom!"
p "Do it again Nikki!"
scene morningbothplay02 with dissolve
$ renpy.pause(1.0, hard=True)
scene morningbothplay03 with dissolve
play sound "Sounds/sucking02.mp3"
$ renpy.pause(1.0, hard=True)
stop sound
menu:
    "Repeat":
        p "I wanna see more of that..."
        m "Good thing I still have some milk..."
        jump MorningPlayDay07b
    "Move on":
        s "I'm not sure I'll need breakfast anymore today...(giggles)"
        scene morningfuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        m "What would you like to do next [name]?"
        jump MorningChoiceDay07

label MorningBlowDay07:
$ morningblow = True
scene morningsisblow03 with dissolve
play sound "Sounds/morningsisperfect.mp3"
$ renpy.pause(1.0, hard=True)
s "Mmh, your cock is so perfect..."
p "There you go Nikki, rockhard for you..."
s "MMMh, it's so tasty, I can't ever get enough of your cock [name]."
scene morningsisblow01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Then prepare to take it down your throat. DEEP!"
label MorningBlowDay07b:
scene morningsisblow02 with dissolve
play music "Sounds/morningsisblow.mp3"
$ renpy.pause(0.3, hard=True)
scene morningsisblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningsisblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        jump MorningBlowDay07b
    "Move on":
        scene morningsisblow03 with fastdissolve
        play sound "Sounds/morningsisperfect.mp3"
        $ renpy.pause(1.0, hard=True)
        s "I think I've sucked about a pint of precum from that monstrous rod..."
        p "I'm always VERY bloated in the morning..."
        m "My turn! Please fuck my mouth my sweet little pumpkin!"
        jump BothMomMorningSuckDay07
                
label BothMomMorningSuckDay07:
scene morningmomblow01
$ renpy.pause(1.0, hard=True)
p "Open wide Nancy. I'll pile-drive my shaft down your throat..."
m "MMM, gggllr..."
scene morningmomblow02
$ renpy.pause(1.0, hard=True)
p "There. Hold it..."
s "This is so hot, you're really fucking her mouth without mercy [name]."
p "She asked for it, didn't she?"
label BothMomMorningSuckDay07b:
play music "Sounds/hardsucking.mp3"
scene morningmomblow01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningmomblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningmomblow01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningmomblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningmomblow01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningmomblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningmomblow01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningmomblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningmomblow01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningmomblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningmomblow01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene morningmomblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        jump BothMomMorningSuckDay07b
    "Move on":
        scene morningmomblow03 with fastdissolve
        $ renpy.pause(1.0, hard=True)
        m "*cough* Thank you [name], that was so kind of you."
        p "Get up Nancy, and let's move on to something else, I'm still horny."
        m "Of course my sweet little pumpkin!"
        jump MorningChoiceDay07

label MorningDoubleDay07:
$ morningdp = True
scene morningdp01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Mmh, which pussy to choose... Tough decision..."
m "I'm your landlady and I ORDER you to fuck me first!"
s "Hey! I'm your landlady's daughter and I REQUIRE some tenant love right now!"
menu:
    "Fuck Nancy first":
        p "Nancy's pussy is so warm and inviting, I'll do her first!"
        m "That's a good boy! Now come and give me the fuck of my lifetime. AGAIN!"
        s "Be quick, my pussy is DRIPPING WET!"
        $ momfirst = True
        jump MorningMomFirstDay07
    "Fuck Nikki first":
        p "Nikki's pussy is so tight and tempting, I'll do her first!"
        s "Yeah! I'm ready, pound it hard [name]! I'll stand against the wall for you."
        m "Be quick, I NEED that cock!"
        $ sisfirst = True
        jump MorningSisFirstDay07
    
label MorningMomFirstDay07:
scene morningdpmom01 with dissolve
play sound "Sounds/generic.mp3"
$ renpy.pause(0.1, hard=True)
scene morningdpmom02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom01 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom01 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom01 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom01 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom02 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom01 with dissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom02 with fastdissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom01 with fastdissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom02 with fastdissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom01 with fastdissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom02 with fastdissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom01 with fastdissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom02 with fastdissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom01 with fastdissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom02 with fastdissolve
$ renpy.pause(0.1, hard=True)
scene morningdpmom01 with fastdissolve
$ renpy.pause(0.1, hard=True)
stop sound
if (sisfirst == True):
    jump MorningDoubleEndDay07
s "Let's switch now, my turn!"
jump MorningSisFirstDay07

label MorningSisFirstDay07:
scene morningdppresis with dissolve
$ renpy.pause(1.0, hard=True)
s "Just shove your meatpole in [name], I can't wait any longer! I WANT IT!"
p "I like your enthusiasm Nikki."
play music "Sounds/morningsisslow.mp3"
show morningsisslow
show faster
call screen morningsisslowday07
screen morningsisslowday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MorningSisFastDay07")
label MorningSisFastDay07:
hide faster
stop music
play music "Sounds/morningsisfast.mp3"
show morningsisfast
show next
call screen morningsisfastday07
screen morningsisfastday07:
    modal True
    button:
        xpos .82
        ypos .9
        xysize(100, 50)        
        action Jump ("MorningSisEndDay07")

label MorningSisEndDay07:
hide morningsisslow
hide morningsisfast
stop music
scene morningdppresis
$ renpy.pause(1.0, hard=True)
p "Phew, I pulled out just in time. I was about to burst a nut there, your pussy is so TIGHT Nikki!"
if (momfirst == True):
    s "That's cos your dong is so fucking HUGE [name]! *giggles*"
    m "Now, since your cock is still hard and ready, what should we do next my stud tenant?"
    jump MorningDoubleEndDay07
m "I can't wait any longer either, my turn!"
jump MorningMomFirstDay07

label MorningDoubleEndDay07:
scene morningfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
m "What would you like to do next [name]?"
jump MorningChoiceDay07

label MorningCumDay07:
scene morningbothcum01 with dissolve
$ renpy.pause(1.0, hard=True)
p "There it goes, get ready for some cum flying your way! AAAH!"
window hide
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(3.0, hard=True)
m "Let it all out sweetie, I don't want you to have blueballs today."
scene morningbothcum02 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(2.0, hard=True)
s "[name]! You're blowing your load all over ME! Yummy!"
p "There's more Nikki, wait for it, RHAAA!"
m "What about me? I hope you kept some for me..."
scene morningbothcum03 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(3.0, hard=True)
p "Of course mom, here you go, half a pint to cover your sumptuous tits! FUCK YEAH, I'm DA MAN!"
m "Ooooh, I'm ssoo proud of you [name], you really had a HUGE supply of warm cum for me didn't you?"
s "And after he TOTALLY covered me from head to toe in spunk too..."
scene morningbothcumend with dissolve
$ renpy.pause(3.0, hard=True)
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.4
    linear 1.0 yalign 0.6
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
s "Now I'm going to have to take ANOTHER shower."
m "So do I. Mind if I join you Nikki?"
s "Of course not mom!"
p "What about me, mind if I join you?"
m "There's not enough space in the shower cubicle for THREE people, sweetie."
p "Oh, that's just great. I give you my most prized and sacred reproductive fluids, and this is all the gratitude I get in return."
s "Your reproductive fluids are soon to become sewer filth... See you at breakfast [name]!"
$ hour += 1
$ threesome += 1
$ familythreesome = True
scene ryanbedroomday with fade
p "I might as well get dressed and head down for breakfast then."
jump BreakfastDay07

label BreakfastDay07:
stop music
scene breakfastday03a
$ renpy.pause(1.0, hard=True)
if familythreesome:
    m "Okay, eat up both of you, especially you pumpkin, after the exercise you had this morning... *wink*"
    show breakfastday03c with dissolve
    s "I think this really brought us closer... In a deep and meaningful way."
    p "Yep, in a very DEEP way, I agree."
    hide breakfastday03c
    show breakfastday03d with dissolve
    s "I knew you would have to turn what I said into some filthy sexual innuendo... I see SOME things never change..."
    show breakfastday03b with dissolve
    m "Don't start arguing or breakfast will get cold..."
    hide breakfastday03b
    show breakfastday03c with dissolve
    s "Chantelle is coming for a sleepover tonight. I trust no one will mention what happened this morning."
    show breakfastday03f with dissolve
    m "Of course not Nikki, that would be... awkward."
    p "I'll stay mum, I promise."
    hide breakfastday03f
    scene breakfastday03a with fastdissolve
    m "So what are you going to do today on this beautful Saturday since you don't have school [name]?"
    p "I have a super-important competition at the gym downtown this afternoon."
    show breakfastday03d with dissolve
    s "Yeah, I heard about it. José is also competing."
    m "And I bet you really want to WIN don't you my little muscle tenant?"
    hide breakfastday03d
    p "Sure Nancy, I want to become the island's Muscle Stud!"
    show breakfastday03b with dissolve
    m "Ooh, I'm sure you'll win [name]! After all, we just saw what you are capable of this morning, didn't we Nikki?"
    show breakfastday03d with dissolve
    s "I hope [name] wins too. And even that he beats José. There, I said it!"
    p "Glad to hear Nikki, your encouragement are really what I needed to boost my self-esteem, because the competition is really going to be tough form what I gather..."
    jump BreakfastDay07b

if familythreesome == False:
    show breakfastday03b with dissolve
    m "So what are you going to do today on this beautfiul Saturday since you don't have school?"
    show breakfastday03c with dissolve
    s "I'm hanging out with Chantelle at the beach. And then I invited her over for a sleepover tonight."
    scene breakfastday03a with fastdissolve
    m "And you [name]?"
    p "I have a super-important competition at the gym downtown this afternoon."
    show breakfastday03d with dissolve
    s "Yeah, I heard about it. José is also competing."
    m "And I bet you really want to WIN don't you my little muscle tenant?"
    hide breakfastday03d
    p "Sure Nancy, I want to become the island's Muscle Stud!"
    m "Ooh, is that what the competition is about? I can help you focus with some yoga training this morning. I think it will help you a lot."    
    p "Sure, but I also need to train my muscles."
    m "If it's this afternoon, I'm sure you have some quality time to spend with me so I can help you. I'll set up the mat so we can start straight after breakfast..."
    p "Sure, why not..."
    $ momyogatrainingday07 = True
    jump BreakfastDay07b

label BreakfastDay07b:
scene breakfastday03a with fade
$ renpy.pause(1.0, hard=True)
$ hour+=1
m "Well, see you tonight for dinner then. I made both of you a sandwich so you can eat it for lunch wherever you end up being..."
show breakfastday03c with dissolve
s "Wow, thanks mom, you're the best mom ever!"
p "Yes, this will come in very handy, since I'm forced to eat lunch every day even when I don't want to."

if momyogatrainingday07:
    m "And go and get dressed for our yoga session pumpkin!"
    p "Ah yeah, I almost forgot about that..."
    jump MomYogaTrainingDay07

jump BurbsChoiceDay07

label MomYogaTrainingDay07:
scene saturdayyoga01 with dissolve
$ renpy.pause(1.0, hard=True)
m "Ah there you are my sweet little tenant. Just watch me and try and do exactly as I do, alright?"
p "Sure Nancy, I'll try."
scene saturdayyoga02 with dissolve
$ renpy.pause(1.0, hard=True)
m "First, we'll start by stretching our arms, like so..."
p "(Damn, she's weary a see-through body.... What a tease my landlady is, don't you guys agree?)"
scene saturdayyoga03 with dissolve
$ renpy.pause(1.0, hard=True)
m "Next, stretch our legs a bit to let the tension out of our bodies."
p "I'm not sure this is getting ALL the tension out of my body..."
scene saturdayyoga04 with dissolve
$ renpy.pause(1.0, hard=True)
m "Move your legs up and down. Up and down."
scene saturdayyoga05 with dissolve
$ renpy.pause(1.0, hard=True)
m "And now, legs stretched out and hands joined..."
p "(I've got something else that's stretching out...)"   
scene saturdayyoga06 with dissolve
$ renpy.pause(1.0, hard=True)
m "Are you getting a hardon? You need to CONCENTRATE young man!"
p "I am, I am. I'm concentrating on trying not to get a hardon, but it's tough with you around."
m "Well, stop looking at my big tits for starters. What if you pop a boner during the competition? That would be most embarrassing."
p "Sure, it would..."
scene saturdayyoga07 with dissolve
$ renpy.pause(1.0, hard=True)
m "So let's finish off with the lotus position, which is great to help you in your concentration and brings positive energy into your body. Just breath in..."
m "And breath out."
m "And breath in...."
m "And breathe out."
p "This is working Nancy, I can feel... More focused and full of energy."
if (stamina <= 4):
    window hide
    $ stamina += 1
    show stamina01:
        xalign 0.1 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide stamina01
scene saturdayyoga08 with dissolve
$ renpy.pause(1.0, hard=True)
m "Well, that's great honey pot! You can thank me later tonight when you bring back home the trophy and make me proud... *wink*"
p "Sure Nancy, thanks a lot for your help, now I'm gonna win FOR SURE!"
p "I'd better get going, see you tonight."
m "Have a great day my sweet little tenant!"
$ hour += 1
jump BurbsChoiceDay07

label BurbsDay07:
stop music
scene burbsday with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_100
    $ lustaddedB = 1
    call Challenger from _call_Challenger_101
    $ challengercalls += 2

if (hour == 20):
    p "Just in time for dinner"
    jump DinnerDay07
if (hour == 18 or hour == 19):
    p "I don't have time for much at this time of the day..."
    jump BurbsChoiceDay07

p "The burbs are so quiet during the day. And the weekend apparently."

label BurbsChoiceDay07:
scene burbsday
if hour == 12 or hour == 13 and atelunchday07 == False:
    p "I'd better take a break and eat that sandwich Nancy prepared for me, I'm hungry... Let's sit on a bench by the sidewalk since I'm in the burbs."
    scene burbsday
    show mceating
    with dissolve
    $ renpy.pause(1.0, hard=True)
    p "What are you looking at? You never saw a guy eat a sandwich?"
    $ hour += 1
    $ atelunchday07 = True
    hide mceating
    show mcate
    with dissolve
    p "Ah, now I'm not hungry anymore. Amazing what eating does to your body. Let's move on then..."

if (hour == 20):
    p "Damn, it's 8pm already, I should really head back home for dinner..."
    jump DinnerDay07
p "What should I do?"
menu:
    "Explore the Burbs" if (discoverstore == False):
        jump BurbsExploreDay07
    "Go to the convenience store" if (discoverstore == True) and (evictedfromstore == False):
        jump StoreDay07
    "Go back home" if hour >= 12:
        jump HomeDay07
    "Go to Debby's house" if (auntdebbyseen07 == False):
        jump AuntDebbyHouseDay07
    "Take the bus to the beach" if (hour <= 17):
        $ busbeach = True
        jump BusDriveDay07
    "Take the bus heading downtown" if (hour <= 17):
        $ bustown = True
        jump BusDriveDay07
    "Take the shortcut to the Beach" if (hour <= 19) and (discoverclinic == True):
        stop music
        scene clinicentrance with dissolve
        play music "Sounds/gardensound.mp3"
        $ renpy.pause(1.0, hard=True)
        p "I wish I had discovered this shortcut earlier, it is really helpful in cutting my travel time between the burbs and the beach..."
        jump Beach01Day07
    "Go to the clinic" if (hour <= 18) and (discoverclinic == True) and (seenclinic05 == False) and (seenclinic06 == False) and (seenclinic07 == False):
        jump Insemination01Day07

label BurbsExploreDay07:
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
jump BurbsChoiceDay07

label BusDriveDay07:
stop music
scene busdrive with dissolve
play music "Sounds/busidle.mp3"
$ renpy.pause(1.0, hard=True)
p "Here's the bus. Let's get on."

label BusEndDay07:
if (busbeach == True):
    $ hour += 1
    $ busbeach = False
    jump Beach01Day07
elif (bustown == True):
    $ hour += 1
    $ bustown = False
    jump DowntownDay07
elif (bushome == True):
    $ hour += 1
    $ bushome = False
    jump BurbsDay07
    
label HomeDay07:
stop music
scene livingroom01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah, home sweet home..."
    
if (hour == 20):
    p "Just in time for dinner..."
    jump DinnerDay07

p "What should I do?"
menu:
    "Go to my room":
       jump RyanBedroomDay07
    "Go to the bathroom":
        jump BathRoomDay07
    "Go to Nancy's room" if (momroomseen07 == False):
        jump MomRoomDay07
    "Go to the swimming pool" if (locswimmingpool == False):
        jump SwimmingPoolDay07
    "Leave the house":
        jump BurbsDay07

label SwimmingPoolDay07:
$ locswimmingpool = True
if (hour <= 18):
    scene poolempty with dissolve
    play music "Sounds/gardensound.mp3"
    $ renpy.pause(1.0, hard=True)
    p "There's no one around, I can't even, like, perv on Nancy or Nikki in a bikini right now. SAD."
    $ locswimmingpool = False
    jump HomeDay07
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
    jump DinnerDay07

label RyanBedroomDay07:
stop music
$ locroom = True
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
if (hour >= 20):
    $ hour = 20
    p "Oh, it's time for dinner. I'd better go downstairs to the kitchen."
    jump DinnerDay07

p "What to do, what to do..."
menu:
    "Turn the computer on":
        jump ComputerDay07
    "Do some heavy bodybuilding (+2hrs)" if (hour <= 18):
        if (workout == True):
            "You already trained today."
            jump RyanBedroomDay07
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
            jump RyanBedroomDay07        
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump RyanBedroomDay07
    "Go the living room":
        jump HomeDay07
    "Go to the bathroom" if (showerseen07 == False):
        jump BathRoomDay07
    "Go to Nancy's room" if (momroomseen07 == False):
        jump MomRoomDay07

label ComputerDay07:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label Computer02Day07:
scene ryancomputerday
menu:
    "Check the map":
        jump MapDay07
    "Check the stats":
        jump StatsDay07
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump Computer02Day07
    "Learn how to use the pendulum" if (pendulum == True) and (pendulumactive ==False):
        jump CompPendulumDay07
    "Play a smutty game (+1hr)":
        jump CompGameDay07
    "Turn the computer off":
        jump RyanBedroomDay07

label CompPendulumDay07:
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump Computer02Day07

label MapDay07:
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
jump Computer02Day07

label StatsDay07:
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
jump Computer02Day07

label CompGameDay07:
scene ryancomputergameday
$ renpy.pause(1.0, hard=True)
p "This game is tough. My fingers hurt like hell from so much clicking..."
$ hour += 1
jump Computer02Day07

label MomRoomDay07:
scene nancybedroomday with dissolve
$ renpy.pause(1.0, hard=True)
$ momroomseen07 = True
p "Nancy's room is so clean and tidy. Not like mine."
menu:
    "Snoop around" if (dildo == False):
        jump MomBedroomSnoopDay07  
    "Go back to my room":
        jump RyanBedroomDay07
    "Put the dildo back in its drawer" if (dildo == True):
        show dildo
        show square
        play sound "Sounds/lost.mp3"
        "You relinquish a giant black dildo. Yes, that's right, \"relinquish\". Look it up in the dictionary."
        hide square
        hide dildo
        $ dildo = False
        jump RyanBedroomDay07

label MomBedroomSnoopDay07:
p "There might be an interesting item hidden somewhere... Time to snoop around..."
p "But I have a limited amount of time to look for it, Nancy might come back from work anytime for all I know."
play music "Sounds/snooping.mp3"
call screen mombedroomsnoopDay07
stop music
"You were too slow and didn't find anything."
jump RyanBedroomDay07

label FoundDildoDay07:
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
jump RyanBedroomDay07

label BathRoomDay07:
stop music
if (hour <= 17):
    jump EmptyBathRoomDay07
if (hour == 18) or (hour == 19):
    jump MomShowerDay07

label EmptyBathRoomDay07:
scene bathroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "No one is around right now, I could take a shower if I wanted to."
menu:
    "Take a shower":
        jump ShowerDay07
    "Leave":
        jump RyanBedroomDay07

label ShowerDay07:
scene shower with dissolve
stop music
play music "Sounds/shower.mp3"
$ renpy.pause(1.0, hard=True)
p "That's nice and relaxing..."
if (stamina <= 4) and (showerseen07 == False):
    window hide
    $ stamina += 1
    show stamina01:
        xalign 0.4 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide stamina01
$ showerseen07 = True
jump RyanBedroomDay07

label MomShowerDay07:
play music "Sounds/shower.mp3"
$ locroom = False
scene bathroomdoorclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "Someone's taking a shower..."
menu:
    "Use lubricant on the door hinges" if (wd69 == True) and (squeakfixed == False):
        "The door should not squeak anymore."
        $ squeakfixed = True
        jump MomShowerDay07        
    "Have a peek":
        jump MomPeekBathroomDay07
    "Leave":
        jump RyanBedroomDay07

label MomPeekBathroomDay07:
if (squeakfixed == False):
    play sound "Sounds/doorsqueak.mp3"
    scene bathroomdooropen with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Shit, the door is squeaking..."
    m "I'm in the shower sweetie, don't get in!"
    p "Ah, sorry Nancy...I'm leaving..."
    p "Damn, I should try and find a way of stopping that door from squeaking if I want to spy on Nancy or Nikki in the shower like every other MC..."
    jump RyanBedroomDay07
if (squeakfixed == True):
    scene nancyshower01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Cool, she didn't hear me come in, I can see her naked in the shower now..."
    p "Fuck yeah, look at those huge titties... How I would love to rub my pud between them..."
menu:
        "Watch a little longer...":
            jump MomShower02Day07
        "Leave before she turns round and catches me":
            jump RyanBedroomDay07
    
label MomShower02Day07:
if (momshowerpeep == False):
    $ peeping += 1
$ momshowerpeep = True
if (peeping >= 8) and (achievement.has("peeper") == False):
    show achievement15:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement15
    $ achievement.grant("peeper")
scene nancyshower02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, her arse was made for fucking a great big cock. MY giant cock!"
menu:
        "Watch a little longer still...":
            jump MomShower03Day07
        "Leave before she turns round and catches me":
            jump RyanBedroomDay07
 
label MomShower03Day07:
scene nancyshower03 with dissolve
$ renpy.pause(1.0, hard=True)
m "OMG, my own tenant is spying on me in the shower! What kind of monster did I let into my house?"
if lust_points[16] <= 9:
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
jump RyanBedroomDay07

label AuntDebbyHouseDay07:
stop music
scene debbyentrance with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/debbydoorbell.mp3"
p "Let's see if Debby is around..."
if (hour <=12):
    p "No one's answering..."
    menu:
        "Sneak round the back" if (debbypeep07 == False and debbypeep06 == False):
            scene debbyhousewall with dissolve
            $ renpy.pause(1.0, hard=True)
            p "It might be worth climbing that wall to see if she's by the pool area..."
            menu:
                "No time for this outrageous peeping behavior!":
                    jump BurbsDay07
                "Yeah, why not.":
                    $ auntdebbyseen07 = True
                    jump DebbyPeep01Day07
        "Leave, so much stuff still to do!":
             jump BurbsDay07

if (hour >=13):
    scene debbyhouse01 with dissolve
    d "Well, look who came to visit me. What brings you here [name]?"
    $ auntdebbyseen07 = True
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
    jump AuntDebbyHouseMenuDay07
        
label DebbyPeep01Day07:
scene debbytopless01 with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
p "OOh, it WAS worth it after all... I can see Debby topless coming out of the pool."
p "But I'm quite far, I should squint my eyes to see better. It always works right?"
scene debbytopless02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Yeah, that's better, I can see in more details the action now..."
scene debbytopless03 with dissolve
$ renpy.pause(1.0, hard=True)
p "She hasn't seen me, I'm too far away..."
menu:
    "Call her from your vantage point":
        scene debbytopless04 with dissolve
        $ renpy.pause(1.0, hard=True)
        d "Who is that? I'm warning you, I'm calling the cops on you you fucking hidden pervert!"
        p "Oh, I'd better skip... I don't want to end up with a truncheon up mny arse for pervert activities..."
        $ hour += 1
        jump BurbsChoiceDay07
    "Continue watching, there's no way she'll find out I'm spying on her":
        jump DebbyPeep02Day07

label DebbyPeep02Day07:
$ debbypeep07 = True
scene debbytopless05 with dissolve
$ renpy.pause(1.0, hard=True)
p "She went to fetch something it seems... What could it be I wonder?"
scene debbytopless06 with dissolve
$ renpy.pause(1.0, hard=True)
p "A huge dildo! She's prepping her arse for the incoming anal insertion..."
scene debbytopless07 with dissolve
play sound "Sounds/moaning.mp3"
p "Wow, she's doing it, right there in her private garden..."
scene debbytopless08 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless07 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless08 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless07 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless08 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless07 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless08 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless07 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless08 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless07 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless08 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless07 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless08 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless07 with dissolve
$ renpy.pause(0.3, hard=True)
scene debbytopless08 with dissolve
$ renpy.pause(0.3, hard=True)
p "She's really going for it... I wish it was my cock..."
scene debbytopless09 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, she's got it stuck all the way up her backdoor..."
$ hour += 1
p "Well, that was something everyone should see at least once in their lives... But it's getting late, I should move on."
$ peeping += 1
if (peeping >= 8) and (achievement.has("peeper") == False):
    show achievement15:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement15
    $ achievement.grant("peeper")
jump BurbsChoiceDay07
        
label AuntDebbyHouseMenuDay07:
menu:
    "I wanted to see you model some more bikinis for me." if (debbybikini04 == False) and (debbybikini == False) and (debbybikini03 == False) and (debbybikini05 == False) and (debbybikini06 == False) and (debbybikini07 == False):
        d "Well, that's bold of you young man!"
        d "But you're in luck, I just received a new swimsuit which I haven't tested yet... Come on in..."
        $ debbybikini07 = True
        jump AuntDebbyInsideDay07
    "I was wondering if your car needed washing?" if (debbycarwashed == False):
        d "Oh, I see, you want to make a bit of money do ya? Fair enough."
        d "I'll give you five dollars... But I want to be able to watch and you have to be bare-chested...(wink)"
        menu:
            "It's a deal!":
                jump AuntCarWashDay07
            "Five dollars? It will take me at least one hour to wash it... Not interested.":
                d "Your choice mr I'm-too-important-to-wash-a-car-for-five-dollars!..."
                d "Anything else?"
                jump AuntDebbyHouseMenuDay07
    "How about you get down on your knees and worship your Master's cock again?" if (debbyfuckedoffice == True) or (debbyfuckedhome == True)):
        d "Well... I don't know [name], I..."
        p "Your Master ir ORDERING YOU bitch!"
        d "Of course Master, come in and your slave will get ready for you."
        jump DebbyCockSlapDay07
    "Just coming by to say hi Debby.":
        d "Well, it's much appreciated... Maybe I could entice you with a bikini session I'm having with my secretary [name]? You could give us your valuable opinion."
        p "Oh really? Cool, That's a NEW thing to do at your house, I can't miss it."
        d "Let's move to the swimming pool area then... Where the high-tech camera can record everything."
        jump DebbyNewBikiniDay07
    
label DebbyNewBikiniDay07:
scene debbynewbikinipool with dissolve
show secretarybikini01 at left
show debbynewbikini01 at right
$ renpy.pause(1.0, hard=True)
d "This is Gwendoline. Maybe you've met her?"
if stolecamera:
    p "Err... Yeah, maybe I did. I don't recall. Err... I plead the fifth."
    st "I think I DO remember you. You STOLE a camera from Audacious HQ!"
    d "All is forgiven Gwendoline. He is my guest today..."
    st "Sure boss..."
if stolecamera == False:
    p "Nope, but I'm looking forward to meeting her NOW."
    st "What a charmer!"
d "Gwendoline is wearing one of our futurewear line. What do you think?"
window hide
hide secretarybikini01
show secretarybikini02 at left with dissolve
$ renpy.pause(1.0, hard=True)
p "I feel like I'm already in 2021!"
d "And what about mine? It's also from the futurewear line.."
window hide
hide debbynewbikini01
show debbynewbikini02 at right with dissolve
$ renpy.pause(1.0, hard=True)
p "Very nice Debby. I feel like I'm in 2022 now."
d "Then let's get moving FORWARD into the future then... First, with Gwendoline."
window hide
hide secretarybikini02
hide debbynewbikini02
show secretarybikini03
with dissolve
$ renpy.pause(1.0, hard=True)
p "Nice arse. I mean back. Of the bikini that is."
window hide
hide secretarybikini03
show secretarybikini04
with dissolve
$ renpy.pause(1.0, hard=True)
p "Nice..."
play sound "Sounds/phonering.mp3"
$ renpy.pause(1.0, hard=True)
window hide
hide secretarybikini04
show debbynewbikini03
with dissolve
play sound "Sounds/auntphone.mp3"
$ renpy.pause(1.0, hard=True)
d "Sorry, I need to go and answer my phone in private. It's probably an important business call."
d "You two can continue posing. Maybe [name] can join you Gwendoline. I'll be back in a short while."
st "Okay boss, I'll take care of him!"
scene debbypoolsec01 with dissolve
$ renpy.pause(1.0, hard=True)
st "Oh, damn... I didn't realize... You were so BIG down there!"
p "Most girls can't believe their eyes. But it ain't fake news, it's the Real McCoy lady!"
st "Prove it. I don't believe you."
scene debbypoolsec02 with dissolve
$ renpy.pause(1.0, hard=True)
p "See, no conspiracy there..."
st "*gulp* Can I touch it to check that it's REAL?"
p "Be my guest."
scene debbypoolsec03 with dissolve
$ renpy.pause(1.0, hard=True)
st "Damn boy, that is one MASSIVE fuckpole. You could be in a pon movie with Angelina Jolly for sure. I heard she only does scene with horse-hung pornstars."
p "Let's see how good YOU would fare in a movie with a cock as big as mine..."
st "I can handle it. Let me prove it to you..."
scene debbynewbikinipool blurred
show debbysec04
with dissolve
$ renpy.pause(1.0, hard=True)
st "Ready for a double-handed tugjob?"
p "I'm ALWAYS ready. Cos I'm Da Man!"
label SecretaryHandjobDay07:
window hide
play music "Sounds/wanksound.mp3"
hide debbysec04
show debbysec05
with dissolve
hide debbysec05
show debbysec06
with dissolve
hide debbysec06
show debbysec05
with dissolve
hide debbysec05
show debbysec04
with dissolve
hide debbysec04
show debbysec05
with dissolve
hide debbysec05
show debbysec06
with dissolve
hide debbysec06
show debbysec05
with dissolve
hide debbysec05
show debbysec04
with dissolve
hide debbysec04
show debbysec05
with dissolve
hide debbysec05
show debbysec06
with dissolve
hide debbysec06
show debbysec05
with dissolve
hide debbysec05
show debbysec04
with dissolve
hide debbysec04
show debbysec05
with fastdissolve
hide debbysec05
show debbysec06
with fastdissolve
hide debbysec06
show debbysec05
with fastdissolve
hide debbysec05
show debbysec04
with fastdissolve
hide debbysec04
show debbysec05
with fastdissolve
hide debbysec05
show debbysec06
with fastdissolve
hide debbysec06
show debbysec05
with fastdissolve
hide debbysec05
show debbysec04
with fastdissolve
hide debbysec04
show debbysec05
with fastdissolve
hide debbysec05
show debbysec06
with fastdissolve
hide debbysec06
show debbysec05
with fastdissolve
hide debbysec05
show debbysec04
with fastdissolve
hide debbysec04
show debbysec05
with fastdissolve
hide debbysec05
show debbysec06
with fastdissolve
stop music
menu:
    "Repeat":
        jump SecretaryHandjobDay07
    "Blast your semen over her":
        jump SecretaryCumDay07

label SecretaryCumDay07:
hide debbysec06
show debbyseccum01
with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "FUCK! Cumming!"
st "Oh my God, your shots are so ENORMOUS!"
hide debbyseccum01
show debbyseccum02
with dissolve
$ renpy.pause(1.0, hard=True)
p "There's more where that came from! RHAAA!"
st "Yes, cover my face in your hot teenage spunk!"
scene debbyseccum03 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
st "Oh, I LOVE IT! Cum RAINING DOWN on me!"
p "Damn, my balls are BURSTING!"
$ gwendolinewank = True
$ extras +=1
if extras >= 5 and (achievement.has("extrasontheside") == False):
    show achievement21:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement21
    $ achievement.grant("extrasontheside")

scene debbyseccum04 with dissolve
$ renpy.pause(1.0, hard=True)
d "What the hell is going on here?"
p "Err. We got carried away."
d "Gwendoline! I told you to take care of [name], not to make him blast his cum all over my patio floor!"
st "I'm so sorry boss, but his cock... Did you see how HUGE it is?"
d "Yeah, well... It's still no excuse. Now go and clean yourself so we can continue this modelling session without CUM ALL OVER YOU."
d "And you, [name]. Get out of my house, you are nothing but a disturbance everywhere you carry that massive fuckstick of yours!"
if debbyfucked:
    p "You weren't saying that the other day..."
    d "Shut up and leave!"
    jump BurbsChoiceDay07
window hide
if lust_points[5] <=9:
    $ lust_points[5] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.3 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
jump BurbsChoiceDay07

label AuntDebbyInsideDay07:
scene debbyhouse02 with dissolve    
$ renpy.pause(1.0, hard=True)
play sound "Sounds/footsteps.mp3"
d "This way to the living room..."
p "Wow, Debby has such a huge house... And such a tight ass..."
scene debbyhouse03 with dissolve    
$ renpy.pause(1.0, hard=True)
d "Where should I model this new bikini for you?"
menu:
    "Why not in your bedroom?":
        d "No, that's my special place. You can't go there ever, you hear me?"
        p "Alright, alright. How about the backyard then?"
        d "Yes, that will do, go and sit outside and wait for me, I'll be back in a minute."
        d "Get down to your underwear, I might need you... to do something for me."
        p "(Well, that's an unusual request... I hope it leads to something...)"
        jump DebbyHouseBikini01Day07
    "The outside light will better reveal every detail of your hot bo...swimsuit.":
        d "Yes, you're right, you are a fine connoisseur. Go and sit outside then, I'll be back in a sec." 
        d "Get down to your underwear, I might need you... to do something for me."
        p "(Well, that's an unusual request... I hope it leads to something...)"
        jump DebbyHouseBikini01Day07

label AuntCarWashDay07:
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
            p "Shit, it's 8pm, I'd better get back home for dinner or I'll be late."
            $ money += 5
            jump DinnerDay07
        jump AuntDebbyMoneyDay07
    "Stop and sneak inside to get the money anyway":
        $ debbycarwashed = True
        $ debbycarunwashed = True
        jump AuntDebbyMoneyDay07
    
label DebbyHouseBikini01Day07:
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
    jump DebbyBikiniPrefuck01Day07
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
jump BurbsDay07

label DebbyBikiniPrefuck01Day07:
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
jump DebbyFuckChoiceDay07

label AuntDebbyMoneyDay07:
stop music
scene debbymoney with dissolve    
$ renpy.pause(1.0, hard=True)
p "Here's the money."
play sound "Sounds/auntviolent.mp3"
p "What's that sound? It seems to be coming from upstairs where Debby's bedroom is..."
menu:
    "Go investigate":
        jump AuntDebbyStairsDay07
    "Take the money and leave":
        $ money += 5
        jump BurbsDay07

label AuntDebbyStairsDay07:
scene debbystairway with dissolve
play sound "Sounds/auntwhip01.mp3"
$ renpy.pause(1.0, hard=True)
p "Jeezus, this sounds violent, I'd better hurry up!"

label AuntDebbyBedroomDay07:
scene debbybedroom01 with dissolve    
play sound "Sounds/auntwhip02.mp3"
$ renpy.pause(1.0, hard=True)
p "WTF? That masked naked guy is brutalizing Debby!"
menu:
    "Leave quietly and take the money on the way out":
        $ money += 5 
        jump BurbsDay07
    "Get involved":
        p "Hey you, stop this immediately or...I swear I'll beat you up!"
        jump AuntDebbyBondage01Day07

label AuntDebbyBondage01Day07:
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
d "Please don't tell your mom or anybody. I'll give you twenty dollars if you promise me to keep quiet."
menu:
    "So you're into bondage then? I like that...I like that a lot....":
        d "What? No, I'm not interested in doing such a vile thing with you and corrupting your fragile young mind...."
        d "You need to leave now...Take your carwash money and go."
        p "Hey! But..."
        d "Just GO!"
        $ money += 5
        jump BurbsDay07
    "You deserve a good cock slapping, get on your knees bitch!":
        d "Wh...what?..But..."
        p "You heard me. Remove your mask and ON YOUR KNEES BITCH!"
        d "Y..yes master..."        
        jump DebbyCockSlapDay07
    "OK, I didn't see a thing. I won't say a word. I'll just erase everything from my memory.":
        d "Oh Thank you [name], I owe you big time. Here's your twenty bucks. Now get out of here and don't say a word to anyone!"
        $ money += 20
        jump BurbsDay07

label DebbyCockSlapDay07:
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
if lust_points[5] <= 9:
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
p "Now I'm gonna cock-slap that tight arse of yours filthy slut!"
d "Oooh, yes master, I deserve it..."
jump ArseCockSlapDay07

label ArseCockSlapDay07:
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
if (lust_points[5] >= 10) and debbyfucked == False:
    show epiclust:
        xalign 0.6 yalign 0.3
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    d "I'm such a dirty whore for your great big cock Master... Please, do whatever you want with my filthy body!"
    jump DebbyFuckChoiceDay07
d "It's enough for now [name], here's 10 dollars, don't say a word to Nancy and we might do something like that again (wink...)."
menu:
    "Sure, nice doing business with you Debby...":
        $ money += 10
        d "I feel so...cheap...so dirty...I love it, thank you [name]...Just go now..."
        p "I feel like...10 dollars worth apparently. See you another time Debby!"
        if (debbycarunwashed == True):
            $ hour +=1
        jump BurbsDay07
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
        jump BurbsDay07

label DebbyFuckChoiceDay07:
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
            jump DebbyFuckChoiceDay07b
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
    jump BurbsDay07        
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
    jump BurbsDay07        

label DebbyFuckChoiceDay07b:
scene debbybed01 with dissolve
menu:
    "Let me titfuck your massive tits filthy slut!" if (debbytitfuck == False):
        jump DebbyTitfuckDay07
    "On the bed on your back slave!" if (debbyback == False):
        jump DebbyBackFuckDay07
    "I want to lick your hard nipples and maul your tits!":
        jump DebbyNippleDay07
    "A cheap whore like you deserves a good pussy-pounding!" if (debbyfrontfuck == False):
        jump DebbyFrontFuckDay07
    "Be a good bitch and get on all fours for this horny dog!" if (debbydoggy01 == False):
        jump DebbyDoggyFuckDay07        
    "Time to finish me off slave!" if (debbydoggy01 == True) and (debbyfrontfuck == True) and (debbyback == True) and (debbytitfuck == True):
        jump DebbyBedMovie07

label DebbyDoggyFuckDay07:
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
label DebbyDoggyFuckDay07b:
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
        jump DebbyDoggyFuckDay07b
    "Move on":
        p "You did good slave, it's now time to move on to something else..."
        jump DebbyFuckChoiceDay07b
        
label DebbyTitfuckDay07:
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
label DebbyTitFuckDay07b:
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
        jump DebbyTitFuckDay07b
    "Move on":
        p "You did good slave, it's now time to move on to something else..."
        jump DebbyFuckChoiceDay07b

label DebbyBackFuckDay07:
$ debbyback = True
scene debbyback01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Offer your gaping slut-hole to my massive teenage cock slave!"
d "My filthy hole belongs to you Master... Do as you please with it!"
label DebbyBackFuckDay07b:
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
        jump DebbyBackFuckDay07b
    "Move on":
        p "I've punished your dirty hole enough for the moment slave... I'm giving you a respite..."
        d "Thank you Master, I am not worthy of such generosity..."
        jump DebbyFuckChoiceDay07b

label DebbyNippleDay07:
scene debbybed02 with dissolve
play sound "Sounds/sucking.mp3"
$ renpy.pause(2.0, hard=True)
d "Ooh, you suck on my nipples ssoo good! Maul my tits Master!"
p "They look red and erect now, it's time for something else slave..."
jump DebbyFuckChoiceDay07b

label DebbyFrontFuckDay07:
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
label DebbyFrontFuckDay07b:
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
        jump DebbyFrontFuckDay07b
    "Move on":
        p "Your dirty hole is creaming all over the place, let's switch position whore!"
        jump DebbyFuckChoiceDay07b

label DebbyBedMovie07:
scene debbyballs with dissolve
$ renpy.pause(1.0, hard=True)
d "I can feel your balls are ready to unleash their massive store of pent-up young and yummy cum Master!"
p "Fuck yeah! I'm close to bursting a nut, finish me off slave!"
play music "Sounds/debbybedslow.mp3"
show debbybedslow
show faster
call screen debbyfuckslowDay07
screen debbyfuckslowDay07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("DebbyFuckFastDay07")
label DebbyFuckFastDay07:
hide faster
stop music
play music "Sounds/debbybedfast.mp3"
show debbybedfast
show cum
call screen debbyfuckfastDay07
screen debbyfuckfastDay07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("DebbyFuckCumDay07")

label DebbyFuckCumDay07:
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
    p "I'd better get going, dinner is about to start and I'll be late."
    d "Don't tell anyone about this, okay?"
    if (debbyjosewin == True):
        p "Umpf, coming from a whore who fucked José, that's grand!"
        scene debbybedcum03b
        d "What? But... How do you know? That little shit!"
        p "That's right, he's a fucking douchebag and you screwed him! That makes YOU a FILTHY WHORE!"
        d "I'm so ashamed of myself... I'm just a dirty slut... You'd better go and leave your whore of a slave alone..."
        jump DinnerDay07
    menu:
        "Fine, but don't you dare get anywhere near that arsehole José, you hear me slave? (Cockblock José)":
            d "Yes, Master."
            $ josedebbycockblocked = True
            jump DinnerDay07
        "Alright, but I want 5 bucks for my silence...SLAVE!":
            d "There you are, you greedy little pig! Now get out of my house!"
            $ money += 5
            jump DinnerDay07

if (hour <= 19):
    p "I'd better get going now Debby.... You drained my nuts..."
    d "Don't tell anyone about this, okay?"
    if (debbyjosewin == True):
        p "Umpf, coming from a whore who fucked José, that's grand!"
        scene debbybedcum02b
        d "What? But... How do you know? That little shit!"
        p "That's right, he's a fucking douchebag and you screwed him! That makes YOU a FILTHY WHORE!"
        d "I'm so ashamed of myself... I'm just a dirty slut... You'd better go home and leave your whore of a slave alone..."
        jump BurbsDay07
    menu:
        "Fine, but don't you dare get anywhere near that arsehole José, you hear me slave? (Cockblock José)":
            d "Yes, Master."
            $ josedebbycockblocked = True
            jump BurbsDay07
        "Alright, but I want 5 bucks for my silence...SLAVE!":
            d "There you are, you greedy little pig! Now get out of my house!"
            $ money += 5
            jump BurbsDay07
            
            
label TeaganHouse02Day07:
$ seenteaganhouseday07 = True
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
        jump TeaganPool01Day07
    "I'm kinda busy right now, I'm already late for...err... some other stuff.":
        t "Here's five bucks for bringing my groceries over."
        $ money += 5
        jump BurbsChoiceDay07

label TeaganPool01Day07:
scene teagan03day05 with dissolve
$ renpy.pause(1.0, hard=True)
p "I can see her ogling my bulge... Good thing I got a semi while admiring her, it must look even bigger than usual..."
window hide
if (teaganfucked == True):
    t "Just as big as I remember it yesterday..."
    p "I'm not even hard yet teach, it will grow even bigger!"
    t "I know... YOu are so MASSIVE when you are rock-hard... Come in the pool with me stud!"
    jump TeaganPool02Day07
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

label TeaganPool02Day07:
scene teagan04day05 with dissolve
$ renpy.pause(1.0, hard=True)
t "You know, it's highly inappropriate for a teacher to be spending time like this with a student..."
t "So let's just pretend you are only my delivery boy today... and not a boy in the class I teach."
p "Sure Ms Cocque, I don't mind role-playing!"
t "So... What do you have for me Mr grocery boy? (wink)"
label TeaganPool02Day07b:
menu:
    "I picked up an extra-large zucchini for you ma'am!":
        if (lust_points[22] == 10):
            t "That is so corny [name]... Try again."
            jump TeaganPool02Day07b
        t "That is so corny [name]... I don't want to play anymore. Please go home. (sigh)"
        p "But... What about my zucchini? Don't you want to see my big zucchini?"
        jump BurbsChoiceDay07
    "I do pick-ups and deliveries. Right now, I'm picking you up...":        
        t "Ooh? And when will the delivery be?"
        scene teagan05day05 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "In a while... I first need to unpack those heavy bags..."
        if (teaganfucked == True):
            t "You like them don't you... And I KNOW you liked fucking them with your huge, young, hard COCK!"
            p "What can I say, I can't resist such lovely MILF knockers..."
            t "Let's move out of the pool, I want to see that monstercock of yours again!"
            jump TeaganFuckChoicePreDay07
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
            jump TeaganFuckChoicePreDay07
        t "Oh... I like it... But I think this is going too far young man..."
        p "What do you mean?"
        t "I'm your teacher... I can't... let a student fondle my big breasts like that. What if a nosy neighbor reported on us?"
        t "It's best that you leave [name]."
        p "But I'm not your student, you said it! I'm just your delivery boy, it's not fair!"
        jump BurbsChoiceDay07

label TeaganFuckChoicePreDay07:
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
            jump TeaganFuckChoiceDay07
        "Don't drink white bull and keep it for another time":
            p "Teagan, I'm having second thoughts. I read so many stories of teachers going to jail because they fucked their student..."
            p "I wouldn't want that to happen to you..."
            t "What? You're fondling my tits and then you don't want to fuck me? Get out of my house at once [name]!"
            jump BurbsChoiceDay07

label TeaganFuckChoiceDay07:
stop music
scene teaganchoiceday05 with dissolve
$ renpy.pause(1.0, hard=True)
t "So, now that you are here, proudly displaying your gigantic erection to your schoolteacher, what would you like us to do [name]?"
menu:
    "I think anal is in order. Yes, anal." if (teagananalday05 == False):
        t "That massive fuckstick up my arse? You can't be serious..."
        p "I am serious and I'll prove it!"        
        jump TeaganAnalDay07
    "My studcock is sore from so much fucking. It needs a nice foot massage." if (teaganfeet == False):
        t "Mmh, you're a footboy are you? Then get ready for the best footjob in town stud!"
        jump TeaganFeetDay07
    "Get in the lounge chair, I'm gonna pound that sweet teacher pussy of yours!" if (teaganpussy == False):
        t "It's ready to receive your massive teenage pussy-pleaser!"
        jump TeaganPussyDay07
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (teaganpussy == True) and (teaganfeet == True) and (teagananalday05 == True):
        t "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump TeaganMovieDay07

label TeaganAnalDay07:
$ teagananalday05 = True
scene teagananal01 with dissolve
$ renpy.pause(1.0, hard=True)
p "How do you like your student's cock up your fuckhole teach?"
t "I'm such a dirty slut... Pound me with your massive fuckstick I beg you!"
scene teagananal02 with dissolve
$ renpy.pause(1.0, hard=True)
t "AAAH, it's so fucking deep!"
label TeaganAnalDay07b:
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
        jump TeaganAnalDay07b
    "Move on":
        t "Have mercy on my poor arse [name]!"
        p "Ok Teagan, I'll give you a respite. FOR NOW."
        jump TeaganFuckChoiceDay07

label TeaganFeetDay07:
$ teaganfeet = True
scene teaganfeet01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Ready? Cos my feet are going to make your dick extra-hard and extra-HUGE, guaranteed!"
p "Let's see if you're better than Sophia then shall we?"
t "Oh? A competition with the principal? I'm in!"
label TeaganFeetDay07b:
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
        jump TeaganFeetDay07b
    "Move on":
        pass    
t "Ooh, look at all that precum flowing from your tip...You're ready to pop aren't you? So, was it better than Sophia's footjobs?"
p "Y...Yes... So it's best if we move on to something else." 
jump TeaganFuckChoiceDay07    

label TeaganPussyDay07:
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
label TeaganPussyDay07b:
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
        jump TeaganPussyDay07b
    "Move on":
        pass    
jump TeaganFuckChoiceDay07    

label TeaganMovieDay07:
scene teaganfuckmovieday05 with dissolve
p "Bounce up and down on my dong teach! I want to be buried balls-deep inside you!"
t "OOOh, I don't know if I can take that much cock [name], but I sure as hell will try!"
play music "Sounds/teaganfuckslow02.mp3"
show teaganfuckslow02
show faster
call screen teaganfuckslowday07
screen teaganfuckslowday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TeaganFuckFastDay07")

label TeaganFuckFastDay07:
stop music
hide faster
play music "Sounds/teaganfuckfast02.mp3"
show teaganfuckfast02
show cum
call screen teaganfuckfastday07
screen teaganfuckfastday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TeaganFuckCumDay07")

label TeaganFuckCumDay07:
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
if (teaganfucked == True):
    $ hour += 1
    jump BurbsChoiceDay07
$ teaganfucked = True
$ hour += 1
$ backdoor += 1
if (backdoor >= 12) and (achievement.has("banger") == False):
    window hide
    show achievement19:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement19
    $ achievement.grant("banger")    
if (teaganjosewin == False):
    p "(She didn't notice I took a picture of her with her tits plastered in my cum... Now I'll send it to José)."
    $ teaganwin = True    
if (vivianefucked == True) and (sophiafucked == True) and (achievement.has("faculty") == False):
    window hide
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
jump BurbsChoiceDay07

label Insemination01Day07:
stop music
scene clinic04 with dissolve
$ renpy.pause(1.0, hard=True)
dr "Ah, welcome back [name], are you ready to use your \"talents\" to help a poor wife whose husband is shooting blanks?"
p "What do you mean exactly?"
dr "Well, while most insemination programs use artificial means, some of our clients prefer the more \"traditional\" method of insemination."
dr "And there's 10 shiny dollars for you if you unleash one of your spectacular loads inside one of our customers who is here and awaiting insemination to get pregnant."
label Insemination01Day07b:
menu:
    "Na, not today doc.":
        dr "What a waste of a stud's life. Don't forget there are ten shiny dollars in it for you if you ever come back!"
        jump ClinicOutDay07
    "Your establishment is nothing but a depraved whorehouse exploiting men!":
        dr "Yes. And the problem is?"
        p "Well, err... Nothing."
        jump Insemination01Day07b
    "Alright, I'm in! Is she hot?":
        dr "She is indeed \"hot\" as you put it. We doctors prefer the legal term \"rapable\"."
        dr "However, I am not at liberty to disclose her identity and the deed shall be done anonymously through a specially-designed aperture in the wall."
        p "You mean a gloryhole."
        dr "While it is my inclination to refrain from using such vulgar terms, yes, it's just a gloryhole."
        dr "Nurse Racque will show you the way to the insemination room and get you prepared. Please follow her."
        jump Insemination02Day07    

label Insemination02Day07:
$ seenclinic07 = True
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
        jump InseminationNOTDay07
    "Don't say a word":
        ra "I'll show you how to get the best out of that huge dick. By having a go on it myself for a while..."
        je "Don't make him cum, his sperm belongs to me!"
        ra "Don't worry Mrs Anonymous. I know how to control my pussy muscles to bring men to the edge and maintain them there..."
        jump Insemination03Day07

label Insemination03Day07:
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
$ nursefucked07 = True
$ extras += 1
if extras >= 5 and (achievement.has("extrasontheside") == False):
    show achievement21:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement21
    $ achievement.grant("extrasontheside")
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
            jump JenniferFuckChoiceDay07
        je "But I just can't... It's so wrong... I want out of this deal!"
        ra "What a disappointment (sigh). But you're the customer..."
        ra "[name], tuck that monstrous rod back in your pants and leave, we'll call you again if we need you..."
        p "WHAT? Like that? Dismissed like a cheap he-whore? Pfff!"
        jump InseminationNOTDay07
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
                jump JenniferFuckChoiceDay07
            je "But I just can't... It's so wrong... I want out of this deal!"
            ra "What a disappointment (sigh). But you're the customer..."
            ra "[name], tuck that monstrous rod back in your pants and leave, we'll call you again if we need you..."
            p "WHAT? Like that? Dismissed like a cheap he-whore? Pfff!"
            jump InseminationNOTDay07            
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
        jump InseminationNOTDay07
        
label JenniferFuckChoiceDay07:
scene insemination13 with dissolve
$ renpy.pause(1.0, hard=True)
je "Get on with it, I need your sweet cum!"
menu:
    "Get on your back, I'll drill you slowly to stretch your fuckhole!" if (jenniferpussy == False):
        je "Yes, I think that's in order. Since you're so big..."
        jump JenniferPussyDay07
    "Spread those legs, I'm gonna pound you from behind!" if (jenniferdoggy == False):
        je  "Of course, pummel me like a ragdoll [name]!"
        jump JenniferDoggyDay07
    "Yeah, OK, but I want your sweet arse!" if (jenniferanal == False):
        je "What? But you can't impregnate me that way!"
        p "It's to get my cock really hard and ready to explode in your other hole. Come on, you know you want it!"
        je "I definitely DON'T want it, but if it's for a good cause..."
        jump JenniferAnalDay07
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (jenniferpussy == True) and (jenniferdoggy == True) and (jenniferanal == True):
        je  "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump JenniferMovieDay07

label JenniferPussyDay07:
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
label JenniferPussyDay07b:
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
        jump JenniferPussyDay07b
    "Move on":
        pass
je "Now I'm totally stretched out!"
ra "I can see that, your hole is gaping wide open Jennifer!"
p "Good, so we can move on to another position then..."
jump JenniferFuckChoiceDay07

label JenniferDoggyDay07:
$ jenniferdoggy = True
scene insemination12 with dissolve
play sound "Sounds/jennifer02.mp3"
$ renpy.pause(12.0, hard=True)
je "Oh God, oh God! I'm gonna take the biggest fattest cock I've ever seen! I'm dripping wet, shove it in [name] I beg you!"
p "Sure, Here I come, ten inches in one swift go!"
scene insemination12b with dissolve
$ renpy.pause(1.0, hard=True)
je "Damn it, you're so fucking deep!"
label JenniferDoggyDay07b:
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
        jump JenniferDoggyDay07b
    "Move on":
        pass    
je "I feel like a hog on a spitfire!"
p "My dick sure took some heat, I'm red-hot and ready for more action!"
jump JenniferFuckChoiceDay07    

label JenniferAnalDay07:
$ jenniferanal = True
scene insemination18 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Show the naysayers that a woman is also perfectly capable of taking well over a foot of fat hosepipe up her backside [name]!"
je "What? No, please, show instead some restraint when you plunge that massive pole int....!"
scene insemination18b with dissolve
play sound "Sounds/jenniferanal01.mp3"
$ renpy.pause(1.0, hard=True)
je "... MEEEE! FUCK! AAAH!"
label JenniferAnalDay07b:
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
        jump JenniferAnalDay07b
    "Move on":
        pass    
je "Thank God you didn't waste your virile spunk in that hole..."
p "I know where to aim... Let me show you." 
jump JenniferFuckChoiceDay07    

label JenniferMovieDay07:
scene insemination14 with dissolve
p "Ok, you want my sperm Jennifer? I want to hear you SAY IT!"
je "YES! Breed me [name], I want to have your baby!"
play music "Sounds/jenniferfuckslow.mp3"
show jenniferslowfuck
show faster
call screen jenniferslowfuckday07
screen jenniferslowfuckday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("JenniferFastFuckDay07")

label JenniferFastFuckDay07:
stop music
hide faster
play music "Sounds/jenniferfuckfast.mp3"
show jenniferfastfuck
show cum
call screen jenniferfastfuckday07
screen jenniferfastfuckday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("JenniferCumDay07")

label JenniferCumDay07:
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
if (backdoor >= 12) and (achievement.has("banger") == False):
    window hide
    show achievement19:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement19
    $ achievement.grant("banger")
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
        jump Beach01Day07
    "Go to the Burbs":
        jump BurbsDay07
    
label InseminationNOTDay07:
$ inseminationfail07 = True
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
        jump Beach01Day07
    "Go to the Burbs":
        jump BurbsDay07    

label ClinicOutDay07:
scene clinicentrance
$ renpy.pause(1.0, hard=True)
p "Where should I go?"
menu:
    "Go to the beach":
        jump Beach01Day07
    "Go to the Burbs":
        jump BurbsDay07    

label StoreDay07:
stop music
scene store01 with dissolve
play music "Sounds/storemusic.mp3"
$ renpy.pause(1.0, hard=True)

label StoreClerkDay07:
scene store01
if (workedseconddaystore == True) and (hour == 17):
    fa "Oh hi [name]. I guess you came to work here again?"
    fa "I'm really sorry but you can't. I took another boy for the work today, since you already worked here twice already."
    fa "He was desperate for money, I couldn't really say no. He's a nice boy called José."
    p "WHAT???? AAARGH! This is not fair!"
    fa "Oh, moan, moan, moan, that's all I ever hear from you..."
    jump ClerkChoiceDay07    
if ((catchfrancine == True) or (catchbeer == True)) and (hour == 17):
    fa "Are you ready to start another shift today?"
    menu:
        "Yes, I'm ready.":
            jump StoreSecondWork01Day07
        "No, I'm too busy right now.":
            fa "Well, that's unfortunate... I could have really used your help again today..."
            jump ClerkChoiceDay07    
if (storework == True) and (hour == 17) and (catchfrancine == False) and (catchbeer == False):
    fa "Are you ready to start your shift today?"
    menu:
        "Yes, I'm ready.":
            jump StoreWork01Day07
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
            jump ClerkChoiceDay07
elif (storework == True) and (hour == 18):
    fa "You're late for your shift! Although you're lucky cos you don't have one today. I gave the job to someone else."
    fa "Come back tomorrow. At 5pm, not 6pm."
    jump ClerkChoiceDay07   
elif (hour == 19) and (teagangrocery07 == True) and (seenteaganhouseday07 == False):
    fa "Oh, you're just in time to pick up Miss Cocque's groceries. I was about to close."
    p "I'll get them to her right away!"
    jump TeaganHouse02Day07
elif (hour == 19):
    fa "Welcome to \"Seven Square\", your local shop that's opened from seven till... seven."
    fa "I'm sorry, but it is seven o'clock. The second seven. So we are closing."
    fa "Please come back tomorrow to your local convenience store \"Seven Square\" between 7am and... 7pm!"
    jump BurbsDay07    
else:
    fa "Welcome to \"Seven Square\", your local shop that's opened from seven till... seven."

label ClerkChoiceDay07:
if (catchfrancine == True) or (catchbeer == True):
    fa "So, how may I help you?"
else:
    fa "My name is Francine, how may I help you?"
menu:
    "Chat with her":
        jump StoreChatDay07 
    "Buy something":
        jump StoreBuyDay07
    "Invite her to the gym" if (gymmember == True):
        p "Hey, would you like to come to the gym with me today?"
        fa "Ooh, yes! Please let me know when you get there, thanks!"
        $ invitedfrancine07 = True
        jump ClerkChoiceDay07
    "Leave":
        jump BurbsDay07

label StoreChatDay07:
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
                        jump StoreNoDealDay07
                    "It's a deal!":
                        $ halfprice = True
                        jump StoreDealDay07
            "It's a deal!":
                jump StoreDealDay07
    "Just thought I’d check a few things out, you being one of them...":
        scene store03
        fa "I can barely contain my laughter."
        jump ClerkChoiceDay07
    
label StoreDealDay07:
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
            jump StoreBuyDay07
        "No thanks.":
            fa "Alright, see you another day then."
            jump BurbsDay07
jump StoreClerkDay07

label StoreWork01Day07:
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
        jump CatchFrancineDay07
    "Catch the beer":
        jump CatchBeerDay07

label CatchFrancineDay07:
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
jump StoreTeagan01Day07

label CatchBeerDay07:
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
jump StoreTeagan01Day07

label StoreTeagan01Day07:
play music "Sounds/storemusic.mp3"
scene storeteagan01 with dissolve
$ renpy.pause(1.0, hard=True)
p "There's Miss Cocque doing her shopping, she hasn't noticed me yet."
menu:
    "Hide and hope she doesn't see you":
        jump StoreHideDay07
    "Greet her and ask her if you can help with anything":
        jump StoreTeagan02Day07

label StoreHideDay07:
scene storeteaganhide with dissolve
$ renpy.pause(1.0, hard=True)
p "Phew, she almost saw me but I'm think I managed to avoid her... And she's on her way out."
p "At the same time, watching that arse... Maybe I should have greeted her..."
p "Oh well, only a few more minutes of hard labour and my shift ends. I'll just stack these bubble gums once she's out of the store."
jump StoreShiftEndDay07

label StoreTeagan02Day07:
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
            jump StoreParkDay07
    "Sure Miss Cocque, let me help you with these heavy items, it'll be easy for me!":
        jump StoreTeagan05Day07

label StoreTeagan05Day07:
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

label StoreParkDay07:
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
        jump StoreShiftEndDay07
    "I don't know, I don't think I'll have time for that extra job...":
        t "Uh... OK, just think about it... Have a nice evening [name], I'll see you tomorrow at class, 9am sharp!"
        jump StoreShiftEndDay07

label StoreSecondWork01Day07:
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
        jump CleanStorageDay07
    "Build a pole-dancing platform with all the shit lying around" if (quentintipfrancine == True):
        jump PoleDancingDay07

label CleanStorageDay07:
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
jump StoreShiftEndSecondDay07

label PoleDancingDay07:
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
        jump PoleDance01Day07
    "Me no parl-ay Froggie. Sorry.":
        re "But you are supposed to! All shops must cater to French-speakers on Veri-Bosti island, it's the law!"
        p "Well clearly you speak English. So what are you moaning about?"
        re "Humpf, yes I do, but it is not my first language. I am looking for.. how do you say?... Washing powder?"
        p "Ah, let me show you, we have all the big brands and also the cheap ones that are exactly the same shit."
        jump StoreCustomerDay07
    "Vou-lay-vous couch-ay avec moi ce soir?":
        re "Hein? Mais ça va pas la tête? C'est un scandale!"
        p "Calm down now lady, I was just kidding... Why don't we speak English for a change, you speak English right?"
        re "Humpf, yes I do, but it is not my first language. I am looking for.. how do you say?... Washing powder?"
        p "Ah, let me show you, we have all the big brands and also the cheap ones that are exactly the same shit."
        jump StoreCustomerDay07

label StoreCustomerDay07:
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
        jump PoleDance01Day07
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
        
        jump PoleDance01Day07

label PoleDance01Day07:
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
            $ invitedfrancine07 = True
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
    jump BurbsChoiceDay07

label StoreShiftEndSecondDay07:
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
jump HalfPriceDay07

label StoreShiftEndDay07:
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
    jump StoreShiftEnd02Day07
if (catchfrancine == True):
    fa "Here's five dollars for your hard work [name]! I hope you come back again to work here. Goodbye."
    $ money += 5
    p "Yeah, maybe, I'll see..."
    jump StoreShiftEnd02Day07
    
label StoreShiftEnd02Day07:
if (halfprice == True):
    p "Hey, I can buy something half-price remember?"
    fa "Ah yes, silly me for not remembering..."
    jump HalfPriceDay07

label HalfPriceDay07:
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
        jump StoreShiftEnd03Day07
        
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
        jump StoreShiftEnd03Day07

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
        jump StoreShiftEnd03Day07

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
        jump StoreShiftEnd03Day07
    
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
        jump StoreShiftEnd03Day07

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
        jump StoreShiftEnd03Day07
    
    "Nothing actually...":
        jump StoreShiftEnd03Day07
        
label StoreShiftEnd03Day07:
scene store01 with dissolve
fa "That's it, you bought your item, now I have to close the store... Come back anytime to \"Seven Square\", your local shop that's opened from seven till... seven."
jump BurbsDay07
    
label StoreNoDealDay07:
scene store03 with dissolve
fa "That's a pity... Think about it, the job offer will be on all week."
jump StoreClerkDay07

label StoreBuyDay07:
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
        jump ClerkChoiceDay07

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
        jump ClerkChoiceDay07

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
        jump ClerkChoiceDay07

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
        jump ClerkChoiceDay07
    
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
        jump ClerkChoiceDay07

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
        jump ClerkChoiceDay07
    "Nothing actually...":
        jump ClerkChoiceDay07
        
label Beach01Day07:
$ seenbeach07 = True
stop music
play music "Sounds/oceanwaves.mp3"
scene beach with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah! Here's Tini-Wini-Bikini beach, as sunny as always... I should probably head for the beach bar first..."
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_102
    $ lustaddedB = 1
    call Challenger from _call_Challenger_103
    $ challengercalls += 2

label BeachBar01Day07:
$ beachbarseen07 = True
stop music
play music "Sounds/tropicalmusic.mp3"
scene beachbar01 with dissolve
$ renpy.pause(1.0, hard=True)
bb "Aloha, welcome to Tini-Wini-Bikini Beach bar! Again..."
bb "I regret to inform you that Randy Beach is closed today. For...err... cleaning."
p "Cleaning? Cleaning what?"
bb "Beachgoers have been complaining about the sand being err... sticky. With cum."
p "Ah, I see. I might be guilty as charged on that one if you see what I mean..."
bb "I don't want to see what you mean, I would rather poke my eyes out."
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
    p "Anyway, I'll be going I guess."
    bb "You guessed right."
    jump ExploreBeachDay07
if (hour <= 18) and (pierseen05 == False) and (pierseen06 == False):
    p "What horny news will you tell me today to brighten up my day?"
    scene beachbar01 with dissolve
    bb "Well, you'll be happy to know that today is \"Topless Saturday\". Most girls take advantage of that to get rid of their tanlines."
    p "Ooh! Now that lifted my spirits up, as well as something else... Excuse me while I readjust my bulge."
    bb "I hope you do realize you're just a sick pervert, right?"
    p "Maybe... Pray tell me, where are the topless girls, I haven't seen any on my way here?"
    bb "Well, for your perverse information, they usually hang out by the beach pier..."
    p "Thank you, kind lady! I shall bid you farewell and go on my adventurous quest." 
    $ toplesssaturday = True
    jump ExploreBeachDay07
bb "Today is \"Saturday Bikini Pageant.\" A weekly event organized by Audacious Bikinis. You might have heard of them..."
p "Yeah, I think I heard of them. My landlady's sister is the CEO of Audacious actually..."
scene beachbar03 with dissolve
bb "Oh, really? Then you might want to go and talk to her, she's over there and she's looking for jury members."
p "I shall indeed be on my merry way to perform my duty for the community!"
scene beachbar01 with dissolve
bb "That's good to hear. Now I can attend to REAL customers."
$ saturdaybikini = True
jump ExploreBeachDay07    

label ExploreBeachDay07:
if hour == 12 or hour == 13 and atelunchday07 == False:
    p "I'd better take a break and eat that sandwich Nancy prepared for me, I'm hungry... Let's find a cool place to enjoy the view."
    scene beach
    show mceating
    with dissolve
    $ renpy.pause(1.0, hard=True)
    p "What are you looking at? You never saw a guy eat a sandwich?"
    $ hour += 1
    $ atelunchday07 = True
    hide mceating
    show mcate
    with dissolve
    p "Ah, now I'm not hungry anymore. Amazing what eating does to your body. Let's move on then..."

stop music
play music "Sounds/oceanwaves.mp3"
if (hour >= 19) and (discoverclinic == False):
    p "It's getting late, I should really take the bus and get home now."
    $ bushome = True
    jump BusBeachHomeDay07
if (hour >= 20) and (discoverclinic == True):
    p "It's getting late, I should really take the shortcut through the clinic to get back home in time for dinner..."
    stop music
    scene clinicentrance with dissolve
    play music "Sounds/gardensound.mp3"
    $ renpy.pause(1.0, hard=True)   
    p "I wish I had discovered this shortcut earlier, it is really helpful in cutting my travel time between the burbs and the beach..."
    jump DinnerDay07

p "Hum... Where should I go?"
menu:
    "Go and meet Debby" if saturdaybikini and hour <= 18 and didsaturdaybikini == False:
        jump BikiniCompDay07
    "Walk along the beach" if (walkbeachseen07 == False):
        jump BeachWalkDay07
    "Go to the lifeguard tower" if (lifeguarddiscovered == True) and (seenlifeguard07 == False):
        jump Lifeguard01Day07
    "Head for the beach pier" if (hour <= 18) and toplesssaturday:
        jump PierDay07
    "Take the Bus to town" if (hour <= 18):
        $ bustown = True
        jump BusBeachTownDay07
    "Take the Bus back home" if (discoverclinic == False):
        $ bushome = True
        jump BusBeachHomeDay07
    "Take the shortcut back to the Burbs" if (discoverclinic == True):
        stop music
        scene clinicentrance with dissolve
        play music "Sounds/gardensound.mp3"
        $ renpy.pause(1.0, hard=True)   
        p "I wish I had discovered this shortcut earlier, it is really helpful in cutting my travel time between the burbs and the beach..."
        jump BurbsDay07

label BikiniCompDay07:
$ didsaturdaybikini = True
scene debbybikinicompbackground with dissolve
show debbybikiniprecomp01
$ renpy.pause(1.0, hard=True)   
p "(There's Debby turning her back to me. Time to ogle that fine arse a bit before talking to her...)"
window hide
hide debbybikiniprecomp01
show debbybikiniprecomp02
$ renpy.pause(1.0, hard=True)   
d "Oh hello [name]! I'm glad to see you, I'm looking for men to rate hot women in bikinis. *wink* Interested?"
p "You bet I am Debby!"
d "Then come along, the competition is about to start.. You'll be in the jury."
scene bikinicompbackground with fade
show debbybikinicomp02
$ renpy.pause(1.0, hard=True)   
d "Hello ladies and gentlemen, it is my pleasure to introduce you to this week's Audacious Tini-Wini-Bikini Beack Bikini pageant contestants."
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
p "(Well, that was a mouthful...)"
hide debbybikinicomp02
show debbybikinicomp03 with fastdissolve
d "First up is Brittany, who also happens to have won the beauty pageant at Hardcox High last night!"
hide debbybikinicomp03
show brittanybikinicomp01 with moveinright
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
br "HE-LLO Tini-Wini-Bikini beachgoers!"
d "Brittany is wearing a swimsuit from our \"Naughty Girl\" line..."
hide brittanybikinicomp01
show brittanybikinicomp02
br "Yes, I can be VERY naughty. If you're worthy of my Princess body..."
d "Well, Brittany is certainly a girl who knows what she wants and knows how to get it."
hide brittanybikinicomp02
show brittanybikinicomp03
br "And what I WANT is to WIN this tournament, and be forever known as the Tini-Wini-Bikini Queen!"
d "Of course, the title is up for grabs every week, but anyway... Thank you Brittany!"
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
hide brittanybikinicomp03
show sandybikinicomp01  with moveinright
d "Next up is Sandy, a student at Veri-Bosti University. She takes her studies seriously and her bikini line even MORE seriously!"
sa "A clean body is the first step to a clean mind. *wink*"
d "Ah, well said Sandy, and with THAT body, we had no other choice but to make you wear a bikini from our \"Bosomed Ladies\" line!"
hide sandybikinicomp01
show sandybikinicomp02
sa "My rack is as big as my IQ. So if you want a DEEP meaningful girl, be my Prince Charming boys!"
d "As you can see, the line is perfectly cut for a thick firm arse such as Sandy's..."
hide sandybikinicomp02
show sandybikinicomp03
sa "I just LOVE wearing it Debby, it's gorgeous! So everyone, be GORGEOUS TOO and vote for me!"
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
d "Thank you Sandy, let's meet our next contestant now. It's Anna! Please welcome her!"
hide sandybikinicomp03
show annabikinicomp01  with moveinright
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
d "Anna is a more mature contestant, so she's wearing a bikini from our \"Stacked MILF\" line, available in all our stores worldwide."
hide annabikinicomp01
show annabikinicomp02
an "And as you can see, I'm filling it up pretty well. Both up front and out back..."
d "Indeed, you are a great role-model for this line. So much so that Anna will feature in the next edition of Audacious Swimwear Magazine!"
hide annabikinicomp02
show annabikinicomp03
an "I'm very proud of this honor, and I'll gladly take another one today, so vote for me guys! *wink*"
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
hide annabikinicomp03
show hallebikinicomp01 with moveinright
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
d "Halle likes to study on the beach, wearing a skimpy Audacious Bikini such as the new \"Monokini X-Tream\" she's wearing right now for your eyes only!"
ha "I live life to the extreme... And I would be EXTREMELY grateful to WIN this competition! *wink"
hide hallebikinicomp01
show hallebikinicomp02
ha "And now... My firm buns wrapped around this EXTREMELY THIN bikini..."
da "It's almost as if you were wearing nothing at all. Exactly the look we were looking for. Thank you Halle!"
hide hallebikinicomp02
show hallebikinicomp03
ha "I LOVE to wear bikinis but I alos LOVE to wear nothing at all! *wink"
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
hide hallebikinicomp03
show debbybikinicomp02 with moveinleft
d "Thank you to all our contestants, it is now up to the jury to decide on this week's winner."
hide debbybikinicomp02
show debbybikiniprecomp02
d "So, [name], since you're the only jury member today, YOU get to decide."
p "What? Me? Ahem, that's a heavy responsability... I think the hott... I mean the best bikini model is..."
menu:
    "Brittany":
        jump BrittanyWinDay07
    "Sandy":
        jump SandyWinDay07
    "Anna":
        jump AnnaWinDay07
    "Halle":
        jump HalleWinDay07

label BrittanyWinDay07:
hide debbybikiniprecomp02
show debbybikinicomp02  at left with move
show brittanybikinicomp01 at right with moveinright
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
br "Yes, I win AGAIN! I'm the ultimate Beauty Queen!"
d "Yeah, ok, calm down, this is just a small weekly pageant. You don't get a trophy, just a $20 gift card from Audacious Bikinis."
br "Still, I'm the BEST WEEKLY QUEEN!"
p "*cough* Don't forget I voted for you your Highly Magnificious Majesty..."
br "It was the obvious choice, but I will still reward you my loyal subject."
window hide
if lust_points[1] == 9:
    $ lust_points[1] +=1
    $ score += 1
    show lustplus01:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lustplus01
if lust_points[1] <= 8:
    $ lust_points[1] +=2
    $ score += 2
    show lustplus02:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lustplus02
if lust_points[1] >= 10 and brittanyfucked == False:
    show epiclust:
        xalign 0.8 yalign 0.1
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    p "Ah, now we're talking!"
    br "Follow me to my quarters loyal subject."
    p "Which are where my Sumptuous Queen?"
    br "Err... In the beach bathrooms for the moment."
    p "How befitting."
    $ hour += 1
    jump BritPrefuckDay07
if lust_points[1] >= 10 and brittanyfucked:
    br "Follow me to my quarters loyal subject, your Queen needs some hot loving."
    menu:
        "Of course your Subliminal Empress of Beauty. Where are they?":
            br "Err... In the beach bathrooms for the moment."
            p "How befitting."
            $ hour += 1
            jump BritPrefuckDay07
        "Your Majesty deserves some quiet time, I cannot encroach on her Most Valuable Pampering.":
            br "What the hell are you talking about? I said come and FUCK ME!"
            p "And I heard \"Go and get fucked\". I will therefore follow your orders and quickly run away."
            $ hour += 1
            jump ExploreBeachDay07 
br "Though my reward is not sufficient to grant you an audience in my royal quarters."
p "Ah, damn."
d "The competition is over, thank you all for coming!"
$ hour += 1
jump ExploreBeachDay07

label SandyWinDay07:
hide debbybikiniprecomp02
show debbybikinicomp02  at left with move
show sandybikinicomp01 at right with moveinright
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
sa "I'm so happy! This is the best day of my week!"
d "Yeah, ok, calm down, this is just a small weekly pageant. You don't get a trophy, just a $20 gift card from Audacious Bikinis."
hide debbybikinicomp02 with dissolve
hide sandybikinicomp01
show sandybikinicomp03 with dissolve
sa "And I especially am happy with YOU my Prince Charming! You saved my week and you deserve a reward..."
p "I can't wait for it..."
window hide
if lust_points[19] == 9:
    $ lust_points[19] +=1
    $ score += 1
    show lustplus01:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lustplus01
if lust_points[19] <= 8:
    $ lust_points[19] +=2
    $ score += 2
    show lustplus02:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lustplus02
if lust_points[19] >= 10 and sandyfucked == False:
    show epiclust:
        xalign 0.8 yalign 0.1
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    p "Ah, finally, some epic sex coming my way!"
    sa "It will be epic my Prince Charming. Let's get naked and move to a quiet place. In total communion with Mother Nature..."
    $ hour += 1
    jump SandyFuckDay07
if lust_points[19] >= 10 and sandyfucked:
    sa "And my reward is... my body to you again my Prince Charming!"
    menu:
        "Of course, I'm looking forward to some more HOT loving Sandy!":
            sa "Let's get naked and move to a quiet place. In total communion with Mother Nature..."
            $ hour += 1
            jump SandyFuckDay07
        "Ah, you know what, I'm too busy right now, gotta go. Gotta go, gotta go.":
            sa "What? But... My Prince Charming!"
            p "Yep, see you later Sandy. gotta go."
            $ hour += 1
            jump ExploreBeachDay07 
sa "Unfortunately, I will still wait for my True Prince Charming to come along."
p "What, it's not me?"
sa "Did you see an epiclust icon?"
p "Err... No."
sa "Then it's not you. Bye [name]!"
d "The competition is over, thank you all for coming!"
$ hour += 1
jump ExploreBeachDay07

label AnnaWinDay07:
hide debbybikiniprecomp02
show debbybikinicomp02  at left with move
show annabikinicomp01 at right with moveinright
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
an "Yes, I win AGAIN! I'm the ultimate Beauty Queen!"
d "Yeah, ok, calm down, this is just a small weekly pageant. You don't get a trophy, just a $20 gift card from Audacious Bikinis."
an "Still, I'm the BEST WEEKLY QUEEN!"
p "*cough* Don't forget I voted for you your Highly Magnificious Majesty..."
an "It was the obvious choice, but I will still reward my loyal subject."
window hide
if lust_points[0] == 9:
    $ lust_points[0] +=1
    $ score += 1
    show lustplus01:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lustplus01
if lust_points[0] <= 8:
    $ lust_points[0] +=2
    $ score += 2
    show lustplus02:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lustplus02
if lust_points[0] >= 10 and annafucked == False:
    show epiclust:
        xalign 0.8 yalign 0.1
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    p "Ah, finally, the douchebag's mother!"
    an "I'm really horny but it will have to wait tonight [name]. Come to my house *discreetly* this evening for your reward... *wink*"
    p "I won't miss our hot date Anna!"
    $ annawaiting = True
    $ hour += 1
    jump ExploreBeachDay07
an "Nice try but this stacked MILF is harder to get than that, boy!"
p "Ah, damn."
d "The competition is over, thank you all for coming!"
$ hour += 1
jump ExploreBeachDay07

label HalleWinDay07:
hide debbybikiniprecomp02
show debbybikinicomp02 at left with move
show hallebikinicomp01 at right with moveinright
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)   
ha "Finally, I'll be able to afford buying a new bikini without having to screw some guy for his money!"
d "You just a $20 gift card from Audacious Bikinis so it will have to be an extremely TINY bikini for that price."
hide debbybikinicomp02 with dissolve
hide hallebikinicomp01
show hallebikinicomp03 with dissolve
ha "Having said that, I wouldn't mind screwing around with YOU, stud... You deserve a reward for being such a gentleman."
p "Me? Oh, I'm... I didn't expect this at all! What a pleasant surprise."
window hide
if lust_points[9] == 9:
    $ lust_points[9] +=1
    $ score += 1
    show lustplus01:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lustplus01
if lust_points[9] <= 8:
    $ lust_points[9] +=2
    $ score += 2
    show lustplus02:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lustplus02
if lust_points[9] >= 10 and hallefucked == False:
    show epiclust:
        xalign 0.8 yalign 0.1
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    p "Ah, finally, some epic sex coming my way!"
    ha "I can't wait for your MASSIVE dong, let's go quickly NAKED into the sea! Where no one can see us..."
    $ hour += 1
    jump HalleFuckDay07a
if lust_points[9] >= 10 and hallefucked:
    ha "I want your MASSIVE dong again, let's go quickly NAKED into the sea! Where no one can see us..."
    menu:
        "Of course, I'm already hard and almost tearing a hole in my speedos!":
            $ hour += 1
            jump HalleFuckDay07a
        "Ah, you know what, I'm late for something.":
            ha "Something more important than fucking ME???"
            p "Yeah, err... It's like MEGA-important. Bye Halle."
            $ hour += 1
            jump ExploreBeachDay07 
ha "On second thoughts... I need to study."
p "I can teach anatomy. With my cock."
ha "I think my textbook is more appropriate right now."
p "Damn... That line never works, I don't understand why."
d "The competition is over, thank you all for coming!"
$ hour += 1
jump ExploreBeachDay07

label BusBeachTownDay07:
scene beach with dissolve
$ renpy.pause(1.0, hard=True)   
p "Bye bye Tini-Wini-Bikini beach!"
p "Ah, here's the bus going to town..."
jump BusEndDay07

label BusBeachHomeDay07:
scene beach with dissolve
$ renpy.pause(1.0, hard=True)   
p "Bye bye Tini-Wini-Bikini beach!"
p "Ah, here's the bus going to the burbs..."
jump BusEndDay07

label BeachWalkDay07:
$ walkbeachseen07 = True    
if (boughthallebikini == True) and ((walkbeachseen == False) or (beachswimday03 == True)) and (((walkbeachseen04 == False) or (beachswimday04 == True)) or ((walkbeachseen05 == False) or (beachswimday05 == True)) and (hallefucked == False)):
    jump HalleBeachDay07

else:
    scene beachempty with dissolve
    $ renpy.pause(1.0, hard=True)  
    if (beachswimday04 == False) and (beachswimday03 == False) and (beachswimday05 == False) and (beachswimday06 == False):
        "This secluded part of the beach is empty... I could always go for a swim I guess."
        menu:
            "Go for a swim" if (beachswimday05 == False) and (beachswimday04 == False) and (beachswimday03 == False) and (beachswimday06 == False) and (beachswimday07 == False):
                jump BeachSwimDay07
            "Don't go for a swim":
                jump ExploreBeachDay07
    "This secluded part of the beach is empty today. BORING!"
    jump ExploreBeachDay07

label PierDay07:
$ pierseen07 = True
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
        jump Pier02Day07
    "Well, I'm just a boy, you have nothing to fear from me. I'm just here to learn about the bees and the boo-bees.":
        re "Umpf. I think that it is highly inappropriate. Your mother is the one who is supposed to teach you about that, not me!"
        p "She's doing it, she's doing it, don't worry..."
        re "Come Isabelle, we'll leave, I don't want to have anything to do with this!"
        p "(Pfff, what did I say wrong?)"
        jump Pier02Day07        
        
label Pier02Day07:
scene pier03 with dissolve
$ renpy.pause(1.0, hard=True)
p "I'd better be more discreet, I'm making them flee like... fleas."
scene pier04 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ho Ho Ho! What do we have here? Nikki and Chantelle sunbathing topless!"
menu:
    "Approach them quietly":
        jump NikkiChantellePier01Day07
    "Call out Nikki's name":
        jump NikkiChantellePier02Day07
    "Call out Chantelle's name":
        jump NikkiChantellePier03Day07

label NikkiChantellePier01Day07:
scene pier05 with dissolve
$ renpy.pause(1.0, hard=True)
p "(boobies... Boobies... BOOBIES!)"
scene pier06 with dissolve
$ renpy.pause(1.0, hard=True)
s "Oh, I should have known it was you. The only boy who can't keep his mouth shut when he's thinking."
ch "What was he saying exactly? \"Boobies\" repeatedly, if I recall correctly."
menu:
    "Err... It was just a song that was in my head.":
        ch "Right, it had nothing to do with Nikki and me being topless... I'm starting to think your mother's tenant is a serial liar... and pervert."
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
        jump NikkiChantelleChoiceDay07
    "Well, your boobies are indeed so nice that they messed with my mind. It's a compliment really!":
        ch "I see... So you like what you see then naughty boy?"
        s "You really shouldn't encourage [name]. He's a total pervert..."
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
            jump NikkiChantelleChoiceDay07

label NikkiChantelleChoiceDay07:
menu:
    "Chantelle, I was wondering if you wanted to accompany me to the downtown gym, I'm a member and I can invite you for free..." if (gymmember == True) and (invitedchantelle == False) and (invitedchantelle05 == False) nd (invitedchantelle06 == False):
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
        $ invitedchantelle07 = True
        p "Well, I'll call you when I get there so you can join me then. See you around Chantelle!"
        ch "Goodbye [name]. Thanks for stopping by."
        s "Umpf..."
        $ hour += 1
        jump ExploreBeachDay07
    "Not really. I was just coming by to say hi. I'll leave you two alone then.":
        ch "Yes, please don't disturb us again when we're sunbathing. Girls need to concentrate to get the perfect tan."
        p "Right... Of course."
        $ hour += 1
        jump ExploreBeachDay07

label NikkiChantellePier02Day07:
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
jump NikkiChantelleChoiceDay07
  
label NikkiChantellePier03Day07:
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
    "Actually yes. I was wondering if you wanted to accompany me to the downtown gym, I'm a member and I can invite you for free..." if (gymmember == True):
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
        p "Well, I'll call you when I get there so you can join me then. See you around Chantelle!"
        ch "Goodbye [name]. Thanks for stopping by."
        s "Umpf..."
        $ hour += 1
        jump ExploreBeachDay07
    "Not really. I was just coming by to say hi. I'll leave you two alone then.":
        ch "Yes, please don't disturb us again when we're sunbathing. Girls need to concentrate to get the perfect tan."
        p "Right... Of course."
        $ hour += 1
        jump ExploreBeachDay07

label BeachSwimDay07:
$ beachswimday07 = True
play music "Sounds/randybeachsound.mp3"
scene beachswim01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I can see some coral reefs below. Let's dive and have a look!"        
scene beachswim02 with dissolve
play music "Sounds/underwater.mp3"
$ renpy.pause(1.0, hard=True)
p "What the hell is that thing swimming towards me?"
jump Mermaid01Day07

label HalleBeachDay07:
$ walkbeachseen07 = True 
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
        jump Underwater01bDay07
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
        jump Underwater01bDay07

label Underwater01bDay07:
scene hallebeach03 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Come on, this way! You'll see, it's gonna be ssoo much fun!"

label Underwater02Day07:
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
        jump Mermaid01Day07
    "Sneak under her":
        scene underwater03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Bingo, she's smiling at me... I wonder what a kiss underwater feels like..."
        scene underwater03b with dissolve
        p "What's wrong, she seems to be scared of something..."
        scene underwater04 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "She's darting off... OMG, what the fuck is that?..."
        jump Mermaid01Day07

label Mermaid01Day07:
scene mermaid01 with dissolve
$ renpy.pause(1.0, hard=True)
p "This mermaid is captivating... OK, she has a fish tail and all that but... Mmmh, those tits..."
scene mermaid02 with dissolve
$ renpy.pause(1.0, hard=True)
p "She seems to be signalling me to follow her..."
menu:
    "Follow her":
        jump Mermaid02Day07
    "Get the hell out of here and re-join Halle" if (beachswimday07 == False):
        $ underwaterleft = True
        jump Underwater03Day07
    "Get the hell out of here" if (beachswimday07 == True):
        scene beachswim01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Phew, that was close!I'm still shaking. Better go back to the beach..." 
        scene beachempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ExploreBeachDay07

label Mermaid02Day07:
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
        jump Mermaid03Day07
    "Get the hell out of here and re-join Halle" if (beachswimday07 == False):
        jump Underwater03Day07
    "Get the hell out of here" if (beachswimday07 == True):
        scene beachswim01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Phew, that was close!I'm still shaking. Better go back to the beach..." 
        scene beachempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ExploreBeachDay07
        
label Mermaid03Day07:
scene mermaid08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Here we go, it's tough to aim underwater but once I'm in, it shouldn't move too much..."
scene
play movie "Day3/mermaidfuckslow.ogv" loop
show movie with fade
show faster
call screen mermaidfuckslowDay07
screen mermaidfuckslowDay07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MermaidFuckFastDay07")
label MermaidFuckFastDay07:
hide faster
play movie "Day3/mermaidfuckfast.ogv" loop
show cum
call screen mermaidfuckfastDay07
screen mermaidfuckfastDay07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MermaidFuckCumDay07")
label MermaidFuckCumDay07:
stop movie
scene mermaid09 with dissolve
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
if extras >= 5 and (achievement.has("extrasontheside") == False):
    show achievement21:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement21
    $ achievement.grant("extrasontheside")
if (beachswimday07 == False):
    jump Underwater03Day07
if (beachswimday07 == True):
    scene beachswim01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "The sea is getting rough. I'd better go back to the beach..." 
    scene beachempty with dissolve
    $ renpy.pause(1.0, hard=True)
    jump ExploreBeachDay07

label Underwater03Day07:
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
            jump HalleBackBeach01Day07
        else:
            scene hallesea04 with dissolve
            $ renpy.pause(1.0, hard=True)
            ha "Ha ha! You boys really are all the same... A pair of tits, that's all that counts!"
            ha "Let's get back to the beach, the sea is getting rough..."
            p "Great idea..."
            jump HalleBackBeach01Day07
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
        jump HalleBackBeach01Day07        
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
        jump HalleBackBeach01Day07
        
label HalleBackBeach01Day07:
stop music
play music "Sounds/oceanwaves.mp3"
scene hallebeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Well, that was fun, apart from this vile creature... I think I'd better head back to the university, I need to study."
menu:
    "Okay, I hope to see you again Halle...":
        ha "You will, don't worry... If you come back to the beach, I'll be here..."
        jump ExploreBeachDay07
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True) and (lust_points[9] >=8):
        jump HallePendulumDay07
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
        jump ExploreBeachDay07

label HallePendulumDay07:
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
    jump HalleFuckDay07
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
    jump HalleFuckDay07   

label HalleFuckDay07:
scene hallebeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "I think I changed my mind... I would rather spend some \"quality\" time with you after all..."
ha "And by \"quality\", I mean some hot, steamy SEX!"
p "Alright, I'm in baby!"
label HalleFuckDay07b:
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
label HalleFuckDay07a:
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
label HallePrefuckDay07:
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
        jump HallePrefuckDay07
    "Spread her legs and fuck her pussy slowly":
        ha "You want to fuck me some more stud? Yeah, I 'm ready for your great big horsecock, come and ram that monstercock home!"
        jump HalleFuckMovieDay07

label HalleFuckMovieDay07:
stop music
play sound "Sounds/oceanwaves.mp3"
play music "Sounds/hallefuckslow.mp3"
show hallefuckslow
show faster
call screen hallefuckslowDay07
screen hallefuckslowDay07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("HalleFuckFastDay07")
label HalleFuckFastDay07:
hide faster
play music "Sounds/hallefuckfast.mp3"
show hallefuckfast
show cum
call screen hallefuckfastDay07
screen hallefuckfastDay07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("HalleFuckCumDay07")

label HalleFuckCumDay07:
hide hallefuckfast
hide hallefuckslow
stop sound
stop music
play music "Sounds/oceanwaves.mp3"

scene hallefuckcum01 with dissolve
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
    
jump ExploreBeachDay07

label Lifeguard01Day07:
stop music
scene tower01 with dissolve
$ seenlifeguard07 = True
$ renpy.pause(1.0, hard=True)

if (hour == 16) and (workedseconddaylifeguard == True):
    pa "Oh, hi there [name]. You still have some energy to work after this morning's swimming practise?"
    p "Yeah, sure, full of ENERGY!..."
    pa "So, you wanna start working today?"
    menu:
        "Sure, I'm in!":
            jump LifeGuardWorkThirdDay07
        "Maybe another day...":
            pa "Fine, your choice, hope to see you back here at 4pm another day..."
            jump ExploreBeachDay07
    
if (hour == 16) and (wonarmwrestling == True):
    pa "Hi again [name]. So, you wanna start working today?"
    menu:
        "Sure, I'm in!":
            jump LifeGuardWorkDay07
        "Maybe another day...":
            pa "Fine, your choice, hope to see you back here at 4pm another day..."
            jump ExploreBeachDay07
if (hour >=17) and (wonarmwrestling == True):
    pa "It's a bit late to start a workshift. We're almost done here. Come back tomorrow at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay07
if (hour <=15) and (wonarmwrestling == True):
    pa "It's a bit early to start a workshift. Come back at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay07

mb "What do you want kid? You lost your mommy?"
pa "Ha ha, nice one Mitch!"
p "Is making fun of people part of your job?"
pa "Calm down boy, it was just in jest... I'm Pamela, the head lifeguard, this dufus is Mitch, how may we help you?"
p "I'd like to become a lifeguard, I'm strong and I can swim well."
scene tower02 with dissolve
$ renpy.pause(1.0, hard=True)
mb "Ooh! Is that so? Look Pam, David Hasselhof! Ha ha!"
p "(I'm really starting to dislike this jerk...)"
pa "Well, we could use some additional help at peak time, between 4pm and 6pm, would you be interested?"
p "Sure, anything to help the community."
window hide
$ lust_points[18] += 1
$ score += 1
show lust01:
    xalign 0.6 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
scene tower07 with dissolve
$ renpy.pause(1.0, hard=True)
pa "What's your name?"
p "[name] Johnson. So, when can I start working as a lifeguard then?"
pa "Such eagerness! At 4pm, that's peak time for beachgoers. And we need you for two hours, pay is 10 dollars an hour."
if (hour == 16):
    pa "And as it turns out, it's 4pm. So, you wanna start working today?"
    menu:
        "Sure, I'm in!":
            jump LifeGuardWorkDay07
        "Maybe another day...":
            pa "Fine, your choice, hope to see you back here at 4pm another day..."
            jump ExploreBeachDay07
if (hour >=17) and (wonarmwrestling == True):
    pa "It's a bit late to start a workshift. We're almost done here. Come back tomorrow at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay07
if (hour <=15) and (wonarmwrestling == True):
    pa "It's a bit early to start a workshift. Come back at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay07

label LifeGuardWorkDay07:
if (workedfirsdaylifeguard == True):
    jump LifeGuardSecondWorkDay07
$ workedfirsdaylifeguard = True
scene tower08 with dissolve
$ renpy.pause(1.0, hard=True)
pa "We have to take turns looking out for swimmers in distress. Mitch, get me a beer."
mb "Sure boss!"
menu:
    "You shouldn't be drinking on the job...":
        pa "Says who? Just a beer here and there, no big deal!"
        window hide
        $ lust_points[18] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump LifeGuardWork02Day07
    "Oh yeah, I'll get one too!":
        pa "No you won't, you're too young. Your turn on the binoculars anyway."
        jump LifeGuardWork02Day07
    "None for me, I'm fully concentrated on the job.":
        pa "Nice, so I can drink my beer and not worry then..."
        window hide
        $ lust_points[18] += 1
        $ score += 1
        show lust01:
            xalign 0.7 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump LifeGuardWork02Day07    

label LifeGuardWork02Day07:
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
        jump LifeguardSmall01Day07
    "The tall woman on the right. (Sandy)":
        jump LifeguardsBig01Day07


label LifeguardSmall01Day07:
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
        jump TowerEndDay07
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
        jump TowerEndDay07
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
        jump TowerEndDay07

label LifeguardsBig01Day07:
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
window hide
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
        window hide
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
        jump TowerEndDay07
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
        jump TowerEndDay07

label LifeGuardSecondWorkDay07:
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
        jump LifeGuardWorkSecond02Day07
    "Oh yeah, I'll get one too!":
        pa "No you won't, you're too young. Your turn on the binoculars anyway."
        jump LifeGuardWorkSecond02Day07
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
        jump LifeGuardWorkSecond02Day07

label LifeGuardWorkSecond02Day07:
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
    jump SavedLollySecondDay07
if (savedlolly == True):
    jump SavedSandySecondDay07
    
label SavedLollySecondDay07:
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
        jump TowerEndDay07
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
        jump TowerEndDay07
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
        jump TowerEndDay07

label SavedSandySecondDay07:
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
    jump SavedSandyLowStrengthDay07
if (strength >= 9):
    jump SavedSandyHighStrengthDay07

label SavedSandyLowStrengthDay07:
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
        jump TowerEndDay07
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
        jump TowerEndDay07

label SavedSandyHighStrengthDay07:
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
        jump SandyFuckDay07a     
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
        jump SandyFuckDay07a

label LifeGuardWorkThirdDay07:
pa "Great, let's start then! Today, we'll be heading to Lust Lagoon to check on sailboats in the area."
mb "Hey, what about me?"
pa "You stay here to watch the beachgoers. You can handle that Mitch, can't you?"
mb "Grumpf...."
scene tower07 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Alright, let's go, I hope you don't get seasick easily..."
p "Na, I'm fine, I'm DA MAN!"
pa "Well, help me get the boat afloat instead of bragging [name]..."
scene pamelasea01 with dissolve
play music "Sounds/boatengine.mp3"
$ renpy.pause(1.0, hard=True)
pa "Not too cold for you [name]?"
p "I'm fine Pamela... When are we arriving?"
pa "Soon..."
stop music
scene pamelasea02 with dissolve
play music "Sounds/oceanwaves.mp3"
$ renpy.pause(1.0, hard=True)
pa "There, a sailboat. Strange, there doesn't seem to be anyone on board..."
scene pamelasea03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oh no, it's that boy again! He's EVERYWHERE! Can we book him for indecency?"
pa "I'm afraid not, it's perfectly legal to fuck in public in Lust Lagoon... So there's nothing you can do about it."
pa "But Lord is his cock GIGANTIC! That girl must be having the time of her life!"
play sound "Sounds/distantfuck.mp3"
rb "Hi there buddy, enjoying the view? My girlfriend is sure enjoying the pounding I'm giving her..."
p "FUCK YOU! Let's get out of here Pamela..."
pa "Ha ha, you seem to be a tad jealous [name]..."
p "Pfff, he's got nothing on me! I'm da man, I'm DA MAN!"
stop sound
$ hour += 1
scene pamelasea01 with dissolve
play music "Sounds/boatengine.mp3"
$ renpy.pause(1.0, hard=True)
pa "I'm feeling thirsty, seeing all that water around us..."
stop music
play sound "Sounds/boatenginefail.mp3"
pa "What's going on, why did the engine stop?"
scene pamelasea04 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Shit, the rotor is stuck, I would need some lubricant to get it going again or we're stuck here until Mitch comes to get us... And I have no beer..."
menu:
    "I've got some extra-strong lubricant!" if (wd69 == True):
        scene pamelasea05 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "Really, that's great! You truly are DA MAN, a man with many talents!"
        $ enginerepaired = True
        $ lust_points[18] += 1
        $ score += 1
        window hide
        show lust01:
            xalign 0.4 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        scene pamelasea04 with dissolve
        $ renpy.pause(1.0, hard=True)        
        pa "We're good to go again!"
        if (lust_points[18] >= 10):
            window hide
            show epiclust:
                xalign 0.2 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust
            scene pamelasea05 with dissolve
            $ renpy.pause(1.0, hard=True)
            pa "But I'm not in a hurry... We won't leave until you've FUCKED ME GOOD AND HARD!"
            jump PamelaPrefuckDay07
        if (beercase == True):
            p "You know what? I also happen to have some beer with me... Conveniently packed in my backpack which I carry with me everywhere;"
            scene pamelasea05 with dissolve
            $ renpy.pause(1.0, hard=True)
            pa "Ooh, really? Gimme, gimme, gimme..."
            if (lust_points[18] == 9):
                window hide
                $ lust_points[18] += 1
                $ score += 1
                show lust01:
                    xalign 0.4 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
            if (lust_points[18] <= 8):
                window hide
                $ lust_points[18] += 2
                $ score += 2
                show lust02:
                    xalign 0.4 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust02
            scene pamelasea07 with dissolve
            play sound "Sounds/canopening.mp3"
            $ renpy.pause(1.0, hard=True)
            pa "Mmh, this beer is so nice... I could drink beer all day. Just like a Supreme Court Justice."
            if (lust_points[18] >= 10):
                window hide
                show epiclust:
                    xalign 0.7 yalign 0.2
                    zoom 0.5
                    linear 2.0 zoom 1.0
                play sound "Sounds/epiclust.mp3"
                $ renpy.pause(4.0, hard=True)
                hide epiclust
                scene pamelasea05 with dissolve
                $ renpy.pause(1.0, hard=True)
                pa "But I'm not in a hurry... We won't leave until you've FUCKED ME GOOD AND HARD!"
                jump PamelaPrefuckDay07
            scene pamelasea06 with dissolve
            $ renpy.pause(1.0, hard=True)
            pa "We should probably head back to the beach, we've seen enough... And I can't get that kid's HUGE cock out of my head..."
            $ hour += 1
            scene tower01 with dissolve
            play music "Sounds/oceanwaves.mp3"
            $ renpy.pause(1.0, hard=True)
            pa "Here's your twenty dollars."
            p "Thanks Pamela, always a pleasure to work with you!"
            pa "Hopefully, if you come back to work here, you'll be more productive than today..."
            $ money += 20
            jump ExploreBeachDay07            
        scene pamelasea06 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "We should probably head back to the beach, we've seen enough... And I can't get that kid's HUGE cock out of my head..."
        $ hour += 1
        scene tower01 with dissolve
        play music "Sounds/oceanwaves.mp3"
        $ renpy.pause(1.0, hard=True)
        pa "Here's your twenty dollars."
        p "Thanks Pamela, always a pleasure to work with you!"
        pa "Hopefully, if you come back to work here, you'll be more productive than today..."
        $ money += 20
        jump ExploreBeachDay07       
    "I've got some beer!" if (beercase == True):
        scene pamelasea05 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "Really, that's great! You truly are DA MAN, give me a bottle!"
        if (lust_points[18] == 9):
            window hide
            $ lust_points[18] += 1
            $ score += 1
            show lust01:
                xalign 0.4 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        if (lust_points[18] <= 8):
            window hide
            $ lust_points[18] += 2
            $ score += 2
            show lust02:
                xalign 0.4 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust02
        scene pamelasea07 with dissolve
        play sound "Sounds/canopening.mp3"
        $ renpy.pause(1.0, hard=True)
        pa "Mmh, this beer is so nice... I could drink beer all day. Just like a Supreme Court Justice."
        if (lust_points[18] >= 10):
            window hide
            show epiclust:
                xalign 0.7 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust
            scene pamelasea05 with dissolve
            $ renpy.pause(1.0, hard=True)
            pa "But I'm not in a hurry... We won't leave until you've FUCKED ME GOOD AND HARD!"
            jump PamelaPrefuckDay07 
        scene pamelasea06 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "We should probably head back to the beach, we've seen enough... And I can't get that kid's HUGE cock out of my head..."
        $ hour += 1
        scene tower01 with dissolve
        play music "Sounds/oceanwaves.mp3"
        $ renpy.pause(1.0, hard=True)
        pa "Here's your twenty dollars. Even though we didn't get much done."
        if (enginerepaired == False):
            p "It's not my fault the engine stopped running..."
            pa "I'll have it fixed tomorrow morning. Hopefully, if you come back to work here, you'll be more productive..."
        $ money += 20
        jump ExploreBeachDay07       
    "Ah damn. Maybe we could fuck like that couple while we wait for Mitch?":
        scene pamelasea06 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "How dare you! I'm your BOSS remember!"
        window hide
        $ lust_points[18] -= 2
        $ score -= 2
        show lustminus02:
            xalign 0.5 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus02
        pa "Now we'll just have to wait like idiots on this boat until Mitch arrives..."
        scene pamelasea08 with dissolve
        $ hour += 1
        $ renpy.pause(1.0, hard=True)
        mb "Yo boss! Mitch Bigcannon to the rescue!"
        pa "About time... Get us back on shore, I'm sick and tired of this boring empty ocean..."
        stop music
        scene tower01 with dissolve
        play music "Sounds/oceanwaves.mp3"
        $ renpy.pause(1.0, hard=True)
        pa "Here's your twenty dollars. Even though you hardly deserve them..."
        p "Hey, it's not my fault the engine stopped running!"
        pa "I'll have it fixed tomorrow morning. Hopefully, if you come back to work here, you'll be more productive..."
        $ money += 20
        jump ExploreBeachDay07        
    "I guess there's nothing we can do but wait...":
        scene pamelasea06 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "I thought men were good with engines..."
        p "I don't want to dirty my hands with oil and shit."
        pa "Well, you're useless then! Now we'll just have to wait like idiots on this boat until Mitch arrives..."
        window hide
        $ lust_points[18] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.5 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        scene pamelasea08 with dissolve
        $ hour += 1
        $ renpy.pause(1.0, hard=True)
        mb "Yo boss! Mitch Bigcannon to the rescue!"
        pa "About time... Get us back on shore, I'm sick and tired of this boring empty ocean..."
        stop music
        scene tower01 with dissolve
        play music "Sounds/oceanwaves.mp3"
        $ renpy.pause(1.0, hard=True)
        pa "Here's your twenty dollars. Even though you hardly deserve them..."
        if (enginerepaired == False):
            p "It's not my fault the engine stopped running..."
            pa "I'll have it fixed tomorrow morning. Hopefully, if you come back to work here, you'll be more productive..."
        $ money += 20
        jump ExploreBeachDay07
        
label PamelaPrefuckDay07:
scene pamelaprefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "So let's get lusty in Lust Lagoon!"
if (stamina <=0) and (whitebull == False):
    p "I'm kind of sea-sick actually... I'm not at my peak and I want to go back on land..."
    scene pamelaprefuck01a with dissolve
    $ renpy.pause(1.0, hard=True)
    pa "So you LIED to me when you said you didn't get sea-sick... I see. I'm bitterly disappointed."
    if (pamelajosewin == True):
        pa "José did'nt have any trouble at all fucking me with his GIANT cock..."
    pa "I'll bring you back on land and then you can get lost, I'm not paying you today!"
    window hide
    $ lust_points[18] -=2
    $ score -= 2
    show lustminus02:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus02
    p "What? Hey, my work doesn't actually include FUCKING YOU..."
    pa "Alright, I'll give you 10 dollars, but don't push your luck!"
    $ hour += 1
    scene tower12 with dissolve
    pa "Here's your ten bucks. If you want to come back and work here, you'd better have some STAMINA left in you, got it?"
    p "Err... Yeah, got it, sorry about that..."    
    $ money += 10
    jump ExploreBeachDay07    
if (stamina <=0) and (whitebull == True):
    p "Now is definitely the time to take some white bull, she'll throw me overboard if I can't perform..."
    show whitebull
    show square
    play sound "Sounds/lost.mp3"
    "You gulped down your White Bull energy drink."
    hide square
    hide whitebull
    $ whitebull = False
    $ stamina += 2
    
label PamelaFuckDay07:
scene pamelaprefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
pa "I'm totally naked and dripping wet, come and get me stud!"
p "I would cross water, big water, like ocean water to get you Pamela! And this island is surrounded by it too!"
scene pamelaprefuck03 with dissolve
play sound "Sounds/pamela01.mp3"
$ renpy.pause(3.0, hard=True)
pa "Mmmh, your cock is just as HUGE as that kid we saw! What do they feed you boys?"
p "I don't know but what I can feed YOU are 18 inches of prime beef right there...."
pa "And what should we do with this thing and my dripping wet pussy?"
label PamelaFuckChoiceDay07:
menu:
    "I need to see that scrumptious arse of yours while I fuck you!" if (pameladoggy == False):
        pa "I'm guessing doggy then, right?"
        p "Correct answer. You've just won... 18 inches of boymeat up your twat!"
        jump PamelaDoggyDay07
    "Let's fuck in the water!" if (pamelastand == False):
        pa "What? That sounds dangerous.... but so adventurous too, I'm in!"
        jump PamelaStandDay07
    "There's a cave that still needs exploring..." if (pamelaanal == False):
        pa "Wh... What do you mean?"
        p "I mean, I'm going to bang your backside!"        
        jump PamelaAnalDay07
    "Why don't you kneel in front of my giant prong and worship it?" if (pamelablow == False):
        pa "It certainly is big enough to warrant worshipping!"
        jump PamelaBlowDay07
    "Let me lift you up on my shaft for the grand finale..." if (pamelastand == True) and (pameladoggy == True) and (pamelaanal == True) and (pamelablow == True):
        jump PamelaMovieDay07

label PamelaDoggyDay07:
$ pameladoggy = True
scene pameladoggy01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Easy for you to say, it's the size of my fist!"
p "I'll lube it up with some precum..."
scene pameladoggy02 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Wow, can you just spurt on demand?"
p "Well, I do have a HUGE supply of baby-batter in my giant nuts..."
scene pameladoggy03 with dissolve
$ renpy.pause(1.0, hard=True)
p "There, that's better, it just slipped in..."
pa "OOOH, DAMN! How far is it already?"
p "Not far enough..."
label PamelaDoggyDay07b:
play music "Sounds/pameladoggy.mp3"
scene pameladoggy04 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy03 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy04 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy03 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy04 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy03 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy04 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy03 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy04 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy03 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy04 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy03 with dissolve
$ renpy.pause(0.1, hard=True)
scene pameladoggy04
$ renpy.pause(0.3, hard=True)
scene pameladoggy03
$ renpy.pause(0.3, hard=True)
scene pameladoggy04
$ renpy.pause(0.3, hard=True)
scene pameladoggy03
$ renpy.pause(0.3, hard=True)
scene pameladoggy04
$ renpy.pause(0.3, hard=True)
scene pameladoggy03
$ renpy.pause(0.3, hard=True)
scene pameladoggy04
$ renpy.pause(0.3, hard=True)
scene pameladoggy03
$ renpy.pause(0.3, hard=True)
scene pameladoggy04
$ renpy.pause(0.3, hard=True)
scene pameladoggy03
$ renpy.pause(0.3, hard=True)
scene pameladoggy04
$ renpy.pause(0.3, hard=True)
scene pameladoggy03
$ renpy.pause(0.3, hard=True)
scene pameladoggy04
$ renpy.pause(0.3, hard=True)
scene pameladoggy03
$ renpy.pause(0.3, hard=True)
scene pameladoggy04
$ renpy.pause(0.3, hard=True)
scene pameladoggy03
$ renpy.pause(0.3, hard=True)
scene pameladoggy04
$ renpy.pause(0.3, hard=True)
scene pameladoggy03
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        p "Let's do it one more time!"
        pa "Oh Lord have mercy on me!"
        jump PamelaDoggyDay07b
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaFuckChoiceDay07

label PamelaStandDay07:
$ pamelastand = True
scene pamelastand01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Just the tip of your monster cock is already filling me up like never before!"
p "Wait till you get another fifteen inches of it..."
label PamelaStandDay07b:
play music "Sounds/pamelawater.mp3"
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelastand01 with dissolve
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        p "I'm still horny for some more of that!"
        jump PamelaStandDay07
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaFuckChoiceDay07

label PamelaAnalDay07:
$ pamelaanal = True
scene pamanal01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "I don't know... It doesn't look your mammoth dong could possibly fit inside my tiny backdoor..."
p "We'll soon find out..."
pa "My God, those balls are so FULL! And that shaft is so THICK!"
scene pamanal02 with dissolve
$ renpy.pause(1.0, hard=True)
p "See, it fits..."
pa "OK, then pile-drive into me and show me how you really fuck an arse stud!"
label PamelaAnalDay07b:
scene pamanal03
play music "Sounds/pameladoggy.mp3"
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
scene pamanal03
$ renpy.pause(0.3, hard=True)
scene pamanal02
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        p "Your arse feels so tight and warm around my shaft... I want MORE OF THAT!"
        pa "I'll try and keep up with your pounding, go for it!"
        jump PamelaAnalDay07b
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaFuckChoiceDay07

label PamelaBlowDay07:
$ pamelablow = True
scene pamelablow01 with dissolve
play sound "Sounds/pamelablow01.mp3"
$ renpy.pause(3.0, hard=True)
pa "Oh my... This MONSTER cock is truly a thing of beauty!"
p "Why don't you show your appreciation by kissing the tip?..."
scene pamelablow02 with dissolve
play sound "Sounds/kissing.mp3"
$ renpy.pause(2.0, hard=True)
p "Yeah! And now, kiss the helmet with... your THROAT!"
pa "I'll need to open wide to fit this battering ram inside... But it deserves it, a dong this size needs to be SERVICED and WORSHIPPED!"
p "You've got that right!"
label PamelaBlowDay07b:
scene pamelablow03 with dissolve
play music "Sounds/hardsucking.mp3"
$ renpy.pause(0.3, hard=True)
scene pamelablow04 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow04 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow04 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow04 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow04 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow04 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow04 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelablow04
$ renpy.pause(0.3, hard=True)
scene pamelablow03
$ renpy.pause(0.3, hard=True)
scene pamelablow04
$ renpy.pause(0.3, hard=True)
scene pamelablow03
$ renpy.pause(0.3, hard=True)
scene pamelablow04
$ renpy.pause(0.3, hard=True)
scene pamelablow03
$ renpy.pause(0.3, hard=True)
scene pamelablow04
$ renpy.pause(0.3, hard=True)
scene pamelablow03
$ renpy.pause(0.3, hard=True)
scene pamelablow04
$ renpy.pause(0.3, hard=True)
scene pamelablow03
$ renpy.pause(0.3, hard=True)
scene pamelablow04
$ renpy.pause(0.3, hard=True)
scene pamelablow03
$ renpy.pause(0.3, hard=True)
scene pamelablow04
$ renpy.pause(0.3, hard=True)
scene pamelablow03
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        p "You can blow a pipe so well Pamela, let's do it some more!"
        pa "Years of practice on mega-sized special brews..."
        jump PamelaBlowDay07b
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaFuckChoiceDay07

label PamelaMovieDay07:
scene pamelafuckmovie with dissolve
$ renpy.pause(1.0, hard=True)
p "Yeah, grind your pussy on my shaft and get it nice and wet..."
pa "I'm ready... FUCK ME!"
play music "Sounds/pamelafuckslow.mp3"
show pamfuckslow
show faster
call screen pamfuckslowday07
screen pamfuckslowday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PamelaFuckFastDay07")

label PamelaFuckFastDay07:
stop music
hide faster
play music "Sounds/pamelafuckfast.mp3"
show pamfuckfast
show cum
call screen pamfuckfastday07
screen pamfuckfastday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PamelaCumDay07")

label PamelaCumDay07:
hide pamfuckslow
hide pamfuckfast
stop music
hide cum
scene pamelacum01
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
pa "Shoot your potent seed inside of me [name]!"
p "I am, believe me, I am! RHAAA!"
scene pamelacum02 with dissolve
play sound "Sounds/cumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "Shit, I've got more deliveries to make! UUUGHH, AAAH!"
pa "Damn, you're spraying all over the deck!"
p "Then lie down and I'll plaster your body with the rest of my load!"
scene pamelacum03 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "Fuck, it's blasting non-stop! RHAAA!"
pa "Yes, cover me in your thick spunk [name]!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
pa "Incredible, you totally covered my body on your heavy dose..."
p "Yep, I told you I was a STUD, even better than that boy we saw earlier..."
if (pamelajosewin == False):
    $ pamelawin = True
    p "(José is going to LOATHE me for sending him this pic...)"
else:
    p "(I finally nailed Pamela on the high seas, but too late for her to count towards my tally... sigh)"
$ pamelafucked = True
$ hour += 1
if (vivianefucked == True) and (achievement.has("watersport") == False):
    window hide
    show achievement18:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement18
    $ achievement.grant("watersport")
$ backdoor += 1
if (backdoor >= 12) and (achievement.has("banger") == False):
    window hide
    show achievement19:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement19
    $ achievement.grant("banger")
if (enginerepaired == False):
    pa "I'd better call Mitch so he can come and rescue us..."
    scene pamelasea08 with dissolve
    $ renpy.pause(1.0, hard=True)
    mb "Yo boss! Mitch Bigcannon to the rescue!"
    pa "About time... Get us back on shore, I'm sick and tired of this boring empty ocean..."
    stop music
    scene tower01 with dissolve
    play music "Sounds/oceanwaves.mp3"
    $ renpy.pause(1.0, hard=True)
    pa "Here's your twenty dollars. Even though you hardly deserve them..."
    p "Hey, it's not my fault the engine stopped running!"
    pa "I'll have it fixed tomorrow morning. Hopefully, if you come back to work here, you'll be more productive..."
    $ money += 20
    jump ExploreBeachDay07        

pa "We should head back to the beach... Mitch might get worried and send a party for us..."
scene pamelasea01 with dissolve
play music "Sounds/boatengine.mp3"
$ renpy.pause(1.0, hard=True)
pa "And try to wipe that smirk off your face [name]... I don't want Mitch being jealous and all..."
p "Alright, I'll try..."
stop music
scene tower01 with dissolve
play music "Sounds/oceanwaves.mp3"
$ renpy.pause(1.0, hard=True)
pa "Here's your twenty dollars..."
p "Thanks Pamela, always a pleasure working for you!"
pa "Hopefully, if you come back to work here, you'll be more productive..."
$ money += 20
jump ExploreBeachDay07        

label SandyFuckDay07a:
stop music
play music "Sounds/oceanwaves.mp3"
scene sandybeach01b with dissolve
$ renpy.pause(1.0, hard=True)
sa "Oh, my Prince Charming, what a beautifully romantic place you found, far from the madding crowd!"
menu:
    "Yes, it's the perfect spot for us to get...more intimate..." if (lust_points[19] ==10):
        scene sandybeach02a with dissolve
        sa "And to get back to our natural human state without constraints by being naked...In total communion with Mother Nature."
        jump SandyFuckDay07
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True) and (lust_points[19] >=8) and (lust_points[19] <=9):
        jump SandyPendulumDay07
    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[19] >=8) and (lust_points[19] <=9):
        play sound "Sounds/spray.mp3"
        $ renpy.pause(1.0, hard=True)
        jump SandyPheromoneDay07
    "Leave, I don't have time for hanky-panky right now.":
        scene sandybeach02b with dissolve
        sa "What? Are you f*cking bl**dy kidding me???"
        p "Well, that's not very poetic language if I may say so..."
        p "(I should go back to Pamela, I haven't been paid yet...)"
        jump BeachPamela01Day07

label SandyPheromoneDay07:
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
    jump SandyFuckDay07
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
    jump SandyFuckDay07   

label SandyPendulumDay07:
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
jump ExploreBeachDay07

label SandyFuckDay07:
scene sandyfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
sa "First, my top, so you can admire my large, firm and TOTALLY NATURAL breasts."
p "Yep, entirely believable, especially in a 3D game."
if stamina <= 0 and whitebull == False:
    p "Hang on, before you continue, I have a confession to make. I can't fuck you."
    sa "But why my Prince CHarming?"
    p "I'm the romantic type you know, being a Prince Charming and all that."
    sa "Oh, I understand. You're playing hard to get..."
    p "Yes, another day maybe my Princess?"
    sa "Fine. (sigh)"
    jump ExploreBeachDay07
if stamina <= 0 and whitebull == True:
    p "(This seems like a good time to recharge my batteries and reload my balls with cum by drinking an energy drink...)"
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
        "Bail out":
            p "Hang on, before you continue, I have a confession to make. I can't fuck you."
            sa "But why my Prince Charming?"
            p "I'm the romantic type you know, being a Prince Charming and all that."
            sa "Oh, I understand. You're playing hard to get..."
            p "Yes, another day maybe my Princess?"
            sa "Fine. (sigh)"
            jump ExploreBeachDay07

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
label SandyBlowDay07:
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
        jump SandyBlowDay07
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay07

label SandyFuckChoiceDay07:
menu:
    "Spoon her from the side" if (sandyside == False):
        jump SandySideDay07
    "Stick your cock between her huge jugs" if (sandytits == False):
        jump SandyTitsDay07
    "Take her from behind like a bitch in heat" if (sandydoggy == False):
        jump SandyDoggyDay07
    "Watch her bounce up and down your giant crank" if (sandyside == True) and (sandytits == True) and (sandydoggy == True):
        jump SandyFinalDay07

label SandySideDay07:
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
label SandySideDay07b:
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
        jump SandySideDay07b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay07

label SandyTitsDay07:
$ sandytits = True
scene sandytits01 with dissolve
play sound "Sounds/sandytitfuck01.mp3"
$ renpy.pause(2.0, hard=True)
sa "OOoh, my Prince Charming, my huge tits can't even bury that massive fuckstick, the head is sticking out..."
p "It will be sticking out way more once I do this..."
scene sandytits02 with dissolve
sa "It's so fucking big... Ssooo fucking big..."
label SandyTitsDay07b:
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
        jump SandyTitsDay07b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay07

label SandyDoggyDay07:
$ sandydoggy = True
scene sandydoggy01 with dissolve
$ renpy.pause(1.0, hard=True)
sa "My hole is all yours my Prince! Ram it in as deep as you like!"
p "Sure will do!"
scene sandydoggy01 with dissolve
play sound "Sounds/sandydoggy01.mp3"
$ renpy.pause(3.0, hard=True)
sa "AAAAH, it's so good feeling your giant teenage cock stretching my tiny fuckhole!"
label SandyDoggyDay07b:
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
        jump SandyDoggyDay07b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay07

label SandyFinalDay07:
scene sandybeachkiss with dissolve
play sound "Sounds/sandyslut.mp3"
$ renpy.pause(3.0, hard=True)
sa "I'm going to bounce up and down your shaft and make you feel sssoo good my Prince... You'll pop in no time!"
stop music
play sound "Sounds/oceanwaves.mp3"
play music "Sounds/sandyfuckslow.mp3"
show sandyfuckslow
show faster
call screen sandyfuckslowday07
screen sandyfuckslowday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("SandyFuckFastday07")
label SandyFuckFastday07:
hide faster
play music "Sounds/sandyfuckfast.mp3"
show sandyfuckfast
show cum
call screen sandyfuckfastday07
screen sandyfuckfastday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("SandyFuckCumday07")

label SandyFuckCumday07:
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
jump ExploreBeachDay07

label TowerEndDay07:
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
label TowerEndChoiceDay07:
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
        jump TowerEndChoiceDay07        
    "Go and meet Pamela at the beach bar":
        jump BeachPamela01Day07  
    "Leave":
        jump ExploreBeachDay07       
        
label BeachPamela01Day07:
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
        jump ExploreBeachDay07        
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
        jump ExploreBeachDay07        
    "Talk to Pamela about working some more as a lifeguard":
        scene beachbarpamela02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "Yeah, I guess we could use your help some more. You can come back anytime to work for us..."
        mb "Humpf..."
        jump ExploreBeachDay07
    
label BritPrefuckDay07:
scene brittanyprefuck01b with dissolve
$ renpy.pause(1.0, hard=True)
br "The beach bathroom is clear... It's just you and me now STUD!"
if (stamina <=0) and (whitebull == False):
    p "Ah, but I came here for a piss, nothing more. Wanna watch me urinate?"
    scene britprefuck01a with dissolve
    $ renpy.pause(1.0, hard=True)
    br "WHAT? How dare you think a princess like me would want to watch such a thing! My God, I should have known, you're just a junior WIMP!"
    if (brittanyjosewin == True):
        br "José is a REAL stud, he didn't back out like YOU, LOSER!..."
    br "Don't EVER talk to me again!"
    window hide
    $ lust_points[1] -=2
    $ score -= 2
    show lustminus02:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus02
    p "I guess next time, although there won't be any in this run of the game, I should make sure I can perform for that prissy queen bitch..."
    jump ExploreBeachDay07    
if (stamina <=0) and (whitebull == True):
    p "Now is definitely the time to take some white bull, I can't look like a wimp in front of the school's beauty queen..."
    show whitebull
    show square
    play sound "Sounds/lost.mp3"
    "You gulped down your White Bull energy drink."
    hide square
    hide whitebull
    $ whitebull = False
    $ stamina += 2
if ((seengloryhole03 == True) or (seengloryhole04 == True) or (seengloryhole05 == True) or (seengloryhole06 == True)) and (gloryholetold == True):
    p "Yeah, just like last time when you polished my crank through the gloryhole..."
    br "And it was a MIGHTY piece of boymeat if I recall correctly... Let's see if I can get it as HARD as last time..."
if ((seengloryhole03 == True) or (seengloryhole04 == True) or (seengloryhole05 == True) or (seengloryhole06 == True)) and (gloryholetold == False):
    p "Yeah, just like last time when you polished my crank through the gloryhole..."
    br "Oh, it was you? It was a MIGHTY piece of boymeat if I recall correctly... Let's see if I can get it as HARD as last time..."
label BritFuckday07:
scene brittanyprefuck02b with dissolve
$ renpy.pause(1.0, hard=True)
br "See those perfect tits? That's why I'm the ultimate beauty queen of this island!"
p "Yes, Your Majesty, let me be your unyielding pillar... of lust!"
scene britprefuck03 with dissolve
$ renpy.pause(1.0, hard=True)
br "Now my loyal subject, why don't you come over here and show me what you've got as offering to your Queen?..."
p "Of course Your Magnificent Beautifulness. A Queen like you needs a scepter, and I have just the one for you!"
scene britprefuck04 with dissolve
play sound "Sounds/britprefuck.mp3"
$ renpy.pause(15.0, hard=True)
p "So, what do you think of my offering Your Sublime Hotness?"
br "Oooh, I like it! Show me how to handle it properly my loyal subject!"
label BrittanyFuckChoiceDay07:
menu:
    "Let me lift you up on my scepter!" if (britup == False):
        jump BritUpDay07
    "Let me show you how peasants like me fuck like wild animals!" if (britdoggy == False):
        br "Ooh, that's so dirty!"
        jump BritdoggyDay07
    "Let's get dirty on the floor..." if (britfloor == False):
        br "You are so filthy... I name you Knight of the Scum!"
        p "I'll soon become Knight of the Cum..."        
        jump BritFloorDay07
    "Your royal backside needs a good pounding!" if (britanal == False):
        br "My... Royal backside? No one has ever fucked me there, and your scepter is too big for it!"
        p "Na, it will fit. And anyway, a true beauty queen needs to know how to take it every which way... Get on the floor and expose that royal rump!"
        jump BritAnalDay07
    "Let's fuck sideways. For the viewer that is..." if (britup == True) and (britdoggy == True) and (britfloor == True) and (britanal == True):
        jump BritMovieDay07

label BritUpDay07:
$ britup = True
scene britfuckup04 with dissolve
$ renpy.pause(1.0, hard=True)
p "Get ready for lift-off!"
br "Yes, hold me in your massively-muscled arms my Knight in shining armor!"
scene britfuckup02 with dissolve
$ renpy.pause(1.0, hard=True)
br "OOOH, FUCK! It's so fucking thick and DEEP!"
p "Hang on, I'll drill even deeper!"
label BritUpDay07b:
play sound "Sounds/britup01.mp3"
scene britfuckup01 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup02 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup01 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup02 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup01 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup02 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup01 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup02 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup01 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup02 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup01 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup02 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup01 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup02 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup01 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup02 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup01 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup02 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup01 with dissolve
$ renpy.pause(0.1, hard=True)
scene britfuckup02
$ renpy.pause(0.3, hard=True)
scene britfuckup01
$ renpy.pause(0.3, hard=True)
scene britfuckup02
$ renpy.pause(0.3, hard=True)
scene britfuckup01
$ renpy.pause(0.3, hard=True)
scene britfuckup02
$ renpy.pause(0.3, hard=True)
scene britfuckup01
$ renpy.pause(0.3, hard=True)
scene britfuckup02
$ renpy.pause(0.3, hard=True)
scene britfuckup01
$ renpy.pause(0.3, hard=True)
scene britfuckup02
$ renpy.pause(0.3, hard=True)
scene britfuckup01
$ renpy.pause(0.3, hard=True)
scene britfuckup02
$ renpy.pause(0.3, hard=True)
scene britfuckup01
$ renpy.pause(0.3, hard=True)
scene britfuckup02
$ renpy.pause(0.3, hard=True)
scene britfuckup01
$ renpy.pause(0.3, hard=True)
scene britfuckup02
$ renpy.pause(0.3, hard=True)
scene britfuckup01
$ renpy.pause(0.3, hard=True)
p "And a bit deeper now..."
scene britfuckup05 with dissolve
play sound "Sounds/britup02.mp3"
$ renpy.pause(4.0, hard=True)
br "Oh my dear Lord, it's so fucking DEEP! AAAH!"
p "Yeah, I can feel you creaming down my shaft..."

menu:
    "Repeat":
        p "Let's do it one more time!"
        jump BritUpDay07b
    "Move on":
        p "Time to show you some other uses to my scepter..."
        br "What would you like to do next [name]?"        
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        jump BrittanyFuckChoiceDay07

label BritdoggyDay07:
$ britdoggy = True
scene britdoggy03 with dissolve
play sound "Sounds/britwet.mp3"
$ renpy.pause(6.0, hard=True)
br "Just the tip of your monster cock is already filling me up like never before!"
if (brittanyjosewin == True):
    p "So I'm much bigger than that dickhead José then?"
    br "Oh yes, MUCH bigger! Fuck me hard and deep and prove me you deserve my royal fuckhole more than him!"
label BritdoggyDay07b:
play sound "Sounds/britdoggy02.mp3"
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britdoggy01
$ renpy.pause(0.3, hard=True)
scene britdoggy02
$ renpy.pause(0.3, hard=True)
scene britdoggy01
$ renpy.pause(0.3, hard=True)
scene britdoggy02
$ renpy.pause(0.3, hard=True)
scene britdoggy01
$ renpy.pause(0.3, hard=True)
scene britdoggy02
$ renpy.pause(0.3, hard=True)
scene britdoggy01
$ renpy.pause(0.3, hard=True)
scene britdoggy02
$ renpy.pause(0.3, hard=True)
scene britdoggy01
$ renpy.pause(0.3, hard=True)
scene britdoggy02
$ renpy.pause(0.3, hard=True)
scene britdoggy01
$ renpy.pause(0.3, hard=True)
scene britdoggy02
$ renpy.pause(0.3, hard=True)
scene britdoggy01
$ renpy.pause(0.3, hard=True)
scene britdoggy02
$ renpy.pause(0.3, hard=True)
scene britdoggy01
$ renpy.pause(0.3, hard=True)
scene britdoggy02
$ renpy.pause(0.3, hard=True)
scene britdoggy01
$ renpy.pause(0.3, hard=True)
scene britdoggy02
$ renpy.pause(0.3, hard=True)
stop sound
menu:
    "Repeat":
        p "I need to fill up your royal pussy some more!"
        jump BritdoggyDay07
    "Move on":
        p "Time to show you some other uses to my scepter..."
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What would you like to do next [name]?"        
        jump BrittanyFuckChoiceDay07

label BritFloorDay07:
$ britfloor = True
scene britprefloor01 with dissolve
play sound "Sounds/britfloor01.mp3"
$ renpy.pause(4.0, hard=True)
br "I feel so dirty lying on the floor like that [name]..."
p "Sometimes a Queen has to get closer to her people..."
br "Why don't YOU come closer to me instead of teasing me by waving that monstrous scepter?"
scene britfloor01 with dissolve
$ renpy.pause(1.0, hard=True)
p "As you wish my Queen..."
br "Dang boy, you're plowing into me so deep!"
label BritFloorDay07b:
scene britfloor02 with dissolve
play music "Sounds/britfloor02.mp3"
$ renpy.pause(0.3, hard=True)
scene britfloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britfloor01 with dissolve
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        p "Damn, I'm feeling super-horny melady, I need to fuck you like that some more..."
        jump BritFloorDay07b
    "Move on":
        p "Time to show you some other uses to my scepter..."
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What would you like to do next [name]?"        
        jump BrittanyFuckChoiceDay07

label BritAnalDay07:
$ britanal = True
scene britanal01 with dissolve
$ renpy.pause(1.0, hard=True)
br "Aah, be careful my loyal subject!"
p "Just relax Brittany, open your arse to the people!"
label BritAnalDay07b:
scene britanal02 with dissolve
play music "Sounds/britanal.mp3"
$ renpy.pause(0.3, hard=True)
scene britanal03 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal03 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal03 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal03 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal03 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal03 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene britanal03
$ renpy.pause(0.3, hard=True)
scene britanal02
$ renpy.pause(0.3, hard=True)
scene britanal03
$ renpy.pause(0.3, hard=True)
scene britanal02
$ renpy.pause(0.3, hard=True)
scene britanal03
$ renpy.pause(0.3, hard=True)
scene britanal02
$ renpy.pause(0.3, hard=True)
scene britanal03
$ renpy.pause(0.3, hard=True)
scene britanal02
$ renpy.pause(0.3, hard=True)
scene britanal03
$ renpy.pause(0.3, hard=True)
scene britanal02
$ renpy.pause(0.3, hard=True)
scene britanal03
$ renpy.pause(0.3, hard=True)
scene britanal02
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        p "I like fucking your royal rectum, let's do it again!"
        jump BritAnalDay07b
    "Move on":
        p "Time to show you some other uses to my scepter..."
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What would you like to do next [name]?"        
        jump BrittanyFuckChoiceDay07

label BritMovieDay07:
scene britfuckpremovie with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready your Sumptuous Highness?"
br "I'm ready... FUCK ME!"
play music "Sounds/britfuckmovie.mp3"
show britfuckmovie
show cum
call screen britfuckmovieday07
screen britfuckmovieday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("BritCumDay07")

label BritCumDay07:
hide britfuckmovie
stop music
hide cum
scene britcum01
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "Let me plaster your royal back in my commoner's spunk!"
scene britcum02 with dissolve
play sound "Sounds/cumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "Shit, I've got more deliveries to make! UUUGHH, AAAH!"
br "You're ruining my skin ointment!"
p "My cream is better, it's 100\%\ natural!"
scene britcum03 with dissolve
play sound "Sounds/britcum.mp3" 
$ renpy.pause(1.0, hard=True)
p "I gave you the last of my cream your Exquisite Sublimeness!"
if (brittanyjosewin == True):
    br "Thank you [name], your offering was by far superior to José's weak attempt the other day!"
    p "Fuck yeah! That's cos I'm DA MAN and he's just a loser wimp!"
if (brittanyjosewin == False):
    br "Oh my God, it's such a BIG load!"        
    p "Fuck yeah! I'm da man, I'm DA MAN!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
br "So how does it feel having fucked the most beautiful girl on the island [name]?"
p "I feel like the King of the World!"
br "It doesn't work that way. I'm the Queen and you're NOTHING. Now leave me to pamper myself and DON'T TELL ANYONE!"
p "But... Surely, I deserve something in return for my loyal servicing of your royal fuckholes?!"
br "You are hereby knighted and allowed to service my royal holes at my leisure... Now shoo!"
p "Oh thank you so much your Magnanimous Kindness (snickers)..."
if (brittanyjosewin == False):
    $ brittanywin = True
    p "(Oh, I can't wait to imagine José's shocked face when I send him a pic of his supposed girlfriend covered in my thick spunk...)"
else:
    p "(I fucked the school's beauty queen, but too late for her to count towards my tally... sigh)"
if (chantellefucked == True) and (katefucked == True) and (achievement.has("grabber") == False):
    p "Yeah! I've scored with all the teen beauty pageants... That should make me a..."
    window hide
    show achievement16:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement16
    $ achievement.grant("grabber")
$ brittanyfucked = True
$ hour += 1
$ backdoor += 1
if (backdoor >= 12) and (achievement.has("banger") == False):
    window hide
    show achievement19:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement19
    $ achievement.grant("banger")    
jump ExploreBeachDay07

label DowntownDay07:
stop music
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"
$ renpy.pause(1.0, hard=True)
p "The bus left me right in front of the main downtown plaza."
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_104
    $ lustaddedB = 1
    call Challenger from _call_Challenger_105
    $ lustaddedB = 1
    call Challenger from _call_Challenger_106
    $ challengercalls += 2

if hour == 12 or hour == 13 and atelunchday07 == False:
    p "I'd better take a break and eat that sandwich mom prepared for me, I'm hungry... Let's eat here, in the middle of the polluted air."
    scene downtownbackground
    show mceating
    with dissolve
    $ renpy.pause(1.0, hard=True)
    p "What are you looking at? You never saw a guy eat a sandwich?"
    $ hour += 1
    $ atelunchday07 = True
    hide mceating
    show mcate
    with dissolve
    p "Ah, now I'm not hungry anymore. Amazing what eating does to your body. Let's move on then..."

if (hour >= 19):
    p "It's getting late, I should really take the bus and get home."
    $ bushome = True
    jump BusDowntownHomeDay07
else:
    jump DowntownChoiceDay07b

label BusDowntownHomeDay07:
p "Ah, here's the bus heading to the Burbs, I'd better take it..."
$ bushome = True
jump BusDriveDay07

label DowntownChoiceDay07b:
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"
if hour == 12 or hour == 13 and atelunchday07 == False:
    p "I'd better take a break and eat that sandwich mom prepared for me, I'm hungry... Let's eat here, in the middle of the polluted air."
    scene downtownbackground
    show mceating
    with dissolve
    $ renpy.pause(1.0, hard=True)
    p "What are you looking at? You never saw a guy eat a sandwich?"
    $ hour += 1
    $ atelunchday07 = True
    hide mceating
    show mcate
    with dissolve
    p "Ah, now I'm not hungry anymore. Amazing what eating does to your body. Let's move on then..."

if (hour >= 19):
    p "It's getting late, I should really take the bus and get home."
    jump BusDowntownHomeDay07

p "Where should I go?"
menu:
    "Go shopping":
        jump ShopDay07
    "Go to the massage parlour" if (discovermassage == True) and (parlourseen07 == False):
        jump Parlour01Day07
    "Take the bus home":
        $ bushome = True
        jump BusDowntownHomeDay07
    "Take the bus to the beach" if (hour <= 17):
        $ busbeach = True
        jump BusDowntownBeachDay07
    "Go to the downtown gym" if (discovergym == True):
        jump Gym01Day07
    "Go to Old Joe's Emporium" if (discoveremporium == True):
        jump PawnShop01Day07
    "Go to the main plaza" if (discoverplaza == True) and (redpill <= 1) and (bluepill <=1) and studwin == False and studlose == False:
        jump PlazaDay07

label PlazaDay07:
scene dealer01 with dissolve
$ renpy.pause(1.0, hard=True)
menu:
    "Approach the dodgy guy":
        jump DrugDay07
    "Leave":
        jump DowntownChoiceDay07b
   
label DrugDay07:
if (redpill == 1) or (bluepill == 1):
    jump DrugDay07b

label DrugDay07a:
mx "Hola gringo! You looka for soma-fingo?"
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
    jump DowntownChoiceDay07b    
call screen drugday07
stop music
"You were too slow and the drug dealer leaves in a hurry."
scene dealer03 with dissolve
$ renpy.pause(1.0, hard=True)
mx "I gotta go. The copos are on me...."
p "Oh well, it was probably some dodgy shit anyways. Drugs are bad, m'kay?"
play music "Sounds/downtown.mp3"
jump DowntownChoiceDay07b

label DrugRedDay07:
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
jump DowntownChoiceDay07b

label DrugBlueDay07:
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
jump DowntownChoiceDay07b

label DrugDay07b:
mx "Wassup gringo?"
p "'Ello. I wish to register a complaint."
mx "We're closing for lunch."
p "Never mind that, my lad. I wish to complain about these pills what I purchased not a day ago from this very boutique."
if (redpill == 1):
    mx "Oh yes, the, uh, the Mérican Red...Qué, uh... What's wrong with it?"
if (bluepill == 1):
    mx "Oh yes, the, uh, the Mérican Blue...Qué, uh... What's wrong with it?"
p "I'll tell you what's wrong with it, my lad. It makes people sick, that's what's wrong with it!"
mx "No, no, it's... a resting pill."
p "Look, matey, I know a rotten pill when I see one, and I'm looking at one right now."
mx "No no! it's a pining pill!"
p "It's NOT a pining pill. It's a rotten pill. This pill is no more! It has ceased to be! It's expired and gone to meet its maker! It's pushing up the daisies!"
p "Its metabolic processes are now history! It's kicked the bucket, it's shuffled off its mortal coil, run down the curtain and joined the bleedin' choir invisible!! THIS IS AN EX-PILL!!"
window hide
$ renpy.pause(1.0, hard=True)
mx "Well, I'd better replace it, then. But it will cost you gringo."
p "What? This is outrageous!"
if (redpill == 1):
    mx "Tell you qué gringo. I'll give you a blue pill instead for only cinco dollares..."
if (bluepill == 1):
    mx "Tell you qué gringo. I'll give you a red pill instead for only cinco dollares..."
menu:
    "Deal!" if (money >= 5):
        if (redpill == 1):
            $ bluegood = True
            show bluepills
            show square
            play sound "Sounds/found.mp3"
            "You acquired a blue pill. With unknown effects..."
            $ bluepill = 1
            hide bluepills
            hide square
            $ money -= 5
            jump DrugEndDay07b
        if (bluepill == 1):
            $ redgood = True
            show redpills
            show square
            play sound "Sounds/found.mp3"
            "You acquired a red pill. With unknown effects..."
            $ redpill = 1
            hide redpills
            hide square
            $ money -= 5
            jump DrugEndDay07b
    "No deal, this is a rip-off!":
        scene dealer03 with dissolve
        $ renpy.pause(1.0, hard=True)
        mx "Hasta la vista, I gotta go."
        $ hour += 1
        jump DowntownChoiceDay07b
        
label DrugEndDay07b:
mx "Nice doing business with you gringo!"
scene dealer03 with dissolve
$ renpy.pause(1.0, hard=True)
mx "Hasta la vista, I gotta go."
$ hour += 1
jump DowntownChoiceDay07b

label BusDowntownBeachDay07:
p "Ah, here's the bus heading for the beach, I'd better take it..."
jump BusDriveDay07

label PawnShop01Day07:
scene emporium01 with dissolve
$ renpy.pause(1.0, hard=True)
oj "Hello young man. Welcome to Old Joe's Emporium. We buy and sell all sorts of wares."
label PawnShop01Day07b:
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
                jump DowntownChoiceDay07b
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
                        jump DowntownChoiceDay07b
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
                                jump DowntownChoiceDay07b
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
                                jump DowntownChoiceDay07b
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
                        jump DowntownChoiceDay07b
    "What's this place?":
        oj "I just told you boy, are you deaf?"
        jump PawnShop01Day07b
    "Leave":
        jump DowntownChoiceDay07b

label Parlour01Day07:
scene parlour01
$ parlourseen07 = True
$ renpy.pause(1.0, hard=True)
play music "Sounds/parlourmusic.mp3"
ka "Welcome big American boy to \"Misohawny Massage Parlour\"! Me Katsumi, you want massage?"
menu:
    "I was told you did \"full-body massage\"...":
        ka "Yes, sucky sucky 50 dolla."
        p "Ah, I see. Sucky sucky indeed. That's quite expensive for just sucky sucky."
        ka "Me love you long time. For you, more than sucky sucky."
        p "Oh, the conversations we could have my dear..."
        jump ParlourChoiceDay07
    "Yes, how much is it?":
        ka "Normal massage? 10 dolla. More massage, 50 dolla."
        p "And what do I get for 50 dollars exactly?"
        ka "Sucky sucky 50 dolla."
        p "That's a lot of inflation since the Vietnam War..."
        jump ParlourChoiceDay07
    "Nope, not interested...":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceDay07b

label ParlourChoiceDay07:
menu:
    "Get a normal massage (10 $)" if (money >=10):
        jump NormalMassageDay07
    "Choose the \"full-body massage\" experience... (50 $)" if (money >=50) and (stamina >=1):
        jump FullMassageDay07
    "Mmh...I don't seem to have enough money at the moment." if (money <=9):
        ka "You poor. Hah hah. Me not poor. Come back when you not poor."
        p "I certainly will, if just for the highly stimulating conversations."
        jump DowntownChoiceDay07b
    "Mmh, I don't seem to have enough stamina at the moment." if(stamina == 0):
        ka "Ah! You not man enough. You leave and come back when you can cum."
        jump DowntownChoiceDay07b
    "Actually, I don't want anything right now.":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceDay07b

label NormalMassageDay07:
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
                jump Parlour05Day07
            "Forget it. Just give me a normal massage.":
                ka katsumi "Ok, me gonna massage your cock because ssooo BIG."
                jump Parlour05Day07
    "OK, OK, I'll pay the difference for a sucky sucky..." if (money >=40) and (stamina >=1):
        $ suckysucky = True
        $ fuckyfucky = True
        $ money -= 40
        jump Parlour05Day07
    "Why don't you just massage it then like if it was one of my big tense muscles?...":
        ka "Oooh, boy very smart. OK, me gonna massage big American cock. But no sucky sucky, you not pay."
        jump Parlour05Day07

label FullMassageDay07:
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
        jump Parlour05Day07        
    "That's cos all Asian men have small penises.":
        ka "Not true. Some Asian men big penis. You like Trump, you racist."
        ka "Me only do sucky sucky. No fucky fucky. Because you bad boy."
        $ fuckyfucky = False
        jump Parlour05Day07

label Parlour05Day07:
scene parlour05 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Big American monster boycock so big and hard!"
p "Yeah, play with it Katsumi! It's all yours!"

label Parlour06Day07:
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
                jump Parlour07Day07
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
                jump DowntownChoiceDay07b
    
label Parlour07Day07:  
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

label Parlour08Day07:  
scene parlour08 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Reaching top of monstercock take me so long... Me love you long time!"
p "Keep going, you still have quite a few inches to go..."

label Parlour09Day07:  
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
                jump DowntownChoiceDay07b

label Parlour10Day07:  
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
        
label ParlourFuckDay07:
stop music
play music "Sounds/katsumifuck.mp3"
show movieparlourfuck
show cum
call screen parlourfuckcumday07
screen parlourfuckcumday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("ParlourCumDay07")

label ParlourCumDay07:
stop music
hide movieparlourfuck
scene parlourcum01
stop music
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
ka "You filling me up with so much boyjuice! You so incredible!"

label ParlourCum02Day07:
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
jump DowntownChoiceDay07b

label ShopDay07:
if (evictedfromshop == True):
    "You are banned from entering this boutique until tomorrow. Bad boy. VERY bad boy."
    jump DowntownChoiceDay07b
if (shoppingseen07 == True):
    "You already went shopping today. Looks like you might be a shopaholic..."
    jump DowntownChoiceDay07b
if (shoppingseen04 == True):
    jump Shop01Day07
if (shoppingseen04 == False) and (altshop == False):
    jump ShopAltDay07
if (shoppingseen04 == False) and (altshop == True):
    $ altshop07 = True
    jump Shop01Day07

label ShopAltDay07:
$ shoppingseen07 = True
$ altshop07 = True
stop music
scene shopday04 with dissolve
play music "Sounds/shopmusic.mp3"
$ renpy.pause(1.0, hard=True)
p "This boutique looks very expensive..."
p "There's a nice-looking clerk standing behind the counter and several customers looking at skimpy swimsuits...The shop seems to be very busy today..."

label Shop01AltDay07b:
scene shopday04 with dissolve
menu:
    "Go talk to the clerk":
        jump ShopClerkDay07
    "Go talk to the black girl on the left":
        jump ShopCustomerDay07
    "Go talk to the redhead in the middle":
        jump ShopCustomerRedDay07
    "Go talk to the blonde on the right":
        jump ShopCustomerBlondeDay07
    "Go to the changing rooms" if (foundcabins == True) and (rightcabinseen06 == False) and (rightcabinseen07 == False):
        jump ShopCabinChoiceAltDay07
    "Leave":
        stop music
        jump DowntownChoiceDay07b    

label Shop01Day07:
$ shoppingseen07 = True
stop music
scene shop with dissolve
play music "Sounds/shopmusic.mp3"
$ renpy.pause(1.0, hard=True)
p "This boutique looks very expensive..."
p "There's a nice-looking clerk standing behind the counter and one customer looking at a skimpy swimsuit..."

label Shop01Day07b:
scene shop with dissolve
menu:
    "Go talk to the clerk":
        jump ShopClerkDay07
    "Go talk to the customer":
        jump ShopCustomerDay07
    "Go to the changing rooms" if (foundcabins == True):
        jump ShopCabinChoiceDay07
    "Leave":
        stop music
        jump DowntownChoiceDay07b

label ShopCustomerRedDay07:
scene shopred01 with dissolve
$ renpy.pause(1.0, hard=True)
re "Oh, you're a man, give me your advice. Should I choose the red or the green bikini?"
menu:
    "The red bikini, it will match your hair.":
        re "Yes, you're right, thank you!"
        jump Shop01AltDay07b    
    "The green bikini, it will match your eyes.":
        re "Yes, you're right, thank you!"
        jump Shop01AltDay07b
    "Imagine her naked":
        scene shopred01b with dissolve
        play sound "Sounds/dreaming.mp3"
        $ renpy.pause(2.0, hard=True)
        re "Err... Hello? Are you ogling my breasts? What a pervert!"
        sc "Stop disturbing the customers! This is a respectable establishment. I must ask you to leave at once!"
        $ evictedfromshop = True
        jump DowntownChoiceDay07b

label ShopCustomerBlondeDay07:
scene shopblonde01 with dissolve
$ renpy.pause(1.0, hard=True)
bl "Can't you see I'm busy thinking? There's too many new bikinis to choose from in this store!"
sc "Stop disturbing the customers!"
jump Shop01AltDay07b

label ShopClerkDay07:
scene shop01 with dissolve
sc "How may I help you?"
menu:
    "Talk to her":
        jump ShopTalkDay07
    "Buy something":
        jump ShopBuyDay07  
    "Leave the counter":
        if (altshop07 == True):
            jump Shop01AltDay07b
        jump Shop01Day07b

label ShopTalkDay07:
menu:
    "You know what would look good on you? Me.":
        scene shop03
        sc "Mmh, lemme think... Yes, it's the worst pick-up line ever."
        jump ShopClerkDay07
    "What's the word on the street downtown?":
        if (downtowntipgiven == True):
            sc "I already gave you a tip today. Stop pestering me."
            jump ShopClerkDay07
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
            jump ShopClerkDay07
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
            jump ShopClerkDay07
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
            jump ShopClerkDay07
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
            jump ShopClerkDay07
        if (downtowntips >= 4):
            sc "It's the weekend, I'm out of tips."
            jump ShopClerkDay07        
    "What's going on today? It seems unusually busy..." if (altshop07 == True):
        sc "We have just received the new summer line of \"Audacious Bikinis\". People are going crazy for them."
        sc "We've also received the new \"Mega-sized Audacious Briefs for Boys\". But not many people seem interested in them unfortunately..."
        p "Err... I might be interested, I want to try one."
        sc "Oh great!, you can pick one from the shelf for your size and try it in one of the changing rooms, if you can find one that's empty..."
        $ foundcabins = True
        jump ShopClerkDay07
        
label ShopBuyDay07:
menu:
    "Buy swimsuit for customer (40$ - pay 20$ from your own pocket)" if (money >= 20) and (seenhallebikini == True) and (boughthallebikini == False):
        scene shop02
        play sound "Sounds/cashregister.wav"
        sc "Here you are. That's for one lucky girl!"        
        $ money -= 20
        $ boughthallebikini = True
        jump HalleGiftDay07

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
        jump ShopClerkDay07

    "Nothing actually":
        jump ShopClerkDay07

    "I don't have enough money to buy anything here." if (money <=9):
        sc "We don't do credit. We don't trust poor people like you."
        p "I feel like... dirt..."
        jump ShopClerkDay07

label ShopCustomerDay07:
scene halleshop01 with dissolve
$ renpy.pause(1.0, hard=True)
if (boughthallebikini == True) and (seenhallebikini == True):
    p "Hey, Halle, why are you still here? I bought you this swimsuit already!"
    show halleshop01b
    ha "Yeah, I know, but the dev is too lazy to remove me from this image..."
    ha "Remember, I'm ACTUALLY at the beach."
    jump Shop01Day07
elif (boughthallebikini == False) and (seenhallebikini == True):
    p "You're still staring at this swimsuit..."
    show halleshop01b
    ha "And I'll keep staring at it until you chip in 20 bucks to buy it for me!"
    if (altshop07 == True):
        jump Shop01AltDay07b
    jump Shop01Day07b

else:
    menu:
        "May I help you with anything miss? Would you like to try this item in one of our cabins?":
            show halleshop01b
            ha "Oh...hum.. Sorry, I didn't realize you worked here... Well, I don't know, it's quite expensive..."
            p "Well, try it on, that's free anyway..."
            ha "Yeah, I guess you're right, I might as well try it on..."
            $ pretendshop = True
            jump HalleChangeDay07
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
                    jump HalleChangeDay07
                "That's too bad, cos I'm sure you would be a hit with that thing on...":
                    ha "(sigh)... Yes, it's too bad..."
                    if (altshop07 == True):
                        jump Shop01AltDay07b
                    jump Shop01Day07b

label HalleChangeDay07:
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
            jump DowntownChoiceDay07b
        "Wait for her to come out":
            jump HalleBikini01Day07
else:
    ha "Hang on a minute, I'm almost ready..."

label HalleBikini01Day07:
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
        jump HalleBikini02Day07
    "Yeah, really hot... Turn around now...":
        ha "Like...that?"
        jump HalleBikini02Day07

label HalleBikini02Day07:
    scene hallebikini02 with dissolve
$ renpy.pause(1.0, hard=True)
if (pretendshop == True):
    p "Yes, that is a definitive perfect fit..."
    ha "Would...you..consider giving me a discount? I'm twenty bucks short to buy it and I really need a new bikini to go to the beach!"
    "The bikini is marked at 40 dollars..."
    menu:
        "Sure, for a girl like you, half-price! Give it to me and I'll make all the arrangements" if (money >= 20):
            ha "Oh, thank you sssoo much. My name is Halle by the way and I'll be wearing this at the beach if you ever fancy joining me (wink)!"
            if (altshop07 == True):
                jump Shop01AltDay07b
            jump Shop01Day07b
        "Mmh, you'll have to show me more to get such a discount price miss...":
            jump HalleTopOffDay07
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
            if (altshop07 == True):
                jump Shop01AltDay07b
            jump Shop01Day07b

else:
    p "Wow, you look really hot...err..."
    ha "The name's Halle. So, since you like it so much, time to chip in 20 bucks like you promised so I can buy it!"
    menu:
        "Ah... About that.. I just realized I don't have enough money." if (money <= 19):
            ha "But..You promised me!"
            p "OK, OK, as soon as I get the money, I'll come back I swear!"
            ha "I'll be here every afternoon, lamenting as to why I can't own this lovely bikini!"
            "Well at least, I know where to find her..."
            if (altshop07 == True):
                jump Shop01AltDay07b
            jump Shop01Day07b
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
            if (altshop07 == True):
                jump Shop01AltDay07b
            jump Shop01Day07b
        "Well, sure...sure... But a little incentive wouldn't hurt... If you know what I mean...":
            ha "I know what you mean...You boys are all the same..."
            jump HalleTopOffDay07
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
            jump ShopClerkDay07
            
label HalleTopOffDay07:
scene halletopoff with dissolve
$ renpy.pause(1.0, hard=True)  
ha "So... Now that you've seen my big sumptuous tits... Time to cough up the money!"
p "Let me regain my breath first... WOW! I'll pay the difference for you baby!"
jump ShopClerkDay07

label HalleGiftDay07:
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
if (altshop07 == True):
    jump Shop01AltDay07b
jump Shop01Day07b

label ShopCabinChoiceDay07:
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
if (chiyofucked == False) and (rightcabinseen == True):
    p "Now let's see, I hope Chiyo is here again... I haven't fucked her yet."
    jump NewChiyoDay07
if (chiyofucked == False) and (rightcabinseen == False):
    jump ShopCabinChoiceAltDay07
if (chiyofucked == True):
    p "I guess I've already fucked Chiyo, no need to waste my time checking the right cabin, let's open the door on the left."
    jump RandyRed01Day07
    
label RandyRed01Day07:
$ randyredseen07 = True
scene randyred01 with dissolve
play sound "Sounds/dooropen.mp3"
$ renpy.pause(1.0, hard=True)
p "Not AGAIN! That redhead boy with the giant cock is about to bang YET ANOTHER HOT CHICK!"
menu:
    "I've had enough of this nonsense, I'm outta here":
        jump Shop01Day07b
    "Continue watching, I'll get an extra peeper point at least... (+1 hr)":
        jump RandyRed02Day07

label RandyRed02Day07:
scene randyred02 with dissolve
$ renpy.pause(1.0, hard=True)
rb "Oh, it's YOU again. Can't get enough of watching me bang some hot chicks hey?"
p "Well... err. Just shut up and carry on."
rb "I didn't plan to stop buddy..."
scene randyred03 with dissolve
$ renpy.pause(1.0, hard=True)
rb "See how she can barely manage more than five inches of my monster?"
p "I have the same problem, but with more inches sticking OUT!"
rb "Whatever you say man."
p "DA MAN to be more precise."
rb "We'll see about that tomorrow at the Muscle Stud Competition. Now watch and learn..."
scene randyred02 with dissolve
play sound "Sounds/hardsucking.mp3"
$ renpy.pause(0.3, hard=True)
scene randyred03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred02 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred02 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred02 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred02 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred03 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred02 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred03 with dissolve
$ renpy.pause(0.3, hard=True)
re "Mon Dieu! Your cock is sssooo THICK and HUGE! Baise-moi tout de suite!"
scene randyred04 with dissolve
$ renpy.pause(1.0, hard=True)
rb "Her talking French to me while I ram my pole up her tight pussy is getting me so HARD man!"
scene randyred05 with dissolve
$ renpy.pause(1.0, hard=True)
play music "Sounds/planefuck.mp3"
re "Oh OUI! C'est si BON! Fuck me please, fuck me HARD!"
scene randyred04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred05 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred05 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred05 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred05 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred05 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred05 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred04 with dissolve
$ renpy.pause(0.3, hard=True)
scene randyred05 with dissolve
$ renpy.pause(0.3, hard=True)
rb "And now for the cumming all over the place part!"
stop music
scene randyred05b with dissolve
play sound "Sounds/imcumming.mp3"
play sound "Sounds/randybeachchickmoaning.mp3"
$ renpy.pause(1.0, hard=True)
rb "First I'll fill her pussy up with a quart of spunk..."
scene randyred06 with dissolve
play sound "Sounds/imcumming02.mp3"
$ renpy.pause(1.0, hard=True)
rb "Then I cover her face and tits in huge cum blasts..."
re "OUI! You're cumming ssoo much! J'ADORE!"
$ hour += 1
$ peeping += 1
if (peeping >= 8) and (achievement.has("peeper") == False):
    show achievement15:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement15
    $ achievement.grant("peeper")
    rb "See, it was worth it. You finally achieved something..."
p "You don't impress me! Prepare to lose your crown tomorrow!"
rb "Ignorance is bliss. Now if you'll excuse us, I still have a raging hardon and gallons of cum to unload..."
jump Shop01Day07b


label NewChiyoDay07:
stop music
play sound "Sounds/dooropen.mp3"
$ renpy.pause(1.0, hard=True)
scene chiyo01day05 with dissolve
$ rightcabinseen07 = True
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
    if (lust_points[3] == 9):
        $ lust_points[3] += 1
        $ score += 1
        show lust01:
            xalign 0.8 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
    if (lust_points[3] <= 8):
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
        jump ChiyoNewFuckREALDay07
    if (lust_points[3] >= 8) and (((pendulumactive == True) and (pendulum == True)) or (pheromone == True)):
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
                jump ChiyoPendulumDay07           
            "Spray yourself with pheromones" if (pheromone == True):
                window hide
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump ChiyoPheromoneDay07
            "Don't use anything":
                jump ChiyoNoFuckDay07
    else:
        jump ChiyoNoFuckDay07
    
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
    jump DowntownChoiceDay07b

label ShopCabinChoiceAltDay07:
stop music
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
label ShopCabinChoiceDay07b:
p "Mmh, which cabin should I choose?"
menu:
    "The cabin on the left" if (leftcabinseen05 == False):
        jump ShopCabin01Day07
    "The cabin in the middle":
        jump ShopCabin02Day07
    "The cabin on the right" if (rightcabinseen05 == False):
        jump ShopCabin03Day07
    "Leave":
        scene shop01 with dissolve
        sc "So, did they fit you big boy? Are you ready to buy a pair?"
        p "Err... No, they're soiled actually, don't know how it happened really..."
        scene shop04 with dissolve
        sc "What? You're soiling my products? Get out of my shop immediately!"
        $ evictedfromshop = True
        jump DowntownChoiceDay07b

label ShopCabin01Day07:
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
        jump ShopCabinChoiceDay07b
    "Ok, why not, I'm bored anyway. (50\%\ chance of +1 stamina)":
        rc "First, I'll get my pussy wet to take my boyfriend's behemoth! I'ts important since he's so gigantic..."
        rb "Watch this buddy. I'm gonna pound her sweet pussy till she's begging for me to stop!"
        jump RandyShop02Day07
        
label RandyShop02Day07:
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
jump ShopCabinChoiceDay07b

label ShopCabin02Day07:
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
jump ShopCabinChoiceDay07b

label ShopCabin03Day07:
stop music
play sound "Sounds/dooropen.mp3"
scene shopcabin03 with dissolve
$ rightcabinseen05 = True
label ShopCabin03Day07b:
cy "How rude, I'm all naked and you barge in here just as I was about to put on this bikini..."
p "Sorry but all the stalls are taken and I wanted to try on these new mega-sized briefs."
cy "Mega-sized briefs? Well maybe I could make some room for you in here then... But no touching naughty boy..."
cy "But first, let me put on this bikini..."
scene shopcabin03b with dissolve
$ renpy.pause(1.0, hard=True)
cy "What do you think? Will you be having problems putting on your briefs over that hardening rod, hee hee..."
menu:
    "I'll...try anyway if you don't mind...":
        jump ShopCabin03bDay07
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
        jump ShopCabinChoiceDay07b

label ShopCabin03bDay07:
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
        jump ChiyoFuck01Day07
    if (lust_points[3] >= 8) and (((pendulumactive == True) and (pendulum == True)) or (pheromone == True)):
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
                jump ChiyoPendulumDay07           
            "Spray yourself with pheromones" if (pheromone == True):
                window hide
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump ChiyoPheromoneDay07
            "Don't use anything":
                jump ChiyoFuck01Day07
    if (lust_points[3] <= 7):
        jump ChiyoFuck01Day07
    
if (dildo == False):
    p "I don't have a dildo, I have a REAL cock."
    cy "Too bad then that you don't have one.... I was really horny... But I'm not anymore, you spoilt the mood. Shoot little boy. Hee hee."
    p "What? But you can't leave me in such a state!"
    cy "Of course I can. You shouldn't be in the same stall as me anyway. The woman in the stall next door is horny, you can get that fat cock serviced by her."
    p "AAARGH!"
    play sound "Sounds/doorclosing.mp3"
    scene shopcabin01 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump ShopCabinChoiceAltDay07
            
label ChiyoPendulumDay07:
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
    if (altshop07 == True):
        jump ChiyoFuck01Day07
    jump ChiyoNewFuckREALDay07
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
    if (altshop07 == True):
        jump ChiyoFuck01Day07
    jump ChiyoNewFuckREALDay07

label ChiyoPheromoneDay07:
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
    jump ChiyoFuck01Day07
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
    if (altshop07 == True):
        jump ChiyoFuck01Day07
    jump ChiyoNewFuckREALDay07

label ChiyoFuck01Day07:
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
label ChiyoFuckALTDay07:
scene chiyofuck02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Come on, enough of that, I've got the real thing right here!"

label ChiyoNewFuckREALDay07:
if (lust_points[3] == 10):
    cy "Mmh, I know and it DOES look tasty... What would you want to do with it naughty naughty boy?"
    menu:
        "If it looks tasty, then give me a blowjob!":
            jump ChiyoBlowjobDay07
        "Your pussy looks tasty... And ready for a good pounding!":
            jump ChiyoPussyDay07

cy "I think you've seen enough naughtiness for the day. I came here to buy a bikini, not to get fucked by some random horse-hung boy. So you can leave now..."
p "AAARGH! She's doing it to me again!"
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
jump ShopCabinChoiceAltDay07
            
label ChiyoBlowjobDay07:
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
label ChiyoBlowjobDay07b:
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
        jump ChiyoBlowjobDay07b
    "Your pussy looks tasty... And ready for a good pounding!" if (chiyopussy == False):
         jump ChiyoPussyDay07
    "It's time to stretch that gaping anus even more than that puny dildo you used!" if (chiyoblowjob == True) and (chiyopussy == True):
        jump ChiyoArseDay07

label ChiyoPussyDay07:
scene chiyopussy01 with dissolve
play sound "Sounds/chiyopussy01.mp3"
$ renpy.pause(7.0, hard=True)
p "That's nothing, I'm not even half-way in!"
scene chiyopussy02 with dissolve
play sound "Sounds/chiyopussy02.mp3"
$ renpy.pause(11.0, hard=True)
cy "Oh my God, you're so deep!"
label ChiyoPussyDay07b:
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
        jump ChiyoPussyDay07b
    "If it looks tasty, then give me a blowjob!" if (chiyoblowjob == False):
        jump ChiyoBlowjobDay07
    "It's time to stretch that gaping anus even more than that puny dildo you used!" if (chiyoblowjob == True) and (chiyopussy == True):
        jump ChiyoArseDay07

label ChiyoArseDay07:
scene chiyoarse01 with dissolve
$ renpy.pause(0.3, hard=True)
cy "I'm ready to have my little arsehole stretched by your naughty prick!"
scene
play music "Sounds/chiyofuckslow.mp3"
play movie "Day4/chiyofuckslow.ogv" loop
show movie
show faster
call screen chiyofuckslow07
screen chiyofuckslow07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("ChiyoFuckFastDay07")
label ChiyoFuckFastDay07:
hide faster
play music "Sounds/chiyofuckfast.mp3"
play movie "Day4/chiyofuckfast.ogv" loop
show cum
call screen chiyofuckfast07
screen chiyofuckfast07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("ChiyoFuckCumDay07")

label ChiyoFuckCumDay07:
stop movie
stop music
scene chiyocum01 with dissolve
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
if (backdoor >= 12) and (achievement.has("banger") == False):
    window hide
    show achievement19:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement19
    $ achievement.grant("banger")
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
jump DowntownChoiceDay07b

label ChiyoNoFuckDay07:
cy "Looks like you won't be getting any Asian poontang from me today... Now shoot little boy, hee hee..."
p "Damn lustmeter! AARGH!"
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
if (altshop07 == True):
    jump ShopCabinChoiceDay07b
if (altshop07 == False):
    scene shopcabin01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "I might as well check the door on the left then while I'm here..."
    scene redcabin02 with dissolve
    $ renpy.pause(1.0, hard=True)    
    re "Oui?"
    p "Oui! OUI!"
    re "And NON. Get out of here or I'm calling the police!"
    p "Alright, alright. I guess there's a reason she's not on the list of 24 in-game girls..."
    jump DowntownChoiceDay07b
  
label Gym01Day07:
$ seengym07 = True
stop music
scene gym01 with dissolve
play music "Sounds/gymreception.mp3"
$ renpy.pause(1.0, hard=True)
if enteredcompetition:
    jump GymSaturday07a
if (wenttogymday03 == True):
    $ daysgymseen += 1
if (seengym04 == True):
    $ daysgymseen += 1
if (seengym05 == True):
    $ daysgymseen += 1
if (seengym06 == True):
    $ daysgymseen += 1
if (daysgymseen == 0):
    jump GymFirstDay07
if (daysgymseen == 1):
    jump GymSecondDay07
if (daysgymseen >= 2):
    jump GymSaturday07a

label GymFirstDay07:
da "Welcome to \"Jerk n' Clean Fitness Club \". My name is Daniella, how may I help you?"
label Gym01bDay07:
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
                jump Gym03Day07
            "Mmh, I'll think about it.":
                jump Gym01bDay07
    "I'm a member already. A LONG-STANDING \"member\" if you catch my drift...":
        show gym02 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "I tried to catch it but then it flew away..."
        jump Gym01bDay07
    "Why should I pay to join your gym when there are free gyms around the island?":
        da "Because our gym has the best equipment you can find on the island, that's why."
        p "I'm not convinced. You need to prove it."
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Alright Mr-Big-Shot. Follow me and I'll prove it!"
        jump Gym02Day07
    "Leave the gym":
        jump DowntownChoiceDay07b

label Gym02Day07:
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
        jump Gym03Day07
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
        jump Gym03Day07
    "Great, I'll try out the equipment straight away then. See you in a bit.":
        da "Err...Sure... I think..."
        jump Gym03Day07
    "Not convinced, I'll give it a pass for today.":
        da "Your choice, but you're missing out on some great fitness fun!"
        jump DowntownChoiceDay07b

label Gym03Day07:
if hour == 12 or hour == 13 and atelunchday07 == False:
    p "I'd better take a break and eat that sandwich Nancy prepared for me, I'm hungry... Let's eat here, even if its' totally not allowed to eat in a gym."
    scene gymbackground
    show mceating
    with dissolve
    $ renpy.pause(1.0, hard=True)
    p "What are you looking at? You never saw a guy eat a sandwich?"
    $ hour += 1
    $ atelunchday07 = True
    hide mceating
    show mcate
    with dissolve
    p "Ah, now I'm not hungry anymore. Amazing what eating does to your body. Let's move on then..."

scene dorisgym01 with dissolve
play music "Sounds/gymabience.mp3"
$ renpy.pause(1.0, hard=True)
"There's only one \"interesting\" customer in the gym at this time."
menu:
    "Do some heavy training (+1hr)" if (workout == False):
        jump GymWorkoutDay07
    "Approach the woman":
        jump GymDorisDay07

label GymWorkoutDay07:
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
        jump SaunaDorisDay07
    "I don't have time right now I'm afraid, it's getting late...":
        do "Too bad boy, we could have had some good time..."
        jump DowntownChoiceDay07b

label SaunaDorisDay07:
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
jump DowntownChoiceDay07b

label GymDorisDay07:
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
label DorisGymTrainDay07:
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
        jump DorisGymTrainDay07
    "Leave and do some heavy training (+1hr)" if (workout == False):
        jump GymWorkoutDay07    
    "Leave the gym":
        jump DowntownChoiceDay07b

label GymSecondDay07:
da "Welcome back to \"Jerk n' Clean Fitness Club \". Are you planning on using the gym again today?"
scene gym01 with dissolve
menu:
    "Yes, I am a fully-fledged member so it's free right?" if (gymmember == True):
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Of course, just make yourself at home [name]! I can go and get a tan now finally..."
        jump GymSecond01Day07        
    "Yes, here's five bucks to use it for the day...(pay $5)" if (money >= 5):
        $ money -= 5
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Perfect, the gym is all yours... I can go and get a tan now finally..."
        jump GymSecond01Day07
    "Yes, on becoming a fully fledged member." if (money >= 50) and (gymmember == False): 
        $ money -= 50
        $ gymmember = True
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Perfect, the gym is all yours... I can go and get a tan now finally..."
        jump GymSecond01Day07        
    "No, not really, just came to say \"Hi\".":
        show gym02 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Well, \"Hi\" and now \"Goodbye\"..."
        jump DowntownChoiceDay07b

label GymSecond01Day07:
$ wenttogym07 = True
scene gymanna01 with dissolve
play music "Sounds/gymabience.mp3"
$ renpy.pause(1.0, hard=True)
p "There's Anna in a tight outfit..."
if (seendorisgym01 == False) and (seendorissauna == False):
        p "And a muscular lady doing curls."
if (seendorissauna == True) or (seendorisgym01 == True):
        p "And Doris lifting a heavy barbell."
label GymChoiceDay07:
if hour == 12 or hour == 13 and atelunchday07 == False:
    p "I'd better take a break and eat that sandwich Nancy prepared for me, I'm hungry... Let's eat here, even if its' totally not allowed to eat in a gym."
    scene gymbackground
    show mceating
    with dissolve
    $ renpy.pause(1.0, hard=True)
    p "What are you looking at? You never saw a guy eat a sandwich?"
    $ hour += 1
    $ atelunchday07 = True
    hide mceating
    show mcate
    with dissolve
    p "Ah, now I'm not hungry anymore. Amazing what eating does to your body. Let's move on then..."
if (hour >= 19):
    p "Damn, it's getting late. Let's go back home..."
    jump DowntownChoiceDay07b
menu:
    "Do some heavy training (+1hr)" if (workout == False):
        jump GymWorkoutSecondDay07
    "Approach Anna" if (talkedannagym06 == False):
        jump GymAnnaDay07
    "Approach the muscular woman" if (seendorissauna == False) and (seendorisgym05 == False) and (seendorisgym06 == False) and (seendorisgym01 == False):
        jump GymDorisDay07
    "Approach Doris" if ((seendorissauna == True) or (seendorisgym01 == True)) and (seendorisgym05 == False) and (seendorisgym06 == False):
        jump GymDorisBellDay07
    "Go to the tanning rooms" if (seentanningbed05 == False) and (seentanningbed06 == False) and (seentanningbed07 == False):
        jump TanningDay07
    "Leave the gym":
        jump DowntownChoiceDay07b

label TanningDay07:
$ seentanningbed07 = True
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
jump GymChoiceDay07


label GymAnnaDay07:
scene gymanna02 with dissolve
$ renpy.pause(1.0, hard=True)
an "Oh, hello [name]... I'm glad you're here, I don't really know what to do with this machine and the gym owner is not around..."
$ talkedannagym06 = True
menu:
    "Help her":
        jump GymAnnaHelpDay07
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
        jump GymChoiceDay07
    "Ask her if she wants to join you in the sauna":
        scene gymanna02b with dissolve
        $ renpy.pause(1.0, hard=True)
        an "I just arrived here, I haven't even worked out yet!"
        an "So no, I am not interested in wasting my time in the sauna with you...Goodbye [name]."
        jump GymChoiceDay07

label GymWorkoutSecondDay07:
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
jump GymChoiceDay07

label GymAnnaHelpDay07:
$ helpedannagym07 = True
p "Just sit on the bench with your head down, and then do crunches. I'll hold your legs for you if you want."
an "Oh, that's what this machine is for? I hope it works, I would really like to get better abs..."
menu:
    "Your abs are already pretty damn fit Ms Longrod...":
        an "Well, thank you for the compliment, but I have seen the gym owner and hers are like a wall of bricks!"
        an "So let's get to crunching then!"
        jump GymAnnaCrunchDay07
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
        jump GymAnnaCrunchDay07
        
label GymAnnaCrunchDay07:
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
jump GymChoiceDay07

label GymDorisBellDay07:
scene dorisbell01 with dissolve
$ renpy.pause(1.0, hard=True)
if (seendorisgym01 == True) or (seendorissauna == True):
    p "There's Doris training with what looks like a pretty heavy barbell..."
if (seendorisgym01 == False) and (seendorissauna == False):
    p "There's a muscular lady training with what looks like a pretty heavy barbell..."
$ seendorisgym06 = True
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
        jump GymDorisBell03Day07
    "Now I get why you are so muscular, this barbell is super-heavy!":
        do "Yeah, I'm the strongest woman on the island, wanna spot me?"
        p "Sure, I'll spot you Doris."
        jump GymDorisBell02Day07    
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
        jump GymDorisBell03Day07

label GymDorisBell02Day07:
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
                    jump SaunaDorisDay07                    
                "Na, no time, busy busy...":
                    do "You clearly don't have what it takes to become the island's Muscle Stud..."
                    jump GymChoiceDay07
        if (seendorisgym01 == True):
            do "Bailing out are we? How do you expect to win the Muscle Stud competition Saturday if you don't train?"
            p "I train every day! You'll see, I'll be ready on Saturday, I'm da man, I'm DA MAN!"
            do "Well go and play with your tiny toys boy, I'm gonna add some more weights to this barbell, I'm not done with my training yet."
            jump GymChoiceDay07
        if (seendorisgym01 == False):
            do "Too bad, I was looking for a muscle stud to take under my wing for the upcoming Muscle Stud Competition..."
            p "No, I'm a muscle stud, I swear! What's that competition about?"
            do "About more than muscles... Hence the stud part... You'll find out on Saturday. If you don't chicken out."
            jump GymChoiceDay07
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
        jump GymChoiceDay07
    "Pff, piece of cake for me, I'm DA MAN, I'll show you!":
        jump GymDorisBell03Day07
  
label GymDorisBell03Day07:
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
jump GymChoiceDay07

label GymSaturday07a:
if (invitedchantelle == True) or (invitedfrancine == True) or (invitedchantelle05 == True) or (invitedfrancine05 == True) or (invitedchantelle06 == True) or (invitedfrancine06 == True) or (invitedchantelle07 == True) or (invitedfrancine07 == True):
    menu:
        "Call Francine to join you here" if ((gymmember == True) and ((invitedfrancine == True) or (invitedfrancine05 == True) or (invitedfrancine06 == True) or (invitedfrancine07 == True))) and (hour <= 17):
            $ francinegym07 = True
            p "I guess it will take her a while to get there, I might as well enjoy the gym until then."
            jump GymSaturdayChoice07
        "Call Chantelle to join you here" if ((gymmember == True) and ((invitedchantelle == True) or (invitedchantelle05 == True) or (invitedchantelle06 == True)or (invitedchantelle07 == True))) and (hour <= 17):
            $ chantellegym07 = True
            p "I guess it will take her a while to get there, I might as well enjoy the gym until then."
            jump GymSaturdayChoice07
        "Don't invite anyone and enter the gym":
            da "Are you ready for the Muscle Stud competition today [name]?"
            da "Yep! That's why I'm here!"
            jump GymSaturdayChoice07

label GymSaturdayChoice07:
stop music
if hour == 12 or hour == 13 and atelunchday07 == False:
    scene gymbackground
    p "I'd better take a break and eat that sandwich Nancy prepared for me, I'm hungry... Let's eat here, even if its' totally not allowed to eat in a gym."
    show mceating
    with dissolve
    $ renpy.pause(1.0, hard=True)
    p "What are you looking at? You never saw a guy eat a sandwich?"
    $ hour += 1
    $ atelunchday07 = True
    hide mceating
    show mcate
    with dissolve
    p "Ah, now I'm not hungry anymore. Amazing what eating does to your body. Let's move on then..."
        
if hour == 14 or hour == 15 and studwin == False and studlose == False:
    scene gymbackground
    show daniellacomp01 at left
    show doriscomp01 at right
    with dissolve
    da "Ah, there you are. The Muscle Stud competition is about to start. Get in your gear and join us in the sauna room. *wink*"
    p "Right, I'll go the boy's locker room and put on my XXXL jockstrap then."
    do "Oooh, I like to hear THAT."
    jump StudComp01

if chantellegym07 and talkedchantellegym07 == False:
    $ talkedchantellegym07 = True
    scene chantellegym        
    ch "Hi [name], I've arrived!"
    p "Oh, hey Chantelle, I'm glad you came. Isn't this gym great or what?"
    ch "Yeah, I saw they have amazing tanning beds near the entrance."
    ch "I'll actually go and work on my tan now. See you [name]"
if francinegym07 and talkedfrancinegym07 == False:
    $ talkedfrancinegym07 = True
    scene francinegym
    fa "Hello [name], I've finally made it! I can't wait to see the pole-dancing room!"
    p "Hi Francine, yeah, it's at the back over there. But apparently, men are not allowed in there..."
    fa "Well, if there's no one else around, I might let you in (wink). Enjoy your training, I'm off to work on some dance moves!"

scene daniellagym00 with dissolve
play music "Sounds/gymabience.mp3"
$ renpy.pause(1.0, hard=True)
p "There's Daniella working on a machine..."
menu:
    "Approach Daniella" if (gymdaniellatest07 == False):
        jump DaniellaSaturday07
    "Go to the locker room" if (gymlockers05 == False) and (gymlockers06 == False) and (gymlockers07 == False):
        jump GymBoySaturday07
    "Train to get stronger" if (workout == False):
        jump GymWorkoutSaturday07
    "Go to the tanning beds" if (chantellegym07 == True) and (seenchantelletanning07 == False):
        jump ChantelleTanningSaturday07
    "Go to the pole-dancing studio" if (francinegym07 == True) and (seenfrancinegym07 == False):
        jump FrancineSaturday07
    "Leave the gym":
        jump DowntownChoiceDay07b
    
label DaniellaSaturday07:
scene daniellagym01 with dissolve
$ renpy.pause(1.0, hard=True)
p "(Let's see how she handles herself when someone's watching her. Or ogling her as the case may be.)"
scene daniellagym02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellagym03 with fastdissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.5, hard=True)
scene daniellagym02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellagym01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellagym02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellagym03 with fastdissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.5, hard=True)
scene daniellagym02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellagym01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellagym02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellagym03 with fastdissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.5, hard=True)
scene daniellagym02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellagym01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellagym02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellagym03 with fastdissolve
play sound "Sounds/womangroan.mp3"
$ renpy.pause(0.5, hard=True)
scene daniellagym04 with dissolve
da "You thought you could distract me?"
p "Err. No, just enjoying watching a muscle chick performing is all."
da "I hope I performed well enough for you?"
p "You sure did Daniella!"
da "The Muscle Stud competition is very soon... Are you ready big boy?"
p "I sure am Daniella!"
da "Well, let's check this out..."
if workout == False:
    menu:
        "Err... I'd rather not. I still need to train today to get stronger.":
            da "What? So you LIED to me then, You're NOT ready!"
            window hide
            $ lust_points[4] -=1
            show lustminus01:
                xalign 0.7 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            jump GymSaturdayChoice07
        "Okay, I'm in.":
            da "The l000 lbs barbell we'll use for the competition is over there. Get in your jockstrap, as you have to perform half-naked under pressure..."
            p "I'm comfortable performing in my XXXL jockstraps, no worries..."
            da "You certainly have the confidence to win..."
            jump DaniellaTest02Day07
p "Okay, I'm in."
da "The l000lbs barbell we'll use for the competition is over there. Get in your jockstrap, as you have to perform half-naked under pressure..."
p "I'm comfortable performing in my XXXL jockstraps, no worries..."
da "You certainly have the confidence to win..."
jump DaniellaTest02Day07
        
label DaniellaTest02Day07:
scene daniellagym05 with dissolve
$ renpy.pause(1.0, hard=True)
da "Still feeling confident big boy? This barbell is not even the heaviest set you'll have to lift..."
p "Err.. Yeah, 1000lbs should be no problem for me..."
scene daniellagym06 with dissolve
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
da "Well done [name]. Now keep that pose. For as long as I tell you to..."
p "Not too long please, it's fucking heavy!"
scene daniellagym07 with dissolve
$ renpy.pause(1.0, hard=True)
da "What's the hurry big boy? I need to check how you fare under pressure, remember?"
p "You're... feeling me up... Shit, I'm gonna get a hardon!"
scene daniellagym08 with dissolve
$ renpy.pause(1.0, hard=True)
da "That's the plan... And the faster you get hard, the sooner this will be over. Don't forget, keep the barbell up to chest level!"
p "But..."
da "No buts, just do as you're told!"
scene daniellagym09 with dissolve
$ renpy.pause(1.0, hard=True)
da "Let's give this piece of hardening boymeat some fresh air shall we?"
scene daniellagym10 with dissolve
$ renpy.pause(1.0, hard=True)
da "Mmmh, very NICE. Such a LONG, THICK shaft... And not even fully hard yet!"
window hide
$ lust_points[4] +=1
$ score += 1
show lust01:
    xalign 0.8 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
da "I think... I want to see it ROCKHARD!"
scene daniellagym11 with dissolve
$ renpy.pause(1.0, hard=True)
da "Now we're talking! This thing is already well over a foot long... Max is going to have some STIFF competition by the looks of it."
p "Who's Max?"
da "Your main opponent... The current title holder. An alpha-teen STUD like you've rarely seen one."
p "I'll beat him!"
da "Yeah? You think so? Prove it to me then."
scene daniellagym12 with dissolve
$ renpy.pause(1.0, hard=True)
da "I see, you want to impress me with your MASSIVE dong by getting ROCKHARD in front of me... And drooling TONS of precum all over my arm."
p "That's right. I'm the biggest STUD on the island. I'm da man, I'm DA MAN!"
da "And are your loads as big as your package suggests?"
menu:
    "Sure, and with unlimited capacity! I'll show you in no time if you keep pumping it! (- 1 stamina)":
        da "Now THAT is something I'd like to see. RIGHT NOW!"
        jump DaniellaTest03Day07
    "Yeah, but I'm keeping it for the competition..." if studwin == False and studlose == False:
        da "I understand, you don't want to unload before the MAIN event... Still, I would have LOVED to get a peek. *wink*"
        $ hour += 1
        jump GymSaturdayChoice07

label DaniellaTest03Day07:
scene daniellagym13 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
da "YES! BLAST that hot cum all over the place! I don't care if it's my gym and customers will be complaining about the sticky mess you've made!"
window hide
$ lust_points[4] +=1
$ score += 1
show lust01:
    xalign 0.8 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
scene daniellagym14 with dissolve
$ renpy.pause(1.0, hard=True)
da "Mmmh, I was lucky enough to catch some of that sweet cum in my face and mouth too..."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.4
    linear 1.0 yalign 0.6
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ hour += 1
p "I should get going... Thanks for the hand. Job."
jump GymSaturdayChoice07

label GymWorkoutSaturday07:
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
jump GymSaturdayChoice07

label ChantelleTanningSaturday07:
$ seenchantelletanning07 = True
scene chantelletan01 with dissolve
$ renpy.pause(1.0, hard=True)
p "(Ooh... Chantelle is about to get on the tanning bed and she conveniently left the door slightly open...)"
p "(It's amazing how many people forget to close doors on this island really...)"
menu:
    "Leave, you don't want to get caught":
        p "(While I have a nice view of her sumptuous rump, I should probably leave before she sees me...)"
        jump GymSaturdayChoice07
    "Hang around, what could possibly go wrong?":
        jump ChantelleTanningSaturday07b            

label ChantelleTanningSaturday07b:
scene chantelletan02 with dissolve
$ renpy.pause(1.0, hard=True)
p "(Oh yeah, strip for me baby, take that top off!)"
scene chantelletan02b with dissolve
$ renpy.pause(1.0, hard=True)
p "(And now the bottom, please!)"
scene chantelletan03 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Do you realize I could hear everything you said [name]?"
p "(Oh my God, she's a witch, just like sis!)"
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
jump GymSaturdayChoice07

label GymBoySaturday07:
stop music
scene gymboy01 with dissolve
$ renpy.pause(1.0, hard=True)
$ gymlockers07 = True
p "What is going on here? Looks like a young horse-hung muscle stud being serviced by a couple of dykes..."
menu:
    "Leave, this looks like it's going to be NTR-ish and I don't like that one bit!":
        scene gymboy02
        l01 "Yeah, leave us, you're not invited to the party anyway!"
        jump GymSaturdayChoice07
    "What the hell, just watch and hope I can join this time (unlikely...)":
        jump GymBoySaturday07b

label GymBoySaturday07b:
scene gymboy02 with dissolve
$ renpy.pause(1.0, hard=True)
rb "Came to watch how a real stud fucks again?"
menu:
    "Fuck you arsehole! I can have any girl I want too!":
        rb "What do you say girls?"
        l01 "In his dreams! He can watch, but our pussies belong to you daddy!"
        l02 "We can't wait to get rammed by that massive horsecock of yours and covered in ounces of your virile teen seed!"
        p "Well gee, thanks for the warm welcome girls..."
        menu:
            "Leave, you are not wanted clearly...":
                jump GymSaturdayChoice07
            "Stay on, you might get an opportunity somehow...":
                jump GymBoySaturday07c
    "No, I'm just bored, that's all.":
        rb "Ha Ha, right, yeah... Well, watch and learn boy. This is part of my training to retain my title as Muscle Stud saturday." 
        rb "I heard you might be competing too, although you have no chance against me, I've been winning this competition three years in a row already!"
        p "Well, you're about to lose your crown dumbass!"
        l01 "Why don't you shut the hell up and make yourself useful by fisting me, I need to have my pussy loosened up for this young stud's monstercock!"
        menu:
            "I'm in for some good old-fashioned fist-fucking!":
                jump GymBoySaturday07c
            "Leave, it's starting to sound more and more NTR-ish.":
                jump GymSaturdayChoice07
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
                jump GymBoySaturday07c
            "Leave, it's starting to sound more and more NTR-ish.":
                jump GymSaturdayChoice07

label GymBoySaturday07c:
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
label GymBoySaturday07cb:
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
        jump GymBoySaturday07cb
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
        jump GymBoySaturday07d

label GymBoySaturday07d:
if (peeping >= 8) and (achievement.has("peeper") == False):
    show achievement15:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement15
    $ achievement.grant("peeper")
scene gymboy04 with dissolve    
$ renpy.pause(1.0, hard=True)
p "Hey, what about you, how about you give me a blowjob or something?"
scene gymboy04b with dissolve    
$ renpy.pause(1.0, hard=True)
l02 "How about you go fuck yourself? I'm busy gulping down the huge amount of nutjuice this super-stud plastered me with, I have no time for you boy!"
l01 "Oh damn, daddy! Your thingie is so massive! I'm gonna cum in no time! AAAAH!"
rb "There's more where that came from!"
label GymBoySaturday07db:
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
        jump GymBoySaturday07db
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
        jump GymSaturdayChoice07
        
label FrancineSaturday07:
$ seenfrancinegym07 = True
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
        jump GymSaturdayChoice07
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
            jump FrancineSaturdayFuck07
        fa "Thank you for such a nice compliment [name]!"
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (lust_points[7] >=8):
                jump FrancinePendulumSaturday07
            "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[7] >=8):
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump FrancinePheromonesSaturday07
            "Well, I'd better leave you finish off your dance routine and get back to the gym...":
                fa "Bye [name], thanks again for inviting me!"
                $ hour += 1
                jump GymSaturdayChoice07  
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
                jump GymSaturdayChoice07
        
label FrancinePendulumSaturday07:
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
    jump FrancineSaturdayFuck07
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
    jump FrancineSaturdayFuck07

label FrancinePheromonesSaturday07:
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
    jump FrancineSaturdayFuck07
if (lust_points[7] ==9):
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
    jump FrancineSaturdayFuck07

label FrancineSaturdayFuck07:
stop music
fa "Tell me what you think of THIS art!"
scene francinepole05 with dissolve
$ renpy.pause(1.0, hard=True)
fa "Like so..."
p "Damn, she's doing it half-naked now!"
scene francinepole05 with dissolve
$ renpy.pause(1.0, hard=True)
fa "I LOVE holding onto big POLES like that... Do you have one for me [name]?"
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
            jump FrancineCanFuckDay07
        "Don't drink white bull and keep it for another time":
            p "Err. Francine, I think we should keep our relationship purely on the professional level. As colleagues and such."
            fa "Oh. Well, I... You're reprobably right. I should put my clothes back on... And take back that epic lust icon."
            window hide
            $ lust_points[17] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.2 yalign 0.3
                linear 1.0 yalign 0.5
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01            
            jump GymSaturdayChoice07
if (stamina <= 0) and (whitebull == False):
    p "Err. Francine, I think we should keep our relationship purely on the professional level. As colleagues and such."
    fa "Oh. Well, I... You're reprobably right. I should put my clothes back on... And take back that epic lust icon."
    window hide
    $ lust_points[17] -= 1
    $ score -= 1
    show lustminus01:
        xalign 0.2 yalign 0.3
        linear 1.0 yalign 0.5
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01            
    jump GymSaturdayChoice07

label FrancineCanFuckDay07:
p "Fuck yeah! Let me show you MY pole!"
scene francinepole06 with dissolve
play sound "Sounds/francinefuck01.mp3"
$ renpy.pause(3.0, hard=True)
fa "Oh my, that pole is even thicker than a pole-dancing pole! I can't wait for you to FUCK me!"

label FrancineSaturdayFuckChoice07:
scene francineprefuck with dissolve
$ renpy.pause(1.0, hard=True)
fa "I'm ready when you are!"
menu:
    "Well, I'm ready to facefuck your mouth then! Get on your knees." if (francineblow == False):
        fa "I hope my mouth can stretch enough to take on THAT monster..."
        jump FrancineBlowDay07d
    "Hold on to the pole, I'm gonna fuck you from behind!" if (francinedoggy == False):
        fa  "Ooh, I LOVE that idea!"
        jump FrancineDoggyDay07d
    "Let's make sweet love on the floor." if (francineground == False):
        fa "I hope not TOO sweet... My pussy wants a good pounding (wink)."
        p "Yeah, don't worry about it, just get on board for starters..."
        jump FrancineGroundDay07d
    "I'm ready to blow anytime now, do something Francine!" if (francineblow == True) and (francinedoggy == True) and (francineground == True):
        fa  "I know exactly what to do... Double-handed monstercock handjob it is!"
        jump FrancineMovieDay07d

label FrancineBlowDay07d:
$ francineblow = True
scene francineblow01 with dissolve
play sound "Sounds/francinefuck02.mp3"
$ renpy.pause(3.0, hard=True)
p "Easy...Open wide..."
fa "Mmmm, ggglll..."
scene francineblow02 with dissolve
$ renpy.pause(1.0, hard=True)
p "And your throat now... Wider, wider! Aah, this feels good!"
label FrancineBlowDay07bd:
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
        jump FrancineBlowDay07bd
    "Move on":
        pass
fa "Gaaa gaaa, I think... my jaw... is dislocated..."
p "Never mind that, it will get back to normal soon, let's switch position!"
jump FrancineSaturdayFuckChoice07

label FrancineDoggyDay07d:
$ francinedoggy = True
scene francinefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
fa "Oh fuck, FUCK! Give it to me [name]"
p "No problemo. Get ready, set, GO!"
scene francinefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
fa "AAAOUUW, FUCK it hurts! But it's so good! Do it again, please!"
label FrancineDoggyDay07bd:
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
        jump FrancineDoggyDay07bd
    "Move on":
        pass    
fa "That was the best pole-dancing workout I ever got!"
p "My pole sure did give you a workout! Let's do something else now."
jump FrancineSaturdayFuckChoice07    

label FrancineGroundDay07d:
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
label FrancineGroundbDay07bd:
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
        jump FrancineGroundbDay07bd
    "Move on":
        pass    
fa "My pussy is creaming all over the place..."
p "My cock needs a good cleaning then, let's think of another position shall we?" 
jump FrancineSaturdayFuckChoice07    

label FrancineMovieDay07d:
fa "You'll see, my hands will milk a huge load straight out of that cum-cannon!"
play music "Sounds/francinefuckmovie.mp3"
show francinefuckslow
show faster
call screen francineslowfuckday07d
screen francineslowfuckday07d:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FrancineFastFuckDay07d")

label FrancineFastFuckDay07d:
stop music
hide faster
play music "Sounds/francinefuckmovie.mp3"
show francinefuckfast
show cum
call screen francinefastfuckday07d
screen francinefastfuckday07d:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FrancineCumDay07d")

label FrancineCumDay07d:
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
    window hide
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
jump GymSaturdayChoice07

label StudComp01:
stop music
scene stud01 with fade
$ renpy.pause(1.0, hard=True)
da "Welcome everyone to Veri-Bosti's Muscle Stud competition. Today, we have the great honor of hosting the founder of this event,..."
scene stud02 with dissolve
$ renpy.pause(1.0, hard=True)
da "...Arnold Schwarzenpecker!"
ar "I'm back!"
da "As you can see, Arnie has also gone back into top shape, despite being over seventy. No doubt he could win such competitions again today with those HUGE muscles!"
ar "I actually did Daniella... Just came back from the California Muscle Stud Event with the crown..."
da "Oh, wow..."
scene stud03 with dissolve
$ renpy.pause(1.0, hard=True)
da "But today, we have three competitors for our island's title, all young and virile and hung like horses."
scene stud04 with dissolve
$ renpy.pause(1.0, hard=True)
da "Teen defending champion Max!"
window hide
play sound "Sounds/gasp.mp3"
scene stud05 with dissolve
$ renpy.pause(1.0, hard=True)
da "High-school challenger José..."
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
scene stud06 with dissolve
stop sound
$ renpy.pause(1.0, hard=True)
da "And another teenage challenger who recently arrived on the island, [name]!"
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
scene stud03 with dissolve
stop sound
$ renpy.pause(1.0, hard=True)
da "Max's girlfriend has volunteered to handle him, I will assist José, and Doris will be [name]'s handler, if I'm not mistaken?"
do "That's correct. I think my boy has a good chance this year of unseating the current champ..."
if daniellajosewin == True:
    da "So does mine. José is the current local high school stud. And I can vouch for his sexual PROWESS."
    jo "He he... Did you hear that [NAME]? I gave it to her good and HARD and she sure as hell remembers it!"
    p "Won't change a thing, you'll still LOSE this competition douchebag!"
if daniellajosewin == False:
    da "So does mine. José is the current local high school stud from what I hear..."
scene stud02 with dissolve
$ renpy.pause(1.0, hard=True)
da "But we'll soon find out... Arnie, would you be so kind as to launch the competition?"
ar "I declare the 2020 Veri-Bosti Muscle Stud competition OPEN!"
da "First round, get your heaviest dumbbells boys! We want to see how strong you are! We start at 500 pounds."
scene stud07 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/applause.mp3"
da "Piece of cake for Max, as usual!"
scene stud09 with dissolve
$ renpy.pause(1.0, hard=True)
da "José is struggling a bit, but he did it, well done José!"
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
stop sound
if (strength <= 9):
    scene stud13b with dissolve
    play sound "Sounds/dumbbell.mp3"
    $ renpy.pause(1.0, hard=True)
    p "Shit! I'm not even strong enough for THAT???"
    da "Looks like [name] is already out..."
    scene stud03 with dissolve
    $ renpy.pause(1.0, hard=True)
    da "Let's move on to 1000 pounds ..."
    j "I give up, I know I can't lift that much. I prefer to keep my strength for the other rounds..."
    da "Fair enough... This means Max wins the first round by default! Will you show us how you lift 1000 pounds anyway Max?"
    rb "Sure... Here goes..."
    scene stud11 with dissolve
    play sound "Sounds/applause.mp3"
    $ renpy.pause(1.0, hard=True)
    da "Wow, you're getting stronger every year Max...."
    rc "He's a beast... Biggest muscles and... biggest cock on the island!"
    $ round01randywin = True
    jump StudComp02
if (strength >= 10):
    scene stud13b with dissolve
    $ renpy.pause(1.0, hard=True)
    scene stud13a with dissolve
    play sound "Sounds/workoutgroan.mp3"
    $ renpy.pause(0.4, hard=True)
    scene stud13a with dissolve
    $ renpy.pause(0.4, hard=True)
    scene stud13b with dissolve
    $ renpy.pause(0.4, hard=True)
    scene stud13a with dissolve
    $ renpy.pause(0.4, hard=True)
    scene stud13b with dissolve
    $ renpy.pause(0.4, hard=True)
    stop music
    p "Easy, I can do that all day..."
    da "[name] is through to the next round."
    j "What a show-off..."    
scene stud03 with dissolve
$ renpy.pause(1.0, hard=True)
da "Let's move on to 1000 pounds..."
j "I give up, I know I can't lift that much. I prefer to keep my strength for the other rounds..."
da "Fair enough. Your turn to start [name]."
if (strength <= 11):
    if (redgood and redpill >= 1) or (bluegood and bluepill >= 1):
        p "(I haven't trained enough this week, I might need to take the not-bad pill and see if that's a good pill...)"
        menu:
            "Take a red pill" if redgood:
                $ redpill -= 1
                "You quickly swallow a red pill. You feel great and ready to rumble!"
                jump Lift1000pounds
            "Take a bluepill" if bluegood:
                $ bluepill -= 1
                "You quickly swallow a blue pill. You feel great and ready to rumble!"
                jump Lift1000pounds        
            "Don't take a pill":
                pass
    scene stud14 with dissolve
    play sound "Sounds/workoutgroan.mp3"
    $ renpy.pause(1.0, hard=True)
    p "I can do it, I can do it. I'm Da man..."
    scene stud16b with dissolve
    play sound "Sounds/dumbbell.mp3"
    $ renpy.pause(1.0, hard=True)
    p "Shit! I'm not strong enough for that much weight..."
    da "Looks like Max wins this round then... Will you show us how you lift 2000 pounds anyway Max?"
    rb "Sure... Here goes..."
    scene stud12 with dissolve
    play sound "Sounds/applause.mp3"
    $ renpy.pause(1.0, hard=True)
    da "Wow, you're getting stronger every year Max...."
    rc "He's a beast... Biggest muscles and... biggest cock on the island!"
    p "(We'll see about that! I can still win, there are two more rounds.)"
    $ round01randywin = True 
    jump StudComp02
if (strength >= 12):
    label Lift1000pounds:
    scene stud14 with dissolve
    play sound "Sounds/workoutgroan.mp3"
    $ renpy.pause(1.0, hard=True)
    p "I can do it, I can do it. I'm Da man..."
    scene stud15 with dissolve
    play sound "Sounds/applause.mp3"
    $ renpy.pause(1.0, hard=True)
    p "I'm DA MAN!"
    da "Very nice lift there [name]. You are through to the next round. Let's see how our defending champion handles it."
    scene stud10 with dissolve
    play sound "Sounds/grunt.mp3"
    $ renpy.pause(1.0, hard=True)
    p "(Make him drop it, make him drop it...)"
    scene stud11 with dissolve
    play sound "Sounds/applause.mp3"
    $ renpy.pause(1.0, hard=True)
    da "Incredible, Max lifted the barbell with one arm only!"
    ar "I think the defending champion is trying to intimidate his opponent. A common tactic among muscle studs."
scene stud02 with dissolve
$ renpy.pause(1.0, hard=True)
da "Since both Max and [name] are still battling it out, let's move to our heaviest barbell set. TWO THOUSAND POUNDS!"
ar "Even I have trouble managing such an amount. I can only do a dozen or so reps with that much weight."
da "Wow, Arnie, you're sssoo strong. Our contenders here only need to be able to lift the barbell once. Max, you start!"
scene stud12 with dissolve
$ renpy.pause(1.0, hard=True)
da "Max managed 2000 pounds, what a muscle stud! Your turn [name]..."
$ renpy.pause(1.0, hard=True)
scene stud16a with dissolve
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
p "Shit! This thing is fucking heavy... I'll need to push myself to the limits to lift it..."
menu:
    "Just do it! (-1 stamina)":
        p "I can do it, I can do it. I'm Da man..." 
        scene stud16c with dissolve
        play sound "Sounds/workoutgroan.mp3"        
        $ renpy.pause(1.0, hard=True)        
        $ stamina -=1
        show staminaminus01:
            xalign 0.6 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/panting.mp3"
        $ renpy.pause(2, hard=True)
        hide staminaminus01
        da "Looks like [name] also managed to lift 2000lbs! It's a TIE!"
        play sound "Sounds/applause.mp3"
        $ renpy.pause(1.0, hard=True)
        $ muscleman += 1
        if muscleman >= 4:
            window hide
            show achievement20:
                xalign 0.5 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/achievement.mp3"
            $ renpy.pause(4.0, hard=True)
            hide achievement20
            $ achievement.grant("muscleman")            
        $ round01tie = True 
        jump StudComp02        
    "Keep my stamina, I'm sure I can do it anyway...":
        scene stud16b with dissolve
        play sound "Sounds/dumbbell.mp3"
        $ renpy.pause(1.0, hard=True)
        p "SH-III-IT! It's too heavy!"
        scene stud03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "[name] didn't manage to lift 2000lbs, which means that Max wins the first round!"
        play sound "Sounds/applause.mp3"
        $ renpy.pause(1.0, hard=True)
        rc "He's a beast... Biggest muscles and... biggest cock on the island!"
        p "(We'll see about that! I can still win, there are two more rounds.)"
        $ round01randywin = True 
        jump StudComp02
    "Take a red pill" if redgood and redpill >= 1:
        $ redpill -= 1
        "You quickly swallow a red pill. You feel great and ready to rumble!"
        jump Lift2000pounds
    "Take a bluepill" if bluegood and bluepill >= 1:
        $ bluepill -= 1
        "You quickly swallow a blue pill. You feel great and ready to rumble!"
        jump Lift2000pounds        
        
label Lift2000pounds:
scene stud16c with dissolve
play sound "Sounds/gasp.mp3"
$ renpy.pause(1.0, hard=True)
da "Looks like [name] also managed to lift 2000lbs! It's a TIE!"
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
$ muscleman += 1
if muscleman >= 4:
    window hide
    show achievement20:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement20
    $ achievement.grant("muscleman")    
$ round01tie = True 
jump StudComp02

label StudComp02:
scene studcomp02 with dissolve
$ renpy.pause(1.0, hard=True)
if round01randywin:
    ar "So at the end of this round, Max has the lead. Now let's see that other muscle of yours boys! The most important one..."
if round01tie:
    ar "So at the end of this round, Max and [name] are tied to first place. Now let's see that other muscle of yours boys! The most important one..."
da "The rumor has it you've ploughed your way through thousands of women Arnie. Is that true?"
ar "Yes, I can confirm that. Even today, I'm averaging a couple dozen women a week."
da "Mmmh, such a STUD! Even at 70+.... Max, time to unleash the beast and show us what you're packing!"
ar "I'm guessing his girlfriend will do the honors... One of the perks of bringing your girlfriend along."
scene randymeasuring01 with dissolve
$ renpy.pause(1.0, hard=True)
rc "Mmh, your cock is really stretching that jockstrap Max... If I don't pull it aside, you'll TEAR it apart..."
rb "That's right, I still have a few more inches to add to my length and girth before I'm ROCKHARD!"
scene randymeasuring02 with dissolve
$ renpy.pause(1.0, hard=True)
rc "There, that's better, now it can grow to full mast without hindrance..."
rb "And I will get hard in no time if you continue playing with it like that..."
rc "I want you at your BIGGEST and HARDEST for me!"
scene randymeasuring03 with dissolve
$ renpy.pause(1.0, hard=True)
rc "My boyfriend is 18 inches long fully erect from base to tip!"
da "Wow, that's HUGE! An inch bigger than last year too. And he already won easily back then."
ar "Even bigger than me, I'm very impressed... Let's see what that latino boy is hiding in his oversized shorts."
scene josemeasuring01 with dissolve
$ renpy.pause(1.0, hard=True)
da "Definitely a very LARGE bulge. See how it stretches the fabric of his swimming trunks to overcapacity?"
j "And I'm not even hard yet..."
da "Well, you'd better get HARD and ERECT, boy, cos I'm about to pull those trunks down and measure the length of your fuckpole with Swiss precision!"
scene josemeasuring02 with dissolve
$ renpy.pause(1.0, hard=True)
da "José is a very impressive 11 inches of fat boymeat! We've got some real \"wieners\" this year! Everyone is in the double-digits."
ar "I don't know what you feed your boys on this island but I've never seen such a density of young horsecocks anywhere else in the world... Or huge boobs for that matter..."
do "That's why our island is so special Arnie. We beat every other country in sexual satisfaction according to Spew Research."
da "Now for our last contender, [name]. Will he at least beat José and stay in the race to win this competition?"
p "Pff, José is just a weakling and I'll prove it, my cock will put his to SHAME!"
da "OOh, someone seems to be in a hurry to show us his hard monster shaft. Doris will be the one measuring this time..."
scene mcmeasuring01 with dissolve
$ renpy.pause(1.0, hard=True)
do "Your bulge is getting BIGGER and BIGGER... I guess it's time to reveal your GIANT teenage horsedick to everyone here..."
scene mcmeasuring02 with dissolve
$ renpy.pause(1.0, hard=True)
do "Damn, even in its semi-flaccid state, this thing is GIGANTIC!"
p "Already bigger than that douchebag José, I'm da man!"
j "Fuck you [name], I'm still the local school stud and you're nothing but a WORM!"
scene mcmeasuring03 with dissolve
play sound "Sounds/gasp.mp3"
$ renpy.pause(1.0, hard=True)
do "My boy here is sporting a REAL 18-incher! I definitely wouldn't call it a worm... *wink*"
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
scene stud03 with dissolve
$ renpy.pause(1.0, hard=True)
da "Incredible! We have a tie for this round. The ultimate round will therefore be the one that determines who between Max and [name] will go home with the crown!"
if (lust_points[4] <= 8):
    window hide
    $ lust_points[4] +=1
    $ score += 1
    show lust01:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
scene studcomp02 with dissolve
$ renpy.pause(1.0, hard=True)
ar "The final round is always the toughest for the contestants since they need to ejaculate and prove their virility."
scene stud03 with dissolve
$ renpy.pause(1.0, hard=True)
da "Exactly Arnie, you should know, you designed the rules when you first launched the Mr Muscle Stud contests worlwide twenty years ago."
da "And so what we'll happen is that we'll measure the volume of cum that each of our studs can produce. Who can cum the most? First, we'll take a short break."
$ hour += 1
scene studbreak01 with fade
da "You can all have some energy drinks, courtesy of the gym."
menu:
    "Drink and take a red pill at the same time" if redgood and redpill >= 1:
        $ redpill -= 1
        jump MCPillDrink
    "Drink and take a blue pill at the same time" if bluegood and bluepill >= 1:
        $ bluepill -= 1
        jump MCPillDrink
    "Drop a red pill in José's drink" if bluegood and redpill >= 1:
        $ redpill -= 1
        jump JosePillDrink
    "Drop a blue pill in José's drink" if redgood and bluepill >= 1:
        $ bluepill -= 1
        jump JosePillDrink
    "Drop a red pill in Max's drink" if bluegood and redpill >= 1:
        $ redpill -= 1
        jump MaxPillDrink
    "Drop a blue pill in Max's drink" if redgood and bluepill >= 1:
        $ bluepill -= 1
        jump MaxPillDrink
    "Just enjoy your break and chat with Doris.":
        scene dorisbreak with dissolve
        $ renpy.pause(1.0, hard=True)
        do "So, [name], are you going to pump out an EXTRA-BIG load for me today?"
        p "I sure will Doris. You'll fucking drown in it, I promise!"
        do "I'm glad to hear that, I want you to WIN this competition, you hear me?"
        if (lust_points[6] >= 8):
            window hide
            $ lust_points[6] +=1
            $ score += 1
            show lust01:
                xalign 0.2 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        p "You can count on me Doris!"
        jump StudComp03

label MCPillDrink:
$ mctookpill = True
if redgood:
    "You quickly swallow a red pill. You feel great and ready to rumble!"
    jump StudComp03
if bluegood:
    "You quickly swallow a blue pill. You feel great and ready to rumble!"
    jump StudComp03

label MaxPillDrink:
scene studbreak02 with dissolve
$ renpy.pause(1.0, hard=True)
p "There you go buddy, have an energy drink."
rb "Thanks [name]. I see you have already accepted your defeat and you are being subservient to the ultimate island stud."
p "(We'll see about that arsehole, enjoy your pill!)"
$ maxtookpill = True
jump StudComp03

label JosePillDrink:
scene studbreak03 with dissolve
$ renpy.pause(1.0, hard=True)
p "There you go José, have an energy drink."
j "Ha ha, you're literally being a slave to me. Finally!"
p "Just being nice, that's all. You should try it some day."
p "(We'll see who laughs last, enjoy your pill douchebag!)"
$ josetookpill = True
jump StudComp03


label StudComp03:
scene stud03 with dissolve
$ renpy.pause(1.0, hard=True)
da "First up, José. How much cum will erupt from his fully-loaded cum cannon? Only one way to find out! And I'll do the honors."
scene josewanked01 with dissolve
$ renpy.pause(1.0, hard=True)
da "So, are you ready to deliver a HUGE load for me José? I'm your handler so I've got to make sure you are at your absolute BEST when you explode!"
j "Oh fuck... Those tits..."
scene josewanked02 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
j "SHIT, I can't hold it, I'm cumming!"
da "Oh my, I didn't expect such an early dose! I know I have EXPERT hands but still... Quick Doris, hand me the measuring glass!"
do "Sure, here it is, you'd better hurry up, cum is flying everywhere already!"
da "We always count the amount IN the jar and the amount ON the floor because of such premature ejaculations..."
do "They happen every year. Especially when YOU handle the boys Daniella!"
if josetookpill:
    scene josewanked04b with dissolve
    $ renpy.pause(1.0, hard=True)
    da "Well that's disappointing, you only managed 100ml of sperm??? That's one of our LOWEST measurements EVER."
    if (lust_pointsB[4] <= 9):
        window hide
        $ lust_pointsB[4] -=2
        show challengerlustminus02:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus02
    j "But... I don't understand what happened!"
    p "You're a wimp, that's what happened José, HA HA!"
    jump MaxCumDay07
scene josewanked03 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
da "There you go, keep pumping that ball-batter José... Mmmh, I can feel the warmth from where I'm kneeling... It's SCOLDING!"
scene josewanked04 with dissolve
$ renpy.pause(1.0, hard=True)
da "Nice fat load there José, a very impressive 300ml of spunk. Your competitors are going to have to churn up an extra-big load to beat you for sure!"
j "And they won't, I'm quite confident. Especially [name], he's just a junior wimp!"
p "Yeah? We'll see about that douchebag!"
label MaxCumDay07:
scene stud03 with dissolve
$ renpy.pause(1.0, hard=True)
da "Now, now boys, let's keep this competition civil. Only one of you is going home with the crown and the others will be total losers. That's the take-home message."
da "And now, it's Max's turn to show us what he's got in his bull-balls! I leave you and your girlfriend the floor... I see she's already naked and ready for this round..."
scene redheadfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
rc "First, I'll warm him up and get him all excited..."
rb "Good idea, the hornier I'll get, the bigger my cumload..."
rc "Then let me get your juices REALLY going..."
scene redheadfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
rc "I know my muscle stud loves it when I rub his shaft between my legs..."
rb "Oh fuck, your thighs feel amazing, ssoo much friction..."
scene redheadfuck02b with dissolve
$ renpy.pause(1.0, hard=True)
rc "Then let me rub it some more..."
scene redheadfuck02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02b with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02b with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02b with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02b with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02b with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02b with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck02b with fastdissolve
$ renpy.pause(0.4, hard=True)
rb "Fuck yeah! I'm as hard as granite!"
if randyboyspiked == True:
    p "(Damn it, when will this pill take effect?)"
scene redheadfuck04 with dissolve
$ renpy.pause(1.0, hard=True)
rc "Then cum for me Max! Blast as many fat ropes of teenage cum as you can muster!"
scene redheadfuck04cum with dissolve
play sound "Sounds/randyboycumming.mp3"
$ renpy.pause(1.0, hard=True)
rb "That's it, I'm CUMMING! Sooo fucking strong!"
if maxtookpill:
    scene redheadfuck04 with dissolve
    $ renpy.pause(1.0, hard=True)
    rc "What's going on stud? You stopped cumming already???"
    rb "I... don't know what happened.... Normally, I can come WAY MORE than that!"
    p "(He he... Got him!)"
    da "Our current champ seems to have suffered from stage fright I assume... Doris, will you estimate the amout of cum for us?"
    scene randycum01 with dissolve
    $ renpy.pause(1.0, hard=True)
    do "Sure thing Daniella... I'd say we have roughly 500ml of warm sperm in the jar."
    da "Max takes the lead nonetheless. We'll see if [name] can beat him for this final stage of our competition."    
if maxtookpill == False:
    scene redheadfuck04cum4b with dissolve
    play sound "Sounds/randyboycumming02.mp3"
    $ renpy.pause(1.0, hard=True)
    rc "Mmh, yes, spew that hot sauce and fill up the glass STUD!"
    rb "I will, don't worry, I'll overflow it like last year! RHAAA!"
    da "That's again a MONSTER load that we are witnessing from the reigning champion!"    
    do "Damn, the jar is already full and he's still spewing non-stop... Not to mention all the cum puddles on the floor..."
    da "What's the final tally Doris?"
    scene randycum01b with dissolve
    $ renpy.pause(1.0, hard=True)
    do "Well, counting the full glass and the cum that's everywhere else, I estimate the volume at a FULL LITER of teenage spunk."
    ar "That's astounding, I don't recall seeing a competitor deliver that much cum in all my travels to various competitions worldwide."
    da "Veri-Bosti rules! But we still have a final contestant, will he be able to surpass this incredible amount of virile spunk with HIS load?"    
menu:
    "Strain yourself and churn up an EXTRA-BIG load (-2 stamina)" if stamina >=2:
        $ extrahugeload = True
        pass
    "Don't strain yourself and keep your stamina (-1 stamina)":
        pass
            
scene mcwanked01 with dissolve
$ renpy.pause(1.0, hard=True)
do "Are you ready to give us a big load [name]? A REALLY big load?"
p "Yeah, I'll show those two wimps how a REAL man comes. How DA MAN cums!"
scene mcwanked02 with dissolve
$ renpy.pause(1.0, hard=True)
do "I can feel you tensing up, just release yourself, let it ALL out!"
p "Fuck, I'm about to..."
scene mcwanked03 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "... CUM BIG TIME! RHAAA!"
$ stamina -=1
show staminaminus01:
    xalign 0.6 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
if extrahugeload or mctookpill:
    jump CompRoundThreeHugeLoad
else:
    jump CompRoundThreeNormalLoad

label CompRoundThreeHugeLoad:
scene mcwanked04b with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
do "There you go, let it all out [name]! KEEP PUMPING!"
p "RHAAAA!"
scene mcwanked04 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
do "Keep going, blast those thick viscous jets inside the glass for me... There you go..."
p "Oh Damn, you've totally drained me..."
if extrahugeload:
    $ stamina -=1
    show staminaminus01:
        xalign 0.8 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
do "That was the point. Getting a MONSTER LOAD out of your giant balls!"
da "That looked like it was a LOT of cum, but was it enough to beat the current champ? Doris, what's the tally?"
play sound "Sounds/drumroll.mp3"
$ renpy.pause(3.0, hard=True)
stop sound
do "We have well OVER 1 full liter of sperm here, counting the overflowing jar and the ENORMOUS puddles of cum on the floor!"
$ round03mcwin = True
da "Damn, [name] definitely wins this round then!"
jump StudTally

label CompRoundThreeNormalLoad:
scene mcwanked04b with dissolve
$ renpy.pause(1.0, hard=True)
da "That was a LOT of cum, but was it enough to beat the current champ? Doris, what's the tally?"
play sound "Sounds/drumroll.mp3"
$ renpy.pause(3.0, hard=True)
stop sound
if maxtookpill == False:
    scene randycum01b with dissolve
    $ renpy.pause(1.0, hard=True)    
    do "We have around 500ml of sperm. A HUGE amount for sure, but far less than Max... What a disappointment you have been [name]. I'm never handling YOU again!"
    $ round03randywin = True
if maxtookpill:
    scene randycum01b with dissolve
    $ renpy.pause(1.0, hard=True)
    do "We have around 500ml of sperm! A HUGE amount of young thick ball-batter.... Mmmh."
    da "The same amount as Max then. Then we have another tie..."
    $ round03tie = True
jump StudTally

label StudTally:
scene stud03 with dissolve
$ renpy.pause(1.0, hard=True)
if (round01tie and round03tie):
    da "We have a perfect tie between Max and [name]."
    da "However, the rules are clear. The current holder retains his title."
    ar "I agree. These are the rules. Sorry [name], you did very well, but you had to BEAT Max to take his title..."
    p "(FUUUUCCKKK! What a rip-off...)"
    da "And therefore..."
    $ studlose = True
    jump CompEndRandyWin
if (round01tie and round03randywin) or (round01randywin and round03tie) or (round01randywin and round03randywin):
    da "We have a clear winner today. Just like in previous years..."
    da "And therefore..."
    $ studlose = True
    jump CompEndRandyWin
if (round01tie and round03mcwin):
    da "We have a clear winner today. And it's a NEW title holder..."
    $ studwin = True
    jump CompEndWin
if (round01randywin and round03mcwin):
    da "We have a tie between Max and [name]. Max won the first round, but [name] was the biggest cum-blaster in round 03..."
    da "The rules are clear in the event of such a tie. Round 03 takes precedence and therefore we have a NEW title holder..."
    $ studwin = True
    jump CompEndWin
                                                                                                                        
label CompEndRandyWin:
scene compwinrandy with dissolve
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
da "For the third year in a row, Max wins the title of Veri-Bosti's Muscle Stud! Congrats to the winner!"
ar "Here is your trophy, boy. I predict a HUGE future for you. Maybe even the title of Mister World Muscle Stud."
p "(Damn it... Now I'll have to find a way of fucking Daniella and Doris separately and I have very little time left...)"
rc "Max, I see you are still hard as usual... I think we should give them a show, don't you think?"
rb "Sure babe, I'm always ready to fuck you anywhere and anytime!"
rc "Mmh, that's why you're my boyfriend even if you're so young... I can always count on you and that ROCK-HARD MONSTER of yours to satisfy me!"
scene redheadfuck05 with fade
$ renpy.pause(1.0, hard=True)
play sound "Sounds/moaning.mp3"
rc "Oh fuck, you're ssoo big. Truly the BIGGEST!"
rb "That's just the tip baby, wait for the rest of it..."
scene redheadfuck05b with dissolve
$ renpy.pause(1.0, hard=True)
rc "AAAH! Yes, fuck me faster! I'm squirting on that MONSTERDICK!"
play music "Sounds/womansex01.mp3"
scene redheadfuck05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck05b with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck05b with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck05b with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck05b with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene redheadfuck05b with fastdissolve
$ renpy.pause(0.3, hard=True)
scene redheadfuck05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene redheadfuck05b with fastdissolve
$ renpy.pause(0.3, hard=True)
scene redheadfuck05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene redheadfuck05b with fastdissolve
$ renpy.pause(0.3, hard=True)
scene redheadfuck05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene redheadfuck05b with fastdissolve
$ renpy.pause(0.3, hard=True)
scene redheadfuck05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene redheadfuck05b with fastdissolve
$ renpy.pause(0.3, hard=True)
stop music
scene redheadfuck06 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
rc "Such a nice fat load, even after your MONUMENTAL discharge earlier on STUD... Fuck me some MORE!"
rb "No problem, I still have over a dozen loads churning in my balls right now!"
p "I'm outta here, I'm sick and tired of watching this arsehole fucking his girlfriend in front of me like that."
$ hour += 1
jump DowntownChoiceDay07b


label CompEndWin:
scene compwinmc01 with dissolve
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
da "[name] wins the crown and is officially Veri Bosti's Muscle Stud 2020! Congrats to the winner!"
ar "Here is your trophy, boy. I predict a HUGE future for you. Maybe even the title of Mister World Muscle Stud."
if (lust_points[4] == 9):
    window hide
    $ lust_points[4] +=1
    $ score += 1
    show lust01:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[4] <= 8):
    window hide
    $ lust_points[4] +=2
    $ score += 2
    show lust02:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
if (lust_points[4] >= 10):
    window hide
    show epiclust:
        xalign 0.8 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
do "My boy wins! Thanks to the INTENSE training I had with him this week. *wink*"
if (lust_points[6] == 9):
    window hide
    $ lust_points[6] +=1
    $ score += 1
    show lust01:
        xalign 0.2 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[6] == 8):
    window hide
    $ lust_points[6] +=2
    $ score += 2
    show lust02:
        xalign 0.2 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
if (lust_points[6] <= 7):
    window hide
    $ lust_points[6] +=3
    $ score += 3
    show lust03:
        xalign 0.2 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust03
if (lust_points[6] >= 10):
    window hide
    show epiclust:
        xalign 0.2 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
if (lust_points[6] >= 10) and (lust_points[4] >= 10):
    window hide
    show doubledelight:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/delight.mp3"
    $ renpy.pause(4.0, hard=True)
    hide doubledelight
    da "The winner needs to stay behind so that Arnie can give him his prize money... Everyone can leave now, see you all next year!"
    ar "And thanks for inviting me Daniella. It sure was a great competition."
    do "And we'll make it even BETTER once everyone's left Arnie! *wink*"
    scene compwinmc02 with dissolve
    $ renpy.pause(1.0, hard=True)
    da "And now we're alone at last, with two HUGE cocks at our disposal."
    if stamina >= 1:
        do "One is already hard and ready... Yours, [name]... And we want it to FUCK our pussies."
        $ hour += 1
        jump FoursomeDay07
    if stamina <= 0 and whitebull == False:
            p "Err... You know what? This competition has exhausted me... I need to rest... How about we put it off till tomorrow?"
            da "Arnie will be gone by tomorrow! We wanted a foursome and now you're chickening out!"
            do "And you call yourself a msucle stud? You should give that crown back to Max, you don't deserve it! And we'll take that double-delight icon back too..."
            p "I do, I WON the competition fair and square! It's just that I hadn't planned on the AFTER-competition party..."
            da "Then go back home and sleep like a baby [name]. We'll have fun with Arnie without you! He's ready to satisfy us, UNLIKE YOU!"
            ar "I sure am ladies. Plenty of cock and cum for both of you till the sun rises in the morning!"
            p "(How humiliating.. In front of my hero...)"
            window hide
            $ lust_points[4] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.6 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            window hide
            $ lust_points[6] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.6 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            $ hour += 1
            jump DowntownChoiceDay07b
    if stamina <= 0 and whitebull == True:
            p "(This seems like a good time to recharge my batteries and reload my balls with cum by drinking an energy drink...)"
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
                    p "Ok, I'm ready to show you girls what a true muscle stud is capable of!"
                    do "We can see that, you're already hard and ready..."
                    $ hour += 1
                    jump FoursomeDay07                    
                "Bail out":
                    p "Err... You know what? This competition has exhausted me... I need to rest... How about we put it off till tomorrow?"
                    da "Arnie will be gone by tomorrow! We wanted a foursome and now you're chickening out!"
                    do "And you call yourself a msucle stud? You should give that crown back to Max, you don't deserve it! And we'll take that double-delight icon back too..."
                    p "I do, I WON the competition fair and square! It's just that I hadn't planned on the AFTER-competition party..."
                    da "Then go back home and sleep like a baby [name]. We'll have fun with Arnie without you! He's ready to satisfy us, UNLIKE YOU!"
                    ar "I sure am ladies. Plenty of cock and cum for both of you till the sun rises in the morning!"
                    p "(How humiliating.. In front of my hero...)"
                    window hide
                    $ lust_points[4] -= 1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.6 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                    window hide
                    $ lust_points[6] -= 1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.6 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                    $ hour += 1
                    jump DowntownChoiceDay07b


if (lust_points[6] >= 10) and (lust_points[4] <= 9):
    do "The winner needs to stay behind so that Arnie can give him his prize money... Everyone can leave now, see you all next year!"
    ar "And thanks for inviting me both of you. It sure was a great competition."
    da "And I'll make it even BETTER once everyone's left Arnie! *wink* You come with me... Backstage."
    scene compwindoris with dissolve
    $ renpy.pause(1.0, hard=True)
    do "And now we're alone at last, and I intend to make good use of that Muscle Stud GIANT cock of yours [name]!."
    if stamina >= 1:
        p "And I'm ready to bang your pussy into oblivion Doris!"
        do "Ooh, such a sweet talker. Now let's see if you can walk the walk..."
        $ hour += 1
        jump DorisFuckDay07
    if stamina <= 0 and whitebull == False:
            p "Err... You know what? This competition has exhausted me... I need to rest... How about we put it off till tomorrow?"
            do "And you call yourself a msucle stud? You should give that crown back to Max, you don't deserve it! And I'll take that epiclust icon back too..."
            p "I WON the competition fair and square! It's just that I hadn't planned on the AFTER-competition party..."
            do "Then go back home and sleep like a baby [name]. I'll have fun with Arnie without you! He's ready to satisfy both of us, UNLIKE YOU!"
            ar "I sure am ladies. Plenty of cock and cum for both of you till the sun rises in the morning!"
            p "(How humiliating.. In front of my hero...)"
            window hide
            $ lust_points[5] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.6 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            $ hour += 1
            jump DowntownChoiceDay07b
    if stamina <= 0 and whitebull == True:
            p "(This seems like a good time to recharge my batteries and reload my balls with cum by drinking an energy drink...)"
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
                    p "And I'm ready to bang your pussy into oblivion Doris!"
                    do "Ooh, such a sweet talker. Now let's see if you can walk the walk..."
                    $ hour += 1
                    jump DorisFuckDay07                    
                "Bail out":
                    p "Err... You know what? This competition has exhausted me... I need to rest... How about we put it off till tomorrow?"
                    do "And you call yourself a msucle stud? You should give that crown back to Max, you don't deserve it! And I'll take that epiclust icon back too..."
                    p "=I WON the competition fair and square! It's just that I hadn't planned on the AFTER-competition party..."
                    do "Then go back home and sleep like a baby [name]. I'll have fun with Arnie without you! He's ready to satisfy both of us, UNLIKE YOU!"
                    ar "I sure am ladies. Plenty of cock and cum for both of you till the sun rises in the morning!"
                    p "(How humiliating.. In front of my hero...)"
                    window hide
                    $ lust_points[5] -= 1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.6 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                    $ hour += 1
                    jump DowntownChoiceDay07b

if (lust_points[6] <= 9) and (lust_points[4] >= 10):
    da "The winner needs to stay behind so that Arnie can give him his prize money... Everyone can leave now, see you all next year!"
    ar "And thanks for inviting me Daniella. It sure was a great competition."
    do "And I'll make it even BETTER once everyone's left Arnie! *wink* You come with me... Backstage."
    scene compwindaniella with dissolve
    $ renpy.pause(1.0, hard=True)
    da "And now we're alone at last, and I intend to make good use of that Muscle Stud GIANT cock of yours [name]!."
    if stamina >= 1:
        p "And I'm ready to bang your pussy into oblivion Daniella!"
        da "Ooh, such a sweet talker. Now let's see if you can walk the walk..."
        $ hour += 1
        jump DaniellaFuckDay07
    if stamina <= 0 and whitebull == False:
            p "Err... You know what? This competition has exhausted me... I need to rest... How about we put it off till tomorrow?"
            da "And you call yourself a muscle stud? You should give that crown back to Max, you don't deserve it! And I'll take that epiclust icon back too..."
            p "I WON the competition fair and square! It's just that I hadn't planned on the AFTER-competition party..."
            da "Then go back home and sleep like a baby [name]. I'll have fun with Arnie without you! He's ready to satisfy both of us, UNLIKE YOU!"
            ar "I sure am ladies. Plenty of cock and cum for both of you till the sun rises in the morning!"
            p "(How humiliating.. In front of my hero...)"
            window hide
            $ lust_points[4] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.6 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            $ hour += 1
            jump DowntownChoiceDay07b
    if stamina <= 0 and whitebull == True:
            p "(This seems like a good time to recharge my batteries and reload my balls with cum by drinking an energy drink...)"
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
                    p "And I'm ready to bang your pussy into oblivion Daniella!"
                    da "Ooh, such a sweet talker. Now let's see if you can walk the walk..."
                    $ hour += 1
                    jump DaniellaFuckDay07                    
                "Bail out":
                    p "Err... You know what? This competition has exhausted me... I need to rest... How about we put it off till tomorrow?"
                    da "And you call yourself a muscle stud? You should give that crown back to Max, you don't deserve it! And I'll take that epiclust icon back too..."
                    p "I WON the competition fair and square! It's just that I hadn't planned on the AFTER-competition party..."
                    da "Then go back home and sleep like a baby [name]. I'll have fun with Arnie without you! He's ready to satisfy both of us, UNLIKE YOU!"
                    ar "I sure am ladies. Plenty of cock and cum for both of you till the sun rises in the morning!"
                    p "(How humiliating.. In front of my hero...)"
                    window hide
                    $ lust_points[4] -= 1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.6 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                    $ hour += 1
                    jump DowntownChoiceDay07b

if (lust_points[6] <= 9) and (lust_points[4] <= 9):
    da "The winner needs to stay behind so that Arnie can give him his prize money... Everyone can leave now, see you all next year!"
    ar "And thanks for inviting me Daniella. It sure was a great competition."
    do "And we'll make it even BETTER once [name]'s left Arnie! *wink* You go backstage. And we'll come and join you..."
    scene compwinmc02 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Hey! What about me? I'm the MUSCLE STUD here!"    
    da "Yeah, but the muscle stud without enough lust points. While we've already both reached 10 with Arnie. So we'll fuck him instead of you. In private."
    do "Now shoo [name]. See you another time."
    p "AAAARGHHHH!"
    $ hour += 1
    jump DowntownChoiceDay07b
    
label DorisFuckDay07:
stop music
scene dorisprefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
do "I see you are already standing at FULL ATTENTION."
p "I'm always hard and ready when I'm next to some HOT BUSTY BABE Doris!"
scene dorisprefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
do "That's good. Now STAY hard for the titfuck of your life with those HUGE balloons!"
p "Oh fuck, I'm getting even HARDER now thinking about those giant jugs of yours wrapped around my dong!"
scene doristits01 with dissolve
play sound "Sounds/dorismouth01.mp3"
$ renpy.pause(1.0, hard=True)
do "You're so HUGE I can easily lick your drooling tip while I engulf your shaft between my firm knockers..."
p "Oooh, that's nice... Your tongue..."
scene doristits02 with dissolve
play sound "Sounds/dorismouth02.mp3"
$ renpy.pause(2.0, hard=True)
do "What about my warm mouth?"
p "It feels so good on my helmet. Keep going down Doris..."
scene doristits03 with dissolve
$ renpy.pause(1.0, hard=True)
p "That's it, you're doing good... Open that throat and let it slide in..."
scene doristits04 with dissolve
$ renpy.pause(1.0, hard=True)
do "GGGLluuurrr"
p "You're almost all the way to the root! I don't even know where my tip is right now..."
label DorisTitDay07b:
play music "Sounds/hardsucking.mp3"
scene doristits02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits04 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits04 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits04 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits04 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits04 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits04 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits04 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene doristits04 with fastdissolve
$ renpy.pause(0.2, hard=True)
stop music   
menu:
    "Repeat":
        scene doristits01 with dissolve
        $ renpy.pause(1.0, hard=True)
        do "Oh, you want some more dual blowjob-titjob action do you?"
        p "Of course, it's making my cock as stiff as an iron bar!"
        jump DorisTitDay07b
    "Move on":
        scene doristits01 with dissolve
        $ renpy.pause(1.0, hard=True)
        do "Had enough? Scared you might cum too early perhaps?"
        p "N..No, it's just that... I need a... pause..."
        do "So what do you want to do next?"
    
label DorisFuckChoiceDay07:
menu:
    "I want to feel that tight arse wrapped around my monster pole!" if (dorisanal == False):
        do "In my arse? I sure hope I can take something as COLOSSAL as your cock in there!"
        p "So do I. But I'm guessing that somehow the dev will make it fit."
        jump DorisAnalDay07
    "Get on all fours, I'm gonna pound you from behind!!" if (dorisdoggy == False):
        do "WARF, warf! I'll be a good BITCH in heat for you [name]!"
        jump DorisDoggyDay07
    "Ride me like a bull... that's hung like a bull." if (dorisanal == True) and (dorisdoggy == True):
        do "A bull has nothing on YOU Mr MUSCLE STUD!"
        jump DorisCumDay07

label DorisAnalDay07:
$ dorisanal = True
scene dorispreanal with dissolve
$ renpy.pause(1.0, hard=True)
p "First, I'll let some precum drip down your backside."
do "So thoughtful of you. It certainly needs to be WELL lubricated."
p "Ready to get impaled by the island's Muscle Stud's cock Doris?"
do "YES! Just RAM IT IN STUD!"
scene dorisanal01 with dissolve
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
do "It feels like a giant LOG inside me!"
p "That's cos it IS."
scene dorisanal02 with dissolve
$ renpy.pause(1.0, hard=True)
do "AAAAAH! And there was even MORE cock inches to go? My God, what an true ALPHA-STUD you are [name]!"
p "I didn't win the title for nothing! Get ready for the anal pounding of your lifetime Doris!"
do "I'm ready, just SODOMIZE ME HARD!"
label DorisAnalDay07b:
play music "Sounds/dorisanal.mp3"
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.2, hard=True)
stop music
menu:
    "Repeat":
        do "I don't know if I can take anymore of that POUNDING!"
        p "Yes you can. And I'll prove it!"
        jump DorisAnalDay07b
    "Move on":
        do "Thank you so much for such an anal pounding. I feel like my butthole virginity has been taken away from me once again."
        p "Let's switch position then."
        do "What do you have planned for me next STUD?"
        jump DorisFuckChoiceDay07

label DorisDoggyDay07:
$ dorisdoggy = True
scene dorispredoggy with dissolve
play sound "Sounds/dorisbiggest.mp3"
$ renpy.pause(2.0, hard=True)
do "Your dong is drooling precum all over my stomach baby... You're really excited thinking about fucking my sweet pussy, aren't you?"
p "Yes, your body was made for fucking. A HUGE STUDCOCK."
do "Then show me what you can do it with it. Quick, I'm so horny for it!"
scene dorisdoggy01 with dissolve
$ renpy.pause(1.0, hard=True)
do "That's it, now fuck me as hard as you can [name]!"
p "Hold on tight Doris, when I start, I won't be able to stop pummelling that warm fuckhole of yours!"
scene dorisdoggy02 with dissolve
$ renpy.pause(1.0, hard=True)
do "FUCKKKK! It's so fucking BIG!"
label DorisDoggyDay07b:
play sound "Sounds/dorisdoggy.mp3"
scene dorisdoggy01 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy02 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy01 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy02 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy01 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy02 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy01 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy02 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy01 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy02 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy01 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy02 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy01 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy02 with dissolve
$ renpy.pause(0.4, hard=True)
scene dorisdoggy01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene dorisdoggy02 with fastdissolve
$ renpy.pause(0.2, hard=True)
stop sound
menu:
    "Repeat":
        do "My pussy has turned into a mush..."
        p "Well, let's turn it into a pulp then."
        jump DorisDoggyDay07b
    "Move on":
        do "You've fucked my pussy raw...."
        p "That was the deal Doris, you knew what you were getting yourself into."
        do "And I LOVED IT. But let's do something else so it can recover a bit..."
        jump DorisFuckChoiceDay07

label DorisCumDay07:
scene dorispredoggy with dissolve
$ renpy.pause(1.0, hard=True)
do "I don't know how I'm ever going to take such a MASSIVE dong up my poor little fuckhole..."
p "You're going to have to be brave and open wide for it..."
do "Alright. I'll do my best."
label DorisFuckSlowDay07:
show dorisfuckslow
play music "Sounds/dorisslow.mp3"
call screen dorisfuckslow07
screen dorisfuckslow07:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("DorisFuckFastDay07") 

label DorisFuckFastDay07:
hide dorisfuckslow
show dorisfuckfast
stop music
play music "Sounds/dorisfast.mp3"
call screen dorisfuckfast07
screen dorisfuckfast07:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("DorisFuckEndDay07")

label DorisFuckEndDay07:
p "I'm about to cum Doris!"
do "I want to feel those massive sperm grenades exploding inside me first, so I'm not moving, you just unload as much as you like [name]!"
stop music
scene doriscum01 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "RHAAA! It's happening, I'm unloading inside your womb!"
do "YES, keep blasting that red-hot boyspunk! There's so much of it, I want to see that monstercock erupting in the flesh!"
scene doriscum02 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
do "There, now I can admire those ENORMOUS geysers of scum your giant cum factories can produce!"
p "Here you go, more of my boyload coming your way Doris! AAAHH!"
scene doriscum03 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
do "COVER me from head to toe in that rich creamy hot load! I'm cumming just watching you, you're so virile! AAAH!"
scene doriscum04 with dissolve
play sound "Sounds/doriscum.mp3"
$ renpy.pause(1.0, hard=True)
do "Let me lick that HUGE cock clean... Even as it's softening, it's still a MASSIVE love muscle with a LOT of surface."
if studwin:
    p "Yeah, I wanted to PROVE that I fully deserved the island's title of Muscle Stud."
if studlose:
    p "Yeah, I should have won that competition, but as you can see, I can fuck you like a true muscle stud anyway!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.6
    linear 1.0 yalign 0.8
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
if studwin:
    do "And you proved it well... Over and over again. A TRUE MUSCLE STUD!"
    p "I'm definitely DA MAN!"
if studlose:
    do "That boy Randy... He's really a tough stud to beat. But you almost won, you're MY Muscle Stud [name]!"
if (gymmember == False):
    $ gymmember = True
$ dorisfucked = True
if (dorisjosewin == False):
    p "(She didn't notice I took a picture of my cock in her tight arse... Now I'll send it to José)."
    $ doriswin = True 
$ backdoor += 1
if (backdoor >= 12) and (achievement.has("banger") == False):
    window hide
    show achievement19:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement19
    $ achievement.grant("banger")
do "I'm gonna go to the shower now, no boys allowed in our locker room, remember!"
p "I'd better get going too then..."
$ hour += 1
jump DowntownChoiceDay07b
label DaniellaFuckDay07:
stop music
scene predaniella01 with dissolve
$ renpy.pause(1.0, hard=True)
da "So, what do you think? Can you handle THAT muscled body?"
p "Yeah, I can handle it, I'm da MAN! And now DA MUSCLE STUD!"
scene predaniella02 with dissolve
$ renpy.pause(1.0, hard=True)
da "Since you won the Mr Muscle Stud competition [name], you get to choose what we do next..."

label DaniellaFuckChoiceDay07:
menu:
    "Give me a blowjob as a reward for being DA MUSCLE STUD MAN!" if (daniellaoral == False):
        da "Of course [name], it's fully deserved after all..."
        jump DaniellaOralDay07
    "Anal is in order. I order anal please." if (daniellaanal == False):
        play sound "Sounds/danielladestroyed.mp3"
        $ renpy.pause(1.0, hard=True)
        da "Oh my God, my tight little butthole is really going to take a pounding isn't it?"
        p "You got that right."
        jump DaniellaAnalDay07
    "I'll spoon you and feed you... MY DONG!" if (daniellaside == False):
        da "I can't wait to feel that log inside me [name]!"
        jump DaniellaSideDay07
    "I'm gonna fuck you from behind until I blast my powerful load all over you!" if (daniellaoral == True) and (daniellaanal == True) and (daniellaside == True):
        da "Of fuck, I'm in for a MASSIVE dose of teenage cum then, hey?"
        p "Yep, you sure are."
        jump DaniellaCumDay07

label DaniellaOralDay07:
$ daniellaoral = True
scene daniellabj01 with dissolve
$ renpy.pause(1.0, hard=True)
da "I think I'm going to have a LOT of fun with THIS muscle of yours [name]."
p "And I'm going to have a lot of fun with that mouth of yours Daniella!"
scene daniellabj02 with dissolve
$ renpy.pause(1.0, hard=True)
da "I can see you are really excited about me giving you a blowjob. Your precum is already DROOLING from your spermtube..."
p "That's cos you're making me so HORNY Daniella!"
scene daniellabj03 with dissolve
$ renpy.pause(1.0, hard=True)
da "Let me lick that delicious pre-spunk... Mmmh, so tasty!"
p "Please suck me off, I can't wait to feel your mouth wrapped around my dong!"
da "You're sssoo excited aren't you?"
label DaniellaOralDay07b:
play music "Sounds/hardsucking.mp3"
scene daniellabj04 with dissolve
$ renpy.pause(1.0, hard=True)
scene daniellabj05 with dissolve
$ renpy.pause(1.0, hard=True)
scene daniellabj04 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj04 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj04 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj04 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj04 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj04 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj04 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj04 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj04 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj04 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj05 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj04 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellabj05 with fastdissolve
$ renpy.pause(0.4, hard=True)
stop music
menu:
    "Repeat":
        scene daniellabj01 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "You want more of my warm mouth around that fat fuckpole?"
        p "Yes please Daniella!"
        jump DaniellaOralDay07b
    "Move on":
        scene daniellabj01 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "I sure had fun with that fat fuckstick filling up my belly with warm precum..."
        p "Every good thing must end. With an even BETTER thing starting!"
        da "And what BETTER thing do you have planned [name]?"
        jump DaniellaFuckChoiceDay07

label DaniellaAnalDay07:
$ daniellaanal = True
scene daniellapreanal with dissolve
$ renpy.pause(1.0, hard=True)
p "Are you ready to get your butthole stretched out by a muscle stud's cock?"
da "Oh Lord, have mercy... Go on, do your deed and shove it in [name]!"                                                                
scene daniellaanal01 with dissolve
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
da "Oh, you're stretching my tight butthole so much..."
p "Wait for the rest of my alpha-studcock..."
scene daniellaanal02 with dissolve
$ renpy.pause(1.0, hard=True)
da "AAAH! You're so brutal, but it feels so good! Keep pumping that fat pole inside my backdoor [name]!"
label DaniellaAnalDay07b:
play music "Sounds/daniellaanal.mp3"
scene daniellaanal01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal02 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene daniellaanal02 with fastdissolve
$ renpy.pause(0.4, hard=True)
stop music
scene daniellaanal03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oh damn, you're gripping on my shaft so tight, I just can't hold back, I've got some cum coming your backdoor way! AAAHH!!!!"
da "Wow, I'm so proud my arse is THAT irresistible to your young donkey-cock!"
stop music
menu:
    "Repeat":
        da "Oh, you want MORE of that tight arse don't you? Even after you just dumped a load in it? Then go for it [name]!"
        jump DaniellaAnalDay07b
    "Move on":
        da "Ooh, my tender butthole is finally going to have a respite..."
        p "But some other hole isn't."
        da "What do you have planned for me next?"
        jump DaniellaFuckChoiceDay07

label DaniellaSideDay07:
$ daniellaside = True
scene daniellapreside with dissolve
$ renpy.pause(1.0, hard=True)
p "Let me prep your pussy by coating it with my precum..."
da "This is so hot... Your precum is sssoo abundant, it's like you're PISSING sex slime!"
p "I think there's enough now..."
da "Then RAM your giant boymeat inside my hungry fuckhole [name]!"
scene daniellaside01 with dissolve
$ renpy.pause(1.0, hard=True)
da "Oh, FUCK! That's DEEP!"
p "Hold on steady Daniella, that's not even half of it, I'm gonna take full fifteen-inch strokes now!"
da "YES, I can't wait for this! GO on!"
scene daniellaside02 with dissolve
$ renpy.pause(1.0, hard=True)
da "Damn, that's sssooo DEEP!"
label DaniellaSideDay07b:
play music "Sounds/daniellafuckside.mp3"
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
stop music
menu:
    "Repeat":
        da "I don't know if my pussy can take much more of that brutal pounding but I WANT more!"
        p "And more you shall have Daniella."
        jump DaniellaSideDay07b
    "Move on":
        da "Please give my poor pussy a break... Let's switch position."
        p "Sure, I can think of many other things we can do..."
        da "Like what?"        
        jump DaniellaFuckChoiceDay07
                
label DaniellaCumDay07:
scene daniellapremoviefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
da "I can feel your cock on my butt. It's so HEAVY! It must weigh a TON!"
p "Several pounds of boymeat for you Daniella!"
da "Fuck me hard with your monster pole [name] I want it in me NOW!"
scene daniellapremoviefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
da "AAAH! It's so fucking BIG!"
p "You asked for it. And now you shall receive."
label DaniellaFuckSlowDay07:
show daniellafuckslow
play music "Sounds/daniellafuckmovie.mp3"
call screen daniellafuckslow07
screen daniellafuckslow07:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("DaniellaFuckFastDay07") 

label DaniellaFuckFastDay07:
hide daniellafuckslow
show daniellafuckfast
call screen daniellafuckfast07
screen daniellafuckfast07:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("DaniellaFuckEndDay07") 

label DaniellaFuckEndDay07:
p "Ready to take the full brunt of my sperm pellets deep inside your pussy Daniella?"
da "I am as ready as I ever will be, with such a monster dong lodged so deep inside my tender fuckhole!"
stop music
scene daniellacum01 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "RHAAA! I'm cumming!!!"
da "Fill me up with a MONSTER load [name], I want my womb to be DROWNING in your creamy spunk!"
scene daniellacum02 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "FUCK, I can't STTTOOOPPP! AAAH!"
da "I'm already bloated with your sperm and you're STILL going?"
scene daniellacum03 with dissolve
$ renpy.pause(1.0, hard=True)
da "My God, you really churned up a LOT of rich viscous boycream for me, didn't you MUSCLE STUD?"
p "Yeah, I wanted to PROVE that I fully deserve the island's title of Muscle Stud."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.4
    linear 1.0 yalign 0.6
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
scene daniellaprefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
da "Well, you did... And you now have a LIVE membership to this fitness club [name]! And an open invitation to my pussy! (wink)"
if (gymmember == False):
    $ gymmember = True
$ daniellafucked = True
if (daniellajosewin == False):
    p "(She didn't notice I took a picture of her pussy leaking with my cum... Now I'll send it to José)."
    $ daniellawin = True 
$ backdoor += 1
if (backdoor >= 12) and (achievement.has("banger") == False):
    window hide
    show achievement19:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement19
    $ achievement.grant("banger")
da "I'm gonna go to the shower now, no boys allowed in our locker room, remember!"
p "I'd better get going too..."
$ hour += 1
jump DowntownChoiceDay07b

label FoursomeDay07:
p "Since I'm already naked, it's only fair you girls get undressed too..."
da "I thought you'd never ask... I'll get out of this outfit in no time, I'm so horny..."
scene gangbangpre01 with dissolve
$ renpy.pause(1.0, hard=True)
ar "I'm getting out my trunks too if you don't mind ladies... It's starting to get cramped down there..."
do " That's cos you must have a HUGE muscle cock Arnie!"
ar "You think so? Why don't you come and check for yourself Doris..."
do "Mmmh, I can't wait... Let me get down on my knees to get a better view as you reveal your mammoth Austrian meatpole..."
scene gangbangarnie01 with dissolve
$ renpy.pause(1.0, hard=True)
do "Of Fuck Arnie, your cock... It's so fucking THICK and VEINY! And to think you are over 70yo..."
ar "And I'm not even fully hard yet, so get working on it Doris..."
scene gangbangarnie02 with dissolve
$ renpy.pause(1.0, hard=True)
ar "Yeah, that's good. Now I'm nice and hard and ready for your thick lips around my Austrian bratwurst."
do "It must be well over a FOOT of thick HARD cock! Yummy!"
ar "15 inches, the same size I was at 13 when I won my first bodybuilding contest!"
da "Damn, you must have fucked a lot of happy MILFs with that log back then Arnie! Let's watch the show as a warming-up [name]..."
scene gangbangarnie03 with dissolve
$ renpy.pause(1.0, hard=True)
ar "For sure, I was well known in Austria as the Wunderkid with the grosse Schwanze!"
do "Then let me wrap my lips around that fat meatpole, I'll make you cum in no time Arnie!"
ar "Wunderbar! Let's get you out of those panties and on your knees sucking my fat knob!"
scene gangbangarnie04 with dissolve
$ renpy.pause(1.0, hard=True)
ar "You're doing good Doris, stretch that mouth and swallow my giant dong."
do "MMMggllb."
scene gangbangarnie05 with dissolve
$ renpy.pause(1.0, hard=True)
ar "Damn woman, muscled ladies are so flexible, you're gulping down almost a foot of my fat dick!"
da "She's a pro, but so am I Arnie..."
ar "I'll be sure to test that later on Daniella... But for now..."
label GangBangDaniellaDay07b:
play music "Sounds/hardsucking.mp3"
scene gangbangarnie04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05
$ renpy.pause(0.3, hard=True)
scene gangbangarnie04
$ renpy.pause(0.3, hard=True)
scene gangbangarnie05
$ renpy.pause(0.3, hard=True)
stop music
ar "That's it, swallow my first load... I'm going to give you a healthy Arnie cum meal! RHAAA!"
scene gangbangarnie06 with dissolve
play sound "Sounds/mancum.mp3"
$ renpy.pause(1.0, hard=True)
ar "That's a good girl, swallow it down... Wait, there's still some more... AAAH, so gooood!"
scene gangbangarnie07 with dissolve
$ renpy.pause(1.0, hard=True)
ar "You did well Doris! Now you can lick off the last dollop that's hanging from my cocktip and clean my dong."
do "And you're still hard and ready for some more HOT action! As studly as an older man could ever hope to be Arnie!"
p "Now let's do something else, I want in on the action!"
da "Then let's show you what WE have in store for you guys..."
scene pregangbang01 with dissolve
$ renpy.pause(1.0, hard=True)
da "So, what do you guys think? Can you handle THAT?"
do "Are our bodies hot enough for two STUDS like you?"
p "Yeah, I can handle both of you, I'm da MAN!"
ar "And I used to be da Man but I can still please the ladies, as you can see..."
scene pregangbang02 with dissolve
$ renpy.pause(1.0, hard=True)
da "We don't doubt it Arnie... That cock of yours... It's everything the thousands of fitness girls you've fucked have been raving about on socal media."
do "And now, it's OUR turn since you're on OUR island!"
ar "I'm glad I came! And... I'll be back!"
da "Since you won the Mr Muscle Stud competition [name], you get to choose what we do next..."

label GangBangChoiceDay07:
menu:
    "Get sucked by Daniella while Arnie rams her from behind" if (foursomeoral == False) and (foursomedoggy == False):
        da "I hope I can open my mouth wide enough for that MONSTER log Mr Muscle Stud!"
        p "It will be tough but it will fit."
        jump GangBangOralDay07
    "Now I'll be the one getting sucked by Daniella while Arnie rams her from behind" if (foursomeoral == False) and (foursomedoggy == True):
        da "I hope I can open my mouth wide enough for that MONSTER log Mr Muscle Stud!"
        p "It will be tough but it will fit."
        jump GangBangOralDay07
    "Fuck Daniella doggy-style while Arnie rams his cock down her throat" if (foursomedoggy == False)and (foursomeoral == False):
        da "MMmh, a sandwich from both ends, just what I was craving for..."
        jump GangBangDoggyDay07
    "Now I'll be the one fucking Daniella doggy-style while Arnie rams his cock down her throat" if (foursomedoggy == False) and (foursomeoral == True):
        da "MMmh, a sandwich from both ends, just what I was craving for..."
        jump GangBangDoggyDay07
    "I want to have some one-on-one special time with Doris' backdoor!" if (foursomedoris == False):
        do "My backdoor you said? Ooooh, I'm ready for your monstercock STUD!"
        jump GangBangDorisDay07
    "I want to have some one-on-one special time with Daniella's pussy!" if (foursomedaniella == False):
        da "I'm honored... Getting fucked by the island's ultimate STUD!"
        jump GangBangDaniellaDay07
    "Get on with the grand gangbang finale!!" if (foursomedoris == True) and (foursomeoral == True) and (foursomedoggy == True) and (foursomedaniella == True):
        jump GangBangCumDay07

label GangBangOralDay07:
$ foursomeoral = True
scene gangbangsuck01 with dissolve
$ renpy.pause(1.0, hard=True)
da "Mmmmh, that cock is sssoo thick down my throat...."
p "And your mouth is so warm around my meatpole Daniella!"
do "What about my feet [name]?"
p "Oh yeah, love their feel around my shaft...."
window hide
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
scene gangbangsuck03 with dissolve
play music "Sounds/foursomesuck.mp3"
$ renpy.pause(1.0, hard=True)
p "Fuck! Your throat is really deep!"
scene gangbangsuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck03 with fastdissolve
$ renpy.pause(0.3, hard=True)
do "Fuck her hard Arnie, while I pump [name]'s rod with my feet!"
scene gangbangsuck02 with dissolve
$ renpy.pause(1.0, hard=True) 
ar "I'm at full thrust back here, don't worry Doris!"
stop music
play sound "Sounds/foursomefuck01.mp3"
scene gangbangsuck04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck04 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene gangbangsuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
da "FUUUUCK! Getting rammed both ends by GIANT monstercocks!"
scene gangbangsuck01 with fastdissolve
$ renpy.pause(1.0, hard=True)
stop music
p "Maybe it's time we switch position before my STUDCOCK dislocates your jaws!"
do "And what would you like to do next [name]?"
jump GangBangChoiceDay07

label FoursomeSuckDay07b:
#play music "Sounds/chantelleblow02.mp3"

stop music
menu:
    "Repeat":
        p "Let's keep going, my cock is on fire!"
        da "And my MOUTH is on fire too!"
        jump FoursomeSuckDay07b
    "Move on":
        do "You guys fucked us so good... But we want MORE!"
        p "Then MORE you shall have."        
        scene pregangbang02 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "And what will that be?"      
        jump GangBangChoiceDay07

label GangBangDoggyDay07:
$ foursomedoggy = True
scene daniellafoursome01 with dissolve
$ renpy.pause(1.0, hard=True)
do "Damn, Daniella, I can see over a foot of [name]'s cock sticking out of your pussy... You're going to get rammed DEEP!"
ar "From both ends, I'll force my dong down her throat at the same time that [name] plunges his giant teenage cock inside her fuckhole..."
p "You got that right Arnie! Let's be DA MEN on Daniella!"
scene daniellafoursome02 with dissolve
$ renpy.pause(1.0, hard=True)
p "There you go, it went in nice and easy..."
play sound "Sounds/moaning.mp3"
da "AAAAH!"
ar "Same thing my end, her throat is really flexible..."
scene daniellafoursome03 with dissolve
$ renpy.pause(1.0, hard=True)
do "Watching you boys fuck her like beasts... It's making me all wet down there..."
p "You ain't seen nothing yet Doris."
label GangBangDoggyDay07b:
scene daniellafoursome01 with dissolve
play music "Sounds/foursomefuck02.mp3"
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01
$ renpy.pause(0.3, hard=True)
scene daniellafoursome02
$ renpy.pause(0.3, hard=True)
scene daniellafoursome01
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        da "Please be gentle, you guys are destroying my holes from both ends..."
        p "You're a pro, you can take it..."
        jump GangBangDoggyDay07b
    "Move on":
        scene daniellafoursome04 with dissolve
        $ renpy.pause(1.0, hard=True)
        ar "I'd like her to lick my balls before if you don't mind... While I rest my shaft on her head like that..."
        play sound "Sounds/lick.mp3"
        da "They are just so delicious.... And I bet FULL of cum for us!"
        p "Let's move on girls, We're not done with you yet."
        stop sound
        scene pregangbang02 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "And what do you have planned for us next?"
        jump GangBangChoiceDay07
                
label GangBangDorisDay07:
$ foursomedoris = True
scene dorispreanal with dissolve
$ renpy.pause(1.0, hard=True)
p "First, I'll let some precum drip down your backside."
do "So thoughtful of you. It certainly needs to be WELL lubricated."
p "Ready to get impaled by the island's Muscle Stud's cock Doris?"
do "YES! Just RAM IT IN STUD!"
scene dorisanal01 with dissolve
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
do "Oh, you're stretching my tight butthole so good..."
p "Wait for the rest of my alpha-studcock..."
scene dorisanal02 with dissolve
$ renpy.pause(1.0, hard=True)
do "AAAH! You're so brutal, but it feels so good! Keep pumping that fat pole inside my backdoor [name]!"
label DorisFoursomeDay07b:
play music "Sounds/dorisanal.mp3"
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene dorisanal02 with fastdissolve
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        do "Oh, you want MORE of that tight arse don't you? Then go for it [name]!"
        jump DorisFoursomeDay07b
    "Move on":
        do "Ooh, my tender butthole is finally going to have a respite..."
        p "That's cos my cock demands some other hole!"
        scene pregangbang02 with dissolve
        $ renpy.pause(1.0, hard=True)
        do "And what do you have planned for us next?"
        jump GangBangChoiceDay07

label SaunaUpDay07:
$ saunaup = True
ar "So, which girl do you want to bang first [name]?"
menu:
    "Doris":
        $ dorisfirst = True
        da "Alright, but be quick with her, I want to feel that monster teenage log in my tight pussy real quick!"
        ar "Calm down ladies, there's enough cock for both of you..."
        jump DorisUpDay07
    "Daniella":
        $ daniellafirst = True
        do "Bang her good and hard [name]. I want your cock to be at maximum STUD POWER when my turn comes!"
        ar "Calm down ladies, you'll both get plenty of cockmeat in turn..."
        jump DaniellaUpDay07
label DorisUpDay07:
scene dorisup01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready for impalement? Impalement in three... two... one..."
scene dorisup02 with dissolve
$ renpy.pause(1.0, hard=True)
do "Oh FUCK! It's so MASSIVE!"

label DaniellaUpDay07:
scene dorisup01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready for impalement? Impalement in three... two... one..."
scene dorisup02 with dissolve
$ renpy.pause(1.0, hard=True)
da daniellaprite "Oh FUCK! It's so MASSIVE!"

label GangBangDaniellaDay07:
$ foursomedaniella = True
scene daniellapreside with dissolve
$ renpy.pause(1.0, hard=True)
p "Let me prep your pussy by coating it with my precum..."
da "This is so hot... Your precum is sssoo abundant, it's like you're PISSING sex slime!"
p "I think there's enough now..."
da "Then RAM your giant boymeat inside my hungry fuckhole [name]!"
scene daniellaside01 with dissolve
$ renpy.pause(1.0, hard=True)
da "Oh, FUCK! That's DEEP!"
p "Hold on steady Daniella, that's not even half of it, I'm gonna take full fifteen-inch strokes now!"
da "YES, I can't wait for this! GO on!"
label DaniellaFoursomeDay07b:
scene daniellaside02 with dissolve
$ renpy.pause(1.0, hard=True)
da "Damn, that's sssooo DEEP!"
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.3, hard=True)
scene daniellaside02
$ renpy.pause(0.3, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
scene daniellaside01
$ renpy.pause(0.2, hard=True)
scene daniellaside02
$ renpy.pause(0.2, hard=True)
stop sound
menu:
    "Repeat":
        da "I don't know if my pussy can take much more of that brutal pounding but I WANT more!"
        p "And more you shall have Daniella."
        jump DaniellaFoursomeDay07b
    "Move on":
        da "Please give my poor pussy a break... Let's switch position."
        p "Sure, I can think of many other things we can do..."
        scene pregangbang02 with dissolve
        $ renpy.pause(1.0, hard=True)        
        da "Like what?"        
        jump GangBangChoiceDay07

label GangBangCumDay07:
scene pregangbang02 with dissolve
$ renpy.pause(1.0, hard=True)
da "And now for the Grand Finale. We want both of you to PLASTER us in your hot thick cum!"
ar "Are you ready for that [name]? Cos I'm dying to ERUPT all over those hotties!"
p "Of course, my dong is ready to conquer the island with my STUD cum!"
da "Then come and fuck me while Daniella sucks a thick load out of Arnie!"
label GangbangSlowDay07:
show gangbangslow
play music "Sounds/foursomemovie.mp3"
call screen gangbangslow01
screen gangbangslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("GangbangFastDay07") 

label GangbangFastDay07:
hide gangbangslow
show gangbangfast
call screen gangbangfast01
screen gangbangfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("GangbangEndDay07")

label GangbangEndDay07:
p "I'm going to UNLOAD NOW! RHAAA!"
stop music
scene gangbangcum01 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(3.0, hard=True)
da "Oh my God! I can see [name] shooting MONSTER WADS all over your back Doris!"
do "And he's already filled me up with OUNCES of boycum!"
scene gangbangcum02 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(3.0, hard=True)
p "There's MORE where that came from ladies! AAAAH!"
do "I can feel your HUGE splashes of ball-batter all over my arse. Mmmmh, I LOVE IT [name]!"
ar "I'm about to unload too! Daniella, get ready to receive a HEAVY dose!"
da "Fuck yeah, two MUSCLE STUDS erupting at the same time all over us!"
do "Keep going boys, we want to be CAKED in your red-hot cream!"
scene gangbangcum03 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(2.0, hard=True)
da "Ooh, Arnie, I didn't know a man your age could cum so MUCH!"
do "And [name] keeps blasting even bigger spunk volleys all over me, it's raining cum!"
play sound "Sounds/mancum.mp3"
$ renpy.pause(0,5, hard=True)
play music "Sounds/bothcum.mp3"
$ renpy.pause(3.0, hard=True)
ar "Damn, here's the last of my governor's load you horny sluts!"
stop music
da "I love it when the muscles of a true ALPHA-COCKSMAN are tensed up after a monster cumblast!"
do "And you, boy, you came plenty already during the contest, but KEEP GOING! We want MORE from the island's Muscle Stud!"
scene gangbangcum04 with dissolve
play sound "Sounds/mancum.mp3"
play music "Sounds/cumming.mp3"
$ renpy.pause(3.0, hard=True)
p "FUCK! Take these last cumshots, RHAAAA!"
do "Let me suck out the after dregs, there's more spunk in just one dollop from you than a normal man's full load..."
stop music
da "Mmmh, Arnie, your cum is so tasty...."
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.4
    linear 1.0 yalign 0.6
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ threesome += 1
if (tanyafucked == True) and (nikkifucked == True) and (achievement.has("brickhouse") == False):
    window hide
    show achievement22:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement22
    $ achievement.grant("brickhouse")
if threesome >= 4 and (achievement.has("threesomer") == False):
    window hide
    show achievement23:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement23
    $ achievement.grant("threesomer")
$ backdoor += 1
if (backdoor >= 12) and (achievement.has("banger") == False):
    window hide
    show achievement19:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement19
    $ achievement.grant("banger")
da "We'll head for the locker room showers now, no boys allowed! (wink)..."
ar "I spotted some hot fitness MILF in the gym, so if you'll excuse me ladies..."
do "Come back and visit us anytime you want Arnie!"
ar "I'll BE BACK."
p "Hey, what about me?"
da "Of course, you now have a LIVE membership to this fitness club [name]! And an open invitation to our pussies! (wink)"
if (gymmember == False):
    $ gymmember = True
$ dorisfucked = True
if (dorisjosewin == False):
    p "(Doris didn't notice that I took a picture of my cock in her tight pussy... Now I'll send it to José)."
    $ doriswin = True 
$ daniellafucked = True
if (daniellajosewin == False):
    p "(Daniella didn't notice that I took a picture of her mouth wrapped around my knob... Now I'll send it to José)."
    $ daniellawin = True 

if annafucked and brittanyfucked and chantellefucked and chiyofucked and daniellafucked and debbyfucked and dorisfucked and francinefucked and friedafucked and hallefucked and jenniferfucked and katefucked and katsumifucked and laurafucked and maddyfucked and mariafucked and nancyfucked and nikkifucked and pamelafucked and sandyfucked and sophiafucked and tanyafucked and teaganfucked and vivianefucked and (achievement.has("conqueror") == False):
    window hide
    show achievement17:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement17
    $ achievement.grant("conqueror")
if annawin and brittanywin and chantellewin and chiyowin and daniellawin and debbywin and doriswin and francinewin and friedawin and hallewin and jenniferwin and katewin and katsumiwin and laurawin and maddywin and mariawin and nancywin and nikkiwin and pamelawin and sandywin and sophiawin and tanyawin and teaganwin and vivianewin and (achievement.has("ultimate") == False):
    window hide
    show achievement24:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement24
    $ achievement.grant("ultimate")
$ hour += 1
jump DowntownChoiceDay07b

label DinnerDay07:
stop music
scene dinnerday03a with dissolve
$ renpy.pause(1.0, hard=True)
m "Enjoy your meal kids!"
s "Thanks mom, it looks delicious as always!"
m "So, how was your day? Did you do something interesting on your first day off school on Veri-Bosti?"
scene dinnerday03b
s "I hung out with Chantelle downtown, we went to the movies and did some shopping."
m "That sounds exciting!"
menu:
    "I won the Muscle Stud 2020 competition. It means I'm the biggest muscle stud on the island." if studwin == True:
        scene dinnerday03a
        m "Ooh, my little tenant has the biggest MUSCLES on the island? I'm VERY proud."
        if lust_points[16] == 9:
            $ lust_points[16] +=1
            $ score +=1
            show lust01:
                xalign 0.6 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        if lust_points[16] <= 8:
            $ lust_points[16] +=2
            $ score +=2
            show lust02:
                xalign 0.6 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust02
            if (lust_points[16] == 10):
                show epiclust:
                    xalign 0.6 yalign 0.2
                    zoom 0.5
                    linear 2.0 zoom 1.0
                play sound "Sounds/epiclust.mp3"
                $ renpy.pause(4.0, hard=True)
                hide epiclust
                m "I wants to spend the evening with my muscle stud tenant... We could watch a movie? Would you like that [name]?"
                p "Sure Nancy! I already have a movie in mind..."
                $ mommovie07 = True
                show dinnerday03c
                s "Good, so you'll leave Chantelle and me alone for our sleepover then."
                p "I would never have intruded."
                jump DinnerDay07b            
        p "Don't forget I'm also the biggest STUD."
        s "What the hell does that even mean? How can they decide such a thing?"
        if josenikkicockblocked == False:
            p "Well..err... Suffice to say José has nothing on me. He's a total wimp and lost big time. You shouldn't even talk to the loser."
            s "I guess you're right, he promised me he would win. What a liar and a lOSER!"
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
        if josenikkicockblocked == True:
            p "Well...err... Suffice to say José has nothing on me. He's a total wimp and lost big time. I told you this loser wans't worth your time."
            
            s "I guess you're right, he promised me he would win earlier this week. What a liar and a lOSER!"
        jump DinnerDay07b        
    "I competed in the Muscle Stud 2020 competition. I almost won but I'm sure the guy who beat me at the end cheated." if studwin == False:
        m "Ooh, I'm so sorry to hear that. I'm sure you'll get there eventually my little pumpkin."
        p "Yeah, next year, I'll be the island's MUSCLE STUD for sure!"
        s "And no one will be there to witness it since this game ends tomorrow."
        jump DinnerDay07b
    
label DinnerDay07b:
m "Now finish up your meal, and don't forget to do the dishes afterwards!"
show dinnerday04b
s "Sure mom, I'll do the washing and [name] will do the drying, as usual... "
hide dinnerday04b
show dinnerday03c
s "Cos we can't trust him with cleaning up the dishes properly..."
p "My hands can't get wet. I need to maintain a firm grip on...err... my dumbbells."
if (mommovie07 == False):
    "You finish cleaning up the dishes and head to your room."
    $ hour += 1
    jump EveningChoiceDay07
if (mommovie07 == True):
    "You finish cleaning up the dishes and head to the living room."
    $ hour += 1
    jump EveningMomDay07

label EveningMomDay07:
scene eveningtvmom01 with dissolve
$ renpy.pause(1.0, hard=True)
m "What movie should we watch tonight? Do you have an idea sweetie?"
p "Let's watch Conan the Barbarian."
m "Alright, anything for you tonight my little pumpkin."
scene eveningconan with dissolve
play music "Sounds/conan.mp3"
$ renpy.pause(2.0, hard=True)
$ hour += 1
m "This movie is terrible, but I liked the beginning, where the muscle kid with the big bulge grows up... It made me horny [name]!"
stop music
scene ryanconanposing02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Look Nancy, I'm just like him, only with a MUCH bigger bulge!"
m "It looks so big.... and not even hard. I know it's wrong but I NEED to feel up that monster!"
scene eveningmomstrap with dissolve
$ renpy.pause(1.0, hard=True)
m "Mmmh, honey, this is the biggest thing I've ever felt in my life... My tiny hands can't even wrap around your giant boycock. Let me see it please, I beg you!"
p "I'm getting really hard watching you worshipping my bulge like that... FUCK!"
scene eveningmomrip with dissolve
play sound "Sounds/rip.mp3"
$ renpy.pause(1.0, hard=True)
m "Oh my God! Your massive rock-hard cock just ripped right through your jockstrap!"
p "That's cos you're making me so horny Nancy... Please take off your blouse... I'll turn the lights on..."
m "I don't know... It's just so wrong... Just a peek for my horse-hung muscle stud then!"
scene eveningmomfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
m "You like what you see [name]? What would you like me to do next my studly tenant?"
if stamina >= 1:
    menu:
        "I need to stick my cock between those big jugs...":
            jump MomTitfuckDay07
        "I don't know but I'm about to explode!":
            jump MomBlowjobDay07
if stamina == 0 and whitebull == False:
    p "Err... I think this is wrong. I mean, it's landlady sex, right? That's definitely wrong."
    m "What the hell are you talking about? Are you chickening out NOW?"    
    $ lust_points[16] -=1
    $ score -=1
    show lustminus01:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    m "And I'm taking that epiclust icon back too. Now I'm going to bed, you've ruined the mood..."
    jump EveningChoiceDay07
if stamina == 0 and whitebull:
    p "(I guess this is as good a time as ever to drink that White Bull energy drink..."
    show whitebull
    show square
    play sound "Sounds/lost.mp3"
    "You gulped down your White Bull energy drink."
    hide square
    hide whitebull
    $ whitebull = False
    $ stamina += 2
    menu:
        "I need to stick my cock between those big jugs...":
            jump MomTitfuckDay07
        "I don't know but I'm about to explode!":
            jump MomBlowjobDay07

label MomTitfuckDay07:
$ nancytitfuck07 = True
scene momtitfuck01 with dissolve
m "Of course [name]. I will take care of that monster with my huge jugs, you just relax and let me do all the work."
label MomTitfuckDay07b:
#play sound "Sounds/momtitfuck.mp3"            
window hide
$ renpy.pause(1.0, hard=True)
scene momtitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene momtitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene momtitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene momtitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene momtitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene momtitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene momtitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene momtitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene momtitfuck02
$ renpy.pause(0.3, hard=True)
scene momtitfuck01
$ renpy.pause(0.3, hard=True)
scene momtitfuck02
$ renpy.pause(0.3, hard=True)
scene momtitfuck01
$ renpy.pause(0.3, hard=True)
scene momtitfuck02
$ renpy.pause(0.3, hard=True)
scene momtitfuck01
$ renpy.pause(0.3, hard=True)
scene momtitfuck02
$ renpy.pause(0.3, hard=True)
scene momtitfuck01
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump MomTitfuckDay07b
    "Move on":
        pass
if (stamina >=2):
    menu: 
        "Cum, you've got another load for later":
            jump MomTitfuckCumDay07            
        "Don't cum yet and tell her you're about to explode":
            m "Oh sweetie, your huge cock looks like it's ready to explode!"
            if (nancyblowjob07 == False):
               m "Bring that massive fuckstick to my mouth [name]!"
               jump MomBlowjobDay07
            else: 
                m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
                jump MomPussyLickDay07
if (stamina <=1):
    m "Oh sweetie, your huge cock looks like it's ready to explode!"
    if (nancyblowjob07 == False):
        m "Bring that massive fuckstick to my mouth [name]!"
        jump MomBlowjobDay07
    else: 
        m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
        jump MomPussyLickDay07            

label MomTitfuckCumDay07:
scene momtitfuckcum01 with dissolve
play sound "Sounds/ryancumming.mp3"            
$ renpy.pause(2.0, hard=True)
scene momtitfuckcum02 with dissolve
#play sound "Sounds/momtitfuckcum.mp3"            
$ renpy.pause(1.0, hard=True)
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.4
    linear 1.0 yalign 0.6
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
m "Damn [name], you really had a lot of pent-up cum stored in those huge balls..."
if (nancyblowjob07 == False):
    m "Bring that massive fuckstick to my mouth [name]!"
    jump MomBlowjobDay07
else: 
    m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
    jump MomPussyLickDay07

label MomBlowjobDay07:
$ nancyblowjob07 = True
scene momblowjob01 with dissolve
#play sound "Sounds/momlick01.mp3"  
$ renpy.pause(1.0, hard=True)
m "My God [name], your cock... It's just GIGANTIC! I can't even wrap my fingers around its incredible girth..."
scene momblowjob01b with dissolve
#play sound "Sounds/momlick02.mp3"  
$ renpy.pause(1.0, hard=True)         
m "Mmmh... And those balls... So HEAVY, I just have to taste them..."         
label MomBlowjobDay07b:
scene momblowjob02 with dissolve
play sound "Sounds/hardsucking.mp3"            
$ renpy.pause(0.3, hard=True)
scene momblowjob03 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob02 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob03 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob02 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob03 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob02 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob03 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob02 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob03 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob02 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob03 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob02 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob03 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob02 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
scene momblowjob03 with Dissolve(0.3, alpha=True)
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump MomBlowjobDay07b
    "Move on":
        pass

m "Oh sweetie, your huge cock looks like it's ready to explode!"
if (nancytitfuck07 == False):
    m "Why don't you stick your pud between my big tits?"
    jump MomTitfuckDay07
if (nancytitfuck07 == True):
    m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
    jump MomPussyLickDay07            
 
label MomPussyLickDay07:
scene eveningmomclit with dissolve
#play sound "Sounds/momclit.mp3"
$ renpy.pause(1.0, hard=True)
m "Mmmh, you do that so well sweetie! You really know what you're doing! AAAH!"
m "Now it's time for me to reward you... With my pussy!"
jump MomFullFuckDay07

label MomFullFuckDay07:
scene eveningmomready with dissolve
#play sound "Sounds/momready.mp3"
$ renpy.pause(1.0, hard=True)
m "See my tender pink pussy? It's wet and ready for you my studly tenant! Come and pound it!"
#play music "Sounds/momslowfuck.mp3"
show momfuckslow
show faster
call screen nancyfuckslowday07
screen nancyfuckslowday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("NancyFuckFastDay07")
label NancyFuckFastDay07:
hide faster
stop music
#play music "Sounds/momfastfuck.mp3"
show momfuckfast
show cum
call screen nancyfuckfastday07
screen nancyfuckfastday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("NancyFuckCumDay07")

label NancyFuckCumDay07:
hide momfuckfast
hide momfuckslow
stop music
scene momfuckcum01
play sound "Sounds/cumming.mp3"            
$ renpy.pause(4.0, hard=True)
scene momfuckcum02 with dissolve
#play sound "Sounds/momcum01.mp3"            
$ renpy.pause(1.0, hard=True)
scene momfuckcum03 with dissolve
#play sound "Sounds/momcum02.mp3"            
$ renpy.pause(1.0, hard=True)
$ hour +=1
$ stamina -=1
show staminaminus01:
    xalign 0.3 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
m "Damn [name], you really had a lot of pent-up cum stored in those huge balls..."
m "It's my duty to make sure you empty them regularly so you don't get blue balls and it hurts..."
m "I should go and take a shower, since I'm covered in your red-hot spunk... We'll keep this...incident... between us sweetie."
if (debbyfucked == True) and (nikkifucked == True) and (achievement.has("homesteader") == False):
    show achievement07:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement07
    $ achievement.grant("homesteader")
if (nancyjosewin == False):
    p "Sure Nancy! (She didn't notice I took a picture of us... Now I'll send it to José)."
    $ nancywin = True
if (nancyjosewin == True):
    p "Sure Nancy! (Although everyone already knows you fucked José you slut...)"
if (achievement.has("mfucker") == False):
    show achievement02:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement02
    $ achievement.grant("mfucker")
$ nancyfucked = True
jump EveningChoiceDay07

label SleepoverDay07:
$ nightsisroomseen07 = True
stop music
scene sleepover01 with fade
$ renpy.pause(1.0, hard=True)
s "Hey! Why are you here? This is a girls' sleepover!"
if bothhouseplay == True:
    ch "I wouldn't mind making it a THREESOME sleepover... Like last night..."
    s "Well, I'm horny too actually. So come and fuck us again then [name]!"
    if stamina <= 0:
        p "You misunderstood my intentions. This was merely a cordial visit to bid you good night my fair ladies."
        ch "What the fuck? I bet he's been fucking that slut Brittany today, that's why he can't get it up!"
        p "What? No!"
        s "If you can't satisfy us, then get out of here [name]!"
        p "Gee, I didn't realize girls could be such sex fiends. Boys don't think about sex all the time like you two."
        s "Yeah, right!"
        jump EveningChoiceDay07
    if stamina >= 1:
        p "Alright! Another awesome threesome night! Exactly like yesterday."
        s "Let us put on some lingerie. Exactly the same sets as yesterday actually."
        jump NikkiThreesomeDay07 
ch "I don't mind him being here Nikki. Maybe we can have some fun at his expense..."
show sleepover01b with dissolve
s "What do you have in mind?"
ch "A game of truth or dare..."
menu:
    "I don't want to play this stupid game. How about strip poker instead?":
        scene sleepover01 with dissolve
        $ renpy.pause(1.0, hard=True)
        s "You're such a pervert, really, [name]... Get out of here."
        if lust_points[17] <= 9:
            window hide
            $ lust_points[17] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.2 yalign 0.6
                linear 1.0 yalign 0.8
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
        ch "How disappointing of you..."
        if lust_points[2] <= 9:
            window hide
            $ lust_points[2] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.8 yalign 0.6
                linear 1.0 yalign 0.8
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
        p "Err... Okay, I'll leave you two to it then..."
        jump EveningChoiceDay07
    "Okay, I'm in, I like a challenge!":
        ch "Great, then let's all sit down on the floor in a circle."
        p "A circle jerk?"
        scene sleepover01 with dissolve
        ch "No, not a circle jerk. (sigh)"
scene sleepover02 with dissolve
$ renpy.pause(1.0, hard=True)
ch "I start then, since I had the idea of playing this game..."
ch "Truth or dare [name]?"
menu:
    "Truth.":
        ch " Mmmh, Let me think... Did you fuck Brittany?"
        if brittanyfucked == True:
            p "Err... Maybe... I can't recall. I take the fifth!"
            show sleepover02c
            ch "That's a yes... And a disappointment that you would go for such a bitch."
            if lust_points[2] <= 9:
                window hide
                $ lust_points[2] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.8 yalign 0.6
                    linear 1.0 yalign 0.8
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
            p "It's not my fault. She made me do it!"
            s "Yeah, right. PERV!"
            jump Sleepover02
        if brittanyfucked == False:
            p "Nope. I wouldn't go near that skank. I much prefer nice girls. Like you."
            show sleepovernikkishockeda with dissolve
            s "I don't think he was lying for once..."
            if lust_points[2] <= 9:
                window hide
                $ lust_points[2] +=1
                $ score += 1
                show lust01:
                    xalign 0.8 yalign 0.6
                    linear 1.0 yalign 0.4
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
            jump Sleepover02            
    "Dare.":
        ch " Mmmh, Let me think... Kiss your landlady's daughter on the mouth!"
        show sleepovernikkishockeda with dissolve
        s "What? But.. Chantelle!"
        ch "Come on, I know you want it Nikki, you told me everything, remember?"
        p "I'm in!"
        show sleepovernikkishockedc with dissolve
        s "Of course you're in, you're ALWAYS in."
        scene sleepovernikkikiss with dissolve
        play sound "Sounds/kissing.mp3"
        $ renpy.pause(1.0, hard=True)
        ch "That was... sexy."
        if lust_points[17] <= 9:
            window hide
            $ lust_points[17] +=1
            $ score += 1
            show lust01:
                xalign 0.2 yalign 0.6
                linear 1.0 yalign 0.4
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01    
        jump Sleepover02
label Sleepover02:
scene sleepover02 with dissolve
play sound "Sounds/kissing.mp3"
$ renpy.pause(1.0, hard=True)
p "Now it's MY turn. Nikki, truth or dare?"
s "DARE!"
p "Alright. Why don't you..."
menu:
    "...take your top off.":
        show sleepovernikkishockedc with dissolve
        s "What? That's disgusting! Asking your landlady's daughter to show you her tits!"
        p "Hey! It's the rules of the game Nikki!"
        ch "He's right Nikki."
        show sleepovernikkishockeda with dissolve
        s "Fine, I'll do it... But you really are a PERV."
        scene sleepovernikki01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Now that game is starting to get interesting..."
        scene sleepovernikki02 with dissolve
        $ renpy.pause(1.0, hard=True)
        s "There, happy now?"
        p "Yep."
        $ nikkitopoff = True
        jump Sleepover03
    "...kiss Chantelle.":
        ch "It was to be expected. Boys just love watching women kiss."
        s "Cos they are such PERVERTS!"
        p "It's purely for educational purposes."
        scene sleepoverkissing with dissolve
        play sound "Sounds/kissing.mp3"
        $ renpy.pause(1.0, hard=True)
        s "There, happy now?"
        p "Yep."
        jump Sleepover03

label Sleepover03:
if nikkitopoff:
    scene sleepover02
    show sleepovernikkitopoff
    with dissolve
if nikkitopoff == False:
    scene sleepover02 with dissolve
$ renpy.pause(1.0, hard=True)
s "My turn. For Chantelle. Truth or dare?"
ch "Dare..."
if nikkitopoff:
    show sleepovernikkishockedb with dissolve
    s "Since I'm half-naked, it's only fair that..."
    ch "I take MY top off? *wink*"
    s "That's right."
    scene sleepoverchantelle01
    show sleepovernikkitopoffb
    with dissolve
    $ renpy.pause(1.0, hard=True)
    ch "Alright then... I bet your landboy is going to enjoy this."
    p "Purely for educational purposes."
    scene sleepoverchantelle02
    show sleepovernikkitopoff
    with dissolve
    $ renpy.pause(1.0, hard=True)
    ch "I'll slowly pull it up..."
    p "(Dang, what a fine arse she has...)"
    scene sleepoverchantelle03 with dissolve
    $ renpy.pause(1.0, hard=True)
    ch "To reveal my Triple-D boobies... Like what you see [name]?"
    p "Yes... Yes... I do. Thank you Chantelle."
    jump Sleepover04
if nikkitopoff == False:
    show sleepovernikkishockeda with dissolve
    s "Why don't you... Kiss [name] on the mouth this time..."
    ch "Mmmh. And he'll still have the taste of YOUR kiss on my mouth."
    s "Ah yes, I hadn't thought about that. I'm changing my dare."
    p "What? You can't do that!"
    hide sleepovernikkishockeda
    show sleepovernikkishockedc with dissolve
    s "I can do what I want! You're in MY room, remember?"
    p "Umpf."
    hide sleepovernikkishockedc
    show sleepovernikkishockeda with dissolve
    s "Maybe you should get a little bit... less clothed Chantelle."
    ch "Oh Nikki, that is so bold of you... *wink*"
    p "(Ah, finally, this thing is going somewhere.)"
    scene sleepoverchantelle01 with dissolve
    $ renpy.pause(1.0, hard=True)
    ch "Alright then... I bet your landboy is going to enjoy this."
    p "Purely for educational purposes."
    scene sleepoverchantelle02 with dissolve
    $ renpy.pause(1.0, hard=True)
    ch "I'll slowly pull it up..."
    p "(Dang, what a fine arse she has...)"
    scene sleepoverchantelle03 with dissolve
    $ renpy.pause(1.0, hard=True)
    ch "To reveal my Triple-D boobies... Like what you see [name]?"
    p "Yes... Yes... I do. Thank you Chantelle."
    jump Sleepover04

label Sleepover04:
if nikkitopoff:
    scene sleepover02
    show sleepovernikkitopoff
    show sleepoverchantelletopoff    
    with dissolve
    $ renpy.pause(1.0, hard=True)
    ch "My turn then... Truth or dare [name]?"
    p "Dare of course!"
    ch "MMmh... let me think. Since we're now both half-naked, YOU get to join us and be half-naked too. And show us that BIG BULGE of yours in all its glory!"
    show sleepovernikkishockedb with dissolve
    s "Chantelle!"
    ch "Well, it's only fair. I get to decide. *wink*"
    p "Alright, you asked for it. Prepare to be amazed by the size of my massive manmeat!"
    hide sleepovernikkishockedb
    s "Yeah, yeah, whatever..."
    jump Sleepover04b
if nikkitopoff == False:
    scene sleepover02
    show sleepoverchantelletopoff    
    with dissolve
    $ renpy.pause(1.0, hard=True)
    ch "My turn then... Truth or dare [name]?"
    p "Dare of course!"
    ch "MMmh... let me think. Since I'm half-naked, YOU get to be half-naked too, and show us that BIG BULGE of yours in all its glory!"
    show sleepovernikkishockedb with dissolve
    s "Chantelle!"
    ch "Well, it's only fair. I get to decide. *wink*"
    p "Alright, you asked for it. Prepare to be amazed by the size of my massive manmeat!"
    hide sleepovernikkishockedb
    s "Yeah, yeah, whatever..."
    jump Sleepover04b
    
label Sleepover04b:
if nikkitopoff:
    scene sleepoverryanstrap01a
    show sleepoverryanstrap01b
    with dissolve
    $ renpy.pause(1.0, hard=True)
if nikkitopoff == False:
    scene sleepoverryanstrap01a with dissolve
    $ renpy.pause(1.0, hard=True)
p "There. Amazed yet?"
if nikkifucked and chantellefucked:
    ch "Of course we are... And we BOTH know it can grow MUCH bigger, don't we Nikki?"
    window hide
    show doubledelight:
        xalign 0.4 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/delight.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    p "Hang on. Did I... Just see a double delight here?"
    s "Yes you did [name]. You managed to lure Chantelle and me into your den of depravity with that huge log you're hiding down there."
    ch "And those huge muscles... Your landboy is making me so horny..."
    p "WOO-HOO! Double delight it is then!"
    s "Let us get ready for a HOT night of love with you by getting into some sexy lingerie..."
    $ hour += 1 
    jump NikkiThreesomeDay07    
if nikkifucked and chantellefucked == False:
    ch "Of course we are... And I bet it can grow MUCH better, isn't that right Nikki?"   
    s "Well...err... I wouldn't know Chantelle."
    p "She DOES know. And she LOVED it."
    s "Alright, I admit it! My landboy's cock is a GIANT piece of beautiful manmeat!"
    ch "Wow..."
    if lust_points[2] == 9:
        window hide
        $ lust_points[2] +=1
        $ score += 1
        show lust01:
            xalign 0.8 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
    if lust_points[2] <= 8:
        window hide
        $ lust_points[2] +=2
        $ score += 2
        show lust02:
            xalign 0.8 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02    
    if lust_points[2] >= 10:
        window hide
        show epiclust:
            xalign 0.2 yalign 0.3
            zoom 0.5
            linear 2.0 zoom 1.0
        play sound "Sounds/epiclust.mp3"
        $ renpy.pause(4.0, hard=True)
        hide epiclust        
        show doubledelight:
            xalign 0.4 yalign 0.2
            zoom 0.5
            linear 2.0 zoom 1.0
        play sound "Sounds/delight.mp3"
        $ renpy.pause(4.0, hard=True)
        hide epiclust
        p "Hang on. Did I... Just see a double delight here?"
        s "Yes you did [name]. You managed to lure Chantelle and me into your den of depravity with that huge log you're hiding down there."
        ch "And those huge muscles... Your landboy is making me so horny..."
        p "WOO-HOO! Double delight it is then!"
        s "Let us get ready for a HOT night of love with you by getting into some sexy lingerie..."
        $ hour += 1 
        jump NikkiThreesomeDay07
    c "I'm impressed. But somehow not impressed enough."
    s "I agree with Chantelle. You're not THAT impressive really. The party's over. Go back to your room."
    p "Damn it..."
    $ hour += 1
    jump EveningChoiceDay07
if nikkifucked == False and chantellefucked:
    ch "Of course we are... And I KNOW it can grow MUCH better..."   
    s "H...How do you know?"
    p "She KNOWS cos she saw it in ACTION sis! And she loved it!"
    ch "Yes, it's true Nikki... Your landboy's cock is a mouthwatering GIANT piece of beautiful manmeat!"
    s "Wow..."
    if lust_points[17] == 9:
        window hide
        $ lust_points[17] +=1
        $ score += 1
        show lust01:
            xalign 0.2 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
    if lust_points[17] <= 8:
        window hide
        $ lust_points[17] +=2
        $ score += 2
        show lust02:
            xalign 0.2 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
    if lust_points[17] >= 10:
        window hide
        show epiclust:
            xalign 0.8 yalign 0.3
            zoom 0.5
            linear 2.0 zoom 1.0
        play sound "Sounds/epiclust.mp3"
        $ renpy.pause(4.0, hard=True)
        hide epiclust        
        show doubledelight:
            xalign 0.4 yalign 0.2
            zoom 0.5
            linear 2.0 zoom 1.0
        play sound "Sounds/delight.mp3"
        $ renpy.pause(4.0, hard=True)
        hide epiclust
        p "Hang on. Did I... Just see a double delight here?"
        s "Yes you did [name]. You managed to lure Chantelle and me into your den of depravity with that huge log you're hiding down there."
        ch "And those huge muscles... Your landboy is making me so horny..."
        p "WOO-HOO! Double delight it is then!"
        s "Let us get ready for a HOT night of love with you by getting into some sexy lingerie..."
        $ hour += 1 
        jump NikkiThreesomeDay07
    s "Pretty amazed, but not enough I'm afraid [name]... The party's over, go back to your room."
    p "Damn it..."
    $ hour += 1
    jump EveningChoiceDay07

label NikkiThreesomeDay07:
scene bothhouse01 with dissolve
$ renpy.pause(1.0, hard=True)
s "Now [name], you'd better make this worthwhile for US!"
ch "We'll certainly make it worthwhile for YOU!"
if (stamina <= 0) and (whitebull == False):
    p "Oh! Look at the time! It's like...err... late and all that. ANd I have the swim competition tomorrow. I need to sleep well tonight."
    ch "Are you bailing out on us???"
    p "What? No, well, yes actually. Bye."
    s "Pathetic..."
    $ lust_points[2] -= 1
    $ score -= 1
    show lustminus01:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.6
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    jump EveningChoiceDay07
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
scene bothhouse02 with dissolve
$ renpy.pause(1.0, hard=True)
s "First, by getting that cock of yours HARD and READY to go!"
p "Jeezus Nikki... AAAH!"
ch "Nikki, you are clearly already making him EXTRA-HARD! I can see his bulge almost tearing at the seams of his shorts..."
scene bothhouse03 with dissolve
$ renpy.pause(1.0, hard=True)
s "Not quite yet, I know it can get BIGGER!"
p "AAh... Nikki... Your TITS!"
ch "Allow me to also show him my curves so he has no choice but to pull his shorts down and reveal that MONSTERCOCK he's packing!"
scene bothhouse04 with dissolve
$ renpy.pause(1.0, hard=True)
p "I can't... hold it any longer!"
play sound "Sounds/rip.mp3"
scene bothhouse05 with dissolve
$ renpy.pause(1.0, hard=True)
s "Wow, you tore apart your jockstrap [name]! How are you going to explain that to Nancy? (giggles)"
p "It's not the first time it happens..."
scene bothhouse06 with dissolve
play sound "Sounds/threesome01.mp3"
$ renpy.pause(3.0, hard=True)
ch "So, are you going to wave that flagpole at full mast all evening or do you want us to do something about it?"
p "I want you to do something about it."
ch "I thought you might. Nikki, why don't we show [name] how it feels to have four huge jugs wrapped around his monster shaft?"
s "Ooh, that's a great idea, but let's make sure the poor boy doesn't have a heart attack! (giggles)"
scene bothtitfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oh my God, I think I died and went to heavens!"
scene bothtitfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
scene bothtitfuck01 with dissolve
play music "Sounds/threesome02.mp3"
$ renpy.pause(0.3, hard=True)
scene bothtitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothtitfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
s "His cock is literally trembling with lust now..."
p "FUCK, this is so good, I'm about to blast!!!"
stop music
scene bothtitfuck03 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
p "AAAH!!!"
ch "YES! Shower us in your hot spunk [name]!"
window hide
play sound "Sounds/cumming.mp3"
$ renpy.pause(2.0, hard=True)
s "MMmh, that's a LOT! I hope you can still keep going though..."
p "Of course Nikki, I'm still raging hard for your amazing bodies!"
scene bothhouse06 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Wow, what a real STUD! So, what would you like to do next then [name]?"
jump BothFuckChoiceDay07

label BothFuckChoiceDay07:
menu:
    "Why don't you play with each other for a while, like best pals and all that..." if (bothhouseplay02 == False):
        s "I'm so horny I don't even mind..."
        ch "Me neither Nikki, let's do it!"
        jump BothPlayDay07
    "I want some oral action!" if (bothoral02 == False):
        ch "Ooh, I can't wait to blow that massive log AGAIN!"
        p "First, I wanna lick Nikki's pussy..."
        jump BothOralDay07
    "OK, time for some fun with Nikki's tight pussy!" if (bothnikkipussy02 == False):
        s "I can't wait to feel that log in me again [name]!"
        jump BothNikkiFuckDay07
    "I've had it earlier, but I want it AGAIN! I'm talking Chantelle's sweet hole..." if (bothchantellepussy02 == False):
        ch "I'm honored... Getting fucked TWICE in a day by the island's ultimate STUD!"
        jump BothChantelleFuckDay07
    "Lie on the bed and get ready to receive my load both of you!" if (bothhouseplay02 == True) and (bothoral02 == True) and (bothchantellepussy02 == True) and (bothnikkipussy02 == True):
        $ hour +=1
        p "(Shit, time is really flying, I've already been fucking them for an hour... Better wrap this up.)"
        jump BothFuckCumDay07

label BothPlayDay07:
$ bothhouseplay02 = True
scene both01 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Mmh Nikki, you play with my pussy really well..."
window hide
play sound "Sounds/threesomeboth01.mp3"
$ renpy.pause(3.0, hard=True)
p "I guess she has a lot of experience playing with herself..."
s "[name]! (giggles) It's true, I know what makes a woman feel good... More than a man, even DA MAN!"
scene both02 with dissolve
$ renpy.pause(1.0, hard=True)
s "And what if I lick your back and play with your large funbags?"
window hide
play sound "Sounds/moaning.mp3"
$ renpy.pause(2.0, hard=True)
ch "Ooooh Nikki..."
p "Why don't you lick Nikki's pussy Chantelle?"
s "Everything in due time [name]... Watch and learn about foreplay [name]..."
scene both03 with dissolve
play sound "Sounds/threesomeboth02.mp3"
$ renpy.pause(3.0, hard=True)
s "Mmh Chantelle, you lick my pussy so good..."
ch "Thats' because it tastes so good... We should have done that earlier Nikki!"
s "I want to kiss you... My Best Friend Forever...."
scene both04 with dissolve
play sound "Sounds/kissing.mp3"
$ renpy.pause(2.0, hard=True)
p "OK, that was hot but I want in!"
scene bothhouse06 with dissolve
$ renpy.pause(1.0, hard=True)
ch "So, what would you like us to do next [name]?"
jump BothFuckChoiceDay07

label BothOralDay07:
$ bothoral02 = True
scene bothoral01 with dissolve
$ renpy.pause(1.0, hard=True)
s "You're learning fast [name]...."
window hide
play sound "Sounds/moaning.mp3"
$ renpy.pause(2.0, hard=True)
p "My expert tongue has no match on this island!"
ch "Always bragging... It's part of your charm....But now WE are in charge, aren't we Nikki? (wink)"
s "That's right! Lie down [name] and we'll show you how we handle... DA MAN!"
scene bothoral02 with dissolve
$ renpy.pause(1.0, hard=True)
p "GGl... Mmmm..."
s "Hush [name]r... Let Chantelle take care of that monstercock of yours..."
ch "You'll see, lack of oxygen will enhance your pleasure (giggles)...!"
scene bothoral03 with dissolve
play sound "Sounds/chantelleblow01.mp3"
$ renpy.pause(12.0, hard=True)
ch "First, I'll just lick around the sensitive glans..."
scene bothoral04 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Then the tip..."
scene bothoral05 with dissolve
$ renpy.pause(1.0, hard=True)
s "Mmh, look how hungry Chantelle is for your huge delicious log!"
label BothOral07b:
play sound "Sounds/chantelleblow02.mp3"
scene bothoral06 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral04 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral06 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral04 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral06 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral04 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral06 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral04 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral06 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral04 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral06 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral04 with dissolve
$ renpy.pause(0.2, hard=True)
scene bothoral05 with dissolve
$ renpy.pause(0.1, hard=True)
scene bothoral06
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
scene bothoral04
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
scene bothoral06
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
scene bothoral04
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
scene bothoral06
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
scene bothoral04
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
scene bothoral06
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
scene bothoral04
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
scene bothoral06
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
scene bothoral04
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
scene bothoral06
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
scene bothoral04
$ renpy.pause(0.3, hard=True)
scene bothoral05
$ renpy.pause(0.2, hard=True)
stop sound
menu:
    "Repeat":
        p "GGlll.. mmmore...mmmglore..."
        s "I think he meant to say he wants more of that sumptuous blowjob you're giving him Chantelle!"
        jump BothOral07b
    "Move on":
        s "How was that [name]? It sure looked good for you from where I'm standing... Your body was convulsing..."
        p "Phew... That was cos I couldn't breathe... Let's do something that doesn't involve me almost dying please..."        
        scene bothhouse06 with dissolve
        $ renpy.pause(1.0, hard=True)
        s "Like what?"        
        jump BothFuckChoiceDay07

label BothChantelleFuckDay07:
$ bothchantellepussy02 = True
scene bothchantelle01 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Fuck me hard again like you did this afternoon [name]!"
scene bothchantelle02 with dissolve
$ renpy.pause(1.0, hard=True)
ch  "Oh, FUCK! That's so DEEP!"
p "Hold on steady Chantelle, I'm gonna take full fifteen-inch strokes now!"
label BothChantelleFuckDay07b:
scene bothchantelle01 with dissolve
play sound "Sounds/threesomechantellefuck01.mp3"
$ renpy.pause(0.3, hard=True)
scene bothchantelle02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothchantelle02
$ renpy.pause(0.3, hard=True)
scene bothchantelle01
$ renpy.pause(0.3, hard=True)
scene bothchantelle02
$ renpy.pause(0.3, hard=True)
scene bothchantelle01
$ renpy.pause(0.3, hard=True)
scene bothchantelle02
$ renpy.pause(0.3, hard=True)
scene bothchantelle01
$ renpy.pause(0.3, hard=True)
scene bothchantelle02
$ renpy.pause(0.3, hard=True)
scene bothchantelle01
$ renpy.pause(0.3, hard=True)
scene bothchantelle02
$ renpy.pause(0.3, hard=True)
scene bothchantelle01
$ renpy.pause(0.3, hard=True)
stop sound
menu:
    "Repeat":
        ch "My pussy has turned into a mush..."
        p "Well, let's turn it into a pulp then."
        jump BothChantelleFuckDay07b
    "Move on":
        s "I think you've fucked her enough [name], give her a break..."
        p "Sure, I have other plans anyway..."
        scene bothhouse06 with dissolve
        $ renpy.pause(1.0, hard=True)
        s "Which are?"        
        jump BothFuckChoiceDay07
                
label BothNikkiFuckDay07:
$ bothnikkipussy02 = True
scene bothsisfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Open that tender pussy wide Nikki..."
ch "I don't even know how it's going to fit..."
s "Be caref..."
scene bothsisfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
p "That's how it fits! By rammming it in HARD!"
label BothNikkiFuckDay07b:
scene bothsisfuck01 with dissolve
play sound "Sounds/threesomenikki01.mp3"
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01
$ renpy.pause(0.3, hard=True)
scene bothsisfuck02
$ renpy.pause(0.3, hard=True)
scene bothsisfuck01
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        s "You want more? You want more of my sweet pussy, hey [name]?"
        play sound "Sounds/wantmore.mp3"
        $ renpy.pause(2.0, hard=True)
        p "Fuck YEAH!"
        jump BothNikkiFuckDay07b
    "Move on":
        scene bothsisfuck03
        $ renpy.pause(1.0, hard=True)
        s "Oh my God, that was so good [name]... You really pounded that bull-dick in me this time..."
        p "I aim to please..."
        s "Kiss me..."
        scene bothsisfuck04
        $ renpy.pause(1.0, hard=True)
        ch "Wow, that's so hot... But I want in on the action now, you're making me jealous! (wink)"
        scene bothhouse06 with dissolve
        $ renpy.pause(1.0, hard=True)        
        ch "What would you like to do next [name]?"
        jump BothFuckChoiceDay07

label BothFuckCumDay07:
scene bothsiscum01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I'm about to launch some massive cum missiles!"
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(3.0, hard=True)
s "Go on, we want the BIGGEST load you can muster [name]!"
scene bothsiscum02 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(2.0, hard=True)
ch "MMmh, look at all that cum flying everywhere!"
scene bothsiscum03 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(3.0, hard=True)
s "YES, cover us in your warm cream [name]!"
ch "Damn, your landboy is shooting cum non-stop all over us!"
p "RHAAA! Phew, I think that's the last of it girls..."
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.4
    linear 1.0 yalign 0.6
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
s "I need a shower now, to clean up all that sticky mess you made [name]..."
ch "And I'll join you Nikki..."
scene bothsiscum04 with dissolve
$ renpy.pause(1.0, hard=True)
ch "But first... Let's exchange some of that yummy cum with our mouths Nikki..."
p "Wow, that's so NASTY! Can I join you in the shower?"
ch "You don't want your landlady to catch the three of us naked in the bathroom do you?"
p "Err.. No. I guess not. I'll leave you two to it then."
if (chantellejosewin == False):
    $ chantellewin = True
    p "(One less classmate for that douchebag José to fuck before me... I'll send him a pic as proof.)"
else:
    p "(Chantelle's pussy was amazing...  But with an aftertaste of \"Déja fucked\". By José...sigh)"
$ chantellefucked = True
$ threesome += 1
if threesome >= 4 and (achievement.has("threesomer") == False):
    window hide
    show achievement23:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement23
    $ achievement.grant("threesomer")
if (brittanyfucked == True) and (katefucked == True) and (achievement.has("grabber") == False):
    p "Yeah! I've scored with all the teen beauty pageants... That should make me a..."
    window hide
    show achievement16:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement16
    $ achievement.grant("grabber")
if (nikkijosewin == False):
    $ nikkiwin = True
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
if (daniellafucked == True) and (dorisfucked == True) and (tanyafucked == True) and (achievement.has("brickhouse") == False):
    window hide
    show achievement22:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement22
    $ achievement.grant("brickhouse")
if annafucked and brittanyfucked and chantellefucked and chiyofucked and daniellafucked and debbyfucked and dorisfucked and francinefucked and friedafucked and hallefucked and jenniferfucked and katefucked and katsumifucked and laurafucked and maddyfucked and mariafucked and nancyfucked and nikkifucked and pamelafucked and sandyfucked and sophiafucked and tanyafucked and teaganfucked and vivianefucked:
    window hide
    show achievement17:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement17
    $ achievement.grant("conqueror")
if annawin and brittanywin and chantellewin and chiyowin and daniellawin and debbywin and doriswin and francinewin and friedawin and hallewin and jenniferwin and katewin and katsumiwin and laurawin and maddywin and mariawin and nancywin and nikkiwin and pamelawin and sandywin and sophiawin and tanyawin and teaganwin and vivianewin:
    window hide
    show achievement24:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement24
    $ achievement.grant("ultimate")
$ hour += 1
jump EveningChoiceDay07


label EveningChoiceDay07:
stop music
scene ryanbedroomnight with dissolve
$ locroom = True
$ renpy.pause(1.0, hard=True)

if (hour >= 24):
    if (challengercalls <= 10):
        $ lustaddedB = 2
        call Challenger from _call_Challenger_107
        $ lustaddedB = 1
        call Challenger from _call_Challenger_108
        $ challengercalls += 2        
    p "I should really go to sleep now, tomorrow is the last day... Very important day."
    jump SleepDay07
p "mmmh, what should I do?"
menu:
    "Do some heavy bodybuilding (+2hrs)" if (hour <= 22):    
        if (workout == True):
            "You already trained today."
            jump EveningChoiceDay07
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
            jump EveningChoiceDay07
    "Check the computer":
        jump ComputerEveningDay07
    "Admire my body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump EveningChoiceDay07
    "Go to Nikki's room" if nightsisroomseen07 == False:
        jump SleepoverDay07
    "Go to Tanya's House" if (discovertanya == True) and (seentanyaday07 == False) and (tanyafucked == False) and (hour<=23):
        jump TanyaHouseDay07
    "Go to nancy's room" if (nightmomroomseen02 == False) and (seenmomundressingfullday03  == False) and (seenmomundressingfullday04  == False) and (seenmomundressingfullday05  == False) and (nightmomroomseen06 == False) and (nightmomroomseen07 == False) and (hour >=22):
        jump MomUndressingDay07
    "Go to Anna's house" if (seenannaevening07 == False) and (annafucked == False) and annawaiting and (hour<=23):
        jump AnnaRoomDay07
        
label ComputerEveningDay07:
scene ryancomputer with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label ComputerEveningDay07b:
scene ryancomputer
$ renpy.pause(1.0, hard=True)
menu:
    "Check the map":
        jump MapEveningDay07
    "Check the stats":
        jump StatsEveningDay07
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump ComputerEveningDay07b
    "Learn how to use the pendulum" if (pendulum == True) and (pendulumactive ==False):
        jump CompPendulumEveningDay07
    "Play a smutty game (+1hr)":
        jump CompGameEveningDay07
    "Turn the computer off":
        jump EveningChoiceDay07

label CompPendulumEveningDay07:
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump ComputerEveningDay07b

label MapEveningDay07:
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
jump ComputerEveningDay07b

label StatsEveningDay07:
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
jump ComputerEveningDay07b       

label CompGameEveningDay07:
scene ryancomputergame with dissolve
$ renpy.pause(1.0, hard=True)
p "This game is tough. My fingers hurt like hell from so much clicking..."
$ hour +=1
jump ComputerEveningDay07b 
        
label MomUndressingDay07:
stop music
$ nightmomroomseen07 = True
$ locroom = False
scene nancybedroomclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "The door is locked but I can see some light poking through the keyhole."
menu:
    "Look through the keyhole":
        jump MomUndressingDay07b
    "Leave and go back to my room":
        jump EveningChoiceDay07
        
label MomUndressingDay07b:
scene nancyundressing01 with dissolve
$ renpy.pause(1.0, hard=True)
p "nancy is sitting on her bed. She looks like she's thinking about doing something..."
p "More landlady blueballing on the way for you guys it seems... What should I do?"
menu:
    "Why do you even ask? Look on of course!":
        jump MomUndressing02Day07
    "I feel dirty watching mom like that. Go back to my room and cry into my pillow":
        jump EveningChoiceDay07

label MomUndressing02Day07:
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
    jump EveningChoiceDay07

scene nancyundressing07 with dissolve
$ seenmomundressingfullday07 = True
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
if lust_points[16] <= 9:
    $ lust_points[16] +=1
    $ score += 1
    show lust01:
        xalign 0.6 yalign 0.6
        linear 1.0 yalign 0.4
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
p "I think I heard her say my name while she was creaming all over her huge dildo... Wish it was my cock instead."
p "Probably best to leave now, I don't want to be seen peeping through mom's keyhole like that."    
$ hour +=1
stop music

jump EveningChoiceDay07   


label TanyaHouseDay07:
if (seentanyaday03 == False) and (seentanyaday04 == False) and (seentanyaday05 == False):
    jump TanyaHouse01Day07

if (seentanyaday03 == True) or (seentanyaday04 == True) or (seentanyaday05 == True):
    jump TanyaBed01Day07
    
label TanyaHouse01Day07:
$ seentanyaday07 = True
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
                jump TanyaHouse02Day07
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay07
    "I'm out of here, you guys are crazy!":
        ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
        jump EveningChoiceDay07
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
                jump TanyaHouse02Day07
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay07
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
        jump EveningChoiceDay07
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
                jump TanyaHouse02Day07
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay07

label TanyaHouse02Day07:
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
call screen tanyawankslowDay07
screen tanyawankslowDay07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("TanyaWankFastDay07")
label TanyaWankFastDay07:
hide faster
show tanyawankfast
show cum
call screen tanyawankfastDay07
screen tanyawankfastDay07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TanyaWankCumDay07")

label TanyaWankCumDay07:
stop sound
hide tanyawankslow
hide tanyawankfast
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
        jump EveningChoiceDay07

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
                jump EveningChoiceDay07
            "Go back to Anna's house" if (seenannaevening07 == False) and (annafucked == False) and annawaiting and (hour<=23):
                jump AnnaRoomDay07
                
label TanyaBed01Day07:
$ seentanyaday07 = True
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
                jump TanyaHouse02Day07
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
                jump EveningChoiceDay07            
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
        jump EveningChoiceDay07
    menu:
        "Ok, I'll do it! I'm da man, I'm DA MAN!":
            jump TanyaHouse02Day07
        "I'm out of here, you guys are crazy!":
            ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
            jump EveningChoiceDay07

if (tanyawebcamday03 == True):
    jump TanyaBed02Day07
    
label TanyaBed02Day07:
$ tanyawebcamday07 = True
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
            jump TanyaCondomsDay07
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
            jump EveningChoiceDay07            
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
    jump EveningChoiceDay07
p "Alright! Let's do it then, I'm getting a massive boner just thinking about it!"
label TanyaCondomsDay07:
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
    jump TanyaBed03Day07
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
    jump EveningChoiceDay07
        
label TanyaBed03Day07:   
scene tanyabed01 with dissolve
play music "Sounds/tanyamusic.mp3"
$ renpy.pause(1.0, hard=True)
ta "Oh, look at poor little Darryl... All tied up and with his cock constrained in his tight briefs..."
dl "Untie me for fuck's sake Tanya! Wh... Why is this boy here again? I told you I never wanted to see him again in MY house!"
ta "He's here to get us lots of money... I'm sorry honeypot, but I read our viewers' requests last night on twatter and they all wanted to see me handle his young monster cock!"
dl "No please, don't do this to me, I'm all tied up, this is so humiliating!"
ta "Well that's the idea darling... Now hush, showtime is in a few seconds, [name], can you go and turn the webcam on please?"
p "Sure Tanya!"
$ tanyabedday07 = True
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
    jump TanyaBed04Day07
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

label TanyaBed04Day07:
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
label TanyaBed04Day07b:
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
        jump TanyaBed04Day07b
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
        jump TanyaBlowjobDay07
    "Fuck her above Darryl" if (tanyaride == False):
        jump TanyaRideDay07
    
label TanyaBlowjobDay07:
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
label TanyaBlowjobDay07b:
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
        jump TanyaBlowjobDay07b
    "Get her to take MORE of your cock!":
        p "I think you can take more Tanya, come on, do it! AAAH!"
        scene tanyabed11c with dissolve    
        play sound "Sounds/hallesuck02.mp3"
        $ renpy.pause(3.0, hard=True)
        dl "I can't watch this! This is too humiliating!"
        jump TanyaBlowjobDay07b
    "Fuck her above Darryl" if (tanyaride == False):
        jump TanyaAboveDay07
    "Let her ride you like a wild bronco" if (tanyaride == True) and (tanyablow == True):
        jump TanyaRideDay07
        
label TanyaAboveDay07:
$ tanyaride = True
scene tanyabed12 with dissolve
play sound "Sounds/tanya04.mp3"
$ renpy.pause(3.0, hard=True)
ta "Come and stick that big fucking cock in me!"
scene tanyabed13 with dissolve
$ renpy.pause(3.0, hard=True)
p "Ready to have your pussy ruined for your hubby by a way bigger cock than his?"
ta "Ooh, fuck yeah!"
label TanyaAboveDay07b:
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
        jump TanyaAboveDay07b
    "Get a blowjob" if (tanyablow == False):
        ta "Good idea, and let's do it right in front of Darryl's face, you don't mind do you hubby?"
        dl "Of course I fucking mind! Don't do this to me!"
        ta "Sorry, but that's what our viewers want and that's what we'll give them..."
        jump TanyaBlowjobDay07
    "Let her ride you like a wild bronco" if (tanyaride == True) and (tanyablow == True):
        jump TanyaRideDay07
    

label TanyaRideDay07:
scene tanyabed15 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Let me ride that donkey-dick stud! I can't wait to feel that monstrous rock-hard member deep inside of me while my helpless hubby watches on!"
dl "No, don't fuck him please Tanya!"
ta "Stop pretending you don't like it honey, I can see your erection distending your tight briefs... Just watch and enjoy the ride, I sure will!"
play music "Sounds/tanyafuckslow.mp3"
show tanyafuckslow
show faster
call screen tanyafuckslow07
screen tanyafuckslow07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("TanyaFuckFast07")
label TanyaFuckFast07:
hide faster
play music "Sounds/tanyafuckfast.mp3"
show tanyafuckfast
show cum
call screen tanyafuckfast07b
screen tanyafuckfast07b:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TanyaFuckCum07")

label TanyaFuckCum07:
hide tanyafuckslow
hide tanyafuckfast
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
if (nikkifucked == True) and (dorisfucked == True) and (daniellafucked == True) and (achievement.has("brickhouse") == False):
    window hide
    show achievement22:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement22
    $ achievement.grant("brickhouse")
if annafucked and brittanyfucked and chantellefucked and chiyofucked and daniellafucked and debbyfucked and dorisfucked and francinefucked and friedafucked and hallefucked and jenniferfucked and katefucked and katsumifucked and laurafucked and maddyfucked and mariafucked and nancyfucked and nikkifucked and pamelafucked and sandyfucked and sophiafucked and tanyafucked and teaganfucked and vivianefucked:
    window hide
    show achievement17:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement17
    $ achievement.grant("conqueror")
if annawin and brittanywin and chantellewin and chiyowin and daniellawin and debbywin and doriswin and francinewin and friedawin and hallewin and jenniferwin and katewin and katsumiwin and laurawin and maddywin and mariawin and nancywin and nikkiwin and pamelawin and sandywin and sophiawin and tanyawin and teaganwin and vivianewin:
    window hide
    show achievement24:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement24
    $ achievement.grant("ultimate")
$ hour += 1
$ tanyafucked = True
$ backdoor += 1
if (backdoor >= 12) and (achievement.has("banger") == False):
    window hide
    show achievement19:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement19
    $ achievement.grant("banger")
if (tanyajosewin == False):
    p "(She didn't notice I took a picture of us... Now I'll send it to José)."
    $ tanyawin = True

menu:
    "Go back home":
        jump EveningChoiceDay07
    "Go to Anna's house" if (seenannaevening07 == False) and (annafucked == False) and annawaiting and (hour<=23):
        jump AnnaRoomDay07

label AnnaRoomDay07:
scene annaroom01 with dissolve
$ renpy.pause(1.0, hard=True)
$ seenannaevening07 = True
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
        jump EveningChoiceDay07
    if (annajosewin == True):
        an "My son wasn't tired like you when he rammed his giant pole up all my holes the other day! I guess I'll just have to fuck him again tonight..."
        an "Now get out of my house!"
        $ hour += 1
        jump EveningChoiceDay07
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
            jump AnnaRoom02PreDay07
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
                jump EveningChoiceDay07
            if (annajosewin == True):
                an "My son wasn't tired like you when he rammed his giant pole up all my holes the other day! I guess I'll just have to fuck him again tonight..."
                an "Now get out of my house!"
                $ hour += 1
                jump EveningChoiceDay07

label AnnaRoom02PreDay07:            
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
    jump AnnaRoom02Day07
if (lust_points[0] <= 9):
    an "Well, it's too late. I'm not in the mood anymore. I'm tired and I'm going to sleep."
    p "What? But I did everything right! It's not fair!"
    an "Clearly you didn't. If you had, my lust for you would be epic. And it isn't."
    $ hour += 1
    jump EveningChoiceDay07

label AnnaRoom02Day07:
scene annaroom02 with dissolve
$ renpy.pause(1.0, hard=True)
an "Let me first get more comfortable by getting rid of this bathrobe. So you can admire my curves..."
if (stamina <=0) and (whitebull == False):
    p "You know what? This is getting a bit too saucy for me. I'm like, real tired, you know, school, homework, stuff like that."
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
        $ hour += 1
        jump EveningChoiceDay07
    if (annajosewin == True):
        an "My son wasn't tired like you when he rammed his giant pole up all my holes! I guess I'll just have to fuck him again tonight..."
        an "Now get out of my house!"
        $ hour += 1
        jump EveningChoiceDay07
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
label AnnaFuckChoiceDay07:
menu:
    "Let me lift you up on my crank!" if (annacrank == False):
        jump AnnaCrankDay07
    "How about giving me a nice blowjob?" if (annablow == False):
        jump AnnaBlowDay07
    "Your boobs seem ideal for a titfuck..." if (annatits == False):
        jump AnnaTitfuckDay07
    "Let's get on the bed and fuck like wild animals!" if (annabed == False):
        jump AnnaBedDay07
    "I need to get my rocks off SOON! In YOUR ARSE!" if (annacrank == True) and (annablow == True) and (annatits == True) and (annabed == True):
        an "What? But... You're way too big for that! On the other hand, you're my guest so I'll let you do it, naughty boy!"
        jump AnnaMovieDay07

label AnnaCrankDay07:
$ annacrank = True
scene annaroom11 with dissolve
play sound "Sounds/annacrank01.mp3"
$ renpy.pause(4.0, hard=True)
an "Mmh, I like how POWERFUL that giant tool feels! Please IMPALE me on it [name]!"
scene annaroom12b with dissolve
$ renpy.pause(1.0, hard=True)
an "OOOH, FUCK! It's so fucking thick and DEEP!"
p "Hang on, I'll drill even deeper!"
label AnnaCrankDay07b:
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
        jump AnnaCrankDay07b
    "Move on":
        p "That was a nice workout. Let's do something else..."
        an "The best workout my fuckhole ever got... Phew... What would you like to do next [name]?"        
        jump AnnaFuckChoiceDay07

label AnnaBlowDay07:
$ annablow = True
scene annaroom13 with dissolve
play sound "Sounds/annablow01.mp3"
$ renpy.pause(7.0, hard=True)
an "Let me lick it first... God, it's so fucking big and beautiful!"
label AnnaBlowDay07b:
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
        jump AnnaBlowDay07b
    "Move on":
        scene annaroom13 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "That's good, now my cock is nice and shiny with your spit..."
        an "I was choking on it, it's so massive!"
        jump AnnaFuckChoiceDay07

label AnnaTitfuckDay07:
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
label AnnaTitfuckDay07b:
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
        jump AnnaTitfuckDay07b
    "Move on":
        p "I've creamed my precum all over your tits, so that's marked, let's do something else!"
        jump AnnaFuckChoiceDay07

label AnnaBedDay07:
$ annabed = True
scene annaroom08 with dissolve
play sound "Sounds/annabed01.mp3"
$ renpy.pause(5.0, hard=True)
an "Mmh, I can't wait to feel this big dick in my tight little pussy..."
scene annaroom08b with dissolve
$ renpy.pause(1.0, hard=True)
an "AAh, you're stretching me wide open!"
label AnnaBedDay07b:
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
        jump AnnaBedDay07b
    "Move on":
        p "Let's do something else!"
        jump AnnaFuckChoiceDay07

label AnnaMovieDay07:
scene annafuckmovie with dissolve
p "As I said, I'll finish off by ramming my pole up your tight arse!"
an "I'm ready, just be gentle will you? No one has ever gone up my backside before... Even my ex-husband."
p "Cool, I'll take your arse virginity then!"
play music "Sounds/annafuckslow.mp3"
show annafuckslow
show faster
call screen annaslowfuckday07
screen annaslowfuckday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("AnnaFastFuckDay07")

label AnnaFastFuckDay07:
stop music
hide faster
play music "Sounds/annafuckfast.mp3"
show annafuckfast
show cum
call screen annafastfuckday07
screen annafastfuckday07:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("AnnaCumDay07")

label AnnaCumDay07:
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
if (backdoor >= 12) and (achievement.has("banger") == False):
    window hide
    show achievement19:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement19
    $ achievement.grant("banger")
if annafucked and brittanyfucked and chantellefucked and chiyofucked and daniellafucked and debbyfucked and dorisfucked and francinefucked and friedafucked and hallefucked and jenniferfucked and katefucked and katsumifucked and laurafucked and maddyfucked and mariafucked and nancyfucked and nikkifucked and pamelafucked and sandyfucked and sophiafucked and tanyafucked and teaganfucked and vivianefucked:
    window hide
    show achievement17:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement17
    $ achievement.grant("conqueror")
if annawin and brittanywin and chantellewin and chiyowin and daniellawin and debbywin and doriswin and francinewin and friedawin and hallewin and jenniferwin and katewin and katsumiwin and laurawin and maddywin and mariawin and nancywin and nikkiwin and pamelawin and sandywin and sophiawin and tanyawin and teaganwin and vivianewin:
    window hide
    show achievement24:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement24
    $ achievement.grant("ultimate")
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
jump EveningChoiceDay07

label SleepDay07:
scene ryansleeping with dissolve
play music "Sounds/ryansnoring.mp3"
$ renpy.pause(1.0, hard=True)
"You fall asleep and dream of your adventures to come..."
$ renpy.pause(2.0, hard=True)

"Your current score (not that it matters) is: {b}[score]{/b}"
if (score <=150):
    "Your ranking: {b}Douchebag{/b}"
elif (score <=170):
    "Your ranking: {b}Noob{/b}"
elif (score <=190):
    "Your ranking: {b}Average Joe{/b}"
elif (score <=210):
    "Your ranking: {b}Hunk{/b}"
else:
    "Your ranking: {b}Babe Magnet{/b}"
stop music
window hide

jump Day08