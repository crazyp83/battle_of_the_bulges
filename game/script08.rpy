label Day08:
# reboot variables
$ day = 1
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

$ busbeach = False
$ bustown = False
$ bushome = False
$ debbytitfuck = False
$ debbyback = False
$ debbyfrontfuck = False
$ debbydoggy01 = False

stop music
play sound "Sounds/yawning.mp3"
scene ryanyawning with dissolve
$ renpy.pause(1.0, hard=True)
p "Yet another beautiful day... Where I show José who's the island's ultimate stud!"
if (nursefucked07 == True):
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
call Challenger from _call_Challenger_109
$ lustaddedB = 1
call Challenger from _call_Challenger_110
$ challengercalls += 2

label MorningDay08b:
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "What should I do?"
menu:
    "Take a shower" if familythreesome == False:
        jump ShowerMorningDay08
    "Go for a jog":
        jump JogMorningDay08
    "Check the computer":
        jump ComputerMorningDay08
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump MorningDay08b
    "Go for breakfast" if familythreesome:
        jump MomYogaDay08
        
label JogMorningDay08:
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
$ hour += 1
jump BreakfastDay08

label ComputerMorningDay08:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label ComputerMorningDay08b:
scene ryancomputerday
menu:
    "Check the map":
        jump MapMorningDay08
    "Check the stats":
        jump StatsMorningDay08
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump ComputerMorningDay08b
    "Turn the computer off":
        jump MorningDay08b

label MapMorningDay08:
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
jump ComputerMorningDay08b

label StatsMorningDay08:
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
jump ComputerMorningDay08b

label ShowerMorningDay08:
scene bothshowermorning01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oooh... Both Nikki AND Nancy are in the shower, with the door wide open and their fine arses in lingerie staring at me..."
menu:
    "Having said that... I might need to save some stamina for later today... I'd better leave quietly.":
        jump MorningDay08b
    "To hell with the game's objectives, I want some poontang NOW!" if (nikkifucked == True) and (nancyfucked == True):
        jump ShowerMorningDay08b
    "This is going to be tough. I've fucked Nancy, but not Nikki yet..." if (nikkifucked == False) and (nancyfucked == True):
        jump ShowerMorningDay08b
    "This is going to be tough. I've fucked Nikki, but not Nancy yet..." if (nikkifucked == True) and (nancyfucked == False):
        jump ShowerMorningDay08b
    "This is going to be tough. I didn't fuck either of them yet..." if (nikkifucked == False) and (nancyfucked == False):
        jump ShowerMorningDay08b

label ShowerMorningDay08b:
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
    jump MorningThreesomeDay08
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
    jump BreakfastDay08            
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
    jump BreakfastDay08       
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
    jump BreakfastDay08            

label MorningThreesomeDay08:
scene morningfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
m "Since we all agree, what would you like to do for morning fun [name]?" 
label MorningChoiceDay08:
menu:
    "My cock is rock-hard and ready to burst, cool it down please!" if (morningfeet == False):
        s "My feet are exactly what you need..."
        m "And my tits will help too..."
        jump MorningFeetDay08
    "How about some lesbian fun... I'll watch." if (morningplay == False):
        s "Great idea... I've always wanted to play with your fat funbags mom!"
        jump MorningPlayDay08
    "A household that sucks together is a household that sticks together!" if (morningblow == False):
        s "I volunteer to blow you first!"
        m "But don't make him pop too soon Nikki, I want him to fuck my mouth next..."
        jump MorningBlowDay08
    "I can't decide which pussy to fuck!" if (morningdp == False):
        s "Then we should let you test-drive both."
        jump MorningDoubleDay08
    "I'm about to burst a nut!" if (morningplay == True) and (morningblow == True) and (morningdp == True) and (morningfeet == True):
        jump MorningCumDay08

label MorningFeetDay08:
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
label MorningFeetDay08b:
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
stop sound
menu:
    "Repeat":
        p "Yeah, keep going Nikki, I'm close..."
        s "Oooh, you're gonna give us a great big load of pearly white cum [name]?"
        m "I can't wait to get my tits covered in your spunk [name]!"
        jump MorningFeetDay08b
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
        jump MorningChoiceDay08

label MorningPlayDay08:
$ morningplay = True
scene morningbothplay01 with dissolve
$ renpy.pause(1.0, hard=True)
s "Mom... Your tits are so big and soft...."
m "You were always tugging at them when you were a suckling baby. Do it again... I have some milk for you my sweet child."
p "Fuck yeah!"
label MorningPlayDay08b:
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
        jump MorningPlayDay08b
    "Move on":
        s "I'm not sure I'll need breakfast anymore today...(giggles)"
        scene morningfuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        m "What would you like to do next [name]?"
        jump MorningChoiceDay08

label MorningBlowDay08:
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
label MorningBlowDay08b:
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
        jump MorningBlowDay08b
    "Move on":
        scene morningsisblow03 with fastdissolve
        play sound "Sounds/morningsisperfect.mp3"
        $ renpy.pause(1.0, hard=True)
        s "I think I've sucked about a pint of precum from that monstrous rod..."
        p "I'm always VERY bloated in the morning..."
        m "My turn! Please fuck my mouth my sweet little pumpkin!"
        jump BothMomMorningSuckDay08
                
label BothMomMorningSuckDay08:
scene morningmomblow01
$ renpy.pause(1.0, hard=True)
p "Open wide Nancy. I'll pile-drive my shaft down your throat..."
m "MMM, gggllr..."
scene morningmomblow02
$ renpy.pause(1.0, hard=True)
p "There. Hold it..."
s "This is so hot, you're really fucking her mouth without mercy [name]."
p "She asked for it, didn't she?"
label BothMomMorningSuckDay08b:
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
        jump BothMomMorningSuckDay08b
    "Move on":
        scene morningmomblow03 with fastdissolve
        $ renpy.pause(1.0, hard=True)
        m "*cough* Thank you [name], that was so kind of you."
        p "Get up Nancy, and let's move on to something else, I'm still horny."
        m "Of course my sweet little pumpkin!"
        jump MorningChoiceDay08

label MorningDoubleDay08:
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
        jump MorningMomFirstDay08
    "Fuck Nikki first":
        p "Nikki's pussy is so tight and tempting, I'll do her first!"
        s "Yeah! I'm ready, pound it hard [name]! I'll stand against the wall for you."
        m "Be quick, I NEED that cock!"
        $ sisfirst = True
        jump MorningSisFirstDay08
    
label MorningMomFirstDay08:
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
    jump MorningDoubleEndDay08
s "Let's switch now, my turn!"
jump MorningSisFirstDay08

label MorningSisFirstDay08:
scene morningdppresis with dissolve
$ renpy.pause(1.0, hard=True)
s "Just shove your meatpole in [name], I can't wait any longer! I WANT IT!"
p "I like your enthusiasm Nikki."
play music "Sounds/morningsisslow.mp3"
show morningsisslow
show faster
call screen morningsisslowday08
screen morningsisslowday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MorningSisFastDay08")
label MorningSisFastDay08:
hide faster
stop music
play music "Sounds/morningsisfast.mp3"
show morningsisfast
show next
call screen morningsisfastday08
screen morningsisfastday08:
    modal True
    button:
        xpos .82
        ypos .9
        xysize(100, 50)        
        action Jump ("MorningSisEndDay08")

label MorningSisEndDay08:
hide morningsisslow
hide morningsisfast
stop music
scene morningdppresis
$ renpy.pause(1.0, hard=True)
p "Phew, I pulled out just in time. I was about to burst a nut there, your pussy is so TIGHT Nikki!"
if (momfirst == True):
    s "That's cos your dong is so fucking HUGE [name]! *giggles*"
    m "Now, since your cock is still hard and ready, what should we do next my stud tenant?"
    jump MorningDoubleEndDay08
m "I can't wait any longer either, my turn!"
jump MorningMomFirstDay08

label MorningDoubleEndDay08:
scene morningfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
m "What would you like to do next [name]?"
jump MorningChoiceDay08

label MorningCumDay08:
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
jump BreakfastDay08

label MomYogaDay08:
scene saturdayyoga01 with dissolve
$ renpy.pause(1.0, hard=True)
m "ooh, you're up early my sweet little tenant. I was about to some yoga. Why don't you join me since breakfast isn't ready yet?"
p "Sure Nancy. I was going to do some stretching anyway to get ready for the swimming competition later this morning."
m "This will definitely be just as good. Just watch me and try and do exactly as I do, alright?"
p "I'll try..."
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
m "Well, stop looking at my big tits for starters. What if you pop a boner during the swimming competition? That would be most embarrassing."
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
m "Well, that's great honey pot! You can thank me later today when you bring back home the swimming trophy and make me proud... *wink*"
p "Sure Nancy, thanks a lot for your help, now I'm gonna win FOR SURE!"
m "I'll prepare breakfast, it will be ready in no time."
$ hour += 1
label BreakfastDay08:
stop music
scene breakfastday03a with dissolve
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
    m "Don't start arguing or breakfast will get cold... What are your plans today Nikki?"
    hide breakfastday03b
    show breakfastday03c with dissolve
    s "I've been invited by José to be at the beach precisely at 6pm. He said it was super-important."
    hide breakfastday03b
    show breakfastday03f
    with dissolve
    m "What a coincidence! Anna also arranged a meeting with me there at 6pm."
    p "Gee, that's amazing. I happen to have invited Debby at the beach at the very same time..."
    hide breakfastday03f
    scene breakfastday03a with fastdissolve
    m "Mmmh, something doesn't seem quite right."
    p "Seems totally right to me. It's precisely the time at which the game ends."
    show breakfastday03d with dissolve
    s "What game?"
    p "I have a little bet with José... Tonight, we'll find out who won and you should definitely be all there for the outcome..."
    hide breakfastday03d
    show breakfastday03b with dissolve
    m "Now I'm intrigued! I hope you win your bet my sweet tenant, whatever it is..."
    show breakfastday03d with dissolve
    s "I hope so too..."
    p "t will be... epic."
    jump BreakfastDay08b

if familythreesome == False:
    show breakfastday03b with dissolve
    m "So what are you going to do today Nikki on this beautiful Sunday since you don't have school?"
    show breakfastday03c with dissolve
    s "I've been invited by José to be at the beach precisely at 6pm. He said it was super-important."
    hide breakfastday03b
    show breakfastday03f
    with dissolve
    m "What a coincidence! Anna also arranged a meeting with me there at 6pm."
    p "Gee, that's amazing. I happen to have invited Debby at the beach at the very same time..."
    hide breakfastday03f
    scene breakfastday03a with fastdissolve
    m "Mmmh, something doesn't seem quite right."
    p "Seems totally right to me. It's precisely the time at which the game ends."
    show breakfastday03d with dissolve
    s "What game?"
    p "I have a little bet with José... Tonight, we'll find out who won and you should definitely be all there for the outcome..."
    hide breakfastday03d
    show breakfastday03b with dissolve
    m "Now I'm intrigued! I hope you win your bet my sweet tenant, whatever it is..."
    show breakfastday03d with dissolve
    s "I hope so too..."
    p "It will be... epic."
    jump BreakfastDay08b

label BreakfastDay08b:
scene breakfastday03a
p "But first, I have to head for school for the swimming competition. It's soon, like right now almost."
m "I hope you win THAT too my sweet tenant!"
show breakfastday03d
s "Yes, good luck representing Hardcox High, [name]. I can't come and cheer for you because I... have prior engagements this morning."
"You clean the table with Nikki and head for the swimming hall at Hardcox High with your sportsbag..."
$ hour += 1
stop music
scene lockerswim01 with fade
$ renpy.pause(1.0, hard=True)
q "Are you ready for the competition [name]? We're counting on you."
p "Don't worry Quentin, I trained hard with Maddy and we'll beat those arseholes!"
q "Good, cos I'm not feeling well and I don't think I can beat anybody today..."
scene succubus01  with dissolve
$ renpy.pause(1.0, hard=True)
rc "Well, hello boys... Could I interest you in a pre-competition reward from an admiring fan?"
q "Don't listen to her [name], she's from the other team!"
scene succubus06  with dissolve
$ renpy.pause(1.0, hard=True)
rc "So? I'm still in AWE of BOTH of you..."
q "...She's saying nice things about me... No girl has ever said such nice things!"
scene succubus07  with dissolve
$ renpy.pause(1.0, hard=True)
rc "And I'll DO nice things TO you too if you help me out of this TIGHT bikini..."
p "Alright! Show us ya titties, girl!"
q "No!... [name]...You must... resist... She's a SUCCUBUS!"
menu:
    "Tell her to go fuck herself!":
        scene succubus02 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "You get anywhere near me and I'll bust your arse lady! I mean, not literally."
        rc "Why are you scared? I'm not here to HARM you, I'm here to make you feel GOOD... With a little reward..."
        p "I don't want no stinkin reward from you! Go back to hell where you came from!"
        rc "Humpf..."
        jump Succubus01
    "She's hot, who cares if she sucked a whole bus?":
        scene succubus02 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "You have five minutes to show your appreciation lady..."
        rc "That is PLENTY of time, don't worry."
        q "No, what have you done [name]? She'll suck the life energy out of us!"
        p "Na, we'll be fine. I can control myself, don't worry."
        q "I think you fell into her TRAP!"
        jump Succubus02
        
label Succubus01:
scene succubus03  with dissolve
$ renpy.pause(1.0, hard=True)
rc "What about you, boy? You want a little reward?"
q "No... Leave me alone, please!"
rc "Let's see what you're hiding in those trunks, shall we?"
q "gggg.... Your...breasts!"
rc "That's right. Just look at them, waiting to be plastered in hot cum... I WANT your cum, BOY!"
scene succubus04  with dissolve
$ renpy.pause(1.0, hard=True)
q "Oh no! She's got her hand on my... penis!"
rc "And you've got a cute hardon for me. Is it because of my big tits?"
q "Please...no... should not... watch..."
rc "But you can't help yourself, right? I think I'll just need a few tugs on that little thing and you'll blow your..."
scene succubus05  with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
rc "... LOAD! Yes, that's it, let it all out from your little friend! All over my BIG tits, that's what you wanted, didn't you?"
q "AAAAH! She made me cum!"
scene succubus05b  with dissolve
$ renpy.pause(1.0, hard=True)
rc "What about you, big boy, you sure you don't want the same TREATMENT?"
p "I've said no and I mean it!"
rc "Your loss..."
q "She got me... My balls ache now..."
p "Get dressed and let's join the competition Quentin. I kept my stamina, it's what counts."
jump SwimCompStart

label Succubus02:
scene succubus08 with dissolve
$ renpy.pause(1.0, hard=True)
p "On second thoughts, you might be right..."
rc "Don't resist, cute boy. I can feel something VERY BIG with my knee... And it's getting BIGGER, isn't it?"
p "You're really... a succubus! Help!"
scene succubus09 with dissolve
$ renpy.pause(1.0, hard=True)
rc "There's no need to call for help, I only want to RELIEVE you of all that TENSION in your... HUMONGOUS COCK!"
p "I'm not tense, I'm not tense!"
rc "Let me check, I think you REALLY need help after all... FROM ME!"
scene succubus10 with dissolve
$ renpy.pause(1.0, hard=True)
rc "Ooh, that MONSTERDONG looks VERY TENSE to me..."
p "I..."
rc "Shush, boy, let my mouth do all the talking. ON YOUR COCK!"
p "Oh God!"
rc "Quentin, I'm sure you're HARD for me too, come over here and join the FUN!"
q "I... must... resist... can't... resist... AAAH!"
scene succubus11 with dissolve
$ renpy.pause(1.0, hard=True)
rc "Mmmh, both HARD and READY for me! I'm gonna have some FUN with you boys..."
p "Just do your dirty deed, the competition will start soon."
rc "Don't worry BIG BOY, I'll make you BOTH cum in no time!"
scene succubus12 with dissolve
play sound "Sounds/lick.mp3"
$ renpy.pause(1.0, hard=True)
rc "...First with my expert tongue licking over the VAST expanse of that donkey-dick..."
rc "...To that little friend being massaged by my right hand..."
q "Uuuh, oohhh!"
stop sound
scene succubus13 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
q "Noooo, she's making me CUM! AAAH!"
rc "Your little friend really liked my hand, didn't it? Pump it ALL out, boy!"
scene succubus14 with dissolve
$ renpy.pause(1.0, hard=True)
rc "Now, YOUR turn, BIG BOY!"
p "Damn, she'a real cock-gobbler that one!"
q "Try and resist [name]!"
scene succubus15a with dissolve
play sound "Sounds/hardsucking.mp3"
$ renpy.pause(1.0, hard=True)
p "I can see why you came so fast Quentin, this girl is a PRO!"
rc "Come on, give me... Glurb... Your... CREAM!"
stop sound
scene succubus15b with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "AAAH, her mouth is ssoooo good, I'm CUMMMIIING!"
rc "Gglgllr!"
scene succubus15c  with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "Fuck, she's draining my nuts! RHAAAA!"
rc "That's it, let it ALL OUT, STUD!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.6
    linear 1.0 yalign 0.8
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
scene succubus16  with dissolve
play sound "Sounds/lotofcum.mp3"
$ renpy.pause(2.0, hard=True)
rc "Wow, that's a lot of cum... I'd better get going now, thank you boys for the fun time!"
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
q "She got us [name]. I already feel weaker."
p "Weaker than you already were??? Don't worry about it, I'll be swimming anyway."
q "I'm afraid not. You weren't registered in time except for the mixed relay."
p "Ah, shit. Let's go anyway, we're late."
jump SwimCompStart

label SwimCompStart:
scene pamelacomp01 with fade
$ renpy.pause(1.0, hard=True)
pa "Welcome to the Veri-Bosti Academy Swimming Cup Final! I'm your host, Pamela Udderson."
pa "And now, let the music begin for the cheerleaders' routines and the teams' entrance!"
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
play music "Sounds/pompom.mp3"
scene pompom01 with dissolve
$ renpy.pause(1.0, hard=True)
br "H-A-R-D..."
hg "Sainte-Nitouche, Sainte-Nitouche!"
br"...C-O-X..."
scene pompom02 with dissolve
$ renpy.pause(1.0, hard=True)
hg "...Give it a PUSH!"
scene pompom03 with dissolve
$ renpy.pause(1.0, hard=True)
br "...We're the STRONGEST! They're the WEAKEST!"
scene pompom04 with dissolve
$ renpy.pause(1.0, hard=True)
hg "Shove it IN our opponents' TEAM!"
scene pompom05 with dissolve
$ renpy.pause(1.0, hard=True)
br "You SLUTTY BITCH, you ruined MY routine!"
scene pompom06 with dissolve
$ renpy.pause(1.0, hard=True)
hg "You're just jealous because I have bigger TITS than YOU! Like ALL the girls at the Lycée de Sainte-Nitouche!"
br "What? How dare you, filthy WHORE! That is NOT true!"
hg "Well, let's find out then!"
scene pompom07 with dissolve
$ renpy.pause(1.0, hard=True)
hg "See? We Sainte-Nitouche girls are STACKED and PACKED! Packed full of our boys' monster dongs, ROFL!"
scene pompom08 with dissolve
$ renpy.pause(1.0, hard=True)
br "So what? HARDCOX has the BIGGEST tits and the HUGEST HUNG STUDS on the island!"
if brittanywin:
    br "Especially [name], I should know, I saw his MASSIVE BOYMEAT UP CLOSE AND PERSONAL!"
hg "We'll see about THAT! We're the DEFENDING CHAMPIONS may I remind you, LOSERS!"
br "And in a couple of hours, you'll be the EX-DEFENDING CHAMPIONS!"
scene team01enter with dissolve
$ renpy.pause(1.0, hard=True)
pa "Welcome to our first team, the hosts of this competition, HARDCOX HIGH!"
play sound "Sounds/applause.mp3"
p "Yo, Laura, Frieda... Quentin, nice to see you."
md "I can sense the smell of VICTORY today!"
scene team02enter with dissolve
$ renpy.pause(1.0, hard=True)
pa "And the team defending their title, LYCEE DE SAINTE-NITOUCHE!"
play sound "Sounds/applause.mp3"
rb "What do I see over there? GLORY to us YET AGAIN!"
rc "Oooh, look, the LOSERS are here... How cute!"
pa "And Max is wearing the coveted \"Swimbelt of Veri-Bosti Academy\", which will be handed out to the winning school after today's competition!"
vi "Kate, what the hell are you doing on this side, it's reserved for team managers!"
k "Oh no, am I supporting the wrong team then?"
stop music
p "I have a bit of time to talk to someone before the competition starts..."
menu:
    "Talk to Kate":
        jump CompKate
    "Talk to Maddy":
        jump CompMaddy
    "Talk to Viviane":
        jump CompViviane
    "Talk to Brittany":
        jump CompBrittany

label CompKate:
$ compkate = True
scene compkatetalk01 with dissolve
$ renpy.pause(1.0, hard=True)
k "Hi [name]! I put my swimsuit on, but apparently, I don't get to swim, YIPPEE!"
p "But you'll support our team, right?"
k "Of course! Especially that Max boy. He also offered to meet me in the showers after the competition, I don't know why he wants to meet there..."
p "You shouldn't support or meet with him, Kate, he's on the opposing team for crying out loud!"
scene compkatetalk02 with dissolve
$ renpy.pause(1.0, hard=True)
k "Ooh, sorry,I didn't know. So I'm supporting you then?"
p "That's right, you're supporting ME!"
if lust_points[11] <= 8:
    window hide
    $  lust_points[11] += 1
    $ score += 1
    show lust01:
        xalign 0.3 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
k "Alright, I got it. I think."
jump CompStart02

label CompMaddy:
$ compmaddy = True
scene compmaddytalk01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah. Maddy is doing some stretching exercises. Maybe I should join her..."
scene compmaddytalk02 with dissolve
$ renpy.pause(1.0, hard=True)
md "There you are. Stretch with me [name], we both need to be in TOP form for the relay."
p "Ok... What should I do?"
scene compmaddytalk03 with dissolve
$ renpy.pause(1.0, hard=True)
md "Just do the same as me..."
p "(Fuck, is she spreading her legs for me or what?)"
scene compmaddytalk04 with dissolve
$ renpy.pause(1.0, hard=True)
md "And stop mumbling while you do it, I could hear what you said."
p "*oops*"
scene compmaddytalk05 with dissolve
$ renpy.pause(1.0, hard=True)
md "There. That wasn't so hard, was it?"
if stamina <= 4:
    window hide
    $ stamina += 1
    show stamina01:
        xalign 0.1 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide stamina01
p "You're right, I feel better already."
md "Let's go to our team's bench, it's about to start."    
jump CompStart02

label CompViviane:
$ compviviane = True
vi "I'm warning you [name], you'd better make sure you bring me back this trophy, it belongs to ME, you hear me?"
p "Gee, teach, ok, I get it. I've got to win."
jump CompStart02

label CompBrittany:
$ compbrittany = True
scene brittanycomp01 with dissolve
$ renpy.pause(1.0, hard=True)
br "[name], I overheard that SLUT cheerleader talk about a special swimming method that Max guy uses..."
p "What is it?"
br "Apparently, he uses \"Cum Propulsion\". You'd better watch out, I really want US to WIN!"
p "Thanks for the tip Brittany. I'm actually surprised you're here to cheerlead us, we're the junior team."
scene team01reaction04 with dissolve
$ renpy.pause(1.0, hard=True)
br "I ALWAYS support ALL our school's sports team. H-A-R-D-C...."
p "Ok, I think I know the rest, thanks, I'd better get going, it's about to start."
$ knowpropulsion = True

