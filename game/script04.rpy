label Day04:
# reboot variables
$ day = 4
$ hour = 7
$ stamina = 5
$ wentforjog = False
$ longjog = False
$ shortjog = False
$ detention = False
$ evictedfromstore = False
$ quentinnotfriends = False
$ locswimmingpool = False
$ audacioustried = False
$ evictedfromshop = False
$ shoppingseen = False
$ katephotoplanned04 = False
$ katephotoshoot04 = False
$ katephotoshootleft04 = False
$ quentintipfrancine = False
$ downtowntipgiven = False
$ beachtipgiven = 0
$ schooltipgiven = False
$ workout = False
$ pretendshop = False
$ challengercalls = 0
$ ryangrounded = False

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
call Challenger from _call_Challenger_47
$ lustaddedB = 1
call Challenger from _call_Challenger_48
$ challengercalls += 2

label MorningDay04b:
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "What should I do?"
menu:
    "Put on a black tank top" if (tanktop == True):
        p "Yeah, I'm ready to be a goth. Or a rebel. Or just someone with terrible tastes."
        $ blacktop04 = True
        jump MorningDay04b
    "Take a shower":
        jump ShowerMorningDay04
    "Go for breakfast":
        jump BreakfastDay04
    "Check the computer":
        jump ComputerMorningDay04
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump MorningDay04b
        
label ComputerMorningDay04:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label ComputerMorningDay04b:
scene ryancomputerday
menu:
    "Check the map":
        jump MapMorningDay04
    "Check the stats":
        jump StatsMorningDay04
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump ComputerMorningDay04b
    "Turn the computer off":
        jump MorningDay04b

label MapMorningDay04:
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
p "This shows all the places I know so far on Veri-Bosti Island..."
show screen statsbackground
show screen inventorybutton
show screen calendar
jump ComputerMorningDay04b

label StatsMorningDay04:
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
jump ComputerMorningDay04b

label ShowerMorningDay04:
scene mommorning01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oops, Nancy is in the bathroom, but it's not my fault this time, she left the door open..."
if (nancyfucked == True):
    menu:
        "Walk up behind her and rub your cock between her asscheeks":
            scene mommorning03 with dissolve
            $ renpy.pause(1.0, hard=True)
            m "Oh sweetie... We... don't have time for that right now... You have to get to school at 8am today..."
            p "But Nancy, look at how hard I am for you. A quickie perhaps?"
            m "I'm not like one of your cheap whores from school, it takes longer to satisfy a mature woman like me!"
            m "Just take a quick shower and meet me for breakfast honey."
            scene shower with dissolve
            play music "Sounds/shower.mp3"
            $ renpy.pause(1.0, hard=True)
            p "What a shame we don't have time for sex..."
            jump BreakfastDay04        
        "Call her name so she knows you're there":
            scene mommorning02 with dissolve
            $ renpy.pause(1.0, hard=True)
            m "Oh hello sweetie... I've just finished taking my shower. Remember, you have to get to school at 8am today..."
            p "Sure Nancy, I'll take a quick shower and join you in the kitchen for breakfast in a bit."
            scene shower with dissolve
            play music "Sounds/shower.mp3"
            $ renpy.pause(1.0, hard=True)
            p "What a shame we don't have time for sex..."
            jump BreakfastDay04
if (nancyfucked == False):
    p "Hi Nancy, good morning!"
    scene mommorning02 with dissolve
    $ renpy.pause(1.0, hard=True)
    m "Oh hello sweetie...I've just finished taking my shower. Remember, you have to get to school at 8am today..."
    menu: 
        "Wait for her to leave before entering the shower":
            m "I'll will go down to prepare breakfast. You can take a quick shower honey and come down when you're ready."
            p "Sure Nancy!"
            scene shower with dissolve
            play music "Sounds/shower.mp3"
            $ renpy.pause(1.0, hard=True)
            p "That's nice and relaxing..."
            stop music
            p "I should get dressed and go for breakfast now."
            jump BreakfastDay04
        "Get totally undressed and enter the shower":
            scene mommorning04 with dissolve
            $ renpy.pause(1.0, hard=True)
            m "Oh my sweet Jezus!"
            if (lust_points[16] <= 9):
                $ lust_points[16] +=1
                $ score += 1
                show lust01:
                    xalign 0.5 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
            if (lust_points[16] >= 10):
                show epiclust:
                    xalign 0.5 yalign 0.2
                    zoom 0.5
                    linear 2.0 zoom 1.0
                play sound "Sounds/epiclust.mp3"
                $ renpy.pause(4.0, hard=True)
                hide epiclust
                m "Oh, I'm so horny right now... Come with me downstairs son, I need a quick pounding from that massive cock of yours!"
                p "Alright! No shower for me today, straight to sext with my super-stacked landlady! Yippee!"
                jump MomMorningFuckDay04
            m "(cough) Err, I'll leave you to take your shower honey. Come down when you're ready..."
            scene shower with dissolve
            play music "Sounds/shower.mp3"
            $ renpy.pause(1.0, hard=True)
            p "He he, she saw the mighty dong... I'm da man, I'm DA MAN!"
            stop music
            p "I should get dressed and go for breakfast now."
            jump BreakfastDay04

label MomMorningFuckDay04:
scene eveningmomfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
m "You like what you see [name]? What would you like me to do next my studly tenant?"
menu:
    "I need to stick my cock between those big jugs...":
        jump MorningTitfuckDay04
    "I don't know but I'm about to explode!":
        jump MorningBlowjobDay04

label MorningTitfuckDay04:
$ momtitfuck = True
scene momtitfuck01 with dissolve
m "Of course [name]. I will take care of that monster with my huge jugs, you just relax and let me do all the work."
label MorningTitfuckDay04b:
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
        jump MorningTitfuckDay04b
    "Move on":
        pass
if (stamina >=2):
    menu: 
        "Cum, you've got another load for later":
            jump MorningTitfuckCumDay04            
        "Don't cum yet and tell her you're about to explode":
            m "Oh sweetie, your huge cock looks like it's ready to explode!"
            if (momblowjob == False):
               m "Bring that massive fuckstick to my mouth [name]!"
               jump MorningBlowjobDay04
            else: 
                m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
                jump MorningPussyLickDay04
if (stamina <=1):
    m "Oh sweetie, your huge cock looks like it's ready to explode!"
    if (momblowjob == False):
        m "Bring that massive fuckstick to my mouth [name]!"
        jump MorningBlowjobDay04
    else: 
        m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
        jump MorningPussyLickDay04            

label MorningTitfuckCumDay04:
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
if (momblowjob == False):
    m "Bring that massive fuckstick to my mouth [name]!"
    jump MorningBlowjobDay04
else: 
    m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
    jump MorningPussyLickDay04

label MorningBlowjobDay04:
$ momblowjob = True
scene momblowjob01 with dissolve
#play sound "Sounds/momlick01.mp3"  
$ renpy.pause(.0, hard=True)
m "My God [name], your cock... It's just GIGANTIC! I can't even wrap my fingers around its incredible girth..."
scene momblowjob01b with dissolve
#play sound "Sounds/momlick02.mp3"  
$ renpy.pause(1.0, hard=True)         
m "Mmmh... And those balls... So HEAVY, I just have to taste them..."         
label MorningBlowjobDay04b:
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
        jump MorningBlowjobDay04b
    "Move on":
        pass

m "Oh sweetie, your huge cock looks like it's ready to explode!"
if (momtitfuck == False):
    m "Why don't you stick your pud between my big tits?"
    jump MorningTitfuckDay04
if (momtitfuck == True):
    m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
    jump MorningPussyLickDay04            
 
label MorningPussyLickDay04:
scene eveningmomclit with dissolve
#play sound "Sounds/momclit.mp3"
$ renpy.pause(1.0, hard=True)
m "Mmmh, you do that so well sweetie! You really know what you're doing! AAAH!"
m "Now it's time for meto reward you... With my pussy!"
jump MorningFullFuckDay04

label MorningFullFuckDay04:
scene eveningmomready with dissolve
#play sound "Sounds/momready.mp3"
$ renpy.pause(1.0, hard=True)
m "See my tender pink pussy? It's wet and ready for you my studly tenant! Come and pound it!"
scene
#play music "Sounds/momslowfuck.mp3"
play movie "Day3/momfuckslow.ogv" loop
show movie with fade
show faster
call screen morningfuckslowday04
screen morningfuckslowday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MorningFuckFastDay04")
label MorningFuckFastDay04:
hide faster
stop music
#play music "Sounds/momfastfuck.mp3"
play movie "Day3/momfuckfast.ogv" loop
show cum
call screen morningfuckfastday04
screen morningfuckfastday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MorningFuckCumDay04")

label MorningFuckCumDay04:
stop movie
stop music
scene momfuckcum01 with dissolve
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
if (achievement.has("mfucker") == False):
    show achievement02:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement02
    $ achievement.grant("mfucker")
"Press a at any time during the game to access the achievements screen."
m "Damn [name], you really had a lot of pent-up cum stored in those huge balls..."
m "It's my duty to make sure you empty them regularly so you don't get blue balls and it hurts..."
m "Oh my God, you're gonna be late for your school trip [name]!"
m "Go and get dressed quickly, I'll make some sandwiches for you to take with you... We'll keep this...incident... between us sweetie."
if (nancyjosewin == False):
    p "Sure Nancy! (She didn't notice I took a picture of us... Now I'll send it to José)."
    $ nancywin = True
if (nancyjosewin == True):
    p "Sure Nancy! (Although everyone already knows you fucked José you slut...)"
$ nancyfucked = True
jump BigDong01b

label BreakfastDay04:
scene breakfastday04 with dissolve
stop music
$ renpy.pause(1.0, hard=True) 
m "So, are you excited about your school trip son?"
p "Sure, beats being inside a classroom anyway."
m "Mmmpf, it is meant to be an academic outing where you learn things about the island's natural riches...."
m "I made you a sandwich for lunch since I've been told you will not come back in time for school lunch. Don't forget it on your way to school!"
p "What about pocket money?"
if (nancywin == True):
    m "Oh honey... Nikki is not here, it wouldn't be fair. But you were so good to me lately..."
    m "I'll give you pocket money but don't tell Nikki or she'll be jealous."
    p "My lips are sealed!"
    $ money += 5
if (pocketmoney == True):
    m "You are punished remember? No pocket money for you again today!"
    p "It's not fair, I was set up... (mumble mumble)..."
if (nancywin == False):
    m "Oh honey... Nikki is not here, it wouldn't be fair... So no pocket money today I'm afraid."
if (blacktop == True) and (blacktop04 == True): 
    scene breakfastday04b with dissolve
    m "And you're wearing this horrible black top AGAIN?"
    if (lust_points[16] <= 9):
        $ lust_points[16] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.5 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
    p "Well, I kinda like it..."
    jump BreakfastEndDay04
if (blacktop == False) and (blacktop04 == True): 
    m "Why are you wearing a black top all of a sudden? I always only bought you white t-shirts..."
    p "It's my new style. I'm a rebel now."
    show mombreakfast02day04 with dissolve
    scene breakfastday04b with dissolve
    m "Well, I can't say that I approve of this new \"rebel\" style..."
    if (lust_points[16] <= 9):
        $ lust_points[16] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.5 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
    p "Well I wear what I want! I bought it with my own money, so there!"

label BreakfastEndDay04:
scene breakfastday04 with dissolve
m "Now hurry up or you'll be late and the bus leaves at 8am sharp, you don't want to miss it!"

label BigDong01:
$ hour += 1
label BigDong01b:
scene bigdongbus with dissolve
play music "Sounds/busidle.mp3"
$ renpy.pause(1.0, hard=True)
ma "Ah, there's the last boy. Come on [name], move it, the bus is ready to leave."
t "OK, is everyone here now? I can 't see Maddy. Has anyone seen her?"
vi "I didn't see her board the bus. She's obviously late."
t "Well, we can't wait for her. The bus is leaving and it's a long trip to Bigdong Falls. Take a seat on the bus everyone."
if (teagangrocery == True) and (seenteaganhouse == False):
    scene busteagan with dissolve
    $ renpy.pause(1.0, hard=True)    
    t "I am very disappointed that you failed to deliver my groceries yesterday as promised!"
    $ lust_points[22] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.3 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    t "I won't be needing them delivered by YOU today! I found myself another grocery boy... José."
    if (teaganjosewin == False):
        $ lust_pointsB[22] +=1
        show challengerlustplus01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustplus01
    p "(WHAT??? I can't believe Teagan could possibly fall for this douchebag! I mean, what does he have on me?)"
    jump BusDongChoice
    
label BusDongChoice:
scene bigdongbus02 with dissolve
play music "Sounds/busdrive.mp3"
$ renpy.pause(1.0, hard=True)
p "We're on our way to Bigdong Falls!"
label BusDongChoiceb:
scene bigdongbus02 with dissolve
$ renpy.pause(1.0, hard=True)
menu:
    "Talk to Frieda":
        scene busfrieda with dissolve
        $ renpy.pause(1.0, hard=True)
        fr "I'm worried about Maddy. It's not like her to be late for anything."
        p "Don't worry, I'm sure it's nothing, she must have overslept, that's all."
        jump BusDongChoiceb
    "Talk to Laura" if (spokenlaurabus == False):
        $ spokenlaurabus = True
        scene buslaura01 with dissolve
        $ renpy.pause(1.0, hard=True)
        menu:
            "Hey Laura, did you sleep well? After last night..." if (laurafucked == True):
                scene buslaura02 with dissolve
                $ renpy.pause(1.0, hard=True)
                la "Not really, my pussy is sore and I can barely walk..."
                la "And now, we're going on a bloody trek, thanks for nothing [name]!"
                p "Well... err... It's not my fault I have a huge penis you know..."
                jump BusDongChoiceb
            "Hey Laura, you look like Laura Croft. Lara Croft, Laura Croft, get it?":
                scene buslaura02 with dissolve
                $ renpy.pause(1.0, hard=True)
                la "You think you're funny? I hate these clothes and you're comparing me to a video game character?"
                la "I'm a REAL person, not the figment of some computer nerd's imagination! Get out of my face!"
                p "But... it was just a joke..."
                if (lust_points[13] <= 9):
                    $ lust_points[13] -=1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.6 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                jump BusDongChoiceb
            "What are you up to this afternoon Laura?":
                if (seencampfireday03 == False) and (lauraritual == True):
                    scene buslaura02 with dissolve
                    la "You didn't turn up last night. That was yet another major disappointment in my life."
                    $ lust_points[13] -=1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.35 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                    p "Yeah, I was busy dealing with... err... family matters. God I hate my family!"
                    scene buslaura01 with dissolve
                    la "That's good. We might give you another chance then. Meet us tonight. For real this time!"
                    p "I'll be there, you can count on me Laura! Oh, and death to all but metal and all that."
                    $ lauraritual04 = True
                    jump BusDongChoiceb
                la "Hanging out with Damian and Joséphine. Discussing how much life sucks. As per usual... (sigh)"
                if (seencampfireday03 == True):
                    p "Will you try out again some... you know... goth things around the campfire tonight?"
                    if (blacktop04 == True):
                        la "Yeah, why don't you join us? I like having you around... Damian is such a bore..."
                        p "Err... yeah, I'll think about it."
                        $ lauraritual04 = True
                        jump BusDongChoiceb
                    if (blacktop04 == False):
                        la "Probably, but you're not invited. Not with this boring white t-shirt you're wearing..."
                        p "Well, I only have one black top, that's why I'm wearing white today. But deep inside, I'm like, totally a goth!"
                        scene buslaura02 with dissolve
                        $ renpy.pause(1.0, hard=True)                        
                        la "A true goth's wardrobe is filled entirely with dark and depressing clothes..."                        
                        jump BusDongChoiceb
                if (seencampfireday03 == False):
                    p "Alright, then maybe I'll see you at the back of the school then... To talk about how much life sucks and whatnot."
                    if (blacktop04 == True):
                        la "Sure... Damian is such a bore, I wouldn't mind someone else to talk to..."
                        jump BusDongChoiceb
                    if (blacktop04 == False):
                        scene buslaura02 with dissolve
                        la "Unlikely. You're not wearing black, how could you possibly discuss the inequities of life in a white tanktop?"
                jump BusDongChoiceb
            "I read that book you gave me." if (bookread == True) and (toldlaurabook == False):
                $ toldlaurabook = True
                la "Oh really? And what did you think about it then?"
                p "Fascinating. I didn't realize so many celebrities were goths."
                p "Ozzy Osbourne, Marilyn Manson, the Addams Family, Mike Pence... It opened my eyes." 
                la "Well, that's great! You're half-way to becoming a true goth then."
                $ lust_points[13] +=1
                $ score += 1
                show lust01:
                    xalign 0.1 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01 
                jump BusDongChoiceb            
    "Talk to Quentin":
        if (katefucked == True):
            scene busquentin02 with dissolve
            $ renpy.pause(1.0, hard=True)
            p "Any tips for me today buddy?"
            q "I can't believe you're asking. After what you did with my.... girlfriend...."
            p "(Oh shit, he knows I fucked Kate....)"
            jump BusDongChoiceb
        if (katefucked == False):
            scene busquentin01 with dissolve
            $ renpy.pause(1.0, hard=True)
            p "Any tips for me today buddy?"
            q "Of course, I have my ears everywhere on this island, I am a fountain of knowledge!"
            p "Yeah, OK... So what do you have for me today then?"
            q "Ah ah! I know for a fact that Francine loves pole-dancing and practices it wherever and whenever she can."
            p "Mmh, interesting. Thanks for the tip Quentin."
            $ quentintipfrancine = True
            jump BusDongChoiceb
    "Talk to Kate" if (spokenkatebus == False):
        $ spokenkatebus = True
        if (katephotoplanned == True) and (katephotoshoot == False) and (katephotoshootleft == False):
            scene buskate02 with dissolve
            $ renpy.pause(1.0, hard=True)
            k "I came round to your place yesterday and you stood me up!"
            p "Ah... Shit, I'm so sorry, I was caught up with something else..."
            k "What could be more important than my bikinis? I just can't rely on you clearly [name]! Don't talk to me!"
            $ lust_points[11] -=2
            show lustminus02:
                    xalign 0.3 yalign 0.2
                    linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus02
            jump BusDongChoiceb
        scene buskate01 with dissolve
        $ renpy.pause(1.0, hard=True)
        menu:   
            "Hey Kate, did you have a good time yesterday? (Wink wink)" if (katefucked == True):
                k "Why are you winking? I don't understand..."
                p "I mean, by the pool, at my place, you know... What we did..."
                k "Oh yeah, I chose a bikini for the beauty pageant, I remember! Thank you for helping me out [name]!"
                p "No, I meant the \"other\" thing... Oh, forget it.(sigh)"
                jump BusDongChoiceb
            "Hey Kate, you know what I found out? That scumbag José is totally backing Brittany for prom queen!" if ((seenlockerbrit == True) or (lust_pointsB[1] >= 8)) and (toldkatejose == False):
                scene buskate02 with dissolve
                $ renpy.pause(1.0, hard=True)
                k "What? Oooh, no... I need his vote to win... What a loser, what does he find in her?"
                $ toldkatejose = True
                if (lust_pointsB[11] == 1):
                    $ lust_pointsB[11] -=1
                    show challengerlustminus01:
                        xalign 0.3 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide challengerlustminus01
                if (lust_pointsB[11] >= 2):
                    $ lust_pointsB[11] -=2
                    show challengerlustminus02:
                        xalign 0.3 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide challengerlustminus02                    
                p "Who knows, that guy has shit for brains."
                jump BusDongChoiceb
            "Since you will compete in the bikini pageant, I could maybe take pictures of you so you can better decide which bikini to choose?" if (katephotoasked == False):
                k "Ooh, are you a photographer? I've been looking for someone who could show me what I look like, because I can't see myself."
                p "Yeah sure... I have a great camera, I'll let you know when I set everything up and you can come round to my place to try on some bikinis."
                k "Oooh, I can't wait! Hee hee!"
                window hide
                $ lust_points[11] += 1
                $ score += 1
                show lust01:
                    xalign 0.3 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
                p "(I'd better find a good camera real soon...)"
                $ katephotoasked = True
                jump BusDongChoiceb
            "Hey Kate, are you ready for a photoshoot today?" if (katephotoasked == True) and (katefucked == False):
                $ katephotoplanned04 = True
                k "Oooh, yes! I have a couple of bikinis I would like to try on!"
                p "Come to my place at 5 or 6pm then, I'll have everything set up!"
                k "Oh, really? That's so great, I'll be there!"
                if (camera == False):
                    p "(I'd better find a camera TODAY or she'll be mighty disappointed...)"
                    jump BusDongChoiceb
                if (camera == True):
                    p "(I'd better make sure I'm back home by 5 or 6pm...)"
                    jump BusDongChoiceb
            "Why don't you tell Quentin you're not interested in him?":
                scene buskate02 with dissolve
                k "I keep telling him but he doesn't understand..."
                p "I guess that's because he's in love with you."
                k "Eeww. I don't want anything to do with him. He's such a nerd."
                jump BusDongChoiceb
    "I'm done talking to people.":
        jump BigDong02

label BigDong02:
stop music
play music "Sounds/trail.mp3"
scene trail01 with dissolve
$ hour += 1
$ renpy.pause(1.0, hard=True)
t "Is everyone's gear ready? We will be hiking first through the forest before reaching our destination, the island's famous Bigdong Falls!"
t "Stay close to one of us, Maria who will be at the front of the party, Viviane at the back or me in the middle."
menu:
    "Stay close to the teacher (Teagan)":
        jump TeaganTrail
    "Stay close to the sports instructor (Viviane)":
        jump VivianeTrail
    "Stay close to the librarian (Maria)":
        jump MariaTrail

label TeaganTrail:
$ teagantrail = True
scene trailteagan01 with dissolve
$ renpy.pause(1.0, hard=True)
t "I see you've chosen to be with us [name]..."
menu:
    "My thirst for knowledge is insatiable and you are the best teacher.":
        t "Why don't I believe you?"
        p "Err..."
        k "What a nerd..."
        if (katefucked == False):
            $ lust_points[11] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.3 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01        
        jump TeaganTrail02   
    "In case we are attacked by savages, the center is the safest place.":
        t "There are no savages on this island. They were all slaughtered by the French centuries ago."
        t "And I am surprised by your cowardly attitude I must say..."
        $ lust_points[22] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump TeaganTrail02
    "Well, Quentin is my best friend, right buddy?":
        if (katefucked == True):
            q "I don't think so. Humpf."
        if (katefucked == False):
            q "Of course, and we are both adventurous and.... Eeek, a snake!"
        jump TeaganTrail02

label VivianeTrail:
$ vivianetrail = True
scene trailviviane01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "I see you've chosen to be with us at the back [name]..."
menu:
    "You need me to defend you in case we are attacked by savages.":
        vi "Are you suggesting that I am not capable of defending myself?"
        p "No.. Err... I meant..."
        $ lust_points[23] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        vi "And anyway, there are no savages on this island, they were all slaughtered by the French centuries ago... And I'm a descendant of those French colonists..."
        jump VivianeTrail02
    "I want to take my time and admire the view.":
        vi "Well, we still need to get to Bigdong Falls fast. So don't fall back too much."
        jump VivianeTrail02

label MariaTrail:
$ mariatrail = True
scene trailmaria01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "I see you've chosen to be with us at the front [name]..."
menu:
    "You need a boy to defend you in case we are attacked by savages.":
        ma "I think we girls are perfectly capable of defending ourselves, thank you very much."
        ma "And anyway, there are no savages on this island, they were all slaughtered by the French centuries ago..."
        jump MariaTrail02
    "My thirst for knowledge is insatiable and you are an open encyclopedia.":
        ma "That's real cute. I'm just a part-time librarian but your compliment is much appreciated... [name]."
        $ lust_points[15] += 1
        $ score += 1
        show lust01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01        
        jump MariaTrail02
        
label TeaganTrail02:
scene trailteagan02 with dissolve
$ renpy.pause(1.0, hard=True)
t "This forest is millions of years old and has an amazing biodiversity..."
menu:
    "Look out for a \"Bostiboobicus Gigantus\"":
        scene trailflower with dissolve
        $ renpy.pause(1.0, hard=True)
        menu:
            "Ask Teagan if she knows what it is":
                t "It looks like a \"Bostiboobicus Gigantus\". Don't touch it [name], it stings... I think."
                p "Ah Ok. It stinks too."
                jump LyreBird
            "Investigate":
                if (plantknowledge == True):
                    p "It definitely looks like a \"Bostiboobicus Gigantus\"... And it stinks like one too."
                    menu:
                        "Pick it up":
                            $ flower = True
                            show flower
                            show square
                            play sound "Sounds/found.mp3"
                            "You acquired a smelly flower."
                            hide square
                            hide flower
                            $ smellyflower = True
                            jump LyreBird
                        "Don't pick it up, it will probably rot in my pocket anyway and it stinks to high heavens.":
                            jump LyreBird
                if (plantknowledge == False):
                    p "Hum, I have no idea what this plant is and it stinks to high heavens. I'd better leave it, I doubt this is what Principal Titsworthy is after."
                    jump LyreBird                    
    "Continue listening to the teacher":
        t "Veri-Bosti has a unique flora and fauna. Unfortunately, our President-Governor recently said that he would stop protecting this area."
        p "I think he was misunderstood by the fake media. He actually meant to say that \"he would NOT stop protecting this area.\" He corrected himself on Fuxnews."
        t "In any case, enjoy this beautiful site while it lasts kids..."
        t "Oh, I hear something in those bushes over there..."
        jump LyreBird                    

label VivianeTrail02:
scene trailviviane02 with dissolve
$ renpy.pause(1.0, hard=True)
vi "That's a nice hike, it 's good for the leg muscles!"
menu:
    "Look out for a \"Bostiboobicus Gigantus\"":
        scene trailflower with dissolve
        $ renpy.pause(1.0, hard=True)
        menu:
            "Ask Viviane if she knows what it is":
                vi "How should I know, I'm not a botanist! It's just some stupid flower, move along [name], we're trailing the others."
                jump LyreBird
            "Investigate":
                if (plantknowledge == True):
                    p "It definitely looks like a \"Bostiboobicus Gigantus\"... And it stinks like one too."
                    menu:
                        "Pick it up":
                            $ flower = True
                            show flower
                            show square
                            play sound "Sounds/found.mp3"
                            "You acquired a smelly flower."
                            hide square
                            hide flower
                            jump LyreBird
                            $ smellyflower = True
                        "Don't pick it up, it will probably rot in my pocket anyway and it stinks to high heavens.":
                            jump LyreBird
                if (plantknowledge == False):
                    p "Hum, I have no idea what this plant is and it stinks to high heavens. I'd better leave it, I doubt this is what Principal Titsworthy is after."
                    jump LyreBird 
    "Offer to carry Frieda":
        scene trailviviane03 with dissolve
        $ renpy.pause(1.0, hard=True)
        if (friedafucked == False):
            fr "I can walk [name], I am not tired at all, thank you."
            p "OK, let me know if you ever get tired Frieda, I'll be there for you!"
            jump LyreBird
        if (friedafucked == True):
            fr "Thank you [name]. I am zooo tired, after all the exercise I did yesterday... vith you."
            vi "What are you talking about Frieda? Have you too been practising swimming together?"
            p "Yes, exactly, we did some more swimming in the afternoon, right Frieda? (nudge nudge)"
            fr "Ja, swimming! We... practised ze backstroke a lot... "
            vi "Well, I'm glad to see you are taking the swimming competition on Sunday so seriously [name]!"
            $ lust_points[23] += 1
            $ score += 1
            show lust01:
                xalign 0.1 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01        
            jump LyreBird

label MariaTrail02:
scene trailmaria02 with dissolve
$ renpy.pause(1.0, hard=True)
menu:
    "Look out for a \"Bostiboobicus Gigantus\"":
        scene trailflower with dissolve
        $ renpy.pause(1.0, hard=True)
        p "There's a peculiar flower on the side of the trail..."
        if (plantknowledge == True):
            p "It definitely looks like a \"Bostiboobicus Gigantus\"... And it stinks like one too."
            menu:
                "Pick it up":
                    ma "What on earth do you think you're doing? Do not even touch that protected plant, it's illegal!"
                    $ lust_points[15] -=1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.15 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                    p "Ah, err, sorry, I just thought it was a common flower..."
                    ma "Now stay close to me, we still have a few more miles to walk. And don't touch the wildlife!"
                    jump LyreBird
                "Let Maria know you spotted a \"Bostiboobicus Gigantus\"":
                    ma "It is indeed a \"Bostiboobicus Gigantus\"! That's a very rare plant, well done for spotting it [name]!"
                    $ lust_points[15] +=1
                    $ score += 1
                    show lust01:
                        xalign 0.15 yalign 0.4
                        linear 1.0 yalign 0.2
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lust01
                    ma "Gather round everyone, and admire the island's national flower. But don't get too close to it, it stinks to high heavens."
                    fc "Oh, c'est une \"Gigantus Bostinichoncus\", incroyable!"
                    p "Mmh, I didn't realize Latin was different in French than in English..."
                    la "This smell is unbearable! God I hate this flower..."
                    ma "Well, it's a very expensive flower, it can fetch thousands of dollars on the black market. But it's illegal to pick it up, so let's move on."                    
                    jump LyreBird
        if (plantknowledge == False):
            p "Hum, I have no idea what this plant is... Maybe I should ask Maria."
            ma "It's a \"Bostiboobicus Gigantus\"! That's a very rare plant, you're lucky to have spotted one [name]!"
            ma "Gather round Laura and Joséphine, and admire the island's national flower. But don't get too close to it, it stinks to high heavens."
            fc "Oh, c'est une \"Gigantus Bostinichoncus\", incroyable!"
            p "Mmh, I didn't realize latin was different in French than in English..."
            la "This smell is unbearable! God I hate this flower... This is your fault [name]!"
            if (lust_points[13] <=9):
                $ lust_points[13] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.15 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01            
            ma "Well, it's a very expensive flower, it can fetch thousands of dollars on the black market. But it's illegal to pick it up, so let's move on."
            jump LyreBird 
    "Ask Maria to carry her bag for her":
        ma "Thanks for the offer [name], but I am perfectly capable of carrying my bag myself..."
        jump LyreBird 
        

label LyreBird:
stop music
play music "Sounds/trail.mp3"
scene lyrebird01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Oh, look kids, there's a lyrebird in those bushes! Shh, don't make any sudden moves... This is a real treat, they usually hide in the forest."
ma "The lyrebird can reproduce any sound he hears, he's like the imitator of the animal kingdom."
menu:
    "Fart":
        window hide
        play sound "Sounds/fart.mp3"
        $ renpy.pause(1.0, hard=True)
        scene lyrebird02 with dissolve
        ly "(fart)"
        window hide
        play sound "Sounds/fart.mp3"
        $ renpy.pause(1.0, hard=True)
        scene lyrebird01 with dissolve
        t "Really? That's the best you can do? You are so immature [name]..."
        vi "And thanks for the smell! Phew, stinky stinky... What did you eat this morning for Christ's sake?"
        $ lust_points[23] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.1 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01       
        t "Yeah, it's disgusting... Let's move on, Bigdong Falls are not far away."
        jump BigDongFalls01
    "Burp":
        window hide
        play sound "Sounds/burp.mp3"
        $ renpy.pause(1.0, hard=True)
        scene lyrebird02 with dissolve
        ly "(burp)"
        window hide
        play sound "Sounds/burp.mp3"
        $ renpy.pause(1.0, hard=True)
        scene lyrebird01 with dissolve
        t "Really? That's the best you can do? You are so immature [name]..."
        vi "Ha ha, I thought that was quite funny actually... It's just a frigging bird Teagan..."
        $ lust_points[23] += 1
        $ score += 1
        show lust01:
            xalign 0.1 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01        
        t "Humpf... Let's move on, Bigdong Falls are not far away."
        jump BigDongFalls01
    "Wolf-whistle":
        window hide
        play sound "Sounds/wolfwhistle.mp3"
        $ renpy.pause(1.0, hard=True)
        scene lyrebird02 with dissolve
        ly "(whistle)"
        window hide
        play sound "Sounds/wolfwhistle.mp3"
        $ renpy.pause(1.0, hard=True)
        scene lyrebird01 with dissolve
        t "Did you hear that? He just repeated exactly the same sound that [name] made, isn't that amazing?"
        play sound "Sounds/katehihi.mp3"
        $ renpy.pause(1.0, hard=True)
        t "Let's move on, Bigdong Falls are not far away."
        jump BigDongFalls01
        
        
label BigDongFalls01:
$ hour += 1
scene bigdong01 with dissolve
play music "Sounds/waterfalls.mp3"
$ renpy.pause(1.0, hard=True)
t "There you are kids, the spectacular and famous Bigdong Falls!"
$ discoverfalls = True
show addedlocation:
    xalign 0.4 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide addedlocation
vi "Let's cool off by taking a dip in those crystal clear waters!"
k "But... What about the crocodiles?"
vi "There aren't any crocodiles on the island. The French killed them off centuries ago. I own some croc boots made by my great-great grandfather actually..."
p "(Gee, those French really like killing things... I'd better not piss Viviane off then...)"
t "I mentioned yesterday during class that the trip was totally safe."
t "Clearly, you weren't listening Kate, detention for you today!"
k "What... But I was only asking a question... Why are you doing this to me?"
label BigDongChoice:
scene bigdong02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Everyone seems to be enjoying themselves. Who should I approach?"
menu:
    "Talk to Laura, Kate and Quentin" if (spokenbigdongall == False):
        jump BigDongAll
    "Talk to Frieda" if (spokenbigdongfrieda == False):
        jump BigDongFrieda
    "Talk to Teagan and Maria" if (spokenbigdongteagan == False):
        jump BigDongTeagan
    "Talk to Viviane" if (spokenbigdongviviane == False):
        jump BigDongViviane
    "Talk to the French chick and whats-his-name" if (spokenbigdongnobody == False):
        jump BigDongNobody
    "I've done everything I could here" if (spokenbigdongall == True) and (spokenbigdongfrieda == True) and (spokenbigdongteagan == True) and (spokenbigdongviviane == True) and (spokenbigdongnobody == True):
        jump BigDongEnd
        
label BigDongNobody:
scene bigdongnobody with dissolve
$ spokenbigdongnobody = True
$ renpy.pause(1.0, hard=True)
no "Look!"
p "Look at what?"
no "Water. Falling."
p "Well, that was a complete waste of time..."
jump BigDongChoice
    
label BigDongAll:
scene bigdongall with dissolve
$ spokenbigdongall = True
$ renpy.pause(1.0, hard=True)
menu:
    "How about we play in the water, I'll carry Laura on my shoulders and Quentin can carry Kate!":
        k "Oh yeah, this is going to be ssoo much fun, hee hee!"
        play sound "Sounds/katehihi.mp3"
        la "Umpf, I'm not sure about that but I'll try cos I'm just ssoo bored..."
        jump BigDongWaterplay
    "How about we play in the water, I'll carry Kate on my shoulders and Quentin can carry Laura!":
        scene bigdongall02 with dissolve
        la "I'm not letting that boring nerd anywhere near me! Why did you suggest that?"
        if (lust_points[13] <= 9):
            $ lust_points[13] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.3 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
        p "Err, cos I thought it would be fun..."
        la "I HATE having fun!"
        k "What a party-pooper! Quentin, let's have fun in the water, it's so nice here!"
        q "Wow, yeah sure Kate!"
        p "(Well, Quentin and Kate will be having fun at least... Sigh)"
        jump BigDongChoice
    "What are you up to?":
        scene bigdongall02 with dissolve
        la "We're up to being bored by this hellish trip, that's what we're up to!"
        k "Speak for yourself, I want to look for seashells! Quentin, will you help me!"
        q "Seashells on a river, that sounds like an impossible challenge, but I'm in!"
        la "Don't even think about asking me to help you look for dumb seashells...."
        p "(Well, Quentin and Kate will be having fun at least... Sigh)"
        jump BigDongChoice

label BigDongWaterplay:
scene bigdongall03 with dissolve
play sound "Sounds/katehihi.mp3"
$ renpy.pause(1.0, hard=True)
k "Hee hee! Forward to combat Quentin!"
q "Yeah, I'm trying..."
la "Alright, you asked for it Kate!"
scene bigdongall04 with dissolve
play sound "Sounds/diving.mp3"
$ renpy.pause(1.0, hard=True)
la "We got them [name]! I hate to admit it but you had a great idea..."
if (lust_points[13] <= 8):
    $ lust_points[13] += 1
    $ score += 1
    show lust01:
        xalign 0.3 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
k "Oops, I fell in the water... This is so much fun, let's do it again!"
if (lust_points[11] <= 8):
    $ lust_points[11] += 1
    $ score += 1
    show lust01:
        xalign 0.7 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
q "Hold tight to my body this time Kate, we'll get them eventually!"
if (katefucked == True):
    p "(Everyone seems to be having a lot of fun, and Quentin is getting on with Kate...)"
if (katefucked == False):
    p "(Everyone seems to be having a lot of fun, but Quentin is getting real close to Kate, I should be careful...)"
$ hour +=1
p "How time flies when you're having fun!"
jump BigDongEnd

label BigDongFrieda:
scene bigdongfrieda01 with dissolve
$ spokenbigdongfrieda = True
$ renpy.pause(1.0, hard=True)
p "Hey Frieda, wanna play in the water with the rest of us?"
fr "I don't think so. I am still zo worried about Maddy..."
p "Oh, come on! She's not here, you're here, I 'm here, the water's h..."
fr "Achtung, shut up! You talk too much."
if (lust_points[8] <= 9):
    $ lust_points[8] -= 1
    $ score -= 1
    show lustminus01:
        xalign 0.3 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    p "Alright, alright, I'll leave you alone then... Sheesh..."
jump BigDongChoice


label BigDongTeagan:
scene bigdongteagan01 with dissolve
$ spokenbigdongteagan = True
$ renpy.pause(1.0, hard=True)
p "Why are the falls called \"Bigdong\"? I don't see any big dongs here. Well, except mine."
ma "Ah, err... Well, there's another waterpool where..."
t "I think he needs to see them. Then, he'll stop bragging all the time about his \"huge cock\"..."
t "Follow us big boy, but don't tell anyone we took you to the \"special place\"..."
p "(The \"special place\"? What is she on about I wonder?)"
ma "But there is a curse that befalls anyone who isn't naked who approaches that place..."
t "You believe in that legend?"
ma "I'm afraid it's not just a legend. It is well documented that people who failed to undress suddenly fell ill and died."
t "Right, well, we're all mature enough here, we'll go naked then. [name], don't you dare ogle our tits."
p "That would never have crossed my mind..."

scene bigdongteagan02 with dissolve
stop music
$ renpy.pause(1.0, hard=True)
p "(He he, I promised not to ogle their tits, but I never said anything about not ogling their fine arses...)"
t "There we are, look at the endownments on this statue, one of many in this gorge. Now you get why it's called \"Bigdong Falls\" [name]?"
scene bigdongteagan03 with dissolve
$ renpy.pause(1.0, hard=True)
ma "The natives lived in matriarchal tribes where boys were selected at a young age for breeding based on their physical attributes..."
ma "It is believed that this system led to extraordinarily well-endowed muscle boys to be born and worshipped by the tribe women..."
t "It's such a shame that the French ended up killing all those natives... (sigh)."
p "Well, they would have worshipped me for sure... What about the female statue? She has huge knockers..."
ma "Ah, yes... They were also \"breeders\" and selected for their physical attributes... And then mated with the horse-hung boys."
t "The ones who truly were equipped with a massive penis, not the ones who just bragged about it..."
menu:
    "Looks like you ladies could have been breeders in that tribe.":
        t "And why is that?"
        p "Cos, err... You have massive racks."
        scene bigdongteagan04 with dissolve
        $ renpy.pause(1.0, hard=True)
        t "I see, so you HAVE been ogling our breasts then! That's it, this guided tour is over for me, I'm leaving!"
        $ lust_points[22] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.8 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump BigdongMaria01
    "Get a hardon and show them your mighty cock":
        scene bigdongteagan05 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Look at me, I'm posing just like that statue!"
        t "What the hell are you doing [name]?"
        p "Proving to you that I would have fitted right into that tribe!"
        ma "Wow, what a HUGE cock! My ex-husband was so tiny compared to that monster..."
        $ lust_points[15] +=2
        $ score += 2
        show lust02:
            xalign 0.15 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
        t "Yeah, OK, you have a huge cock, I said it, are you happy now?"
        $ lust_points[22] +=1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        menu:
            "You can do better than that teach...":
                t "And what do you expect me to say about your...thing?"
                p "Pretend you're a tribeswoman and worship it."
                t "Why would I want to do such a thing?"
                p "Cos your knockers are really awesome, so you could definitely have been in their breeding program..."
                t "Awesome? That's the word you use to describe them? That's pretty lame worshipping boy... I'll show you what proper worshipping sounds like..."
                ma "Oh, I'm in too!"
                jump BigDongTeagan04
            "Yeah, I'm da man, I'm DA MAN!":
                t "...who talks like a mentally-retarded boy... This guided tour is over for me, you simply can't take anything seriously [name]..."
                window hide 
                $ lust_points[22] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.7 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
                jump BigdongMaria01

label BigDongTeagan04:
scene bigdongdouble01 with dissolve
$ teagantoucheddick = True
$ renpy.pause(1.0, hard=True)
t "Now, with my sumptuous, heavy breasts right in your face, do you have any better words that come to mind [name]?"
if (lust_points[22] == 9):
    window hide 
    $ lust_points[22] +=1
    $ score += 1
    show lust01:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[22] <= 8):
    window hide 
    $ lust_points[22] +=2
    $ score += 2
    show lust02:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
if (lust_points[22] >= 10):
    window hide
    show epiclust:
        xalign 0.6 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
p "mm..hummmuuummmm..."
t "Say again?"
ma "What about if I worship your giant, thick, veiny, beautiful, godlike cock, stud?"
if (lust_points[15] <= 9):
    window hide 
    $ lust_points[15] +=1
    $ score += 1
    show lust01:
        xalign 0.2 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[15] >= 10):
    window hide
    show epiclust:
        xalign 0.2 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
jump MariaTeaganDay04

label BigdongMaria01:
scene mariabigdong01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "So you are a  breast man [name] it seems?"
menu:
    "Err, yes, on top of enjoying the superior intellect of women that is.":
        ma "Stop pretending [name], it's so obvious it's pathetic really."
        window hide 
        $ lust_points[15] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        ma "Since you can't be trusted, I'm going back to the main waterfalls too. You might want to take care of that monstrous hardon before heading back...(wink)."
        p "(Shit, I totally screwed up with both of them. Women are so complicated these days...)"
        jump BigDongChoice
    "Yeah, and an ass man too. A titass-man is what I am.":
        scene mariabigdong02 with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "And what do you think about MY tits and MY arse?"
        p "Statues should be devoted to their perfection!"
        if (lust_points[15] <= 9):
            window hide 
            $ lust_points[15] +=1
            $ score += 1
            show lust01:
                xalign 0.4 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01
        if (lust_points[15] >= 10):
            window hide
            show epiclust:
                xalign 0.4 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust
            ma "Such a charmer! Let's do someting naughty while the others are busy..."
            jump MariaFuckDay04
        ma "Such a charmer! But I think you've seen enough... for the day. Let's put our clothes back on and go back with the others."
        p "(Shit, her lust just wasn't high enough to get me some poontang this morning... (sigh))"
        jump BigDongChoice

label MariaTeaganDay04:
if (lust_points[15] >= 10) and (lust_points[22] >= 10):
    window hide
    show doubledelight:
        xalign 0.4 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/delight.mp3"
    $ renpy.pause(4.0, hard=True)
    hide doubledelight
    ma "Let's move to a shallower part of the gorge, I want to be able to admire your pole AND your nuts!"
    t "Good idea... I want to see everything too..."
    p "(Jackpot! I'm gonna get me some double-poontang!)"
    jump MariaTeaganFuckDay04
if (lust_points[15] <= 9) and (lust_points[22] >= 10):
    ma "Well, I had my fun, but I'm gonna leave you two and go back with the rest of the group. Don't stay here too long! (wink)"
    t "Well, err.. I think I'll stay a while longer... I have so many more things to teach [name] about these gorges..."
    ma "(chuckle). Don't do anything I wouldn't do! (wink)"
    t "Let's move to a shallower part of the gorge, I want to be able to admire your pole AND your nuts!"
    jump TeaganFuckDay04
if (lust_points[15] >= 10) and (lust_points[22] <= 9):
    t "Well, I had my fun, but I'm gonna leave you two and go back with the rest of the group. Don't stay here too long! (wink)"
    ma "Well, err.. I think I'll stay a while longer... I have so many more things to teach [name] about these gorges..."
    t "(chuckle). Don't do anything I wouldn't do! (wink)"
    ma "Let's move to a shallower part of the gorge, I want to be able to admire your pole AND your nuts!"
    jump MariaFuckDay04
if (lust_points[15] <= 9) and (lust_points[22] <= 9):
    ma "I think we teased you enough... [name], you might want to take care of that monstrous hardon before heading back...(wink)" 
    p "What? You're BOTH leaving me like that! AAARGH!"
    jump BigDongChoice

label MariaTeaganFuckDay04:
    scene bothprefuck with dissolve
    $ renpy.pause(1.0, hard=True)
    t "I can tell my huge tits are really getting your huge cock hard [name]..."
    ma "So, what would you like us to do to get that massive love pole down before anyone sees us?"
    jump BothFuckChoiceDay04
label TeaganFuckDay04:
    scene teaganprefuck with dissolve
    $ renpy.pause(1.0, hard=True)
    t "Now that my sumptuous breasts have gotten you rock-hard, what do you want to do [name]?"
    jump TeaganFuckChoiceDay04
label MariaFuckDay04:
    scene mariaprefuck with dissolve
    $ renpy.pause(1.0, hard=True)
    ma "So, what would you like me to do to get that massive love pole down before anyone sees us?"
    jump MariaFuckChoiceDay04

label BothFuckChoiceDay04:
menu:
    "Come and worship my muscles ladies!":
        jump BothMuscles01
    "Why don't you play with each other for a while...":
        jump BothPlay01
    "I'd like to titfuck your giant tits as a good sloppy workout teach!" if (teagantits == False):
        jump BothTeaganTitFuck01
    "I'm thirsty... for some milk! Let me suck on your huge nipples Maria!" if (mariamilk == False):
        jump BothMariaMilk01
    "Let me fuck your tender pussy Maria while teach sucks on my heavy nuts!" if (mariapussy == False):
        jump BothMariaFuck01
    "Get ready for a heavy pounding Teagan while Maria jacks my crank!" if (teaganpussy == False):
        jump BothTeaganFuck01
    "Open your mouth and get ready to receive my load both of you!" if (teaganpussy == True) and (mariapussy == True) and (mariamilk == True) and (teagantits == True):
        jump BothTeaganBlow

label BothMuscles01:
scene bothworship01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Mmh, your biceps are so big [name]... They must be at least 20 inches around fully flexed..."
scene bothworship02 with dissolve
$ renpy.pause(1.0, hard=True)
t "Which is about the size of that monstrous rod... I'm sorry I didn't believe a boy your age could be such a super-stud..."
jump BothFuckChoiceDay04

label BothMariaFuck01:
$ mariapussy = True
scene mariaplay01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Come and unload those huge Grapes of Wraths down my rabid hole!"
scene mariaprefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
p "First, let me prime that pussy with my heavy pile-driver...."
ma "OOh, what are you going to do?"
scene mariaprefuck02 with dissolve
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
p "Just toying with you a bit, letting you know how much meat you're about to take..."
scene mariaprefuck01
$ renpy.pause(0.5, hard=True)
scene mariaprefuck02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
ma "That filthy slapping noise... It's making me so wet!"
scene mariaprefuck01
$ renpy.pause(0.5, hard=True)
scene mariaprefuck02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene mariaprefuck01
$ renpy.pause(0.5, hard=True)
scene mariaprefuck02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
p "I think you're ready now. Teach, get between my nuts and lick my balls!"
scene mariafuckboth01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Mmh, they're so tasty and smell so MANLY!"
p "That's cos they're filled with ounces of virile teenage cum! Now keep up while I ram my pole up Maria's sweet pussy!"
scene mariafuckboth02 with dissolve
$ renpy.pause(1.0, hard=True)
ma "It's sssoo DEEP! AAAH!"
label BothMariaFuck01b:
    play sound "Sounds/bothmariafuck01.mp3"
    scene mariafuckboth01
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth02
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth01
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth02
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth01
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth02
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth01
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth02
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth01
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth02
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth01
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth02
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth01
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth02
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth01
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth02
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth01
    $ renpy.pause(0.5, hard=True)
    scene mariafuckboth02
    $ renpy.pause(0.5, hard=True)
    menu:
        "Repeat":
            jump BothMariaFuck01b
        "Move on":
            ma "You made me cum ssooo much..."
            p "Let's switch position and I'll make you cum even more..."
            jump BothMariaFuck02

label BothMariaFuck02:
scene mariafuck03 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Please be gentle with that monstrous thing, you're at least five times longer and thicker than my ex-husband..."
p "What a pindick, time for you to feel a REAL man. Me, DA MAN!"
scene mariafuck04 with dissolve
$ renpy.pause(1.0, hard=True)
ma "You're stabbing me in the womb with your giant love muscle!"
t "Fuck her harder! I want to see her pussy creaming over that fat shaft!"
label BothMariaFuck02b:
play sound "Sounds/bothmariafuck02.mp3"
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        jump BothMariaFuck02b
    "Move on":
        ma "Too... Too much..."
        jump BothFuckChoiceDay04

label BothTeaganTitFuck01:
$ teagantits = True
scene teagantitfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Incredible, your cock is so big, I can see the head poking through my massive cleavage! That's never happened before!"
p "Wait till I pummel your titflesh and it will stick far enough for you to suck on it too!"
play sound "Sounds/teagantitfuck01.mp3"
$ renpy.pause(5.0, hard=True)
ma "Oh my God, he wasn't kidding! And I can still see several inches left below your huge rack Teagan!"
t "Yes, fuck my tits and my mouth you horse-hung stud!"
p "Ah? So you acknowledge that I wasn't bragging? That's good teach, you're learning!"
p "Now learn to worship my monster cock with your lips!"
label BothTeaganTitFuck01b:
play sound "Sounds/teagantitfuck02.mp3"
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        jump BothTeaganTitFuck01b
    "Move on":
        scene teagantitfuck03 with dissolve
        play sound "Sounds/teagantitfuck03.mp3"
        $ renpy.pause(4.0, hard=True)
        t "Damn, I'm all sticky with your abundant precum [name]!"
        jump BothFuckChoiceDay04

label BothMariaMilk01:
$ mariamilk = True
scene mariasuck01 with dissolve
play sound "Sounds/sucking.mp3"
$ renpy.pause(1.0, hard=True)
ma "You're in luck, Lolly was such a hungry kid that I am still lactating..."
p "Nothing like drinking directly from the source!"
scene mariasuck02 with dissolve
play sound "Sounds/sucking02.mp3"
$ renpy.pause(3.0, hard=True)
t "Mmh, that's so hot... Go on [name], maul those milkbags and suck them dry!"
ma "Ooooh, I'm feeling so strange feeding you... But I love it, keep suckling!"
label BothMariaMilk01b:
scene mariasuck01
play sound "Sounds/sucking02.mp3"
$ renpy.pause(1.0, hard=True)
scene mariasuck02
$ renpy.pause(1.0, hard=True)
scene mariasuck01
$ renpy.pause(1.0, hard=True)
scene mariasuck02
play sound "Sounds/sucking02.mp3"
$ renpy.pause(1.0, hard=True)
scene mariasuck01
$ renpy.pause(1.0, hard=True)
scene mariasuck02
$ renpy.pause(1.0, hard=True)
menu:
    "Repeat":
        jump BothMariaMilk01b
    "Move on":
        ma "I don't think I have any milk left... You sucked me dry, you were more hungry than my daughter Lolly ever was!"
        jump BothFuckChoiceDay04

label BothTeaganFuck01:
$ teaganpussy = True
scene teaganslap01 with dissolve
$ renpy.pause(1.0, hard=True)
p "But first, let me teach you to respect me..."
t "Ooh, what are you going to do?"
scene teaganslap02 with dissolve
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Just slapping your slutty face, letting you know who's in charge here..."
t "I'll let you do that for NOW. But I'm your teacher, I can't let a student take control over me..."
scene teaganslap02 with dissolve
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01 with dissolve
$ renpy.pause(1.0, hard=True)
p "We'll see about that..."
t "Slap me some more [name], while I'm so horny that you have a chance to get away with it..."
ma "God, Teagan, I didn't know you were such a slut...You two are making me ssoo horny..."
label BothTeaganFuck01b:
scene teaganslap02 with dissolve
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01
$ renpy.pause(0.5, hard=True)
scene teaganslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01
$ renpy.pause(0.5, hard=True)
scene teaganslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01
$ renpy.pause(0.5, hard=True)
scene teaganslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        jump BothTeaganFuck01b
    "Move on":
        t "I am ready to receive that great big monster cock [name]!"
        jump BothTeaganFuck02
        
label BothTeaganFuck02:
p "Maria, get a hold of my shaft while I ram it inside Teagan and claim her pussy as mine!"
scene teaganfuck01b with dissolve
$ renpy.pause(1.0, hard=True)
t "What? No, my pussy is my property!"
p "You sure about that?"
scene teaganfuck02b with dissolve
$ renpy.pause(1.0, hard=True)
t "AAH, FUCK, it's sssoo DEEP! AAAH!"
ma "Sounds like your pussy is [name]'s property after all..."
label BothTeaganFuck02b:
    play sound "Sounds/bothteaganfuck01.mp3"
    scene teaganfuck01b with dissolve
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02b with dissolve
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01b with dissolve
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02b with dissolve
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01b
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02b
    $ renpy.pause(0.5, hard=True)
    menu:
        "Repeat":
            jump BothTeaganFuck02b
        "Move on":
            t "My pussy has turned into a mush from so many orgasms..."
            ma "I can see that, my hand is caked in your cream Teagan... I bet it's real tasty too, especially mixed with [name]'s copious precum!"
            jump BothFuckChoiceDay04

label BothPlay01:
scene bothplay01 with dissolve
play sound "Sounds/bothplay01.mp3"
$ renpy.pause(3.0, hard=True)
ma "Your boobs feel so soft and warm Teagan..."
t "I can't believe I'm playing with your enormous funbags Maria, we should have done this earlier..."
p "Then why don't you get on your knees and lick her pussy teach? That would be hot and would get my crank even bigger...."
t "Mmh, in that case... I'm in!"
scene bothplay02 with dissolve
$ renpy.pause(1.0, hard=True)
t "It's so tasty, your pussy juices are delicious!"
ma "Ooh, Teagan, what are you doing to me? I'm... I'm gonna cum... AAAHH!"
scene bothplay03 with dissolve
play sound "Sounds/bothplay02.mp3"
$ renpy.pause(0.5, hard=True)
scene bothplay03b
$ renpy.pause(0.5, hard=True)
scene bothplay03
$ renpy.pause(0.5, hard=True)
scene bothplay03b
$ renpy.pause(0.5, hard=True)
scene bothplay03
$ renpy.pause(0.5, hard=True)
scene bothplay03b
$ renpy.pause(0.5, hard=True)
scene bothplay03
$ renpy.pause(0.5, hard=True)
scene bothplay03b
$ renpy.pause(0.5, hard=True)
scene bothplay03
$ renpy.pause(0.5, hard=True)
scene bothplay03b
$ renpy.pause(0.5, hard=True)
scene bothplay03
$ renpy.pause(0.5, hard=True)
p "Alright! I got two MILFs to go at each other! Now let's do something that involves my mega-dong..."
jump BothFuckChoiceDay04

label BothTeaganBlow:
scene teaganslap01 with dissolve
$ renpy.pause(1.0, hard=True)
p "You start first teach, open that mouth wide..."
stop music
play music "Sounds/teaganslow.mp3"
show teaganslow
show faster
call screen bothteaganslow
screen bothteaganslow:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("BothTeaganFast")
label BothTeaganFast:
hide faster
play music "Sounds/teaganfast.mp3"
show teaganfast
show next
call screen bothteaganfast
screen bothteaganfast:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("BothMariaBlow")

label BothMariaBlow:
hide teaganslow
hide teaganfast
stop music
hide next
scene mariablow01
$ renpy.pause(1.0, hard=True)
p "And now your turn Maria, suck me good, just like Teagan did!"
ma "I'll try my best [name].... But your cock is SO BIG!"
stop music
play music "Sounds/hardsucking.mp3"
show mariablowslow
show faster
call screen bothmariablowslow
screen bothmariablowslow:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("BothMariaBlowFast")
label BothMariaBlowFast:
hide faster
play music "Sounds/hardsucking.mp3"
show mariablowfast
show cum
call screen bothmariablowfast
screen bothmariablowfast:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("BothFuckCum")

label BothFuckCum:
hide mariablowfast
hide mariablowslow
stop music
scene bothcum01
$ renpy.pause(1.0, hard=True)
p "Gather round both of you, I'm about to cum!"
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
ma "There's so much cum shooting out of your great big teenage monster cock!"
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
t "Gimme, gimme, gimme, I want some too!"
scene bothcum02
play sound "Sounds/cumming.mp3"
$ renpy.pause(3.0, hard=True)
p "SHIT, I'm hosing at full charge, RHAAA! There's plenty to go round and cover both your hot busty bodies! AAAHH!"
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
scene bothcum03
$ renpy.pause(3.0, hard=True)
t "Damn, [name], you came like a true stallion. We are covered from head to toes in your warm cream.... Mmmh!"
ma "Yeah, suck it up Teagan, and feed me some too please! It's so tasty and there's so much of it!"
play sound "Sounds/bothplay01.mp3"
$ renpy.pause(3.0, hard=True)
t "Let's get back to the others, it's getting late..."
ma "And they might wonder why we took so long..."
$ mariafucked = True
$ teaganfucked = True
$ threesome += 1
$ hour += 1
if (mariajosewin == False):
    p "(Maria didn't notice I took a picture of her with her face plastered in my cum... Now I'll send it to José)."
    $ mariawin = True
if (teaganjosewin == False):
    p "(Teagan didn't notice I took a picture of her with her face plastered in my cum... Now I'll send it to José)."
    $ teaganwin = True    
jump BigDongEnd

label MariaFuckChoiceDay04:
menu:
    "Come and worship my muscles Maria!":
        jump MariaMuscles01
    "I'm thirsty... for some milk! Let me suck on your huge nipples Maria!" if (mariamilk == False):
        jump MariaMilk01
    "Let me fuck your tender pussy Maria!" if (mariapussy == False):
        jump MariaPussyFuck01
    "Open your mouth and get ready to receive my load Maria!" if (mariapussy == True) and (mariamilk == True):
        jump MariaBlow01

label MariaMuscles01:
scene mariaworship with dissolve
$ renpy.pause(1.0, hard=True)
ma "Mmh, your biceps are so big [name]... They must be at least 20 inches around fully flexed..."
p "Way more after a heavy workout!"
ma "Mmh, so powerful... Time to show me what you can do with those muscles... Especially the one sticking straight up from your groin..."
jump MariaFuckChoiceDay04

label MariaPussyFuck01:
$ mariapussy = True
scene mariaplay01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Come and unload those huge Grapes of Wraths down my rabid hole!"
scene mariaprefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
p "First, let me prime that pussy with my heavy pile-driver...."
ma "OOh, what are you going to do?"
scene mariaprefuck02 with dissolve
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
p "Just toying with you a bit, letting you know how much meat you're about to take..."
scene mariaprefuck01
$ renpy.pause(0.5, hard=True)
scene mariaprefuck02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
ma "That filthy slapping noise... It's making me so wet!"
scene mariaprefuck01
$ renpy.pause(0.5, hard=True)
scene mariaprefuck02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
scene mariaprefuck01
$ renpy.pause(0.5, hard=True)
scene mariaprefuck02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(0.5, hard=True)
p "I think you're ready now."
scene mariafuck01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "It's sssoo DEEP! AAAH!"
p "And it can get deeper still!"
scene mariafuck02 with dissolve
$ renpy.pause(1.0, hard=True)
label MariaPussyFuck01b:
play sound "Sounds/mariafuck01.mp3"
scene mariafuck01 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck02 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck01 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck02 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck01 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck02 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck01
$ renpy.pause(0.5, hard=True)
scene mariafuck02
$ renpy.pause(0.5, hard=True)
scene mariafuck01
$ renpy.pause(0.5, hard=True)
scene mariafuck02
$ renpy.pause(0.5, hard=True)
scene mariafuck01
$ renpy.pause(0.5, hard=True)
scene mariafuck02
$ renpy.pause(0.5, hard=True)
scene mariafuck01
$ renpy.pause(0.5, hard=True)
scene mariafuck02
$ renpy.pause(0.5, hard=True)
scene mariafuck01
$ renpy.pause(0.5, hard=True)
scene mariafuck02
$ renpy.pause(0.5, hard=True)
scene mariafuck01
$ renpy.pause(0.5, hard=True)
scene mariafuck02
$ renpy.pause(0.5, hard=True)
scene mariafuck01
$ renpy.pause(0.5, hard=True)
scene mariafuck02
$ renpy.pause(0.5, hard=True)
scene mariafuck01
$ renpy.pause(0.5, hard=True)
scene mariafuck02
$ renpy.pause(0.5, hard=True)
scene mariafuck01
$ renpy.pause(0.5, hard=True)
scene mariafuck02
$ renpy.pause(0.5, hard=True)
scene mariafuck01
$ renpy.pause(0.5, hard=True)
scene mariafuck02
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        jump MariaPussyFuck01b
    "Move on":
        ma "You made me cum ssooo much..."
        p "Let's switch position and I'll make you cum even more..."
        jump MariaPussyFuck02

label MariaPussyFuck02:
scene mariafuck03 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Please be gentle with that monstrous thing, you're at least five times longer and thicker than my ex-husband..."
p "What a pindick, time for you to feel a REAL man. Me, DA MAN!"
scene mariafuck04 with dissolve
$ renpy.pause(1.0, hard=True)
ma "You're stabbing me in the womb with your giant love muscle!"
ma "Fuck me harder! I want to feel my pussy creaming over that fat shaft!"
label MariaPussyFuck02b:
play sound "Sounds/mariafuck02.mp3"
scene mariafuck03 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck04 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck03 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck04 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck03 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck04 with dissolve
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
scene mariafuck03
$ renpy.pause(0.5, hard=True)
scene mariafuck04
$ renpy.pause(0.5, hard=True)
stop sound
menu:
    "Repeat":
        jump MariaPussyFuck02b
    "Move on":
        ma "Too... Too much..."
        jump MariaFuckChoiceDay04
        
label MariaMilk01:
$ mariamilk = True
scene mariasuck01 with dissolve
play sound "Sounds/sucking.mp3"
$ renpy.pause(1.0, hard=True)
ma "You're in luck, Lolly was such a hungry kid that I am still lactating..."
p "Nothing like drinking directly from the source!"
scene mariasuck02 with dissolve
play sound "Sounds/sucking02.mp3"
$ renpy.pause(3.0, hard=True)
ma "Ooooh, I'm feeling so strange feeding you... But I love it, keep suckling!"
label MariaMilk01b:
scene mariasuck01
play sound "Sounds/sucking02.mp3"
$ renpy.pause(1.0, hard=True)
scene mariasuck02
$ renpy.pause(1.0, hard=True)
scene mariasuck01
$ renpy.pause(1.0, hard=True)
scene mariasuck02
play sound "Sounds/sucking02.mp3"
$ renpy.pause(1.0, hard=True)
scene mariasuck01
$ renpy.pause(1.0, hard=True)
scene mariasuck02
$ renpy.pause(1.0, hard=True)
menu:
    "Repeat":
        jump MariaMilk01b
    "Move on":
        ma "I don't think I have any milk left... You sucked me dry, you were more hungry than my daughter Lolly ever was!"
        jump MariaFuckChoiceDay04
        
label MariaBlow01:
scene mariablow01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Suck me good Maria, and you'll get a nice creamy reward!"
ma "I'll try my best [name].... But your cock is SO BIG!"
stop music
scene
play music "Sounds/hardsucking.mp3"
play movie "Day4/mariablowslow.ogv" loop
show movie
show faster
call screen mariablowslow
screen mariablowslow:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MariaBlowFast")
label MariaBlowFast:
hide faster
play music "Sounds/hardsucking.mp3"
play movie "Day4/mariablowfast.ogv" loop
show cum
call screen mariablowfast
screen mariablowfast:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MariaFuckCum")

label MariaFuckCum:
stop movie
stop music
scene mariacum01
$ renpy.pause(1.0, hard=True)
p "Get ready to receive my cum Maria!"
window hide
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
ma "There's so much cum shooting out of your great big teenage monster cock!"
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
scene mariacum02
window hide
play sound "Sounds/cumming.mp3"
$ renpy.pause(3.0, hard=True)
p "SHIT, I'm hosing at full charge, RHAAA! There's plenty to go round and cover your hot busty body! AAAHH!"
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
ma "Thank you for giving me SO MUCH cream [name] It's delicious... My ex-husband could never come like that..."
ma "Let's get back to the others, it's getting late, and they might wonder why we took so long..."
$ mariafucked = True
$ hour += 1
if (mariajosewin == False):
    p "(She didn't notice I took a picture of us... Now I'll send it to José)."
    $ mariawin = True
jump BigDongEnd


label TeaganFuckChoiceDay04:
menu:
    "Come and worship my muscles Teagan!":
        jump TeaganMuscles01
    "I'd like to titfuck your giant tits as a good sloppy workout teach!" if (teagantits == False):
        jump TeaganTitFuck01
    "Lick my balls and make them shiny with your spit!":
        jump TeaganLick01
    "Get ready for a heavy pounding teach!" if (teaganpussy == False):
        jump TeaganPussyFuck01
    "Open your mouth and get ready to receive my load teach!" if (teaganpussy == True) and (teagantits == True):
        jump TeaganBlow01
        
label TeaganMuscles01:
scene teaganworship with dissolve
$ renpy.pause(1.0, hard=True)
t "Wow, you're so muscular [name]... ALL OVER. I'm sorry I didn't believe a boy your age could be such a super-stud..."
p "Now you'll stop accusing me of bragging Teagan. Fuck yeah, I'm da man, I'm DA MAN!"
t "Mmmh, well show me what you can do with it then mister DA MAN!"
jump TeaganFuckChoiceDay04
    
label TeaganTitFuck01:
$ teagantits = True
scene teagantitfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Incredible, your cock is so big, I can see the head poking through my massive cleavage! That's never happened before!"
p "Wait till I pummel your titflesh and it will stick far enough for you to suck on it too!"
play sound "Sounds/teagantitfuck01.mp3"
$ renpy.pause(5.0, hard=True)
t "Yes, fuck my tits and my mouth you horse-hung stud!"
p "Ah? So you acknowledge that I wasn't bragging? That's good teach, you're learning!"
p "Now learn to worship my monster cock with your lips!"
label TeaganTitFuck01b:
play sound "Sounds/teagantitfuck02.mp3"
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
scene teagantitfuck01
$ renpy.pause(0.5, hard=True)
scene teagantitfuck02
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        jump TeaganTitFuck01b
    "Move on":
        scene teagantitfuck03 with dissolve
        play sound "Sounds/teagantitfuck03.mp3"
        $ renpy.pause(4.0, hard=True)
        t "Damn, I'm all sticky with your abundant precum [name]!"
        jump TeaganFuckChoiceDay04

label TeaganLick01:
scene teaganlick01 with dissolve
play sound "Sounds/teaganlick01.mp3"
$ renpy.pause(4.0, hard=True)
p "Yeah, that's it, roll your tongue all over my massive seedmakers teach!"
t "They are each ssoo big, I can't even fit one in my mouth!"
scene teaganlick02 with dissolve
$ renpy.pause(1.0, hard=True)
p "You're doing good, AAHH!"
label TeaganLick01b:
play sound "Sounds/teaganlick02.mp3"
scene teaganlick01 with dissolve
$ renpy.pause(0.5, hard=True)
scene teaganlick02 with dissolve
$ renpy.pause(0.5, hard=True)
scene teaganlick01 with dissolve
$ renpy.pause(0.5, hard=True)
scene teaganlick02 with dissolve
$ renpy.pause(0.5, hard=True)
scene teaganlick01 with dissolve
$ renpy.pause(0.5, hard=True)
scene teaganlick02 with dissolve
$ renpy.pause(0.5, hard=True)
scene teaganlick01 with dissolve
$ renpy.pause(0.5, hard=True)
scene teaganlick02 with dissolve
$ renpy.pause(0.5, hard=True)
scene teaganlick01 with dissolve
$ renpy.pause(0.5, hard=True)
scene teaganlick02 with dissolve
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        jump TeaganLick01b
    "Move on":
        t "I hope I serviced your balls well [name]! And that you'll give me a nice big fat juicy load in exchange..."
        p "Don't worry about that! I have an endless supply of teenage spunk in there!"
        jump TeaganFuckChoiceDay04

label TeaganPussyFuck01:
$ teaganpussy = True
scene teaganslap01 with dissolve
$ renpy.pause(1.0, hard=True)
p "But first, let me teach you to respect me..."
t "Ooh, what are you going to do?"
scene teaganslap02 with dissolve
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Just slapping your slutty face, letting you know who's in charge here..."
t "I'll let you do that for NOW. But I'm your teacher, I can't let a student take control over me..."
scene teaganslap02 with dissolve
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01 with dissolve
$ renpy.pause(1.0, hard=True)
p "We'll see about that..."
t "Slap me some more [name], while I'm so horny that you have a chance to get away with it..."
label TeaganPussyFuck01b:
scene teaganslap02 with dissolve
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01
$ renpy.pause(0.5, hard=True)
scene teaganslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01
$ renpy.pause(0.5, hard=True)
scene teaganslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01
$ renpy.pause(0.5, hard=True)
scene teaganslap02
play sound "Sounds/cockslap.mp3"
$ renpy.pause(1.0, hard=True)
scene teaganslap01
$ renpy.pause(0.5, hard=True)
menu:
    "Repeat":
        jump TeaganPussyFuck01b
    "Move on":
        t "I am ready to receive that great big monster cock [name]!"
        jump TeaganPussyFuck02

label TeaganPussyFuck02:
scene teaganfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
t "What? No, my pussy is my property!"
p "You sure about that?"
scene teaganfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
t "AAH, FUCK, it's sssoo DEEP! AAAH!"
ma "Sounds like your pussy is [name]'s property after all..."
label TeaganPussyFuck02b:
    play sound "Sounds/teaganfuck01.mp3"
    scene teaganfuck01
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck01
    $ renpy.pause(0.5, hard=True)
    scene teaganfuck02
    $ renpy.pause(0.5, hard=True)
    menu:
        "Repeat":
            jump TeaganPussyFuck02b
        "Move on":
            t "My pussy has turned into a mush from so many orgasms..."
            jump TeaganFuckChoiceDay04
            
label TeaganBlow01:
scene teaganslap01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Time to get your creamy reward teach, open that mouth wide..."
stop music
play music "Sounds/teaganslow.mp3"
show teaganslow
show faster
call screen teaganblowslow
screen teaganblowslow:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("TeaganBlowFast")
label TeaganBlowFast:
hide faster
play music "Sounds/teaganfast.mp3"
show teaganfast
show cum
call screen teaganblowfast
screen teaganblowfast:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TeaganFuckCum")

label TeaganFuckCum:
hide teaganfast
hide teaganslow
stop music
scene teagancum01
$ renpy.pause(1.0, hard=True)
p "Hold still teach, I'm about to cum!"
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
t "There's so much cum shooting out of your great big teenage monster cock!"
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
scene teagancum02
play sound "Sounds/cumming.mp3"
$ renpy.pause(3.0, hard=True)
p "SHIT, I'm hosing at full charge, RHAAA! There's plenty to go round and cover both your hot busty body! AAAHH!"
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
t "Damn, [name], you came like a true stallion. I'm covered from head to toes in your warm cream.... Mmmh!"
t "Let's get back to the others, it's getting late..."
$ teaganfucked = True
$ threesome += 1
$ hour += 1
if (teaganjosewin == False):
    p "(She didn't notice I took a picture of her with her face plastered in my cum... Now I'll send it to José)."
    $ teaganwin = True    
jump BigDongEnd

label BigDongViviane:
scene bigdongviviane01 with dissolve
$ spokenbigdongviviane = True
$ renpy.pause(1.0, hard=True)
vi "You should be practicing your swimming here, I need you to be ready for the competition!"
p "Well, Maddy isn't here so I can't train with her and she's my swimming partner remember?"
vi "Ah yes, that's true. Well, I wouldn't mind swimming with you a bit then... If that can get you stronger for Sunday."
menu:
    "I don't need to practice, I'm already a very good swimmer.":
        vi "Even the best swimmers need to practice to keep up. I'm not letting you off the hook that easily [name]!"
        $ lust_points[23] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.6 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        vi "So swim with me, I'll be your partner!"
        p "(Jeezus, this trip was supposed to be fun...)"
        jump VivianeSwimDay04
    "I was rather thinking about exploring the area, this is an academic outing after all...":
        vi "Umpf... So why did you bother coming to speak to me then?"
        p "Err... I was just being polite..."
        vi "You'd better be ready on Sunday and beat those scumbags I'm warning you!"
        jump BigDongChoice
    "Alright, I wouldn't mind training with you either...":
        vi "Great, that's the spirit! To beat those scumbags from Sainte-Nitouche..."
        $ lust_points[23] +=1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        p "Err... yeah, sure. So where do we swim?"
        vi "Up and down the gorge, follow me!"

label VivianeSwimDay04:
scene bigdongviviane03 with dissolve
play sound "Sounds/swimming.mp3"
$ renpy.pause(1.0, hard=True)
vi "Faster, faster, you're slacking off!"
p "Puff, puff, the currents are really strong in this gorge!"
vi "Ok, we'll do another exercise then..."
stop sound
vi "I'll hold your body so you don't move, I want to have a closer look at how you move your arms."
scene bigdongviviane04 with dissolve
play music "Sounds/swimming.mp3"
$ renpy.pause(1.0, hard=True)
menu:
    "Do the exercise correctly":
        jump VivianeSwim02Day04
    "\"Inadvertently\" swing your arms and unsnap her top":
        jump VivianeSwim03Day04

label VivianeSwim02Day04:
vi "There, you're doing good, large arm movements, that's it, get as much traction as possible from the water!"
p "(Yeah, thanks, I know how to swim...)"
stop music
scene bigdongviviane01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Well, that was a good exercise wasn't it? I'm really proud of you, we'll beat those scumbags on Sunday!"
$ lust_points[23] +=2
$ score += 2
show lust02:
    xalign 0.6 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
$ hour += 1
p "(What, we've been doing this shit for ONE HOUR???)"
jump BigDongEnd

label VivianeSwim03Day04:
scene bigdongviviane05 with dissolve
play sound "Sounds/snap.mp3"
$ renpy.pause(1.0, hard=True)
stop music
vi "Hey! Did you do that on purpose?"
p "What? No, I swear! I'll get your bikini top teach, don't worry!"
vi "Don't bother, I'll get it myself..."
scene bigdongviviane06 with dissolve
$ renpy.pause(1.0, hard=True)
p "(I'm getting a nice view from here... He he...)"
vi "Now back to the exercise..."
jump VivianeSwim02Day04

label BigDongEnd:
stop movie
stop music
scene bigdongend with dissolve
$ renpy.pause(1.0, hard=True)
t "We'd better head back to the bus, it's already 11am."
t "Get your gear ready and remember to stay close to one of us. A different person from last time."
menu:
    "Stay close to the teacher (Teagan)" if (teagantrail == False):
        jump TeaganReturn
    "Stay close to the sports instructor (Viviane)" if (vivianetrail == False):
        jump VivianeReturn
    "Stay close to the librarian (Maria)" if (mariatrail == False):
        jump MariaReturn

label TeaganReturn:
scene trailteagan01 with dissolve
$ renpy.pause(1.0, hard=True)
t "I see you've chosen to be with us [name]..."
menu:
    "My thirst for knowledge is insatiable and you are the best teacher.":
        t "Why don't I believe you?"
        p "Err..."
        k "What a nerd..."
        if (katefucked == False):
            $ lust_points[11] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.3 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01        
        jump TeaganReturn02   
    "In case we are attacked by savages, the center is the safest place.":
        t "There are no savages on this island. They were all slaughtered by the French centuries ago."
        t "And I am surprised by your cowardly attitude I must say..."
        if (teaganfucked == False):
            $ lust_points[22] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.3 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
        jump TeaganReturn02
    "Well, Quentin is my best friend, right buddy?":
        if (katefucked == True):
            q "Maybe, I'm still deciding..."
        if (katefucked == False):
            q "Of course, and we are both adventurous and.... Eeek, a snake!"
        jump TeaganReturn02

label VivianeReturn:
scene trailviviane01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "I see you've chosen to be with us at the back [name]..."
menu:
    "You need me to defend you in case we are attacked by savages.":
        vi "Are you suggesting that I am not capable of defending myself?"
        p "No.. Err... I meant..."
        $ lust_points[23] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        vi "And anyway, there are no savages on this island, they were all slaughtered by the French centuries ago... And I'm a descendant of those French colonists..."
        jump VivianeReturn02
    "I want to take my time and admire the view.":
        vi "Well, we still need to get back to the bus fast. So don't fall back too much."
        jump VivianeReturn02

label MariaReturn:
scene trailmaria01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "I see you've chosen to be with us at the front [name]..."
menu:
    "You need a boy to defend you in case we are attacked by savages.":
        ma "I think we girls are perfectly capable of defending ourselves, thank you very much."
        ma "And anyway, there are no savages on this island, they were all slaughtered by the French centuries ago..."
        jump MariaReturn02
    "My thirst for knowledge is insatiable and you are an open encyclopedia.":
        ma "That's real cute. I'm just a part-time librarian but your compliment is much appreciated... [name]."
        if (mariafucked == False) and (lust_points[15] <=8):
            $ lust_points[15] += 1
            $ score += 1
            show lust01:
                xalign 0.3 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01        
        jump MariaReturn02
        
label TeaganReturn02:
scene trailteagan02 with dissolve
$ renpy.pause(1.0, hard=True)
t "This forest is millions of years old and has an amazing biodiversity..."
menu:
    "Look out for a \"Bostiboobicus Gigantus\"":
        scene trailflower with dissolve
        $ renpy.pause(1.0, hard=True)
        menu:
            "Ask Teagan if she knows what it is":
                t "It looks like a \"Bostiboobicus Gigantus\". Don't touch it [name], it stings... I think."
                p "Ah Ok. It stinks too."
                jump LunchBus01
            "Investigate":
                if (plantknowledge == True):
                    p "It definitely looks like a \"Bostiboobicus Gigantus\"... And it stinks like one too."
                    menu:
                        "Pick it up":
                            $ flower = True
                            show flower
                            show square
                            play sound "Sounds/found.mp3"
                            "You acquired a smelly flower."
                            hide square
                            hide flower
                            jump LunchBus01
                        "Don't pick it up, it will probably rot in my pocket anyway and it stinks to high heavens.":
                            jump LunchBus01
                if (plantknowledge == False):
                    p "Hum, I have no idea what this plant is and it stinks to high heavens. I'd better leave it, I doubt this is what Principal Titsworthy is after."
                    jump LunchBus01
    "Continue listening to the teacher":
        t "Veri-Bosti has a unique flora and fauna. Unfortunately, our President-Governor recently said that he would stop protecting this area."
        p "I think he was misunderstood by the fake media. He actually meant to say that \"he would NOT stop protecting this area.\" He corrected himself on Fuxnews."
        t "In any case, enjoy this beautiful site while it lasts kids..."
        t "Ah, I think we are about to reach our destination, I can hear the bus engine..."
        jump LunchBus01

label VivianeReturn02:
scene trailviviane02 with dissolve
$ renpy.pause(1.0, hard=True)
vi "That's a nice hike, it 's good for the leg muscles!"
menu:
    "Look out for a \"Bostiboobicus Gigantus\"":
        scene trailflower with dissolve
        $ renpy.pause(1.0, hard=True)
        menu:
            "Ask Viviane if she knows what it is":
                vi "How should I know, I'm not a botanist! It's just some stupid flower, move along [name], we're trailing the others."
                jump LunchBus01
            "Investigate":
                if (plantknowledge == True):
                    p "It definitely looks like a \"Bostiboobicus Gigantus\"... And it stinks like one too."
                    menu:
                        "Pick it up":
                            $ flower = True
                            show flower
                            show square
                            play sound "Sounds/found.mp3"
                            "You acquired a smelly flower."
                            hide square
                            hide flower
                            jump LunchBus01
                        "Don't pick it up, it will probably rot in my pocket anyway and it stinks to high heavens.":
                            jump LunchBus01
                if (plantknowledge == False):
                    p "Hum, I have no idea what this plant is and it stinks to high heavens. I'd better leave it, I doubt this is what Principal Titsworthy is after."
                    jump LunchBus01
    "Offer to carry Frieda":
        scene trailviviane03 with dissolve
        $ renpy.pause(1.0, hard=True)
        if (friedafucked == False):
            fr "I can walk [name], I am not tired at all, thank you."
            p "OK, let me know if you ever get tired Frieda, I'll be there for you!"
            jump LunchBus01
        if (friedafucked == True):
            fr "Thank you [name]. I am zooo tired, after all the exercise I did yesterday... vith you."
            vi "What are you talking about Frieda? Have you too been practising swimming together?"
            p "Yes, exactly, we did some more swimming in the afternoon, right Frieda? (nudge nudge)"
            fr "Ja, swimming! We... practised ze backstroke a lot... "
            vi "Well, I'm glad to see you are taking the swimming competition on Sunday so seriously [name]!"
            $ lust_points[23] += 1
            $ score += 1
            show lust01:
                xalign 0.1 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01 
        jump LunchBus01

label MariaReturn02:
scene trailmaria02 with dissolve
$ renpy.pause(1.0, hard=True)
menu:
    "Look out for a \"Bostiboobicus Gigantus\"":
        scene trailflower with dissolve
        $ renpy.pause(1.0, hard=True)
        p "There's a peculiar flower on the side of the trail..."
        if (plantknowledge == True):
            p "It definitely looks like a \"Bostiboobicus Gigantus\"... And it stinks like one too."
            menu:
                "Pick it up":
                    ma "What on earth do you think you're doing? Do not even touch that protected plant, it's illegal!"
                    $ lust_points[15] -=1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.15 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                    p "Ah, err, sorry, I just thought it was a common flower..."
                    ma "Now stay close to me, we still have a few more miles to walk. And don't touch the wildlife!"
                    jump LunchBus01
                "Let Maria know you spotted a \"Bostiboobicus Gigantus\"":
                    ma "It is indeed a \"Bostiboobicus Gigantus\"! That's a very rare plant, well done for spotting it [name]!"
                    $ lust_points[15] +=1
                    $ score += 1
                    show lust01:
                        xalign 0.15 yalign 0.4
                        linear 1.0 yalign 0.2
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lust01
                    ma "Gather round everyone, and admire the island's national flower. But don't get too close to it, it stinks to high heavens."
                    fc "Oh, c'est une \"Gigantus Bostinichoncus\", incroyable!"
                    p "Mmh, I didn't realize Latin was different in French than in English..."
                    la "This smell is unbearable! God I hate this flower..."
                    ma "Well, it's a very expensive flower, it can fetch thousands of dollars on the black market. But it's illegal to pick it up, so let's move on."                    
                    jump LunchBus01
        if (plantknowledge == False):
            p "Hum, I have no idea what this plant is... Maybe I should ask Maria."
            ma "It's a \"Bostiboobicus Gigantus\"! That's a very rare plant, you're lucky to have spotted one [name]!"
            ma "Gather round Laura and Joséphine, and admire the island's national flower. But don't get too close to it, it stinks to high heavens."
            fc "Oh, c'est une \"Gigantus Bostinichoncus\", incroyable!"
            p "Mmh, I didn't realize latin was different in French than in English..."
            la "This smell is unbearable! God I hate this flower... This is your fault [name]!"
            if (lust_points[13] <=9):
                $ lust_points[13] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.15 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01            
            ma "Well, it's a very expensive flower, it can fetch thousands of dollars on the black market. But it's illegal to pick it up, so let's move on."
            jump LunchBus01
    "Are we there yet?":
        ma "No."
        p "Are we there yet?"
        ma "No."
        p "Are we there yet?"
        ma "No."
        p "Are we there yet?"
        ma "YES! NOW STOP IT!"
        jump LunchBus01
        
label LunchBus01:
$ hour += 1
scene trailend with dissolve
play music "Sounds/trail.mp3"
$ renpy.pause(1.0, hard=True)
t "Well, we made it back to the bus on time everyone!"
t "Your packed lunches were kept in a cooler. Since the drive back will take one hour, you can eat them on the bus. The school cafeteria will be closed by the time we arrive there."
ma "I hope this trip made you discover the natural beauties of our island and that you will remember them for a long time."
if (teaganfucked == True)and (mariafucked == True):
    scene trailendbothdream with dissolve
    $ renpy.pause(1.0, hard=True)
    p "I sure did discover some \"natural beauties\"... I'll remember them... I can see them in my mind already..."
    t "Well....Err... I'm glad you did [name], now get on the bus and stop fooling around."
    ma "And keep those memories IN YOUR MIND!"
    jump LunchBusChoice
if (mariafucked == True):
    scene trailendmariadream with dissolve
    $ renpy.pause(1.0, hard=True)
    p "I sure did discover some \"natural beauties\"... I'll remember them... I can see them in my mind already..."
    ma "Well....Err... I'm glad you did [name], now get on the bus and stop fooling around."
    jump LunchBusChoice
if (teaganfucked == True):
    scene trailendteagandream with dissolve
    $ renpy.pause(1.0, hard=True)
    p "I sure did discover some \"natural beauties\"... I'll remember them... I can see them in my mind already..."
    t "Well....Err... I'm glad you did [name], now get on the bus and stop fooling around."
    jump LunchBusChoice
scene trailendbothdream with dissolve
$ renpy.pause(1.0, hard=True)
p "(I wish I had gotten a closer look at some of these \"natural beauties\".... (sigh))"

label LunchBusChoice:
scene bigdongbus02 with dissolve
stop music
play music "Sounds/busdrive.mp3"
if (spokenlunchday04 == 2):
    "You finish eating your lunch as the bus pulls into the school grounds."
    jump LunchEndDay04
menu:
    "Talk to Frieda":
        scene busfrieda with dissolve
        $ renpy.pause(1.0, hard=True)
        fr "I'm worried about Maddy. She's still not answering her calls. Her mother has reported her missing to the polizei." 
        fr "I fear ze worst, she might have been ex-ter-mi-na-ted!"
        p "What? No, she got lost, she'll find her way home eventually, don't worry."
        if (lust_points[8] <= 8):
            $ lust_points[8] += 1
            $ score += 1
            show lust01:
                xalign 0.3 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01 
            fr "Well, thank you for comforting me [name], I feel better. Even though I am still zo worried..."            
        p "(Hum, it is getting kind of worrying though... Especially since I haven't fucked her yet.)."        
        $ spokenlunchday04 += 1
        jump LunchBusChoice
    "Talk to Laura":
        scene buslaura01 with dissolve
        $ spokenlunchday04 += 1
        $ renpy.pause(1.0, hard=True)
        menu:
            "Hey Laura, I read that book you gave me." if (bookread == True) and (toldlaurabook == False):                
                $ toldlaurabook = True
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
                jump LunchBusChoice
            "What are you up to this afternoon Laura?":
                if (seencampfireday03 == False) and (lauraritual == True):
                    scene buslaura01 with dissolve
                    la "You didn't turn up last night. That was yet another major disappointment in my life."
                    $ lust_points[13] -=1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.35 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01
                    p "Yeah, I was busy dealing with... err... family matters. God I hate my family!"
                    scene buslaura01 with dissolve
                    la "That's good. We might give you another chance then. Meet us tonight. For real this time!"
                    p "I'll be there, you can count on me Laura! Oh, and death to all but metal and all that."
                    $ lauraritual04 = True
                    jump LunchBusChoice
                la "Hanging out with Damian and Joséphine. Discussing how much life sucks. As per usual... (sigh)"
                if (seencampfireday03 == True):
                    p "Will you try out again some... you know... goth things around the campfire tonight?"
                    if (blacktop04 == True):
                        la "Yeah, why don't you join us? I like having you around... Damian is such a bore..."
                        p "Err... yeah, I'll think about it."
                        $ lauraritual04 = True
                        jump LunchBusChoice
                    if (blacktop04 == False):
                        la "Probably, but you're not invited. Not with this boring white t-shirt you're wearing..."
                        p "Well, I only have one black top, that's why I'm wearing white today. But deep inside, I'm like, totally a goth!"
                        scene buslaura02 with dissolve
                        $ renpy.pause(1.0, hard=True)                        
                        la "A true goth's wardrobe is filled entirely with dark and depressing clothes..."                        
                        jump LunchBusChoice
                if (seencampfireday03 == False):
                    p "Alright, then maybe I'll see you at the back of the school then... To talk about how much life sucks and whatnot."
                    if (blacktop04 == True):
                        la "Sure... Damian is such a bore, I wouldn't mind someone else to talk to..."
                        jump LunchBusChoice
                    if (blacktop04 == False):
                        scene buslaura02 with dissolve
                        la "Unlikely. You're not wearing black, how could you possibly discuss the inequities of life in a white tanktop?"
                jump LunchBusChoice
    "Talk to Kate":
        scene buskate02 with dissolve
        $ renpy.pause(1.0, hard=True)
        k "I've got detention again... When I could be thinking about what bikini I could wear..."
        p "Yeah, our teacher is really nasty to you, I don't understand why."
        $ spokenlunchday04 += 1
        menu:
            "Hey Kate, you know what I found out? That scumbag José is totally backing Brittany for prom queen!" if ((seenlockerbrit == True) or (lust_pointsB[1] >= 8)) and (toldkatejose == False):
                scene buskate02 with dissolve                
                k "What? Oooh, no... I need his vote to win... What a loser, what does he find in her?"                
                $ toldkatejose = True
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
                jump LunchBusChoice
            "Since you will compete in the bikini pageant, I could maybe take pictures of you so you can better decide which bikini to choose?" if (katephotoasked == False):
                scene buskate01 with dissolve 
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
                jump LunchBusChoice
            "Maybe I could cheer you up with a photoshoot session this afternoon?" if (katephotoasked == True) and (katefucked == False):
                scene buskate01 with dissolve
                $ renpy.pause(1.0, hard=True)
                k "Oooh, yes! I have a couple of bikinis I would like to try on!"
                p "Come to my place at 5pm or 6pm then, I'll have everything set up!"
                k "Oh, really? That's so great, I'll be there!"
                $ katephotoplanned04 = True                
                if (camera == False):
                    p "I'd better find a camera TODAY or she'll be mighty disappointed..."
                    jump LunchBusChoice
                if (camera == True):
                    p "(I'd better make sure I'm back home by 5 or 6pm...)"
                    jump LunchBusChoice
            "Don't study, and daydream about stuff instead. That's what I always do during detention.":
                scene buskate01 with dissolve
                $ renpy.pause(1.0, hard=True)
                k "Oooh, thanks for the advice [name]!"
                jump LunchBusChoice
    "Talk to Quentin":
        scene busquentin01 with dissolve
        $ renpy.pause(1.0, hard=True)
        if (katefucked == True):
            p "Hey Quentin, I'm really sorry about what happened with Kate. I'm not interested in her at all really, she's all yours."
            q "Apologies accepted! I worked hard to renew her love for me this morning anyway. I'm sure I'm getting closer!"
            p "Sure buddy, sure buddy... (what a tool!)"
            q "Thanks for your support, it means a lot to me since we are best friends! Now I will consent to giving you a tip then."
            q "I know for a fact that Francine loves pole-dancing and practices it wherever and whenever she can."
            p "Mmh, interesting. Thanks for the tip Quentin."
            $ quentintipfrancine = True
            $ spokenlunchday04 += 1
            jump LunchBusChoice
        if (katefucked == False):
            q "Wasn't that school trip amazing? The beauty of the natural world never ceases to amaze me! I feel like there should TV documentaries about it."
            p "Err, yeah sure. What a great idea, shame no one ever thought about that."
            if (quentintipfrancine == False):            
                p "Any tips for me today buddy?"
                q "Of course, I have my ears everywhere on this island, I am a fountain of knowledge!"
                p "Yeah, OK... So what do you have for me today then?"
                q "Ah ah! I know for a fact that Francine loves pole-dancing and practices it wherever and whenever she can."
                p "Mmh, interesting. Thanks for the tip Quentin."
                $ quentintipfrancine = True
            $ spokenlunchday04 += 1
            jump LunchBusChoice

label LunchEndDay04:
if (smellyflower == True):
    scene mariabus with dissolve
    $ renpy.pause(1.0, hard=True)
    ma "What's this stench? [name], did you pick up a flower you shouldn't have picked up?"
    p "Err.. No, of course not... Flowers are for sissies, why would I do that?"
    ma "Empty your pockets immediately!"
    p "Oh, look, a flower in my pocket! Fancy that, I wonder how it got there..."
    ma "Stop pretending, you're a terrible liar! Now throw it out of the window, its smell is nauseating!"
    if (lust_points[15] <= 9):
        $ lust_points[15] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01     
    p "(Shit, I was found out, maybe I shouldn't have picked it up so soon during the trip, it started to rot in my pocket...)"
    show flower
    show square
    play sound "Sounds/lost.mp3"
    "You threw away a stinky flower."
    hide square
    hide flower
    $ flower = False
    $ smellyflower = False
    
    vi "That's better, we can finally breathe in here! Good thing we're almost arriving."

stop music
scene lunchempty with dissolve
$ hour += 1
$ renpy.pause(1.0, hard=True)
p "Too late to catch up with Nikki and Chantelle... Damn."

if (fuckedschoolgirlday03 == True):
    play sound "Sounds/pasystem.mp3"
    ps "[name] Johnson, please report to the principal's office immediately."
    p "Why? What have I done this time I wonder... I guess I don't have a choice or I might be expelled and mom would be mad... (sigh)."
    jump PrincipalGuidanceDay04

label SchoolChoiceDay04:
stop music
p "I've got the afternoon free. What should I do?"
menu:
    "Go to my locker" if (seenlocker04 == False):
        jump LockerDay04
    "Go to the school gym" if (seenschoolgym04 == False):
        jump SchoolGym01Day04
    "Go to the school library" if (seenlibrary04 == False):
        jump Library01Day04
    "Go to the school backyard" if (seengoths04 == False):
        jump GothsDay04
    "Go on the school rooftop" if (discoverrooftop == True)and (seenrooftop04 == False):
        jump RooftopDay04
    "Go to the principal's office" if (seenwillie04 == False):
        jump WillieCorridorDay04
    "Go to the sports hall" if (seenhall04 == False) and (williequest == True):
        jump SportsHallDay04
    "Go to the school bathroom" if (seenbathroom04 == False):
        jump SchoolBathroom01Day04
    "Go to the nurse's office" if (seennurse04 == False):
        jump NurseDay04
    "Leave the school and go the Burbs":
        jump BurbsDay04

label PrincipalGuidanceDay04:
stop music
scene guidance01 with dissolve
$ renpy.pause(1.0, hard=True)
so "Do you know why I called you in [name]?"
p "Err, no..."
so "Because despite my strict orders, you FUCKED ONE OF OUR GIRLS YESTERDAY!"
menu:
    "Yeah, so? I'm DA MAN, I fuck whoever I want!":
        so "(sigh) Once again, you leave me no choice... Get undressed and get that cock of yours hard NOW!"
        jump PrincipalGuidance02Day04
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
        jump PrincipalGuidance02Day04
    "But I put some posters up for your senate campaign downtown!" if (posterup == True) and (postersaid == False):
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
                            jump PrincipalHypnoDay04
                        "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                            play sound "Sounds/spray.mp3"
                            $ renpy.pause(1.0, hard=True)
                            jump PrincipalPheromonesDay04
                        "Leave":
                            jump SchoolChoiceDay04
                        
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
                            jump PrincipalHypnoDay04
                        "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                            play sound "Sounds/spray.mp3"
                            $ renpy.pause(1.0, hard=True)
                            jump PrincipalPheromonesDay04
                        "Leave":
                            jump SchoolChoiceDay04
        if (flower == False):
            so "So come on, shoot off. I'd better not see you again tomorrow because you fucked one of our girls YET AGAIN! Is that understood?"
            jump SchoolChoiceDay04
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
                        jump PrincipalHypnoDay04
                    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                        play sound "Sounds/spray.mp3"
                        $ renpy.pause(1.0, hard=True)
                        jump PrincipalPheromonesDay04
                    "I also put some posters up for your senate campaign downtown!" if (posterup == True) and (postersaid == False):
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
                            jump SchoolChoiceDay04
                        menu:
                            "Use the pendulum on her" if (pendulumactive == True) and (lust_points[20] >=8):
                                jump PrincipalHypnoDay04
                            "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                                play sound "Sounds/spray.mp3"
                                $ renpy.pause(1.0, hard=True)
                                jump PrincipalPheromonesDay04
                            "Leave":
                                so "So come on, shoot off. I'd better not see you again tomorrow because you fucked one of our girls YET AGAIN! Is that understood?"
                                jump SchoolChoiceDay04

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
                        jump PrincipalHypnoDay04
                    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                        play sound "Sounds/spray.mp3"
                        $ renpy.pause(1.0, hard=True)
                        jump PrincipalPheromonesDay04
                    "Leave":
                        so "And where do you think you're going? You have a guidance session, remember?"
                        p "Oh, that thing..."
                        jump PrincipalGuidance02Day04
                    "I also put some posters up for your senate campaign downtown!" if (posterup == True) and (postersaid == False):
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
                            jump SchoolChoiceDay04
                        menu:
                            "Use the pendulum on her" if (pendulumactive == True) and (lust_points[20] >=8):
                                jump PrincipalHypnoDay04
                            "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                                play sound "Sounds/spray.mp3"
                                $ renpy.pause(1.0, hard=True)
                                jump PrincipalPheromonesDay04
                            "Leave":
                                so "So come on, shoot off. I'd better not see you again tomorrow because you fucked one of our girls YET AGAIN! Is that understood?"
                                jump SchoolChoiceDay04
  

label PrincipalGuidance02Day04:
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
$ lust_points[20] +=2
$ score += 2
show lust02:
    xalign 0.1 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02

stop music
play music "Sounds/principalslow02.mp3"
show guidanceslow
show faster
call screen principalfootjob04
screen principalfootjob04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("FootJobFast02Day04")

label FootJobFast02Day04:
stop movie
hide faster
play music "Sounds/principalfast02.mp3"
show guidancefast
show cum
call screen footjobfaster04
screen footjobfaster04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PrincipalCum02Day04")

label PrincipalCum02Day04:
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

if (principaldeal == False):
    p "I heard you were looking for volunteers to help you in your senate seat election campaign."
    so "Yes, that is correct. A boy like you could put posters up downtown, are you interested in helping?"
    p "What do I get in return?"
    so "Humpf... Normally, people volunteer because they adhere to a political ideal! But fine, I will suspend your guidance session for a day if you spend an hour of your time putting posters up downtown."
    menu:
        "Deal!":
            so "Welcome aboard! The posters are in the corner over there. Take a stack of them on your way out."            
            $ principaldeal = True
            so "Now off you go, I need to call Willie our janitor to clean that mess you made... I'd better not see you again because you fucked yet ANOTHER of our girls!"
            jump SchoolChoiceDay04
        "Not interested, sorry, I'll be rooting for your opponent anyway!":
            so "Then you'll be on the losing side! Now get out of here, I need to call Willie our janitor to clean that mess you made!"
            jump SchoolChoiceDay04
jump SchoolChoiceDay04

label PrincipalHypnoDay04:
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
    jump PrincipalFuckDay04
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
    jump PrincipalFuckDay04
    
label PrincipalPheromonesDay04:
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
    jump PrincipalFuckDay04
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
    jump PrincipalFuckDay04

label PrincipalFuckDay04:
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
label PrincipalStartFuckDay04:
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
        jump PrincipalStartFuckDay04
    "Move on":
        pass
so "NNOO! too... too much.... I can't take it anymore, AAAAHH!"
p "Giving up already principal? You're gonna screw the people as a senator, now it's time for the people to screw YOU!"
label PrincipalFuckChoiceDay04:
menu:
    "I want to stick my cock between your huge jugs..." if (principaltits == False):
        jump PrincipalTitfuckDay04
    "Let's switch position, get on your back!" if (principalback == False):
        jump PrincipalBackFuckDay04
    "Time to finish me off with your arse muscles!" if ((principaltits == True) and (principalback == True)):
        jump PrincipalArseFuckDay04
    
label PrincipalTitfuckDay04:
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
label PrincipalTitFuckDay04b:
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
        jump PrincipalTitFuckDay04b
    "Move on":
        pass
jump PrincipalFuckChoiceDay04

label PrincipalBackFuckDay04:
scene principalback02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready for a good pussy pounding principal?..."
so "Oh yeah, you've made me addicted to that monster cock of yours [name], fuck me hard, as hard as you want!"
label PrincipalBackFuckDay04b:
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
        jump PrincipalBackFuckDay04b
    "Move on":
        pass
so "Oooh, my poor pussy! I'll never recover from such a pounding.... (puff)"
p "Then it's time to try something else..."
jump PrincipalFuckChoiceDay04

label PrincipalArseFuckDay04:
scene principalarse01 with dissolve
$ renpy.pause(1.0, hard=True)
so "You can't be serious! My arse is too tiny for your massive piece of teenage meat!"
p "We're about to find out..."
scene principalarse02 with dissolve
$ renpy.pause(1.0, hard=True)
so "Oh my God, you're stretching me ssooo much!"
p "Just hang in there, there's quite a few more inches to go..."
so "What? Wait...AAAH!"

label PrincipalMainFuckDay04:
play music "Sounds/sophiaslowfuck.mp3"
show sophiafuckslow
show faster
call screen sophiafuckslowday04
screen sophiafuckslowday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("SophiaFuckFastDay04")
label SophiaFuckFastDay04:
hide faster
stop music
play music "Sounds/sophiafastfuck.mp3"
show sophiafuckfast
show cum
call screen sophiafuckfastday04
screen sophiafuckfastday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("SophiaFuckCumDay04")

label SophiaFuckCumDay04:
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
if (sophiajosewin == False):
    p "(She didn't notice I took a picture of her being filled by my dick... Now I'll send it to José)."
    $ sophiawin = True
if (sophiajosewin == True):
    p "(I hate sloppy seconds, especially after that dickhead José already ploughed their insides... But it was worth it, what a pair of tits!)"
$ backdoor += 1
$ sophiafucked = True
jump SchoolChoiceDay04

label RooftopDay04:
$ seenrooftop04 = True
scene rooftop01 with dissolve
play music "Sounds/wind.mp3"
$ renpy.pause(1.0, hard=True)
p "Ah, here's Quentin's telescope..."
if (blacktop04 == True):
    scene rooftop02black with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop02Day04
else:
    scene rooftop02 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop02Day04

label Rooftop02Day04:
p "Let's see what the neighbors are up to..."
$ renpy.pause(1.0, hard=True)
p "Mr Anderson is doing some gardening... BORING!"
p "Hang on a minute, his wife and daughter are on the upper deck jacuzzi..."
scene voyeur01 with dissolve
$ renpy.pause(1.0, hard=True)
p "And there's some muscular redhead boy proudly displaying his massive dong to them. That could become interesting..."
menu:
    "Continue watching (+1 stamina and +1hr)":
        jump Rooftop03Day04
    "Leave, this is bordering on NTR and my fragile ego can't take it!":
        jump SchoolChoiceDay04

label Rooftop03Day04:
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
if (blacktop04 == True):
    scene rooftop02black with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop04Day04
else:
    scene rooftop02 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop04Day04

label Rooftop04Day04:
$ hour += 1
$ stamina += 1
show stamina01:
    xalign 0.7 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide stamina01
jump SchoolChoiceDay04

label SchoolBathroom01Day04:
$ seenbathroom04 = True
if (seenbathroom03 == True):
    if (d2rollbath == 0):
        jump SchoolBathroom01Day04c     
    if (d2rollbath == 1):
        jump SchoolBathroom01Day04b       
$ d2rollbathday04=renpy.random.randint(0, 1)
if (d2rollbathday04 == 0):
    jump SchoolBathroom01Day04b      
if (d2rollbathday04 == 1):
    jump SchoolBathroom01Day04c   

label SchoolBathroom01Day04b:
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
                if (blacktop04 == True):
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
                jump SchoolChoiceDay04
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
                if (lust_pointsB[1] >=1):
                    $ lust_pointsB[1] -=1
                    show challengerlustminus01:
                        xalign 0.6 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide challengerlustminus01
                if (lust_pointsB[1] ==0):
                    pass
            "Yeah, I do that too. I stare at the mirror and admire my huge muscles and say \"I'm da man, I'm DA MAN!\".":
                if (blacktop04 == True):
                    scene schoolbathroombrittany06black with dissolve
                    $ renpy.pause(1.0, hard=True)
                else:
                    scene schoolbathroombrittany06 with dissolve
                    $ renpy.pause(1.0, hard=True)
                br "Pff, pathetic! Now leave me alone little boy, I need to pamper myself."
                jump SchoolChoiceDay04


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
        jump SchoolChoiceDay04

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
        jump SchoolChoiceDay04
    "Walk past her and ignore her":
        if (blacktop04 == True):
            scene schoolbathroombrittany05black with dissolve
            $ renpy.pause(1.0, hard=True)
        else:
            scene schoolbathroombrittany05 with dissolve
            $ renpy.pause(1.0, hard=True)
        br "Hey you, look at me!"
        if (blacktop04 == True):
            scene schoolbathroombrittany06black with dissolve
            $ renpy.pause(1.0, hard=True)
        else:
            scene schoolbathroombrittany06 with dissolve
            $ renpy.pause(1.0, hard=True)
        p "Why? I prefer to look at myself. Yeah, I'm da man, I'm DA MAN!"
        br "Pff, pathetic! Now leave me alone little boy, I need to pamper myself."
        jump SchoolChoiceDay04

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
        jump SchoolChoiceDay04

    "Hey Brittany, José is getting real close to Kate. I wonder why..." if (lust_pointsB[1] >=6) and (lust_pointsB[1] <=9) and (brittanyjosewin == False):
        scene schoolbathroombrittany02c with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What? How could he... This is a crime of lese-majesty that shall not go unpunished!"
        if (lust_pointsB[1] >= 1):
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
        jump SchoolChoiceDay04
        
label SchoolBathroom01Day04c:
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
        jump GloryholeDay04
    "Have a piss and leave.":
        play sound "Sounds/peeing.mp3"
        $ renpy.pause(10.0, hard=True)
        p "Aaah, I needed that."
        jump SchoolChoiceDay04

label GloryholeDay04:
$ seengloryhole04 = True
if (seengloryhole03 == True):
    if (d2rollglory == 0):
        jump GloryholeDay04c     
    if (d2rollglory == 1):
        jump GloryholeDay04b       

$ d2rollglory04=renpy.random.randint(0, 1)
if (d2rollglory04 == 0):
    jump GloryholeDay04b      
if (d2rollglory04 == 1):
    jump GloryholeDay04c 

label GloryholeDay04b:
if (blacktop04 == True):
    scene gloryhole01black with dissolve
    $ renpy.pause(1.0, hard=True)
else:
    scene gloryhole01 with dissolve
    $ renpy.pause(1.0, hard=True)
$ hour += 1
"I waited long enough. Nobody came to take the bait, I'm out of here."
scene schoolbathroom01 with dissolve
$ renpy.pause(1.0, hard=True)
jump SchoolChoiceDay04

label GloryholeDay04c:
if (blacktop04 == True):
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
label GloryHoleSuckDay04:
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
        jump GloryHoleSuckDay04
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
if (blacktop04 == True):
    scene gloryholebrit06black with dissolve
    $ renpy.pause(1.0, hard=True)
else:
    scene gloryholebrit06 with dissolve
    $ renpy.pause(1.0, hard=True)
play sound "Sounds/footsteps.mp3"
p "Oooh, it was Brittany! What a slut! Then again, I'm a he-slut too..."
menu:
    "Call her and let her know it was you":
        jump GloryHoleEnd01Day04
    "Stay put and wait for her to leave":
        jump GloryHoleEnd02Day04
        
label GloryHoleEnd01Day04:
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
jump SchoolChoiceDay04
    
label GloryHoleEnd02Day04:
scene gloryholend with dissolve
$ renpy.pause(1.0, hard=True)
p "She's gone. Now I can do other stuff..."
jump SchoolChoiceDay04

label WillieCorridorDay04:
if (williequestdone == True):
    $ seenwillie04 = True
    jump PrincipalOfficeBackDay04
stop music
scene williecorridor with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/Willie.wav"
$ seenwillie04 = True
wi "Where do you think you're going lad?..."

if (vivianepic == True) and (cantgoback == False) and (williequest == True):
    jump PrincipalBackDay04b
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
            jump PrincipalSnoopingDay04
        if (vivianejosewin == False):
            p "OK, I'll get you your picture you fucking pervert! But I strongly condemn your immorality."
            wi "So says the lad who wants to sneak into Principal Titsworthy's office! Take a hike! And come back with a sexy picture of my Viviane..."
            $ williequest = True
            jump SchoolChoiceDay04
    "I have an appointment with Principal Titsworthy.":
        wi "Oh yeah? Well, she ain't there, so that's a wee bit suspicious."
        p "I'll wait for her then."
        wi "No you won't. Move it lad or Willie will report you to the Principal. And you wouldn't want to cross her, I tell ya!"
        jump SchoolChoiceDay04

label PrincipalSnoopingDay04:
scene principalsnooping with dissolve
play music "Sounds/snooping.mp3"
$ d2rollofficeday04=renpy.random.randint(0, 1)
if (d2rollofficeday04 == 0):
    call screen officesnoop01day04
if (d2rollofficeday04 == 1):
    call screen officesnoop02day04
$ renpy.pause(1.0, hard=True)
stop music
"I was too slow and didn't find the right folder... Now I have to leave or Willie will lock me up..."
jump SchoolChoiceDay04

label FoundFriedaGradeDay04:
scene principalsnooping
$ renpy.pause(1.0, hard=True)
stop music
p "Frieda...Frieda....Ah, there it is, now I'll change the F grade for an A. Piece of cake, I'm DA MAN!"
play sound "Sounds/Willie02.wav"
$ renpy.pause(2.0, hard=True)
$ friedachangedgrade = True
p "Let's get the hell out of here before the principal comes back..."
jump SchoolChoiceDay04

label LockerDay04:
$ seenlocker04 = True
if (seenlocker02 == True) and (seenlocker03 == True):
    if (seenlockerempty == True) and (seenlockerbrit == True):
            jump LockerKate01Day04  
    if (seenlockerempty == True) and (seenlockerkate == True):
            jump BritLockerDay04  
    if (seenlockerbrit == True) and (seenlockerkate == True):
            jump LockerEmpty02Day04  

if ((seenlocker02 == True) and (seenlocker03 == False)) or ((seenlocker02 == False) and (seenlocker03 == True)):
    $ d2rolllocker04=renpy.random.randint(0, 1)
    if (seenlockerkate == True):
        if (d2rolllocker04 == 0):
            jump BritLockerDay04
        if (d2rolllocker04 == 1):
            jump LockerEmpty02Day04  
    if (seenlockerbrit == True):
        if (d2rolllocker04 == 0):
            jump LockerKate01Day04  
        if (d2rolllocker04 == 1):
            jump LockerEmpty02Day04  
    if (seenlockerempty == True):
        if (d2rolllocker04 == 0):
            jump BritLockerDay04
        if (d2rolllocker04 == 1):
            jump LockerKate01Day04  
    if (seenlockerbrit == True):
        if (d2rolllocker04 == 0):
            jump LockerEmpty02Day04
        if (d2rolllocker04 == 1):
            jump LockerKate01Day04 

$ d3rolllocker04=renpy.random.randint(0, 2)
if (d3rolllocker04 == 0):
    jump LockerKate01Day04      
if (d3rolllocker04 == 1):
    jump LockerEmpty02Day04    
if (d3rolllocker04 == 2):
    jump BritLockerDay04
 
label LockerEmpty02Day04:
scene lockerempty with dissolve
$ renpy.pause(1.0, hard=True)
$ seenlockerempty = True
p "There's no one around... Like everyone left school or something. And I'm here, wasting my time in empty corridors like an idiot."
jump SchoolChoiceDay04

label LockerKate01Day04:
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
        jump LockerKate08Day04
    "Well pick it up then.":
        k "Uh...oh...OK."
        scene lockerkate02
        $ renpy.pause(1.0, hard=True)
        k "Oooh, it's too far, I can't reach it...Uuh..."
        menu:
            "Well, bend over some more...":
                jump LockerKate03Day04
            "Offer to help":
                k "No, I'm...OK....Ooh, I hope my panties aren't...like... showing.... Are they?"
                menu: 
                    "Not at all, I can't see a thing. You can bend more.":
                        jump LockerKate03Day04
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
                        jump LockerKate03Day04
 
label LockerKate03Day04:
scene lockerkate03 with dissolve
$ renpy.pause(1.0, hard=True)
k "Like that?... I still can't find my pen...Oooh, Where is it?"
menu:
    "It's right in front of you, you dumb bimbo.":
        k "Oooh, yes, I see it now...Hee...hee..."
        play sound "Sounds/katehihi.mp3"
        jump LockerKate07Day04
    "Look some more, meanwhile, I'll probe behind you, it might be stuck somewhere...":
        k "Ooh, OK...hee...hee..."
        play sound "Sounds/katehihi.mp3"
        if (blacktop04 == True):
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
                jump LockerKate08Day04
            "Don't mind me, I'm in control of the situation...":
                jump LockerKate07Day04

label LockerKate07Day04:
scene lockerkate06 with dissolve
$ renpy.pause(1.0, hard=True)
k "Uh...OK...I'll continue looking... Oh, look, I found my pen!"
label LockerKate08Day04:
scene lockerkate07 with dissolve
$ renpy.pause(1.0, hard=True)
p "Well done, you're such a smart girl! By the way, it's actually a pencil, not a pen."
label KateLockerEndDay04:
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
    jump SchoolChoiceDay04
menu:
    "How about this afternoon at 5 or 6pm at my place for our photoshoot session?" if (katephotoasked == True):
        $ katephotoplanned04 = True
        k "Ooh, yeah, yippee! I'll DEFINITELY be there!"
        jump SchoolChoiceDay04
    "Ok, see you tomorrow Kate!":
        k "Ooh, yeah, see you tomorrow [name], hee hee!"
        play sound "Sounds/katehihi.mp3"
        jump SchoolChoiceDay04
        

label BritLockerDay04:
scene
stop music
play sound "Sounds/footsteps.mp3"
$ renpy.movie_cutscene("Day2/britlocker.ogv")
scene lockerbritmovie
show slowmo
call screen britslowmoDay04
screen britslowmoDay04:
    modal True
    button:
        xpos .82
        ypos .9
        xysize(120, 50)
        action Jump ("BritSlowMoDay04")
label BritSlowMoDay04:
play sound "Sounds/britlockerslowmo.mp3"
$ renpy.movie_cutscene("Day2/britlockerslowmo.ogv")
scene lockerbritmovie
$ renpy.pause(1.0, hard=True)

label LockerBrit01Day04:
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
        jump LockerBritEavesdropDay04
    "Barge in on the conversation":
        jump LockerBrit02Day04
        
label LockerBrit02Day04:
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
        jump SchoolChoiceDay04
    "I might be a junior student, but I'm a senior in bed.":
        show lockerbrit02b
        br "So boring, another wannabe stud. I only date REAL studs."
        j "Yeah, like ME. Do you hear that [name]?"
        br "I don't recall saying YOU were a REAL stud either..."
        show lockerbrit02c
        j "But, babe, everyone knows I'm the school stud..."
        br "Well, maybe I should look OUTSIDE of this school... A goddess like me deserves the BEST..."
        jump BritLocker03Day04
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
        jump BritLocker03Day04

label BritLocker03Day04:
scene lockerbrit02 with dissolve
$ renpy.pause(1.0, hard=True)
br "I've wasted enough time talking to you. A true princess like me needs to spend more time pampering herself."
br "Do not disturb me until I grant you permission."
menu:
    "Sure ma'am, at your cervix your Magnificent Beautifulness! (snickers)":
        show lockerbrit02b
        br "Be gone!"
        jump SchoolChoiceDay04
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
        jump SchoolChoiceDay04
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
            jump SchoolChoiceDay04
        menu: 
            "José is lying. It was actually 4 dollars.":
                br "Oh my God, that's even worse!!! Be gone and keep your cheap wristband!"
                jump SchoolChoiceDay04
            "Oh, hang on a minute, I seem to have given you the wrong one. My bad, this one was meant for...err.. Kate.":
                br "That would indeed suit that cheap bimbo... Who dares try to claim my throne as bikini pageant queen this year again!"
                br "Come back with your \"proper\" present tomorrow then. Or else..."
                p "Yeah... Of course... Ahem... Thank you, your...err.. majesty."
                $ britpresentfail = True
                jump SchoolChoiceDay04

label LockerBritEavesdropDay04:
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
        jump LockerBrit02Day04
    "Leave, you are defeated, what's the point in arguing...":
        jump SchoolChoiceDay04


label GothsDay04:
stop music
$ seengoths04 = True
scene goth01 with dissolve
$ renpy.pause(1.0, hard=True)

if (seengoths == False) and (seengoths03 == False):
    jump GothsFirstDay04
if (seengoths == True) and (seengoths03 == True):
    jump GothsThirdDay04
if (seengoths == True) or (seengoths03 == True):
    jump GothsSecondDay04

label GothsFirstDay04:
p "Apparently, this is where the goth kids hang out… Laura is here, with some douchebag dude and the local girl."
la "Hey [name], you decided to join us?"
go "What’s he doing here? Do you know him Laura?"
if (madelaurasmile == True):
    la "Yeah, he’s a new classmate, he’s kinda cool though."
elif (madelaurasmile == False):
    la "Yeah, he’s a new classmate, he’s kinda of a bore though."

label GothChoiceDay04:
menu:
    "What's the local chick doing with you?" if (gothmenu <= 1):
        go "She's black, so she must be a goth."
        menu:
            "That makes absolutely no sense at all...":
                $ gothmenu += 1
                jump GothChoiceDay04
            "Of course, silly me.":
                $ gothmenu += 1
                jump GothChoiceDay04
    "Can I join your club?" if (gothmenu <= 1):
        go "No fucking way dude. You ain't no goth."
        $ gothmenu += 1
        jump GothChoiceDay04
    "Talk to the black girl" if (gothmenu >= 2):
        show goth01d
        fc "Ou suis-je, que fais-je, dans quel état j’erre?"
        p "Hum... moi... non par-ley... frenchie."
        fc "Hein? Quoi?"
        p "Yeah, I think she got it..."
        hide goth01d
        jump GothChoiceDay04
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
                        jump GothChoiceDay04
                    "Refuse and say that your body is your temple":
                        go "What a chicken..."
                        window hide
                        $ lust_points[13] -=1
                        $ score -= 1
                        show lustminus01:
                            xalign 0.35 yalign 0.2
                            linear 1.0 yalign 0.4
                        play sound "Sounds/less.mp3"
                        $ renpy.pause(2, hard=True)
                        hide lustminus01
                        scene goth01
                        jump GothChoiceDay04
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
                    jump SchoolChoiceDay04      
    "Talk to the goth kid" if (gothmenu >= 2):
        go "What’s your favorite band?"
        menu:
            "New Kids on the Block":
                go "What? Get the hell out of here!"
                la "So lame... I hate you."
                jump SchoolChoiceDay04
            "Pharell Williams":
                go "Someone please kill me... That's not even a band!"
                jump GothChoiceDay04
            "The Cure":
                go "Nice..."
                jump GothChoiceDay04
            "What's it to you dipshit?":
                go "What the fuck?..."
                la "Haha, he got you there..."
                go "He didn't answer the question..."
                la "Real goths don't have to answer questions..."
                jump GothChoiceDay04

label GothsSecondDay04:
if (blacktop04 == False):
    go "You're not a goth, how many times do I have to tell you? GET OUT OF HERE!"
    show lauraangrygoth with dissolve
    la "Sorry [name], but Damian is right. I mean, look at you, wearing a conformist white tank top... Pathetic."
    $ lust_points[13] -=1
    $ score -=1
    show lustminus01:
        xalign 0.35 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    jump SchoolChoiceDay04
    
if (blacktop04 == True):
    go "Ah, I see you've actually made an effort this time with your clothing. Although you're still not a goth clearly."
    show goth01c with dissolve
    la "He's learning Damian, we should encourage him... Maybe he could come tonight..."
    show damianangry with dissolve
    $ renpy.pause(1.0, hard=True)
    go "What? Are you out of your mind? We don't let newbies onto our little secrets like that!"
    if (toldlaurabook == True):
        la "He's also read that book I gave him. He's ready I say. Joséphine agrees with me too."
        hide damianangry with dissolve
        go "Alright, but you'd better not screw anything up tonight I'm warning you boy!"
        p "What's this about? I'll decide if I can be bothered joining whatever it is you're up to tonight anyway!"
        la "Such antiestablishmentarism! We are performing a goth ritual, summoning demons and stuff. Meet us at the campfire on the local beach tonight if you're interested..."
        $ lauraritual04 = True
    if (toldlaurabook == False):
        hide goth01c with dissolve
        la "I guess you're right. He hasn't even read the book I gave him yet."
        if (bookread == True):
            $ toldlaurabook = True
            p "No I did, I swear! Took me a full hour too."
            show goth01c with dissolve
            la "Oh really? And what did you think about it then?"
            hide damianangry with dissolve
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
            la "Alright, then you're ready. We are performing a goth ritual, summoning demons and stuff. Meet us at the campfire on the local beach tonight if you're interested..."
            $ lauraritual04 = True
        if (bookread == False):
            p "I didn't have time. But I'm planning on reading it, I swear!"
            la "Well, come back to us when you have. Right now, Damian is right, you're not ready."
    p "Time to leave them and do something else."
    jump SchoolChoiceDay04

label GothsThirdDay04:
if (blacktop04 == False):
    go "You're not a goth, how many times do I have to tell you? GET OUT OF HERE!"
    show lauraangrygoth with dissolve
    la "Sorry [name], but Damian is right. I mean, look at you, wearing a conformist white tank top... Pathetic."
    if (laurafucked == True):
        p "But I thought... You and I..."
        la "A true goth is no true friend to anyone but death!"
        p "(I'm starting to really dislike this way of... life.)"
    if (lust_points[13] <= 9):
        $ lust_points[13] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.35 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
    jump SchoolChoiceDay04

if (blacktop04 == True):
    go "Ah, I see you've actually made an effort  with your clothing. Although I still don't consider you to be a true goth."
    show goth01c with dissolve
    if (seencampfireday03 == True):
        p "So, will you guys try out again some... you know... goth things around the campfire tonight?"
        la "Yes, the world needs to be punished! And especially my parents..."
        go "You can join us, but don't screw up like you did last night!"
        p "I didn't screw up! YOU screwed up!"
        la "Enough you two! You'll settle your differences tonight..."
        $ lauraritual04 = True
        jump SchoolChoiceDay04
    if (seencampfireday03 == False) and (lauraritual == True):
        show lauraangrygoth with dissolve
        la "You didn't turn up last night. That was yet another major disappointment in my life."
        $ lust_points[13] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.35 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        p "Yeah, I was busy dealing with... err... family matters. God I hate my family!"
        hide lauraangrygoth with dissolve
        la "That's good. We might give you another chance then. Meet us tonight. For real this time!"
        go "You won't get another chance, we're warning you! Now get out of here. DEATH TO ALL BUT METAL!"
        la "DEATH TO ALL BUT METAL!"
        p "I'll be there, you can count on me Laura! Oh, and death to all but metal and all that."
        $ lauraritual04 = True
        jump SchoolChoiceDay04
    if (seencampfireday03 == False) and (lauraritual == False):
        la "He's learning Damian, we should encourage him... Maybe he could come tonight..."
        show damianangry with dissolve
        $ renpy.pause(1.0, hard=True)
        go "What? Are you out of your mind? We don't let newbies onto our little secrets like that!"
        if (toldlaurabook == True):
            la "He's also read that book I gave him. He's ready I say. Joséphine agrees with me too."
            hide damianangry with dissolve
            go "Alright, but you'd better not screw anything up tonight I'm warning you boy!"
            p "What's this about? I'll decide if I can be bothered joining whatever it is you're up to tonight anyway!"
            la "Such antiestablishmentarism! We are performing a goth ritual, summoning demons and stuff. Meet us at the campfire on the local beach tonight if you're interested..."
            $ lauraritual04 = True
        if (toldlaurabook == False):
            hide goth01c with dissolve
            la "I guess you're right. He hasn't even read the book I gave him yet."
            if (bookread == True):
                $ toldlaurabook = True
                p "No I did, I swear! Took me a full hour too."
                show goth01c with dissolve
                la "Oh really? And what did you think about it then?"
                hide damianangry with dissolve
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
                la "Alright, then you're ready. We are performing a goth ritual, summoning demons and stuff. Meet us at the campfire on the local beach tonight if you're interested..."
                $ lauraritual04 = True
            if (bookread == False):
                p "I didn't have time. But I'm planning on reading it, I swear!"
                la "Well, come back to us when you have. Right now, Damian is right, you're not ready."
        p "Time to leave them and do something else."
        jump SchoolChoiceDay04

label SportsHallDay04:
$ seenhall04 = True
stop music
scene sportshall01 with dissolve
$ renpy.pause(1.0, hard=True)
p "The lockers are empty... But I can hear some sound from the girl's shower area..."
menu:
    "Go and have a peek":
        jump SportsHall02Day04
    "Don't do it, you might get caught...":
        jump SchoolChoiceDay04

label SportsHall02Day04:
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
        jump PrincipalBackDay04
    "Do something else":
        $ cantgoback = True
        jump SchoolChoiceDay04

label PrincipalBackDay04:
$ d2principalback04=renpy.random.randint(0,1)  
if (d2principalback04 == 0):
    scene williecorridor with dissolve
    $ renpy.pause(1.0, hard=True)
    label PrincipalBackDay04b:
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
    jump PrincipalSnoopingDay04

if (d2principalback04 == 1):
    jump PrincipalOfficeBackDay04

label PrincipalOfficeBackDay04:
scene principalback01 with dissolve
$ renpy.pause(1.0, hard=True)
so "What are you doing here? Can't you see I'm busy?"
menu:
    "Ah. Yes, I got the wrong door sorry.":
        so "Apparently, you can't read. It says \"Principal's Office\" in huge letters on the door. Now get out!"
        jump SchoolChoiceDay04  
    "I'm interested in joining your campaign as a volunteer." if (principaldeal == False) and (posterup == False):
        so "That's great, I can always use some extra help in putting posters up! Welcome on board!"
        so "I need some posters to be put up downtown. The posters are in the corner over there. Take a stack of them on your way out." 
        p "Will do Senator Titsworthy!"
        $ principaldeal = True
        jump SchoolChoiceDay04
    "I found a \"Bostiboobicus Gigantus\" in full bloom..." if (flower == True) and (gaveflower == False):
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
                        jump PrincipalHypnoDay04
                    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                        play sound "Sounds/spray.mp3"
                        $ renpy.pause(1.0, hard=True)
                        jump PrincipalPheromonesDay04
                    "Leave":
                        so "So come on, shoot off. I'd better not see you again tomorrow because you fucked one of our girls YET AGAIN! Is that understood?"
                        jump SchoolChoiceDay04                        
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
                if (lust_points[20] >=10):
                    show epiclust:
                        xalign 0.2 yalign 0.2
                        zoom 0.5
                        linear 2.0 zoom 1.0
                    play sound "Sounds/epiclust.mp3"
                    $ renpy.pause(4.0, hard=True)
                    hide epiclust
                    so "However, right now, I want your pants ZIPPED DOWN!"
                    jump PrincipalFuckDay04                            
                menu:
                    "Use the pendulum on her" if (pendulumactive == True) and (lust_points[20] >=8):
                        jump PrincipalHypnoDay04
                    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[20] >=8):
                        play sound "Sounds/spray.mp3"
                        $ renpy.pause(1.0, hard=True)
                        jump PrincipalPheromonesDay04
                    "Leave":
                        jump SchoolChoiceDay04
    
label SchoolGym01Day04:
$ seenschoolgym04 = True
if (schoolgymchantelle == True):
    $ schoolgymempty = True
    jump SchoolGymEmptyDay04
if (schoolgymempty == True):
    $ schoolgymchantelle = True
    play music "Sounds/gymmusic.mp3"
    scene chantellegym01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Chantelle is doing some curls... She hasn't seen me come in."
    menu:
        "Do some heavy training, better equipment means I can cut on my routine time (+1hr)":
            p "I hope you don't mind if I do some heavy training with barbells in my jockstrap?"
            ch "What?.. No, it's fine...Be my guest..."
            jump ChantelleRyanWorkoutDay04
        "Watch her for a while":
            jump SchoolGymChantelle02Day04
if (schoolgymmaddy == True) and (schoolgymchantelle == False) and (schoolgymempty == False):
    $ d2rollsday04=renpy.random.randint(0,1)    
    if (d2rollsday04 ==0):
        $ schoolgymchantelle = True
        play music "Sounds/gymmusic.mp3"
        scene chantellegym01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Chantelle is doing some curls... She hasn't seen me come in."
        menu:
            "Do some heavy training, better equipment means I can cut on my routine time (+1hr)":
                p "I hope you don't mind if I do some heavy training with barbells in my jockstrap?"
                ch "What?.. No, it's fine...Be my guest..."
                jump ChantelleRyanWorkoutDay04
            "Watch her for a while":
                jump SchoolGymChantelle02Day04
    if (d2rollsday04 ==1):
        $ schoolgymempty = True    
        jump SchoolGymEmptyDay04
    
label SchoolGymEmptyDay04:
scene schoolgymempty with dissolve
$ renpy.pause(1.0, hard=True)
p "There's no one around, I could use this gym to train and get stronger..."
menu:
    "Do some heavy training, better equipment means I can cut on my routine time (+1hr)" if (workout == False):
        jump SchoolGymWorkoutDay04
    "Leave":
        jump SchoolChoiceDay04

label ChantelleRyanWorkoutDay04:
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
$ muscleman += 1
p "What next?"
ch "This..is going too fast...maybe...I don't want to lose your landlady's daughter's friendship...sorry...I shouldn't have..."
p "But...What did I do wrong? It's not fair!"
ch "Another time maybe [name]... Let's leave it at that for now...I...should go now..."
jump SchoolChoiceDay04

label SchoolGymChantelle02Day04:
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
        jump SchoolGymChantelle03Day04
    "Of course, I only use the biggest weights around all the time, piece of cake for me!":
        ch "Mmh, I want to see that..."
        jump SchoolGymChantelle04Day04
    "Actually, I was planning on a serious routine with barbells, but I need to concentrate...(+1hr)":
        ch "Sure, I'll continue my exercises and I'll leave you alone, don't worry..."
        p "Also, I like to train with my shorts and tank top off, hope you don't mind..."
        ch "Ooh? No... I don't mind..."
        jump ChantelleRyanWorkoutDay04
        
label SchoolGymChantelle03Day04:
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
        jump SchoolGymWorkoutDay04   
    "Leave": 
        jump SchoolChoiceDay04
 

label SchoolGymChantelle04Day04:
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
            jump SchoolGymWorkoutDay04
        "Leave":
            jump SchoolChoiceDay04
         
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
            jump SchoolGymWorkoutDay04
        "Leave":
            jump SchoolChoiceDay04
   
label SchoolGymWorkoutDay04:
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
jump SchoolChoiceDay04
    
label NurseDay04:
scene clinic01 with dissolve
$ seennurse04 = True
$ renpy.pause(1.0, hard=True)
je "Oh, hello [name]. The... hum... test results for your sperm sample came back and the clinic says they would like to extract some more for further analysis..."
menu:
    "What does that mean exactly?":
        je "They wouldn't elaborate but they claimed it was very important... I could take you there by car, it's not far away and we would get there in no time at all!"
        je "And you'll be next to the beach if you wanted to get there afterwards..."
        menu:
            "Ok, why not.":
                je "Great! I'll get dressed and we can be on our way."
                jump ClinicDay04
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
                jump SchoolChoiceDay04                    
    "What's in it for me?":
        je "I'll give you 5 dollars if you come with me to the clinic right now."
        je "It's not far, we'll get there in no time by car. And you'll be next to the beach if you wanted to get there."
        menu:
            "Ok, why not.":
                $ money += 5
                je "Great! I'll get dressed and we can be on our way."
                jump ClinicDay04
            "Not interested, I have other plans for the day.":
                scene clinic02 with dissolve
                $ renpy.pause(1.0, hard=True)
                jump SchoolChoiceDay04
    "I'm too busy this afternoon, another time.":
        je "I hope you decide to take them up on their offer soon. Like tomorrow..."
        scene clinic02 with dissolve
        $ renpy.pause(1.0, hard=True)
        jump SchoolChoiceDay04
        
label ClinicDay04:
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
dr "That is indeed an exceptional load... Please bring the receptacle over to the lab for analysis once the boy is done cumming like a firehose into the extractor nurse Racks..."
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
        jump ClinicEndDay04
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
        jump ClinicEndDay04
    "I'll think about it. I am totally drained...":
        dr "And that is why you should come back. With just one load, you can give us enough sperm to impregn... I mean perform lots and lots of scientific tests."
        dr "Now off you go, I have some patients with tiny useless noodle dicks to attend to."
        jump ClinicEndDay04        

label ClinicEndDay04:
scene clinicentrance with dissolve
$ renpy.pause(1.0, hard=True)
p "It seems this place is like a shortcut between the Burbs and Tini-Wini Bikini Beach... I can go to either way in no time."
menu:
    "Go to the Burbs":
        jump BurbsDay04
    "Go to the beach":
        jump Beach01Day04


label Library01Day04:
stop music
play music "Sounds/coughing.mp3"
if (seenjosemarialibrary == False):
    scene mariajoselibrary01 with dissolve
    $ renpy.pause(1.0, hard=True)
    $ seenjosemarialibrary = True
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
        if (lust_pointsB[15] <= 9):
            $ lust_pointsB[15] += 1
            show challengerlustplus01:
                xalign 0.3 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide challengerlustplus01
    menu:
        "Ignore them and find Frieda":
            jump Library04Day04
        "Barge in on the conversation":
            jump Library02Day04
        "Wait for José to leave and talk to Maria":
            jump Library03Day04
        "Leave the library and go elsewhere":
            jump SchoolChoiceDay04
        
if (seenjosemarialibrary == True):
    jump Library03Day04

label Library02Day04:
scene mariajoselibrary02 with dissolve
$ renpy.pause(1.0, hard=True)
j "What do you want worm?"
menu:
    "Your head on a spike":
        window hide
        show mariajoselibrary02b with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "Stop it you two! I will not have two students fighting in my library!"
        if (lust_points[15] <= 9):
            $ lust_points[15] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.2 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
        ma "Now disperse! In OPPOSITE directions..."
        jump LibraryChoiceDay04
    "I need to speak to Maria about some important stuff...":
        window hide
        if (mariawin == True):
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
            jump Library03Day04
        if (mariafucked == False):
            j "Oh really? How fascinating. I was just talking myself about important stuff to Maria... Fancy that..."
            show mariajoselibrary02b
            ma "And you literally barged in on the conversation. Which is very rude."
            if (lust_points[15] <= 9):
                $ lust_points[15] -= 1
                $ score -= 1
                show lustminus01:
                    xalign 0.2 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
            show mariajoselibrary02c
            j "Ha Ha... LOSER! I'm laughing so hard, I have to leave or I'll disturb the whole library... HA HA HA!"
            p "(Fucking arsehole...)"
            jump Library03Day04
            
label Library03Day04:
scene marialibrary04 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Hello [name]. What can I do for you today?"
menu:
    "I'm looking for a book on... how to have sex with a huge cock without hurting girls." if (mariafucked == False):
        scene marialibrary03 with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "Oh, that is sssoo subtle..."
        jump LibraryChoiceDay04
    "Thanks for coming with us on the schooltrip this morning. And the in-depth knowledge of Bigdong Falls you provided..." if (spokenbigdongteagan == True):
        ma "Yes... err... Let's not talk about this too much in a public space..."
        jump LibraryChoiceDay04
    "I was wondering if you had any books about the native plants of Veri-Bosti..." if (plantknowledge == False):
        jump Library03Day04b
    "I don't need any help, I know what I'm doing...":
        ma "Fine. Come back here though if you want to borrow a book."
        label LibraryChoiceDay04:
        menu:
            "Talk to Maria" if (spokemaria04 == False):
                jump Library03Day04
            "Look for Frieda" if (spokefriedalibraryday04 == False):
                jump Library04Day04
            "Look for a book on native plants" if (spokenerdy == False) and (spokenerdy04 == False) and (plantknowledge == False):
                jump Library05Day04
            "Learn how to use the hypnosis pendulum" if (pendulum == True) and (pendulumactive == False):
                jump LibraryPendulumDay04
            "Read the book about Goths that Laura gave you" if (book == True) and (bookread == False):
                jump LibraryGothDay04
            "Leave the library":
                jump SchoolChoiceDay04

label Library03Day04b:
stop music
$ spokemaria04 = True
ma "Of course, follow me!"
scene marialibrary05 with dissolve
$ renpy.pause(1.0, hard=True)
p "(Man, what a fine booty Maria has... Not to mention her rack...)"
scene marialibrary06 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Let's see... Yes, the \"Compendium of flora and fauna of Veri-Bosti Island\" by Charles Dick'em."
p "I am particularly interested in the \"Bostiboobicus Gigantus\"..."
ma "Ah yes, our most famed and rare native plant. Do you have to write an essay on it?"
p "Err... Yeah, sure."
ma "It almost became extinct because so many rich people overseas wanted one until our President-Governor put a ban on its export."
scene marialibrary07 with dissolve
$ renpy.pause(1.0, hard=True)
ma "I still don't get the craze for this plant. It stinks of rotten milk, because there's a putrid white liquid that oozes from its flower tip, see?"
p "Ah, very interesting. Where could you find these plants on the island?"
ma "It says here that they grow in very humid tropical forests, or possibly near waterfalls."
ma "We could have spotted one this morning. But we didn't, they are very rare. Of course, you can't pick one up, it's illegal."
ma "But you can learn more about it by borrowing this book and studying it for your essay. Here!"
p "Thanks...(shit, now she expects me to study this godamn book... What a waste of time.)"
$ plantknowledge = True
if (blacktop04 == True):
    scene ryanreadinglibraryblack with dissolve
else:
    scene ryanreadinglibrary with dissolve
$ renpy.pause(1.0, hard=True)
p "I'm not learning anything useful by reading this stupid compendium... It just talks about all kinds of silly plants I don't care about..."
$ hour += 1
p "That's enough, I'll tell her I studied the book and wrote my essay so I can leave this God-forsaken place!"
scene marialibrary01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "So, did the book help you for your essay?"
p "Sure, thanks for pointing it out to me..."
ma "You're welcome, I hope you get a straight A, you deserve it, you're such an earnest student!"
if (lust_points[15] <= 8):
    $ lust_points[15] += 1
    $ score += 1
    show lust01:
        xalign 0.3 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
jump LibraryChoiceDay04

label Library05Day04:
stop music
scene nerdy00 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, this library has too many books, I'll never find what I'm looking for..."
menu:
    "Go back and talk to Maria":
        jump Library03Day04
    "Talk to the nerdy girl with glasses" if (spokenerdy04 == False) and (spokenerdy == False):
        jump Library06Day04

label Library06Day04:
$ spokenerdy04 = True
p "Excuse me, do you know where the section on native plants is?"
scene nerdy01 with dissolve
play sound "Sounds/gasping.mp3"
$ renpy.pause(1.0, hard=True)
ne "A boy is talking to me! I'm so excited!"
menu:
    "Calm down, take a deep breath...":
        ne "I can't, I'm too excited! I'm wetting my panties!"
        menu:
            "Let's have a look at that problem of yours...":
                scene nerdy02 with dissolve
                play sound "Sounds/gasping.mp3"   
                $ renpy.pause(1.0, hard=True)
                ne "Wh..what are you doing? A boy is touching my naughty bits, oh my God, oh my God, I'm so excited!"
                p "Jeeezus girl, it's like the Niagara Falls down there! Calm down!"
                ne "Eek, I can't take it anymore, I'm gonna piss myself!"
                scene nerdy03 with dissolve
                $ renpy.pause(1.0, hard=True)
                p "Hey, where are you going, come back, you didn't tell me where the section on native plants was!"
                p "Shit...Now I have to go back and ask Maria..."
                jump Library03Day04

            "Just tell me where the section is already!":
                play sound "Sounds/gasping.mp3"
                ne "It's behind you. Don't move, I'll get that book for you..."
                if (blacktop04 == True):
                    scene nerdy05black with dissolve
                else:
                    scene nerdy05 with dissolve
                $ renpy.pause(1.0, hard=True)
                ne "There you are... Sorry, I need to go, my panties are all wet!"
                scene nerdy03 with dissolve
                $ renpy.pause(1.0, hard=True)                
                p "Err, sure... Thanks... See you around..."
                if (blacktop04 == True):
                    scene nerdy06black with dissolve
                else:
                    scene nerdy06 with dissolve
                p "Ah, there's a picture of the \"Bostiboobicus Gigantus\". It says it stinks of rotten milk..."
                p "... Because there's a putrid white liquid that oozes from its flower tip... I see, interesting..."
                $ plantknowledge = True
                jump LibraryChoiceDay04                
    "Ah, I see, you're crazy.":
        ne "Oh no, the only boy who ever spoke to me thinks I'm crazy, AAARGH!"
        scene nerdy03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Hey, where are you going, come back, you didn't tell me where the section on native plants was!"
        p "Shit...Now I have to go back and ask Maria..."
        jump Library03Day04
    "You talk like you've never seen a cock in your life.":
        ne "What? A COCK? Oh my God, do you have ONE?"
        p "Err, Yeah, I have one."
        ne "Show me, show me, show me!"
        p "What, like here right now?"
        ne "Yes, show me right now and I'll tell you where the section on native plants is!"
        menu:
            "Pull your shorts down...":
                if (blacktop04 == True):
                    scene nerdy04black with dissolve
                else:
                    scene nerdy04 with dissolve                    
                $ renpy.pause(1.0, hard=True)
                ne "Oh, it's so beautiful! I want to touch it..."
                menu:
                    "Be my guest...":
                        if (blacktop04 == True):
                            scene nerdy07black with dissolve
                        else:
                            scene nerdy07 with dissolve    
                        $ renpy.pause(1.0, hard=True)
                        ne "Oh my God, I'm holding a boy's sin snake... It's so big, like an anaconda..."
                        menu:
                            "Watch out, it might spew its venom if you keep going...":
                                ne "What??? This thing is evil! My pastor warned me! Eek!"
                                scene nerdy03 with dissolve
                                $ renpy.pause(1.0, hard=True)
                                p "Hey, where are you going, come back, you didn't tell me where the section on native plants was!"
                                p "Shit...Now I have to go back and ask Maria..."
                                jump Library03Day04
                            "Now that you've touched it, show me where that book I'm looking for is...":
                                ne "It's behind you. Don't move, I'll get it for you..."
                                play sound "Sounds/gasping.mp3"
                                if (blacktop04 == True):
                                    scene nerdy05black with dissolve
                                else:
                                    scene nerdy05 with dissolve
                                $ renpy.pause(1.0, hard=True)
                                ne "There you are... Sorry, I need to go, my panties are all wet!"
                                p "Err, sure... Thanks... See you around..."
                                if (blacktop04 == True):
                                    scene nerdy06black with dissolve
                                else:
                                    scene nerdy06 with dissolve
                                p "Ah, there's a picture of the \"Bostiboobicus Gigantus\". It says it stinks of rotten milk..."
                                p "...Because there's a putrid white liquid that oozes from its flower tip... I see, interesting..."
                                $ plantknowledge = True
                                jump LibraryChoiceDay04
                    "First, tell me where the section on native plants is...":
                        ne "It's behind you. Don't move, I'll get that book for you..."
                        play sound "Sounds/gasping.mp3"
                        if (blacktop04 == True):
                            scene nerdy05black with dissolve
                        else:
                            scene nerdy05 with dissolve
                        $ renpy.pause(1.0, hard=True)
                        ne "There you are... Sorry, I need to go, my panties are all wet!"
                        p "Err, sure... Thanks... See you around..."
                        if (blacktop04 == True):
                            scene nerdy06black with dissolve
                        else:
                            scene nerdy06 with dissolve 
                        p "Ah, there's a picture of the \"Bostiboobicus Gigantus\". It says it stinks of rotten milk..."
                        p "...Because there's a putrid white liquid that oozes from its flower tip... I see, interesting..."
                        $ plantknowledge = True
                        jump LibraryChoiceDay04
            "First, tell me where the section on native plants is...":
                ne "It's behind you. Don't move, I'll get that book for you..."
                play sound "Sounds/gasping.mp3"
                if (blacktop04 == True):
                    scene nerdy05black with dissolve
                else:
                    scene nerdy05 with dissolve
                $ renpy.pause(1.0, hard=True)
                ne "There you are... Sorry, I need to go, my panties are all wet!"
                p "Err, sure... Thanks... See you around..."
                if (blacktop04 == True):
                    scene nerdy06black with dissolve
                else:
                    scene nerdy06 with dissolve 
                p "Ah, there's a picture of the \"Bostiboobicus Gigantus\". It says it stinks of rotten milk..."
                p "...Because there's a putrid white liquid that oozes from its flower tip... I see, interesting..."
                $ plantknowledge = True
                jump LibraryChoiceDay04                
            "Ah, I see, you're crazy.":
                ne "Oh no, the only boy who ever spoke to me thinks I'm crazy, AAARGH!"
                scene nerdy03 with dissolve
                $ renpy.pause(1.0, hard=True)
                p "Hey, where are you going, come back, you didn't tell me where the section on native plants was!"
                p "Shit...Now I have to go back and ask Maria..."
                jump Library03Day04

label Library04Day04:
scene friedalibrary01day03 with dissolve
$ renpy.pause(1.0, hard=True)
$ spokefriedalibraryday04 = True
p "Hi Frieda, what's up? You seem to be studying hard... Again."
fr "I can think a bit more clearly now with those new clothes... But it's still tough.... I really need an A or my parents vill kill me."
label FriedaChoiceDay04:
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
        jump FriedaChoiceDay04
    "So, Frieda... Looking at my epiclust meter, I see you've reached 10..." if (friedachangedgrade == True) and (friedatoldgrades == True) and (friedafucked == False) and (lust_points[8]>=10):
        scene friedalibrary03day03 with dissolve
        fr "Is that so? Then, ve must have sex, it's the rules..."
        jump FriedaFuckDay04
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
            jump FriedaFuckDay04  
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (lust_points[8] >=8):
                jump FriedaPendulumDay04
            "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[8] >=8):
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump FriedaPheromonesDay04
            "Say she's welcome":
                p "You're welcome. Hopefully, this will lead to a growing relationship between us. Mine is definitely growing right now."
                jump FriedaChoiceDay04
        p "You're welcome. Hopefully, this will lead to a growing relationship between us. Mine is definitely growing right now."
        jump FriedaChoiceDay04
    "I haven't managed to sneak into the principal's office but I'm planning on it..." if (friedahelped == True) and (friedachangedgrade == False) and (friedatoldgrades == False):
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
        jump FriedaChoiceDay04
    "OK, I'll leave you alone to study then...":
        jump Library03Day04

label FriedaPendulumDay04:
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
jump FriedaFuckDay04
    
label FriedaPheromonesDay04:
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
jump FriedaFuckDay04

label FriedaFuckDay04:
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
label FriedaCockRubDay04:
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
        jump FriedaCockRubDay04
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
label FriedaFuckChoiceDay04:
menu:
    "Let her ride you" if (friedaride == False):
        jump FriedaFuckRideDay04
    "Take her up the arse" if (friedaarse == False):
        jump FriedaFuckArseDay04
    "Tell her to finish you off with a blowjob" if (friedaarse == True) and (friedaride == True):
        jump FriedaFuckBlowjobDay04


label FriedaFuckRideDay04:
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
        jump FriedaFuckArseDay04
    "Tell her to finish you off with a blowjob" if (friedaarse == True) and (friedaride == True):
        jump FriedaFuckBlowjobDay04

label FriedaFuckArseDay04:
scene friedafuck10 with dissolve
$ friedaarse = True
$ renpy.pause(1.0, hard=True)
fr "You are stretching my poor little anus zo much! AAAAH!"
p "That's nothing, I'm not even halfway in. Let me stretch it a bit more..."
scene friedafuck10b with dissolve
$ renpy.pause(1.0, hard=True)
p "There. That's better. A solid ten inches of my ramrod up your arse!"
fr "Be caref.."
label FriedaFuckArseDay04b:
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
        jump FriedaFuckArseDay04b        
    "Let her ride you" if (friedaride == False):
        jump FriedaFuckRideDay04
    "Tell her to finish you off with a blowjob" if (friedaarse == True)and (friedaride == True):
        jump FriedaFuckBlowjobDay04

label FriedaFuckBlowjobDay04:
stop music
play music "Sounds/friedaslow.mp3"
show friedafuckslow
show faster
call screen friedafuckslowday04
screen friedafuckslowday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("FriedaFuckFastDay04")

label FriedaFuckFastDay04:
hide faster
play music "Sounds/friedafast.mp3"
show friedafuckfast
show cum
call screen friedafuckfastday04
screen friedafuckfastday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FriedaFuckCumDay04")

label FriedaFuckCumDay04:
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
$ backdoor += 1
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ friedafucked = True
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
p "Yes, that is probably a good idea. I mean, some people DO use the library sometimes."
if (friedajosewin == False):
    $ friedawin = True
    p "(José is going to be mightily pissed off when he gets the pic I'm sending him...)"
$ fuckedschoolgirlday04 = True
$ hour += 1
jump LibraryChoiceDay04

label LibraryPendulumDay04:
if (blacktop04 == True):
    scene ryanlibraryinternetblack with dissolve
else:
    scene ryanlibraryinternet with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/keyboard.ogg"
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump LibraryChoiceDay04

label LibraryGothDay04:
if (blacktop04 == True):
    scene ryanreadinglibraryblack with dissolve
else:
    scene ryanreadinglibraryinternet with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump LibraryChoiceDay04


label BurbsDay04:
stop music
if (hour == 7):
    p "Time to jog back home, I think I might have missed breakfast."
    jump Breakfast02jDay04

scene burbsday with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_49
    $ lustaddedB = 1
    call Challenger from _call_Challenger_50
    $ challengercalls += 2

if (hour == 20):
    p "Just in time to head back home for dinner!"
    jump DinnerDay04
if (hour == 18 or hour == 19):
    p "I don't have time for much at this time of the day... Dinner is at 8pm."
    jump BurbsChoiceDay04

p "The burbs are so quiet during the day. I guess everyone is at work. Except me!"

label BurbsChoiceDay04:
if (hour == 20):
    p "Damn, it's 8pm already, I should really head back home for dinner..."
    jump DinnerDay04
p "What should I do?"
menu:
    "Explore the Burbs" if (discoverstore == False):
        jump BurbsExploreDay04
    "Go to the convenience store" if (discoverstore == True) and (evictedfromstore == False):
        jump StoreDay04
    "Go back home":
        jump HomeDay04
    "Go to Debby's house" if (auntdebbyseen04 == False):
        jump AuntDebbyHouseDay04
    "Take the bus to the beach" if (hour <= 17):
        $ busbeach = True
        jump BusDriveDay04
    "Take the bus heading downtown" if (hour <= 17):
        $ bustown = True
        jump BusDriveDay04
    "Go to the school" if (hour <= 15):
        scene lockerempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump SchoolChoiceDay04
    "Take the shortcut to the Beach" if (hour <= 19) and (discoverclinic == True):
        stop music
        scene clinicentrance with dissolve
        play music "Sounds/gardensound.mp3"
        $ renpy.pause(1.0, hard=True)   
        p "I wish I had discovered this shortcut earlier, it is really helpful in cutting my travel time between the burbs and the beach..."
        jump Beach01Day04

label BurbsExploreDay04:
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
jump BurbsChoiceDay04

label BusDriveDay04:
stop music
scene busdrive with dissolve
play music "Sounds/busidle.mp3"
$ renpy.pause(1.0, hard=True)
p "Here's the bus. Let's get on."

label BusDriveDayb04:
if (shadyguyseen04 == True):
    jump BusEndDay04

scene shadybus01 with dissolve
$ shadyguyseen04 = True
$ renpy.pause(1.0, hard=True)
p "This guy looks shady..."
sg "Oy, who you're looking at?"
p "Are you talking to me? Are you talking to me?"
scene shadybus02 with dissolve
$ renpy.pause(1.0, hard=True)
sg "You wanna taste some blade boy?"
menu:
    "Oh, sorry sir, my apologies. I'll be on my merry way.":
        sg "You're lucky I'm getting off at the next stop boy!"
        jump EscapeShadyGuyDay04
    "You don't scare me, I'm da man, I'm DA MAN!":
        jump FightShadyGuyDay04

label EscapeShadyGuyDay04:
$ escapeshadyguy = True
scene shadyguyleft with dissolve
$ renpy.pause(1.0, hard=True)
p "Phew, that was close, that guy's crazy!"
"The man leaves at the next stop. He seems to have dropped something."
window hide
show maddyphoto with dissolve
$ renpy.pause(1.0, hard=True)
p "OMG, it's a picture of Maddy! The bastard must have kidnapped her!"
p "Damn, I don't know where he went or where that picture was taken... Next time I meet him, I should confront him."
jump BusEndDay04

label EscapeShadyGuyDay04b:
$ escapeshadyguy = True
scene shadyguyleft with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, that hurts! I can't run after him, I can barely breathe..."
"The man leaves at the next stop. He seems to have dropped something."
window hide
show maddyphoto with dissolve
$ renpy.pause(1.0, hard=True)
p "OMG, it's a picture of Maddy! The bastard must have kidnapped her!"
p "Next time I cross paths with this cunt, I'd better be stronger and prepared."
$ maddylead = True
jump BusEndDay04

label FightShadyGuyDay04:
scene shadybus03 with dissolve
$ renpy.pause(1.0, hard=True)
sg "You asked for it! Get ready to BLEED!"
if (knife == True) and (blacktop04 == False):
    scene shadybus04whiteknife with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Ah, ah, you didn't see that coming did you, shady guy?"
    sg "Pff! A Japanese army knife? Look at my blade! It's as big as Rambo's! Now enough talk, let's FIGHT!"
    if (strength >=8):
        play sound "Sounds/punch.mp3"
        scene shadyguyfall with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Take that you scumbag!"
        "You deliver a mighty kick to your foe who falls unconscious to the ground."
        jump ShadyGuyDownDay04
    jump ShadyGuyLoseDay04

if (knife == True) and (blacktop04 == True):
    scene shadybus04blackknife with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Ah, ah, you didn't see that coming did you, shady guy?"
    sg "Pff! A Japanese army knife? Look at my blade! It's as big as Rambo's! Now enough talk, let's FIGHT!"
    if (strength >=8):
        play sound "Sounds/punch.mp3"
        scene shadyguyfallblack with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Take that you scumbag!"
        "You deliver a mighty kick to your foe who falls unconscious to the ground."
        jump ShadyGuyDownDay04
    jump ShadyGuyLoseDay04

if (knife == False) and (blacktop04 == False):
    scene shadybus04white with dissolve
    $ renpy.pause(1.0, hard=True)
    p "(If only I had a knife like him...)"
    sg "Enough thinking to yourself in your head, let's FIGHT!"
    if (strength >=10):
        play sound "Sounds/punch.mp3"
        scene shadyguyfall with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Take that you scumbag!"
        "You deliver a mighty kick to your foe who falls unconscious to the ground."
        jump ShadyGuyDownDay04
    jump ShadyGuyLoseDay04

if (knife == False) and (blacktop04 == True):
    scene shadybus04black with dissolve
    $ renpy.pause(1.0, hard=True)
    p "(If only I had a knife like him...)"
    sg "Enough thinking to yourself in your head, let's FIGHT!"
    
    if (strength >=10):
        play sound "Sounds/punch.mp3"
        scene shadyguyfallblack with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Take that you scumbag!"
        "You deliver a mighty kick to your foe who falls unconscious to the ground."
        jump ShadyGuyDownDay04
    jump ShadyGuyLoseDay04

label ShadyGuyLoseDay04:
if (blacktop04 == True):
    scene shadyguyinjuredblack with dissolve
if (blacktop04 == False):
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
jump EscapeShadyGuyDay04b

label ShadyGuyDownDay04:
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
jump BusEndDay04

label BusEndDay04:
if (busbeach == True):
    $ hour += 1
    $ busbeach = False
    jump Beach01Day04
elif (bustown == True):
    $ hour += 1
    $ bustown = False
    jump DowntownDay04
elif (bushome == True):
    $ hour += 1
    $ bushome = False
    jump BurbsDay04

label StoreDay04:
stop music
scene store01 with dissolve
play music "Sounds/storemusic.mp3"
$ renpy.pause(1.0, hard=True)

label StoreClerkDay04:
scene store01
if ((catchfrancine == True) or (catchbeer == True)) and (hour == 17):
    fa "Are you ready to start another shift today?"
    menu:
        "Yes, I'm ready.":
            jump StoreSecondWork01Day04
        "No, I'm too busy right now.":
            fa "Well, that's unfortunate... I could have really used your help again today..."
            jump ClerkChoiceDay04
    
if (storework == True) and (hour == 17) and (catchfrancine == False) and (catchbeer == False):
    fa "Are you ready to start your shift today?"
    menu:
        "Yes, I'm ready.":
            jump StoreWork01Day04
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
            jump ClerkChoiceDay04
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
    jump BurbsChoiceDay04   
elif (hour == 19):
    fa "Welcome to \"Seven Square\", your local shop that's opened from seven till... seven."
    fa "I'm sorry, but it is seven o'clock. The second seven. So we are closing."
    fa "Please come back tomorrow to your local convenience store \"Seven Square\" between 7am and... 7pm!"
    jump BurbsDay04    
else:
    fa "Welcome to \"Seven Square\", your local shop that's opened from seven till... seven."

label ClerkChoiceDay04:
if (catchfrancine == True) or (catchbeer == True):
    fa "So, how may I help you?"
else:
    fa "My name is Francine, how may I help you?"
menu:
    "Chat with her":
        jump StoreChatDay04 
    "Buy something":
        jump StoreBuyDay04
    "Leave":
        jump BurbsDay04

label StoreChatDay04:
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
                        jump StoreNoDealDay04
                    "It's a deal!":
                        $ halfprice = True
                        jump StoreDealDay04
            "It's a deal!":
                jump StoreDealDay04
    "Just thought I’d check a few things out, you being one of them...":
        scene store03
        fa "I can barely contain my laughter."
        jump ClerkChoiceDay04
    
label StoreDealDay04:
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
            jump StoreBuyDay04
        "No thanks.":
            fa "Alright, see you another day then."
            jump BurbsDay04
jump StoreClerkDay04

label StoreWork01Day04:
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
        jump CatchFrancineDay04
    "Catch the beer":
        jump CatchBeerDay04

label CatchFrancineDay04:
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
jump StoreTeagan01Day04

label CatchBeerDay04:
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
jump StoreTeagan01Day04

label StoreTeagan01Day04:
play music "Sounds/storemusic.mp3"
scene storeteagan01 with dissolve
$ renpy.pause(1.0, hard=True)
p "There's Miss Cocque doing her shopping, she hasn't noticed me yet."
menu:
    "Hide and hope she doesn't see you":
        jump StoreHideDay04
    "Greet her and ask her if you can help with anything":
        jump StoreTeagan02Day04

label StoreHideDay04:
scene storeteaganhide with dissolve
$ renpy.pause(1.0, hard=True)
p "Phew, she almost saw me but I'm think I managed to avoid her... And she's on her way out."
p "At the same time, watching that arse... Maybe I should have greeted her..."
p "Oh well, only a few more minutes of hard labour and my shift ends. I'll just stack these bubble gums once she's out of the store."
jump StoreShiftEndDay04

label StoreTeagan02Day04:
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
            jump StoreParkDay04
    "Sure Miss Cocque, let me help you with these heavy items, it'll be easy for me!":
        jump StoreTeagan05Day04

label StoreTeagan05Day04:
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

label StoreParkDay04:
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
        jump StoreShiftEndDay04
    "I don't know, I don't think I'll have time for that extra job...":
        t "Uh... OK, just think about it... Have a nice evening [name], I'll see you tomorrow at class, 9am sharp!"
        jump StoreShiftEndDay04

label StoreSecondWork01Day04:
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
        jump CleanStorageDay04
    "Build a pole-dancing platform with all the shit lying around" if (quentintipfrancine == True):
        jump PoleDancingDay04

label CleanStorageDay04:
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
jump StoreShiftEndSecondDay04

label PoleDancingDay04:
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
        jump PoleDance01Day04
    "Me no parl-ay Froggie. Sorry.":
        re "But you are supposed to! All shops must cater to French-speakers on Veri-Bosti island, it's the law!"
        p "Well clearly you speak English. So what are you moaning about?"
        re "Humpf, yes I do, but it is not my first language. I am looking for.. how do you say?... Washing powder?"
        p "Ah, let me show you, we have all the big brands and also the cheap ones that are exactly the same shit."
        jump StoreCustomerDay04
    "Vou-lay-vous couch-ay avec moi ce soir?":
        re "Hein? Mais ça va pas la tête? C'est un scandale!"
        p "Calm down now lady, I was just kidding... Why don't we speak English for a change, you speak English right?"
        re "Humpf, yes I do, but it is not my first language. I am looking for.. how do you say?... Washing powder?"
        p "Ah, let me show you, we have all the big brands and also the cheap ones that are exactly the same shit."
        jump StoreCustomerDay04

label StoreCustomerDay04:
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
        jump PoleDance01Day04
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
        
        jump PoleDance01Day04

label PoleDance01Day04:
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
            $ invitedfrancine = True
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
    jump BurbsChoice04

label StoreShiftEndSecondDay04:
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
jump HalfPriceDay04

label StoreShiftEndDay04:
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
    jump StoreShiftEnd02Day04
if (catchfrancine == True):
    fa "Here's five dollars for your hard work [name]! I hope you come back again to work here. Goodbye."
    $ money += 5
    p "Yeah, maybe, I'll see..."
    jump StoreShiftEnd02Day04
    
label StoreShiftEnd02Day04:
if (halfprice == True):
    p "Hey, I can buy something half-price remember?"
    fa "Ah yes, silly me for not remembering..."
    jump HalfPriceDay04

label HalfPriceDay04:
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
        jump StoreShiftEnd03Day04
        
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
        jump StoreShiftEnd03Day04

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
        jump StoreShiftEnd03Day04

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
        jump StoreShiftEnd03Day04
    
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
        jump StoreShiftEnd03Day04

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
        jump StoreShiftEnd03Day04
    
    "Nothing actually...":
        jump StoreShiftEnd03Day04
        
label StoreShiftEnd03Day04:
scene store01 with dissolve
fa "That's it, you bought your item, now I have to close the store... Come back anytime to \"Seven Square\", your local shop that's opened from seven till... seven."
jump BurbsDay04
    
label StoreNoDealDay04:
scene store03 with dissolve
fa "That's a pity... Think about it, the job offer will be on all week."
jump StoreClerkDay04

label StoreBuyDay04:
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
        jump ClerkChoiceDay04

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
        jump ClerkChoiceDay04

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
        jump ClerkChoiceDay04

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
        jump ClerkChoiceDay04
    
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
        jump ClerkChoiceDay04

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
        jump ClerkChoiceDay04
    "Nothing actually...":
        jump ClerkChoiceDay04

label AuntDebbyHouseDay04:
stop music
if (blacktop04 == True):
    scene debbyentranceblack with dissolve
else:
    scene debbyentrance with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/debbydoorbell.mp3"
p "Maybe I could ask Debby if I could wash her car for her and get a bit of money..."
if (hour >=18):
    scene debbyhouse01 with dissolve
    d "Well, look who came to visit me. What brings you here [name]?"
    $ auntdebbyseen04 = True
    if (debbycarunwashed == True):
        scene debbyhouseangry with dissolve
        d "Hang on, now I remember... I paid you 5 bucks to wash my car yesterday and it's still as filthy as ever, but the five bucks are gone!"
        d "Are you trying to rip me off? Give me back my five bucks [name]!"
        $ money -= 5
        $ lust_points[5] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.4 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        $ debbycarunwashed = False
        d "That's better... So what brings you here?"
        scene debbyhouse01 with dissolve
    jump AuntDebbyHouseMenuDay04
if (hour <=17):
    p "She doesn't seem to be in at the moment."
    jump BurbsDay04

label AuntDebbyHouseMenuDay04:
menu:
    "I wanted to see you model some more bikinis for me." if (debbybikini04 == False) and (debbybikini == False) and (debbybikini03 == False):
        d "Well, that's bold of you young man!"
        d "But you're in luck, I just received a new swimsuit which I haven't tested yet... Come on in..."
        $ debbybikini04 = True
        jump AuntDebbyInsideDay04
    "I was wondering if your car needed washing?" if (debbycarwashed == False) or (debbycarunwashed == False):
        d "Oh, I see, you want to make a bit of money do ya? Fair enough."
        d "I'll give you five dollars... But I want to be able to watch and you have to be bare-chested...(wink)"
        menu:
            "It's a deal!":
                jump AuntCarWashDay04
            "Five dollars? It will take me at least one hour to wash it... Not interested.":
                d "Your choice mr I'm-too-important-to-wash-a-car-for-five-dollars!..."
                d "Anything else?"
                jump AuntDebbyHouseMenuDay04
    "Nancy needs some...sugar." if (debbysugar == False) and (debbysugar03 == False) and (debbysugar04 == False):
        d "Oh, alright, come on in then."
        $ debbysugar04 = True
        jump AuntDebbyInsideDay04

label AuntDebbyNewBikiniDay04:
d "Where should I model this new bikini for you?"
menu:
    "Why not in your bedroom?":
        d "No, that's my special place. You can't go there ever, you hear me?"
        p "Alright, alright. How about the backyard then?"
        d "Yes, that will do, go and sit outside and wait for me, I'll be back in a minute."
        d "Get down to your underwear, I might need you... to do something for me."
        p "(Well, that's an unusual request... I hope it leads to something...)"
        jump DebbyHouseBikini01Day04
    "The outside light will better reveal every detail of your hot bo...swimsuit.":
        d "Yes, you're right, you are a fine connoisseur. Go and sit outside then, I'll be back in a sec." 
        d "Get down to your underwear, I might need you... to do something for me."
        p "(Well, that's an unusual request... I hope it leads to something...)"
        jump DebbyHouseBikini01Day04

label AuntCarWashDay04:
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
            jump DinnerDay04
        jump AuntDebbyMoneyDay04
    "Stop and sneak inside to get the money anyway":
        $ debbycarunwashed = True
        jump AuntDebbyMoneyDay04
    
label AuntDebbyInsideDay04:
scene debbyhouse02 with dissolve    
$ renpy.pause(1.0, hard=True)
play sound "Sounds/footsteps.mp3"
d "This way to the living room..."
p "Wow, Debby has such a huge house... And such a tight ass..."
jump AuntDebbyLivingRoomDay04

label AuntDebbyLivingRoomDay04:
scene debbyhouse03 with dissolve    
$ renpy.pause(1.0, hard=True)
if (debbysugar04 == True):
    d "I'll go and fetch some sugar from the kitchen. You can wait for me here. But don't touch anything, these sculptures are worth thousands of dollars!"
    p "Sure Debby. I won't move."
    play sound "Sounds/debbydooropenclose.mp3"
    jump DebbySnoopDay04
if (debbybikini04 == True):
    jump AuntDebbyNewBikiniDay04
    
label DebbySnoopDay04:
scene debbysnooping with dissolve    
$ renpy.pause(1.0, hard=True)
menu:
    "Snoop around":
        jump DebbySnoopingDay04
    "Wait patiently for Debby to return":
        jump DebbySugarDay04

label DebbySnoopingDay04:
play music "Sounds/snooping.mp3"
$ d2rolldebby=renpy.random.randint(0, 1)
if (d2rolldebby == 0):
    call screen debbysnoop01Day04
if (d2rolldebby == 1):
    call screen debbysnoop02Day04
$ renpy.pause(1.0, hard=True)
stop music
"You were too slow and didn't find anything. Debby is coming back..."
jump DebbySugarDay04

label FoundAudaciousPassDay04:
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

label DebbySugarDay04:
scene debbyhouse04 with dissolve    
$ renpy.pause(1.0, hard=True)
d "Here you are. I hope your landlady does some nice cakes with it! Tell her to invite me when she's done."
p "Thanks Debby... I'll be sure to let her know..."
$ hour += 1
jump BurbsDay04
    
label DebbyHouseBikini01Day04:
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
    jump DebbyBikiniPrefuck01
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
jump BurbsDay04

label DebbyBikiniPrefuck01:
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
jump DebbyFuckChoiceDay04

label AuntDebbyMoneyDay04:
stop music
scene debbymoney with dissolve    
$ renpy.pause(1.0, hard=True)
p "Here's the money."
play sound "Sounds/auntviolent.mp3"
p "What's that sound? It seems to be coming from upstairs where Debby's bedroom is..."
menu:
    "Go investigate":
        jump AuntDebbyStairsDay04
    "Take the money and leave":
        $ money += 5
        jump BurbsDay04

label AuntDebbyStairsDay04:
scene debbystairway with dissolve
play sound "Sounds/auntwhip01.mp3"
$ renpy.pause(1.0, hard=True)
p "Jeezus, this sounds violent, I'd better hurry up!"

label AuntDebbyBedroomDay04:
scene debbybedroom01 with dissolve    
play sound "Sounds/auntwhip02.mp3"
$ renpy.pause(1.0, hard=True)
p "WTF? That masked naked guy is brutalizing Debby!"
menu:
    "Leave quietly and take the money on the way out":
        $ money += 5 
        jump BurbsDay04
    "Get involved":
        p "Hey you, stop this immediately or...I swear I'll beat you up!"
        jump AuntDebbyBondage01Day04

label AuntDebbyBondage01Day04:
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
        jump BurbsDay04
    "You deserve a good cock slapping, get on your knees bitch!":
        d "Wh...what?..But..."
        p "You heard me. Remove your mask and ON YOUR KNEES BITCH!"
        d "Y..yes master..."        
        jump DebbyCockSlapDay04
    "OK, I didn't see a thing. I won't say a word. I'll just erase everything from my memory.":
        d "Oh Thank you [name], I owe you big time. Here's your twenty bucks. Now get out of here and don't say a word to anyone!"
        $ money += 20
        jump BurbsDay04

label DebbyCockSlapDay04:
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
        d "Here's 10 dollars, don't say a word to your mom and we might do something like that again (wink...)."
        p "F...fuck! I'm so hard and I can't even cum!"
        if (debbycarunwashed == True):
            $ hour +=1
        jump BurbsDay04
    "Now I'm gonna cock-slap that tight arse of yours filthy slut!":
        d "Oooh, yes master, I deserve it..."
        jump ArseCockSlapDay04

label ArseCockSlapDay04:
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
    jump DebbyFuckChoiceDay04
d "It's enough for now [name], here's 10 dollars, don't say a word to your mom and we might do something like that again (wink...)."
menu:
    "Sure, nice doing business with you Debby...":
        $ money += 10
        d "I feel so...cheap...so dirty...I love it, thank you [name]...Just go now..."
        p "I feel like...10 dollars worth apparently. See you another time Debby!"
        if (debbycarunwashed == True):
            $ hour +=1
        jump BurbsDay04
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
        jump BurbsDay04

label DebbyFuckChoiceDay04:
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
            jump DebbyFuckChoiceDay04b
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
    jump BurbsDay04        
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
    jump BurbsDay04        

label DebbyFuckChoiceDay04b:
scene debbybed01 with dissolve
menu:
    "Let me titfuck your massive tits filthy slut!" if (debbytitfuck == False):
        jump DebbyTitfuckDay04
    "On the bed on your back slave!" if (debbyback == False):
        jump DebbyBackFuckDay04
    "I want to lick your hard nipples and maul your tits!":
        jump DebbyNippleDay04
    "A cheap whore like you deserves a good pussy-pounding!" if (debbyfrontfuck == False):
        jump DebbyFrontFuckDay04
    "Be a good bitch and get on all fours for this horny dog!" if (debbydoggy01 == False):
        jump DebbyDoggyFuckDay04        
    "Time to finish me off slave!" if (debbydoggy01 == True) and (debbyfrontfuck == True) and (debbyback == True) and (debbytitfuck == True):
        jump DebbyBedMovie04
    
label DebbyDoggyFuckDay04:
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
label DebbyDoggyFuckDay04b:
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
        jump DebbyDoggyFuckDay04b
    "Move on":
        p "You did good slave, it's now time to move on to something else..."
        jump DebbyFuckChoiceDay04b
            
label DebbyTitfuckDay04:
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
label DebbyTitFuckDay04b:
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
        jump DebbyTitFuckDay04b
    "Move on":
        p "You did good slave, it's now time to move on to something else..."
        jump DebbyFuckChoiceDay04b

label DebbyBackFuckDay04:
$ debbyback = True
scene debbyback01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Offer your gaping slut-hole to my massive teenage cock slave!"
d "My filthy hole belongs to you Master... Do as you please with it!"
label DebbyBackFuckDay04b:
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
        jump DebbyBackFuckDay04b
    "Move on":
        p "I've punished your dirty hole enough for the moment slave... I'm giving you a respite..."
        d "Thank you Master, I am not worthy of such generosity..."
        jump DebbyFuckChoiceDay04b

label DebbyNippleDay04:
scene debbybed02 with dissolve
play sound "Sounds/sucking.mp3"
$ renpy.pause(2.0, hard=True)
d "Ooh, you suck on my nipples ssoo good! Maul my tits Master!"
p "They look red and erect now, it's time for something else slave..."
jump DebbyFuckChoiceDay04b

label DebbyFrontFuckDay04:
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
label DebbyFrontFuckDay04b:
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
        jump DebbyFrontFuckDay04b
    "Move on":
        p "Your dirty hole is creaming all over the place, let's switch position whore!"
        jump DebbyFuckChoiceDay04b

label DebbyBedMovie04:
scene debbyballs with dissolve
$ renpy.pause(1.0, hard=True)
d "I can feel your balls are ready to unleash their massive store of pent-up young and yummy cum Master!"
p "Fuck yeah! I'm close to bursting a nut, finish me off slave!"
play music "Sounds/debbybedslow.mp3"
show debbybedslow
show faster
call screen debbyfuckslowday04
screen debbyfuckslowday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("DebbyFuckFastDay04")
label DebbyFuckFastDay04:
hide faster
stop music
play music "Sounds/debbybedfast.mp3"
show debbybedfast
show cum
call screen debbyfuckfastday04
screen debbyfuckfastday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("DebbyFuckCumDay04")

label DebbyFuckCumDay04:
hide debbybedfast
hide debbybedslow
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
if (hour == 20):
    p "I'd better get going, it's dinner time and I'm late!"
    d "Don't tell anyone about this, okay?"
    if (debbyjosewin == True):
        p "Umpf, coming from a whore who fucked José, that's grand!"
        scene debbybedcum03b
        d "What? But... How do you know? That little shit!"
        p "That's right, he's a fucking douchebag and you screwed him! That makes YOU a FILTHY WHORE!"
        d "I'm so ashamed of myself... I'm just a dirty slut... You'd better go home and leave your whore of a slave alone..."
        jump DinnerDay04
    menu:
        "Fine, but don't you dare get anywhere near that arsehole José, you hear me slave? (Cockblock José)":
            d "Yes, Master."
            $ josedebbycockblocked = True
            jump DinnerDay04
        "Alright, but I want 5 bucks for my silence...SLAVE!":
            d "There you are, you greedy little pig! Now get out of my house!"
            $ money += 5
            jump DinnerDay04

if (hour <= 19):
    p "I'd better get going now Debby.... You drained my nuts..."
    d "Don't tell anyone about this, okay?"
    if (debbyjosewin == True):
        p "Umpf, coming from a whore who fucked José, that's grand!"
        scene debbybedcum02b
        d "What? But... How do you know? That little shit!"
        p "That's right, he's a fucking douchebag and you screwed him! That makes YOU a FILTHY WHORE!"
        d "I'm so ashamed of myself... I'm just a dirty slut... You'd better go home and leave your whore of a slave alone..."
        jump BurbsDay04
    menu:
        "Fine, but don't you dare get anywhere near that arsehole José, you hear me slave? (Cockblock José)":
            d "Yes, Master."
            $ josedebbycockblocked = True
            jump BurbsDay04
        "Alright, but I want 5 bucks for my silence...SLAVE!":
            d "There you are, you greedy little pig! Now get out of my house!"
            $ money += 5
            jump BurbsDay04

label HomeDay04:
$ momroomseen04  = False
stop music
scene livingroom01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah, home sweet home..."

if (hour == 17 or hour == 18) and (katephotoplanned04 == True) and (katephotoshoot == False) and (katephotoshootleft04 == False):
    p "I think Kate should arrive anytime now for our little photoshoot session... I hope it gets steamy fast..."
    jump KateShoot01Day04  
    
if (hour == 20):
    p "Just in time for dinner..."
    jump DinnerDay04

label Home02Day04:
stop music
scene livingroom01 with dissolve
if (hour == 20):
    p "Time for dinner..."
    jump DinnerDay04

p "What should I do?"
menu:
    "Go to my room":
       jump RyanBedroomDay04
    "Go to the bathroom":
        jump BathRoomDay04
    "Go to mom's room" if (momroomseen04 == False):
        jump MomRoomDay04
    "Go to the swimming pool" if (locswimmingpool == False):
        jump SwimmingPoolDay04
    "Leave the house":
        jump BurbsDay04

label SwimmingPoolDay04:
$ locswimmingpool = True
if (hour <= 18):
    scene poolempty with dissolve
    play music "Sounds/gardensound.mp3"
    $ renpy.pause(1.0, hard=True)
    p "There's no one around, I can't even, like, perv on Nancy or Nikki in a bikini right now. SAD."
    $ locswimmingpool = False
    jump Home02Day04
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
    jump DinnerDay04

label RyanBedroomDay04:
stop music
$ locroom = True
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
if (hour >= 20):
    $ hour = 20
    p "Oh, it's time for dinner, I'd better hurry downstairs..."
    jump DinnerDay04
if (hour == 17 or hour == 18) and (katephotoplanned04 == True) and (katephotoshoot04 == False) and (katephotoshootleft04 == False):
    p "I think Kate should arrive anytime now for our little photoshoot session... I hope it gets steamy fast..."
    jump KateShoot01Day04  

p "What to do, what to do..."
menu:
    "Turn the computer on":
        jump ComputerDay04
    "Do some heavy bodybuilding (+2hrs)" if (hour <= 18):
        if (workout == True):
            "You already trained today."
            jump RyanBedroomDay04
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
            jump RyanBedroomDay04        
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump RyanBedroomDay04
    "Go the living room":
        jump Home02Day04
    "Go to the bathroom" if (showerseen04 == False):
        jump BathRoomDay04
    "Go to mom's room" if (momroomseen04 == False):
        jump MomRoomDay04
    "Read the book Laura gave you (+1hr)" if (book == True) and (bookread == False):
        jump RyanReadingDay04

label RyanReadingDay04:
scene ryanreading with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump RyanBedroomDay04

label ComputerDay04:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label Computer02Day04:
scene ryancomputerday
menu:
    "Check the map":
        jump MapDay04
    "Check the stats":
        jump StatsDay04
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump Computer02Day04
    "Learn how to use the pendulum" if (pendulum == True) and (pendulumactive ==False):
        jump CompPendulumDay04
    "Play a smutty game (+1hr)":
        jump CompGameDay04
    "Turn the computer off":
        jump RyanBedroomDay04

label CompPendulumDay04:
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump Computer02Day04

label MapDay04:
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
p "This shows all the places I know so far on Veri-Bosti Island..."
show screen statsbackground
show screen inventorybutton
show screen calendar
jump Computer02Day04

label StatsDay04:
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
jump Computer02Day04

label CompGameDay04:
scene ryancomputergameday
$ renpy.pause(1.0, hard=True)
p "This game is tough. My fingers hurt like hell from so much clicking..."
$ hour += 1
jump Computer02Day04

label MomRoomDay04:
scene nancybedroomday with dissolve
$ renpy.pause(1.0, hard=True)
$ momroomseen04 = True
p "Nancy's room is so clean and tidy. Not like mine."
menu:
    "Snoop around" if (dildo == False):
        jump MomBedroomSnoopDay04  
    "Go back to my room":
        jump RyanBedroomDay04
    "Put the dildo back in its drawer" if (dildo == True):
        show dildo
        show square
        play sound "Sounds/lost.mp3"
        "You relinquish a giant black dildo. Yes, that's right, \"relinquish\". Look it up in the dictionary."
        hide square
        hide dildo
        $ dildo = False
        jump RyanBedroomDay04

label MomBedroomSnoopDay04:
p "There might be an interesting item hidden somewhere... Time to snoop around..."
p "But I have a limited amount of time to look for it, mom might come back from work anytime for all I know."
play music "Sounds/snooping.mp3"
call screen mombedroomsnoopDay04
stop music
"You were too slow and didn't find anything."
jump RyanBedroomDay04

label FoundDildoDay04:
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
jump RyanBedroomDay04

label BathRoomDay04:
stop music
if (hour <= 17):
    jump EmptyBathRoomDay04
if (hour == 18) or (hour == 19):
    jump MomShowerDay04

label EmptyBathRoomDay04:
scene bathroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "No one is around right now, I could take a shower if I wanted to."
menu:
    "Take a shower":
        jump ShowerDay04
    "Leave":
        jump RyanBedroomDay04

label ShowerDay04:

scene shower with dissolve
stop music
play music "Sounds/shower.mp3"
$ renpy.pause(1.0, hard=True)
p "That's nice and relaxing..."
if (stamina <= 4) and (showerseen04 == False):
    window hide
    $ stamina += 1
    show stamina01:
        xalign 0.4 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide stamina01
$ showerseen04 = True
jump RyanBedroomDay04

label MomShowerDay04:
play music "Sounds/shower.mp3"
$ locroom = False
scene bathroomdoorclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "Someone's taking a shower..."
menu:
    "Use lubricant on the door hinges" if (wd69 == True) and (squeakfixed == False):
        "The door should not squeak anymore."
        $ squeakfixed = True
        jump MomShowerDay04        
    "Have a peek":
        jump MomPeekBathroomDay04
    "Leave":
        jump RyanBedroomDay04

label MomPeekBathroomDay04:
if (squeakfixed == False):
    play sound "Sounds/doorsqueak.mp3"
    scene bathroomdooropen with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Shit, the door is squeaking..."
    m "I'm in the shower sweetie, don't get in!"
    p "Ah, sorry Nancy...I'm leaving..."
    p "Damn, I should try and find a way of stopping that door from squeaking if I want to spy on Nancy or Nikki in the shower like every other MC..."
    jump RyanBedroomDay04
if (squeakfixed == True):
    scene nancyshower01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Cool, she didn't hear me come in, I can see her naked in the shower now..."
    p "Fuck yeah, look at those huge titties... How I would love to rub my pud between them..."
menu:
        "Watch a little longer...":
            jump MomShower02Day04
        "Leave before she turns round and catches me":
            jump RyanBedroomDay04
    
label MomShower02Day04:
if (momshowerpeep == False):
    $ peeping += 1
$ momshowerpeep = True
scene nancyshower02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, her arse was made for fucking a great big cock. MY giant cock!"
menu:
        "Watch a little longer still...":
            jump MomShower03Day04
        "Leave before she turns round and catches me":
            jump RyanBedroomDay04
 
label MomShower03Day04:
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
jump RyanBedroomDay04

label KateShoot01Day04:
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
    $ katephotoshootleft04 = True
    scene livingroom01 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Home02Day04

if (camera == True):
    p "Hi Kate, alright, everything is set up and we are ready to roll...the roll."
    scene katehouse03 with dissolve
    $ renpy.pause(1.0, hard=True)
    k "Oooh, I'm so excited! I'm gonna get to see myself in a bikini!"
    p "Yeah, that's right, the wonders of modern technology... Why don't you change into your first outfit and come by the pool, I'll be waiting for you."
    jump KateShoot02Day04

label KateShoot02Day04:
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
$ katephotoshoot04 = True

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
window hide
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
    jump RyanBedroomDay04

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
        jump KateBehindDay04
    "Push her down and place the head near her pussy":
        jump KatePussyDay04
    "Push her down and stick your rod between her tits":
        jump KateTitsDay04

label KateBehindDay04:
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
label KateBehindDay04b:
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
        jump KateBehindDay04b
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
        jump KatePussyDay04
    "Push her down and stick your rod between her tits" if (katetits == False):
        jump KateTitsDay04
    "Lift her up and fuck her sweet hole" if (katelegs == True) and (katepussy == True) and (katetits == True):
        jump KateLiftDay04

label KatePussyDay04:
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
label KatePussyDay04b:
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
        jump KatePussyDay04b
    "Stick your pud between her legs from behind" if (katelegs == False):
        jump KateBehindDay04
    "Push her down and stick your rod between her tits" if (katetits == False):
        jump KateTitsDay04
    "Lift her up and fuck her sweet hole" if (katelegs == True) and (katepussy == True) and (katetits == True):
        jump KateLiftDay04

label KateTitsDay04:
scene katepool20 with dissolve
$ katetits = True
$ renpy.pause(1.0, hard=True)
p "I think those big jugs of yours are a perfect match for my massive erection!"
k "Uuhh, oooh, you think so?"
p "For sure, I'm dripping precum all over the place cos they make me so horny!"
k "Oooh, I'm so glad you like them..."
menu:
    "Stick your pud between her legs from behind" if (katelegs == False):
        jump KateBehindDay04
    "Push her down and place the head near her pussy" if (katepussy == False):
        jump KatePussyDay04
    "Lift her up and fuck her sweet hole" if (katelegs == True) and (katepussy == True) and (katetits == True):
        jump KateLiftDay04

label KateLiftDay04:
scene katepool17 with dissolve
$ renpy.pause(1.0, hard=True)
k "Uuhh, what? You're lifting me up on your COCK? God, it's ssooo powerful!"
p "Ready for a wild ride Kate?"

stop music
play music "Sounds/kateslow.mp3"
show katefuckslow
show faster
call screen katefuckscreen04
screen katefuckscreen04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("KateFuckFastDay04")

label KateFuckFastDay04:
stop movie
hide faster
play music "Sounds/kate04.mp3"
show katefuckfast
show cum
call screen katefuckscreen04b
screen katefuckscreen04b:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("KateFuckCumDay04")

label KateFuckCumDay04:
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
$ fuckedschoolgirlday04 = True
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
    jump RyanBedroomDay04    
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
            m "My God, on top of that, you lie to me! That's it, you are GROUNDED [name]! Now get dressed and let go of this poor girl!"
            $ lust_points[16] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.1 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            $ ryangrounded = True
            jump RyanBedroomDay04
        "Ah... Let me introduce you to my new classmate Kate. Kate, my landlady and her daughter.":
            m "Who the hell do you think you're kidding? Get dressed and get this \"Kate\" girl out of here, you are GROUNDED this evening [name]!"
            $ ryangrounded = True
            jump RyanBedroomDay04
        "Well, a man's got to do what a man's got to do, right?":
            m "Not HERE in our garden! Now get dressed both of you, I don't want to see such a lewd display in MY house any longer!"
            jump RyanBedroomDay04

label Beach01Day04:
$ seenbeach04 = True
stop music
play music "Sounds/oceanwaves.mp3"
scene beach with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah! Here's Tini-Wini-Bikini beach, as sunny as always... I should probably head for the beach bar first..."
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_51
    $ lustaddedB = 1
    call Challenger from _call_Challenger_52
    $ challengercalls += 2

label BeachBar01d:
$ beachbarseen04 = True
stop music
play music "Sounds/tropicalmusic.mp3"
scene beachbar01 with dissolve
$ renpy.pause(1.0, hard=True)
bb "Aloha, welcome to Tini-Wini-Bikini Beach bar! Again..."
label BeachBar02d:
scene beachbar01
menu:
    "Chat with her":
        jump ChatBeachBarDay04    
    "Leave":
        jump ExploreBeachDay04

label ChatBeachBarDay04:
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
    p "What's going on today? There seems to be more people than usual."
    scene beachbar01 with dissolve
    bb "We have our Wednesday afternoon \"Wet T-shirt Competition\", that's why... It takes place on the main beach in a few minutes."
    bb "If you're interested in being a member of the jury, you need to pay 5 dollars and I'll write your name down..."
    menu:
        "Pay 5 dollars" if (money >= 5):
            bb "Alright, jury duty for you it is then!"
            $ money -= 5
            $ tshirtjury = True
        "Don't pay":
            bb "Your choice sir. You can still assist if you want of course..."        
    jump BeachBar02d

label ExploreBeachDay04:
stop music
play music "Sounds/oceanwaves.mp3"
if (hour >= 19) and (discoverclinic == False):
    p "It's getting late, I should really take the bus and get home now."
    $ bushome = True
    jump BusBeachHomeDay04
if (hour >= 20) and (discoverclinic == True):
    p "It's getting late, I should really take the shortcut through the clinic to get home in time for dinner..."
    stop music
    scene clinicentrance with dissolve
    play music "Sounds/gardensound.mp3"
    $ renpy.pause(1.0, hard=True)   
    p "I wish I had discovered this shortcut earlier, it is really helpful in cutting my travel time between the burbs and the beach..."
    jump DinnerDay04

p "Hum... Where should I go?"
menu:
    "Go to the beach bar" if (beachbarseen04 == False):
        jump BeachBar01d
    "Walk along the beach" if (walkbeachseen04 == False):
        jump BeachWalkDay04
    "Go to Randy Beach" if (randybeachseen04 == False):
        jump RandyBeachDay04
    "Go to the lifeguard tower" if (lifeguarddiscovered == True):
        jump Lifeguard01Day04
    "Go to the address on the shady guy's card" if (discovercabin == True) and (maddysaved == False):
        jump Cabin01Day04
    "Go to the wet T-shirt competition" if (tshirt == False) and (hour <= 18):
        jump Tshirt01Day04
    "Take the Bus to town" if (hour <= 18):
        $ bustown = True
        jump BusBeachTownDay04
    "Take the Bus back home" if (discoverclinic == False):
        $ bushome = True
        jump BusBeachHomeDay04
    "Take the shortcut back to the Burbs" if (discoverclinic == True):
        stop music
        scene clinicentrance with dissolve
        play music "Sounds/gardensound.mp3"
        $ renpy.pause(1.0, hard=True)   
        p "I wish I had discovered this shortcut earlier, it is really helpful in cutting my travel time between the burbs and the beach..."
        jump BurbsDay04

label BusBeachTownDay04:
scene beach with dissolve
$ renpy.pause(1.0, hard=True)   
p "Bye bye Tini-Wini-Bikini beach!"
p "Ah, here's the bus going to town..."
jump BusDriveDayb04

label BusBeachHomeDay04:
scene beach with dissolve
$ renpy.pause(1.0, hard=True)   
p "Bye bye Tini-Wini-Bikini beach!"
p "Ah, here's the bus going to the burbs..."
jump BusDriveDayb04

label BeachWalkDay04:
$ walkbeachseen04 = True
if (boughthallebikini == True) and ((walkbeachseen == False) or (beachswimday03 == True)) and (hallefucked == False):
    jump HalleBeachDay04
else:
    scene beachempty with dissolve
    $ renpy.pause(1.0, hard=True)  
    if (beachswimday04 == False) and (beachswimday03 == False):
        "This secluded part of the beach is empty... I could always go for a swim I guess."
        menu:
            "Go for a swim" if (beachswimday04 == False) and (beachswimday03 == False):
                jump BeachSwimDay04
            "Don't go for a swim":
                jump ExploreBeachDay04
    "This secluded part of the beach is empty today. BORING!"
    jump ExploreBeachDay04

label BeachSwimDay04:
$ beachswimday04 = True
play music "Sounds/randybeachsound.mp3"
scene beachswim01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I can see some coral reefs below. Let's dive and have a look!"        
scene beachswim02 with dissolve
play music "Sounds/underwater.mp3"
$ renpy.pause(1.0, hard=True)
p "What the hell is that thing swimming towards me?"
jump Mermaid01Day04

label HalleBeachDay04:
$ walkbeachseen04 = True 
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
        jump Underwater01bDay04
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
        jump Underwater01bDay04

label Underwater01bDay04:
scene hallebeach03 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Come on, this way! You'll see, it's gonna be ssoo much fun!"

label Underwater02Day04:
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
        jump Mermaid01Day04
    "Sneak under her":
        scene underwater03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Bingo, she's smiling at me... I wonder what a kiss underwater feels like..."
        scene underwater03b with dissolve
        p "What's wrong, she seems to be scared of something..."
        scene underwater04 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "She's darting off... OMG, what the fuck is that?..."
        jump Mermaid01Day04

label Mermaid01Day04:
scene mermaid01 with dissolve
$ renpy.pause(1.0, hard=True)
p "This mermaid is captivating... OK, she has a fish tail and all that but... Mmmh, those tits..."
scene mermaid02 with dissolve
$ renpy.pause(1.0, hard=True)
p "She seems to be signalling me to follow her..."
menu:
    "Follow her":
        jump Mermaid02Day04
    "Get the hell out of here and re-join Halle" if (beachswimday04 == False):
        $ underwaterleft = True
        jump Underwater03Day04
    "Get the hell out of here" if (beachswimday04 == True):
        scene beachswim01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Phew, that was close!I'm still shaking. Better go back to the beach..." 
        scene beachempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ExploreBeachDay04

label Mermaid02Day04:
scene mermaid03 with dissolve
$ renpy.pause(1.0, hard=True)
p "She's taking me to a giant clam... Is this where she lives?..."
scene mermaid04 with dissolve
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
        jump Mermaid03Day04
    "Get the hell out of here and re-join Halle" if (beachswimday04 == False):
        jump Underwater03Day04
    "Get the hell out of here" if (beachswimday04 == True):
        scene beachswim01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Phew, that was close!I'm still shaking. Better go back to the beach..." 
        scene beachempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ExploreBeachDay04
        
label Mermaid03Day04:
scene mermaid08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Here we go, it's tough to aim underwater but once I'm in, it shouldn't move too much..."
show mermaidfuckslow
show faster
call screen mermaidfuckslowday04
screen mermaidfuckslowday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MermaidFuckFastday04")
label MermaidFuckFastday04:
hide faster
show mermaidfuckfast
show cum
call screen mermaidfuckfastday04
screen mermaidfuckfastday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MermaidFuckCumday04")
label MermaidFuckCumday04:
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
if (beachswimday04 == False):
    jump Underwater03Day04
if (beachswimday04 == True):
    scene beachswim01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "The sea is getting rough. I'd better go back to the beach..." 
    scene beachempty with dissolve
    $ renpy.pause(1.0, hard=True)
    jump ExploreBeachDay04

label Underwater03Day04:
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
            jump HalleBackBeach01Day04
        else:
            scene hallesea04 with dissolve
            $ renpy.pause(1.0, hard=True)
            ha "Ha ha! You boys really are all the same... A pair of tits, that's all that counts!"
            ha "Let's get back to the beach, the sea is getting rough..."
            p "Great idea..."
            jump HalleBackBeach01Day04
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
        jump HalleBackBeach01Day04        
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
        jump HalleBackBeach01Day04
        
label HalleBackBeach01Day04:
stop music
play music "Sounds/oceanwaves.mp3"
scene hallebeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Well, that was fun, apart from this vile creature... I think I'd better head back to the university, I need to study."
menu:
    "Okay, I hope to see you again Halle...":
        ha "You will, don't worry... If you come back to the beach, I'll be here..."
        jump ExploreBeachDay04
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True) and (lust_points[9] >=8):
        jump HallePendulumDay04
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
        jump ExploreBeachDay04

label HallePendulumDay04:
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
    jump HalleFuckDay04
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
    jump HalleFuckDay04   

label HalleFuckDay04:
scene hallebeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "I think I changed my mind... I would rather spend some \"quality\" time with you after all..."
ha "And by \"quality\", I mean some hot, steamy SEX!"
p "Alright, I'm in baby!"
label HalleFuckDay04b:
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
label HallePrefuckDay04:
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
        jump HallePrefuckDay04
    "Spread her legs and fuck her pussy slowly":
        ha "You want to fuck me some more stud? Yeah, I 'm ready for your great big horsecock, come and ram that monstercock home!"
        jump HalleFuckMovieDay04

label HalleFuckMovieDay04:
stop music
play sound "Sounds/oceanwaves.mp3"
play music "Sounds/hallefuckslow.mp3"
show hallefuckslow
show faster
call screen hallefuckslowday04
screen hallefuckslowday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("HalleFuckFastday04")
label HalleFuckFastday04:
hide faster
play music "Sounds/hallefuckfast.mp3"
show hallefuckfast
show cum
call screen hallefuckfastday04
screen hallefuckfastday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("HalleFuckCumday04")

label HalleFuckCumday04:
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
    
jump ExploreBeachDay04

label Lifeguard01Day04:
stop music
scene tower01 with dissolve
$ renpy.pause(1.0, hard=True)
if (hour == 16) and (wonarmwrestling == True):
    pa "Hi again [name]. So, you wanna start working today?"
    menu:
        "Sure, I'm in!":
            jump LifeGuardWorkDay04
        "Maybe another day...":
            pa "Fine, your choice, hope to see you back here at 4pm another day..."
            jump ExploreBeachDay04
if (hour >=17) and (wonarmwrestling == True):
    pa "It's a bit late to start a workshift. We're almost done here. Come back tomorrow at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay04
if (hour <=15) and (wonarmwrestling == True):
    pa "It's a bit early to start a workshift. Come back at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay04

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
        jump ArmWrestlingDay04

    "This guy looks too strong, bail out":
        p "Err... Maybe another time... I need to...train."
        scene tower05 with dissolve
        $ renpy.pause(1.0, hard=True)
        mb "Oooooh! Little boy scared... Once again, Mitch Bigcannon is the winner! Choo-chooo!"
        $ lifeguardbail = True
        jump ExploreBeachDay04


label ArmWrestlingDay04:
$ clicked = True
$ points=20
if (strength <= 7):
    jump WrestlingStrength07Day04
if (strength == 8):
    jump WrestlingStrength08Day04
if (strength >= 9):
    jump WrestlingStrength09Day04

label WrestlingStrength07Day04:
$ plus=0
$ max_point=40
scene arm01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Ready guys? On your marks...set.. and go!"
play music "Sounds/grunt.mp3"
scene arm01b with dissolve
centered "Click on the hand!{w=1}{nw}"
call screen clicker7day04
screen clicker7day04:
    modal True
    timer .2 repeat True action [If(points <= 0, true=Jump("LostwrestlingDay04"), false=SetVariable("points", points - 1))]
    button:
        xpos .35
        ypos .3
        xysize(200, 200)
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("WonwrestlingDay04"), false=SetVariable("points", points + plus))]
    bar value StaticValue(points, max_point):
        xalign 0.45 yalign 0.0
        xmaximum 400 
        ymaximum 15

label WrestlingStrength08Day04:
$ plus=1
$ max_point=40
scene arm01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Ready guys? On your marks...set.. and go!"
play music "Sounds/grunt.mp3"
scene arm01b with dissolve
centered "Click on the hand!{w=1}{nw}"
call screen clicker8day04
screen clicker8day04:
    modal True
    timer .3 repeat True action [If(points <= 0, true=Jump("LostwrestlingDay04"), false=SetVariable("points", points - plus))]
    button:
        xpos .35
        ypos .3
        xysize(200, 200)
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("WonwrestlingDay04"), false=SetVariable("points", points + plus))]
    bar value StaticValue(points, max_point):
        xalign 0.45 yalign 0.0
        xmaximum 400 
        ymaximum 15

label WrestlingStrength09Day04:
$ plus=2
$ max_point=40
scene arm01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Ready guys? On your marks...set.. and go!"
play music "Sounds/grunt.mp3"
scene arm01b with dissolve
centered "Click on the hand!{w=1}{nw}"
call screen clicker9day04
screen clicker9day04:
    modal True
    timer .5 repeat True action [If(points <= 0, true=Jump("LostwrestlingDay04"), false=SetVariable("points", points - plus))]
    button:
        xpos .35
        ypos .3
        xysize(200, 200)
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("WonwrestlingDay04"), false=SetVariable("points", points + plus))]
    bar value StaticValue(points, max_point):
        xalign 0.45 yalign 0.0
        xmaximum 400 
        ymaximum 15

label LostwrestlingDay04:
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
jump ExploreBeachDay04

label WonwrestlingDay04:
stop music
play music "Sounds/oceanwaves.mp3"
play sound "Sounds/thump.mp3"
scene armwon with dissolve
$ renpy.pause(1.0, hard=True)
p "I win JERK! I'm da man, I'm DA MAN!"
scene tower06 with dissolve
$ renpy.pause(1.0, hard=True)
if  (strength >=10):
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
            jump LifeGuardWorkDay04
        "Maybe another day...":
            pa "Fine, your choice, hope to see you back here at 4pm another day..."
            jump ExploreBeachDay04
if (hour >=17) and (wonarmwrestling == True):
    pa "It's a bit late to start a workshift. We're almost done here. Come back tomorrow at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay04
if (hour <=15) and (wonarmwrestling == True):
    pa "It's a bit early to start a workshift. Come back at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay04

label LifeGuardWorkDay04:
if (workedfirsdaylifeguard == True):
    jump LifeGuardSecondWorkDay04
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
        jump LifeGuardWork02Day04
    "Oh yeah, I'll get one too!":
        pa "No you won't, you're too young. Your turn on the binoculars anyway."
        jump LifeGuardWork02Day04
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
        jump LifeGuardWork02Day04    

label LifeGuardWork02Day04:
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
        jump LifeguardSmall01Day04
    "The tall woman on the right. (Sandy)":
        jump LifeguardsBig01Day04


label LifeguardSmall01Day04:
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
        jump TowerEndDay04
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
        jump TowerEndDay04
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
        jump TowerEndDay04

label LifeguardsBig01Day04:
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
        jump TowerEndDay04
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
        jump TowerEndDay04

label LifeGuardSecondWorkDay04:
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
        jump LifeGuardWorkSecond02Day04
    "Oh yeah, I'll get one too!":
        pa "No you won't, you're too young. Your turn on the binoculars anyway."
        jump LifeGuardWorkSecond02Day04
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
        jump LifeGuardWorkSecond02Day04

label LifeGuardWorkSecond02Day04:
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
    jump SavedLollySecondDay04
if (savedlolly == True):
    jump SavedSandySecondDay04
    
label SavedLollySecondDay04:
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
        jump TowerEndDay04
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
        jump TowerEndDay04
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
        jump TowerEndDay04

label SavedSandySecondDay04:
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
    jump SavedSandyLowStrength
if (strength >= 9):
    jump SavedSandyHighStrength

label SavedSandyLowStrength:
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
        jump TowerEndDay04
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
        jump TowerEndDay04

label SavedSandyHighStrength:
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
        jump TshirtSandyEnd        
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
        jump TshirtSandyEnd

label TowerEndDay04:
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
label TowerEndChoiceDay04:
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
        jump TowerEndChoiceDay04        
    "Go and meet Pamela at the beach bar":
        jump BeachPamela01Day04  
    "Leave":
        jump ExploreBeachDay04       
        
label BeachPamela01Day04:
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
        jump ExploreBeachDay04        
    "Buy Pamela an alcoholic beverage (6$)":
        $ money -= 6
        scene beachbarpamela02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "Mmh, thanks [name]... That's a lovely... (hips)... cocktail."
        $ lust_points[18] += 1
        $ score += 1
        show lust01:
            xalign 0.1 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01 
        pa "You can come back anytime to work for us..."
        jump ExploreBeachDay04        
    "Talk to Pamela about working some more as a lifeguard":
        scene beachbarpamela02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "Yeah, I guess we could use your help some more. You can come back anytime to work for us..."
        mb "Humpf..."
        jump ExploreBeachDay04
    
        
label RandyBeachDay04:
stop music
scene randybeach01 with dissolve
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
$ randybeachseen04 = True
if (randybeachseen == True) or (randybeachseen02 == True) or (randybeachseen03 == True):
    p "Finally back here again. I'd better take my speedos off."
else:
    p "I guess that's it. I'd better take my speedos off."
window hide
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)

label RandyBeachDay04b:
p "I see three parasols but I can't see the people behind them...Which one should I go to?"
menu:
    "Go to the closest red parasol on the right" if (seenparasold01 == False):
        jump RandyBeachParasold01
    "Go to the middle orange parasol" if (seenparasold02 == False):
        jump RandyBeachParasold02
    "Go to the furthest red parasol on the left" if (seenparasold03== False):
        jump RandyBeachParasold03
    "Leave Randy Beach":
        jump ExploreBeachDay04

label RandyBeachParasold01:
$ seenparasold01 = True

scene britbeach01
show randybeachparasol01
$ renpy.pause(2.0, hard=True)
p "A pair of legs... This means a pussy not too far away..."
window hide
hide randybeachparasol01 with moveoutright
$ renpy.pause(1.0, hard=True)
p "AH AH, it's Brittany!... As naked as a newborn baby, but with with much larger tits."
scene britbeach02 with dissolve
$ renpy.pause(1.0, hard=True)
br "Oh my God, what are you doing here twerp?"
if ((seengloryhole03 == True) or (seengloryhole04 == True)) and (gloryholetold == False):
    br "What is this hanging between your legs? It's so ENORMOUS! And it also looks familiar for a strange reason..."
    menu:
        "That's cos you sucked it through the gloryhole at school.":
            scene britbeach03 with dissolve
            $ renpy.pause(1.0, hard=True)
            br "What? You saw me? Err... Don't tell anyone please!"
            menu:
                "Keeping secrets has a price... If you get what I mean...":
                    scene britbeach04 with dissolve
                    $ renpy.pause(1.0, hard=True)
                    br "A princess like me will not be blackmailed by a junior twerp!"
                    br "Be gone! I did not grant you any audience today!"
                    jump Parasol01dout
                "Of course, keeping secrets is what good friends do...":
                    scene britbeach05 with dissolve
                    $ renpy.pause(1.0, hard=True)
                    br "And loyal subjects to a beautiful queen... You understand that, I can tell..."
                    $ lust_points[1] +=1
                    $ score += 1
                    show lust01:
                        xalign 0.2 yalign 0.4
                        linear 1.0 yalign 0.2
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lust01
                    if (wristband == True):
                        p "I have a present for you Brittany."
                        scene britbeach03 with dissolve
                        $ renpy.pause(1.0, hard=True)        
                        br "Oh really? What is it? It'd better be a present that befits a princess like me!"
                        p "Yes it is, look!"
                        scene britbeach07 with dissolve
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
                        br "Well, thank you [name]? Is that right? Why don't you sit next to me for a while..."
                        jump BritBeach02
                    br "I'll see you around.... dear whats-your-name friend..."
                    p "[name]! You could at least make the effort of remembering it for Christ's sake!"
                    br "I have so many subjects, it's hard to keep track of them all. Now be gone [name], I need to get the perfect tan for Friday's beauty pageant."
                    jump Parasol01dout
        "Why don't you get a closer look just to be sure?":
            scene britbeach04 with dissolve
            $ renpy.pause(1.0, hard=True)
            br "What kind of girl do you take me for?"
            p "Err, one who would suck a random cock through a hole in the wall actually."
            br "I can't believe I'm hearing this, be gone TWERP!"
            jump Parasol01dout

if ((seengloryhole03 == True) or (seengloryhole04 == True)) and (gloryholetold == True): 
    br "And strutting around with that filthy cock I can't believed I sucked!"
    p "Hey! My cock is not filthy. It's squeaky clean after you cleaned it with your mouth."
    br brittany "Oh my God, such insolence! And in front of a beauty Queen no less! WHY are you here exactly?"
                      
menu:
    "Looking for a spot to sunbathe. This one looks pretty good.":
        scene britbeach04 with dissolve
        br "No way, I ain't sharing my spot with a junior! Leave me alone or I'll call José!"
        p "Alright, alright, but you should be nicer to me, I might be a jury on Friday evening for the school beauty pageant..."
        br "I don't need to be nice, I need to be beautiful! So let me work on getting the perfect tan for Friday, be gone!"
        p "(Gee, what an arrogant bitch...)"
        jump Parasol01dout
    "Just looking for hot chicks. I think I just hit the jackpot!":
        br "Of course you have, I am the most beautiful girl on the island! And I'll prove it by winning the beauty pageant on Friday!"
        p "It turns out I might be a jury on Friday evening for the school beauty pageant..."
        scene britbeach03 with dissolve
        br "What? Oh... Why don't you sit here for a while then."
        jump BritBeach02
    "It's so hot and I'm thirsty. I thought you might have some milk for me.":
        scene britbeach04 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "You want to suckle on my nipples and ruin my perfect tits for Friday's pageant? Who sent you? That stupid bimbo Kate?"
        p "What? no, I..."
        br "Get out of my face, SABOTEUR!"
        $ lust_points[1] -=1
        show lustminus01:
            xalign 0.2 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump Parasol01dout
    "I have a present for you Brittany." if (wristband == True):
        scene britbeach05 with dissolve
        $ renpy.pause(1.0, hard=True)        
        br "Oh really? What is it? It'd better be a present that befits a princess like me!"
        p "Yes it is, look!"
        scene britbeach07 with dissolve
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
        br "Well, thank you [name]? Is that right? Why don't you sit next to me for a while..."
        jump BritBeach02

label BritBeach02:
scene britbeach06 with dissolve
$ renpy.pause(1.0, hard=True)
br "So... [name], right? I can't imagine you would vote for anyone else but me on Friday, right?"
menu:
    "My vote for you is a given Brittany.":
        br "Good, that's settled then. I am the most beautiful girl and I WILL win."
        $ lust_points[1] +=1
        $ score += 1
        show lust01:
            xalign 0.2 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        br "You can leave now, I need to work on my tan."
        p "That's it? Nothing more?"
        br "Yes, that's IT. I'm sure you are a busy boy, so shoo, go and do whatever you pervy boys do."
        jump Parasol01dout
    "I don't know, I'll have to decide on Friday really...":
        br "But surely, you can be persuaded to make up your mind already..."
        scene britbeach09 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "Aren't these breasts simply the most succulent you've ever seen?"
        p "They sure are VERY nice...."
        br "Much better than Kate's weird-looking fake tits, don't you think [name]?"
        p "Err... Yeah, sure..."
        scene britbeach10 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "And how about my arse? What man could resist such perfectly defined buttocks and thighs?"
        p "I don't know... A blind man?"
        br "I hope you understand now... There is no other choice than casting your vote for me."
        p "Ga..ga...ga..."
        br "I'm sure you are a busy boy, so shoo, go and do whatever you pervy boys do."
        jump Parasol01dout
    "I quite fancy Kate to be honest.":
        scene britbeach06b with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What? That filthy trollop? How could you? Get out of my sight, I will win anyway, I don't need your vote!"
        $ lust_points[1] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.2 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump Parasol01dout
    "José slept with Kate. It's clear HE's going to vote for her Friday night." if (katejosewin == True) and (brittanyjosewin == False):
        $ toldbritjose = True
        $ renpy.pause(1.0, hard=True)
        br "What? How could he... This is a crime of lese-majesty that shall not go unpunished!"
        scene britbeach08 with dissolve
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
        br "I need... to go... Thanks for letting me know [name]."
        $ lust_points[1] +=1
        $ score +=1
        show lust01:
            xalign 0.2 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        p "Alright...Maybe you and I? One day..."    
        jump Parasol01dout

    "José is getting real close to Kate. I wonder why..." if (lust_pointsB[11] >=6) and (lust_pointsB[11] <=9) and (brittanyjosewin == False):
        scene britbeach08 with dissolve
        $ toldbritjose = True
        $ renpy.pause(1.0, hard=True)
        br "What? How could he... This is a crime of lese-majesty that shall not go unpunished!"
        $ lust_pointsB[1] -=1
        show challengerlustminus01:
            xalign 0.2 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus01
        scene britbeach06b with dissolve
        $ renpy.pause(1.0, hard=True)        
        br "I am going to talk to him and reason this knucklehead!"
        br " In the meantime, I am counting on your vote, my loyal subject."
        jump Parasol01dout

label Parasol01dout:
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeachDay04b

label RandyBeachParasold02:
$ seenparasold02 = True
scene randystewardess01
show randybeachparasol02
$ renpy.pause(2.0, hard=True)
p "Mmmh, a nice leg is sticking out..."
window hide
hide randybeachparasol02 with moveoutleft
$ renpy.pause(1.0, hard=True)
p "Oh it's that hot stewardess that was on my plane when we first arrived on Veri-Bosti! Nice..."
h "I remember you... And that pounding you gave to my poor pussy on the plane..."
p "I could pound you again right here, right now, nobody's watching..."
h "Sorry, but I can only have sex on a plane. Gold membership to the Mile-High Club has some obligations..."
scene randystewardess02 with dissolve
$ renpy.pause(1.0, hard=True)
h "I sure wish I only had a Silver card... Then I'd be allowed to fuck someone on land... Mmmh, Yeah, jerk that fat cock for me [name]..."
p "I didn't realize the Mile-High Club had such restrictions..."
h "That's the way it is (sigh). Please leave or I'll get too horny and break my oath... And then I would be banned from ever flying again and lose my livelihood."
p "Sure, I understand, I'll leave you alone then. (What a waste...)"
jump Parasol02dout

label Parasol02dout:
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeachDay04b
 
label RandyBeachParasold03:
stop music
$ seenparasold03 = True
$ peeping += 1
scene babalesbian01
show randybeachparasol03
$ renpy.pause(1.0, hard=True)
p "What could be hiding behing this parasol?"
window hide
hide randybeachparasol03 with moveoutright
play sound "Sounds/lesbians.mp3"
$ renpy.pause(1.0, hard=True)
if (seenparasolb03 == True) and (seenparasolc01 == True):
    p "Damn, it's one of the lesbian girls and that giant-cocked muscle chick!"
    jump RandyBeachParasold03b
if (seenparasolb03 == True) and (seenparasolc01 == False):
    p "Damn, it's one of the lesbian girls from the other day with a giant-cocked muscle chick! Scary! They'll probably beat me up, I'm out of here!"
    jump Parasol03dout
if (seenparasolc01 == True) and (seenparasolb03 == False):
    p "Damn, it's that giant-cocked muscle chick being serviced by a woman... She seems to be struggling with her giant balls..."
    jump RandyBeachParasold03b
if (seenparasolc01 == False) and (seenparasolb03 == False):
    p "Damn, it's a giant-cocked muscle chick being serviced by a woman... She seems to be struggling with her giant balls..."
    jump RandyBeachParasold03b
label RandyBeachParasold03b: 
l01 "Hey, what are you looking at? Can't you see I'm busy fondling my futa girlfriend's massive nutsack?"
ba "Who's disturbing Rosie and Baba?"
p "Don't mind me ladies, go about your business..."
l01 "If you watch, then you'd better not play with your filthy man-dick or Baba will break your fucking neck, understood boy?"
p "Err, yeah, crystal clear..." 
l01 "Watch as I engulf Baba's mighty fuckpole..."
ba "Yeah, do it Rosie, Baba is horny!"
scene babalesbian02 with dissolve
play sound "Sounds/hallesuck01.mp3"
$ renpy.pause(1.0, hard=True)
p "(Shit, she's really doing it! I'm not sure whether to be turned on or disgusted...)"
scene babalesbian03 with dissolve
play sound "Sounds/hallesuck02.mp3"
$ renpy.pause(1.0, hard=True)
scene babalesbian02 with dissolve
$ renpy.pause(0.3, hard=True)
scene babalesbian03 with dissolve
$ renpy.pause(0.3, hard=True)
scene babalesbian02 with dissolve
$ renpy.pause(0.3, hard=True)
scene babalesbian03 with dissolve
play sound "Sounds/hallesuck02.mp3"
$ renpy.pause(0.3, hard=True)
scene babalesbian02 with dissolve
$ renpy.pause(0.3, hard=True)
scene babalesbian03 with dissolve
$ renpy.pause(0.3, hard=True)
scene babalesbian02 with dissolve
$ renpy.pause(0.3, hard=True)
scene babalesbian04 with dissolve
play sound "Sounds/babacumming.wav"
$ renpy.pause(2.0, hard=True)
p "I guess the show is over, I'd better leave..."

jump Parasol03dout

label Parasol03dout:
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeachDay04b


label Cabin01Day04:
scene cabin01 with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
p "I guess it must be here. God, this place looks dingy."
menu:
    "Enter the cabin":
        jump Cabin02Day04
    "Leave, it looks too dangerous.":
        jump ExploreBeachDay04

label Cabin02Day04:
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
            jump Cabin03Day04
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
            jump Cabin03Day04
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
            jump Cabin03Day04
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
            jump Cabin03Day04
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
        jump Cabin03Day04
        
label Cabin03Day04:
scene cabin04 with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
$ maddysaved = True
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
            jump MaddyPrefuckDay04
        "Don't drink white bull and keep it for another time":
            pass
    md "What? But... I was thinking we could... you know..."
    p "Ah. Yeah, about that. It's just that I feel really tired you know, after fighting with your kidnapper and all that..."
    md "OK, I understand [name], I hope you'll be in better \"shape\" tomorrow (wink)."
    scene beach with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Maddy is in safe hands now. But not in MY safe hands. (sigh)"
    jump ExploreBeachDay04
if (lust_points[14] >=10) and (stamina <= 0):
    p "I'll take you over to the lifeguards so they can take care of you Maddy."
    md "What? But... I was thinking we could... you know..."
    p "Ah. Yeah, about that. It's just that I feel really tired you know, after fighting with your kidnapper and all that..."
    md "OK, I understand [name], I hope you'll be in better \"shape\" tomorrow (wink)."
    scene beach with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Maddy is in safe hands now. But not in MY safe hands. (sigh)"
    jump ExploreBeachDay04 
label MaddyPrefuckDay04:
if (lust_points[14] >=10):
    p "I've got another muscle that's huge and hard... You wanna feel its awesome power?"
    md "Yes, I'm ready! Fuck me with that giant love muscle of yours [name]!"
    p "I spotted a small secluded bay on the way here, let's go there, I'm so horny, I can't wait!"
    jump MaddyFuckDay04

if (lust_points[14] <=9):
    p "I've got another muscle that's huge and hard... You wanna feel its awesome power?"
    md "Err... I just got out of being bound and abused by a filthy pervert, I'm not in the mood right now you FREAK!"
    p "Well, I thought... it might do you good. Like a therapy."
    md "No, I just want to go home... Take me home please [name]..."
    p "OK, I'll carry you to the beach and call the lifeguards so they can take care of you."
    scene beach with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Maddy is in safe hands now. But not in MY safe hands. (sigh)"
    jump ExploreBeachDay04
   
label MaddyFuckDay04:
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
label MaddyFootDay04b:
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
        jump MaddyFootDay04b
    "Cum quickly (no stamina penalty)":
        scene maddyfoot03 with dissolve
        play sound "Sounds/ryancumming.mp3"
        $ renpy.pause(2.0, hard=True)
        p "Fuck, your feet are so good on my knob, RHHAAA!"
        md "Wow, I didn't expect you to cum like a stallion so soon [name]...."
        p "Don't worry, it was just a tiny premature load, let's move on to the main dish of the day!"
        jump MaddyFuckChoiceDay04

label MaddyFuckChoiceDay04:
scene maddybeach04 with dissolve
$ renpy.pause(1.0, hard=True)
md "I'm ready for anything, what are you ready for...?"
menu:
    "How about some anal to really get our juices going?" if (maddyarse == False):
        jump MaddyArseDay04
    "How about a blowjob, and I'll lick your pussy at the same time?" if (maddyblowjob == False):
        jump MaddyBlowjobDay04
        
label MaddyArseDay04:
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
label MaddyArseDay04b:
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
        jump MaddyArseDay04b
    "Move on":
        scene maddyarse02 with dissolve
        $ renpy.pause(1.0, hard=True)
        md "This is too much, my stomach is so full of cock! Please let's switch position!"
        menu:
            "Alright, how about a blowjob, and I'll lick your pussy at the same time?" if (maddyblowjob == False):
                jump MaddyBlowjobDay04
            "Fuck her sweet pussy" if ((maddyarse == True) and (maddyblowjob == True)):
                jump MaddyEndFuckDay04

label MaddyBlowjobDay04:
$ maddyblowjob = True
scene maddyfuck05 with dissolve
$ renpy.pause(1.0, hard=True)

scene maddyfuck05b with dissolve
play sound "Sounds/maddyblow01.mp3"
$ renpy.pause(5.0, hard=True)
md "I've never sucked a cock this huge before... But I don't care, I want to choke on it!"
label MaddyBlowjobDay04b:
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
        jump MaddyBlowjobDay04b
    "Move on":
        scene maddybeach04 with dissolve
        $ renpy.pause(1.0, hard=True)
        md "My jaws are starting to tire, your cock is just too gigantic! Please let's switch position!"
        menu:
            "Alright, how about some anal to real get our juices going?" if (maddyarse == False):
                jump MaddyArseDay04
            "Fuck her sweet pussy" if ((maddyarse == True) and (maddyblowjob == True)):
                jump MaddyEndFuckDay04


label MaddyEndFuckDay04:
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
call screen maddyfuckslow
screen maddyfuckslow:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MaddyFuckFast")
label MaddyFuckFast:
hide faster
play music "Sounds/maddyfuckfast.mp3"
show maddyfuckfast
show cum
call screen maddyfuckfast
screen maddyfuckfast:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MaddyFuckCum")

label MaddyFuckCum:
hide maddyfuckfast
hide maddyfuckslow
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
$ fuckedschoolgirlday04 = True
if (maddyjosewin == False):
    p "(She didn't notice I took a picture of us... Now I'll send it to José)."
    $ maddywin = True

scene maddyafterfuck with dissolve
$ renpy.pause(1.0, hard=True)
md "Don't tell Frieda you had sex with me, she looks up to me, I don't want to disappoint her..."
p "Sure, absolutely nobody will ever know, I swear... (fingers crossed)."
$ hour += 1
jump ExploreBeachDay04

label Tshirt01Day04:
$ tshirt = True
scene tshirt01 with dissolve
stop music
play music "Sounds/oceanwaves.mp3"
$ renpy.pause(1.0, hard=True)
play sound "Sounds/winner.mp3"
mb "Welcome ladies and gentlemen to our weekly wet T-shirt contest, I'm your host Mitch Bigcannon, YEAH, TINI-WINI-BIKINI BEACH ROCKS!"
mb "We have four lovely beauties today, on the left Halle who is one hot mama I tells ya bros!"
mb "Standing next to her is Doris, man, what a muscle lady, you wouldn't want to get on her wrong side, am I right or am I right?"
mb "Also we have lovely young Chantelle who is a senior student at Hardcox High."
mb "Look at that bod people, soon to be sprayed with cold water until her nipples poke holes through her T-shirt, WOO-HOO!"
p "(Jeezus what a douche...)"
mb "And finally Sandy, she's a student, her sorority is Omega-Mega-Boobs, AH, AH, I'm so funny, FUCK YEAH!"
mb "So let's get the spray spraying, and I'm not talking about my personal big cannon, that's for later, right girls?"
p "(Someone get this moron a brain...)"

scene tshirt02 with dissolve
$ renpy.pause(1.0, hard=True)
mb "Time to get wet ladies, let's see some nipples! Woo-HOO!"
# play sound "Sounds/waterspray.mp3"
mb "Now you can come back one by one so the jury can have a good look at those wet t-shirts hugging those yummy breasts! Halle, you're first!"
scene tshirtbackground with dissolve
$ renpy.pause(1.0, hard=True)
window hide
show tshirthalle01:
    xalign 0.99
    linear 4.0 xalign 0.5
$ renpy.pause(3, hard=True)
ha "Look at how hard my nipples are, vote for me please!"
window hide
hide tshirthalle01
show tshirthalle02 with dissolve
$ renpy.pause(3, hard=True)
mb "FUCK YEAH! That's some fine booty, I wanna be mama's boy, OOH-AHH, OOH-AAH! Round of applause for Halle, ladies and gentlemen!"
play sound "Sounds/applause.mp3"
$ renpy.pause(2.0, hard=True)
mb "Doris is next, we almost couldn't find a t-shirt her size for the contest, her balloons are so fucking HU-U-GE!"
window hide
hide tshirthalle02
show tshirtdoris01:
    xalign 0.99
    linear 4.0 xalign 0.5
$ renpy.pause(3, hard=True)
do "Just like my muscles Mitch, look at those biceps, they could crush the jury if, by mistake, they didn't vote for me... (wink)."
window hide
hide tshirtdoris01
show tshirtdoris02 with dissolve
$ renpy.pause(3, hard=True)
mb "Ooooh, I'd be careful if I was a member of the jury. Hang on a minute, I AM a member of the jury, DOH! AH AH, round of applause for Doris guys!"
play sound "Sounds/applause.mp3"
$ renpy.pause(2.0, hard=True)
mb "Chantelle, you're up! Bring those young sweet titties over here baby!"
hide tshirtdoris02
window hide
show tshirtchantelle01:
    xalign 0.99
    linear 4.0 xalign 0.5
$ renpy.pause(3, hard=True)
ch "This is my first wet t-shirt contest, it's so much fun and if you want to see me again, vote for me, thank you!"
window hide
hide tshirtchantelle01
show tshirtchantelle02 with dissolve
$ renpy.pause(3, hard=True)
mb "Now that's what I call a well-rounded argument, AH AH, god I'm so funny, I'm dying! Round of applause for Chantelle, FUCK YEAH!"
play sound "Sounds/applause.mp3"
$ renpy.pause(2.0, hard=True)
mb "And now Sandy ladies and gentlemen!"
window hide
hide tshirtchantelle02
show tshirtsandy01:
    xalign 0.99
    linear 4.0 xalign 0.5
$ renpy.pause(3, hard=True)
mb "Who wouldn't want to feel up those massive funbags, hey?"
sa "Who wants to be my Prince Charming? I'll be your your Princess if you vote for me!"
window hide
hide tshirtsandy01
show tshirtsandy02 with dissolve
$ renpy.pause(3, hard=True)
mb "I'd kiss those nipples anytime to wake them up baby! OOH-AHH, OOH-AAH! Big round of applause for our contestants!"
play sound "Sounds/applause.mp3"
$ renpy.pause(2.0, hard=True)
hide tshirtsandy02
show tshirtdoris01:
    xalign 0.3
show tshirthalle01:
    xalign -0.1
show tshirtchantelle01:
    xalign 0.65
show tshirtsandy01:
    xalign 1.05

mb "Let's tally the jury's vote to find out who will be our weekly winner and leave with a brand new skimpy Audacious Bikini! And let's thank our sponsors, we love you Audacious!"
if (tshirtjury == True):
    mb "Well, it looks like everything will come down to jury number five, since each girl got one vote so far..."
    mb "So, who will you cast your deciding vote for, member of the jury number five?"
    menu:
        "Halle":
            hide tshirthalle01
            hide tshirtdoris01
            hide tshirtchantelle01
            hide tshirtsandy01
            show tshirthalle03:
                xalign -0.1
                linear 2.0 xalign 0.5
            $ renpy.pause(1, hard=True)
            play sound "Sounds/applause.mp3"
            $ renpy.pause(2.0, hard=True)
            ha "I win! Thank you ssoo much [name]!"
            if (lust_points[9] == 8):
                $ lust_points[9] += 2
                $ score += 2
                show lust02:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust02
            if (lust_points[9] == 9):
                $ lust_points[9] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
            if (lust_points[9] <= 7):
                $ lust_points[9] += 3
                $ score += 3
                show lust03:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust03
            if (lust_points[9] >= 10):
                show epiclust:
                    xalign 0.2 yalign 0.2
                    zoom 0.5
                    linear 2.0 zoom 1.0
                play sound "Sounds/epiclust.mp3"
                $ renpy.pause(4.0, hard=True)
                hide epiclust
            if (hallefucked == True):
                p "I'd say let's meet up after the show on a secluded beach... But we already did that, right?"
                ha "Indeed. It's really REALLY nice of you to waste your vote on a girl you've already fucked this week!"                
                jump TshirtEndDay04 
            if (hallefucked == False):
                p "Let's meet up after the show Halle... On a secluded beach..."
                ha "You're so full of surprises. Why not, I'm in! Let me change into my swimsuit..."
            hide tshirthalle03
            show tshirtchantelle04
            ch "I thought there was some chemistry between us... I guess I was wrong..."
            $ lust_points[2] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.7 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            hide tshirtchantelle04
            show tshirtsandy04
            sa "Oh, why didn't you vote for me my Prince UN-Charming?"
            if (lust_points[19] <=9):
                $ lust_points[19] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.7 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
            hide tshirtsandy04
            jump TshirtHalleEnd
        "Doris":
            hide tshirthalle01
            hide tshirtdoris01
            hide tshirtchantelle01
            hide tshirtsandy01
            show tshirtdoris03:
                xalign 0.3
                linear 2.0 xalign 0.5
            $ renpy.pause(1, hard=True)
            play sound "Sounds/applause.mp3"
            $ renpy.pause(2.0, hard=True)
            do "Muscles always win the day! Or they beat the crap out of it..."
            $ lust_points[6] +=3
            $ score += 3
            show lust03:
                xalign 0.7 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust03
            p "I totally agree with you Doris. That's why I have huge muscles myself..."
            do "Yes, I can see that, you'll go far young man..."
            hide tshirtdoris03
            show tshirtchantelle04
            ch "I thought you liked me [name]... I'm sad now..."
            $ lust_points[2] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.7 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            hide tshirtchantelle04
            show tshirtsandy04
            sa "Humpf, my tits are bigger than hers, why didn't you choose me my Prince Charming?"
            if (lust_points[19] <=9):
                $ lust_points[19] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.7 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
            hide tshirtsandy04
            hide tshirtsandy04
            jump TshirtEndDay04            
        "Chantelle":
            hide tshirthalle01
            hide tshirtdoris01
            hide tshirtchantelle01
            hide tshirtsandy01
            show tshirtchantelle03:
                xalign 0.65
                linear 2.0 xalign 0.5
            $ renpy.pause(1, hard=True)
            play sound "Sounds/applause.mp3"
            $ renpy.pause(2.0, hard=True)
            ch "What, I win? I can't believe it, this is so exciting!"
            ch "And I have YOU to thank [name]... If I could, I'd kiss you right here in front of everyone..."
            $ lust_points[2] +=3
            $ score += 3
            show lust03:
                xalign 0.7 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust03
            p "Oh, we'll have plenty of opportunity for that Chantelle... And MORE, I promise you..."
            if (gymmember == True):
                menu:
                    "Invite her as a guest to the downtown gym as your guest":
                        p "You know, as an eminent member of the downtown gym, I can invite you as a guest for free."
                        p "We could train together... I could show you how I lift super-heavy barbells..."
                        ch "Really? Now that's something I'd like to see! (wink)"
                        p "We could go there tomorrow, I'll call you when I get there..."
                        $ invitedchantelle = True
                    "Don't say anything":
                        pass
                
            hide tshirtchantelle03
            show tshirthalle04
            ha "What? She has no experience of life!"
            if (lust_points[9] <= 9):
                $ lust_points[9] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.7 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
            hide tshirthalle04
            show tshirtsandy04
            sa "Choosing this small girl instead of your princess... How dare you!"
            if (lust_points[19] <=9):
                $ lust_points[19] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.7 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
            hide tshirtsandy04
            jump TshirtEndDay04            
        "Sandy":
            hide tshirthalle01
            hide tshirtdoris01
            hide tshirtchantelle01
            hide tshirtsandy01
            show tshirtsandy03:
                xalign 1.05
                linear 2.0 xalign 0.5
            $ renpy.pause(1, hard=True)
            play sound "Sounds/applause.mp3"
            $ renpy.pause(2.0, hard=True)
            sa "My Prince Charming to the rescue! I'm the winner!"
            if (lust_points[19] == 8):
                $ lust_points[19] += 2
                $ score += 2
                show lust02:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust02
            if (lust_points[19] == 9):
                $ lust_points[19] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
            if (lust_points[19] <= 7):
                $ lust_points[19] += 3
                $ score += 3
                show lust03:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust03
            if (lust_points[19] == 10):
                show epiclust:
                    xalign 0.6 yalign 0.1
                    zoom 0.5
                    linear 2.0 zoom 1.0
                play sound "Sounds/epiclust.mp3"
                $ renpy.pause(4.0, hard=True)
                hide epiclust
            p "Let's meet up after the show Sandy... I know a secluded beach cove that's perfect for us..."
            sa "Oooh, what do you have in mind? I can't wait my Prince Charming (wink)!"
            hide tshirtsandy03
            show tshirthalle04
            ha "She's from the worst sorority! You should have chosen me!"            
            if (lust_points[9] <=9):
                $ lust_points[9] -=1
                $ score -= 1
                show lustminus01:
                    xalign 0.7 yalign 0.2
                    linear 1.0 yalign 0.4
                play sound "Sounds/less.mp3"
                $ renpy.pause(2, hard=True)
                hide lustminus01
            hide tshirthalle04
            show tshirtchantelle04
            ch "I thought you liked me [name]... I'm sad now..."
            $ lust_points[2] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.7 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            hide tshirtchantelle04
            hide tshirtsandy04
            jump TshirtSandyEnd

if (tshirtjury == False):
    $ d4rolltshirt=renpy.random.randint(0, 3)
    if (d4rolltshirt == 0):
        mb "The votes have been counted and I can now announce the winner... Halle! WOO-HOO!"
        hide tshirthalle01
        hide tshirtdoris01
        hide tshirtchantelle01
        hide tshirtsandy01
        show tshirthalle03:
            xalign -0.1
            linear 2.0 xalign 0.5
        $ renpy.pause(1, hard=True)
        play sound "Sounds/applause.mp3"
        $ renpy.pause(2.0, hard=True)
        ha "I win! Thank you ssoo much everyone!"
        menu:
            "Congratulate her":
                p "Congrats Halle, that was fully deserved, you are so hot in that wet-t-shirt..."
                ha "Oh thank you!"
                if (lust_points[9] <= 9):
                    $ lust_points[9] += 1
                    $ score += 1
                    show lust01:
                        xalign 0.7 yalign 0.4
                        linear 1.0 yalign 0.2
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lust01     
                    if (lust_points[9] == 10):
                        show epiclust:
                            xalign 0.6 yalign 0.1
                            zoom 0.5
                            linear 2.0 zoom 1.0
                        play sound "Sounds/epiclust.mp3"
                        $ renpy.pause(4.0, hard=True)
                        hide epiclust
                    p "Let's meet up after the show Halle... On a secluded beach..."
                    ha "You're so full of surprises. Why not, I'm in! Let me change into my swimsuit..."
                    jump TshirtHalleEnd
                hide tshirthalle03
                jump TshirtEndDay04                            
            "Console Doris":
                hide tshirthalle03
                show tshirtdoris01
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                do "Thanks, but I really couldn't care less about this contest... I have plenty of bikinis at home, I'm just here to show off my muscles."
                $ lust_points[6] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01    
                hide tshirtDoris01
                jump TshirtEndDay04
            "Console Chantelle":
                hide tshirthalle03
                show tshirtchantelle04
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                ch "Thanks [name], it was my first time competing, I didn't really expect to win..."
                hide tshirtchantelle04
                show tshirtchantelle01
                ch "But I'm really happy you would have voted for me!"
                $ lust_points[2] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01 
                hide tshirtchantelle01
                jump TshirtEndDay04
            "Console Sandy":
                hide tshirtdoris03
                show tshirtsandy04
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                show tshirtsandy01
                sa "Thank you for saying that sweet thing my Prince Charming...Here is a kiss I'm sending you in return..."                
                $ lust_points[19] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
                if (lust_points[19] == 10):
                    show epiclust:
                        xalign 0.6 yalign 0.1
                        zoom 0.5
                        linear 2.0 zoom 1.0
                    play sound "Sounds/epiclust.mp3"
                    $ renpy.pause(4.0, hard=True)
                    hide epiclust
                    p "Let's meet up after the show Sandy... I know a secluded beach cove that's perfect for us..."
                    sa "Oooh, what do you have in mind? I can't wait my Prince Charming (wink)!"
                    hide tshirtsandy01
                    jump TshirtSandyEnd
                jump TshirtEndDay04

    if (d4rolltshirt == 1):
        mb "The votes have been counted and I can now announce the winner... Doris! WOO-HOO!"
        hide tshirthalle01
        hide tshirtdoris01
        hide tshirtchantelle01
        hide tshirtsandy01
        show tshirtdoris03:
            xalign 0.3
            linear 2.0 xalign 0.5
        $ renpy.pause(1, hard=True)
        play sound "Sounds/applause.mp3"
        $ renpy.pause(2.0, hard=True)
        do "Muscles always win the day! Or they beat the crap out of it..."
        menu:
            "Congratulate her":
                p "Congrats Doris, that was fully deserved, you are so hot in that wet-t-shirt..."
                do "Oh thank you!"
                $ lust_points[6] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01     
                hide tshirtdoris03
                jump TshirtEndDay04                
            "Console Halle":
                hide tshirtdoris03
                show tshirthalle04
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                ha "Well why didn't you become a jury member then? You let me down..."
                hide tshirthalle04
                jump TshirtEndDay04
            "Console Chantelle":
                hide tshirtdoris03
                show tshirtchantelle04
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                ch "Thanks [name], it was my first time competing, I didn't really expect to win..."
                hide tshirtchantelle04
                show tshirtchantelle01
                ch "But I'm really happy you would have voted for me!"
                $ lust_points[2] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01    
                hide tshirtchantelle01
                jump TshirtEndDay04
            "Console Sandy":
                hide tshirtdoris03
                show tshirtsandy04
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                sa "I know my Prince Charming, that's why you are so charming..."
                $ lust_points[19] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
                if (lust_points[19] == 10):
                    show epiclust:
                        xalign 0.6 yalign 0.1
                        zoom 0.5
                        linear 2.0 zoom 1.0
                    play sound "Sounds/epiclust.mp3"
                    $ renpy.pause(4.0, hard=True)
                    hide epiclust
                    p "Let's meet up after the show Sandy... I know a secluded beach cove that's perfect for us..."
                    sa "Oooh, what do you have in mind? I can't wait my Prince Charming (wink)!"
                    hide tshirtsandy04
                    jump TshirtSandyEnd
                jump TshirtEndDay04

    if (d4rolltshirt == 2):
        mb "The votes have been counted and I can now announce the winner... Chantelle! WOO-HOO!"
        hide tshirthalle01
        hide tshirtdoris01
        hide tshirtchantelle01
        hide tshirtsandy01
        show tshirtchantelle03:
            xalign 0.65
            linear 2.0 xalign 0.5
        $ renpy.pause(1, hard=True)
        play sound "Sounds/applause.mp3"
        $ renpy.pause(2.0, hard=True)
        ch "What, I win? I can't believe it, this is so exciting!"
        menu:
            "Congratulate her":
                p "Congrats Chantelle, that was fully deserved, you are so hot in that wet-t-shirt..."
                ch "Oh thank you [name]!"
                $ lust_points[2] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01     
                hide tshirtchantelle03
                jump TshirtEndDay04                
            "Console Halle":
                hide tshirtchantelle03
                show tshirthalle04
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                ha "I guess people like the younger girls these days (sigh)..."
                $ lust_points[9] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01    
                hide tshirthalle04
                jump TshirtEndDay04
            "Console Doris":
                hide tshirtchantelle03
                show tshirtdoris01
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                do "Thanks, but I really couldn't care less about this contest... I have plenty of bikinis at home, I'm just here to show off my muscles."
                hide tshirtDoris01
                jump TshirtEndDay04
            "Console Sandy":
                hide tshirtchantelle03
                show tshirtsandy04
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                ha "I know my Prince Charming, that's why you are so charming..."
                $ lust_points[19] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
                if (lust_points[19] == 10):
                    show epiclust:
                        xalign 0.6 yalign 0.1
                        zoom 0.5
                        linear 2.0 zoom 1.0
                    play sound "Sounds/epiclust.mp3"
                    $ renpy.pause(4.0, hard=True)
                    hide epiclust
                    p "Let's meet up after the show Sandy... I know a secluded beach cove that's perfect for us..."
                    sa "Oooh, what do you have in mind? I can't wait my Prince Charming (wink)!"
                    hide tshirtsandy04
                    jump TshirtSandyEnd
                jump TshirtEndDay04

    if (d4rolltshirt == 3):
        mb "The votes have been counted and I can now announce the winner... Sandy! WOO-HOO!"
        hide tshirthalle01
        hide tshirtdoris01
        hide tshirtchantelle01
        hide tshirtsandy01
        show tshirtsandy03:
            xalign 1.05
            linear 2.0 xalign 0.5
        $ renpy.pause(1, hard=True)
        play sound "Sounds/applause.mp3"
        $ renpy.pause(2.0, hard=True)
        sa "I win, I'm the Princess Charming! Or at least my wet tits."
        menu:
            "Congratulate her":
                p "Congrats Sandy, that was fully deserved, you are so hot in that wet-t-shirt..."
                sa "Oh thank you my Prince Charming!"
                $ lust_points[3] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01     
                if (lust_points[19] == 10):
                    show epiclust:
                        xalign 0.6 yalign 0.1
                        zoom 0.5
                        linear 2.0 zoom 1.0
                    play sound "Sounds/epiclust.mp3"
                    $ renpy.pause(4.0, hard=True)
                    hide epiclust
                p "Let's meet up after the show Sandy... I know a secluded beach cove that's perfect for us..."
                sa "Oooh, what do you have in mind? I can't wait my Prince Charming (wink)!"                
                hide tshirtsandy03
                jump TshirtSandyEnd
            "Console Halle":
                hide tshirtsandy03
                show tshirthalle04
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                ha "Thanks, but you couldn't vote so your consolation is pointless..."
                hide tshirthalle04
                jump TshirtEndDay04
            "Console Doris":
                hide tshirtsandy03
                show tshirtdoris01
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                do "Thanks, but I really couldn't care less about this contest... I have plenty of bikinis at home, I'm just here to show off my muscles."
                hide tshirtDoris01
                jump TshirtEndDay04
            "Console Chantelle":
                hide tshirtsandy03
                show tshirtchantelle04
                p "I'm sorry you didn't win, I would have voted for you for sure..."
                ch "Thanks [name], it was my first time competing, I didn't really expect to win..."
                hide tshirtchantelle04
                show tshirtchantelle01
                ch "But I'm really happy you would have voted for me!"
                $ lust_points[2] += 1
                $ score += 1
                show lust01:
                    xalign 0.7 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01    
                hide tshirtchantelle01
                jump TshirtEndDay04
                
label TshirtEndDay04:
scene tshirtbackground with dissolve
$ renpy.pause(1.0, hard=True)
p "The contest is over and everyone left..."
jump ExploreBeachDay04

label TshirtSandyEnd:
stop music
play music "Sounds/oceanwaves.mp3"
if (sandyfuckedlifeguard == True):
    scene sandybeach01b with dissolve
if (sandyfuckedlifeguard == False):
    scene sandybeach01 with dissolve
$ renpy.pause(1.0, hard=True)
sa "Oh, my Prince Charming, what a beautifully romantic place you found, far from the madding crowd!"
menu:
    "Yes, it's the perfect spot for us to get...more intimate..." if (lust_points[19] ==10):
        if (sandyfuckedlifeguard == True):
            scene sandybeach02c with dissolve
        if (sandyfuckedlifeguard == False):
            scene sandybeach02a with dissolve        
        sa "And to get back to our natural human state without constraints by being naked...In total communion with Mother Nature."
        jump SandyFuckDay04
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True) and (lust_points[19] >=8) and (lust_points[19] <=9):
        jump SandyPendulumDay04
    "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[19] >=8) and (lust_points[19] <=9):
        play sound "Sounds/spray.mp3"
        $ renpy.pause(1.0, hard=True)
        jump SandyPheromoneDay04
    "Leave, I don't have time for hanky-panky right now.":
        if (sandyfuckedlifeguard == True):
            scene sandybeach02d with dissolve
        if (sandyfuckedlifeguard == False):
            scene sandybeach02b with dissolve
        sa "What? Are you f*cking bl**dy kidding me???"
        p "Well, that's not very poetic language if I may say so..."
        if (sandyfuckedlifeguard == True):
            p "(I should go back to Pamela, I haven't been paid yet...)"
            jump BeachPamela01Day04
        jump ExploreBeachDay04

label SandyPheromoneDay04:
if (sandyfuckedlifeguard == True):
    scene sandybeach03b with dissolve
if (sandyfuckedlifeguard == False):
    scene sandybeach03 with dissolve
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
    jump SandyFuckDay04
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
    jump SandyFuckDay04   

label SandyPendulumDay04:
if (sandyfuckedlifeguard == True):
    scene sandybeachhypnob with dissolve
if (sandyfuckedlifeguard == False):
    scene sandybeachhypno with dissolve
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
jump ExploreBeachDay04

label SandyFuckDay04:
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
label SandyBlowDay04:
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
        jump SandyBlowDay04
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay04

label SandyFuckChoiceDay04:
menu:
    "Spoon her from the side" if (sandyside == False):
        jump SandySideDay04
    "Stick your cock between her huge jugs" if (sandytits == False):
        jump SandyTitsDay04
    "Take her from behind like a bitch in heat" if (sandydoggy == False):
        jump SandyDoggyDay04
    "Watch her bounce up and down your giant crank" if (sandyside == True) and (sandytits == True) and (sandydoggy == True):
        jump SandyFinalDay04

label SandySideDay04:
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
label SandySideDay04b:
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
        jump SandySideDay04b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay04

label SandyTitsDay04:
$ sandytits = True
scene sandytits01 with dissolve
play sound "Sounds/sandytitfuck01.mp3"
$ renpy.pause(2.0, hard=True)
sa "OOoh, my Prince Charming, my huge tits can't even bury that massive fuckstick, the head is sticking out..."
p "It will be sticking out way more once I do this..."
scene sandytits02 with dissolve
sa "It's so fucking big... Ssooo fucking big..."
label SandyTitsDay04b:
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
        jump SandyTitsDay04b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay04

label SandyDoggyDay04:
$ sandydoggy = True
scene sandydoggy01 with dissolve
$ renpy.pause(1.0, hard=True)
sa "My hole is all yours my Prince! Ram it in as deep as you like!"
p "Sure will do!"
scene sandydoggy01 with dissolve
play sound "Sounds/sandydoggy01.mp3"
$ renpy.pause(3.0, hard=True)
sa "AAAAH, it's so good feeling your giant teenage cock stretching my tiny fuckhole!"
label SandyDoggyDay04b:
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
        jump SandyDoggyDay04b
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay04

label SandyFinalDay04:
scene sandybeachkiss with dissolve
play sound "Sounds/sandyslut.mp3"
$ renpy.pause(3.0, hard=True)
sa "I'm going to bounce up and down your shaft and make you feel sssoo good my Prince... You'll pop in no time!"
stop music
play sound "Sounds/oceanwaves.mp3"
play music "Sounds/sandyfuckslow.mp3"
show sandyfuckslow
show faster
call screen sandyfuckslowday04
screen sandyfuckslowday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("SandyFuckFastday04")
label SandyFuckFastday04:
hide faster
play music "Sounds/sandyfuckfast.mp3"
show sandyfuckfast
show cum
call screen sandyfuckfastday04
screen sandyfuckfastday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("SandyFuckCumday04")

label SandyFuckCumday04:
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
jump ExploreBeachDay04

label TshirtHalleEnd:
stop music
play music "Sounds/oceanwaves.mp3"
scene hallebeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "So, what did you have in mind?..."
if (lust_points[9] >= 10):
    ha "I know what I have in mind... SEX!"
    if (stamina >= 1):
        p "What an amazing coincidence, I had the same idea!"
        jump HalleFuckDay04b
    if (stamina <=0) and (whitebull == False):
        p "Err... Yeah, that could sound like a great idea, but actually, I think it's, like... err... totally illegal to do that here."
        ha "What is wrong with you? I thought you were the adventurous type! What a disappointment! Get out of my face!"
        jump ExploreBeachDay04
    if (stamina <=0) and (whitebull == True):
        p "It might be a good idea to drink some white bull. RIGHT NOW!"
        menu:
            "Drink it":
                show whitebull
                show square
                play sound "Sounds/lost.mp3"
                "You gulped down your White Bull energy drink."
                hide square
                hide whitebull
                $ whitebull = False
                $ stamina += 2
                jump HalleFuckDay04b
            "Don't drink it":
                p "Err.. Yeah, that could sound like a great idea, but actually, I think it's, like... err... totally illegal to do that here."
                ha "What is wrong with you? I thought you were the adventurous type! What a disappointment! Get out of my face!"
                jump ExploreBeachDay04
                
menu:
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True) and (lust_points[9] >=8):
        jump HallePendulumDay04
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
        jump ExploreBeachDay04
    "Well, this place is nice and all that, but I've got to get going.":
        ha "So basically, you brought me here for nothing...Thanks for wasting my time. NOT!"
        $ lust_points[9] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump ExploreBeachDay04



label DowntownDay04:
stop music
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"
$ renpy.pause(1.0, hard=True)
p "The bus left me right in front of the main downtown plaza."
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_53
    $ lustaddedB = 1
    call Challenger from _call_Challenger_54
    $ lustaddedB = 1
    call Challenger from _call_Challenger_55
    $ challengercalls += 2

if (hour >= 19):
    p "It's getting late, I should really take the bus and get home now."
    $ bushome = True
    jump BusDowntownHomeDay04
else:
    jump DowntownChoiceDay04b

jump DowntownStraightChoiceDay04b

label BusDowntownHomeDay04:
p "Ah, here's the bus heading to the Burbs, I'd better take it..."
$ bushome = True
jump BusDriveDayb04

label DowntownChoiceDay04b:
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"

if (hour >= 19):
    p "It's getting late, I should really take the bus and get home now."
    jump BusDowntownHomeDay04

label DowntownStraightChoiceDay04b:
p "Where should I go?"
menu:
    "Go to Audacious HQ" if (discoveraudacious == True):
        jump AudaciousHQDay04
    "Go shopping":
        jump ShopDay04
    "Go to the massage parlour" if (discovermassage == True) and (parlourseen04 == False):
        jump Parlour01Day04
    "Take the bus home":
        $ bushome = True
        jump BusDowntownHomeDay04
    "Take the bus to the beach" if (hour <= 17):
        $ busbeach = True
        jump BusDowntownBeachDay04
    "Go to the downtown gym" if (discovergym == True) and (seengym04 == False):
        jump Gym01Day04
    "Put some posters up for Miss Titsworthy's campaign (+1hr)" if (principaldeal == True) and (posterup == False):
        jump PosterDay04
    "Go to Old Joe's Emporium" if (discoveremporium == True):
        jump PawnShop01Day04

label PosterDay04:
scene downtownposter with dissolve
$ renpy.pause(1.0, hard=True)
$ hour += 1
p "That's done. I almost feel ashamed, this slogan is so cheesy..."
$ posterup = True
jump DowntownChoiceDay04b

label BusDowntownBeachDay04:
p "Ah, here's the bus heading for the beach, I'd better take it..."
jump BusDriveDayb04

label PawnShop01Day04:
scene emporium01 with dissolve
$ renpy.pause(1.0, hard=True)
oj "Hello young man. Welcome to Old Joe's Emporium. We buy and sell all sorts of wares."
label PawnShop01Day04b:
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
                jump DowntownChoiceDay04b
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
                        jump DowntownChoiceDay04b
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
                                jump DowntownChoiceDay04b
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
                                jump DowntownChoiceDay04b
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
                        jump DowntownChoiceDay04b
    "What's this place?":
        oj "I just told you boy, are you deaf?"
        jump PawnShop01Day04b
    "Leave":
        jump DowntownChoiceDay04b

label AudaciousHQDay04:
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
            se "Hmm, OK, everything seems to be in order Mr...Visitor."
            jump AudaciousOffice01Day04

        "Let me through, my landlady's sister is the CEO of this company.":
            hide security01
            show security02
            se "And I'm the pope's daughter. Get out of here kid."
            $ audacioustried = True
            jump DowntownChoiceDay04b

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
                jump AudaciousOffice01Day04
            if (strength <=8):
                hide security01
                show security03
                se "We'll see about that!"
                play sound "Sounds/punch.mp3"
                $ renpy.pause(1, hard=True)
                if (blacktop04 == True):
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
                jump DowntownChoiceDay04b

if (audacioustried == True):
    p "I already tried getting into this building today. I should probably leave."
    jump DowntownChoiceDay04b

label ShopDay04:
if (evictedfromshop == True):
    "You are banned from entering this boutique until tomorrow. Bad boy. VERY bad boy."
    jump DowntownChoiceDay04b
if (shoppingseen04 == True):
    "You already went shopping today. Looks like you might be a shopaholic..."
    jump DowntownChoiceDay04b

label Shop01Day04:
$ shoppingseen04 = True
stop music
scene shopday04 with dissolve
play music "Sounds/shopmusic.mp3"
$ renpy.pause(1.0, hard=True)
p "This boutique looks very expensive..."
p "There's a nice-looking clerk standing behind the counter and several customers looking at skimpy swimsuits...The shop seems to be very busy today..."

label Shop01Day04b:
scene shopday04 with dissolve
menu:
    "Go talk to the clerk":
        jump ShopClerkDay04
    "Go talk to the black girl on the left":
        jump ShopCustomerDay04
    "Go talk to the redhead in the middle":
        jump ShopCustomerRedDay04
    "Go talk to the blonde on the right":
        jump ShopCustomerBlondeDay04
    "Go to the changing rooms" if (foundcabins == True):
        jump ShopCabinChoiceDay04
    "Leave":
        stop music
        jump DowntownChoiceDay04b

label ShopCustomerRedDay04:
scene shopred01 with dissolve
$ renpy.pause(1.0, hard=True)
re "Oh, you're a man, give me your advice. Should I choose the red or the green bikini?"
menu:
    "The red bikini, it will match your hair.":
        re "Yes, you're right, thank you!"
        jump Shop01Day04b    
    "The green bikini, it will match your eyes.":
        re "Yes, you're right, thank you!"
        jump Shop01Day04b
    "Imagine her naked":
        scene shopred01b with dissolve
        play sound "Sounds/dreaming.mp3"
        $ renpy.pause(2.0, hard=True)
        re "Err... Hello? Are you ogling my breasts? What a pervert!"
        sc "Stop disturbing the customers! This is a respectable establishment. I must ask you to leave at once!"
        $ evictedfromshop = True
        jump DowntownChoiceDay04b

label ShopCustomerBlondeDay04:
scene shopblonde01 with dissolve
$ renpy.pause(1.0, hard=True)
bl "Can't you see I'm busy thinking? There's too many new bikinis to choose from in this store!"
sc "Stop disturbing the customers!"
jump Shop01Day04b

label ShopClerkDay04:
scene shop01 with dissolve
sc "How may I help you?"
menu:
    "Talk to her":
        jump ShopTalkDay04
    "Buy something":
        jump ShopBuyDay04   
    "Leave the counter":
        jump Shop01Day04b

label ShopTalkDay04:
menu:
    "You know what would look good on you? Me.":
        scene shop03
        sc "Mmh, lemme think... Yes, it's the worst pick-up line ever."
        jump ShopClerkDay04
    "What's the word on the street downtown?":
        if (downtowntipgiven == True):
            sc "I already gave you a tip today. Stop pestering me."
            jump ShopClerkDay04
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
            jump ShopClerkDay04
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
            jump ShopClerkDay04
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
            jump ShopClerkDay04
    "What's going on today? It seems unusually busy...":
        sc "We have just received the new summer line of \"Audacious Bikinis\". People are going crazy for them."
        sc "We've also received the new \"Mega-sized Audacious Briefs for Boys\". But not many people seem interested in them unfortunately..."
        p "Err... I might be interested, I want to try one."
        sc "Oh great!, you can pick one from the shelf for your size and try it in one of the changing rooms, if you can find one that's empty..."
        $ foundcabins = True
        jump ShopClerkDay04
        

label ShopBuyDay04:
menu:
    "Buy swimsuit for customer (40$ - pay 20$ from your own pocket)" if (money >= 20) and(seenhallebikini == True) and (boughthallebikini == False):
        scene shop02
        play sound "Sounds/cashregister.wav"
        sc "Here you are. That's for one lucky girl!"        
        $ money -= 20
        $ boughthallebikini = True
        jump HalleGiftDay04

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
        jump ShopClerkDay04

    "Nothing actually":
        jump ShopClerkDay04

    "I don't have enough money to buy anything here." if (money <=9):
        sc "We don't do credit. We don't trust poor people like you."
        p "I feel like... dirt..."
        jump ShopClerkDay04

label ShopCustomerDay04:
scene halleshop01 with dissolve
$ renpy.pause(1.0, hard=True)
if (boughthallebikini == True) and (seenhallebikini == True):
    p "Hey, Halle, why are you still here? I bought you this swimsuit already!"
    show halleshop01b
    ha "Yeah, I know, but the dev is too lazy to remove me from this image..."
    ha "Remember, I'm ACTUALLY at the beach."
    jump Shop01Day04
elif (boughthallebikini == False) and (seenhallebikini == True):
    p "You're still staring at this swimsuit..."
    show halleshop01b
    ha "And I'll keep staring at it until you chip in 20 bucks to buy it for me!"
    jump Shop01Day04

else:
    menu:
        "May I help you with anything miss? Would you like to try this item in one of our cabins?":
            show halleshop01b
            ha "Oh...hum.. Sorry, I didn't realize you worked here... Well, I don't know, it's quite expensive..."
            p "Well, try it on, that's free anyway..."
            ha "Yeah, I guess you're right, I might as well try it on..."
            $ pretendshop = True
            jump HalleChangeDay04
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
                    jump HalleChangeDay04
                "That's too bad, cos I'm sure you would be a hit with that thing on...":
                    ha "(sigh)... Yes, it's too bad..."
                    jump Shop01Day04

label HalleChangeDay04:
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
            jump DowntownChoiceDay04b
        "Wait for her to come out":
            jump HalleBikini01Day04
else:
    ha "Hang on a minute, I'm almost ready..."

label HalleBikini01Day04:
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
        jump HalleBikini02Day04
    "Yeah, really hot... Turn around now...":
        ha "Like...that?"
        jump HalleBikini02Day04

label HalleBikini02Day04:
    scene hallebikini02 with dissolve
$ renpy.pause(1.0, hard=True)
if (pretendshop == True):
    p "Yes, that is a definitive perfect fit..."
    ha "Would...you..consider giving me a discount? I'm twenty bucks short to buy it and I really need a new bikini to go to the beach!"
    "The bikini is marked at 40 dollars..."
    menu:
        "Sure, for a girl like you, half-price! Give it to me and I'll make all the arrangements" if (money >= 20):
            ha "Oh, thank you sssoo much. My name is Halle by the way and I'll be wearing this at the beach if you ever fancy joining me (wink)!"
            jump ShopClerkDay04
        "Mmh, you'll have to show me more to get such a discount price miss...":
            jump HalleTopOffDay04
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
            jump Shop01Day04

else:
    p "Wow, you look really hot...err..."
    ha "The name's Halle. So, since you like it so much, time to chip in 20 bucks like you promised so I can buy it!"
    menu:
        "Ah... About that.. I just realized I don't have enough money." if (money <= 19):
            ha "But..You promised me!"
            p "OK, OK, as soon as I get the money, I'll come back I swear!"
            ha "I'll be here every afternoon, lamenting as to why I can't own this lovely bikini!"
            "Well at least, I know where to find her..."
            jump Shop01Day04
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
            jump Shop01Day04
        "Well, sure...sure... But a little incentive wouldn't hurt... If you know what I mean...":
            ha "I know what you mean...You boys are all the same..."
            jump HalleTopOffDay04
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
            jump ShopClerkDay04
            
label HalleTopOffDay04:
    scene halletopoff with dissolve
$ renpy.pause(1.0, hard=True)  
ha "So... Now that you've seen my big sumptuous tits... Time to cough up the money!"
p "Let me regain my breath first... WOW! I'll pay the difference for you baby!"
jump ShopClerkDay04

label HalleGiftDay04:
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
jump Shop01Day04
    
label ShopCabinChoiceDay04:
stop music
$ leftcabinseen = False
$ rightcabinseen = False
default d2randycabin = 0

scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
label ShopCabinChoiceDay04b:
p "Mmh, which cabin should I choose?"
menu:
    "The cabin on the left" if (leftcabinseen == False):
        jump ShopCabin01Day04
    "The cabin in the middle":
        jump ShopCabin02Day04
    "The cabin on the right" if (rightcabinseen == False):
        jump ShopCabin03Day04
    "Leave":
        scene shop01 with dissolve
        sc "So, did they fit you big boy? Are you ready to buy a pair?"
        p "Err... No, they're soiled actually, don't know how it happened really..."
        scene shop04 with dissolve
        sc "What? You're soiling my products? Get out of my shop immediately!"
        $ evictedfromshop = True
        jump DowntownChoiceDay04b

label ShopCabin01Day04:
play sound "Sounds/dooropen.mp3"
scene randyshop01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oh, it's that couple I saw on the beach on the first day I arrived!"
rc "Mmmh, I can see that got you horny!"
rb "Fuck yeah baby, let's do it right here... Hey, there's someone watching us!"
$ leftcabinseen = True
scene randyshop02 with dissolve
$ renpy.pause(1.0, hard=True)
rb "What are you looking at? Never seen a huge thick pre-teen monstercock before or what?"
rc "I doubt it honey, your young giant penis is the biggest ever! I bet he wants to watch, isn't that right boy?"
menu:
    "I don't have time for this lewd display!":
        rc "Pff, such a prude! Get outta here then, while I get my pussy wet to take my boyfriend's behemoth!"
        rb "Too bad for you buddy, you could have learnt a thing or two... I'm gonna pound her sweet pussy till she's begging for me to stop!"
        play sound "Sounds/doorclosing.mp3"
        jump ShopCabinChoiceDay04b
    "Ok, why not, I'm bored anyway. (50\%\ chance of +1 stamina)":
        rc "First, I'll get my pussy wet to take my boyfriend's behemoth! It's important since he's so gigantic..."
        rb "Watch this buddy. I'm gonna pound her sweet pussy till she's begging for me to stop!"
        jump RandyShop02Day04
        
label RandyShop02Day04:
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
$ d2randycabin=renpy.random.randint(0, 1)
if (d2randycabin == 0):
    $ stamina +=1
    show stamina01:    
        xalign 0.2 yalign 0.4   
        linear 1.0 yalign 0.2
    $ renpy.pause(2, hard=True)
    play sound "Sounds/more.mp3"
    hide stamina01
if (d2randycabin == 1):
    pass
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
jump ShopCabinChoiceDay04b

label ShopCabin02Day04:
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
jump ShopCabinChoiceDay04b

label ShopCabin03Day04:
stop music
play sound "Sounds/dooropen.mp3"
scene shopcabin03 with dissolve
$ rightcabinseen = True
cy "How rude, I'm all naked and you barge in here just as I was about to put on this bikini..."
p "Sorry but all the stalls are taken and I wanted to try on these new mega-sized briefs."
cy "Mega-sized briefs? Well maybe I could make some room for you in here then... But no touching naughty boy..."
cy "But first, let me put on this bikini..."
scene shopcabin03b with dissolve
$ renpy.pause(1.0, hard=True)
cy "What do you think? Will you be having problems putting on your briefs over that hardening rod, hee hee..."
menu:
    "I'll...try anyway if you don't mind...":
        jump ShopCabin03bDay04
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
        jump ShopCabinChoiceDay04b

label ShopCabin03bDay04:
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
        jump ChiyoFuck01Day04
    if (lust_points[3] >= 8) and (((pendulumactive == True) and (pendulum == True)) or (pheromone == True)):
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
                jump ChiyoPendulumDay04            
            "Spray yourself with pheromones" if (pheromone == True):
                window hide
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump ChiyoPheromoneDay04
            "Don't use anything":
                jump ChiyoNoFuckDay04
    if (lust_points[3] <= 7):
        jump ChiyoNoFuckDay04
    
if (dildo == False):
    p "I don't have a dildo, I have a REAL cock."
    cy "Too bad then that you don't have one.... I was really horny... But I'm not anymore, you spoilt the mood. Shoot little boy. Hee hee."
    p "What? But you can't leave me in such a state!"
    cy "Of course I can. You shouldn't be in the same stall as me anyway. The woman in the stall next door is horny, you can get that fat cock serviced by her."
    p "AAARGH!"
    play sound "Sounds/doorclosing.mp3"
    scene shopcabin01 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump ShopCabinChoiceDay04b
        
label ChiyoPendulumDay04:
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
    jump ChiyoFuck01Day04
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
    jump ChiyoFuck01Day04


label ChiyoPheromoneDay04:
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
    jump ChiyoFuck01Day04
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
    jump ChiyoFuck01Day04

label ChiyoFuck01Day04:
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
scene chiyofuck02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Come on, enough of that, I've got the real thing right here!"

if (lust_points[3] == 10):
    cy "Mmh, I know and it DOES look tasty... What would you want to do with it naughty naughty boy?"
    menu:
        "If it looks tasty, then give me a blowjob!":
            jump ChiyoBlowjobDay04
        "Your pussy looks tasty... And ready for a good pounding!":
            jump ChiyoPussyDay04

cy "I think you've seen enough naughtiness for the day. I came here to buy a bikini, not to get fucked by some random horse-hung boy. So you can leave now..."
p "AAARGH! She's doing it to me again!"
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
jump ShopCabinChoiceDay04b
            
label ChiyoBlowjobDay04:
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
label ChiyoBlowjobDay04b:
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
        jump ChiyoBlowjobDay04b
    "Your pussy looks tasty... And ready for a good pounding!" if (chiyopussy == False):
         jump ChiyoPussyDay04
    "It's time to stretch that gaping anus even more than that puny dildo you used!" if (chiyoblowjob == True) and (chiyopussy == True):
        jump ChiyoArseDay04

label ChiyoPussyDay04:
scene chiyopussy01 with dissolve
play sound "Sounds/chiyopussy01.mp3"
$ renpy.pause(7.0, hard=True)
p "That's nothing, I'm not even half-way in!"
scene chiyopussy02 with dissolve
play sound "Sounds/chiyopussy02.mp3"
$ renpy.pause(11.0, hard=True)
cy "Oh my God, you're so deep!"
label ChiyoPussyDay04b:
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
        jump ChiyoPussyDay04b
    "If it looks tasty, then give me a blowjob!" if (chiyoblowjob == False):
        jump ChiyoBlowjobDay04
    "It's time to stretch that gaping anus even more than that puny dildo you used!" if (chiyoblowjob == True) and (chiyopussy == True):
        jump ChiyoArseDay04

label ChiyoArseDay04:
scene chiyoarse01 with dissolve
$ renpy.pause(0.3, hard=True)
cy "I'm ready to have my little arsehole stretched by your naughty prick!"
play music "Sounds/chiyofuckslow.mp3"
show chiyofuckslow
show faster
call screen chiyofuckslow
screen chiyofuckslow:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("ChiyoFuckFast")
label ChiyoFuckFast:
hide faster
play music "Sounds/chiyofuckfast.mp3"
show chiyofuckfast
show cum
call screen chiyofuckfast
screen chiyofuckfast:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("ChiyoFuckCum")

label ChiyoFuckCum:
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
if (katsumifucked == True):
    show achievement04:
        xalign 0.5 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/achievement.mp3"
    $ renpy.pause(4.0, hard=True)
    hide achievement04
    $ achievement.grant("asian")

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
jump ShopCabinChoiceDay04b

label ChiyoNoFuckDay04:
cy "Looks like you won't be getting any Asian poontang from me today... Now shoot little boy, hee hee..."
p "Damn lustmeter! AARGH!"
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
jump ShopCabinChoiceDay04b

label Parlour01Day04:
scene parlour01
$ parlourseen04 = True
$ renpy.pause(1.0, hard=True)
play music "Sounds/parlourmusic.mp3"
ka "Welcome big American boy to \"Misohawny Massage Parlour\"! Me Katsumi, you want massage?"
menu:
    "I was told you did \"full-body massage\"...":
        ka "Yes, sucky sucky 50 dolla."
        p "Ah, I see. Sucky sucky indeed. That's quite expensive for just sucky sucky."
        ka "Me love you long time. For you, more than sucky sucky."
        p "Oh, the conversations we could have my dear..."
        jump ParlourChoiceDay04
    "Yes, how much is it?":
        ka "Normal massage? 10 dolla. More massage, 50 dolla."
        p "And what do I get for 50 dollars exactly?"
        ka "Sucky sucky 50 dolla."
        p "That's a lot of inflation since the Vietnam War..."
        jump ParlourChoiceDay04
    "Nope, not interested...":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceDay04b

label ParlourChoiceDay04:
menu:
    "Get a normal massage (10 $)" if (money >=10):
        jump NormalMassageDay04
    "Choose the \"full-body massage\" experience... (50 $)" if (money >=50) and (stamina >=1):
        jump FullMassageDay04
    "Mmh...I don't seem to have enough money at the moment." if (money <=9):
        ka "You poor. Hah hah. Me not poor. Come back when you not poor."
        p "I certainly will, if just for the highly stimulating conversations."
        jump DowntownChoiceDay04b
    "Mmh, I don't seem to have enough stamina at the moment." if(stamina == 0):
        ka "Ah! You not man enough. You leave and come back when you can cum."
        jump DowntownChoiceDay04b
    "Actually, I don't want anything right now.":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceDay04b

label NormalMassageDay04:
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
                jump Parlour05Day04
            "Forget it. Just give me a normal massage.":
                ka katsumi "Ok, me gonna massage your cock because ssooo BIG."
                jump Parlour05Day04
    "OK, OK, I'll pay the difference for a sucky sucky..." if (money >=40) and (stamina >=1):
        $ suckysucky = True
        $ fuckyfucky = True
        $ money -= 40
        jump Parlour05Day04
    "Why don't you just massage it then like if it was one of my big tense muscles?...":
        ka "Oooh, boy very smart. OK, me gonna massage big American cock. But no sucky sucky, you not pay."
        jump Parlour05Day04

label FullMassageDay04:
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
        jump Parlour05Day04        
    "That's cos all Asian men have small penises.":
        ka "Not true. Some Asian men big penis. You like Trump, you racist."
        ka "Me only do sucky sucky. No fucky fucky. Because you bad boy."
        $ fuckyfucky = False
        jump Parlour05Day04

label Parlour05Day04:
scene parlour05 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Big American monster boycock so big and hard!"
p "Yeah, play with it Katsumi! It's all yours!"

label Parlour06Day04:
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
                jump Parlour07Day04
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
                jump DowntownChoiceDay04b
    
label Parlour07Day04:  
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

label Parlour08Day04:  
scene parlour08 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Reaching top of monstercock take me so long... Me love you long time!"
p "Keep going, you still have quite a few inches to go..."

label Parlour09Day04:  
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
                jump DowntownChoiceDay04b

label Parlour10Day04:  
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
        
label ParlourFuckDay04:
stop music
play music "Sounds/katsumifuck.mp3"
show movieparlourfuck
show cum
call screen parlourfuckcumday04
screen parlourfuckcumday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("ParlourCumDay04")

label ParlourCumDay04:
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
jump DowntownChoiceDay04b

label Gym01Day04:
$ seengym04 = True
stop music
scene gym01 with dissolve
play music "Sounds/gymreception.mp3"
$ renpy.pause(1.0, hard=True)
if (wenttogymday03 == True):
    jump GymSecondDay04
da "Welcome to \"Jerk n' Clean Fitness Club \". My name is Daniella, how may I help you?"
label Gym01bDay04:
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
                jump Gym03Day04
            "Mmh, I'll think about it.":
                jump Gym01bDay04
    "I'm a member already. A LONG-STANDING \"member\" if you catch my drift...":
        show gym02 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "I tried to catch it but then it flew away..."
        jump Gym01bDay04
    "Why should I pay to join your gym when there are free gyms around the island?":
        da "Because our gym has the best equipment you can find on the island, that's why."
        p "I'm not convinced. You need to prove it."
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Alright Mr-Big-Shot. Follow me and I'll prove it!"
        jump Gym02Day04
    "Leave the gym":
        jump DowntownChoiceDay04b

label Gym02Day04:
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
        jump Gym03Day04
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
        jump Gym03Day04
    "Great, I'll try out the equipment straight away then. See you in a bit.":
        da "Err...Sure... I think..."
        jump Gym03Day04
    "Not convinced, I'll give it a pass for today.":
        da "Your choice, but you're missing out on some great fitness fun!"
        jump DowntownChoiceDay04b

label Gym03Day04:
scene dorisgym01 with dissolve
play music "Sounds/gymabience.mp3"
$ renpy.pause(1.0, hard=True)
"There's only one \"interesting\" customer in the gym at this time."
menu:
    "Do some heavy training (+1hr)" if (workout == False):
        jump GymWorkoutDay04
    "Approach the woman":
        jump GymDorisDay04

label GymWorkoutDay04:
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
        jump SaunaDorisDay04
    "I don't have time right now I'm afraid, it's getting late...":
        do "Too bad boy, we could have had some good time..."
        jump DowntownChoiceDay04b

label SaunaDorisDay04:
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
do "That's it, plaster me with your hot load! Show me you have what it takes to win that competittion boy!"
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
jump DowntownChoiceDay04b

label GymDorisDay04:
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
label DorisGymTrainDay04:
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
        jump DorisGymTrainDay04
    "Leave and do some heavy training (+1hr)" if (workout == False):
        jump GymWorkoutDay04    
    "Leave the gym":
        jump DowntownChoiceDay04b

label GymSecondDay04:
da "Welcome back to \"Jerk n' Clean Fitness Club \". Are you planning on using the gym again today?"
scene gym01 with dissolve
menu:
    "Yes, I am a fully-fledged member so it's free right?" if (gymmember == True):
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Of course, just make yourself at home [name]! I can go and get a tan now finally..."
        jump GymSecond01Day04
    "Yes, here's five bucks to use it for the day...(pay $5)" if (money >= 5):
        $ money -= 5
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Perfect, the gym is all yours... I can go and get a tan now finally..."
        jump GymSecond01Day04
    "Yes, and on becoming a fully-fledged member (pay $50)" if (money >= 50): 
        $ money -= 50
        $ gymmember = True
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Perfect, the gym is all yours... I can go and get a tan now finally..."
        jump GymSecond01Day04        
    "No, not really, just came to say \"Hi\".":
        show gym02 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Well, \"Hi\" and now \"Goodbye\"..."
        jump DowntownChoiceDay04b

label GymSecond01Day04:
$ wenttogym02 = True
scene gymanna01 with dissolve
play music "Sounds/gymabience.mp3"
$ renpy.pause(1.0, hard=True)
p "There's Anna in a tight outfit..."
if (seendorisgym01 == False) and (seendorissauna == False):
        p "And a muscular lady doing curls."
if (seendorissauna == True) or (seendorisgym01 == True):
        p "And Doris lifting a heavy barbell."
label GymChoiceDay04:
menu:
    "Do some heavy training (+1hr)" if (workout == False):
        jump GymWorkoutSecondDay04
    "Approach Anna" if (talkedannagym04 == False):
        jump GymAnnaDay04
    "Approach the muscular woman" if (seendorissauna == False) and (seendorisgym04 == False) and (seendorisgym01 == False):
        jump GymDorisDay04
    "Approach Doris" if ((seendorissauna == True) or (seendorisgym01 == True)) and (seendorisgym04 == False):
        jump GymDorisBellDay04
    "Go to the tanning rooms" if (seentanningbed04 == False):
        jump TanningDay04
    "Leave the gym":
        jump DowntownChoiceDay04b

label TanningDay04:
$ seentanningbed04 = True
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

$ freegym05 = True
p "Sounds like a $5 dollar reward for saving your life..."
da "Yeah, well, the gym is heavily in debt. I hope that the Muscle Stud competition on Saturday will attract many new female customers..."
p "I'll be in it!"
da "I have no doubt. Seeing how muscular and... big down there you are..."
da "Now I need to put on some fake untan lotion so I don't look like a lobster. Thanks again for saving me [name]!"
jump GymChoiceDay04


label GymAnnaDay04:
scene gymanna02 with dissolve
$ renpy.pause(1.0, hard=True)
an "Oh, hello [name]... I'm glad you're here, I don't really know what to do with this machine and the gym owner is not around..."
$ talkedannagym04 = True
menu:
    "Help her":
        jump GymAnnaHelpDay04
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
        jump GymChoiceDay04
    "Ask her if she wants to join you in the sauna":
        scene gymanna02b with dissolve
        $ renpy.pause(1.0, hard=True)
        an "I just arrived here, I haven't even worked out yet!"
        an "So no, I am not interested in wasting my time in the sauna with you...Goodbye [name]."
        jump GymChoiceDay04

label GymWorkoutSecondDay04:
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
jump GymChoiceDay04

label GymAnnaHelpDay04:
$ helpedannagym04 = True
p "Just sit on the bench with your head down, and then do crunches. I'll hold your legs for you if you want."
an "Oh, that's what this machine is for? I hope it works, I would really like to get better abs..."
menu:
    "Your abs are already pretty damn fit Ms Longrod...":
        an "Well, thank you for the compliment, but I have seen the gym owner and hers are like a wall of bricks!"
        an "So let's get to crunching then!"
        jump GymAnnaCrunchDay04
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
        jump GymAnnaCrunchDay04
        
label GymAnnaCrunchDay04:
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
jump GymChoiceDay04

label GymDorisBellDay04:
scene dorisbell01 with dissolve
$ renpy.pause(1.0, hard=True)
if (seendorisgym01 == True) or (seendorissauna == True):
    p "There's Doris training with what looks like a pretty heavy barbell..."
if (seendorisgym01 == False) and (seendorissauna == False):
    p "There's a muscular lady training with what looks like a pretty heavy barbell..."
$ seendorisgym04 = True
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
        jump GymDorisBell03Day04
    "Now I get why you are so muscular, this barbell is super-heavy!":
        do "Yeah, I'm the strongest woman on the island, wanna spot me?"
        p "Sure, I'll spot you Doris."
        jump GymDorisBell02Day04    
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
        jump GymDorisBell03Day04

label GymDorisBell02Day04:
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
                    jump SaunaDorisDay04                    
                "Na, no time, busy busy...":
                    do "You clearly don't have what it takes to become the island's Muscle Stud..."
                    jump GymChoiceDay04
        if (seendorisgym01 == True):
            do "Bailing out are we? How do you expect to win the Muscle Stud competition Saturday if you don't train?"
            p "I train every day! You'll see, I'll be ready on Saturday, I'm da man, I'm DA MAN!"
            do "Well go and play with your tiny toys boy, I'm gonna add some more weights to this barbell, I'm not done with my training yet."
            jump GymChoiceDay04
        if (seendorisgym01 == False):
            do "Too bad, I was looking for a muscle stud to take under my wing for the upcoming Muscle Stud Competition..."
            p "No, I'm a muscle stud, I swear! What's that competition about?"
            do "About more than muscles... Hence the stud part... You'll find out on Saturday. If you don't chicken out."
            jump GymChoiceDay04
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
        jump GymChoiceDay04
    "Pff, piece of cake for me, I'm DA MAN, I'll show you!":
        jump GymDorisBell03Day04
  
label GymDorisBell03Day04:
scene dorisbell08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Alright, here we go..."
#if (strength >= 10):
#    scene ryanbell03
#    $ renpy.pause(1.0, hard=True)
#    scene ryanbell02
#    $ renpy.pause(0.3, hard=True)
#    scene ryanbell01
#    $ renpy.pause(1.0, hard=True)
#    scene ryanbell02
#    play sound "Sounds/workoutgroan.mp3"
#    $ renpy.pause(0.5, hard=True)
#    p "See? I told you, piece of cake, I'm DA MAN!"
#    do "Very impressive... You might just make the cut at the end of the day..."
#    $ lust_points[6] +=1
#    $ score += 1
#    show lust01:
#        xalign 0.2 yalign 0.6
#        linear 1.0 yalign 0.4
#    play sound "Sounds/more.mp3"
#    $ renpy.pause(2, hard=True)
#    hide lust01

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
jump GymChoiceDay04

label AudaciousOffice01Day04:
$ seenaudaciousday04 = True
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
            $ camera = False 
            $ stolecamera = False
            jump AudaciousOffice01Day04b
        "Yeah, go ahead, I'm not scared, I ain't done nuffin wrong!":
            st "That's it, you're done for mister!"
            $ stolecamera = False
            jump AudaciousCopDay04
if (stolecamera == False):
    jump AudaciousNoCopDay04

label AudaciousCopDay04:
$ audacioustried = True
scene audaciouscop01 with dissolve
$ renpy.pause(1.0, hard=True)
co"What seems to be the matter?"
st "This boy stole a camera from us! He tricked me into believing he was a photographer!"
co"That's it, follow me to the police station immediately!"
if (wenttojail == True):
    p "What? Not AGAIN! Damn, it's pretty easy to accuse people in this country and get them arrested. Good thing I'm not black."
    jump AudaciousCop02Day04
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

label AudaciousCop02Day04:
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
        jump CopFuckBlowDay04
    "Let me out of here or I'll report you for police brutality!":
        co"And you really think anyone will believe you? We can either do this MY way or we'll do this the HARD way!"
        co"Now I'll open the door, don't do anything silly or I'll tase you..."
        jump CopFuckDay04
    "Now that you've seen my massive dong, get on your knees and suck it bitch!":
        co"I don't take orders from a BOY! Even if he's carrying more meat than any man I've ever seen... As a punishment, I'll let you rot in this cell a while longer!"
        jump CopNoFuckDay04
        
        
label CopNoFuckDay04:
scene black with dissolve
$ renpy.pause(1.0, hard=True)
p "Noooo! I need to fuck girls to win and I can't fuck any here!... When will this nightmare end?"
$ lustaddedB = 2
call Challenger from _call_Challenger_56
$ lustaddedB = 2
call Challenger from _call_Challenger_57
$ lustaddedB = 2
call Challenger from _call_Challenger_58
$ lustaddedB = 2
call Challenger from _call_Challenger_59
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
        jump EveningChoiceDay04
    "They brutalized me Nancy, and they threw me in a dirty cell for hours....sniff...":
        show jailmom01b
        m "Oh, sweetie, this is terrible... Let's go home and try and forget about this... Stay out of trouble and everything will be fine..."
        $ hour += 1
        stop music
        jump EveningChoiceDay04

label CopFuckBlowDay04:
scene copblow01 with dissolve
$ renpy.pause(1.0, hard=True)
co"First, you are going to unload that weapon down my throat! And you'd better be quick!"
if (stamina <= 0) and (whitebull == True):
    co"What's wrong? You can't deliver?"
    p "Err... I'm kind of tired, you know, busy busy day and all that...(Shit, she took all my belongings and I can't even drink a White Bull...)"
    co"Is that so? Then, I'll make your day less busy by locking you up in this cell until this evening, limp dick!"
    jump CopNoFuckDay04

if (stamina <= 0):
    co"What's wrong? YOu can't deliver?"
    p "Err... I'm kind of tired, you know, busy busy day and all that..."
    co"Is that so? Then, I'll make your day less busy by locking you up in this cell until this evening, limp dick!"
    jump CopNoFuckDay04

label CopFuckBlowDay04b:
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
label CopFuckDay04:
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
jump DowntownChoiceDay04b

label AudaciousNoCopDay04:
scene secretary01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I think I'm on the corporate floor..."
label AudaciousOffice01Day04b:
scene secretary01 with dissolve
st "How may I help you?"
menu:
    "Where's the CEO's office?" if (debbyofficeseen == False) and (debbyofficeseen04 == False):
        st "Do you have an appointment?"
        p "Err... Yeah, sure, I'm a big time swimwear buyer, I need to sign a contract with her."
        scene secretary04 with dissolve
        $ renpy.pause(1.0, hard=True)
        st "Alright, it's down the hallway on your right..."
        p "Well thank you. (That was easy...)"
        jump DebbyOffice01Day04
    "I'm a photographer. Nudge nudge, wink wink." if (hour <=18) and (seenshoot03 == False) and (seenshoot04 == False):
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
        jump Shoot01Day04
    "A receptionist needs good oral skills. Let me test yours...":
        scene secretary02 with dissolve
        $ renpy.pause(1.0, hard=True)
        st "Quit it cowboy, I ain't falling for that...."
        jump AudaciousOffice01Day04b
    "Leave the building":
        jump DowntownChoiceDay04b
    "Look for mom's office" if (seenmomofficeday04 == False):
        jump MomOffice01Day04

label Shoot01Day04:
$ seenshoot04 = True
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

label Shoot02Day04:
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
        jump Shoot03Day04
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
        jump AudaciousEscapeDay04

label Shoot03Day04:
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
        jump EndShootDay04

    "The gangbang scene with ten men.":
        aj "Nothing like a bukkake session with tons of cum plastering my huge breasts..."
        p "Well I'm a bukkake machine all by myself..."
        scene shoot08 with dissolve
        $ renpy.pause(1.0, hard=True)
        aj "Is that so? I demand some proof Mr Hank..."
        p " Sure thing, I'll offer you ounces of proof...."
        aj "Mmh, such devotion to your job mr photographer... Bring that crank over here then..."
        jump ShootFuckDay04

    "The scene with the amateur fan.":
        aj "Yes, that was tons of fun. The poor sod was so worried at first, but he gained confidence and then pounded me just as hard as a veteran pornstar."
        scene shoot08 with dissolve
        $ renpy.pause(1.0, hard=True)
        aj "Too bad there isn't someone like him right here... I'm so horny..."
        p "I can volunteer... I'm a major fan myself..."
        aj "Mmh, such devotion to your job mr photographer... Bring that crank over here then..."
        jump ShootFuckDay04


label ShootFuckDay04:
stop music
scene shoot09 with dissolve
$ renpy.pause(1.0, hard=True)
aj "Damn kid, that's the biggest \"crank\" I've ever seen and I've seen hundreds of pornstar dongs!"
p "Enough talking, put that mouth to good use and gobble my shaft as deep as you can!"
aj "I'll try..."
label ShootFuckMouthDay04:
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
        jump ShootFuckMouthDay04
    "Move on":
        pass

label ShootFuckPussyDay04:
p "You're doing good. Not many girls can gobble up my monster dong like that!"
aj "I'm not the winner of \"Pornstar Mouth of the Year\" five years in a row for nothing Mr Hank!"
p "Let's test your \"Pornstar Pussy of the Year\" then..."
aj "Ok, but be caref....."
scene shoot12 with dissolve
$ renpy.pause(1.0, hard=True)
aj "AAAH, You're going ssooo deep! Yes, I want more, pound that pussy, I'm creaming all over that giant cock!!!"
label ShootFuckPussyDay04b:
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
        jump ShootFuckPussyDay04b
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

label EndShootDay04:
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
jump DowntownChoiceDay04b

label AudaciousEscapeDay04:
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
scene downtownaudacious with dissolve
$ renpy.pause(1.0, hard=True)
jump DowntownChoiceDay04b

label DebbyOffice01Day04:

if (hour <= 18):
    jump DebbyOffice01bDay04
if (hour > 18):
    scene debbyoffice02 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Looks like Debby isn't in her office. She must have gone home, it's getting quite late actually... I should leave too."
    jump DowntownChoiceDay04b

label DebbyOffice01bDay04:    
scene debbyoffice01 with dissolve
$ renpy.pause(1.0, hard=True)
$ debbyofficeseen04 = True
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
        jump DowntownChoiceDay04b
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
        jump AudaciousOffice01Day04b
    "I would like to offer my services as a critic of your lovely swimsuits.":
        show debbyofficeneutral
        d "That's a bit bold young man... But as it turns out, I have just received this new bikini from our R&D department..."
        show debbyofficedevious
        d "Perhaps you would like to see me wearing it and give your \"professional\" opinion?"
        menu:
            "Sure aunt Debby!":
                d "Such eagerness... Well go and wait in the corridor and I'll call you back in once I'm ready..."
                $ lust_points[5] +=1
                $ score += 1
                show lust01:
                    xalign 0.6 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01
                jump DebbyOffice02Day04
            "I wouldn't want to intrude. Maybe you have a hot.. I mean a model for this kind of work?":
                show debbyofficeneutral
                d "Of course, but I always beta-test the new swimsuits first... since I'm the CEO. So take it or lose it!"
                p "I'll take it of course!"
                d "Then go and wait in the corridor and I'll call you back in once I'm ready..."
                jump DebbyOffice02Day04

label DebbyOffice02Day04:
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
        jump DebbyOffice04Day04
    "Wow, Debby, you look fabulous in it!":
        d "Well, that's very nice of you to say, but you're supposed to be a critic for the BIKINI, not me..."
        d "I guess you don't have what it takes to be a swimsuit critique, you are too easily distracted by the person wearing in it... (sigh)"
        p "Well...err... I didn't mean to..."
        d "It's best if you leave the building now [name], since your services are not required, you have now become \"unauthorized\" personnel..."
        scene downtownaudacious with dissolve
        p "I don't think I'm gonna be allowed back in today. I really pissed her off..."
        jump DowntownChoiceDay04b
    "Feel up her breasts":
        if (blacktop04 == True):
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
        jump DowntownChoiceDay04b

label DebbyOffice04Day04:
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
    if (blacktop04 == True):
        scene debbyoffice08black with dissolve
    else:
        scene debbyoffice08 with dissolve            
    $ renpy.pause(2.0, hard=True)
    d "Oops... See what a dirty whore I am... I guess I have no choice but to pull my bottom down too now... So you can FUCK ME MY STUD NEPHEW!"
    jump OfficeDebbyFuckChoiceDay04
    
menu:
    "pull the string up":
        if (blacktop04 == True):
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
            jump OfficeDebbyFuckChoiceDay04
        d "Oops, pull it down now [name], you've \"inspected\" the fabric enough now..."
        d "Thanks for your help [name], but now I have a lot of work to do..."
        p "Sure Debby, I'll leave you to it then."
        jump AudaciousOffice01Day04b        
    "Feel up her breasts":
        if (blacktop04 == True):
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
        jump DowntownChoiceDay04b

label OfficeDebbyFuckChoiceDay04:
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
            jump DebbyFuckChoiceDay04b
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
            jump DowntownChoiceDay04b        
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
    jump DowntownChoiceDay04b        

label OfficeDebbyFuckChoiceDay04b:
scene debbyofficeprefuck01 with dissolve
menu:
    "Let me fuck your dirty hole nice and slow!" if (debbychair == False):
        jump OfficeDebbyChairFuckDay04
    "Give me a nice sloppy blowjob slave!" if (debbyblow == False):
        jump OfficeDebbyBlowDay04
    "I want to maul your hard nipples with my teeth!" if (debbymaul == False):
        jump OfficeDebbyNippleDay04
    "A cheap whore like you deserves a good pussy-pounding!" if (debbydoggy == False):
        jump OfficeDebbyDoggyDay04
    "Time to finish me off slave!" if (debbymaul == True) and (debbydoggy == True) and (debbyblow == True) and (debbychair == True):
        jump OfficeDebbyMovie
    
label OfficeDebbyBlowDay04:
$ debbyblow = True
scene debbyblowoffice01 with dissolve
$ renpy.pause(1.0, hard=True)
d "Let me lick your bull-sized balls while you pleasure yourself between my tits Master!"
scene debbyblowoffice02 with dissolve
$ renpy.pause(1.0, hard=True)
label OfficeDebbyBlowDay04b:
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
        jump OfficeDebbyBlowDay04b
    "Move on":
        p "You did good slave, it's now time to move on to something else..."
        jump OfficeDebbyFuckChoiceDay04b

label OfficeDebbyChairFuckDay04:
$ debbychair = True
scene debbyofficefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Offer your gaping slut-hole to my massive teenage cock slave!"
d "My filthy hole belongs to you Master... Do as you please with it!"
label OfficeDebbyChairFuckDay04b:
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
        jump OfficeDebbyChairFuckDay04b
    "Move on":
        p "I've punished your dirty hole enough for the moment slave... I'm giving you a respite..."
        d "Thank you Master, I am not worthy of such generosity..."
        jump OfficeDebbyFuckChoiceDay04b

label OfficeDebbyNippleDay04:
if (blacktop04 == True):
    scene debbyofficenippleblack with dissolve
else:
    scene debbyofficenipple with dissolve      
play sound "Sounds/sucking.mp3"
$ renpy.pause(1.0, hard=True)
d "Ooh, you suck on my nipples ssoo good! Maul my tits Master!"
p "They look red and erect now, it's time for something else slave..."
$ debbymaul = True
jump OfficeDebbyFuckChoiceDay04b

label OfficeDebbyDoggyDay04:
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
label OfficeDebbyDoggyDay04b:
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
        jump OfficeDebbyDoggyDay04b
    "Move on":
        p "Your dirty hole is creaming all over the place, let's switch position whore!"
        jump OfficeDebbyFuckChoiceDay04b


label OfficeDebbyMovie:
stop music
play music "Sounds/debbyslow.mp3"
show debbyofficeslow
show faster
call screen officedebbyfuckslowday04
screen officedebbyfuckslowday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("OfficeDebbyFuckFastDay04")

label OfficeDebbyFuckFastDay04:
hide faster
play music "Sounds/debbyfast.mp3"
show debbyofficefast
show cum
call screen officedebbyfuckfastday04
screen officedebbyfuckfastday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("OfficeDebbyFuckCumDay04")

label OfficeDebbyFuckCumDay04:
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
jump DowntownChoiceDay04b

label MomOffice01Day04:
$ seenmomofficeday04 = True
if (hour <= 17) and (seenmomofficeday03 == False):
    scene momwork01 with dissolve
    $ renpy.pause(1.0, hard=True)
    m "[name]! How the hell did you get in here??? You should really leave sweetie, I'm busy with work."
    p "I just wanted to see where you work mom!"
    m "Well now you've seen. Get back home before a security guard finds you, I don't want any trouble from you here!"
    p "Ok mom, I'm sorry... (I'd better leave)."
    $ seenmomofficeday04 = True
    jump AudaciousOffice01Day04b

if (hour <= 17) and (seenmomofficeday03 == True):
    scene momwork01 with dissolve
    $ renpy.pause(1.0, hard=True)
    m "Oh, hello sweetie! YOu came to see your hard-working mom again? I'm sorry, but I'm very busy... Debby is really pushing me, I'm exhausted..."
    menu:
        "Ok mom, I'll see you tonight then... (I'd better leave).":
            jump AudaciousOffice01Day04b
        "Maybe I could give you a massage?":
            m "Mmh, why not, I could certainly do with a footrub at least..."
            $ gavemommassage04 = True
            jump MomMassageDay04

if (hour >= 18):
    scene momofficeempty with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Looks like mom isn't in her office. She must have gone home, it's getting quite late actually... I should leave too."
    jump DowntownChoiceDay04b

label MomMassageDay04:
if (blacktop04 == True):
    scene mommassage01black with dissolve
if (blacktop04 == False):
    scene mommassage01 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/womansigh.mp3"
m "Thank you my sweet little pumpkin, I feel more relaxed now..."
if (lust_points[16] <= 8):
    $ lust_points[16] +=1
    $ score += 1
    show lust01:
        xalign 0.35 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (blacktop04 == True):
    scene mommassage02black with dissolve
if (blacktop04 == False):
    scene mommassage02 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/kissing.mp3"
m "You'd better leave now [name], you really shouldn't be coming to my workplace, you might get me in trouble..."
p "Alright mom, see you tonight at dinner!"
jump AudaciousOffice01Day04b
    
label DinnerDay04:
stop music
if (blacktop04 == True):
    scene dinnerday03ablack with dissolve
else:
    scene dinnerday03a with dissolve
$ renpy.pause(1.0, hard=True)
m "Enjoy your meal kids!"
s "Thanks mom, it looks delicious as always!"
if (maddysaved == True):
    m "I heard on the radio on the way back from work that SOMEONE saved a schoolgirl who had been kidnapped..."
    m "And then, they mentioned the name of her savior, and it was YOU [name]! I'm so proud of you!"
    if (nancyfucked == True):
        show dinnerday03c
        s "Oh, wow, congrats [name]! Maddy must have been so happy seeing you rescue her..."
        p "Err.. Yeah, she was very grateful..."
        m "I could spend the evening with my hero tenant... We could watch a movie? Would you like that [name]?"
        p "Err...Sure Nancy. But I might be busy tonight... After all the fighting I had to do to rescue Maddy..."
        m "Oooh, sure [name], whatever you choose.... Mommy will be there for you."
        hide dinnerday03c        
        jump DinnerDay04b
    if (lust_points[16] == 9):
        $ lust_points[16] +=1
        $ score +=1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        if (lust_points[16] == 10):
            show epiclust:
                xalign 0.6 yalign 0.2
                zoom 0.5
                linear 2.0 zoom 1.0
            play sound "Sounds/epiclust.mp3"
            $ renpy.pause(4.0, hard=True)
            hide epiclust
            m "I want to spend the evening with my hero tenant... We could watch a movie? Would you like that [name]?"
            p "Sure Nancy! I already have a movie in mind..."
            $ momsavior = True
            show dinnerday03c
            s "Oh, wow, congrats [name]! Maddy must have been so happy seeing you rescue her..."
            p "Err.. Yeah, she was very grateful..."
            jump DinnerDay04b
    if (lust_points[16] <= 8):
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
            m "Mommy wants to spend the evening with her hero son... We could watch a movie? Would you like that [name]?"
            p "Sure mom! I already have a movie in mind..."
            $ momsavior = True
            show dinnerday03c
            s "Oh, wow, congrats [name]! Maddy must have been so happy seeing you rescue her..."
            p "Err.. Yeah, she was very grateful..."
            jump DinnerDay04b
        show dinnerday03c
        s "Oh, wow, congrats [name]! Maddy must have been so happy seeing you rescue her..."
        p "Err.. Yeah, she was very grateful..."
        m "Mommy could spend the evening with her hero son... We could watch a movie? Would you like that [name]?"
        p "Err...Sure mom. But I might be busy tonight... After all the fighting I had to do to rescue Maddy..."
        m "Oooh, sure [name], whatever you choose.... Mommy will be there for you."
        hide dinnerday03c        
        jump DinnerDay04b
    
show dinnerday04a
m "I heard some terrible news on the radio. A girl from your school is reported missing. Is that right?"
show dinnerday04b
s "Yes, it's Maddy, she's in [name]'s class actually. No one knows what happened to her, it's quite worrying..."
if (maddylead == True):
    p "I have a lead."
    hide dinnerday04b
    show dinnerday03c
    s "A lead? Are you playing detective now [name]?"
    p "Yeah, I've been investigating, I think she was kidnapped by some shady guy I saw on the bus."    
    m "Oh my God, that's terrible! Poor girl, I hope they find her soon, she must be living a nightmare..."
    s "José said he had a lead too, apparently, he's also been investigating..."
    p "What? What a douchebag! He only does it to get inside her panties I bet!"
    s "Right. Cos of course, you just do it for nothing..."
    p "I do it out of the kindness of my heart!"
    s "Well, she's quite pretty and muscular, although not as much as me... (wink)"
    m "Enough bickering you two! Think about this poor girl..."
    hide dinnerday03c
    jump DinnerDay04b
show dinnerday03c
s "José says he has a lead, he's been investigating..."
p "What? What a douchebag! He only does it to get inside her panties I bet!"
m "Enough bickering you two! Think about this poor girl..."
hide dinnerday03c
    
label DinnerDay04b:
m "Now finish up your meal, and don't forget to do the dishes afterwards!"
s "Sure mom, I'll do the washing and [name] will do the drying, as usual... "
s "Cos we can't trust him with cleaning up the dishes properly..."
p "My hands can't get wet. I need to maintain a firm grip on...err... my dumbbells."
if (momsavior == False):
    "You finish cleaning up the dishes and head to your room."
    jump EveningChoiceDay04
if (momsavior == True):
    "You finish cleaning up the dishes and head to the living room."
    jump EveningMomSaviorDay04

label SisRoomEveningDay04:
stop music
$ nightsisroomseen04 = True
if ((lust_points[17] == 10) and (sisanal == False)):
    jump SisRoomEveningDay04b
elif ((lust_points[17] <= 9) and (nikkijosewin == True)):
    jump SisRoomEveningDay04c
else:
    jump SisRoomEveningDay04d

label SisRoomEveningDay04b:
scene sisbed01b with dissolve
$ renpy.pause(1.0, hard=True)
$ locroom = False
s "Hi [name], what's up? You came to finish off what you tried to start but failed miserably to finish?"
if (stamina >= 1):
    p "Yeah, my problem is solved! My huge cock is now ready to rumble!"
    scene sisbed03b with dissolve
    $ renpy.pause(1.0, hard=True)
    s "Alright, finally! I was starting to think you were a wimp or something... Come and kiss me then..."
    jump SisUndress01Day04
if (stamina <= 0) and (whitebull == False):
    p "Err, no actually, I still have some problems with my... err.. thingie."
    scene sisbed01c with dissolve
    s "You should really go and see a doctor about that, it sounds terrible..."    
    p "Hum, well, I hope it will get better tomorrow. Have a good night Nikki, see you in the morning."
    jump EveningChoiceDay04
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
    p "Yeah, my problem is solved! My huge cock is now ready to rumble!"
    scene sisbed03b with dissolve
    $ renpy.pause(1.0, hard=True)
    s "Alright, finally! I was starting to think you were a wimp or something... Come and kiss me then..."
    jump SisUndress01Day04

label SisRoomEveningDay04c:
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
    jump SisFuckday04
p "You're much better off hanging out with nice people like me who would never do such a horrible thing as take a picture of someone naked..."
scene sisbed01 with dissolve
s "I'm sorry I didn't trust you... I'll bear that in mind in the future...But right now, I'm feeling really tired. Have a good night [name]!"
jump EveningChoiceDay04

label SisRoomEveningDay04d:
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
        jump EveningChoiceDay04
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
        jump EveningChoiceDay04
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
            jump SisFuckday04        
        s "Let me kiss the pain away [name]..."
        scene sisbed05 with dissolve
        $ renpy.pause(1.0, hard=True)
        s "Mmh, I can't feel your HUGE bulge against my thighs... But it's not right. It's not right, right?"
        p "It IS right! It IS right!"
        s "Another day perhaps [name]. When it will feel righter. Have a good night (kiss)."
        jump EveningChoiceDay04

label SisFuckday04:            
if (stamina <= 0) and (whitebull == False):
    p "Err, you know what, I'm like, having little, nothing to worry of course,... urinary problems right now, let's put this off until tomorrow."
    s "Eeew. I didn't want to know that! OK, go back to your room and sort that useless floppy wiener issue FAST!"
    $ hour += 1
    jump EveningChoiceDay04
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
    jump SisUndress01Day04
label SisUndress01Day04:    
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
label SisFuckChoicesDay04:
menu:
    "Maybe we should start off with a gentle blowjob." if (sisblowjob == False):
        jump SisBlowjobDay04
    "How about I lick your pussy to get it nice and wet?" if (sispussy == False):
        jump SisPussyDay04
    "I'm gonna pound that arse of yours to oblivion!" if (sisanal == False):
        jump SisAnalDay04
    "Let's fuck, like, for real!" if (sisall == 3):
        jump SisRealFuckDay04

label SisPussyDay04:
scene nikkilick01 with dissolve
$ sisall += 1
play music "Sounds/lick.mp3"
$ renpy.pause(1.0, hard=True)
$ sispussy = True
s "Oh, God, you're so good at this, I'm cumming!, AAAHH!"
s "Thanks [name], I really needed that... Now it's my turn to pleasure that rock-hard donkey-sized cock of yours!"
stop music
jump SisFuckChoicesDay04

label SisBlowjobDay04:
scene nikkilowjob01 with dissolve
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
            jump SisBlowjobCumDay04
        "Don't blow your load":
            jump SisFuckChoicesDay04
else:
    s "Keep that hardon, I want you to fuck me with your huge cock!"
    p "Phew, that was ssoo close..."
    jump SisFuckChoicesDay04

label SisBlowjobCumDay04:
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
jump SisFuckChoicesDay04

label SisAnalDay04:
scene nikkianal01 with dissolve
$ sisall += 1
$ backdoor += 1
play sound "Sounds/threesomefuck.mp3"
$ renpy.pause(1.0, hard=True)
$ sisanal = True
s "Be gentle [name], you're too rough!"
p "Sorry, I got carried away, your arse is so warm and tight... Let's switch position."
stop sound
jump SisFuckChoicesDay04

label SisRealFuckDay04:
stop music
play music "Sounds/sisfuck.mp3"
show movienikkifuck
show cum
call screen sisfuckcumday04
screen sisfuckcumday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("SisFuckCum01day04")

label SisFuckCum01day04:
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
$ fuckedschoolgirlday04 = True
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
jump EveningChoiceDay04

label EveningMomSaviorDay04:
scene eveningtvmom01 with dissolve
$ renpy.pause(1.0, hard=True)
m "I'm ready! So, what movie did you end up choosing to entertain us tonight?"
p "Conan the Barbarian. It's about a muscle kid who grows up to become a hero and save the world..."
m "Oh? How appropriate!"
jump MovieConanDay04b

label EveningMovieDay04:
scene eveningtvmom01 with dissolve
$ renpy.pause(1.0, hard=True)
m "I was about to watch a movie, but I'm not really a movie buff. Do you have an idea sweetie?"
if (nancyfucked == True):
    p "I guess we watched Conan already, so we'll watch Alien then."
    m "Alright, I've never seen it before."
    jump MovieAlienDay04
menu:
    "Conan the Barbarian":
        m "Alright, I've never seen it before."
        jump MovieConanDay04
    "Alien":
        m "Alright, I've never seen it before."
        jump MovieAlienDay04

label MovieConanDay04b:
scene eveningconan with dissolve
play music "Sounds/conan.mp3"
$ renpy.pause(2.0, hard=True)
m "This movie is terrible, but I liked the beginning, where the muscle kid with the big bulge grows up... It made me horny [name]!"
stop music
scene ryanconanposing02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Look mom, I'm just like him, only with a MUCH bigger bulge!"
m "It looks so big.... and not even hard. I know it's wrong but I need NEEDS to feel up that monster!"
scene eveningmomstrap with dissolve
$ renpy.pause(1.0, hard=True)
m "Mmmh, honey, this is the biggest thing I've ever felt in my life... My tiny hands can't even wrap around your giant boycock. Let me see it please, I beg you!"
p "I'm getting really hard Nancy watching you worshipping my bulge like that... FUCK!"
scene eveningmomrip with dissolve
play sound "Sounds/rip.mp3"
$ renpy.pause(1.0, hard=True)
m "Oh my God! Your massive rock-hard cock just ripped right through your jockstrap!"
p "That's cos you're making me so horny Nancy... Please take off your blouse... I'll turn the lights on..."
m "I don't know... It's just so wrong... Just a peek for my horse-hung muscle stud then!"
scene eveningmomfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
m "You like what you see [name]? What would you like me to do next my studly tenant?"
menu:
    "I need to stick my cock between those big jugs...":
        jump MomTitfuckDay04
    "I don't know but I'm about to explode!":
        jump MomBlowjobDay04

label MovieConanDay04:
scene eveningconan with dissolve
play music "Sounds/conan.mp3"
$ renpy.pause(2.0, hard=True)
$ hour += 1
m "This movie is terrible, but that foreign actor... Mmmh, he sure has huge muscles...everywhere... Whoever he is."
label MovieChoiceDay04b:
menu:
    "It's Schwarzenpecker, everybody knows him, he's super-famous... You've got to go out more often.":
        m "I DO go out, but not to watch that kind of drivel! I'm tired, I'll leave you with your \"super-famous\" actor with a weird accent then!"
        jump MovieMomLeftDay04
    "He's got nothing on me, I bet I have bigger muscles than him!":
        m "If you want to go around pretending that, you need to walk the walk and not just talk the talk, [name]..."
        p "I could pose in my jockstrap and flex my biceps so you can compare with him on the screen! Then, you'll be convinced!"
        m "Alright [name]. Let's see what you've got mister. This is going to be more entertaining than this drivel of a movie!"
        menu: 
            "Do it!":
                jump MovieConan02Day04
            "Do it but use one stamina point to really flex your muscles hard":
                jump MovieConan03Day04
            "Don't do it, Arnie is clearly bigger than you...":
                m "See? Don't brag if you can't follow up, there's a life lesson for you."
                m "I'm tired, I'll leave you to your silly barbarian..."
                jump MovieMomLeftDay04
            "First, drink some white bull because it looks like it might become interesting...." if (stamina <= 0) and (whitebull == True):
                show whitebull
                show square
                play sound "Sounds/lost.mp3"
                "You gulped down your White Bull energy drink."
                hide square
                hide whitebull
                $ whitebull = False
                $ stamina += 2
                jump MovieChoiceDay04b
            "Shit, Nancy looks horny enough but I'm not, my stamina is too low...." if (stamina <= 0) and (whitebull == False):
                m "See? Don't brag if you can't follow up, there's a life lesson for you."
                m "I'm tired, I'll leave you to your silly barbarian..."
                jump MovieMomLeftDay04

label MovieAlienDay04:
scene eveningalien with dissolve
play music "Sounds/alien.mp3"
$ renpy.pause(2.0, hard=True)
$ hour += 1
m "This movie is really scary. I don't think I can finish watching it. I'll leave you to it [name]."
p "But Nancy.... The alien is about to kill everyone, you're missing the best bit!"
jump MovieMomLeftDay04

label MovieMomLeftDay04:
stop music
scene eveningtvkiss with dissolve
$ renpy.pause(2.0, hard=True)
m "Goodnight sweetie, don't stay up too late!"
p "Well crap... Nancy left."
play sound "Sounds/hastalavista.mp3"
$ renpy.pause(2.0, hard=True)
p "Yeah, thanks for reminding me Arnie..."
menu:
    "Continue watching the movie(+1hr)":
        "You finish watching the movie and head to your room."
        $ hour += 1
        jump EveningChoiceDay04
    "Go and meet Laura at the local beach" if (lauraritual == True):
        jump Campfire01Day04
    "Go to Tanya's House" if (discovertanya == True):
        jump TanyaHouse01Day04            
    "Go to your room":
        jump EveningChoiceDay04

label MovieConan02Day04:
scene ryanconanposing01 with dissolve
stop music
play music "Sounds/conan02.wav"
$ renpy.pause(1.0, hard=True)
if (strength >=8):
    m "Oh, sweetie, you're right, you really are BIGGER than this actor! I'm so proud of you!"
    $ lust_points[16] +=1
    $ score += 1
    show lust01:
        xalign 0.9 yalign 0.6
        linear 1.0 yalign 0.4
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    jump MomEvening03Day04
if (strength <=7):
    m "Mmh, you're really big, but not quite as big as what I'm seeing on the screen... But with a bit more training, I'm sure you'll be just as big as your favorite actor honey!"
    p "(Well that's disappointing... I could have sworn I was bigger than him...)"
    m "Anyway, I'm tired, I'll leave you to your silly barbarian..."
    jump MovieMomLeftDay04

label MovieConan03Day04:
scene ryanconanposing01b with dissolve
stop music
play music "Sounds/conan02.wav"
$ renpy.pause(1.0, hard=True)
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(2.0, hard=True)
$ stamina -=1
show staminaminus01:
    xalign 0.3 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
m "Oh, sweetie, you're right, you really are MUCH BIGGER than this actor! I'm so proud of you!"
$ lust_points[16] +=2
$ score += 2
show lust02:
    xalign 0.9 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
jump MomEvening03Day04

label MomEvening03Day04:
stop music
scene eveningmomconan with dissolve
$ renpy.pause(1.0, hard=True)
m "And it's not just your muscles that are bigger than this actor... Your bulge puts his to shame, and I thought his was really huge!"
if (lust_points[16] == 9):
    $ lust_points[16] +=1
    $ score += 1
    show lust01:
        xalign 0.3 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
if (lust_points[16] <= 8):
    $ lust_points[16] +=2
    $ score += 2
    show lust02:
        xalign 0.3 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust02
if (lust_points[16] == 10):
    show epiclust:
        xalign 0.3 yalign 0.2
        zoom 0.5
        linear 2.0 zoom 1.0
    play sound "Sounds/epiclust.mp3"
    $ renpy.pause(4.0, hard=True)
    hide epiclust
    jump MomFuck01Day04
if (lust_points[16] == 9) or (lust_points[16] == 8):
    menu:
        "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
            jump MomPendulumDay04            
        "Spray yourself with pheromones" if (pheromone == True):
            jump MomPheromoneDay04
        "Hold your cock through your jockstrap to show how big it is":
            jump MomStrapDay04
if (lust_points[16] <= 7):
    jump MomStrapDay04

label MomFuck01Day04:
stop music
scene ryanconanposing02 with dissolve
$ renpy.pause(1.0, hard=True)
p "That's right Nancy, you're the one who allowed that thing into your home!"
m "It looks so big.... and not even hard. I know it's wrong but I NEED to feel up that monster!"
scene eveningmomstrap with dissolve
$ renpy.pause(1.0, hard=True)
m "Mmmh, honey, this is the biggest thing I've ever felt in my life... My tiny hands can't even wrap around your giant boycock. Let me see it please, I beg you!"
p "I'm getting really hard Nancy watching you worshipping my bulge like that... FUCK!"
scene eveningmomrip with dissolve
play sound "Sounds/rip.mp3"
$ renpy.pause(1.0, hard=True)
m "Oh my God! Your massive rock-hard cock just ripped right through your jockstrap!"
p "That's cos you're making me so horny Nancy... Please take off your blouse... I'll turn the lights on..."
m "I don't know... It's just so wrong... Just a peek for my horse-hung muscle tenant then!"
scene eveningmomfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
m "You like what you see [name]? What would you like me to do next my studly tenant?"
menu:
    "I need to stick my cock between those big jugs...":
        jump MomTitfuckDay04
    "I don't know but I'm about to explode!":
        jump MomBlowjobDay04
        
label MomStrapDay04:
scene ryanconanposing02 with dissolve
$ renpy.pause(1.0, hard=True)
p "That's right Nancy, you're the one who allowed that thing into your home!"
m "It looks so big.... and not even hard. But this is wrong [name], what am I doing? I should leave, I don't want to be a bad landlady who corrupts her sweet tenant's innocent mind!"
p "Noooo... I'm not a sweet tenant! I'm a bad, BAD TENANT! Come back Nancy! AAARGH!"
jump EveningChoiceDay04

label MomPendulumDay04:
scene eveningmompendulum with dissolve
show pendulum03
$ renpy.pause(1.0, hard=True)
p "Just watch this pendulum as I wiggle it in front of your eyes Nancy..."
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
if (lust_points[16] ==8):
    window hide
    $ lust_points[16] += 2
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
    jump MomFuck01Day04
if (lust_points[16] ==9):
    window hide
    $ lust_points[16] += 1
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
    jump MomFuck01Day04   
    
label MomPheromoneDay04:
scene eveningmompendulum with dissolve
play sound "Sounds/sniffing.mp3"
$ renpy.pause(1.0, hard=True)
m "Oh, it smells funny... And it's making me so horny at the same time..."
p "My spray is now empty... I guess I won't be able to use it again."
show pheromone
show square
play sound "Sounds/lost.mp3"
"You lost a pheromone spray."
hide square
hide pheromone
$ pheromone = False
if (lust_points[16] ==8):
    window hide
    $ lust_points[16] += 2
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
    jump MomFuck01Day04
if (lust_points[16] ==9):
    window hide
    $ lust_points[16] += 1
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
    jump MomFuck01Day04

label MomTitfuckDay04:
$ momtitfuck = True
scene momtitfuck01 with dissolve
m "Of course [name]. I will take care of that monster with my huge jugs, you just relax and let me do all the work."
label MomTitfuckDay04b:
play sound "Sounds/momtitfuck.mp3"            
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
        jump MomTitfuckDay04b
    "Move on":
        pass
if (stamina >=2):
    menu: 
        "Cum, you've got another load for later":
            jump MomTitfuckCumDay04            
        "Don't cum yet and tell her you're about to explode":
            m "Oh sweetie, your huge cock looks like it's ready to explode!"
            if (momblowjob == False):
               m "Bring that massive fuckstick to my mouth!"
               jump MomBlowjobDay04
            else: 
                m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
                jump MomPussyLickDay04
if (stamina <=1):
    m "Oh sweetie, your huge cock looks like it's ready to explode!"
    if (momblowjob == False):
        m "Bring that massive fuckstick to my mouth [name]!"
        jump MomBlowjobDay04
    else: 
        m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
        jump MomPussyLickDay04            

label MomTitfuckCumDay04:
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
if (momblowjob == False):
    m "Bring that massive fuckstick to my mouth [name]!"
    jump MomBlowjobDay04
else: 
    m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
    jump MomPussyLickDay04

label MomBlowjobDay04:
$ momblowjob = True
scene momblowjob01 with dissolve
#play sound "Sounds/momlick01.mp3"  
$ renpy.pause(.0, hard=True)
m "My God , your cock... It's just GIGANTIC! I can't even wrap my fingers around its incredible girth..."
scene momblowjob01b with dissolve
#play sound "Sounds/momlick02.mp3"  
$ renpy.pause(1.0, hard=True)         
m "Mmmh... And those balls... So HEAVY, I just have to taste them..."         
label MomBlowjobDay04b:
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
        jump MomBlowjobDay04b
    "Move on":
        pass

m "Oh sweetie, your huge cock looks like it's ready to explode!"
if (momtitfuck == False):
    m "Why don't you stick your pud between my big tits?"
    jump MomTitfuckDay04
if (momtitfuck == True):
    m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
    jump MomPussyLickDay04            
 
label MomPussyLickDay04:
scene eveningmomclit with dissolve
#play sound "Sounds/momclit.mp3"
$ renpy.pause(1.0, hard=True)
m "Mmmh, you do that so well sweetie! You really know what you're doing! AAAH!"
m "Now it's time for me to reward you... With my pussy!"
jump MomFullFuckDay04

label MomFullFuckDay04:
scene eveningmomready with dissolve
#play sound "Sounds/momready.mp3"
$ renpy.pause(1.0, hard=True)
m "See my tender pink pussy? It's wet and ready for you my studly tenant! Come and pound it!"
#play music "Sounds/momslowfuck.mp3"
show momfuckslow
show faster
call screen momfuckslowday04
screen momfuckslowday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MomFuckFastDay04")
label MomFuckFastDay04:
hide faster
stop music
#play music "Sounds/momfastfuck.mp3"
show momfuckfast
show cum
call screen momfuckfastday04
screen momfuckfastday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MomFuckCumDay04")

label MomFuckCumDay04:
hide momfuckfast
hide momfuckslow
stop music
scene momfuckcum01
play sound "Sounds/cumming.mp3"            
$ renpy.pause(4.0, hard=True)
scene momfuckcum02 with dissolve
play sound "Sounds/momcum01.mp3"            
$ renpy.pause(14.0, hard=True)
scene momfuckcum03 with dissolve
play sound "Sounds/momcum02.mp3"            
$ renpy.pause(15.0, hard=True)
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
jump EveningChoiceDay04

label EveningChoiceDay04:
stop music
scene ryanbedroomnight with dissolve
$ locroom = True
$ renpy.pause(1.0, hard=True)

if (hour >= 24):
    if (challengercalls <= 10):
        $ lustaddedB = 2
        call Challenger from _call_Challenger_60
        $ lustaddedB = 1
        call Challenger from _call_Challenger_61
        $ challengercalls += 2        
    p "I should really go to sleep now, tomorrow is a school day..."
    jump SleepDay04
p "mmmh, what should I do?"
menu:
    "Do some heavy bodybuilding (+2hrs)" if (hour <= 22):    
        if (workout == True):
            "You already trained today."
            jump EveningChoiceDay04
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
            jump EveningChoiceDay04
    "Check the computer":
        jump ComputerEveningDay04
    "Admire my body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump EveningChoiceDay04
    "Read the book Laura gave you (+1hr)" if (book == True) and (bookread == False):
        jump RyanReadingEveningDay04
    "Go to Nikki's room" if (nikkifucked == False) and (nightsisroomseen04 == False):
        jump SisRoomEveningDay04
    "Go to Tanya's House" if (discovertanya == True) and (seentanyaday04 == False)  and (hour<=23):
        if (ryangrounded == True):
            m "You are GROUNDED for tonight mister!"
            jump EveningChoiceDay04
        jump TanyaHouseDay04
    "Go and join Laura at the campsite on the beach" if (lauraritual04 == True) and (seencampfireday04 == False) and (hour<=22):
        if (ryangrounded == True):
            m "You are GROUNDED for tonight mister!"
            jump EveningChoiceDay04
        jump Campfire01Day04
    "Go to the living room to watch a movie with mom" if (nancyfucked == False):
        jump EveningMovieDay04    
    "Go to Nancy's room" if (nightmomroomseen02 == False) and (seenmomundressingfullday03  == False) and (nightmomroomseen04 == False) and (hour >=22):
        jump MomUndressingDay04
        
label ComputerEveningDay04:
scene ryancomputer with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label ComputerEveningDay04b:
scene ryancomputer
$ renpy.pause(1.0, hard=True)
menu:
    "Check the map":
        jump MapEveningDay04
    "Check the stats":
        jump StatsEveningDay04
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump ComputerEveningDay04b
    "Learn how to use the pendulum" if (pendulum == True) and (pendulumactive ==False):
        jump CompPendulumEveningDay04
    "Play a smutty game (+1hr)":
        jump CompGameEveningDay04
    "Turn the computer off":
        jump EveningChoiceDay04
    
label RyanReadingEveningDay04:
scene ryanreading with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump EveningChoiceDay04

label CompPendulumEveningDay04:
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump ComputerEveningDay04b

label MapEveningDay04:
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
p "This shows all the places I know so far on Veri-Bosti Island..."
show screen statsbackground
show screen inventorybutton
show screen calendar
jump ComputerEveningDay04b

label StatsEveningDay04:
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
jump ComputerEveningDay04b       

label CompGameEveningDay04:
scene ryancomputergame with dissolve
$ renpy.pause(1.0, hard=True)
p "This game is tough. My fingers hurt like hell from so much clicking..."
$ hour +=1
jump ComputerEveningDay04b 
        
label MomUndressingDay04:
stop music
$ nightmomroomseen04 = True
$ locroom = False
scene nancybedroomclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "The door is locked but I can see some light poking through the keyhole."
menu:
    "Look through the keyhole":
        jump MomUndressingDay04b
    "Leave and go back to my room":
        jump EveningChoiceDay04
        
label MomUndressingDay04b:
scene nancyundressing01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Nancy is sitting on her bed. She looks like she's thinking about doing something..."
p "More landlady blueballing on the way for you guys it seems... What should I do?"
menu:
    "Why do you even ask? Look on of course!":
        jump MomUndressing02Day04
    "I feel dirty watching Nancy like that. Go back to my room and cry into my pillow":
        jump EveningChoiceDay04

label MomUndressing02Day04:
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
    jump EveningChoiceDay04

scene nancyundressing07 with dissolve
$ seenmomundressingfullday04 = True
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
jump EveningChoiceDay04    

label TanyaHouseDay04:
if (seentanyaday03 == False):
    jump TanyaHouse01Day04

if (seentanyaday03 == True):
    jump TanyaBed01Day04
    
label TanyaHouse01Day04:
$ seentanyaday04 = True
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
                jump TanyaHouse02Day04
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay04
    "I'm out of here, you guys are crazy!":
        ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
        jump EveningChoiceDay04
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
                jump TanyaHouse02Day04
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay04
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
        jump EveningChoiceDay04
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
                jump TanyaHouse02Day04
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay04

label TanyaHouse02Day04:
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
call screen tanyawankslowday04
screen tanyawankslowday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("TanyaWankFastday04")
label TanyaWankFastday04:
hide faster
show tanyawankfast
show cum
call screen tanyawankfastday04
screen tanyawankfastday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TanyaWankCumday04")

label TanyaWankCumday04:
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
        jump EveningChoiceDay04

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
                jump EveningChoiceDay04
            "Meet Laura on the beach" if (lauraritual04 == True) and (seencampfireday04 == False)  and (hour<=22):
                jump Campfire01Day04
                
label TanyaBed01Day04:
$ seentanyaday04 = True
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
                jump TanyaHouse02Day04
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
                jump EveningChoiceDay04            
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
        jump EveningChoiceDay04
    menu:
        "Ok, I'll do it! I'm da man, I'm DA MAN!":
            jump TanyaHouse02Day04
        "I'm out of here, you guys are crazy!":
            ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
            jump EveningChoiceDay04

if (tanyawebcamday03 == True):
    jump TanyaBed02Day04
    
label TanyaBed02Day04:
$ tanyawebcamday04 = True
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
            jump TanyaCondomsDay04
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
            jump EveningChoiceDay04            
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
    jump EveningChoiceDay04
p "Alright! Let's do it then, I'm getting a massive boner just thinking about it!"
label TanyaCondomsDay04:
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
    jump TanyaBed03Day04
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
    jump EveningChoiceDay04
        
label TanyaBed03Day04:   
scene tanyabed01 with dissolve
play music "Sounds/tanyamusic.mp3"
$ renpy.pause(1.0, hard=True)
ta "Oh, look at poor little Darryl... All tied up and with his cock constrained in his tight briefs..."
dl "Untie me for fuck's sake Tanya! Wh... Why is this boy here again? I told you I never wanted to see him again in MY house!"
ta "He's here to get us lots of money... I'm sorry honeypot, but I read our viewers' requests last night on twatter and they all wanted to see me handle his young monster cock!"
dl "No please, don't do this to me, I'm all tied up, this is so humiliating!"
ta "Well that's the idea darling... Now hush, showtime is in a few seconds, [name], can you go and turn the webcam on please?"
p "Sure Tanya!"
$ tanyabedday04 = True
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
    jump TanyaBed04Day04
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

label TanyaBed04Day04:
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
label TanyaBed04Day04b:
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
        jump TanyaBed04Day04b
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
        jump TanyaBlowjobDay04
    "Fuck her above Darryl" if (tanyaride == False):
        jump TanyaRideDay04
    
label TanyaBlowjobDay04:
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
label TanyaBlowjobDay04b:
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
        jump TanyaBlowjobDay04b
    "Get her to take MORE of your cock!":
        p "I think you can take more Tanya, come on, do it! AAAH!"
        scene tanyabed11c with dissolve    
        play sound "Sounds/hallesuck02.mp3"
        $ renpy.pause(3.0, hard=True)
        dl "I can't watch this! This is too humiliating!"
        jump TanyaBlowjobDay04b
    "Fuck her above Darryl" if (tanyaride == False):
        jump TanyaAboveDay04
    "Let her ride you like a wild bronco" if (tanyaride == True) and (tanyablow == True):
        jump TanyaRideDay04
        
label TanyaAboveDay04:
$ tanyaride = True
scene tanyabed12 with dissolve
play sound "Sounds/tanya04.mp3"
$ renpy.pause(3.0, hard=True)
ta "Come and stick that big fucking cock in me!"
scene tanyabed13 with dissolve
$ renpy.pause(3.0, hard=True)
p "Ready to have your pussy ruined for your hubby by a way bigger cock than his?"
ta "Ooh, fuck yeah!"
label TanyaAboveDay04b:
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
        jump TanyaAboveDay04b
    "Get a blowjob" if (tanyablow == False):
        ta "Good idea, and let's do it right in front of Darryl's face, you don't mind do you hubby?"
        dl "Of course I fucking mind! Don't do this to me!"
        ta "Sorry, but that's what our viewers want and that's what we'll give them..."
        jump TanyaBlowjobDay04
    "Let her ride you like a wild bronco" if (tanyaride == True) and (tanyablow == True):
        jump TanyaRideDay04
    

label TanyaRideDay04:
scene tanyabed15 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Let me ride that donkey-dick stud! I can't wait to feel that monstrous rock-hard member deep inside of me while my helpless hubby watches on!"
dl "No, don't fuck him please Tanya!"
ta "Stop pretending you don't like it honey, I can see your erection distending your tight briefs... Just watch and enjoy the ride, I sure will!"
play music "Sounds/tanyafuckslow.mp3"
show tanyafuckslow
show faster
call screen tanyafuckslow
screen tanyafuckslow:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("TanyaFuckFast")
label TanyaFuckFast:
hide faster
play music "Sounds/tanyafuckfast.mp3"
show tanyafuckfast
show cum
call screen tanyafuckfast
screen tanyafuckfast:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TanyaFuckCum")

label TanyaFuckCum:
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
$ hour += 1
$ tanyafucked = True
if (tanyajosewin == False):
    p "(She didn't notice I took a picture of us... Now I'll send it to José)."
    $ tanyawin = True

menu:
    "Go back home":
        jump EveningChoiceDay04
    "Meet Laura on the beach" if (lauraritual04 == True) and (seencampfireday04 == False) and (hour <= 22):
        jump Campfire01Day04

label Campfire01Day04:
$ seencampfireday04 = True
scene campfire01 with dissolve
play music "Sounds/campfire.mp3"
$ renpy.pause(1.0, hard=True)
if (seencampfireday03 == False):
    jump Campfire01Day04First
if (seencampfireday03 == True) and (ritualwords == True):
    jump Campfire01Day04Second
if (seencampfireday03 == True) and (ritualwords == False):
    jump Campfire01Day04First

label Campfire01Day04First:
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
        jump CampfireLeftDay04
    "Whisper the words":
        p "Evil, live, live, evil... Evil, live, live, evil..."
        $ ritualwords = True
        jump Campfire02Day04
    "Just continue watching":
        $ ritualwords = False
        jump Campfire02Day04

label Campfire02Day04:
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
            jump DamianCurseDay04
        "Curse José":
            jump JoseCurseDay04
        "Don't curse anyone, this is too satanic":
            jump NoCurseDay04

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
            jump EveningChoiceDay04
        "Go to Tanya's House" if (discovertanya == True) and (seentanyaday04 == False) and (hour <= 23):
            jump TanyaHouseDay04
    
label DamianCurseDay04:
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
jump CampfireLaura01Day04

label JoseCurseDay04:
p "I curse thee, José!"
"Choose a girl to go with José's curse (-3 challenger lust points for her):"
label ChooseGirlCurseDay04:
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
        jump ChooseGirlCurseDay04
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
        jump CampFireEndDay04
    "Maddy":
        show maddysprite at CampfirePosition
        $ lust_pointsB[14] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay04        
    "Nikki":
        show nikkisprite at CampfirePosition
        $ lust_pointsB[17] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay04
    "Frieda":
        show friedasprite at CampfirePosition
        $ lust_pointsB[8] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay04
    "Kate":
        show katesprite at CampfirePosition
        $ lust_pointsB[11] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay04
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
        jump CampFireEndDay04


label NoCurseDay04:
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
jump EveningChoiceDay04

label CampFireEndDay04:
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
        jump EveningChoiceDay04        
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
        jump CampfireLaura01Day04
                
label CampfireLaura01Day04:
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
    jump LauraFuck01Day04

label LauraCampFireChoiceDay04:
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
                jump EveningChoiceDay04
            "Go to Tanya's House" if (discovertanya == True) and (seentanyaday04 == False) and (hour <= 23):
                jump TanyaHouseDay04
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
                jump EveningChoiceDay04
            "Go to Tanya's House" if (discovertanya == True) and (seentanyaday04 == False)  and (hour <= 23):
                jump TanyaHouse01Day04
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
        jump LauraPendulumDay04
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
        jump LauraCampFireChoiceDay04

label LauraPendulumDay04:
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
    jump LauraFuck01Day04
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
    jump LauraFuck01Day04  

label LauraFuck01Day04:
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
            jump EveningChoiceDay04
        "Go to Tanya's House" if (discovertanya == True) and (seentanyaday04 == False)  and (hour <= 23):
            jump TanyaHouseDay04
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
label LauraFuck01Day04b:
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
        jump LauraFuck01Day04b
    "Move on":
        pass

scene campfire15 with dissolve
play sound "Sounds/laura01.mp3"    
$ renpy.pause(8.0, hard=True)
la "You seem to have liked that... Your cock has turned into a steel-hard pole!"
menu:
    "Make it spew its evil load with your hands!" if (stamina >=2):
        jump LauraFuck03Day04
    "I need to put it into something soft and warm!":
        jump LauraFuck02Day04
    "Tease it with your fingernails!" if (stamina ==1):
        jump LauraFuck03Day04

label LauraFuck03Day04:
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
label LauraFuck03Day04b:
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
        jump LauraFuck03Day04b
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
    jump LauraFuck02Day04b
if (stamina == 1):
    p "Enough, I can't take much more of that teasing, I need to put my cock into something soft and warm! And very deep preferably..."    
    la "Such eagerness... Alright, I will ride that horsecock cowboy!"
    jump LauraFuck02Day04b
label LauraFuck02Day04:
if (lauratease == False):
    la "I think I should first tease that throbbing cock with my fingernails..."
    p "Ah, err. Ok."
    jump LauraFuck03Day04
    
label LauraFuck02Day04b:
stop music
play sound "Sounds/campfire.mp3"
play music "Sounds/laurafuckslow.mp3"
show laurafuckslow
show faster
call screen laurafuckslowday04
screen laurafuckslowday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("LauraFuckFastDay04")

label LauraFuckFastDay04:
stop movie
hide faster
play music "Sounds/laurafuckfast.mp3"
show laurafuckfast
show cum
call screen laurafuckfastday04
screen laurafuckfastday04:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("LauraFuckCumDay04")
    
label LauraFuckCumDay04:
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
$ fuckedschoolgirlday04 = True
$ hour += 1
la "I should go back home now, after an evening dip in the sea to clean myself of your MASSIVE load (giggles). See you tomorrow [name]!"
p "Good night Laura, see you tomorrow!"
menu:
    "Go back home":
        jump EveningChoiceDay04
    "Go to Tanya's House" if (discovertanya == True) and (seentanyaday04 == False)  and (hour <= 23):
        jump TanyaHouseDay04
        
label Campfire01Day04Second:
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
        jump EveningChoiceDay04
    "Go to Tanya's House" if (discovertanya == True) and (seentanyaday04 == False) and (hour <=23):
        jump TanyaHouseDay04
    
label SleepDay04:
scene ryansleeping with dissolve
play music "Sounds/ryansnoring.mp3"
$ renpy.pause(1.0, hard=True)
"You fall asleep and dream of your adventures to come..."
$ renpy.pause(2.0, hard=True)

"Your current score (not that it matters) is: {b}[score]{/b}"
if (score <=90):
    "Your ranking: {b}Douchebag{/b}"
elif (score <=110):
    "Your ranking: {b}Noob{/b}"
elif (score <=130):
    "Your ranking: {b}Average Joe{/b}"
elif (score <=150):
    "Your ranking: {b}Hunk{/b}"
else:
    "Your ranking: {b}Babe Magnet{/b}"
stop music
window hide

jump Day05












        
        

        
        


        


            