label CompStart02:
scene pamelacomp02 with dissolve
$ renpy.pause(1.0, hard=True)
pa "First up, Quentin from Hardcox High vs Max from Lycée de Sainte-Nitouche in the 100m crawl!"
scene quentinswim01 with dissolve
$ renpy.pause(1.0, hard=True)
rb "let me do a few push-ups with one hand first... You're not training Quentin, you already know you're going to LOSE?"
q "I'm not feeling well, this is going to be so humiliating and Viviane is going to have a go at me, please let me win!"
rb "In your DREAMS! I want to keep that title and I WILL!"
scene quentinswim02a with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/racestart.wav"
pa "On your marks... Go!"
scene quentinswim02b with dissolve
$ renpy.pause(1.0, hard=True)
q "Oh no, that water looks bigly WET!"
play sound "Sounds/diving.mp3"
scene quentinswim03 with dissolve
play music "Sounds/swimming.mp3"
$ renpy.pause(1.0, hard=True)
play sound "Sounds/cheering.mp3"
pa "And unsurprisingly, Max takes the lead early on!"
scene team01reaction02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Come on, Quentin, you can do it!"
md "Move your legs godammit!"
vi "You'd better catch up with him Quentin or I swear..."
scene quentinswim04 with dissolve
$ renpy.pause(1.0, hard=True)
pa "And Max is already on the last leg on the race while Quentin still hasn't reached the halfway point! This is a going to be a CRUSHING victory for Sainte-Nitouche!"
scene team01reaction01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Kick him in the groin Quentin, it's your last chance!"
md "I can't watch this..."
vi "What the...?"
scene team02reaction02 with dissolve
$ renpy.pause(1.0, hard=True)
hg "Go on Max, I'll wait for you at the finish!"
scene quentinswim05 with dissolve
$ renpy.pause(1.0, hard=True)
stop music
stop sound
play sound "Sounds/applause.mp3"
pa "And Max wins the race! EASILY."
scene quentinswim06 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/kissing.mp3"
hg "Oooh, Max, watching you has made me so HORNY! Let me kiss you!"
scene quentinswim07 with dissolve
$ renpy.pause(1.0, hard=True)
hg "YES! Play with my big titties, while I grind my arse against your MEGA-DONG!"
rb "Don't worry, when this competition is over, I'll plaster them with a TON of my teenage cum!"
hg "Mmmh, I can't WAIT!"
scene pamelacomp02 with dissolve
$ renpy.pause(1.0, hard=True)
pa "*cough* How about you do that somewhere else please, this is a SWIMMING COMPETITION."
play sound "Sounds/applause.mp3"
pa "Ahem... Next up is Maddy against Suzanne in the women's 100m crawl!"
scene maddyswim01 with dissolve
play sound "Sounds/racestart.wav"
$ renpy.pause(1.0, hard=True)
scene maddyswim02 with dissolve
play sound "Sounds/diving.mp3"
$ renpy.pause(1.0, hard=True)
play music "Sounds/swimming.mp3"
pa "And here they go!"
scene maddyswim03 with dissolve
play sound "Sounds/cheering.mp3"
$ renpy.pause(1.0, hard=True)
pa "Maddy has a slight lead, but Suzanne is catching up!"
scene team01reaction04 with dissolve
$ renpy.pause(1.0, hard=True)
br "Come on Maddy, beat that Sainte-Nitouche WHORE!"
scene team02reaction02 with dissolve
$ renpy.pause(1.0, hard=True)
hg "Suzanne! Suzanne! Think of Max's huge cock in your pussy and give it all you've got!"
scene pamelacomp01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "And Maddy is still ahead a mid-point! But the race is close and there are still 50m to go."
scene team01reaction05 with dissolve
$ renpy.pause(1.0, hard=True)
p "You can do it Maddy! Woo-OOH!"
q "Please make her win God, otherwise we've already lost!"
vi "That's it Maddy, arms, legs, arms, YES!"
scene maddyswim04 with dissolve
$ renpy.pause(1.0, hard=True)
pa "And Maddy is first to touch, she wins that round!"
stop music
stop sound
play sound "Sounds/applause.mp3"
vi "YES, finally, a VICTORY!"
p "I guess I'm up next... I have a bit of time to chat someone up though..."

menu:
    "Talk to Kate" if compkate == False:
        jump CompKate02
    "Talk to Maddy" if compmaddy == False:
        jump CompMaddy02
    "Talk to Viviane" if compviviane == False:
        jump CompViviane02
    "Talk to Brittany":
        jump CompBrittany02

label CompKate02:
scene compkatetalk01 with dissolve
$ renpy.pause(1.0, hard=True)
k "Hi [name]! I put my swimsuit on, but apparently, I don't get to swim, YIPPEE!"
p "But you're supporting our team, right?"
k "Of course! Especially that Max boy. He also offered to meet me in the showers after the competition, I don't know why he wants to meet there..."
p "You shouldn't support or meet with him, Kate, he's on the opposing team for crying out loud!"
scene compkatetalk02 with dissolve
$ renpy.pause(1.0, hard=True)
k "Ooh, sorry,I didn't know. So I'm supporting you then?"
p "That's right, you're supporting ME! I'm next on top of that."
if lust_points[11] <= 8:
    window hide
    $  lust_points[11] += 1
    $ score += 1
    show lust01:
        xalign 0.3 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
k "Alright, I got it. I think."
jump CompStart03

label CompMaddy02:
scene compmaddytalk01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah. Maddy is doing some stretching exercises. Maybe I should join her..."
scene compmaddytalk02 with dissolve
$ renpy.pause(1.0, hard=True)
md "There you are. Stretch with me [name], we both need to be in TOP form for the relay."
p "Ok... What should I do?"
scene compmaddytalk03 with dissolve
$ renpy.pause(1.0, hard=True)
md "Just do the same as me..."
p "(Fuck, is she spreading her legs for me or what?)"
scene compmaddytalk04 with dissolve
$ renpy.pause(1.0, hard=True)
md "And stop mumbling while you do it, I could hear what you said."
p "*oops*"
scene compmaddytalk05 with dissolve
$ renpy.pause(1.0, hard=True)
md "There. That wasn't so hard, was it?"
if stamina <= 4:
    window hide
    $ stamina += 1
    show stamina01:
        xalign 0.1 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide stamina01
p "You're right, I feel better already."
md "Let's get ready, it's about to be our turn to SHINE for our school!"    
jump CompStart03

label CompViviane02:
scene compvivianetalk01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Don't waste my time [name], I need to think of a STRATEGY."
if knowpropulsion:
    p "I can help. Have you ever heard of \"Cum Propulsion\"? If you teach me, I could use it. That Max guy on the other team uses it."
    vi "\"Cum Propulsion?\" Yes, I remember reading about it in a swimming instruction manual, but I never thought it would work, it sounds so silly."
    vi "It requires getting hard but not too hard that you lose aerodynamicity, followed by a cum eruption directed towards the feet that propulses the swimmer forward."
    p "I think I got it... Thanks, Viviane."
    scene compvivianetalk02 with dissolve
    $ renpy.pause(1.0, hard=True)
    vi "If you're going to use this nonsense, you'd better do it at the RIGHT time, you hear me?"
    p "Roger that."
    $ knowpropulsion02 = True
jump CompStart03
        
label CompBrittany02:
if compbrittany == True:
    scene brittanycomp02 with dissolve
    $ renpy.pause(1.0, hard=True)
    br "Last race, you're up, don't let us down [name]!"
    br "H-A-R-D-C.."
    p "COCKS!"
    scene brittanycomp01 with dissolve
    $ renpy.pause(1.0, hard=True)
    br "What did you just blurt out? Are you gay or something?"
    p "No!"
    br "Anyway, I learnt more about that cum propulsion technique. Apparently, you have to have a semi and then erupt towards your feet."
    p "That's it? That's the technique of cum propulsion."
    br "Yeah, That's it. So use it and make us PROUD! H-A-R-D.."
    p "Right, right."
    $ knowpropulsion02 = True
    jump CompStart03
if compbrittany == False:
    scene brittanycomp01 with dissolve
    $ renpy.pause(1.0, hard=True)
    br "[name], I overheard that SLUT cheerleader talk about a special swimming method that Max guy uses..."
    p "What is it?"
    br "Apparently, he uses \"Cum Propulsion\". You'd better watch out, I really want US to WIN!"
    p "Thanks for the tip Brittany. I'm actually surprised you're here to cheerlead us, we're the junior team."
    scene team01reaction04 with dissolve
    $ renpy.pause(1.0, hard=True)
    br "I ALWAYS support ALL our school's sports team. H-A-R-D-C...."
    p "Ok, I think I know the rest, thanks, I'd better get going, it's about to start."
    $ knowpropulsion = True
    
label CompStart03:
$ hour += 1
scene pamelacomp01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "And now for the final and deciding round... The mixed relay! The girls start first."
play sound "Sounds/applause.mp3"
scene maddyswim01 with dissolve
play sound "Sounds/racestart.wav"
$ renpy.pause(1.0, hard=True)
scene maddyswim02 with dissolve
play sound "Sounds/diving.mp3"
$ renpy.pause(1.0, hard=True)
play music "Sounds/swimming.mp3"
pa "And here they go!"
scene maddyswim03b with dissolve
play sound "Sounds/cheering.mp3"
$ renpy.pause(1.0, hard=True)
pa "Maddy and Suzanne are about level, this race is getting so EXCITING!"
scene relay02 with dissolve
$ renpy.pause(1.0, hard=True)
pa "And they are both STILL level as the relay with the boys is about to engage..."
scene relay03 with dissolve
play sound "Sounds/racestart.wav"
$ renpy.pause(1.0, hard=True)
scene relay04 with dissolve
play sound "Sounds/diving.mp3"
$ renpy.pause(1.0, hard=True)
scene relay05 with dissolve
play sound "Sounds/cheering.mp3"
play music "Sounds/swimming.mp3"
$ renpy.pause(1.0, hard=True)
pa "And the boys are now battling it out!"
show relay05b with fastdissolve
pa "But Max is suddenly moving fast ahead, as if he had an engine in his belly!"
if knowpropulsion02:
    p "I'd better use cum propulsion to catch up with him!"
    $ stamina -= 1
    window hide
    show staminaminus01:
        xalign 0.4 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
    p "ooh, that's good..."
    jump LevelMax
if knowpropulsion02 == False:
    p "Shit!"
    menu:
        "Dig into your stamina reserves to catch up with him (-2 stamina)":
            $ stamina -= 2
            window hide
            show staminaminus02:
                xalign 0.4 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/panting.mp3"
            $ renpy.pause(2, hard=True)
            hide staminaminus02
            jump LevelMax
        "Let that arsehole swim ahead for a while...(-1 stamina)":
            $ stamina -= 1
            window hide
            show staminaminus01:
                xalign 0.4 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/panting.mp3"
            $ renpy.pause(2, hard=True)
            hide staminaminus01
            jump AheadMax

label LevelMax:
play sound "Sounds/cheering.mp3"
show relay05c with fastdissolve
$ renpy.pause(1.0, hard=True)
pa "But [name] has not said his final word and levels with Max! Oh, this race is so exciting!"
scene relay06
pa "And now the two boys are level as we head for the final stretch!"
menu:
    "Use your stamina reserves to get ahead of him (-3 stamina)" if stamina >= 3:
        show relay06c with fastdissolve
        p "Yes, I can do it!"
        pa "[name] is now in the lead!"
        $ stamina -= 2
        window hide
        show staminaminus02:
            xalign 0.4 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/panting.mp3"
        $ renpy.pause(2, hard=True)
        hide staminaminus02
        hide relay06c
        show relay06d
        with fastdissolve
        pa "Not anymore! This race is breathtaking!"
        hide relay06d
        show relay06f
        with fastdissolve
        $ stamina -= 1
        window hide
        show staminaminus01:
            xalign 0.4 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/panting.mp3"
        $ renpy.pause(2, hard=True)
        hide staminaminus01
        pa "Sorry, [name] is yet again ahead!"        
        jump EndRyanAhead
    "Continue swimming at your normal pace (-2 stamina)" if stamina >= 2:
        show relay06c with fastdissolve
        p "Yes, I can do it!"
        pa "[name] is now in the lead!"
        $ stamina -= 2
        window hide
        show staminaminus02:
            xalign 0.4 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/panting.mp3"
        $ renpy.pause(2, hard=True)
        hide staminaminus02
        hide relay06c
        show relay06d
        with fastdissolve
        pa "Not anymore! This race is breathtaking!"
        jump EndLevel
    "Let him swim ahead (-1 stamina)" if stamina >= 1:
        show relay06e with fastdissolve
        $ stamina -= 1
        window hide
        show staminaminus01:
            xalign 0.4 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/panting.mp3"
        $ renpy.pause(2, hard=True)
        hide staminaminus01
        pa "Max suddenly takes the lead!"
        jump EndMaxAhead
        
label AheadMax:
play sound "Sounds/cheering.mp3"
scene relay06
show relay06b
with dissolve
$ renpy.pause(1.0, hard=True)
pa "And Max is still ahead of [name] as we head for the final stretch!"
menu:
    "Use your stamina reserves to catch up with him (-2 stamina)" if stamina >= 2:
        $ stamina -= 2
        window hide
        show staminaminus02:
            xalign 0.4 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/panting.mp3"
        $ renpy.pause(2, hard=True)
        show relay06d with fastdissolve
        pa "[name] tries hard to level with Max!"
        jump EndLevel        
    "Use your stamina reserves not to fall too far behind (-1 stamina)" if stamina >= 1:
        $ stamina -= 1
        window hide
        show staminaminus01:
            xalign 0.4 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/panting.mp3"
        $ renpy.pause(2, hard=True)
        show relay06e with fastdissolve
        pa "Max barrels in the lead with only meters to go!"
        jump EndMaxAhead

label EndLevel:
play sound "Sounds/cheering.mp3"
scene relayend01 with fastdissolve
$ renpy.pause(1.0, hard=True)
pa "Oh my God, they are literally within inches of each other!"
p "I should give it all I've got to try and win!"
if stamina <=0:
    p "But I have no stamina left..."
    jump EndRelayMaxWin
if stamina >=1:
    $ stamina -= 1
    window hide
    show staminaminus01:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
    p "Please, let me win!"
    jump EndRelayMCWin
    
label EndRyanAhead:
play sound "Sounds/cheering.mp3"
scene relayend01
show relayend02
with fastdissolve
$ renpy.pause(1.0, hard=True)
pa "[name] looks like he's heading for the win but Max is still on his tails!"
p "I should still give it all I've got to make sure I win!"
if stamina <=0:
    p "But I have none left... Hopefully, it will be enough anyway."
    jump EndRelayMCWin
if stamina >=1:
    $ stamina -= 1
    window hide
    show staminaminus01:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
    p "Please, let me win!"
    jump EndRelayMCWin

label EndMaxAhead:
play sound "Sounds/cheering.mp3"
scene relayend01
show relayend03
with dissolve
p "I'm gonna have to use all my stamina to catch up with him!"
if stamina <=0:
    p "But I have none left..."
    jump EndRelayMaxWin
if stamina <=1:
    $ stamina -= 1
    window hide
    show staminaminus01:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
    p "Please, let me win!"
    jump EndRelayMaxWin
if stamina >=2:
    $ stamina -= 2
    window hide
    show staminaminus02:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    p "Please, let me win!"
    jump EndRelayMCWin
    
label EndRelayMaxWin:
scene relayendmaxwin01 with dissolve
stop music
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
rb "I win! I keep the trophy..."
rc "Come out of the water my hero! I NEED to admire your glorious body..."
hg "And I NEED to feel your POWERFUL muscles... ALL OVER!"
scene relayendmaxwin02 with dissolve
$ renpy.pause(1.0, hard=True)
rc "*kiss* You're such a STUD! I'm so happy to be your girfriend... And I'll NEVER be anyone else's!"
hg "Me too! Your MONSTER COCK is the only one I want! The ONLY one that can satisfy me..."
rb "You hear that [name]? By next week, your WHOLE SCHOOL will be just like them... Delirious with lust for my teenage ALPHA-BULLCOCK!"
rc "Show it to us... ROCK-HARD!"
scene relayendmaxwin03 with dissolve
$ renpy.pause(1.0, hard=True)
rc "I never get tired of seeing this MONSTER fully-hard!"
play sound "Sounds/lick.mp3"
hg "And fully LOADED too! His balls are ssoo SWOLLEN. I bet we can make him cum another load in no time!"
rb "Imagine all your classmates on their knees worshipping my donkey-cock... By next week, you won't have to imagine it anymore!"
p "FUCK YOU! I just didn't have enough time to train, that's all. Next year, we'll beat you guys FOR SURE!"
scene relayendmaxwin04 with flash
play sound "Sounds/randyboycumming02.mp3"
$ renpy.pause(1.0, hard=True)
rb "RHAA! See how powerful my shots are? This is why they all come back to ME!"
p "I come just as much if not more for your information."
rc "Cover us in your teenage MEGA-LOAD, Max!"
hg "And then, FUCK us and FILL us BOTH with ounces of your virile spunk!"
rb "Of course, I have plenty of cum in store for you girls... But we should first go and get my winner's belt back."
p "I'm outta here, this is getting too humiliating, I don't want to see this douchebag with his trophy belt."
scene relayendmaxwin05 with fade
stop sound
$ hour += 1
$ renpy.pause(1.0, hard=True)
q "It was tough... He got the trophy, proudly displaying his bulge in front of everyone... Viviane is furious with you too, I'm warning you."
p "Don't tell me anything more... I have more important things to do today. HUMILIATE JOSE!"
q "Oh yes, I remember now, it's the end of the competition today isn't it? I hope you beat him, I hate this arsehole!"
p "Leave me alone now. I'll take a shower and leave to finish off some things..."
jump SwimCompEnd

label EndRelayMCWin:
$ swimcompwin = True
scene relaywin01 with dissolve
stop music
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
p "I win! We get the trophy!"
md "Oh, well done [name], this is so great, I'm... I just want to kiss you!"
scene relaywin02 with dissolve
play sound "Sounds/kissing.mp3"
$ renpy.pause(1.0, hard=True)
if (lust_points[14] ==9):
    window hide
    $ lust_points[14] += 1
    $ score += 1
    show lust01:
        xalign 0.5 yalign 0.5
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
    $ maddyfucksunday = True
    md "I'll be at the beach relaxing this afternoon... Why don't you join me there? I know a secluded spot by a cabin..."
    p "Ah yes, the cabin where you stayed during your kidnapping. You DO know that place pretty well..."
    jump EndRelayWin02
if (lust_points[14] <=8):
    window hide
    $ lust_points[14] += 2
    $ score += 2
    show lust02:
        xalign 0.5 yalign 0.5
        linear 1.0 yalign 0.3
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
    if (lust_points[14] >=10):
        show epiclust:
            xalign 0.5 yalign 0.2
            zoom 0.5
            linear 2.0 zoom 1.0
        play sound "Sounds/epiclust.mp3"
        $ renpy.pause(4.0, hard=True)
        hide epiclust
        $ maddyfucksunday = True
        md "I'll be at the beach relaxing this afternoon... Why don't you join me there? I know a secluded spot by a cabin..."
        p "Ah yes, the cabin where you stayed during your kidnapping. You DO know that place pretty well..."
        jump EndRelayWin02
    md "Even though I'm really horny right now, I'm just not horny enough... Sorry, you'll end the game without fucking ME!"
    p "Gee, how did I fuck up that badly?"    
label EndRelayWin02:
md "That girl behind me is ssoo jealous! Let's get our trophy now. The belt is for YOU!"
$ hour += 1
scene relaywintrophy with dissolve
$ renpy.pause(1.0, hard=True)
pa "And the belt goes to... Hardcox High!"
play sound "Sounds/applause.mp3"
scene relaywintrophy02 with dissolve
$ renpy.pause(1.0, hard=True)
vi "I'm proud of you [name], your performance in the relay is what made us win this trophy..."
pa "I think the champion needs to rest a bit though. Why don't you go and take a shower to relax? We'll celebrate... later. *wink*"
p "Thanks, I really need a shower indeed right now..."

label SwimCompEnd:
stop music
scene showercomp01 with dissolve
play music "Sounds/shower.mp3"
p "Mmmh, a nice shower after this exhausting competition..."
if (stamina <= 4) and showertaken08 == False:
    window hide
    $ stamina += 1
    show stamina01:
        xalign 0.4 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide stamina01
if vivianefucked == False and pamelafucked == False and (lust_points[23] >=8) and (lust_points[18] <=7) and swimcompwin:
    scene showerfuckviviane01 with dissolve
    play music "Sounds/shower.mp3"
    vi "Well, who do we have here taking a shower... The CHAMPION! In all his glorious naked GLORY!"
    if (lust_points[23] ==9):
        window hide
        $ lust_points[23] += 1
        $ score += 1
        show lust01:
            xalign 0.4 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
    if (lust_points[23] <=8):
        window hide
        $ lust_points[23] += 2
        $ score += 2
        show lust02:
            xalign 0.4 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
    show epiclust:
        xalign 0.4 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    if vivianefucked:
        vi "Well, we KNOW this place don't we? And all the ways you can fuck me with your GIANT TEENAGE COCK. So let's do it again [name]!"
    if vivianefucked == False:
        vi "I see you for what you are now... A SEX GOD to ravish my body!"
    p "Alright!"
    jump VivianeFuckDay08

if (lust_points[18] >=8) and (lust_points[23] <=7) and swimcompwin:
    scene showerfuckpamela01 with dissolve
    play music "Sounds/shower.mp3"
    pa "Well, who do we have here taking a shower... The CHAMPION! In all his glorious naked GLORY!"
    if (lust_points[18] ==9):
        window hide
        $ lust_points[18] += 1
        $ score += 1
        show lust01:
            xalign 0.4 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
    if (lust_points[18] <=8):
        window hide
        $ lust_points[18] += 2
        $ score += 2
        show lust02:
            xalign 0.4 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
    show epiclust:
        xalign 0.4 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    if pamelafucked:
        pa "A new place for you to fuck me with your GIANT TEENAGE COCK. What do you say, STUD?"
    if pamelafucked == False:
        pa "I see you for what you are now... A SEX GOD to ravish my body!"
    p "Alright!"
    pa "Let's move to the lockers area, Someone might see us and I like my sex DANGEROUS and ROUGH!"
    jump PamelaShowerFuckDay08

if  (lust_points[18] >=9) and (lust_points[23] >=9) and swimcompwin:
    scene showerfuckboth01 with dissolve
    play music "Sounds/shower.mp3"
    pa "Well, who do we have here taking a shower... The CHAMPION! In all his glorious naked GLORY!"
    vi "The champion who deserves a sexy REWARD..."
    if (lust_points[18] ==9):
        window hide
        $ lust_points[18] += 1
        $ score += 1
        show lust01:
            xalign 0.8 yalign 0.5
            linear 1.0 yalign 0.3
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        show epiclust:
            xalign 0.8 yalign 0.2
            zoom 0.5
            linear 2.0 zoom 1.0
        play sound "Sounds/epiclust.mp3"
        $ renpy.pause(4.0, hard=True)
        hide epiclust
    if (lust_points[23] ==9):
        window hide
        $ lust_points[23] += 1
        $ score += 1
        show lust01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
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
    window hide
    show doubledelight:
        xalign 0.6 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/delight.mp3"
    $ renpy.pause(4.0, hard=True)
    hide doubledelight
    p "Alright! A threesome coming my way! WOo-ooh!"
    jump BothShowerFuckDay08
stop music
p "And now, I'll eat my sandwich..."
scene gymlockereat with dissolve
show mceating
with dissolve
$ renpy.pause(1.0, hard=True)
p "What are you looking at? You never saw a guy eat a sandwich?"
$ hour += 1
hide mceating
show mcate
with dissolve
p "Ah, now I'm not hungry anymore. Amazing what eating does to your body. Let's move on then..."
jump BurbsDay08

label VivianeFuckDay08:
stop music
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

label VivianeFuckChoiceDay08:
scene vivianechoice with dissolve
$ renpy.pause(1.0, hard=True)
vi "So... What are you going to do to me now [name]?"
menu:
    "I want to take you up the arse and work my hip muscles!" if (vivianeanal == False):
        vi "Great idea! They really help improve the speed of your legs underwater..."
        jump VivianeAnalDay08
    "I'll hold you up while I pummel my great pile-driver in your mouth!" if (vivianeblow == False):
        vi "Mmh, that sounds so hot! Lift me up in your muscular arms and lick my pussy!"
        jump VivianeBlowDay08
    "Let's get on the floor so you can ride my huge dong!" if (vivianepussy == False):
        vi "So I'll be doing all the work? I guess you deserve it STUD!"
        jump VivianePussyDay08
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (vivianepussy == True) and (vivianeblow == True) and (vivianeanal == True):
        vi "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump VivianeMovieDay08

label VivianeAnalDay08:
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
label VivianeAnalDay08b:
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
        jump VivianeAnalDay08b
    "Move on":
        pass
scene vivianeanal03 with dissolve
$ renpy.pause(1.0, hard=True)
vi "My God, it feels like my arse is nothing more than a gaping hole now..."
p "It sure looks like it from where I'm standing..." 
jump VivianeFuckChoiceDay08

label VivianeBlowDay08:
$ vivianeblow = True
scene vivianeoral01 with dissolve
play sound "Sounds/vivianeblow01.mp3"
$ renpy.pause(10.0, hard=True)
vi "Mmh, you're so strong holding me like that!"
p "That's cos I need to lick that tasty pussy of yours!"
vi "While I suck on that giant shaft of yours! It's a deal!"
label VivianeBlowDay08b:
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
        jump VivianeBlowDay08b
    "Move on":
        pass    
vi "I think I dislocated my jaw..."
p "It happens...Let's move on to something else." 
jump VivianeFuckChoiceDay08    

label VivianePussyDay08:
$ vivianepussy = True
scene vivianecowgirl01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Keep steady mustang! This cowgirl is going to ride you into submission!"
p "Oh fuck, I think I'm in for a wild ride!" 
label VivianePussyDay08b:
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
        jump VivianePussyDay08b
    "Move on":
        pass    
vi "How was it for you stallion?"
p "Damn, I feel like I rode all the way to California..." 
jump VivianeFuckChoiceDay08    

label VivianeMovieDay08:
scene vivianeprefuck with dissolve
p "I've pinned you down against the lockers... Time to smash the padlock on your uterus with my sledgehammer!"
vi "OOOh, you have the worst lines [name], but I forgive you because you're about to give me what I want, that fat young bullcock of yours! FUCK ME!"
play music "Sounds/vivianefuck.mp3"
show vivianefuck
show cum
call screen vivianefuckday08
screen vivianefuckday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("VivianeFuckCumDay08")

label VivianeFuckCumDay08:
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
p "Sure I could, but I'm afraid I have to go Viviane. I have a rival I need to meet... And HUMILIATE!"
vi "I understand stud... And I'm sure you'll humiliate him GOOD!"
$ vivianefucked = True
$ hour += 1
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
if (pamelafucked == True) and (achievement.has("watersport") == False):
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
stop music

jump BurbsDay08

label PamelaShowerFuckDay08:
stop music
scene pamelaprefuck02b with dissolve
$ renpy.pause(1.0, hard=True)
pa "Now come and RAVISH my body, CHAMPION!"
jump PamelaFuckChoiceDay08b
label PamelaFuckChoiceDay08:
scene pamelaprefuck02b with dissolve
$ renpy.pause(1.0, hard=True)
pa "So... What are you going to do to me now [name]?"
label PamelaFuckChoiceDay08b:
menu:
    "I want to take you up the arse and work my hip muscles!" if (pamelaanalb == False):
        pa "Great idea! They really help improve the speed of your legs underwater..."
        jump PamelaAnalDay08
    "I'll hold you up while I pummel my great pile-driver in your mouth!" if (pamelablowb == False):
        pa "Mmh, that sounds so hot! Lift me up in your muscular arms and lick my pussy!"
        jump PamelaBlowDay08
    "Let's get on the floor so you can ride my huge dong!" if (pamelapussyb == False):
        pa "So I'll be doing all the work? I guess you deserve it STUD!"
        jump PamelaPussyDay08
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (pamelapussyb == True) and (pamelablowb == True) and (pamelaanalb == True):
        pa "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump PamelaMovieDay08

label PamelaAnalDay08:
$ pamelaanalb = True
p "First, I'll lick that bunghole to warm it up..."
pa "A rimjob? Mmh, you really are a DIRTY boy aren't you [name]?"
scene pamelalick01 with dissolve
$ renpy.pause(1.0, hard=True)
scene pamelalick02 with dissolve
play sound "Sounds/womansigh.mp3"
$ renpy.pause(1.0, hard=True)
pa "YYYES! Your tongue is making me tingle all over!"
scene pamelalick03 with dissolve
play sound "Sounds/womansigh.mp3"
$ renpy.pause(1.0, hard=True)
pa "You do that so well! But don't kiss me afterwards if you don't mind..."
play sound "Sounds/vivianelick.mp3"
scene pamelalick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelalick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelalick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelalick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelalick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelalick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelalick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelalick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelalick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelalick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelalick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelalick03 with dissolve
$ renpy.pause(0.3, hard=True)
pa "Oooh, my little backdoor is now moist and ready for your massive teenage fuckmeat [name]!"
p "Then it's time to turn in into a wide gaping hole..."
scene pamelaanal01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "FUCK! You're sssooo BIG! I feel like I'm getting impaled on a giant spike!"
p "Hang on in there, I'm gonna spike your arse some more..."
scene pamelaanal02 with dissolve
$ renpy.pause(0.3, hard=True)
pa "YES! Fuck my arse [name]! FUCK ME HARD!"
label PamelaAnalDay08b:
play sound "Sounds/vivianeanal.mp3"
scene pamelaanal01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaanal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaanal01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaanal02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaanal01
$ renpy.pause(0.3, hard=True)
scene pamelaanal02
$ renpy.pause(0.3, hard=True)
scene pamelaanal01
$ renpy.pause(0.3, hard=True)
scene pamelaanal02
$ renpy.pause(0.3, hard=True)
scene pamelaanal01
$ renpy.pause(0.3, hard=True)
scene pamelaanal02
$ renpy.pause(0.3, hard=True)
scene pamelaanal01
$ renpy.pause(0.3, hard=True)
scene pamelaanal02
$ renpy.pause(0.3, hard=True)
scene pamelaanal01
$ renpy.pause(0.3, hard=True)
scene pamelaanal02
$ renpy.pause(0.3, hard=True)
scene pamelaanal01
$ renpy.pause(0.3, hard=True)
scene pamelaanal02
$ renpy.pause(0.3, hard=True)
scene pamelaanal01
$ renpy.pause(0.3, hard=True)
scene pamelaanal02
$ renpy.pause(0.3, hard=True)
scene pamelaanal01
$ renpy.pause(0.3, hard=True)
scene pamelaanal02
$ renpy.pause(0.3, hard=True)
scene pamelaanal01
$ renpy.pause(0.3, hard=True)
scene pamelaanal02
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump PamelaAnalDay08b
    "Move on":
        pass
scene pamelaanal03 with dissolve
$ renpy.pause(1.0, hard=True)
pa "My God, it feels like my arse is nothing more than a gaping hole now..."
p "It sure looks like it from where I'm standing..." 
jump PamelaFuckChoiceDay08

label PamelaBlowDay08:
$ pamelablowb = True
scene pamelaoral01 with dissolve
play sound "Sounds/vivianeblow01.mp3"
$ renpy.pause(10.0, hard=True)
pa "Mmh, you're so strong holding me like that!"
p "That's cos I need to lick that tasty pussy of yours!"
pa "While I suck on that giant shaft of yours! It's a deal!"
label PamelaBlowDay08b:
scene pamelaoral02 with dissolve
play sound "Sounds/vivianeblow02.mp3"
$ renpy.pause(0.3, hard=True)
scene pamelaoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral03 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelaoral02 with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump PamelaBlowDay08b
    "Move on":
        pass    
pa "I think I dislocated my jaw..."
p "It happens...Let's move on to something else." 
jump PamelaFuckChoiceDay08    

label PamelaPussyDay08:
$ pamelapussyb = True
scene pamelacowgirl01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Keep steady mustang! This cowgirl is going to ride you into submission!"
p "Oh fuck, I think I'm in for a wild ride!" 
label PamelaPussyDay08b:
scene pamelacowgirl02 with dissolve
play sound "Sounds/vivianecowgirl.mp3"
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump PamelaPussyDay08b
    "Move on":
        pass    
pa "How was it for you stallion?"
p "Damn, I feel like I rode all the way to California..." 
jump PamelaFuckChoiceDay08    

label PamelaMovieDay08:
scene pamelaprefuck02b with dissolve
p "I've pinned you down against the lockers... Time to smash the padlock on your uterus with my sledgehammer!"
pa "OOOh, you have the worst lines [name], but I forgive you because you're about to give me what I want, that fat young bullcock of yours! FUCK ME!"
play music "Sounds/vivianefuck.mp3"
show pamelaanim
show cum
call screen pamelafuckday08
screen pamelafuckday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PamelaFuckCumDay08")

label PamelaFuckCumDay08:
hide pamelaanim
hide cum
stop music
scene pamelalockercum01
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
pa "YES! Fill me up like a sperm tank!"
p "So strong! I'm cumming non-stop!"
pa "Mmmh, yes stallion, I can feel it sloshing around inside me! Pull out and dump the rest on my body please!"
scene pamelalockercum02 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "Oh, Fuck, still spraying, still ssoo good!"
pa "Damn boy, my pussy really got those great big cum factories of yours working overtime didn't they?"
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
scene pamelalockercum03 with dissolve
play sound "Sounds/kissing.mp3" 
$ renpy.pause(1.0, hard=True)
pa "Now kiss me stud! And come with me in the showers so we can get cleaned up!"
scene pamelalockercum04 with dissolve
play music "Sounds/shower.mp3"
$ renpy.pause(1.0, hard=True)
pa "Mmh, I love your body... And that MONSTERCOCK! Can you get hard again and fuck me?"
p "Sure I could, but I'm afraid I have to go Pamela. I have a rival I need to meet... And HUMILIATE!"
pa "I understand stud... And I'm sure you'll humiliate him GOOD!"
$ pamelafucked = True
$ hour += 1
if (pamelajosewin == False):
    p "(She didn't notice I took a picture of her boobs plastered in my cum... Now I'll send it to José)."
    $ pamelawin = True 
if (vivianefucked == True) and (achievement.has("watersport") == False):
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
stop music
jump BurbsDay08

label BothShowerFuckDay08:
stop music
p "But first... Get on your knees and worship my cock Pamela. A CHAMPION'S COCK!"
pa "Of course [name], anything for you... Mitch is a wimp compared to your GODLY body!"
scene showerfuckbothpreblow01 with dissolve
play sound "Sounds/kissing.mp3" 
$ renpy.pause(1.0, hard=True)
pa "Of course [name], anything for you... Mitch is a wimp compared to your GODLY body!"
p "And now, open your mouth WIDE!"
scene showerfuckboth03 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Wow Pamela, I didn't know you could gobble such a MASSIVE piece of BOYMEAT so easily!"
p "Let's make it harder, I'm gonna fuck that gaping mouth of yours!"
scene showerfuckpreblow03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready Pamela?"
pa "Ggglrub.... Y...uusggllr..."
label ShowerThreesomeMouthFuck:
play music "Sounds/hardsucking.mp3"
scene showerfuckpreblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow03 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow02
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow03
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow02
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow03
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow02
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow03
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow02
$ renpy.pause(0.3, hard=True)
scene showerfuckpreblow03
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        p "I ain't done with that mouth YET!"
        jump ShowerThreesomeMouthFuck
    "Move on":
        scene showerfuckboth03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Let's move to the locker area, my cock DEMANDS some more attention!"
        vi "And we'll make sure you GET that attention [name]..."
        pass
        
label ThreesomeShowerFuckChoice:
scene showerthreesomeprefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "FUCK! Look at that MONSTER DONG! Already leaking pre-cum... Mmmh... What shall we do about it [name]?"
label ThreesomeShowerFuckChoiceb:
menu:
    "I want some special time with Viviane... Against the lockers!" if vivianelockerc == False:
        vi "The lockers will lose in that fight... But I' =m in!"
        jump VivianeThreesomefuckDay08
    "Pamela, you're the type to ride me like a cowgirl!" if pamelapussyc == False:
        pa "you got that right, BULL-STUD!"
        jump PamelaBull08
    "Viviane, your mouth on my cock sounds like a perfect patch!" if vivianeoralc == False:
        vi "I have the perfect mouth for your perfect cock indeed!"
        jump VivianeOralc08
    "I'll lift Pamela up in my strong arms while I power-fuck Viviane from behind!" if bothupc == False:
        pa "you got that right, BULL-STUD!"
        jump BothUp08
    "Get on the floor, Pamela. I'm gonna fuck your pussy into submission!" if pamelagroundc == False:
        pa "you got that right, BULL-STUD!"
        jump PamelaGround08
    "Time for me to come inside Pamela's pussy." if (pamelagroundc and bothupc and vivianeoralc and pamelapussyc and vivianelockerc):
        pa "Oh, thank you so much, I'm going to get some CHAMPION CUM in me, yippee!"
        jump BothFinale08

label VivianeThreesomefuckDay08:
$ vivianelockerc = True
scene vivianeprefuck with dissolve
p "I've pinned you down against the lockers... Time to smash the padlock on your uterus with my sledgehammer!"
vi "OOOh, you have the worst lines [name], but I forgive you because you're about to give me what I want, that fat young bullcock of yours! FUCK ME!"
play music "Sounds/vivianefuck.mp3"
show vivianefuck
show cum
call screen vivianefuckday08b
screen vivianefuckday08b:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("VivianeThreesomeCumDay08")

label VivianeThreesomeCumDay08:
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
scene vivianecum03 with dissolve
play sound "Sounds/kissing.mp3" 
$ renpy.pause(1.0, hard=True)
vi "Then kiss me stud! Before we move on to some more HOT FUCKING!"
scene showerthreesomeprefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "So, what next for us, STUD?"
jump ThreesomeShowerFuckChoiceb

label PamelaBull08:
$ pamelapussyc = True
scene pamelacowgirl01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Keep steady mustang! This cowgirl is going to ride you into submission!"
p "Oh fuck, I think I'm in for a wild ride!" 
label PamelaBull08b:
scene pamelacowgirl02 with dissolve
play sound "Sounds/vivianecowgirl.mp3"
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl01 with dissolve
$ renpy.pause(0.3, hard=True)
scene pamelacowgirl02 with dissolve
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        jump PamelaBull08b
    "Move on":
        pass    
pa "How was it for you stallion?"
p "Damn, I feel like I rode all the way to California..." 
jump ThreesomeShowerFuckChoiceb    

label VivianeOralc08:
$ vivianeoralc = True
scene vivianeoral01 with dissolve
play sound "Sounds/vivianeblow01.mp3"
$ renpy.pause(10.0, hard=True)
vi "Mmh, you're so strong holding me like that!"
p "That's cos I need to lick that tasty pussy of yours!"
vi "While I suck on that giant shaft of yours! It's a deal!"
label VivianeOral08b:
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
        jump VivianeOral08b
    "Move on":
        pass    
vi "I think I dislocated my jaw..."
p "It happens...Let's move on to something else." 
jump ThreesomeShowerFuckChoiceb    

label BothUp08:
$ bothupc = True
scene showerup01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Damn, that's a POWERTOOL drilling inside me!"
pa "And some mighty powerful arms lifting me up like I weigh nothing!"
scene showerup03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Don't forget my expert tongue on your pussy..."
vi "Stop talking and FUCK ME!"
label BothUp08b:
play music "Sounds/lesbians.mp3"
scene showerup02 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup01 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup02 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup01 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup02 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup01 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup02 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup01 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup02 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup01 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup02 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup01 with dissolve
$ renpy.pause(0.3, hard=True)
scene showerup02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene showerup01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene showerup02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene showerup01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene showerup02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene showerup01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene showerup02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene showerup01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene showerup02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene showerup01 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene showerup02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene showerup01 with fastdissolve
$ renpy.pause(0.2, hard=True)
stop music
menu:
    "Repeat":
        vi "I want MORE!"
        jump BothUp08b
    "Move on":
        scene showerup03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "One final lick and we're good to go..."
        play sound "Sounds/lick.mp3"
        jump ThreesomeShowerFuckChoiceb
    
label PamelaGround08:
$ pamelagroundc = True
scene bothpamprefuck with dissolve
$ renpy.pause(1.0, hard=True)
p "See that cock Pamela?"
pa "Oh, I see it, how can I NOT see it? It's so fucking ENORMOUS!"
p "I'm going to force it into your tiny fuckhole..."
vi "Hold steady Pamela, it might painful at first..."
scene bothpamfuck01 with dissolve
play sound "Sounds/gasping.mp3"
$ renpy.pause(1.0, hard=True)
pa "AAAAH!"
vi "But it will get better with every plunge of his massive tool..."
scene bothpamfuck02 with dissolve
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
label PamelaGround08b:
play music "Sounds/womansex01.mp3"
scene bothpamfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck01 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck02 with dissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene bothpamfuck02 with fastdissolve
$ renpy.pause(0.3, hard=True)
stop music
menu:
    "Repeat":
        vi "Go on [name], she can take MORE!"
        pa "Please have mercy..."        
        jump PamelaGround08b
    "Move on":
        scene bothpamprefuck with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Good time to stop, I was on the verge of blowing my load... Phew..."
        vi "That means this a was a GOOD pussy Pamela."
        pa "Oooh, I'm so glad he liked it... My poor pussy..."
        jump ThreesomeShowerFuckChoiceb


label BothFinale08:
scene showeranimb11 with dissolve
$ renpy.pause(1.0, hard=True)
p "There you go, impale yourself on my pole. And Viviane, make my balls shiny with your spit."
vi "Of course, I'll make sure you have a HUGE load for Pamela in your GIANT cum factories!"
pa "Oh my God, you're so BIG! I can't believe my poor little pussy can even take it..."
p "And it can take even more inches..."
show threesomeshoweranimslow
play music "Sounds/foursomemovie.mp3"
call screen threesomeshoweranimslow01
screen threesomeshoweranimslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("ThreesomeShowerAnimfast08") 

label ThreesomeShowerAnimfast08:
hide threesomeshoweranimslow
show threesomeshoweranimfast
call screen threesomeshoweranimfast01
screen threesomeshoweranimfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("ThreesomeShowerAnimEnd08")

label ThreesomeShowerAnimEnd08:
p "Get ready to take my load Pamela!"
stop music
scene showerthreesomecum01 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/ryancumming.mp3"
pa "I can feel it, that shot alone was MASSIVE!"
p "RHAAA! There's more where that came from!"
scene showerthreesomecum02 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
pa "God, I'm ALREADY bloated with the stuff! I'm gonna cum too! AAAAH!"
vi "Please give me some too, CHAMPION!"
scene showerthreesomecum03 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "Of course, RHAA! Here comes your share, Viviane!"
vi "FUCK! You're still spewing your sauce NON-STOP all over me! I LOVE IT!"
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
scene showerthreesomecum04 with dissolve
$ renpy.pause(1.0, hard=True)
pa "You did such a mess [name]. Both in my pussy and on Viviane's body..."
play sound "Sounds/lick.mp3"
vi "Yeah, I'm so happy to have such a STUD in my class..."
p "OK, girls, I'd love to continue fucking you all day, but I need to go. I have an old foe to meet... And I also have to eat something."
$ pamelafucked = True
$ vivianefucked = True
if (pamelajosewin == False):
    p "(Pamela didn't notice I took a picture of her boobs plastered in my cum... Now I'll send it to José)."
    $ pamelawin = True 
if (vivianejosewin == False):
    p "(Viviane didn't notice I took a picture of her boobs plastered in my cum... Now I'll send it to José)."
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
if (achievement.has("watersport") == False):
    show achievement18:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement18
    $ achievement.grant("watersport")
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
scene gymlockereat with dissolve
show mceating
with dissolve
$ renpy.pause(1.0, hard=True)
p "What are you looking at? You never saw a guy eat a sandwich?"
hide mceating
show mcate
with dissolve
p "Ah, now I'm not hungry anymore. Amazing what eating does to your body. Let's move on then..."
jump BurbsDay08

label BurbsDay08:
stop music
scene burbsday with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_111
    $ lustaddedB = 1
    call Challenger from _call_Challenger_112
    $ challengercalls += 2

if hour == 17 and discoverclinic == False:
    p "I should head for the beach for the final meeting with José..."
    jump EndGame08
if hour == 18 and discoverclinic:
    p "I should head for the beach for the final meeting with José..."
    jump EndGame08

p "The burbs are so quiet during the day. Even on a Sunday. It's almost like a lockdown situation."

label BurbsChoiceDay08:
scene burbsday
p "What should I do?"
menu:
    "Go to the convenience store" if (discoverstore == True) and (evictedfromstore == False):
        jump StoreDay08
    "Go back home" if hour >= 12:
        jump HomeDay08
    "Go to Debby's house" if (auntdebbyseen08 == False):
        jump AuntDebbyHouseDay08
    "Go to Teagan's house" if (seenteaganhouseday08 == False):
        jump TeaganHouse02Day08
    "Take the bus to the beach" if (hour <= 17):
        $ busbeach = True
        jump BusDriveDay08
    "Take the bus heading downtown" if (hour <= 16):
        $ bustown = True
        jump BusDriveDay08
    "Take the shortcut to the Beach" if (hour <= 18) and (discoverclinic == True):
        stop music
        scene clinicentrance with dissolve
        play music "Sounds/gardensound.mp3"
        $ renpy.pause(1.0, hard=True)
        p "I wish I had discovered this shortcut earlier, it is really helpful in cutting my travel time between the burbs and the beach..."
        jump Beach01Day08
    "Go to the clinic" if (hour <= 17) and (discoverclinic == True) and (seenclinic05 == False) and (seenclinic06 == False) and (seenclinic07 == False)and (seenclinic08 == False):
        jump Insemination01Day08

label BusDriveDay08:
stop music
scene busdrive with dissolve
play music "Sounds/busidle.mp3"
$ renpy.pause(1.0, hard=True)
p "Here's the bus. Let's get on."

label BusEndDay08:
if (busbeach == True):
    $ hour += 1
    $ busbeach = False
    jump Beach01Day08
elif (bustown == True):
    $ hour += 1
    $ bustown = False
    jump DowntownDay08
elif (bushome == True):
    $ hour += 1
    $ bushome = False
    jump BurbsDay08
    
label HomeDay08:
stop music
scene livingroom01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah, home sweet home..."
p "What should I do?"
menu:
    "Go to my room":
       jump RyanBedroomDay08
    "Go to the bathroom":
        jump BathRoomDay08
    "Go to the swimming pool" if (hour <= 16) and seenswimmingpool08 == False:
        jump SwimmingPoolDay08
    "Leave the house":
        jump BurbsDay08

label SwimmingPoolDay08:
$ seenswimmingpool08 = True
scene nikkisunbathing01 with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
p "Nikki is frigging herself on the lounge chair... I wonder what she's thinking about?"
if nikkiwin:
    play sound "Sounds/womansigh.mp3"
    s "Ooh, [name]..."
    p "Nice, she's thinking about ME!"
if nikkijosewin:
    play sound "Sounds/womansigh.mp3"
    s "Ooh, José..."
    p "Shit, she's thinking about that DOUCHEBAG..."
if swimcompwin:
    p "Maybe it's time to make a move..."
    jump NikkiSunbathing08
if swimcompwin == False:
    p "I should leave though, she probably already knows we lost the trophy this morning... And it would be embarrassing having to explain why to her."
    jump HomeDay08
    
label NikkiSunbathing08:
scene nikkisunbathing02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Hey Nikki, guess who won the swimming competition for the school this morning?"
s "I don't need to guess, I already know! Congrats [name]!"
p "Maybe I deserve a little reward for my efforts don't you think?"
s "You're always thinking about the same thing all the time... SEX!"
p "Well, you were masturbating when I arrived if I recall correctly..."
scene nikkisunbathing03 with dissolve
$ renpy.pause(1.0, hard=True)
s "Ok, that's true... I can be a naughty girl sometimes..."
p "Well, I'm DEFINITELY a naughty boy... And your show made my bulge grow BIGGER!"
s "I can see that... But shouldn't you be keeping your stamina for tonight? You have to meet José, right?"
p "Err... How do you know about that?"
s "Oh... I know EVERYTHING [name]... Sit on the lounge chair, I'll give you a head massage to prepare you for tonight..."
scene nikkisunbathing04 with dissolve
$ renpy.pause(1.0, hard=True)
s "There, don't you feel better now? Less stressed about possibly losing tonight?"
p "No way I'll lose to this douchebag! But yeah, I feel great, thanks a lot Nikki!"
s "Off you go now, see you tonight..."
$ hour += 1
jump HomeDay08

label RyanBedroomDay08:
stop music
$ locroom = True
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)

p "What to do, what to do..."
menu:
    "Turn the computer on":
        jump ComputerDay08
    "Do some heavy bodybuilding (+2hrs)" if (hour <= 15):
        if (workout == True):
            "You already trained today."
            jump RyanBedroomDay08
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
            jump RyanBedroomDay08        
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump RyanBedroomDay08
    "Go the living room":
        jump HomeDay08
    "Go to the bathroom" if (showerseen08 == False):
        jump BathRoomDay08

label ComputerDay08:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label Computer02Day08:
scene ryancomputerday
menu:
    "Check the map":
        jump MapDay08
    "Check the stats":
        jump StatsDay08
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump Computer02Day08
    "Play a smutty game (+1hr)" if hour <= 16:
        jump CompGameDay08
    "Turn the computer off":
        jump RyanBedroomDay08

label MapDay08:
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
jump Computer02Day08

label StatsDay08:
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
jump Computer02Day08

label CompGameDay08:
scene ryancomputergameday
$ renpy.pause(1.0, hard=True)
p "This game is tough. My fingers hurt like hell from so much clicking..."
$ hour += 1
jump Computer02Day08

label BathRoomDay08:
$ showerseen08 = True
play music "Sounds/shower.mp3"
$ locroom = False
scene bathroomdoorclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "Someone's taking a shower..."
menu:
    "Use lubricant on the door hinges" if (wd69 == True) and (squeakfixed == False):
        "The door should not squeak anymore."
        $ squeakfixed = True
        jump MomShowerDay08        
    "Have a peek":
        jump MomPeekBathroomDay08
    "Leave":
        jump HomeDay08

label MomPeekBathroomDay08:
if (squeakfixed == False):
    play sound "Sounds/doorsqueak.mp3"
    scene bathroomdooropen with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Shit, the door is squeaking..."
    m "I'm in the shower sweetie, don't get in!"
    p "Ah, sorry Nancy...I'm leaving..."
    p "Damn, I should try and find a way of stopping that door from squeaking if I want to spy on Nancy or Nikki in the shower like every other MC..."
    jump RyanBedroomDay08
if (squeakfixed == True):
    scene nancyshower01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Cool, she didn't hear me come in, I can see her naked in the shower now..."
    p "Fuck yeah, look at those huge titties... How I would love to rub my pud between them..."
menu:
        "Watch a little longer...":
            jump MomShower02Day08
        "Leave before she turns round and catches me":
            jump RyanBedroomDay08
    
label MomShower02Day08:
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
            jump MomShower03Day08
        "Leave before she turns round and catches me":
            jump RyanBedroomDay08
 
label MomShower03Day08:
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
jump RyanBedroomDay08

label AuntDebbyHouseDay08:
stop music
scene debbyentrance with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/debbydoorbell.mp3"
p "Let's see if Debby is around..."
scene debbyhouse01 with dissolve
d "Well, look who came to visit me. What brings you here [name]?"
p "Just coming by to say hi Debby."
d "Well, it's much appreciated... Maybe I could entice you with a bikini session I'm having with my secretary [name]? You could give us your valuable opinion."
p "Oh really? Cool, That's a NEW thing to do at your house, I can't miss it."
d "Let's move to the swimming pool area then... Where the high-tech camera can record everything."
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
label SecretaryHandjobDay08:
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
        jump SecretaryHandjobDay08
    "Blast your semen over her":
        jump SecretaryCumDay08

label SecretaryCumDay08:
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
if gwendolinewank == False:
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
    jump BurbsChoiceDay08
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
jump BurbsChoiceDay08

label TeaganHouse02Day08:
$ seenteaganhouseday08 = True
scene teagan01day05 with dissolve
play music "Sounds/gardensound.mp3"
play sound "Sounds/swimming.mp3"
$ renpy.pause(1.0, hard=True)
p "Oh, there she is, swimming in a different outfit this time... Nice."
t "Oh, Hello [name], I was enjoying the pool , it's so hot..."
if swimcompwin:
    t "I heard you won the swimming competition this morning? Congratulations! Why don't you join me int he pool and show me your moves..."
    menu:
        "Sure, thanks for the offer Ms Cocque!":
            jump TeaganPool01Day08
        "I'm kinda busy right now, I'm already late for...err... some other stuff.":
            t "Umpf...."        
            jump BurbsChoiceDay08
if swimcompwin == False:
    t "I heard you lost the swimming competition this morning? That's too bad. Maybe you should join me in the pool... To train some more... *wink*"
    menu:
        "Sure, thanks for the offer Ms Cocque!":
            jump TeaganPool01Day08
        "I'm kinda busy right now, I'm already late for...err... some other stuff.":
            t "Umpf...."        
            jump BurbsChoiceDay08
    
label TeaganPool01Day08:
scene teagan03day05 with dissolve
$ renpy.pause(1.0, hard=True)
p "I can see her ogling my bulge... Good thing I got a semi while admiring her, it must look even bigger than usual..."
window hide
if (teaganfucked == True):
    t "Just as big as I remember it yesterday..."
    p "I'm not even hard yet teach, it will grow even bigger!"
    t "I know... YOu are so MASSIVE when you are rock-hard... Come in the pool with me stud!"
    jump TeaganPool02Day08
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

label TeaganPool02Day08:
scene teagan04day05 with dissolve
$ renpy.pause(1.0, hard=True)
t "You know, it's highly inappropriate for a teacher to be spending time like this with a student..."
t "So let's just pretend you are only my delivery boy today... and not a boy in the class I teach."
p "Sure Ms Cocque, I don't mind role-playing!"
t "So... What do you have for me Mr grocery boy? (wink)"
label TeaganPool02Day08b:
menu:
    "I picked up an extra-large zucchini for you ma'am!":
        if (lust_points[22] == 10):
            t "That is so corny [name]... Try again."
            jump TeaganPool02Day08b
        t "That is so corny [name]... I don't want to play anymore. Please go home. (sigh)"
        p "But... What about my zucchini? Don't you want to see my big zucchini?"
        jump BurbsChoiceDay08
    "I do pick-ups and deliveries. Right now, I'm picking you up...":        
        t "Ooh? And when will the delivery be?"
        scene teagan05day05 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "In a while... I first need to unpack those heavy bags..."
        if (teaganfucked == True):
            t "You like them don't you... And I KNOW you liked fucking them with your huge, young, hard COCK!"
            p "What can I say, I can't resist such lovely MILF knockers..."
            t "Let's move out of the pool, I want to see that monstercock of yours again!"
            jump TeaganFuckChoicePreDay08
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
            jump TeaganFuckChoicePreDay08
        t "Oh... I like it... But I think this is going too far young man..."
        p "What do you mean?"
        t "I'm your teacher... I can't... let a student fondle my big breasts like that. What if a nosy neighbor reported on us?"
        t "It's best that you leave [name]."
        p "But I'm not your student, you said it! I'm just your delivery boy, it's not fair!"
        jump BurbsChoiceDay08

label TeaganFuckChoicePreDay08:
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
            jump TeaganFuckChoiceDay08
        "Don't drink white bull and keep it for another time":
            p "Teagan, I'm having second thoughts. I read so many stories of teachers going to jail because they fucked their student..."
            p "I wouldn't want that to happen to you..."
            t "What? You're fondling my tits and then you don't want to fuck me? Get out of my house at once [name]!"
            jump BurbsChoiceDay08
if (stamina <= 0) and (whitebull == False):
            p "Teagan, I'm having second thoughts. I read so many stories of teachers going to jail because they fucked their student..."
            p "I wouldn't want that to happen to you..."
            t "What? You're fondling my tits and then you don't want to fuck me? Get out of my house at once [name]!"
            jump BurbsChoiceDay08

label TeaganFuckChoiceDay08:
stop music
scene teaganchoiceday05 with dissolve
$ renpy.pause(1.0, hard=True)
t "So, now that you are here, proudly displaying your gigantic erection to your schoolteacher, what would you like us to do [name]?"
menu:
    "I think anal is in order. Yes, anal." if (teagananalday05 == False):
        t "That massive fuckstick up my arse? You can't be serious..."
        p "I am serious and I'll prove it!"        
        jump TeaganAnalDay08
    "My studcock is sore from so much fucking. It needs a nice foot massage." if (teaganfeet == False):
        t "Mmh, you're a footboy are you? Then get ready for the best footjob in town stud!"
        jump TeaganFeetDay08
    "Get in the lounge chair, I'm gonna pound that sweet teacher pussy of yours!" if (teaganpussy == False):
        t "It's ready to receive your massive teenage pussy-pleaser!"
        jump TeaganPussyDay08
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (teaganpussy == True) and (teaganfeet == True) and (teagananalday05 == True):
        t "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump TeaganMovieDay08

label TeaganAnalDay08:
$ teagananalday05 = True
scene teagananal01 with dissolve
$ renpy.pause(1.0, hard=True)
p "How do you like your student's cock up your fuckhole teach?"
t "I'm such a dirty slut... Pound me with your massive fuckstick I beg you!"
scene teagananal02 with dissolve
$ renpy.pause(1.0, hard=True)
t "AAAH, it's so fucking deep!"
label TeaganAnalDay08b:
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
        jump TeaganAnalDay08b
    "Move on":
        t "Have mercy on my poor arse [name]!"
        p "Ok Teagan, I'll give you a respite. FOR NOW."
        jump TeaganFuckChoiceDay08

label TeaganFeetDay08:
$ teaganfeet = True
scene teaganfeet01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Ready? Cos my feet are going to make your dick extra-hard and extra-HUGE, guaranteed!"
p "Let's see if you're better than Sophia then shall we?"
t "Oh? A competition with the principal? I'm in!"
label TeaganFeetDay08b:
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
        jump TeaganFeetDay08b
    "Move on":
        pass    
t "Ooh, look at all that precum flowing from your tip...You're ready to pop aren't you? So, was it better than Sophia's footjobs?"
p "Y...Yes... So it's best if we move on to something else." 
jump TeaganFuckChoiceDay08    

label TeaganPussyDay08:
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
label TeaganPussyDay08b:
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
        jump TeaganPussyDay08b
    "Move on":
        pass    
jump TeaganFuckChoiceDay08    

label TeaganMovieDay08:
scene teaganfuckmovieday05 with dissolve
p "Bounce up and down on my dong teach! I want to be buried balls-deep inside you!"
t "OOOh, I don't know if I can take that much cock [name], but I sure as hell will try!"
play music "Sounds/teaganfuckslow02.mp3"
show teaganfuckslow02
show faster
call screen teaganfuckslowday08
screen teaganfuckslowday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TeaganFuckFastDay08")

label TeaganFuckFastDay08:
stop music
hide faster
play music "Sounds/teaganfuckfast02.mp3"
show teaganfuckfast02
show cum
call screen teaganfuckfastday08
screen teaganfuckfastday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TeaganFuckCumDay08")

label TeaganFuckCumDay08:
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
p "Of course not Teagan! That would get you in sssoo much trouble..."
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
jump BurbsChoiceDay08

label Insemination01Day08:
stop music
scene clinic04 with dissolve
$ renpy.pause(1.0, hard=True)
dr "Ah, welcome back [name], are you ready to use your \"talents\" to help a poor wife whose husband is shooting blanks?"
p "What do you mean exactly?"
dr "Well, while most insemination programs use artificial means, some of our clients prefer the more \"traditional\" method of insemination."
dr "And there's 10 shiny dollars for you if you unleash one of your spectacular loads inside one of our customers who is here and awaiting insemination to get pregnant."
label Insemination01Day08b:
menu:
    "Na, not today doc.":
        dr "What a waste of a stud's life. Don't forget there are ten shiny dollars in it for you if you ever come back!"
        jump ClinicOutDay08
    "Your establishment is nothing but a depraved whorehouse exploiting men!":
        dr "Yes. And the problem is?"
        p "Well, err... Nothing."
        jump Insemination01Day08b
    "Alright, I'm in! Is she hot?":
        dr "She is indeed \"hot\" as you put it. We doctors prefer the legal term \"rapable\"."
        dr "However, I am not at liberty to disclose her identity and the deed shall be done anonymously through a specially-designed aperture in the wall."
        p "You mean a gloryhole."
        dr "While it is my inclination to refrain from using such vulgar terms, yes, it's just a gloryhole."
        dr "Nurse Racque will show you the way to the insemination room and get you prepared. Please follow her."
        jump Insemination02Day08    

label Insemination02Day08:
$ seenclinic08 = True
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
        jump InseminationNOTDay08
    "Don't say a word":
        ra "I'll show you how to get the best out of that huge dick. By having a go on it myself for a while..."
        je "Don't make him cum, his sperm belongs to me!"
        ra "Don't worry Mrs Anonymous. I know how to control my pussy muscles to bring men to the edge and maintain them there..."
        jump Insemination03Day08

label Insemination03Day08:
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
            jump JenniferFuckChoiceDay08
        je "But I just can't... It's so wrong... I want out of this deal!"
        ra "What a disappointment (sigh). But you're the customer..."
        ra "[name], tuck that monstrous rod back in your pants and leave, we'll call you again if we need you..."
        p "WHAT? Like that? Dismissed like a cheap he-whore? Pfff!"
        jump InseminationNOTDay08
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
                jump JenniferFuckChoiceDay08
            je "But I just can't... It's so wrong... I want out of this deal!"
            ra "What a disappointment (sigh). But you're the customer..."
            ra "[name], tuck that monstrous rod back in your pants and leave, we'll call you again if we need you..."
            p "WHAT? Like that? Dismissed like a cheap he-whore? Pfff!"
            jump InseminationNOTDay08            
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
        jump InseminationNOTDay08
        
label JenniferFuckChoiceDay08:
scene insemination13 with dissolve
$ renpy.pause(1.0, hard=True)
je "Get on with it, I need your sweet cum!"
menu:
    "Get on your back, I'll drill you slowly to stretch your fuckhole!" if (jenniferpussy == False):
        je "Yes, I think that's in order. Since you're so big..."
        jump JenniferPussyDay08
    "Spread those legs, I'm gonna pound you from behind!" if (jenniferdoggy == False):
        je  "Of course, pummel me like a ragdoll [name]!"
        jump JenniferDoggyDay08
    "Yeah, OK, but I want your sweet arse!" if (jenniferanal == False):
        je "What? But you can't impregnate me that way!"
        p "It's to get my cock really hard and ready to explode in your other hole. Come on, you know you want it!"
        je "I definitely DON'T want it, but if it's for a good cause..."
        jump JenniferAnalDay08
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (jenniferpussy == True) and (jenniferdoggy == True) and (jenniferanal == True):
        je  "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump JenniferMovieDay08

label JenniferPussyDay08:
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
label JenniferPussyDay08b:
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
        jump JenniferPussyDay08b
    "Move on":
        pass
je "Now I'm totally stretched out!"
ra "I can see that, your hole is gaping wide open Jennifer!"
p "Good, so we can move on to another position then..."
jump JenniferFuckChoiceDay08

label JenniferDoggyDay08:
$ jenniferdoggy = True
scene insemination12 with dissolve
play sound "Sounds/jennifer02.mp3"
$ renpy.pause(12.0, hard=True)
je "Oh God, oh God! I'm gonna take the biggest fattest cock I've ever seen! I'm dripping wet, shove it in [name] I beg you!"
p "Sure, Here I come, ten inches in one swift go!"
scene insemination12b with dissolve
$ renpy.pause(1.0, hard=True)
je "Damn it, you're so fucking deep!"
label JenniferDoggyDay08b:
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
        jump JenniferDoggyDay08b
    "Move on":
        pass    
je "I feel like a hog on a spitfire!"
p "My dick sure took some heat, I'm red-hot and ready for more action!"
jump JenniferFuckChoiceDay08    

label JenniferAnalDay08:
$ jenniferanal = True
scene insemination18 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Show the naysayers that a woman is also perfectly capable of taking well over a foot of fat hosepipe up her backside [name]!"
je "What? No, please, show instead some restraint when you plunge that massive pole int....!"
scene insemination18b with dissolve
play sound "Sounds/jenniferanal01.mp3"
$ renpy.pause(1.0, hard=True)
je "... MEEEE! FUCK! AAAH!"
label JenniferAnalDay08b:
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
        jump JenniferAnalDay08b
    "Move on":
        pass    
je "Thank God you didn't waste your virile spunk in that hole..."
p "I know where to aim... Let me show you." 
jump JenniferFuckChoiceDay08    

label JenniferMovieDay08:
scene insemination14 with dissolve
p "Ok, you want my sperm Jennifer? I want to hear you SAY IT!"
je "YES! Breed me [name], I want to have your baby!"
play music "Sounds/jenniferfuckslow.mp3"
show jenniferslowfuck
show faster
call screen jenniferslowfuckday08
screen jenniferslowfuckday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("JenniferFastFuckDay08")

label JenniferFastFuckDay08:
stop music
hide faster
play music "Sounds/jenniferfuckfast.mp3"
show jenniferfastfuck
show cum
call screen jenniferfastfuckday08
screen jenniferfastfuckday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("JenniferCumDay08")

label JenniferCumDay08:
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
        jump Beach01Day08
    "Go to the Burbs":
        jump BurbsDay08
    
label InseminationNOTDay08:
$ inseminationfail08 = True
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
        jump Beach01Day08
    "Go to the Burbs":
        jump BurbsDay08    

label ClinicOutDay08:
scene clinicentrance
$ renpy.pause(1.0, hard=True)
p "Where should I go?"
menu:
    "Go to the beach":
        jump Beach01Day08
    "Go to the Burbs":
        jump BurbsDay08    

label StoreDay08:
stop music
scene store01 with dissolve
play music "Sounds/storemusic.mp3"
$ renpy.pause(1.0, hard=True)

label StoreClerkDay08:
scene store01
if (workedseconddaystore == True) and (hour <= 15):
    fa "Oh hi [name]. I guess you came to work here again?"
    fa "I'm really sorry but you can't. I took another boy for the work today, since you already worked here twice already."
    fa "He was desperate for money, I couldn't really say no. He's a nice boy called José."
    p "WHAT???? AAARGH! This is not fair!"
    fa "Oh, moan, moan, moan, that's all I ever hear from you..."
    jump ClerkChoiceDay08    
if ((catchfrancine == True) or (catchbeer == True)) and (hour <= 15):
    fa "Are you ready to start another shift today?"
    menu:
        "Yes, I'm ready.":
            jump StoreSecondWork01Day08
        "No, I'm too busy right now.":
            fa "Well, that's unfortunate... I could have really used your help again today..."
            jump ClerkChoiceDay08    
else:
    fa "Welcome to \"Seven Square\", your local shop that's opened from seven till... seven."

label ClerkChoiceDay08:
if (catchfrancine == True) or (catchbeer == True):
    fa "So, how may I help you?"
else:
    fa "My name is Francine, how may I help you?"
menu:
    "Buy something":
        jump StoreBuyDay08
    "Invite her to the gym" if (gymmember == True):
        p "Hey, would you like to come to the gym with me today?"
        fa "Ooh, yes! Please let me know when you get there, thanks!"
        $ invitedfrancine08 = True
        jump ClerkChoiceDay08
    "Leave":
        jump BurbsDay08

label StoreSecondWork01Day08:
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
        jump CleanStorageDay08
    "Build a pole-dancing platform with all the shit lying around" if (quentintipfrancine == True):
        jump PoleDancingDay08

label CleanStorageDay08:
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
jump StoreShiftEndSecondDay08

label PoleDancingDay08:
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
        jump PoleDance01Day08
    "Me no parl-ay Froggie. Sorry.":
        re "But you are supposed to! All shops must cater to French-speakers on Veri-Bosti island, it's the law!"
        p "Well clearly you speak English. So what are you moaning about?"
        re "Humpf, yes I do, but it is not my first language. I am looking for.. how do you say?... Washing powder?"
        p "Ah, let me show you, we have all the big brands and also the cheap ones that are exactly the same shit."
        jump StoreCustomerDay08
    "Vou-lay-vous couch-ay avec moi ce soir?":
        re "Hein? Mais ça va pas la tête? C'est un scandale!"
        p "Calm down now lady, I was just kidding... Why don't we speak English for a change, you speak English right?"
        re "Humpf, yes I do, but it is not my first language. I am looking for.. how do you say?... Washing powder?"
        p "Ah, let me show you, we have all the big brands and also the cheap ones that are exactly the same shit."
        jump StoreCustomerDay08

label StoreCustomerDay08:
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
        jump PoleDance01Day08
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
        jump PoleDance01Day08

label PoleDance01Day08:
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
            $ invitedfrancine08 = True
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
    jump BurbsChoiceDay08

label StoreShiftEndSecondDay08:
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
jump HalfPriceDay08

label HalfPriceDay08:
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
        jump StoreShiftEnd03Day08
        
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
        jump StoreShiftEnd03Day08

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
        jump StoreShiftEnd03Day08

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
        jump StoreShiftEnd03Day08
    
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
        jump StoreShiftEnd03Day08

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
        jump StoreShiftEnd03Day08
    
    "Nothing actually...":
        jump StoreShiftEnd03Day08
        
label StoreShiftEnd03Day08:
scene store01 with dissolve
fa "That's it, you bought your item, now you can leave... Come back anytime to \"Seven Square\", your local shop that's opened from seven till... seven."
jump BurbsDay08
    
label StoreBuyDay08:
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
        jump ClerkChoiceDay08

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
        jump ClerkChoiceDay08

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
        jump ClerkChoiceDay08

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
        jump ClerkChoiceDay08
    
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
        jump ClerkChoiceDay08

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
        jump ClerkChoiceDay08
    "Nothing actually...":
        jump ClerkChoiceDay08

label Beach01Day08:
stop music
play music "Sounds/oceanwaves.mp3"
scene beach with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah! Here's Tini-Wini-Bikini beach, as sunny as always... I should probably head for the beach bar first..."
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_113
    $ lustaddedB = 1
    call Challenger from _call_Challenger_114
    $ challengercalls += 2

label BeachBar01Day08:
$ beachbarseen08 = True
stop music
play music "Sounds/tropicalmusic.mp3"
scene beachbar01 with dissolve
$ renpy.pause(1.0, hard=True)
bb "Aloha, welcome to Tini-Wini-Bikini Beach bar! Again..."
bb "I regret to inform you that Randy Beach is closed again today. For...err... the same reason as yesterday."
p "Gee, people can be so filthy sometimes."
if saturdaybikini == False:
    bb "Today is \"Sunday Bikini Pageant.\" A weekly event organized by Audacious Bikinis. You might have heard of them..."
    p "Yeah, I think I heard of them. My landlady's sister is the CEO of Audacious actually..."
    scene beachbar03 with dissolve
    bb "Oh, really? Then you might want to go and talk to her, she's over there and she's looking for jury members."
    p "I shall indeed be on my merry way to perform my duty for the community!"
    scene beachbar01 with dissolve
    bb "That's good to hear. Now I can attend to REAL customers."
    $ saturdaybikini = True
jump ExploreBeachDay08    
    
label ExploreBeachDay08:
if hour == 18:
    p "I'd better head for the meeting point with José. It's TIME!"
    jump EndGame08
    
stop music
play music "Sounds/oceanwaves.mp3"
p "Hum... Where should I go?"
menu:
    "Go and meet Debby" if saturdaybikini and hour <= 16 and didsaturdaybikini == False:
        jump BikiniCompDay08
    "Go and meet Maddy" if (hour <= 17) and maddyfucksunday:
        jump MaddyFuckDay08
    "Walk along the beach" if (walkbeachseen08 == False) and hour <= 16:
        jump BeachWalkDay08
    "Go to Randy Beach" if (randybeachseen08 == False):
        jump RandyBeachDay08
    "Go to the lifeguard tower" if (lifeguarddiscovered == True) and (seenlifeguard08 == False):
        jump Lifeguard01Day08
    "Take the Bus to town" if (hour <= 15):
        $ bustown = True
        jump BusBeachTownDay08
    "Take the shortcut back to the Burbs" if (discoverclinic == True) and hour <= 17:
        stop music
        scene clinicentrance with dissolve
        play music "Sounds/gardensound.mp3"
        $ renpy.pause(1.0, hard=True)   
        p "I wish I had discovered this shortcut earlier, it is really helpful in cutting my travel time between the burbs and the beach..."
        jump BurbsDay08

label BikiniCompDay08:
$ didsaturdaybikini = True
scene debbybikinicompbackground with dissolve
show debbybikiniprecomp01
$ renpy.pause(1.0, hard=True)   
p "(There's aunt Debby turning her back to me. Time to ogle that fine arse a bit before talking to her...)"
window hide
hide debbybikiniprecomp01
show debbybikiniprecomp02
$ renpy.pause(1.0, hard=True)   
d "Oh hello my favorite sister's landboy! I'm glad to see you, I'm looking for men to rate hot women in bikinis. *wink* Interested?"
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
        jump BrittanyWinDay08
    "Sandy":
        jump SandyWinDay08
    "Halle":
        jump HalleWinDay08

label BrittanyWinDay08:
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
    jump BritPrefuckDay08
if lust_points[1] >= 10 and brittanyfucked:
    br "Follow me to my quarters loyal subject, your Queen needs some hot loving."
    menu:
        "Of course your Subliminal Empress of Beauty. Where are they?":
            br "Err... In the beach bathrooms for the moment."
            p "How befitting."
            $ hour += 1
            jump BritPrefuckDay08
        "Your Majesty deserves some quiet time, I cannot encroach on her Most Valuable Pampering.":
            br "What the hell are you talking about? I said come and FUCK ME!"
            p "And I heard \"Go and get fucked\". I will therefore follow your orders and quickly run away."
            $ hour += 1
            jump ExploreBeachDay08 
br "Though my reward is not sufficient to grant you an audience in my royal quarters."
p "Ah, damn."
d "The competition is over, thank you all for coming!"
$ hour += 1
jump ExploreBeachDay08

label SandyWinDay08:
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
    jump SandyFuckDay08
if lust_points[19] >= 10 and sandyfucked:
    sa "And my reward is... my body to you again my Prince Charming!"
    menu:
        "Of course, I'm looking forward to some more HOT loving Sandy!":
            sa "Let's get naked and move to a quiet place. In total communion with Mother Nature..."
            $ hour += 1
            jump SandyFuckDay08
        "Ah, you know what, I'm too busy right now, gotta go. Gotta go, gotta go.":
            sa "What? But... My Prince Charming!"
            p "Yep, see you later Sandy. gotta go."
            $ hour += 1
            jump ExploreBeachDay08 
sa "Unfortunately, I will still wait for my True Prince Charming to come along."
p "What, it's not me?"
sa "Did you see an epiclust icon?"
p "Err... No."
sa "Then it's not you. Bye [name]!"
d "The competition is over, thank you all for coming!"
$ hour += 1
jump ExploreBeachDay08

label HalleWinDay08:
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
    jump HalleFuckDay08a
if lust_points[9] >= 10 and hallefucked:
    ha "I want your MASSIVE dong again, let's go quickly NAKED into the sea! Where no one can see us..."
    menu:
        "Of course, I'm already hard and almost tearing a hole in my speedos!":
            $ hour += 1
            jump HalleFuckDay08a
        "Ah, you know what, I'm late for something.":
            ha "Something more important than fucking ME???"
            p "Yeah, err... It's like MEGA-important. Bye Halle."
            $ hour += 1
            jump ExploreBeachDay08 
ha "On second thoughts... I need to study."
p "I can teach anatomy. With my cock."
ha "I think my textbook is more appropriate right now."
p "Damn... That line never works, I don't understand why."
d "The competition is over, thank you all for coming!"
$ hour += 1
jump ExploreBeachDay08

label BusBeachTownDay08:
scene beach with dissolve
$ renpy.pause(1.0, hard=True)   
p "Bye bye Tini-Wini-Bikini beach!"
p "Ah, here's the bus going to town..."
jump BusEndDay08

label BeachWalkDay08:
$ walkbeachseen07 = True    
if (boughthallebikini == True) and ((walkbeachseen == False) or (beachswimday03 == True)) and (((walkbeachseen04 == False) or (beachswimday04 == True)) or ((walkbeachseen05 == False) or (beachswimday05 == True)) and (hallefucked == False)):
    jump HalleBeachDay08

else:
    scene beachempty with dissolve
    $ renpy.pause(1.0, hard=True)  
    if (beachswimday04 == False) and (beachswimday03 == False) and (beachswimday05 == False) and (beachswimday06 == False) and (beachswimday07 == False):
        "This secluded part of the beach is empty... I could always go for a swim I guess."
        menu:
            "Go for a swim" if (beachswimday05 == False) and (beachswimday04 == False) and (beachswimday03 == False) and (beachswimday06 == False) and (beachswimday07 == False) and (beachswimday08 == False):
                jump BeachSwimDay08
            "Don't go for a swim":
                jump ExploreBeachDay08
    "This secluded part of the beach is empty today. BORING!"
    jump ExploreBeachDay08

label BeachSwimDay08:
$ beachswimday08 = True
play music "Sounds/randybeachsound.mp3"
scene beachswim01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I can see some coral reefs below. Let's dive and have a look!"        
scene beachswim02 with dissolve
play music "Sounds/underwater.mp3"
$ renpy.pause(1.0, hard=True)
p "What the hell is that thing swimming towards me?"
jump Mermaid01Day08

label HalleBeachDay08:
$ walkbeachseen08 = True 
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
        jump Underwater01bDay08
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
        jump Underwater01bDay08

label Underwater01bDay08:
scene hallebeach03 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Come on, this way! You'll see, it's gonna be ssoo much fun!"

label Underwater02Day08:
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
        jump Mermaid01Day08
    "Sneak under her":
        scene underwater03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Bingo, she's smiling at me... I wonder what a kiss underwater feels like..."
        scene underwater03b with dissolve
        p "What's wrong, she seems to be scared of something..."
        scene underwater04 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "She's darting off... OMG, what the fuck is that?..."
        jump Mermaid01Day08

label Mermaid01Day08:
scene mermaid01 with dissolve
$ renpy.pause(1.0, hard=True)
p "This mermaid is captivating... OK, she has a fish tail and all that but... Mmmh, those tits..."
scene mermaid02 with dissolve
$ renpy.pause(1.0, hard=True)
p "She seems to be signalling me to follow her..."
menu:
    "Follow her":
        jump Mermaid02Day08
    "Get the hell out of here and re-join Halle" if (beachswimday08 == False):
        $ underwaterleft = True
        jump Underwater03Day08
    "Get the hell out of here" if (beachswimday08 == True):
        scene beachswim01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Phew, that was close!I'm still shaking. Better go back to the beach..." 
        scene beachempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ExploreBeachDay08

label Mermaid02Day08:
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
        jump Mermaid03Day08
    "Get the hell out of here and re-join Halle" if (beachswimday08 == False):
        jump Underwater03Day08
    "Get the hell out of here" if (beachswimday07 == True):
        scene beachswim01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Phew, that was close!I'm still shaking. Better go back to the beach..." 
        scene beachempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ExploreBeachDay08
        
label Mermaid03Day08:
scene mermaid08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Here we go, it's tough to aim underwater but once I'm in, it shouldn't move too much..."
scene
play movie "Day3/mermaidfuckslow.ogv" loop
show movie with fade
show faster
call screen mermaidfuckslowDay08
screen mermaidfuckslowDay08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MermaidFuckFastDay08")
label MermaidFuckFastDay08:
hide faster
play movie "Day3/mermaidfuckfast.ogv" loop
show cum
call screen mermaidfuckfastDay08
screen mermaidfuckfastDay08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MermaidFuckCumDay08")
label MermaidFuckCumDay08:
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
if (beachswimday08 == False):
    jump Underwater03Day08
if (beachswimday08 == True):
    scene beachswim01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "The sea is getting rough. I'd better go back to the beach..." 
    scene beachempty with dissolve
    $ renpy.pause(1.0, hard=True)
    jump ExploreBeachDay08

label Underwater03Day08:
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
            jump HalleBackBeach01Day08
        else:
            scene hallesea04 with dissolve
            $ renpy.pause(1.0, hard=True)
            ha "Ha ha! You boys really are all the same... A pair of tits, that's all that counts!"
            ha "Let's get back to the beach, the sea is getting rough..."
            p "Great idea..."
            jump HalleBackBeach01Day08
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
        jump HalleBackBeach01Day08        
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
        jump HalleBackBeach01Day08
        
label HalleBackBeach01Day08:
stop music
play music "Sounds/oceanwaves.mp3"
scene hallebeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Well, that was fun, apart from this vile creature... I think I'd better head back to the university, I need to study."
menu:
    "Okay, I hope to see you again Halle...":
        ha "You will, don't worry... If you come back to the beach, I'll be here..."
        jump ExploreBeachDay08
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True) and (lust_points[9] >=8):
        jump HallePendulumDay08
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
        jump ExploreBeachDay08

label HallePendulumDay08:
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
    jump HalleFuckDay08
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
    jump HalleFuckDay08   

label HalleFuckDay08:
scene hallebeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "I think I changed my mind... I would rather spend some \"quality\" time with you after all..."
ha "And by \"quality\", I mean some hot, steamy SEX!"
p "Alright, I'm in baby!"
label HalleFuckDay08b:
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
label HalleFuckDay08a:
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
label HallePrefuckDay08:
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
        jump HallePrefuckDay08
    "Spread her legs and fuck her pussy slowly":
        ha "You want to fuck me some more stud? Yeah, I 'm ready for your great big horsecock, come and ram that monstercock home!"
        jump HalleFuckMovieDay08

label HalleFuckMovieDay08:
stop music
play sound "Sounds/oceanwaves.mp3"
play music "Sounds/hallefuckslow.mp3"
show hallefuckslow
show faster
call screen hallefuckslowDay08
screen hallefuckslowDay08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("HalleFuckFastDay08")
label HalleFuckFastDay08:
hide faster
play music "Sounds/hallefuckfast.mp3"
show hallefuckfast
show cum
call screen hallefuckfastDay08
screen hallefuckfastDay08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("HalleFuckCumDay08")

label HalleFuckCumDay08:
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
jump ExploreBeachDay08

label Lifeguard01Day08:
stop music
scene tower01 with dissolve
$ seenlifeguard08 = True
$ renpy.pause(1.0, hard=True)

if (hour == 13 or hour == 14 or hour == 15) and (workedseconddaylifeguard == True):
    pa "Oh, hi there [name]. You still have some energy to work after this morning's swimming competition?"
    p "Yeah, sure, full of ENERGY!..."
    pa "So, you wanna start working today?"
    menu:
        "Sure, I'm in!":
            jump LifeGuardWorkThirdDay08
        "Maybe another day...":
            pa "Fine, your choice, hope to see you back here another day..."
            jump ExploreBeachDay08
    
if (hour >=16) and (wonarmwrestling == True):
    pa "It's a bit late to start a workshift for Sunday. It get quiet soon. You should have come earlier..."
    jump ExploreBeachDay08
jump ExploreBeachDay08

label LifeGuardWorkThirdDay08:
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
            jump PamelaPrefuckDay08
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
                jump PamelaPrefuckDay08
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
            jump ExploreBeachDay08            
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
        jump ExploreBeachDay08       
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
            jump PamelaPrefuckDay08 
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
        jump ExploreBeachDay08       
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
        jump ExploreBeachDay08        
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
        jump ExploreBeachDay08
        
label PamelaPrefuckDay08:
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
    jump ExploreBeachDay08    
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
    
label PamelaFuckSeaDay08:
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
label PamelaSeaFuckChoiceDay08:
menu:
    "I need to see that scrumptious arse of yours while I fuck you!" if (pameladoggy == False):
        pa "I'm guessing doggy then, right?"
        p "Correct answer. You've just won... 18 inches of boymeat up your twat!"
        jump PamelaSeaDoggyDay08
    "Let's fuck in the water!" if (pamelastand == False):
        pa "What? That sounds dangerous.... but so adventurous too, I'm in!"
        jump PamelaSeaStandDay08
    "There's a cave that still needs exploring..." if (pamelaanal == False):
        pa "Wh... What do you mean?"
        p "I mean, I'm going to bang your backside!"        
        jump PamelaSeaAnalDay08
    "Why don't you kneel in front of my giant prong and worship it?" if (pamelablow == False):
        pa "It certainly is big enough to warrant worshipping!"
        jump PamelaSeaBlowDay08
    "Let me lift you up on my shaft for the grand finale..." if (pamelastand == True) and (pameladoggy == True) and (pamelaanal == True) and (pamelablow == True):
        jump PamelaSeaMovieDay08

label PamelaSeaDoggyDay08:
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
label PamelaSeaDoggyDay08b:
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
        jump PamelaSeaDoggyDay08b
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaSeaFuckChoiceDay08

label PamelaSeaStandDay08:
$ pamelastand = True
scene pamelastand01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Just the tip of your monster cock is already filling me up like never before!"
p "Wait till you get another fifteen inches of it..."
label PamelaSeaStandDay08b:
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
        jump PamelaSeaStandDay08
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaSeaFuckChoiceDay08

label PamelaSeaAnalDay08:
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
label PamelaSeaAnalDay08b:
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
        jump PamelaSeaAnalDay08b
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaSeaFuckChoiceDay08

label PamelaSeaBlowDay08:
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
label PamelaSeaBlowDay08b:
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
        jump PamelaSeaBlowDay08b
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaSeaFuckChoiceDay08

label PamelaSeaMovieDay08:
scene pamelafuckmovie with dissolve
$ renpy.pause(1.0, hard=True)
p "Yeah, grind your pussy on my shaft and get it nice and wet..."
pa "I'm ready... FUCK ME!"
play music "Sounds/pamelafuckslow.mp3"
show pamfuckslow
show faster
call screen pamSeafuckslowday08
screen pamSeafuckslowday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PamelaSeaFuckFastDay08")

label PamelaSeaFuckFastDay08:
stop music
hide faster
play music "Sounds/pamelafuckfast.mp3"
show pamfuckfast
show cum
call screen pamSeafuckfastday08
screen pamSeafuckfastday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PamelaSeaCumDay08")

label PamelaSeaCumDay08:
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
    jump ExploreBeachDay08        

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
jump ExploreBeachDay08        

label SandyFuckDay08a:
stop music
play music "Sounds/oceanwaves.mp3"
scene sandybeach01b with dissolve
$ renpy.pause(1.0, hard=True)
sa "Oh, my Prince Charming, what a beautifully romantic place you found, far from the madding crowd!"
menu:
    "Yes, it's the perfect spot for us to get...more intimate..." if (lust_points[19] ==10):
        scene sandybeach02a with dissolve
        sa "And to get back to our natural human state without constraints by being naked...In total communion with Mother Nature."
        jump SandyFuckDay08
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True) and (lust_points[19] >=8) and (lust_points[19] <=9):
        jump SandyPendulumDay08
    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[19] >=8) and (lust_points[19] <=9):
        play sound "Sounds/spray.mp3"
        $ renpy.pause(1.0, hard=True)
        jump SandyPheromoneDay08
    "Leave, I don't have time for hanky-panky right now.":
        scene sandybeach02b with dissolve
        sa "What? Are you f*cking bl**dy kidding me???"
        p "Well, that's not very poetic language if I may say so..."
        p "(I should go back to Pamela, I haven't been paid yet...)"
        jump BeachPamela01Day08

label SandyPheromoneDay08:
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
    jump SandyFuckDay08
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
    jump SandyFuckDay08   

label SandyPendulumDay08:
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
jump ExploreBeachDay08

label SandyFuckDay08:
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
    jump ExploreBeachDay08
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
            jump ExploreBeachDay08

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
label SandyBlowDay08:
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
        jump SandyBlowDay08
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay08

label SandyFuckChoiceDay08:
menu:
    "Spoon her from the side" if (sandyside == False):
        jump SandySideDay08
    "Stick your cock between her huge jugs" if (sandytits == False):
        jump SandyTitsDay08
    "Take her from behind like a bitch in heat" if (sandydoggy == False):
        jump SandyDoggyDay08
    "Watch her bounce up and down your giant crank" if (sandyside == True) and (sandytits == True) and (sandydoggy == True):
        jump SandyFinalDay08

label SandySideDay08:
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
label SandySideDay08b:
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
        jump SandySideDay08b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay08

label SandyTitsDay08:
$ sandytits = True
scene sandytits01 with dissolve
play sound "Sounds/sandytitfuck01.mp3"
$ renpy.pause(2.0, hard=True)
sa "OOoh, my Prince Charming, my huge tits can't even bury that massive fuckstick, the head is sticking out..."
p "It will be sticking out way more once I do this..."
scene sandytits02 with dissolve
sa "It's so fucking big... Ssooo fucking big..."
label SandyTitsDay08b:
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
        jump SandyTitsDay08b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay08

label SandyDoggyDay08:
$ sandydoggy = True
scene sandydoggy01 with dissolve
$ renpy.pause(1.0, hard=True)
sa "My hole is all yours my Prince! Ram it in as deep as you like!"
p "Sure will do!"
scene sandydoggy01 with dissolve
play sound "Sounds/sandydoggy01.mp3"
$ renpy.pause(3.0, hard=True)
sa "AAAAH, it's so good feeling your giant teenage cock stretching my tiny fuckhole!"
label SandyDoggyDay08b:
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
        jump SandyDoggyDay08b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay08

label SandyFinalDay08:
scene sandybeachkiss with dissolve
play sound "Sounds/sandyslut.mp3"
$ renpy.pause(3.0, hard=True)
sa "I'm going to bounce up and down your shaft and make you feel sssoo good my Prince... You'll pop in no time!"
stop music
play sound "Sounds/oceanwaves.mp3"
play music "Sounds/sandyfuckslow.mp3"
show sandyfuckslow
show faster
call screen sandyfuckslowday08
screen sandyfuckslowday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("SandyFuckFastday08")
label SandyFuckFastday08:
hide faster
play music "Sounds/sandyfuckfast.mp3"
show sandyfuckfast
show cum
call screen sandyfuckfastday08
screen sandyfuckfastday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("SandyFuckCumday08")

label SandyFuckCumday08:
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
jump ExploreBeachDay08
    
label BritPrefuckDay08:
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
    jump ExploreBeachDay08    
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
label BritFuckday08:
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
label BrittanyFuckChoiceDay08:
menu:
    "Let me lift you up on my scepter!" if (britup == False):
        jump BritUpDay08
    "Let me show you how peasants like me fuck like wild animals!" if (britdoggy == False):
        br "Ooh, that's so dirty!"
        jump BritdoggyDay08
    "Let's get dirty on the floor..." if (britfloor == False):
        br "You are so filthy... I name you Knight of the Scum!"
        p "I'll soon become Knight of the Cum..."        
        jump BritFloorDay08
    "Your royal backside needs a good pounding!" if (britanal == False):
        br "My... Royal backside? No one has ever fucked me there, and your scepter is too big for it!"
        p "Na, it will fit. And anyway, a true beauty queen needs to know how to take it every which way... Get on the floor and expose that royal rump!"
        jump BritAnalDay08
    "Let's fuck sideways. For the viewer that is..." if (britup == True) and (britdoggy == True) and (britfloor == True) and (britanal == True):
        jump BritMovieDay08

label BritUpDay08:
$ britup = True
scene britfuckup04 with dissolve
$ renpy.pause(1.0, hard=True)
p "Get ready for lift-off!"
br "Yes, hold me in your massively-muscled arms my Knight in shining armor!"
scene britfuckup02 with dissolve
$ renpy.pause(1.0, hard=True)
br "OOOH, FUCK! It's so fucking thick and DEEP!"
p "Hang on, I'll drill even deeper!"
label BritUpDay08b:
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
        jump BritUpDay08b
    "Move on":
        p "Time to show you some other uses to my scepter..."
        br "What would you like to do next [name]?"        
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        jump BrittanyFuckChoiceDay08

label BritdoggyDay08:
$ britdoggy = True
scene britdoggy03 with dissolve
play sound "Sounds/britwet.mp3"
$ renpy.pause(6.0, hard=True)
br "Just the tip of your monster cock is already filling me up like never before!"
if (brittanyjosewin == True):
    p "So I'm much bigger than that dickhead José then?"
    br "Oh yes, MUCH bigger! Fuck me hard and deep and prove me you deserve my royal fuckhole more than him!"
label BritdoggyDay08b:
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
        jump BritdoggyDay08
    "Move on":
        p "Time to show you some other uses to my scepter..."
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What would you like to do next [name]?"        
        jump BrittanyFuckChoiceDay08

label BritFloorDay08:
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
label BritFloorDay08b:
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
        jump BritFloorDay08b
    "Move on":
        p "Time to show you some other uses to my scepter..."
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What would you like to do next [name]?"        
        jump BrittanyFuckChoiceDay08

label BritAnalDay08:
$ britanal = True
scene britanal01 with dissolve
$ renpy.pause(1.0, hard=True)
br "Aah, be careful my loyal subject!"
p "Just relax Brittany, open your arse to the people!"
label BritAnalDay08b:
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
        jump BritAnalDay08b
    "Move on":
        p "Time to show you some other uses to my scepter..."
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What would you like to do next [name]?"        
        jump BrittanyFuckChoiceDay08

label BritMovieDay08:
scene britfuckpremovie with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready your Sumptuous Highness?"
br "I'm ready... FUCK ME!"
play music "Sounds/britfuckmovie.mp3"
show britfuckmovie
show cum
call screen britfuckmovieday08
screen britfuckmovieday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("BritCumDay08")

label BritCumDay08:
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
jump ExploreBeachDay08

label RandyBeachDay08:
stop music
scene randybeach01 with dissolve
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
$ randybeachseen08 = True
if (randybeachseen == True) or (randybeachseen02 == True) or (randybeachseen03 == True) or (randybeachseen04 == True) or (randybeachseen05 == True):
    p "Finally back here again. I'd better take my speedos off."
else:
    p "I guess that's it. I'd better take my speedos off."
window hide
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)

label RandyBeachDay08b:
p "I see three parasols but I can't see the people behind them...Which one should I go to?"
menu:
    "Go to the closest red parasol on the right" if (seenparasolright08 == False):
        jump RandyBeachParasolRight08
    "Go to the middle orange parasol" if (seenparasolmiddle08 == False):
        jump RandyBeachParasolMiddle08
    "Go to the furthest red parasol on the left" if (seenparasolleft08 == False):
        jump RandyBeachParasolLeft08
    "Leave Randy Beach":
        if seenparasolleft08 or seenparasolmiddle08:
            $ hour += 1
        jump ExploreBeachDay08

label RandyBeachParasolLeft08:
$ seenparasolleft08 = True
scene sundayparasolleft01
show sundayparasolleft
$ renpy.pause(2.0, hard=True)
p "Let's see what's behind this parasol..."
window hide
hide sundayparasolleft with moveoutright
$ renpy.pause(1.0, hard=True)
p "Ah, it's Suzanne and that Henderson girl. Doing some lesbian stuff. I hope they're not going to try and beat me up."
scene sundayparasolleft02 with dissolve
$ renpy.pause(1.0, hard=True)
if swimcompwin == False:
    hg "What are you looking at, LOSER? We already told you we BELONG to Max."
    p "Ok, but he's not here now, is he? I'm here on the other hand!"
    rc "We're just get our pussies wet and ready for him actually! So you can watch but you can't touch, got it?"
    p "Fine, fine... (Pff... dykes.)"
if swimcompwin:
    hg "What are you looking at? You winning this morning doesn't give you the right to barge in on us like that!"
    p "Well, I thought you might want a taste of some WINNER's cock for a change..."
    rc "We're getting our pussies wet and ready for Max! We belong to him, your win this morning was just a fluke."
    hg "So you can watch, but you can't touch, is this clear? Only Max can allow you access to our pussies and he's not here yet..."
    p "Fine, fine... (Pff... dykes.)"
   
scene sundayparasolleft03 with dissolve
play sound "Sounds/lesbians.mp3"
hg "Oooh, yes, I'm ready Max, come and fuck me please!"
rc "My hole is wet for you, where are you baby?"
p "No one's answering. So let me..."
hg "Shut up! We told you, you CAN'T TOUCH!"
scene sundayparasolleft04 with dissolve
stop sound
rc "I'll get your hole huge and slippery for him for when he arrives..."
hg "Oh my God, your fist is right up my womb! AAAH!"
play sound "Sounds/womansigh.mp3"
scene sundayparasolleft05 with dissolve
hg "Now you must go, you've seen enough and Max is about to arrive..."
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
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
jump RandyBeachDay08b

label RandyBeachParasolMiddle08:
$ seenparasolmiddle08 = True
scene sundayparasolmiddle01
show sundayparasolmiddle
$ renpy.pause(2.0, hard=True)
p "Let's see what's behind this parasol..."
window hide
hide sundayparasolmiddle with moveoutright
p "Oh no! It's that red-headed boy with an EVEN BIGGER boy having their way with MY hot stewardess!"
h "Fuck me Max, fuck me hard!"
p "And she's letting them fuck her ON THE GROUND?!?"
scene sundayparasolmiddle02 with dissolve
$ renpy.pause(1.0, hard=True)
rb "Oh, it's you... Well, as you can see, I'm busy FUCKING some hot chick."
p "Who's the other boy? I've never seen him before."
rb "Oh, Magnus? He's my younger cousin, he's visiting from the next-door island. Veri-Veri-Bosti. \nHe brought over that stewardess he met on the plane on the way here."
h "Magnus! Your cock is the BIGGEST I've ever see in my ENTIRE LIFE!"
if hostessfuck:
    p "Hey, you said I was the biggest last Sunday!"
if hostessfuck == False:
    p "(Good thing that guy wasn't at the Muscle Stud Competition...)"
p "How does his dong even fit in any hole???"
rb "Oh, you wanna see do you? Hey, Magnus, I've loosened her hole for you, why don't you show pindick over there how you stretch a pussy with your MEGACOCK?"
h "Ooh, YES PLEASE!"
scene sundayparasolmiddle03 with dissolve
play music "Sounds/planefuck.mp3"
$ renpy.pause(1.0, hard=True)
h "Oh, you're sticking over a foot of monster cock into my ravaged pussy! AAAH! I'm CUMMING AGAIN!"
rb "See, it fits. Now if you'll excuse us, we're going to dump a couple of loads inside that broad before heading off to meet up with my girlfriend who's waiting for us."
p "Jeeezus! Those Genesis 8 models are definitely superior to us Genesis 3 models... I should leave now."
stop music
play music "Sounds/randybeachsound.mp3"
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeachDay08b

label RandyBeachParasolRight08:
$ seenparasolright08 = True
scene sundayparasolright03
show randybeachparasol01
$ renpy.pause(2.0, hard=True)
p "Mmmh, legs spread wide..."
window hide
hide randybeachparasol01 with moveoutright
ow "Come to mama boy! It's your LAST chance!"
p "A chance I'm not prepared to take! RUN, RUN FOR YOUR LIFE!"
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
p "That image will remain impregnated in my mind for a long time..."
if stamina >= 1:
    window hide
    $ stamina -=1
    show staminaminus01:
        xalign 0.4 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
jump RandyBeachDay08b

label MaddyFuckDay08:
stop music
play music "Sounds/oceanwaveslow.mp3"
scene maddybeach01 with dissolve
$ renpy.pause(1.0, hard=True)
md "Ah, there you are [name]... I've been waiting for you... TO FUCK ME!"
p "Alright! I'm ready for BUSINESS!"
scene maddybeach02 with dissolve
$ renpy.pause(1.0, hard=True)
md "Then get your trunks off, this part of the beach is very secluded and I'm super-horny!"
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
md "The knowledge you're such a muscled stud gets your rocks off, right [name]?"
p "Oh, AAAH, your words are stirring me into getting even harder!"
md "Well, let's do something about that monstrous fuckpole then shall we?"
label MaddyFootDay08b:
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
        jump MaddyFootDay08b
    "Cum quickly (no stamina penalty)":
        scene maddyfoot03 with dissolve
        play sound "Sounds/ryancumming.mp3"
        $ renpy.pause(2.0, hard=True)
        p "Fuck, your feet are so good on my knob, RHHAAA!"
        md "Wow, I didn't expect you to cum like a stallion so soon [name]...."
        p "Don't worry, it was just a tiny premature load, let's move on to the main dish of the day!"
        jump MaddyFuckChoiceDay08

label MaddyFuckChoiceDay08:
scene maddybeach04 with dissolve
$ renpy.pause(1.0, hard=True)
md "I'm ready for anything, what are you ready for...?"
menu:
    "How about some anal to really get our juices going?" if (maddyarse == False):
        jump MaddyArseDay08
    "How about a blowjob, and I'll lick your pussy at the same time?" if (maddyblowjob == False):
        jump MaddyBlowjobDay08
        
label MaddyArseDay08:
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
label MaddyArseDay08b:
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
        jump MaddyArseDay08b
    "Move on":
        scene maddyarse02 with dissolve
        $ renpy.pause(1.0, hard=True)
        md "This is too much, my stomach is so full of cock! Please let's switch position!"
        menu:
            "Alright, how about a blowjob, and I'll lick your pussy at the same time?" if (maddyblowjob == False):
                jump MaddyBlowjobDay08
            "Fuck her sweet pussy" if ((maddyarse == True) and (maddyblowjob == True)):
                jump MaddyEndFuckDay08

label MaddyBlowjobDay08:
$ maddyblowjob = True
scene maddyfuck05 with dissolve
$ renpy.pause(1.0, hard=True)

scene maddyfuck05b with dissolve
play sound "Sounds/maddyblow01.mp3"
$ renpy.pause(5.0, hard=True)
md "I've never sucked a cock this huge before... But I don't care, I want to choke on it!"
label MaddyBlowjobDay08b:
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
        jump MaddyBlowjobDay08b
    "Move on":
        scene maddybeach04 with dissolve
        $ renpy.pause(1.0, hard=True)
        md "My jaws are starting to tire, your cock is just too gigantic! Please let's switch position!"
        menu:
            "Alright, how about some anal to real get our juices going?" if (maddyarse == False):
                jump MaddyArseDay08
            "Fuck her sweet pussy" if ((maddyarse == True) and (maddyblowjob == True)):
                jump MaddyEndFuckDay08

label MaddyEndFuckDay08:
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
call screen maddyfuckslow08
screen maddyfuckslow08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MaddyFuckFast08")
label MaddyFuckFast08:
hide faster
play music "Sounds/maddyfuckfast.mp3"
show maddyfuckfast
show cum
call screen maddyfuckfast08
screen maddyfuckfast08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MaddyFuckCum08")

label MaddyFuckCum08:
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
md "Good thing this cove is secluded, I can go and clean myself in the sea. Fancy coming along [name]?"
p "Phew, yeah, a nice cooling-off in the ocean would be good!"
$ maddyfucked = True
scene maddyafterfuck with dissolve
$ renpy.pause(1.0, hard=True)
md "Don't tell Frieda you had sex with me, she looks up to me, I don't want to disappoint her..."
p "Sure, absolutely nobody will ever know, I swear... (fingers crossed)."
$ maddyfucksunday = False
$ hour += 1
jump ExploreBeachDay08

label DowntownDay08:
stop music
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"
$ renpy.pause(1.0, hard=True)
p "The bus left me right in front of the main downtown plaza."
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_115
    $ lustaddedB = 1
    call Challenger from _call_Challenger_116
    $ lustaddedB = 1
    call Challenger from _call_Challenger_117
    $ challengercalls += 2

if hour == 17:
    p "I should take the bus for the beach for the final meeting with José..."
    jump EndGame08

label DowntownChoiceDay08b:
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"
if hour == 17:
    p "I should take the bus for the beach for the final meeting with José..."
    jump EndGame08

p "Where should I go?"
menu:
    "Go shopping":
        jump ShopDay08
    "Go to the massage parlour" if (discovermassage == True) and (parlourseen08 == False) and (hour <= 16):
        jump Parlour01Day08
    "Take the bus home":
        $ bushome = True
        jump BusDowntownHomeDay08
    "Take the bus to the beach" if (hour <= 17):
        $ busbeach = True
        jump BusDowntownBeachDay08
    "Go to the downtown gym" if (discovergym == True)  and (hour <= 16):
        jump Gym01Day08
    "Go to Old Joe's Emporium" if (discoveremporium == True):
        jump PawnShop01Day08

label BusDowntownBeachDay08:
p "Ah, here's the bus heading for the beach, I'd better take it..."
$ busbeach = True
jump BusDriveDay08
label BusDowntownHomeDay08:
p "Ah, here's the bus heading to the Burbs, I'd better take it..."
$ bushome = True
jump BusDriveDay08

label PawnShop01Day08:
scene emporium01 with dissolve
$ renpy.pause(1.0, hard=True)
oj "Hello young man. Welcome to Old Joe's Emporium. We buy and sell all sorts of wares."
label PawnShop01Day08b:
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
                jump DowntownChoiceDay08b
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
                        jump DowntownChoiceDay08b
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
                                jump DowntownChoiceDay08b
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
                                jump DowntownChoiceDay08b
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
                        jump DowntownChoiceDay08b
    "What's this place?":
        oj "I just told you boy, are you deaf?"
        jump PawnShop01Day08b
    "Leave":
        jump DowntownChoiceDay08b

label Parlour01Day08:
scene parlour01
$ parlourseen08 = True
$ renpy.pause(1.0, hard=True)
play music "Sounds/parlourmusic.mp3"
ka "Welcome big American boy to \"Misohawny Massage Parlour\"! Me Katsumi, you want massage?"
menu:
    "I was told you did \"full-body massage\"...":
        ka "Yes, sucky sucky 50 dolla."
        p "Ah, I see. Sucky sucky indeed. That's quite expensive for just sucky sucky."
        ka "Me love you long time. For you, more than sucky sucky."
        p "Oh, the conversations we could have my dear..."
        jump ParlourChoiceDay08
    "Yes, how much is it?":
        ka "Normal massage? 10 dolla. More massage, 50 dolla."
        p "And what do I get for 50 dollars exactly?"
        ka "Sucky sucky 50 dolla."
        p "That's a lot of inflation since the Vietnam War..."
        jump ParlourChoiceDay08
    "Nope, not interested...":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceDay08b

label ParlourChoiceDay08:
menu:
    "Get a normal massage (10 $)" if (money >=10):
        jump NormalMassageDay08
    "Choose the \"full-body massage\" experience... (50 $)" if (money >=50) and (stamina >=1):
        jump FullMassageDay08
    "Mmh...I don't seem to have enough money at the moment." if (money <=9):
        ka "You poor. Hah hah. Me not poor. Come back when you not poor."
        p "I certainly will, if just for the highly stimulating conversations."
        jump DowntownChoiceDay08b
    "Mmh, I don't seem to have enough stamina at the moment." if(stamina == 0):
        ka "Ah! You not man enough. You leave and come back when you can cum."
        jump DowntownChoiceDay08b
    "Actually, I don't want anything right now.":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceDay08b

label NormalMassageDay08:
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
                jump Parlour05Day08
            "Forget it. Just give me a normal massage.":
                ka katsumi "Ok, me gonna massage your cock because ssooo BIG."
                jump Parlour05Day08
    "OK, OK, I'll pay the difference for a sucky sucky..." if (money >=40) and (stamina >=1):
        $ suckysucky = True
        $ fuckyfucky = True
        $ money -= 40
        jump Parlour05Day08
    "Why don't you just massage it then like if it was one of my big tense muscles?...":
        ka "Oooh, boy very smart. OK, me gonna massage big American cock. But no sucky sucky, you not pay."
        jump Parlour05Day08

label FullMassageDay08:
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
        jump Parlour05Day08        
    "That's cos all Asian men have small penises.":
        ka "Not true. Some Asian men big penis. You like Trump, you racist."
        ka "Me only do sucky sucky. No fucky fucky. Because you bad boy."
        $ fuckyfucky = False
        jump Parlour05Day08

label Parlour05Day08:
scene parlour05 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Big American monster boycock so big and hard!"
p "Yeah, play with it Katsumi! It's all yours!"

label Parlour06Day08:
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
                jump Parlour07Day08
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
                jump DowntownChoiceDay08b
    
label Parlour07Day08:  
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

label Parlour08Day08:  
scene parlour08 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Reaching top of monstercock take me so long... Me love you long time!"
p "Keep going, you still have quite a few inches to go..."

label Parlour09Day08:  
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
                jump DowntownChoiceDay08b

label Parlour10Day08:  
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
        
label ParlourFuckDay08:
stop music
play music "Sounds/katsumifuck.mp3"
show movieparlourfuck
show cum
call screen parlourfuckcumday08
screen parlourfuckcumday08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("ParlourCumDay08")

label ParlourCumDay08:
stop music
hide movieparlourfuck
scene parlourcum01
stop music
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
ka "You filling me up with so much boyjuice! You so incredible!"

label ParlourCum02Day08:
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
hide staminaminus01
$ hour += 1
jump DowntownChoiceDay08b

label ShopDay08:
if (evictedfromshop == True):
    "You are banned from entering this boutique until tomorrow. Bad boy. VERY bad boy."
    jump DowntownChoiceDay08b
if (shoppingseen08 == True):
    "You already went shopping today. Looks like you might be a shopaholic..."
    jump DowntownChoiceDay08b
if (shoppingseen04 == True):
    jump Shop01Day08
if (shoppingseen04 == False) and (altshop == False):
    jump ShopAltDay08
if (shoppingseen04 == False) and (altshop == True):
    $ altshop08 = True
    jump Shop01Day08

label ShopAltDay08:
$ shoppingseen08 = True
$ altshop08 = True
stop music
scene shopday04 with dissolve
play music "Sounds/shopmusic.mp3"
$ renpy.pause(1.0, hard=True)
p "This boutique looks very expensive..."
p "There's a nice-looking clerk standing behind the counter and several customers looking at skimpy swimsuits...The shop seems to be very busy today..."

label Shop01AltDay08b:
scene shopday04 with dissolve
menu:
    "Go talk to the clerk":
        jump ShopClerkDay08
    "Go talk to the black girl on the left":
        jump ShopCustomerDay08
    "Go talk to the redhead in the middle":
        jump ShopCustomerRedDay08
    "Go talk to the blonde on the right":
        jump ShopCustomerBlondeDay08
    "Go to the changing rooms" if (foundcabins == True) and (rightcabinseen06 == False) and (rightcabinseen07 == False)and (rightcabinseen08 == False):
        jump ShopCabinChoiceAltDay08
    "Leave":
        stop music
        jump DowntownChoiceDay08b    

label Shop01Day08:
$ shoppingseen08 = True
stop music
scene shop with dissolve
play music "Sounds/shopmusic.mp3"
$ renpy.pause(1.0, hard=True)
p "This boutique looks very expensive..."
p "There's a nice-looking clerk standing behind the counter and one customer looking at a skimpy swimsuit..."

label Shop01Day08b:
scene shop with dissolve
menu:
    "Go talk to the clerk":
        jump ShopClerkDay08
    "Go talk to the customer":
        jump ShopCustomerDay08
    "Go to the changing rooms" if (foundcabins == True):
        jump ShopCabinChoiceDay08
    "Leave":
        stop music
        jump DowntownChoiceDay08b

label ShopCustomerRedDay08:
scene shopred01 with dissolve
$ renpy.pause(1.0, hard=True)
re "Oh, you're a man, give me your advice. Should I choose the red or the green bikini?"
menu:
    "The red bikini, it will match your hair.":
        re "Yes, you're right, thank you!"
        jump Shop01AltDay08b    
    "The green bikini, it will match your eyes.":
        re "Yes, you're right, thank you!"
        jump Shop01AltDay08b
    "Imagine her naked":
        scene shopred01b with dissolve
        play sound "Sounds/dreaming.mp3"
        $ renpy.pause(2.0, hard=True)
        re "Err... Hello? Are you ogling my breasts? What a pervert!"
        sc "Stop disturbing the customers! This is a respectable establishment. I must ask you to leave at once!"
        $ evictedfromshop = True
        jump DowntownChoiceDay08b

label ShopCustomerBlondeDay08:
scene shopblonde01 with dissolve
$ renpy.pause(1.0, hard=True)
bl "Can't you see I'm busy thinking? There's too many new bikinis to choose from in this store!"
sc "Stop disturbing the customers!"
jump Shop01AltDay08b

label ShopClerkDay08:
scene shop01 with dissolve
sc "How may I help you?"
menu:
    "Talk to her":
        jump ShopTalkDay08
    "Buy something":
        jump ShopBuyDay08  
    "Leave the counter":
        if (altshop08 == True):
            jump Shop01AltDay08b
        jump Shop01Day08b

label ShopTalkDay08:
menu:
    "You know what would look good on you? Me.":
        scene shop03
        sc "Mmh, lemme think... Yes, it's the worst pick-up line ever."
        jump ShopClerkDay08
    "What's the word on the street downtown?":
        if (downtowntipgiven == True):
            sc "I already gave you a tip today. Stop pestering me."
            jump ShopClerkDay08
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
            jump ShopClerkDay08
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
            jump ShopClerkDay08
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
            jump ShopClerkDay08
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
            jump ShopClerkDay08
        if (downtowntips >= 4):
            sc "It's the weekend, I'm out of tips."
            jump ShopClerkDay08        
    "What's going on today? It seems unusually busy..." if (altshop08 == True):
        sc "We have just received the new summer line of \"Audacious Bikinis\". People are going crazy for them."
        sc "We've also received the new \"Mega-sized Audacious Briefs for Boys\". But not many people seem interested in them unfortunately..."
        p "Err... I might be interested, I want to try one."
        sc "Oh great!, you can pick one from the shelf for your size and try it in one of the changing rooms, if you can find one that's empty..."
        $ foundcabins = True
        jump ShopClerkDay08
        
label ShopBuyDay08:
menu:
    "Buy swimsuit for customer (40$ - pay 20$ from your own pocket)" if (money >= 20) and (seenhallebikini == True) and (boughthallebikini == False):
        scene shop02
        play sound "Sounds/cashregister.wav"
        sc "Here you are. That's for one lucky girl!"        
        $ money -= 20
        $ boughthallebikini = True
        jump HalleGiftDay08

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
        jump ShopClerkDay08

    "Nothing actually":
        jump ShopClerkDay08

    "I don't have enough money to buy anything here." if (money <=9):
        sc "We don't do credit. We don't trust poor people like you."
        p "I feel like... dirt..."
        jump ShopClerkDay08

label ShopCustomerDay08:
scene halleshop01 with dissolve
$ renpy.pause(1.0, hard=True)
if (boughthallebikini == True) and (seenhallebikini == True):
    p "Hey, Halle, why are you still here? I bought you this swimsuit already!"
    show halleshop01b
    ha "Yeah, I know, but the dev is too lazy to remove me from this image..."
    ha "Remember, I'm ACTUALLY at the beach."
    jump Shop01Day08
elif (boughthallebikini == False) and (seenhallebikini == True):
    p "You're still staring at this swimsuit..."
    show halleshop01b
    ha "And I'll keep staring at it until you chip in 20 bucks to buy it for me!"
    if (altshop08 == True):
        jump Shop01AltDay08b
    jump Shop01Day08b

else:
    menu:
        "May I help you with anything miss? Would you like to try this item in one of our cabins?":
            show halleshop01b
            ha "Oh...hum.. Sorry, I didn't realize you worked here... Well, I don't know, it's quite expensive..."
            p "Well, try it on, that's free anyway..."
            ha "Yeah, I guess you're right, I might as well try it on..."
            $ pretendshop = True
            jump HalleChangeDay08
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
                    jump HalleChangeDay08
                "That's too bad, cos I'm sure you would be a hit with that thing on...":
                    ha "(sigh)... Yes, it's too bad..."
                    if (altshop08 == True):
                        jump Shop01AltDay08b
                    jump Shop01Day08b

label HalleChangeDay08:
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
            jump DowntownChoiceDay08b
        "Wait for her to come out":
            jump HalleBikini01Day08
else:
    ha "Hang on a minute, I'm almost ready..."

label HalleBikini01Day08:
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
        jump HalleBikini02Day08
    "Yeah, really hot... Turn around now...":
        ha "Like...that?"
        jump HalleBikini02Day08

label HalleBikini02Day08:
    scene hallebikini02 with dissolve
$ renpy.pause(1.0, hard=True)
if (pretendshop == True):
    p "Yes, that is a definitive perfect fit..."
    ha "Would...you..consider giving me a discount? I'm twenty bucks short to buy it and I really need a new bikini to go to the beach!"
    "The bikini is marked at 40 dollars..."
    menu:
        "Sure, for a girl like you, half-price! Give it to me and I'll make all the arrangements" if (money >= 20):
            ha "Oh, thank you sssoo much. My name is Halle by the way and I'll be wearing this at the beach if you ever fancy joining me (wink)!"
            if (altshop08 == True):
                jump Shop01AltDay08b
            jump Shop01Day08b
        "Mmh, you'll have to show me more to get such a discount price miss...":
            jump HalleTopOffDay08
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
            if (altshop08 == True):
                jump Shop01AltDay08b
            jump Shop01Day08b

else:
    p "Wow, you look really hot...err..."
    ha "The name's Halle. So, since you like it so much, time to chip in 20 bucks like you promised so I can buy it!"
    menu:
        "Ah... About that.. I just realized I don't have enough money." if (money <= 19):
            ha "But..You promised me!"
            p "OK, OK, as soon as I get the money, I'll come back I swear!"
            ha "I'll be here every afternoon, lamenting as to why I can't own this lovely bikini!"
            "Well at least, I know where to find her..."
            if (altshop08 == True):
                jump Shop01AltDay08b
            jump Shop01Day08b
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
            if (altshop08 == True):
                jump Shop01AltDay08b
            jump Shop01Day08b
        "Well, sure...sure... But a little incentive wouldn't hurt... If you know what I mean...":
            ha "I know what you mean...You boys are all the same..."
            jump HalleTopOffDay08
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
            jump ShopClerkDay08
            
label HalleTopOffDay08:
scene halletopoff with dissolve
$ renpy.pause(1.0, hard=True)  
ha "So... Now that you've seen my big sumptuous tits... Time to cough up the money!"
p "Let me regain my breath first... WOW! I'll pay the difference for you baby!"
jump ShopClerkDay08

label HalleGiftDay08:
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
if (altshop08 == True):
    jump Shop01AltDay08b
jump Shop01Day08b

label ShopCabinChoiceDay08:
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
if (chiyofucked == False) and (rightcabinseen == True):
    p "Now let's see, I hope Chiyo is here again... I haven't fucked her yet."
    jump NewChiyoDay08
if (chiyofucked == False) and (rightcabinseen == False):
    jump ShopCabinChoiceAltDay08
if (chiyofucked == True):
    p "I guess I've already fucked Chiyo, no need to waste my time checking the right cabin, let's open the door on the left."
    jump RandyRed01Day08
    
label RandyRed01Day08:
$ randyredseen07 = True
scene randyred01 with dissolve
play sound "Sounds/dooropen.mp3"
$ renpy.pause(1.0, hard=True)
p "Not AGAIN! That redhead boy with the giant cock is about to bang YET ANOTHER HOT CHICK!"
menu:
    "I've had enough of this nonsense, I'm outta here":
        jump Shop01Day08b
    "Continue watching, I'll get an extra peeper point at least... (+1 hr)":
        jump RandyRed02Day08

label RandyRed02Day08:
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
rb "Whatever. Now watch and learn..."
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
p "You don't impress me! You're just some random boy with no meaning in this game anyway!"
rb "Ignorance is bliss. Now if you'll excuse us, I still have a raging hardon and gallons of cum to unload..."
jump Shop01Day08b

label NewChiyoDay08:
stop music
play sound "Sounds/dooropen.mp3"
$ renpy.pause(1.0, hard=True)
scene chiyo01day05 with dissolve
$ rightcabinseen08 = True
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
        jump ChiyoNewFuckREALDay08
    if (lust_points[3] >= 8) and (((pendulumactive == True) and (pendulum == True)) or (pheromone == True)):
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
                jump ChiyoPendulumDay08           
            "Spray yourself with pheromones" if (pheromone == True):
                window hide
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump ChiyoPheromoneDay08
            "Don't use anything":
                jump ChiyoNoFuckDay08
    else:
        jump ChiyoNoFuckDay08
    
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
    jump DowntownChoiceDay08b

label ShopCabinChoiceAltDay08:
stop music
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
label ShopCabinChoiceDay08b:
p "Mmh, which cabin should I choose?"
menu:
    "The cabin on the left" if (leftcabinseen05 == False):
        jump ShopCabin01Day08
    "The cabin in the middle":
        jump ShopCabin02Day08
    "The cabin on the right" if (rightcabinseen05 == False):
        jump ShopCabin03Day08
    "Leave":
        scene shop01 with dissolve
        sc "So, did they fit you big boy? Are you ready to buy a pair?"
        p "Err... No, they're soiled actually, don't know how it happened really..."
        scene shop04 with dissolve
        sc "What? You're soiling my products? Get out of my shop immediately!"
        $ evictedfromshop = True
        jump DowntownChoiceDay08b

label ShopCabin01Day08:
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
        jump ShopCabinChoiceDay08b
    "Ok, why not, I'm bored anyway. (50\%\ chance of +1 stamina)":
        rc "First, I'll get my pussy wet to take my boyfriend's behemoth! I'ts important since he's so gigantic..."
        rb "Watch this buddy. I'm gonna pound her sweet pussy till she's begging for me to stop!"
        jump RandyShop02Day08
        
label RandyShop02Day08:
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
    window hide
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
jump ShopCabinChoiceDay08b

label ShopCabin02Day08:
play sound "Sounds/dooropen.mp3"
scene shopcabin02 with dissolve
$ renpy.pause(1.0, hard=True)
ow "Mmh, what do you think boy? I think this bikini hugs my curves perfectly."
p "Oh no, it's her again! Let's close the door and erase this from my memory..."
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
window hide
$ stamina -=1
show staminaminus01:    
    xalign 0.2 yalign 0.2   
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ eyesore += 1
jump ShopCabinChoiceDay08b

label ShopCabin03Day08:
stop music
play sound "Sounds/dooropen.mp3"
scene shopcabin03 with dissolve
$ rightcabinseen05 = True
label ShopCabin03Day08b:
cy "How rude, I'm all naked and you barge in here just as I was about to put on this bikini..."
p "Sorry but all the stalls are taken and I wanted to try on these new mega-sized briefs."
cy "Mega-sized briefs? Well maybe I could make some room for you in here then... But no touching naughty boy..."
cy "But first, let me put on this bikini..."
scene shopcabin03b with dissolve
$ renpy.pause(1.0, hard=True)
cy "What do you think? Will you be having problems putting on your briefs over that hardening rod, hee hee..."
menu:
    "I'll...try anyway if you don't mind...":
        jump ShopCabin03bDay08
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
        jump ShopCabinChoiceDay08b

label ShopCabin03bDay08:
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
        jump ChiyoFuck01Day08
    if (lust_points[3] >= 8) and (((pendulumactive == True) and (pendulum == True)) or (pheromone == True)):
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
                jump ChiyoPendulumDay08           
            "Spray yourself with pheromones" if (pheromone == True):
                window hide
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump ChiyoPheromoneDay08
            "Don't use anything":
                jump ChiyoFuck01Day08
    if (lust_points[3] <= 7):
        jump ChiyoFuck01Day08
    
if (dildo == False):
    p "I don't have a dildo, I have a REAL cock."
    cy "Too bad then that you don't have one.... I was really horny... But I'm not anymore, you spoilt the mood. Shoot little boy. Hee hee."
    p "What? But you can't leave me in such a state!"
    cy "Of course I can. You shouldn't be in the same stall as me anyway. The woman in the stall next door is horny, you can get that fat cock serviced by her."
    p "AAARGH!"
    play sound "Sounds/doorclosing.mp3"
    scene shopcabin01 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump ShopCabinChoiceAltDay08
            
label ChiyoPendulumDay08:
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
    if (altshop08 == True):
        jump ChiyoFuck01Day08
    jump ChiyoNewFuckREALDay08
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
    if (altshop08 == True):
        jump ChiyoFuck01Day08
    jump ChiyoNewFuckREALDay08

label ChiyoPheromoneDay08:
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
    jump ChiyoFuck01Day08
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
    if (altshop08 == True):
        jump ChiyoFuck01Day08
    jump ChiyoNewFuckREALDay08

label ChiyoFuck01Day08:
scene chiyofuck01 with dissolve
$ renpy.pause(1.0, hard=True)
cy "Get out of those skivvies.... I want to see that monster cock in all its glory!"
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
            jump ChiyoCanFuckDay08
        "Don't drink white bull and keep it for another time":
            p "Lady, I am not the kind of guy you think I am. Begone with your teasing!"
            cy "oh sorry, I didn't realize you were gay."
            p "I'm not, I'm just... tired."
            cy "Poor little boy can get his pee-pee up? boo-hoo!"
            jump DowntownChoiceDay08b
if (stamina <= 0) and (whitebull == False):
    p "Lady, I am not the kind of guy you think I am. Begone with your teasing!"
    cy "oh sorry, I didn't realize you were gay."
    p "I'm not, I'm just... tired."
    cy "Poor little boy can get his pee-pee up? boo-hoo!"
    jump DowntownChoiceDay08b

label ChiyoCanFuckDay08:
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
label ChiyoFuckALTDay08:
scene chiyofuck02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Come on, enough of that, I've got the real thing right here!"

label ChiyoNewFuckREALDay08:
if (lust_points[3] == 10):
    cy "Mmh, I know and it DOES look tasty... What would you want to do with it naughty naughty boy?"
    menu:
        "If it looks tasty, then give me a blowjob!":
            jump ChiyoBlowjobDay08
        "Your pussy looks tasty... And ready for a good pounding!":
            jump ChiyoPussyDay08

cy "I think you've seen enough naughtiness for the day. I came here to buy a bikini, not to get fucked by some random horse-hung boy. So you can leave now..."
p "AAARGH! She's doing it to me again!"
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
jump ShopCabinChoiceAltDay08
            
label ChiyoBlowjobDay08:
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
label ChiyoBlowjobDay08b:
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
        jump ChiyoBlowjobDay08b
    "Your pussy looks tasty... And ready for a good pounding!" if (chiyopussy == False):
         jump ChiyoPussyDay08
    "It's time to stretch that gaping anus even more than that puny dildo you used!" if (chiyoblowjob == True) and (chiyopussy == True):
        jump ChiyoArseDay08

label ChiyoPussyDay08:
scene chiyopussy01 with dissolve
play sound "Sounds/chiyopussy01.mp3"
$ renpy.pause(7.0, hard=True)
p "That's nothing, I'm not even half-way in!"
scene chiyopussy02 with dissolve
play sound "Sounds/chiyopussy02.mp3"
$ renpy.pause(11.0, hard=True)
cy "Oh my God, you're so deep!"
label ChiyoPussyDay08b:
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
        jump ChiyoPussyDay08b
    "If it looks tasty, then give me a blowjob!" if (chiyoblowjob == False):
        jump ChiyoBlowjobDay08
    "It's time to stretch that gaping anus even more than that puny dildo you used!" if (chiyoblowjob == True) and (chiyopussy == True):
        jump ChiyoArseDay08

label ChiyoArseDay08:
scene chiyoarse01 with dissolve
$ renpy.pause(0.3, hard=True)
cy "I'm ready to have my little arsehole stretched by your naughty prick!"
scene
play music "Sounds/chiyofuckslow.mp3"
play movie "Day4/chiyofuckslow.ogv" loop
show movie
show faster
call screen chiyofuckslow08
screen chiyofuckslow08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("ChiyoFuckFastDay08")
label ChiyoFuckFastDay08:
hide faster
play music "Sounds/chiyofuckfast.mp3"
play movie "Day4/chiyofuckfast.ogv" loop
show cum
call screen chiyofuckfast08
screen chiyofuckfast08:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("ChiyoFuckCumDay08")

label ChiyoFuckCumDay08:
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
if (chiyojosewin == False):
    p "(She didn't notice I took a picture of us... Now I'll send it to José)."
    $ chiyowin = True
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I'd better leave this place quietly before anyone notices me..."
jump DowntownChoiceDay08b

label ChiyoNoFuckDay08:
cy "Looks like you won't be getting any Asian poontang from me today... Now shoot little boy, hee hee..."
p "Damn lustmeter! AARGH!"
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
if (altshop07 == True):
    jump ShopCabinChoiceDay08b
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
    jump DowntownChoiceDay08b
  
label Gym01Day08:
$ seengym08 = True
stop music
scene gym01 with dissolve
play music "Sounds/gymreception.mp3"
$ renpy.pause(1.0, hard=True)
if (wenttogymday03 == True):
    $ daysgymseen += 1
if (seengym04 == True):
    $ daysgymseen += 1
if (seengym05 == True):
    $ daysgymseen += 1
if (seengym06 == True):
    $ daysgymseen += 1
if (daysgymseen == 0):
    jump GymFirstDay08
if (daysgymseen == 1) :
    jump GymFirstDay08
if (daysgymseen >= 2):
    jump GymSunday08

label GymFirstDay08:
da "Welcome to \"Jerk n' Clean Fitness Club \". It appears you hardly EVER came HERE?!? What a loser. GET OUT OF MY GYM!"
jump DowntownChoiceDay08b

label GymSunday08:
if studwin:
    da "Well, hello [name]. Glad to see you again. MUSCLE STUD."
if studwin == False:
    da "Well, hello [name]. Glad to see you again."
menu:
    "Call Francine to join you here" if ((gymmember == True) and ((invitedfrancine == True) or (invitedfrancine05 == True) or (invitedfrancine06 == True) or (invitedfrancine07 == True)or (invitedfrancine08 == True))) and (hour <= 15):
        $ francinegym08 = True
        p "I guess it will take her a while to get there, I might as well enjoy the gym until then."
        jump GymSundayChoice08
    "Call Chantelle to join you here" if ((gymmember == True) and ((invitedchantelle == True) or (invitedchantelle05 == True) or (invitedchantelle06 == True) or (invitedchantelle07 == True) or (invitedchantelle08 == True))) and (hour <= 15):
        $ chantellegym08 = True
        p "I guess it will take her a while to get there, I might as well enjoy the gym until then."
        jump GymSundayChoice08
    "Enter the gym as a member" if gymmember:
        if studwin and dorisfucked == False:
            da "Doris has been waiting for you... Arnie left and...She said it was important. Join her in the main room as soon as you're ready."
            p "Alright! POONTANG TIME! I hope."
            $ poontangdoris08 = True
        jump GymSundayChoice08
    "Pay 5$ and enter the gym" if gymmember == False:
        $ money -= 5
        if studwin and dorisfucked == False:
            da "Doris has been waiting for you... Arnie left and...She said it was important. Join her in the main room as soon as you're ready."
            p "Alright! POONTANG TIME! I hope."
            $ poontangdoris08 = True
        jump GymSundayChoice08
    "Leave":    
        jump DowntownChoiceDay08b

label GymSundayChoice08:
stop music
if hour >= 17:
    p "Shit, it's getting late. I need to take the bus to the beach to meet up with José..."
    jump EndGame08
        
if chantellegym08 and talkedchantellegym08 == False:
    $ talkedchantellegym08 = True
    scene chantellegym        
    ch "Hi [name], I've arrived!"
    p "Oh, hey Chantelle, I'm glad you came. Isn't this gym great or what?"
    ch "Yeah, I saw they have amazing tanning beds near the entrance."
    ch "I'll actually go and work on my tan now. See you [name]."
if francinegym08 and talkedfrancinegym08 == False:
    $ talkedfrancinegym08 = True
    scene francinegym
    fa "Hello [name], I've finally made it! I can't wait to see the pole-dancing room!"
    p "Hi Francine, yeah, it's at the back over there. But apparently, men are not allowed in there..."
    fa "Well, if there's no one else around, I might let you in (wink). Enjoy your training, I'm off to work on some dance moves!"

if poontangdoris08 and dorisfucked == False:
    scene gymbackground
    show doriscomp01
    with dissolve
    do "Ah, there you are. I didn't get to fuck you yesterday but I sure will make up for it today. Follow me to the sauna room... *wink*"
    jump DorisFuckDay08

scene daniellagym00 with dissolve
play music "Sounds/gymabience.mp3"
$ renpy.pause(1.0, hard=True)
p "There's Daniella working on a machine..."
menu:
    "Approach Daniella" if daniellafucked == False and stamina >=1:
        jump DaniellaSaturday08
    "Go to the locker room" if (gymlockers05 == False) and (gymlockers06 == False) and (gymlockers07 == False)and (gymlockers08 == False):
        jump GymBoySaturday08
    "Train to get stronger" if (workout == False):
        jump GymWorkoutSaturday08
    "Go to the tanning beds" if (chantellegym08 == True) and (seenchantelletanning08 == False):
        jump ChantelleTanningSaturday08
    "Go to the pole-dancing studio" if (francinegym08 == True) and (seenfrancinegym08 == False):
        jump FrancineSaturday08
    "Leave the gym":
        jump DowntownChoiceDay08b
    
label DaniellaSaturday08:
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
da "Then it's your turn now..."
p "Okay, I'm in."
da "Let's start with the l000lbs barbell we use for competition. Get in your jockstrap, I want to see you half-naked..."
p "I'm comfortable performing in my XXXL jockstraps, no worries..."
da "Good..."
jump DaniellaTest02Day08
        
label DaniellaTest02Day08:
scene daniellagym05 with dissolve
$ renpy.pause(1.0, hard=True)
da "Still feeling confident big boy? This barbell is not even the heaviest set we have..."
p "Err.. Yeah, 1000lbs should be no problem for me..."
scene daniellagym06 with dissolve
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
da "Well done [name]. Now keep that pose. For as long as I tell you to..."
p "Not too long please, it's fucking heavy!"
scene daniellagym07 with dissolve
$ renpy.pause(1.0, hard=True)
da "What's the hurry big boy?"
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
da "Now we're talking! This thing is already well over a foot long..."
p "Eighteen inches to be precise."
scene daniellagym12 with dissolve
$ renpy.pause(1.0, hard=True)
da "And are your loads as big as your package suggests?"
p "Sure, and with unlimited capacity! I'll show you in no time if you keep pumping it!"
da "Now THAT is something I'd like to see. RIGHT NOW!"
scene daniellagym13 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
da "YES! BLAST that hot cum all over the place! I don't care if it's my gym and customers will be complaining about the sticky mess you've made!"
if lust_points[4] == 9:
    window hide
    $ lust_points[4] +=1
    $ score += 1
    show lust01:
        xalign 0.8 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if lust_points[4] <= 8:
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
if lust_points[4] >= 10:
    da "And now, I'm ready to take on that monster cock in EVERY HOLE! I hope you can keep it HARD for me..."
    if (stamina <=0) and (whitebull == True):
        p "(Now is definitely the time to take some White Bull if I want to fuck her on the final day...)"
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
                p "Of course, I'm da man, I'm DA MAN!"
                jump DaniellaFuckDay08
            "Keep your energy drink for another time":
                p "Your handjob was too good and left me with...no more cum.."
                da "What a disappointment. Then I'll leave you like that. Mr not-such-a-stud-after-all. And I'll take my epiclust icon back."
                $ lust_points[14] -=2            
                $ score -= 2
                show lustminus02:
                    xalign 0.8 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus02
                $ hour += 1
                jump GymSundayChoice08
    if (stamina <=0) and (whitebull == False):
        p "I should get going... Thanks for the hand. Job."
        da "What a disappointment. Then I'll leave you like that. Mr not-such-a-stud-after-all. And I'll take my epiclust icon back."
        $ lust_points[14] -=2            
        $ score -= 2
        show lustminus02:
            xalign 0.8 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus02
        $ hour += 1
        jump GymSundayChoice08
$ hour += 1
p "I should get going... Thanks for the hand. Job."
jump GymSundayChoice08

label GymWorkoutSaturday08:
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
jump GymSundayChoice08

label ChantelleTanningSaturday08:
$ seenchantelletanning08 = True
scene chantelletan01 with dissolve
$ renpy.pause(1.0, hard=True)
p "(Ooh... Chantelle is about to get on the tanning bed and she conveniently left the door slightly open...)"
p "(It's amazing how many people forget to close doors on this island really...)"
menu:
    "Leave, you don't want to get caught":
        p "(While I have a nice view of her sumptuous rump, I should probably leave before she sees me...)"
        jump GymSundayChoice08
    "Hang around, what could possibly go wrong?":
        jump ChantelleTanningSaturday08b            

label ChantelleTanningSaturday08b:
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
jump GymSundayChoice08

label GymBoySaturday08:
stop music
scene gymboy01 with dissolve
$ renpy.pause(1.0, hard=True)
$ gymlockers08 = True
p "What is going on here? Looks like a young horse-hung muscle stud being serviced by a couple of dykes..."
menu:
    "Leave, this looks like it's going to be NTR-ish and I don't like that one bit!":
        scene gymboy02
        l01 "Yeah, leave us, you're not invited to the party anyway!"
        jump GymSundayChoice08
    "What the hell, just watch and hope I can join this time (unlikely...)":
        jump GymBoySaturday08b

label GymBoySaturday08b:
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
                jump GymSundayChoice08
            "Stay on, you might get an opportunity somehow...":
                jump GymBoySaturday08c
    "No, I'm just bored, that's all.":
        rb "Ha Ha, right, yeah... Well, watch and learn boy. This is part of my training to retain my title as Muscle Stud saturday." 
        rb "I heard you might be competing too, although you have no chance against me, I've been winning this competition three years in a row already!"
        p "Well, you're about to lose your crown dumbass!"
        l01 "Why don't you shut the hell up and make yourself useful by fisting me, I need to have my pussy loosened up for this young stud's monstercock!"
        menu:
            "I'm in for some good old-fashioned fist-fucking!":
                jump GymBoySaturday08c
            "Leave, it's starting to sound more and more NTR-ish.":
                jump GymSundayChoice08
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
                jump GymBoySaturday08c
            "Leave, it's starting to sound more and more NTR-ish.":
                jump GymSundayChoice08

label GymBoySaturday08c:
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
label GymBoySaturday08cb:
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
        jump GymBoySaturday08cb
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
        jump GymBoySaturday08d

label GymBoySaturday08d:
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
label GymBoySaturday08db:
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
        jump GymBoySaturday08db
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
        jump GymSundayChoice08
        
label FrancineSaturday08:
$ seenfrancinegym08 = True
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
        jump GymSundayChoice08
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
            jump FrancineSaturdayFuck08
        fa "Thank you for such a nice compliment [name]!"
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (lust_points[7] >=8):
                jump FrancinePendulumSaturday08
            "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[7] >=8):
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump FrancinePheromonesSaturday08
            "Well, I'd better leave you finish off your dance routine and get back to the gym...":
                fa "Bye [name], thanks again for inviting me!"
                $ hour += 1
                jump GymSundayChoice08  
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
                jump GymSundayChoice08
        
label FrancinePendulumSaturday08:
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
    jump FrancineSaturdayFuck08
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
    jump FrancineSaturdayFuck08

label FrancinePheromonesSaturday08:
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
    jump FrancineSaturdayFuck08
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
    jump FrancineSaturdayFuck08

label FrancineSaturdayFuck08:
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
            jump FrancineCanFuckDay08
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
            jump GymSundayChoice08
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
    jump GymSundayChoice08

label FrancineCanFuckDay08:
p "Fuck yeah! Let me show you MY pole!"
scene francinepole06 with dissolve
play sound "Sounds/francinefuck01.mp3"
$ renpy.pause(3.0, hard=True)
fa "Oh my, that pole is even thicker than a pole-dancing pole! I can't wait for you to FUCK me!"

label FrancineSaturdayFuckChoice08:
scene francineprefuck with dissolve
$ renpy.pause(1.0, hard=True)
fa "I'm ready when you are!"
menu:
    "Well, I'm ready to facefuck your mouth then! Get on your knees." if (francineblow == False):
        fa "I hope my mouth can stretch enough to take on THAT monster..."
        jump FrancineBlowDay08d
    "Hold on to the pole, I'm gonna fuck you from behind!" if (francinedoggy == False):
        fa  "Ooh, I LOVE that idea!"
        jump FrancineDoggyDay08d
    "Let's make sweet love on the floor." if (francineground == False):
        fa "I hope not TOO sweet... My pussy wants a good pounding (wink)."
        p "Yeah, don't worry about it, just get on board for starters..."
        jump FrancineGroundDay08d
    "I'm ready to blow anytime now, do something Francine!" if (francineblow == True) and (francinedoggy == True) and (francineground == True):
        fa  "I know exactly what to do... Double-handed monstercock handjob it is!"
        jump FrancineMovieDay08d

label FrancineBlowDay08d:
$ francineblow = True
scene francineblow01 with dissolve
play sound "Sounds/francinefuck02.mp3"
$ renpy.pause(3.0, hard=True)
p "Easy...Open wide..."
fa "Mmmm, ggglll..."
scene francineblow02 with dissolve
$ renpy.pause(1.0, hard=True)
p "And your throat now... Wider, wider! Aah, this feels good!"
label FrancineBlowDay08bd:
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
        jump FrancineBlowDay08bd
    "Move on":
        pass
fa "Gaaa gaaa, I think... my jaw... is dislocated..."
p "Never mind that, it will get back to normal soon, let's switch position!"
jump FrancineSaturdayFuckChoice08

label FrancineDoggyDay08d:
$ francinedoggy = True
scene francinefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
fa "Oh fuck, FUCK! Give it to me [name]"
p "No problemo. Get ready, set, GO!"
scene francinefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
fa "AAAOUUW, FUCK it hurts! But it's so good! Do it again, please!"
label FrancineDoggyDay08bd:
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
        jump FrancineDoggyDay08bd
    "Move on":
        pass    
fa "That was the best pole-dancing workout I ever got!"
p "My pole sure did give you a workout! Let's do something else now."
jump FrancineSaturdayFuckChoice08    

label FrancineGroundDay08d:
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
label FrancineGroundbDay08bd:
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
        jump FrancineGroundbDay08bd
    "Move on":
        pass    
fa "My pussy is creaming all over the place..."
p "My cock needs a good cleaning then, let's think of another position shall we?" 
jump FrancineSaturdayFuckChoice08    

label FrancineMovieDay08d:
fa "You'll see, my hands will milk a huge load straight out of that cum-cannon!"
play music "Sounds/francinefuckmovie.mp3"
show francinefuckslow
show faster
call screen francineslowfuckday08d
screen francineslowfuckday08d:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FrancineFastFuckDay08d")

label FrancineFastFuckDay08d:
stop music
hide faster
play music "Sounds/francinefuckmovie.mp3"
show francinefuckfast
show cum
call screen francinefastfuckday08d
screen francinefastfuckday08d:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FrancineCumDay08d")

label FrancineCumDay08d:
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
jump GymSundayChoice08

label DorisFuckDay08:
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
label DorisTitDay08b:
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
        jump DorisTitDay08b
    "Move on":
        scene doristits01 with dissolve
        $ renpy.pause(1.0, hard=True)
        do "Had enough? Scared you might cum too early perhaps?"
        p "N..No, it's just that... I need a... pause..."
        do "So what do you want to do next?"
    
label DorisFuckChoiceDay08:
menu:
    "I want to feel that tight arse wrapped around my monster pole!" if (dorisanal == False):
        do "In my arse? I sure hope I can take something as COLOSSAL as your cock in there!"
        p "So do I. But I'm guessing that somehow the dev will make it fit."
        jump DorisAnalDay08
    "Get on all fours, I'm gonna pound you from behind!!" if (dorisdoggy == False):
        do "WARF, warf! I'll be a good BITCH in heat for you [name]!"
        jump DorisDoggyDay08
    "Ride me like a bull... that's hung like a bull." if (dorisanal == True) and (dorisdoggy == True):
        do "A bull has nothing on YOU Mr MUSCLE STUD!"
        jump DorisCumDay08

label DorisAnalDay08:
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
label DorisAnalDay08b:
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
        jump DorisAnalDay08b
    "Move on":
        do "Thank you so much for such an anal pounding. I feel like my butthole virginity has been taken away from me once again."
        p "Let's switch position then."
        do "What do you have planned for me next STUD?"
        jump DorisFuckChoiceDay08

label DorisDoggyDay08:
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
label DorisDoggyDay08b:
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
        jump DorisDoggyDay08b
    "Move on":
        do "You've fucked my pussy raw...."
        p "That was the deal Doris, you knew what you were getting yourself into."
        do "And I LOVED IT. But let's do something else so it can recover a bit..."
        jump DorisFuckChoiceDay08

label DorisCumDay08:
scene dorispredoggy with dissolve
$ renpy.pause(1.0, hard=True)
do "I don't know how I'm ever going to take such a MASSIVE dong up my poor little fuckhole..."
p "You're going to have to be brave and open wide for it..."
do "Alright. I'll do my best."
label DorisFuckSlowDay08:
show dorisfuckslow
play music "Sounds/dorisslow.mp3"
call screen dorisfuckslow08
screen dorisfuckslow08:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("DorisFuckFastDay08") 

label DorisFuckFastDay08:
hide dorisfuckslow
show dorisfuckfast
stop music
play music "Sounds/dorisfast.mp3"
call screen dorisfuckfast08
screen dorisfuckfast08:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("DorisFuckEndDay08")

label DorisFuckEndDay08:
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
if (nikkifucked == True) and (daniellafucked == True) and (tanyafucked == True) and (achievement.has("brickhouse") == False):
    window hide
    show achievement22:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement22
    $ achievement.grant("brickhouse")
do "I'm gonna go to the shower now, no boys allowed in our locker room, remember!"
p "I'd better get going too then..."
$ hour += 1
jump DowntownChoiceDay08b

label DaniellaFuckDay08:
stop music
scene predaniella01 with dissolve
$ renpy.pause(1.0, hard=True)
da "So, what do you think? Can you handle THAT muscled body?"
p "Yeah, I can handle it, I'm da MAN! And now DA MUSCLE STUD!"
scene predaniella02 with dissolve
$ renpy.pause(1.0, hard=True)
da "Since you won the Mr Muscle Stud competition [name], you get to choose what we do next..."

label DaniellaFuckChoiceDay08:
menu:
    "Give me a blowjob as a reward for being DA MUSCLE STUD MAN!" if (daniellaoral == False):
        da "Of course [name], it's fully deserved after all..."
        jump DaniellaOralDay08
    "Anal is in order. I order anal please." if (daniellaanal == False):
        play sound "Sounds/danielladestroyed.mp3"
        $ renpy.pause(1.0, hard=True)
        da "Oh my God, my tight little butthole is really going to take a pounding isn't it?"
        p "You got that right."
        jump DaniellaAnalDay08
    "I'll spoon you and feed you... MY DONG!" if (daniellaside == False):
        da "I can't wait to feel that log inside me [name]!"
        jump DaniellaSideDay08
    "I'm gonna fuck you from behind until I blast my powerful load all over you!" if (daniellaoral == True) and (daniellaanal == True) and (daniellaside == True):
        da "Of fuck, I'm in for a MASSIVE dose of teenage cum then, hey?"
        p "Yep, you sure are."
        jump DaniellaCumDay08

label DaniellaOralDay08:
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
label DaniellaOralDay08b:
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
        jump DaniellaOralDay08b
    "Move on":
        scene daniellabj01 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "I sure had fun with that fat fuckstick filling up my belly with warm precum..."
        p "Every good thing must end. With an even BETTER thing starting!"
        da "And what BETTER thing do you have planned [name]?"
        jump DaniellaFuckChoiceDay08

label DaniellaAnalDay08:
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
label DaniellaAnalDay08b:
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
        jump DaniellaAnalDay08b
    "Move on":
        da "Ooh, my tender butthole is finally going to have a respite..."
        p "But some other hole isn't."
        da "What do you have planned for me next?"
        jump DaniellaFuckChoiceDay08

label DaniellaSideDay08:
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
label DaniellaSideDay08b:
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
        jump DaniellaSideDay08b
    "Move on":
        da "Please give my poor pussy a break... Let's switch position."
        p "Sure, I can think of many other things we can do..."
        da "Like what?"        
        jump DaniellaFuckChoiceDay08
                
label DaniellaCumDay08:
scene daniellapremoviefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
da "I can feel your cock on my butt. It's so HEAVY! It must weigh a TON!"
p "Several pounds of boymeat for you Daniella!"
da "Fuck me hard with your monster pole [name] I want it in me NOW!"
scene daniellapremoviefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
da "AAAH! It's so fucking BIG!"
p "You asked for it. And now you shall receive."
label DaniellaFuckSlowDay08:
show daniellafuckslow
play music "Sounds/daniellafuckmovie.mp3"
call screen daniellafuckslow07
screen daniellafuckslow07:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("DaniellaFuckFastDay08") 

label DaniellaFuckFastDay08:
hide daniellafuckslow
show daniellafuckfast
call screen daniellafuckfast07
screen daniellafuckfast07:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("DaniellaFuckEndDay08") 

label DaniellaFuckEndDay08:
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
if (daniellajosewin == False):
    p "(She didn't notice I took a picture of her pussy leaking with my cum... Now I'll send it to José)."
    $ daniellawin = True 
if (nikkifucked == True) and (dorisfucked == True) and (tanyafucked == True) and (achievement.has("brickhouse") == False):
    window hide
    show achievement22:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement22
    $ achievement.grant("brickhouse")
da "I'm gonna go to the shower now, no boys allowed in our locker room, remember!"
p "I'd better get going too..."
$ hour += 1
jump DowntownChoiceDay08b

label EndGame08:
hide screen calendar
hide screen statsbackground
stop music
scene finaltally01 with fade
play music "Sounds/oceanwaves.mp3"
$ renpy.pause(1.0, hard=True)
j "There you are, I thought you'd never show up to face the embarrassment, worm..."
p "Oh, I wouldn't have missed this in a thousand years, douchebag!"
if achievement.has("milehigh"):
    $ totalachievements += 1
if achievement.has("mfucker"):
    $ totalachievements += 1
if achievement.has("classroom"):
    $ totalachievements += 1
if achievement.has("asian"):
    $ totalachievements += 1
if achievement.has("colonizer"):
    $ totalachievements += 1
if achievement.has("student"):
    $ totalachievements += 1
if achievement.has("homesteader"):
    $ totalachievements += 1
if achievement.has("lawbreaker"):
    $ totalachievements += 1
if achievement.has("hunter"):
    $ totalachievements += 1
if achievement.has("faculty"):
    $ totalachievements += 1
if achievement.has("cockblocker"):
    $ totalachievements += 1
if achievement.has("cuckmaker"):
    $ totalachievements += 1
if achievement.has("king"):
    $ totalachievements += 1
if achievement.has("bosom"):
    $ totalachievements += 1
if achievement.has("peeper"):
    $ totalachievements += 1
if achievement.has("grabber"):
    $ totalachievements += 1
if achievement.has("watersport"):
    $ totalachievements += 1
if achievement.has("banger"):
    $ totalachievements += 1
if achievement.has("muscleman"):
    $ totalachievements += 1
if achievement.has("threesomer"):
    $ totalachievements += 1
if achievement.has("brickhouse"):
    $ totalachievements += 1
if achievement.has("conqueror"):
    $ totalachievements += 1
if achievement.has("ultimate"):
    $ totalachievements += 1
if achievement.has("extrasontheside"):
    $ totalachievements += 1

if nikkijosewin:
    $ josetally += 1
if nancyjosewin:
    $ josetally += 1
if debbyjosewin:
    $ josetally += 1
if katejosewin:
    $ josetally += 1
if teaganjosewin:
    $ josetally += 1
if sophiajosewin:
    $ josetally += 1
if annajosewin:
    $ josetally += 1
if chantellejosewin:
    $ josetally += 1
if friedajosewin:
    $ josetally += 1
if katsumijosewin:
    $ josetally += 1
if mariajosewin:
    $ josetally += 1
if sandyjosewin:
    $ josetally += 1
if maddyjosewin:
    $ josetally += 1
if jenniferjosewin:
    $ josetally += 1
if laurajosewin:
    $ josetally += 1
if dorisjosewin:
    $ josetally += 1
if chiyojosewin:
    $ josetally += 1
if tanyajosewin:
    $ josetally += 1
if francinejosewin:
    $ josetally += 1
if brittanyjosewin:
    $ josetally += 1
if pamelajosewin:
    $ josetally += 1
if hallejosewin:
    $ josetally += 1
if daniellajosewin:
    $ josetally += 1
if vivianejosewin:
    $ josetally += 1
scene finaltally02 with dissolve
$ renpy.pause(1.0, hard=True)
if [josetally] >= 1:
    j "So here's my tally. I fucked [josetally] girls before you did! What do you have to say about that, loser?"
if [josetally] == 0:
    j "It appears I didn't manage to fuck any girl before you did. But that's only because you cheated by save scumming!"
if nikkiwin:
    $ playertally += 1
if nancywin:
    $ playertally += 1
if debbywin:
    $ playertally += 1
if katewin:
    $ playertally += 1
if teaganwin:
    $ playertally += 1
if sophiawin:
    $ playertally += 1
if annawin:
    $ playertally += 1
if chantellewin:
    $ playertally += 1
if friedawin:
    $ playertally += 1
if katsumiwin:
    $ playertally += 1
if mariawin:
    $ playertally += 1
if sandywin:
    $ playertally += 1
if maddywin:
    $ playertally += 1
if jenniferwin:
    $ playertally += 1
if laurawin:
    $ playertally += 1
if doriswin:
    $ playertally += 1
if chiyowin:
    $ playertally += 1
if tanyawin:
    $ playertally += 1
if francinewin:
    $ playertally += 1
if brittanywin:
    $ playertally += 1
if pamelawin:
    $ playertally += 1
if hallewin:
    $ playertally += 1
if daniellawin:
    $ playertally += 1
if vivianewin:
    $ playertally += 1    
if [playertally] >= ([josetally+1]):
    scene finaltally03 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "I have to say this: I fucked more girls than you, [playertally] to be precise!"
    if [playertally] >= [josetally+10]:
        p "SO WAY MORE THAN YOU. MEGA-LOSER!"
        j "Nooooo! This is so humiliating!!!"
    if [playertally] >= [josetally+5]:
        p "A LOT MORE THAN YOU. LOSER!"
        j "Nooooo! This is so humiliating!!!"
    jump EndWin
    
if [playertally] == [josetally]:
    scene finaltally03 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Ah. It seems we have both fucked the same number of girls... Cos I fucked [playertally] too..."
    if nancyjosewin:
        j "But I fucked your LANDLADY! AH AH, take that!"
        if annawin:
            p "Yeah, but I fucked your MOTHER! Take THAT!"
            if nikkijosewin:
                j "I also fucked your landlady's DAUGHTER! So I WIN!"
                if brittanywin:
                    p "Alright, but listen to this: I FUCKED HARD Brittany! And she loved it, so I WIN!"
                    j "This is getting silly. Let's call it quits then."
                    p "Alright. That bet was dumb anyway."
                    j "Let's go back to our normal lives and pretend nothing happened here."
                    p "What didn't happen?"
                    j "HA HA, touché."
                    jump TotalEnd
                if brittanywin == False:
                    p "Ah shit, that is fucked up, man."
                    j "Still, she was a target, so I WIN! I retain my title, I AM THE SCHOOL STUD!"
                    p "This is so humiliating... OK, I concede. You're the true school stud."
                    j "Oh, but I'm not done with you yet, WORM!"
                    jump EndLose                    
        if annawin == False:
            p "Ah shit, that is fucked up, man."
            j "Still, she was a target, so I WIN! I retain my title, I AM THE SCHOOL STUD!"
            p "This is so humiliating... OK, I concede. You're the true school stud."
            j "Oh, but I'm not done with you yet, WORM!"
            jump EndLose 
    j "Well, you know what that means. I WIN and you LOSE. Cos I'm the CURRENT school stud so I REMAIN the school stud!"
    jump EndLose

if [playertally] <= ([josetally-1]):
    scene finaltally03b with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Ah shit. That's more girls than me since I fucked precisely [playertally] of them..."
    if nancyjosewin:
        j "And to add insult to injury, I fucked your LANDLADY! LOSER!"
    if nikkijosewin:
        j "And let's not forget: your LANDLADY'S DAUGHTER too! So I WIN BIG TIME!"
    p "This is so humiliating... OK, I concede. You're the true school stud."
    j "Oh, but I'm not done with you yet, WORM!"
    jump EndLose
           
label EndWin:    
p "Oh, but I don't think this is humiliating enough. And since everyone has arrived, including your MOTHER, let me demonstrate what I mean..."
j "What....? Don't you DARE!"
scene finalwin01 with dissolve
$ renpy.pause(1.0, hard=True)
an "I'm sorry José, you're my son, but face it, you can't compete with [name], he's a REAL stud. I've been looking for one ever since we moved here and now I've FOUND HIM!"
j "No, mom! Please, don't do this to me!!!!"
p "BE QUIET, WIMP! Nikki, take care of this loudmouth and show him how you treat inferior beta-males like him."
s "With pleasure [name]. Take those trunks off José, we want to see how tiny your pindick is compared to my landboy's MONSTER COCK."
scene finalwin09 with dissolve
play sound "Sounds/sobbing.mp3"
$ renpy.pause(1.0, hard=True)
j "*sob* Please..."
s "See, [name] is about to unveil his monster dong. Watch intently..."
stop sound
scene finalwin01a with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/surprise.mp3"
an "Oh my God, it's even BIGGER than I imagined!"
p "Now you can come back Nikki, the first round is with my landlady's family... Anna, you can go and taunt your son in the meantime. Don't worry, your turn will come."
an "Of course stud, I can't wait to watch what you're made of. While humiliating José. Such a disappointing wimp of a son..."
scene finalwin01aa with dissolve
$ renpy.pause(1.0, hard=True)
an "You call THAT a cock? This pathetic thing is USELESS!"
j "Mother, please! *sob*"
an "Stop wimpering and WATCH the SHOW!"
p "Now, gather round my fair ladies and show him how you worship my HORSECOCK!"
m "Of course my sweet little tenant!"
scene finalwin01b with dissolve
$ renpy.pause(1.0, hard=True)
s "It's ssoo fucking HUGE! My hand can't even get halfway around its incredible GIRTH!"
d "This fat cock was made for being pumped by THREE sets of hands!"
scene finalwin01c with dissolve
$ renpy.pause(1.0, hard=True)
p "Pump my fat shaft! Prep it up!"
label ShaftPumping:
play music "Sounds/wanking.mp3"
play sound "Sounds/lesbians.mp3"
scene finalwin01d with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01c with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01d with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01c with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01d with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01c with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01d with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01c with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01d with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01c with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01d with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01c with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01d with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01c with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01d with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01c with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01d with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01c with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01d with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwin01c with fastdissolve
$ renpy.pause(0.2, hard=True)
stop sound
stop music
menu:
    "Repeat":
        jump ShaftPumping
    "Move on":
        jump FinalWin02
        
label FinalWin02:
p "First, I'll fuck Nikki... While I finger both Nancy's and Debby's pussies with my expert fingers. Spread your legs for me Nikki..."
s "Of course [name]!"
scene finalwinsis01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready?"
m "Yes, we all are my sweet tenant! Fuck my daughter!"
label FinalFuckSis:
play music "Sounds/lesbians.mp3"
play sound "Sounds/sisfuck2.mp3"
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis02 with fastdissolve
$ renpy.pause(0.2, hard=True)
scene finalwinsis03 with fastdissolve
$ renpy.pause(0.2, hard=True)
stop music
stop sound
menu:
    "Repeat":
        jump FinalFuckSis
    "Cum all over her":
        p "I'm gonna dump my first load NOW!"
        m "Cover her tits in your warm spunk, my sweet studly tenant!"
        jump FinalFuckSisCum
  
label FinalFuckSisCum:
scene finalwinsis04 with fastdissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "RHAAA! Nutting BIG TIME!"
d "We can see that [name]! You're HOSING her down with your fat cumpipe!"
scene finalwinsis05 with fastdissolve
$ renpy.pause(1.0, hard=True)
s "Ooh, look at all that RED-HOT SPUNK! It's so warm... Mmmh, I love it... So tasty too! Thank you [name]..."
m "I hope you can still keep it up [name], your landlady is really HORNY!"
p "Don't worry Nancy, you're NEXT. UP THE ARSE. NOW!"
d "Oh wow, such a fucking SUPERSTUD..."
scene finalfuckmom01 with dissolve
$ renpy.pause(1.0, hard=True)
m "I can't believe I'm letting my tenant fuck me right here on a public beach, and RIGHT UP THE ARSE! But it feels sssooo good..."
p "Get ready to ride my dong, Nancy!"
scene finalfuckmom02 with dissolve
play sound "Sounds/womansigh.mp3"
$ renpy.pause(1.0, hard=True)
m "AAAH, sssooo DEEP!"
d "Oooh, you're really taking a LOT of inches in your backside... I'll lick [name]'s monstrous balls so they'll be ready to BLAST another FULL MEGA-LOAD of yummy young cum all over us!"
play music "Sounds/randybeachchickmoaning.mp3"
scene finalfuckmom01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom02 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom01 with fastdissolve
$ renpy.pause(0.3, hard=True)
scene finalfuckmom02 with fastdissolve
$ renpy.pause(0.3, hard=True)
p "I'm about to nut, get ready both of you, I'll PLASTER your bodies in my hot cum!"
stop music
scene finalfuckmom03 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
p "AAAH, FULL BLAST AHEAD!"
d "Damn, your shots are STILL so ENORMOUS [name], where do you keep all that cream? Your balls must have OUNCES of pent-up cum stored in them!"
scene finalfuckmom04 with dissolve
play sound "Sounds/lick.mp3"
$ renpy.pause(1.0, hard=True)
d "And it's so THICK, it's like porridge... Very nourishing too. Maybe I should sell your cum to my customers as an energy drink..."
p "I aim to please..."
scene finalwin02 with dissolve
$ renpy.pause(1.0, hard=True)
an "Oh my God, watching you two FUCK like rabbits has made me so horny...."
p "You're in luck, my giant boymeat is still HARD and READY TO FUCK! Get your bikini off and come over here, Anna..."
m "Ooh, I think you're in for a DEEP, sensuous fuck session Anna.... *wink*"
j "What? But, MOM! You can't fuck that worm like that!"
an "Of course I can, and I WILL, son. You'll just have to take it in like a man. Or more like a cuck-boy! *giggles*"
p "Oh man, getting humiliated by your own mother, that must hurt..."

scene finalwin03a with dissolve
$ renpy.pause(1.0, hard=True)
an "Dear Lord, just look at how HUGE and THICK your rival's cock is, José? I wonder if it will fit in my tiny little pussy..."
p "Beg for it, Anna!"
window hide
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
an "Please Master, fuck me with your ENORMOUS pussy-pleaser! i've been waiting for this moment all week!"
p "With me, not with your lousy son, right?"
an "Of course! He's a wimp, I totally want to humiliate him right now and then I'll kick him out of the house!"
m "Oh, you hear that José? Your mom really wants my landboy's HORSEDICK in her, doesn't she?"
scene finalwin03b with dissolve
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
p "It definitely fits, you were clearly made for taking MY dong, Anna!"
an "YES, I was, and your cock is now the ONLY one I'll fuck!"
show finalfuckannaslow
play music "Sounds/foursomemovie.mp3"
call screen finalfuckannaslow01
screen finalfuckannaslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("FinalFuckAnnaFast08") 

label FinalFuckAnnaFast08:
an "AAAH! Fuck me FASTER please, you GIANT-COCKED SUPERSTUD!"
hide finalfuckannaslow
show finalfuckannafast
call screen finalfuckannafast01
screen finalfuckannafast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("FinalFuckAnnaEnd08")

label FinalFuckAnnaEnd08:    
stop music
scene finalwin04 with dissolve
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
p "She's definitely in LOVE with my DICK, look at how delirious she already is, don't you agree douchebag?"
j "*sob*"
p "I'll take that as a YES."
an "FUCK, I'm cumming... AGAIN! AAAH!"

scene finalwin05a with dissolve
$ renpy.pause(1.0, hard=True)
m "Let me kiss you my sweet little tenant, while you PUMMEL your fuckstick into your new cockslave..."
play sound "Sounds/kissing.mp3"
an "AAAH, AAAH, ssooo good, can't stop CUMMING! Please cum in me [name], I beg you, I WANT your yummy cum!"
p "I'm getting close, don't worry Anna..."
scene finalwin09 with dissolve
$ renpy.pause(1.0, hard=True)
s "Now watch José, watch carefully, [name] is about to blow another monster load deep inside your mother's pussy..."
j "Why are you doing this to me Nikki? I thought we were friends!"
s "No we're not, you're nothing but a weasel and you need to be taught your lesson..."
scene finalwin05b with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "Here you are cockslave! A full fill-up of cum coming your way, RHAAAA!"
an "I can feel it [name], your shots are ssooo POWERFUL!"
m "Pull your mammoth dong out my sweet tenant and cover us in your abundant cream! Show José what a CUM-MISSILE you have between your legs!"
scene finalwin06 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
p "Alright, here you are, receive that hot dose of teenage spunk! RHAAA!"
an "Just look at that will you José? This STUD is BLASTING the biggest cumshots ever!"
s "Each jet is probably more plentiful than a full orgasm from you pathetic prick, isn't it José?"
j "Nooooo! That's not true..."
an "YES IT IS! [name] here can muster OUNCES of cum every time he unleashes a mighty orgasm!"
scene finalwin07 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
p "I ain't done yet, I'm gonna paint you both in my white scum!"
an "YES, you OWE us now [name], my son is nothing but a wimp! YOU'RE THE SCHOOL STUD FOR LIFE!"
s "Did you hear that José? You've lost your title... Big time."
m "Your landlady is ssoo proud of you [name]! Keep pumping that fat load all over the place!"
scene finalwin08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Phew! I'm finally done with your mother José. I think it's time for you to come and clean up the mess I'm made inside her pussy..."
an "Ooh, yes, that will definitely put him in his place. WAY BELOW YOU, STUD!"
scene finalwin09 with dissolve
$ renpy.pause(1.0, hard=True)
s "You heard him... Now go and do your duty. From now on, you're \"creampie cleaning boy\"!"
j "I can't do that, it's.... disgusting!"
an "I'm waiting for you José... Don't make [name] wait or he'll get angry and BEAT YOU UP. He's way more muscular that you are, you know that now, right?"
scene finalwin10 with dissolve
$ renpy.pause(1.0, hard=True)
an "That's it... clean it up, boy. Lick all your rival's virile seed that's seeping from your mom's pussy..."
j "*slurp* *lick*"
p "I think you know your place now douchebag. I'll leave you to your \"family duties\", I have my own to fulfill back home. Not the same kind as you obviously..."
s "Bye LOSER!"
jump Finalwin


label EndLose:
scene finallose01 with dissolve
$ renpy.pause(1.0, hard=True)
j "And now... Prepare for your final humiliation. I'm gonna fuck your landlady right here in front of you!"
m "Oooh, YES PLEASE!"
menu:
    "OK, I admit I've lost but I don't want to see this NTR shit.":
        j "COWARD!"
        jump Finallose
    "I'll watch, I'm a total cuck-boy.":
        pass

scene finallose02 with dissolve
$ renpy.pause(1.0, hard=True)
j "Lie down on the sand Nancy. With your legs spread WIDE OPEN for my MASSIVE cock!"
m "Yes, master STUD."
scene finallose03 with dissolve
$ renpy.pause(1.0, hard=True)
j "Now beg for it. Beg for my TRUE stallion-sized cock!"
window hide
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
m "Please Master, fuck me with your ENORMOUS pussy-pleaser! i've been waiting for this moment all week!"
j "With me, not with your lousy landboy, right?"
m "Of course! He's a wimp, I totally want to NTR him right now and then I'll kick him out of the house!"
an "Oh, you hear that [name]? Your landlady really wants my son's HORSEDICK in her, doesn't she?"
scene finallose04 with dissolve
play sound "Sounds/womansigh.mp3"
$ renpy.pause(1.0, hard=True)
m "Oooh, it's sssoo BIG! He's drilling my pussy all the way to my womb! AAAh, I'm cumming already!!!"
j "The first of many cums... That's what studs do, make women come like crazy on their donkey-dicks. Watch and learn, WORM!"
an "Don't forget about your dear mommy, José!"
scene finallose05 with dissolve
$ renpy.pause(1.0, hard=True)
j "Of course not, mom, come and kiss me while I pound [name]'s landlady's sweet pussy."
play sound "Sounds/kissing.mp3"
$ renpy.pause(1.0, hard=True)
m "Ooh, AAH, CUMMING AGAIN!"
an "And now, fill her up with a HUGE load José!"
j "Sure thing! Right in front of [name]..."
scene finallose06 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
j "FUCK YEAH! I'm dumping my load inside your landlady's pussy, WORM!"
m "I can feel it José, your shots are ssooo POWERFUL!"
an "Pull your mammoth dong out my darling stud-son and cover us in your abundant cream! Show [name] what a CUM-MISSILE you have between your legs!"
scene finallose07 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
j "Alright, here you are, receive that hot dose of teenage spunk! RHAAA!"
m "Just look at that will you my sweet tenant? This STUD is BLASTING the biggest cumshots ever!"
p "Nooo! I can cum WAY MORE than that, I swear!"
s "Not today clearly, you're the beta-weakling now, [name]..."
m "Ooh, I wish you were MY tenant instead of this lousy pindick I have under my roof..."
scene finallose07b with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
j "I ain't done yet, I'm gonna paint you both in my white scum!"
m "YES, you OWE us now José, my tenant is nothing but a wimp! YOU'RE THE SCHOOL STUD FOR LIFE!"
scene finallose09 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
s "Did you hear that [name]? José is the TRUE school STUD... Big time."
an "I'm ssoo proud of you José! Keep pumping that fat load all over the place!"
scene finallose08 with dissolve
$ renpy.pause(2.0, hard=True)
j "FUCK YEAH! I'm finally done with your landlady, [name]. I think it's time for you to come and clean up the mess I've made inside her pussy..."
m "Ooh, yes, that will definitely put him in his place. WAY BELOW YOU, STUD!"
scene finallose09 with dissolve
$ renpy.pause(1.0, hard=True)
s "You heard him... Now go and do your duty [name]. From now on, you're \"creampie cleaning boy\"!"
p "What??? But... I'm da man, I'm..."
s "No you're NOT. You're NOTHING BUT A WORM! Now OBEY your new MASTER!"
m "I'm waiting for you my sweet little tenant... Don't make José wait or he'll get angry and BEAT YOU UP. He's way more muscular that you are, you know that now, right?"
scene finallose10 with dissolve
$ renpy.pause(1.0, hard=True)
m "That's it... clean it up [name]. Lick all your rival's virile seed that's seeping from your landlady's pussy..."
p "*slurp* *lick*"
j "I think you know your place now worm. I'll leave you to your \"household duties\", I have my own to fulfill back home. Not the same kind as you obviously..."
s "Can I come too José?"
j "Of course, there's plenty of inches and cumloads to go around for you Nikki..."
s "Oh goody! Bye [name]. LOSER!"
stop music

label Finallose:
window hide
play sound "Sounds/loser.mp3"
show bigfail:
    xalign 0.5 yalign 0.5
    zoom 0.5
    linear 0.5 zoom 1.0
$ renpy.pause(4.0, hard=True)
hide bigfail
jump TotalEnd

label Finalwin:
play sound "Sounds/winner.mp3"
window hide
show bigwin:
    xalign 0.5 yalign 0.5
    zoom 0.5
    linear 0.5 zoom 1.0
$ renpy.pause(4.0, hard=True)
hide bigwin

label TotalEnd:
hide screen statsbackground
"Your final score is: {b}[score]{/b}"
if (score <=160):
    "Your ranking: {b}Douchebag{/b}"
elif (score <=180):
    "Your ranking: {b}Noob{/b}"
elif (score <=200):
    "Your ranking: {b}Average Joe{/b}"
elif (score <=220):
    "Your ranking: {b}Hunk{/b}"
else:
    "Your ranking: {b}Babe Magnet{/b}"
window hide

"Your have unlocked [totalachievements] achievements out of 24"

play music "Sounds/endmusic.wav"
show newendcredits at left:
    yalign 1.0
    linear 4.0 yalign 0.1
$ renpy.pause(4.0, hard=True)
call screen endcredits
screen endcredits:
    modal True
    imagebutton idle "Icons/epicapocalypse.png" hover "Icons/epicapocalypse.png" xpos 250 ypos 280 focus_mask True action OpenURL("https://www.patreon.com/epiclust")
    imagebutton idle "Icons/replay.png" hover "Icons/replay.png" xpos 100 ypos 580 focus_mask True action Return
    imagebutton idle "Icons/trailer.png" hover "Icons/trailer.png" xpos 600 ypos 500 focus_mask True action OpenURL("https://www.pornhub.com/view_video.php?viewkey=ph5e83164fc28c2")


