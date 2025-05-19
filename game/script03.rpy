label Day03:
# reboot variables
$ day = 3
$ hour = 7
$ stamina = 5
$ blacktop = False
$ wentforjog = False
$ longjog = False
$ shortjog = False
$ walkbeachseen = False
$ detention = False
$ auntdebbyseen = False
$ evictedfromstore = False
$ quentinnotfriends = False
$ locswimmingpool = False
$ audacioustried = False
$ evictedfromshop = False
$ shoppingseen = False

$ downtowntipgiven = False
$ beachtipgiven = 0
$ schooltipgiven = False
$ workout = False
$ pretendshop = False
$ challengercalls = 0
$ busbeach = False
$ bustown = False
$ bushome = False
$ fuckedschoolgirl = False

$ spokenlunchquentin = False
$ spokenlunchlaura = False
$ spokenlunchmaddy = False
$ spokenlunchfrieda = False
$ spokenlunchkate = False

if (nikkifucked == True):
    $ fuckedschoolgirl = True

stop music
play sound "Sounds/yawning.mp3"
scene ryanyawning with dissolve
$ renpy.pause(1.0, hard=True)
p "Yet another beautiful day... Filled with hot steamy sex hopefully!"
scene ryanbedroomday with dissolve
$ lustaddedB = 2
call Challenger from _call_Challenger_45
$ lustaddedB = 1
call Challenger from _call_Challenger_46
$ challengercalls += 2

label MorningDay03b:
stop music
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "What should I do?"
menu:
    "Put on a black tank top" if (tanktop == True) and (blacktop == False):
        p "Yeah, I'm ready to be a goth. Or a rebel. Or just someone with terrible tastes."
        $ blacktop = True
        jump MorningDay03b
    "Take a shower":
        jump ShowerMorningDay03
    "Go for breakfast":
        jump MomYogaMorningDay03
    "Check the computer":
        jump ComputerMorningDay03
    "Go for a jog":
        $ wentforjog = True
        jump MomYogaMorningDay03
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump MorningDay03b


label ComputerMorningDay03:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label ComputerMorningDay03b:
scene ryancomputerday
menu:
    "Check the map":
        jump MapMorningDay03
    "Check the stats":
        jump StatsMorningDay03
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump ComputerMorningDay03b
    "Turn the computer off":
        jump MorningDay03b


label MapMorningDay03:
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
p "This shows all the places I know so far on Veri-Bosti Island..."
show screen statsbackground
show screen inventorybutton
show screen calendar
jump ComputerMorningDay03b

label StatsMorningDay03:
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
jump ComputerMorningDay03b

label ShowerMorningDay03:
play music "Sounds/shower.mp3"
scene bathroomdoorclosed with dissolve
$ renpy.pause(1.0, hard=True)
$ locroom = False
p "Someone's taking a shower..."
label ShowerMorningDay03b:
menu:
    "Use lubricant on the door hinges" if (wd69 == True) and (squeakfixed == False):
        "The door should not squeak anymore."
        $ squeakfixed = True
        jump ShowerMorningDay03b
    "Have a peek":
        jump PeekBathroomMorningDay03
    "Leave":
        jump MorningDay03b

label PeekBathroomMorningDay03:
if (squeakfixed == False):
    play sound "Sounds/doorsqueak.mp3"
    scene bathroomdooropen with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Shit, the door is squeaking..."
    s "Hey, I'm in the shower, don't get in!"
    p "Ah, sorry Nikki...I'm leaving..."
    p "Damn, I should try and find a way of stopping that door from squeaking if I want to spy on Nancy or Niiki in the shower like every other MC..."
    jump MorningDay03b
if (squeakfixed == True):
    scene nikkishower01 with dissolve
    $ renpy.pause(1.0, hard=True)
    if (sisshowerpeep == False):
        $ peeping += 1
    $ sisshowerpeep = True
    p "Cool, she didn't hear me come in, I can see her naked in the shower now..."
    menu:
        "Get closer, it's dangerous but I'm crazy with lust for her!":
            jump SisShowerMorningDay03
        "Admire the view a little longer then leave":
            jump MorningDay03b
    
label SisShowerMorningDay03:
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
    jump MorningDay03b
if (nikkiwin == True): 
    s "[name]! It's not because we... dit it, that you have the right to barge in on me taking a shower like that!"
    p "Oh, come on, how about we do it in the shower stall... Mmmh? wanna another taste of my massive cock?"
    s "Get the hell out of here! You're just a pervert, I knew it, I should never have allowed this to happen!"
    p "Pff, women! One moment they're bouncing up and down your hard shaft, the next minute they're all prude and shit... It's not fair."
    jump MorningDay03b
    
label MomYogaMorningDay03:
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
        m "Oh, good morning sweetie, how are you today?"
        p "Yeah, I'm all set and ready for a new day!"
        if (wentforjog == True):
            jump WentForJogDay03
        elif (wentforjog == False):
            jump MomYogaBreakfastDay03
    "Call her so she knows you're here":
        p "Hey Nancy, good morning!"
        scene nancyyoga04 with dissolve
        $ renpy.pause(1.0, hard=True)       
        m "Oh,good morning sweetie, how are you today?"
        p "Yeah, I'm all set and ready for a new day!"
        if (wentforjog == True):
            jump WentForJogDay03
        elif (wentforjog == False):
            jump MomYogaBreakfastDay03

label WentForJogDay03:
m "Were you going out for a jog? If you do, you might miss breakfast."
p "Yeah, but it's just that I'm so eager to see everything on this island Nancy!..."
m "Fine, your choice [name]."
menu:
    "Go for a jog on the local beach":
        jump JogBeachDay03
    "Go for a jog around the neighborhood":
        jump JogBurbsDay03       


label MomYogaBreakfastDay03:
p "Are we having breakfast soon?"
m "Give me a few minutes to finish my exercises and for Nikki to take her shower."
m "Why don't you sit and watch a bit of TV while you're waiting?"
p "Sure Nancy!"
scene ryantv with dissolve
play music "Sounds/laughter.mp3"
$ renpy.pause(1.0, hard=True)
p "God these morning sitcoms are so boring, nothing ever happens... No wonder this show was cancelled."
m "Breakfast is ready!"
$ hour += 1
stop music
jump Breakfast01Day03

label JogBeachDay03:
$ shortjog = True
scene ryanjog01 with dissolve
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
"You enjoy the fresh sea breeze as you jog along the beach..."
$ d2rolljogday03 = renpy.random.randint(0, 1)

if (d2rolljogday03==0):
        "After running a couple of miles, you head back home for breakfast."
        jump Breakfast02jDay03        
if (d2rolljogday03 ==1):
    if (discovertanya == False):
        jump JogBeach03Day03
    else:
        "After running several miles, you head back home for breakfast full of renewed energy."
        $ stamina += 1
        show stamina01:
            xalign 0.5 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide stamina01        
        jump Breakfast02jDay03


label JogBeach03Day03:
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
jump Breakfast02jDay03

label Breakfast02jDay03:
stop music
$ hour += 1
scene morninglateday03 with dissolve
$ renpy.pause(1.0, hard=True)
if (shortjog == True):
    m "Get a quick shower, we're about to start breakfast!"
    p "Oh, sure Nancy, sorry..."
    "You take a quick shower and head downstairs for breakfast."
    jump Breakfast01Day03
elif (longjog == True): 
    m "You took too long, so we had breakfast without you. Get a quick shower and get dressed, I'll make a jam sandwich for you to eat on the way to school!"
    p "Oh, sure Nancy, sorry I took so long..."
    "You take a quick shower and hurriedly get dressed to join Nikki on the way to school."
    jump SchoolDay03

label JogBurbsDay03:
scene burbsmorning with dissolve
play music "Sounds/morning.mp3"
$ renpy.pause(1.0, hard=True)
p "The burbs are so quiet in the morning."
scene burbsmorningstore with dissolve
$ renpy.pause(1.0, hard=True)
if (discoverstore == False):
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
            jump StoreDay03
        "Go back home in time for breakfast":
            $ shortjog = True
            jump Breakfast02jDay03
if (discoverstore == True):
    "The local convenience store... Might as well enter and see what they have on offer today."
    $ shortjog = True 
    jump StoreDay03

label Breakfast01Day03:
scene breakfastday03a
if (blacktop == True):
    show breakfastday03ablack
$ renpy.pause(1.0, hard=True)
if (nikkiwin == True):
    show breakfastday03f with dissolve
    m "I heard some weird noises coming from your room last night Nikki, was everything okay?"
    show breakfastday03e with dissolve
    s "Oh.... Hum... Yes, mom, it was just [name] helping me find my earrings, we had to move a lot of furniture around..."
    m "I see, and did you manage to find them eventually?"
    s "Yes, I have them now, thanks to [name]!"
    m "Well that's great that you two are helping each other out."
    hide breakfastday03f
    hide breakfastday03e

if (blacktop == True): 
    show breakfastday03d
    s "I've never seen you in a black top before [name]... What is going on?"
    p "It's my new style. I'm a rebel now."
    s "Hee hee, it takes more than a black top to be a rebel [name]!"
    m "And I can't say that I approve of this new \"rebel\" style..."
    $ lust_points[16] -=1
    $ score -= 1
    show lustminus01:
        xalign 0.6 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    p "Well I wear what I want! I bought it with my own money, so there!"
    hide breakfastday03d

label Breakfast02Day03:
if (pocketmoney == True):
    m "Here's some pocket money for the day Nikki, 5 dollars. For you [name], nothing, since you are still punished for what you did yesterday!"
    m "Now eat up so you two can get to school on time."
if (pocketmoney == False):
    m "Here's some pocket money for the day, five dollars each."
    $ money += 5
    show breakfastday03c
    s "Yeah, thanks mom!"
    p "Thanks Nancy!"
    m "Don't spend it on anything silly! Now eat up so you two can get to school on time."
    hide breakfastday03c

label SchoolDay03:
scene schoolentrance with dissolve
$ renpy.pause(1.0, hard=True)
$ hour += 1
s "Have a nice day [name], maybe we'll see each other at lunch."
p "Sure Nikki, have a nice day too!"


label ClassRoomDay03:
play music "Sounds/classambience.mp3"
scene class01day03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah, everyone here and chatting before Ms Cocque arrives... Maybe I have time to chat some girls up..."
menu:
    "Chat with Kate":
        scene classkate01day03 with dissolve
        $ renpy.pause(1.0, hard=True)
        k "Oooh, hi [name]. Hee hee."
        play sound "Sounds/katehihi.mp3"
        menu:
            "Hey Kate, you know what I found out? That scumbag José is totally backing Brittany for prom queen!" if ((seenlockerbrit == True) or (lust_pointsB[1] >= 8)) and (toldkatejose == False):
                scene classkate02day03 with dissolve
                $ renpy.pause(1.0, hard=True)
                $ toldkatejose = True
                k "What? Oooh, no... I need his vote to win... What a loser, what does he find in her?"
                if (lust_pointsB[11] == 1):
                    $ lust_pointsB[11] -=1
                    show challengerlustminus01:
                        xalign 0.3 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide challengerlustminus01
                if (lust_pointsB[11] >= 2):
                    $ lust_pointsB[11] -=2
                    show challengerlustminus02:
                        xalign 0.3 yalign 0.2
                        linear 1.0 yalign 0.4
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide challengerlustminus02                    
                p "Who knows, that guy has shit for brains."
                k "Oooh, the teacher is arriving, stop talking to me or she'll give me detention again!"
                p "Okay Kate, talk to you later then..."
                jump LessonDay03
            "Since you will compete in the bikini pageant, I could maybe take pictures of you so you can better decide which bikini to choose?" if (katephotoasked == False):
                scene classkate03day03 with dissolve
                $ renpy.pause(1.0, hard=True)
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
                k "Oooh, the teacher is arriving, stop talking to me or she'll give me detention again!"
                p "OKay Kate, talk to you later then..."                
                $ katephotoasked = True
                jump LessonDay03
            "Hey Kate, are you ready for a photoshoot today?" if (katephotoasked == True):
                $ katephotoplanned = True
                scene classkate03day03 with dissolve
                $ renpy.pause(1.0, hard=True)
                k "Oooh, yes! I have a couple of bikinis I would like to try on!"
                p "Come to my place at 5 or 6pm then, I'll have everything set up!"
                k "Oh, really? That's so great, I'll be there!"
                if (camera == False):
                    p "(I'd better find a camera TODAY or she'll be mighty disappointed...)"
                    jump LessonDay03
                if (camera == True):
                    p "(I'd better make sure I'm back home by 5 or 6pm...)"
                    k "Oooh, the teacher is arriving, stop talking to me or she'll give me detention again!"
                    p "Okay Kate, talk to you later then..."
                    jump LessonDay03
            "Why don't you tell Quentin you're not interested in him?":
                scene classkate02day03 with dissolve
                $ renpy.pause(1.0, hard=True)
                k "I keep telling him but he doesn't understand..."
                p "I guess that's because he's in love with you."
                k "Eeww. I don't want anything to do with him. He's such a nerd."
                k "Oooh, the teacher is arriving, stop talking to me or she'll give me detention again!"
                p "OKay Kate, talk to you later then..."                
                jump LessonDay03
                
    "Chat with Laura":
        scene classmeet05 with dissolve
        $ renpy.pause(1.0, hard=True)
        la "What do you want [name]? I hope it's not boring..."
        menu:
            "I read that book you gave me." if (bookread == True):
                $ toldlaurabook = True
                la "Oh really? And what did you think about then?"
                p "Fascinating. I didn't realize so many celebrities were goths."
                p "Ozzy Osbourne, Marilyn Manson, the Addams Family, Mike Pence... It opened my eyes." 
                show laurasmile with dissolve
                la "Well, that's great! You're half-way to becoming a true goth then."
                $ lust_points[13] +=1
                $ score += 1
                show lust01:
                    xalign 0.1 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust01 
                show laurasmile with dissolve
                jump LessonDay03
            "See, I'm wearing a black tank top today!" if (blacktop == True)  and (lauratop == False):
                "Wicked, it suits you too [name]!"
                $ lust_points[13] +=2
                $ score += 2
                show lust02:
                    xalign 0.1 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust02 
                $ lauratop = True
                jump LessonDay03
            "Will you be hanging out with Damian and that French chick today?":
                if (blacktop == False):
                    "Yeah, and you're not invited, you're nowhere near to becoming a goth!"
                    $ lust_points[13] -=1
                    $ score -= 1
                    show lustminus01:
                        xalign 0.1 yalign 0.4
                        linear 1.0 yalign 0.2
                    play sound "Sounds/less.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lustminus01 
                if (blacktop == True):
                    "Sure, as usual. You could come since you're wearing a wicked black top now... And dare I say it suits you!"
                    $ lust_points[13] +=1
                    $ score += 1
                    show lust01:
                        xalign 0.1 yalign 0.4
                        linear 1.0 yalign 0.2
                    play sound "Sounds/more.mp3"
                    $ renpy.pause(2, hard=True)
                    hide lust01 
                    $ lauratop = True
                jump LessonDay03

    "Chat with Maddy":
        scene classmeetmaddyday03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Good morning Maddy. How are you today?"
        md "Can't you see I'm talking to Frieda? God, boys can be so rude sometimes!"
        p "Err... Sorry... I just wanted to..."
        md "Get out of my face FREAK!"
        p "Well that escalated quickly... Shit, the teacher is arriving..."
        jump LessonDay03

    "Chat with Frieda":
        scene classmeetfriedaday03 with dissolve
        $ renpy.pause(1.0, hard=True)
        if (friedaclothes == True):
            p "Hi Frieda, I see you took my advice and you're wearing more... like, lighter clothes than a school uniform."
            fr "Ja, we vere just talking about it. Maddy also thinks it's a great idea and might do the same thing."
            $ lust_points[8] +=1
            $ score += 1
            show lust01:
                xalign 0.1 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01 
            md "It certainly looks much more comfortable..."
            $ lust_points[14] +=1
            $ score += 1
            show lust01:
                xalign 0.85 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/more.mp3"
            $ renpy.pause(2, hard=True)
            hide lust01 
            p "Oh-Oh, I hear the teacher arriving...."
            fr "Achtung, we should get back to our seats sehr fast..."
            jump LessonDay03
        if (friedaclothes == False):
            p "Hi Frieda, I see you're wearing some lighter clothing today..."
            fr "I'm glad you noticed. Most girls here always wear the same clothes."
            md "Humpf..."
            p "Oh-Oh, I hear the teacher arriving...."
            fr "Achtung, we should get back to our seats sehr fast..."
            jump LessonDay03

label LessonDay03:
stop music
scene classroom01day03 with dissolve
$ renpy.pause(1.0, hard=True)
t "Stop chuckling, this is serious. You are now all at an age where... let's say, you might have sex."
t "Therefore, it is important you understand how to approach your first sex encounter."
t "The first thing you have to think about is PROTECTING yourself."
t "Now you all have a fake plastic prop on your desk, and we will learn how to put a condom on a man's penis."
scene classroom02day03 with dissolve 
$ renpy.pause(1.0, hard=True)
t "First, carefully remove the condom from its case without tearing it."
scene classroom03day03 with dissolve 
$ renpy.pause(1.0, hard=True)
t "And finally, roll it down the shaft of the penis."
md "Ms Cocque, what's the dangly bit at the end?"
t "That's the sperm reservoir to keep the man's filthy juice inside the condom when he comes, probably like two minutes after penetration...(sigh)"
menu:
    "Pffew, condoms suck. Bareback riding is the best.":
        t "The day you catch syphillis you'll sing a different tune! ALWAYS protect yourself, is this clear?"
        k "OOOh, who is this horrible Syphillis woman Ms Cocque? And what does she look like?"
        t "Kate... Just hush."
        jump Lesson02Day03
    "Miss Cocque, I beg to differ. I can last much more than two minutes.":
        t "Yeah, well, I meant... Of course, some men can last longer. They are just very rare."
        $ lust_points[22] +=1
        $ score += 1
        show lust01:
            xalign 0.5 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01 
        jump Lesson02Day03        
    "These condoms are too small. I would rip them apart.":
        t "Enough bragging [name], take this lesson seriously or you'll end up in detention!"
        if (lust_points[22] >=1):
            $ lust_points[22] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.5 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01 

        jump Lesson02Day03

label Lesson02Day03:
t "So, are you all done? Let me check your handiwork..."
scene classroom04day03 with dissolve 
$ renpy.pause(1.0, hard=True)
t "Kate, you put the condom the wrong way on... You clearly weren't listening or watching me. Detention for you again this afternoon!"
k "What? Oooh, I always end up in detention... Why are you doing this to me?"
$ renpy.pause(1.0, hard=True)
t "Frieda, that's good, well done. Quentin, also... Maddy, perfect. Let's see your handiwork [name]."
menu: 
    "Screw up the exercise like Kate.":
        $ condomscrew = True        
    "Don't screw up the exercise.":
        $ condomscrew = False

if (condomscrew == False):
    scene classroom05day03 with dissolve
    t "That's fine, good. Laura, checked, and the two at the back, done. Let's move on."
    k "Ummmpf..."
    $ lust_points[11] -= 1
    $ score -= 1
    show lustminus01:
        xalign 0.05 yalign 0.5
        linear 1.0 yalign 0.7
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    jump DaydreamerDay03

if (condomscrew == True):
    scene classroom05bday03 with dissolve
    t "[name], I expected more from you. You made the same mistake as Kate. You'll get the same punishment... DETENTION!"
    $ detention = True
    hide lustminus01 
    jump DaydreamerDay03

label DaydreamerDay03:
scene classroom01day03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Now she's talking about male and female anatomy. Well, I know all about that stuff already..."
p "Why don't I spend my time more efficiently by daydreaming about hot chicks?"
menu:
    "Daydream about the teacher":
        jump DayDreamTeaganDay03
    "Daydream about Kate":
        jump DayDreamKateDay03
    "Daydream about Laura":
        jump DayDreamLauraDay03
    "Daydream about Frieda and Maddy":
        jump DayDreamFriedaMaddyDay03
        
label DayDreamTeaganDay03:
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
scene classroom01day03 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
p "Ah, fuck, right when she was about to virtually suck me..."
jump LessonEndDay03

label DayDreamLauraDay03:
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
scene classroom01day03 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
p "Phew, saved by the bell! What the fuck was that? Why did I daydream such a thing..."
p "At least, the NTR-loving sissy-boys who have been harassing the dev will now have to SHUT THE FUCK UP."
jump LessonEndDay03

label DayDreamKateDay03:
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
scene classroom01day03 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
p "She didn't answer, that means a yes right?..."
jump LessonEndDay03

label DayDreamFriedaMaddyDay03:
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
p "Alright! I'm da man, I'll do her fr..."
stop music
scene classroom01day03 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
p "Damn bell! I was just about to get me some virtual pussy!..."
jump LessonEndDay03
        
label LessonEndDay03:
$ hour += 1
t "OK, class dismissed. I'll see you tomorrow since you have swimming practice now. Head for the sports hall."
t "May I also remind you all that we are going on a school trip to Bigdong Falls tomorrow morning! Meet at 8am in front of the school!"

if (deliveryboy == True):
    scene teacherenter with dissolve
    $ renpy.pause(1.0, hard=True)
    t "[name], I would need some groceries delivered this evening. Could you pick them up and bring them to my place at 7pm please?"
    menu:
        "Err... no, I have something planned at that time...":
            t "Hu. How disappointing."
            $ lust_points[22] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.5 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
        "Sure Miss Cocque, I'll make sure to bring them over.":
            $ teagangrocery = True
            t "That's a good boy."

stop music
play music "Sounds/lockersound.mp3"
scene locker with dissolve
$ renpy.pause(1.0, hard=True)
p "Quentin is there again, right in front of my locker..."
$ renpy.pause(1.0, hard=True)
p "What's up, Quentin? Any tip for me?"
q "Yes, indeed! Principal Titsworthy is looking for campaign volunteers for her senate bid. That could be a fun and educative way of getting to know her better!"
p "OK. Not much into politics but why not. Did you volunteer?"
q "Of course not. Her political platform is everything I stand against. But for the sake of beating that arsehole José, I gave you the tip anyway."
q "Hurry up [name], we need to get to the sports hall for swimming practice, I'll lead the way!"

label Sport01Day03:
stop music
scene lockerswim01 with dissolve
$ renpy.pause(1.0, hard=True)
q "Are you trying to impress the girls by hiding a salami down there [name]?"
q "You're exagerating a tad I'd say, I only put a pair of socks myself..."
menu:
    "Show him the truth":
        scene lockerswim02 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Yeah, a big fat salami as you can see..."
        q "OMG, that thing's huge... Gee, you're so lucky. I wish I was hung like that. Don't make fun of my bulge in front of the girls okay?"
        jump Sport02Day03
    "Yeah, trying to get lucky...":
        q "Ha ha, I think you'll scare them more than anything, you went a bit overboard. You should stick to just one pair of socks like I do."
        jump Sport02Day03

label Sport02Day03:
scene swim01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Is everyone here? OK, listen up, I want the best out of you lot."
vi "We NEED to beat those lousy bums from the \"Lycée Public de Sainte-Nitouche\", I WANT the cup, is that clear?"
p "What is she on about?"
q "She's pushing us so hard so she can win her stupid cup. Last week, I almost drowned..."
scene swim02 with dissolve
$ renpy.pause(1.0, hard=True)
vi "YOU! You're new right? Are you a good swimmer?"
menu:
    "Err...yeah, sure.":
        vi "Good, you'll be our lead swimmer then. Get in the water and do a 100m crawl."
        jump Sport03Day03
    "No, I totally suck, my huge bulge slows me down.":
        vi "What...? Your bu.... What are you hiding down there, get these socks out, you too Quentin, I know what you stupid horny boys are up to!"
        q "Oh, shoo... Now the girls are gonna make fun of me..."
        p "I have nothing to remove, that's my normal size."
        vi "Alright mr smart arse, get over here..."
        scene swim03 with dissolve
        play sound "Sounds/gasping.mp3"
        $ renpy.pause(1.0, hard=True)
        vi "OMG! Err... OK, put your speedos back on."
        $ lust_points[23] +=2
        $ score += 2
        show lust02:
            xalign 0.75 yalign 0.6
            linear 1.0 yalign 0.4
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
        k "What did you see teach? Does [name] have a big one? heehee..."
        play sound "Sounds/katehihi.mp3"
        vi "Shut up Kate! Well, your bulge is no excuse, it's kind of aerodynamic actually. I want to see you in the water doing a 100m crawl NOW!"
        jump Sport03Day03

label Sport03Day03:
scene swim04 with dissolve
play sound "Sounds/diving.mp3"
$ renpy.pause(2.0, hard=True)
scene swim05 with dissolve
play sound "Sounds/swimming.mp3"
$ renpy.pause(4.0, hard=True)
p "I'll show her... Puff...puff..."
vi "Faster, faster, you're slacking off!"
menu:
    "Increase the tempo (-1 stamina)":
        jump IncreasedTempo
    "Don't increase the tempo":
        jump NormalTempo

label IncreasedTempo:
scene swim05b with dissolve
play sound "Sounds/swimming.mp3"
$ renpy.pause(4.0, hard=True)
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.6
    linear 1.0 yalign 0.8
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
scene swim06 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Alright! 1mn and 9s, that's the best time anyone has ever achieved in this school! Congrats, whatever your name is!"
$ lust_points[23] += 2
$ score += 2
show lust02:
    xalign 0.4 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
p "[name] Johnson is my name. That was a piece of cake for me!"
scene swim07 with dissolve
$ renpy.pause(1.0, hard=True)
md "Oh wow, [name], I didn't realize you were such a good swimmer!"
$ lust_points[14] += 2
$ score += 2
show lust02:
    xalign 0.2 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
vi "We'll definitely pair you two for the competition on Sunday..."
jump Sport04Day03

label NormalTempo:
scene swim05b with dissolve
play sound "Sounds/swimming.mp3"
$ renpy.pause(4.0, hard=True)
scene swim06 with dissolve
vi "Not bad, 1mn and 30s. But not good enough to beat their lead swimmer... You're gonna have to train hard kiddo, whatever your name is!"
p "[name] Johnson is my name. Sure, I didn't really push myself..."
$ lust_points[23] += 1
$ score += 1
show lust01:
    xalign 0.4 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
scene swim07 with dissolve
$ renpy.pause(1.0, hard=True)
md "Mmh, [name], you're a pretty good swimmer after all..."
$ lust_points[14] += 1
$ score += 1
show lust01:
    xalign 0.2 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
vi "We'll definitely pair you two for the competition on Sunday..."
jump Sport04Day03

label Sport04Day03:
scene swim02 with dissolve
$ hour += 1
$ renpy.pause(1.0, hard=True)
vi "Now, show me your teamwork. Maddy, you go with [name], Quentin with Kate." 
vi "Frieda with... the other boy. Laura with that French chick. Joséphine, tu vas avec Laura, d'accord?"
fc "Pourquoi faire? Je ne sais pas nager."
la "God I fucking hate this school! Viens avec moi Joséphine... (sigh)"
p "Fancy that, Laura speaks French too... I wonder how all of this works in the French version of this game?"

scene swim08 with dissolve
$ renpy.pause(1.0, hard=True)
md "So, we should work on our relay timing maybe."
menu:
    "Sure, this competition is important.":
        md "It's good to see you take it so seriously! I like your dedication!"
        $ lust_points[14] += 1
        $ score += 1
        show lust01:
            xalign 0.1 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        "You spend the rest of the swimming practice training with Maddy."
        jump EndSwimDay03

    "Hang on just a minute, I need to speak to Frieda.":
        scene swimfrieda with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Hi Frieda, are you having fun?"
        fr "Not really, I'm teamed up with that other boy, I don't even know his name and he never speaks."
        p "Maybe next time I'll tell the teacher to team you up with me instead..."
        fr "That would be wunderbar! I like you much better."
        $ lust_points[8] += 1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        vi "I told you to practice with MADDY, not Frieda! Go back immediately to your end of the pool and do what you're told!"
        $ lust_points[23] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.1 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01 
        jump MaddyTrainDay03

    "Hang on just a minute, I need to speak to Laura.":
        scene swimlaura with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Hi Laura, are you having fun?"
        la "Not really, I'm teamed up with Joséphine, she can't even swim! And I hate this school and this dumb swimming practice anyway!"
        p "Yeah, I agree, we should all just drown to spite the teacher."
        la "You're so silly. And such a rebel..."
        $ lust_points[13] += 1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        vi "I told you to practice with MADDY, not Laura! Go back immediately to your end of the pool and do what you're told!"
        $ lust_points[23] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.1 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01 
        jump MaddyTrainDay03

label MaddyTrainDay03:
scene swim08 with dissolve
$ renpy.pause(1.0, hard=True)
md "So, we should work on our relay timing maybe."
p "Sure, this competition is important."
md "It's good to see you take it so seriously! I like your dedication!"
$ lust_points[14] += 1
$ score += 1
show lust01:
    xalign 0.1 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
"You spend the rest of the swimming practice training with Maddy."
jump EndSwimDay03

label EndSwimDay03:
scene swim02 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Ok, time's up, we'll see each other tomorrow morning for our trip to BigDong Falls, don't forget to bring your swimsuits if you want to have some fun there!"
vi "[name], since you're new, it's your turn to help me clean up the pool, it will only take a few minutes."
"You help Viviane with the clean-up chores, head for a shower and then for school lunch."
$ renpy.pause(1.0, hard=True)
jump LunchDay03

label LunchDay03:
scene lunchallday03 with dissolve
$ hour += 1
stop music
play music "Sounds/lunchambience.mp3"
$ renpy.pause(1.0, hard=True)
$ lustaddedB = 2
call Challenger from _call_Challenger_36
$ lustaddedB = 1
call Challenger from _call_Challenger_37
$ challengercalls += 2
p "The school cafeteria is packed... And there seems to be a new girl sitting with Nikki. I arrived too late so I guess I don't have a choice today..."

label LunchClassDay03:
scene lunchday03 with dissolve
$ renpy.pause(1.0, hard=True)
q "Hey [name], there you are! Look, you can sit right next to your best friend who kept this seat for you..."
menu:
    "Cool, thanks Quentin...":
        q "You're welcome, that's what best friends are for!"
        jump LunchClass02Day03
    "I'll make sure to thank Frieda for that then.":
        scene lunchday03b with dissolve
        $ renpy.pause(1.0, hard=True)
        q "Humpf... That's not what I meant..."
        $ quentinnotfriends = True
        jump LunchClass02Day03

label LunchClass02Day03:
scene lunch02sit with dissolve
$ renpy.pause(1.0, hard=True)
if (quentinnotfriends == True):
    show lunchlaurahappy with dissolve
    la "I saw what you did there... That was wicked evil!"
    $ lust_points[13] +=1
    $ score += 1
    show lust01:
        xalign 0.35 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    hide lunchlaurahappy
label LunchChoiceDay03:
scene lunch02sit    
menu:
    "Talk to Laura" if (spokenlunchlaura == False):
        $ spokenlunchlaura = True
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
                jump LunchChoiceDay03
            "See, I'm wearing a black tank top today!" if (blacktop == True) and (lauratop == False):
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
                jump LunchChoiceDay03
            "What are you up to today Laura?":
                la "Hanging out with Damian and Joséphine. Discussing how much life sucks. As per usual... (sigh)"
                jump LunchChoiceDay03
    "Talk to Kate" if (spokenlunchkate == False):
        $ spokenlunchkate = True
        show lunchkateunhappy
        k "I've got detention again... When I could be thinking about what bikini I could wear..."
        p "Yeah, our teacher is really nasty to you, I don't understand why."
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
                jump LunchChoiceDay03
            "Since you will compete in the bikini pageant, I could maybe take pictures of you so you can better decide which bikini to choose?" if (katephotoasked == False):
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
                jump LunchChoiceDay03
            "Maybe I could cheer you up with a photoshoot session this afternoon?" if (katephotoasked == True):
                show lunchkatehappy with dissolve
                k "Oooh, yes! I have a couple of bikinis I would like to try on!"
                p "Come to my place at 5pm or 6pm then, I'll have everything set up!"
                k "Oh, really? That's so great, I'll be there!"
                $ katephotoplanned = True                
                if (camera == False):
                    p "I'd better find a camera TODAY or she'll be mighty disappointed..."
                    jump LunchChoiceDay03
                if (camera == True):
                    p "(I'd better make sure I'm back home by 5 or 6pm...)"
                    jump LunchChoiceDay03
            "Don't study and daydream about stuff instead. That's what I always do during detention.":
                show lunchkatehappy with dissolve
                k "Oooh, thanks for the advice [name]!"
                jump LunchChoiceDay03

    "Talk to Frieda":
        $ spokenlunchfrieda = True
        scene lunchfriedaday03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Hey Frieda, what are you doing this afternoon?"
        fr "I vill be studying in the school library. Again..."
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
        jump LunchChoiceDay03
    "Talk to Maddy" if (spokenlunchmaddy == False):
        $ spokenlunchmaddy = True
        show lunchmaddyhappy
        p "It was great training with you this morning. You're the best swimmer I know."
        md "Oooh, thanks [name], you're not bad yourself..."
        $ lust_points[14] +=1
        $ score += 1
        show lust01:
            xalign 0.8 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01         
        jump LunchChoiceDay03
    "Talk to Quentin" if (spokenlunchquentin == False):
        $ spokenlunchquentin = True
        if (quentinnotfriends == True):
            q "I ain't talking to you. You were mean to me."
            jump LunchChoiceDay03        
        scene lunchquentinhappy with dissolve
        $ renpy.pause(1.0, hard=True)
        q "I bet you're the kind of guy who loves astronomy, right?"
        menu:
            "No I'm not, it's for nerds.":
                k "Hee hee."
                play sound "Sounds/katehihi.mp3"
                q "Humpf, I guess I was wrong then. You're just a boring jock."
                $ spokenlunchquentin = True
                jump LunchChoiceDay03
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
                jump LunchChoiceDay03
    "Just eat up already":
        jump LunchEndDay03

label LunchEndDay03:
stop music
scene lunchempty with dissolve
$ hour += 1
$ renpy.pause(1.0, hard=True)
p "Everyone finished eating and left..."

if (fuckedschoolgirl == True):
    play sound "Sounds/pasystem.mp3"
    ps "[name] Johnson, please report to the principal's office immediately."
    p "Why? What have I done this time I wonder... I guess I don't have a choice or I might be expelled and Nancy would be mad... (sigh)."
    jump PrincipalGuidanceDay03
if (detention == True):
    p "I have to go to detention or I'm in trouble..."
    jump DetentionDay03

label SchoolChoiceDay03:
stop music
p "I've got the afternoon free. What should I do?"
menu:
    "Go to my locker" if (seenlocker03 == False):
        jump LockerDay03
    "Go to the school gym" if (seenschoolgym03 == False):
        jump SchoolGym01Day03
    "Go to the school library" if (seenlibrary03 == False):
        jump Library01Day03
    "Go to the school backyard" if (seengoths03 == False):
        jump GothsDay03
    "Go on the school rooftop" if (discoverrooftop == True):
        jump RooftopDay03
    "Go to the principal's office" if (seenwillie03 == False):
        jump WillieCorridorDay03
    "Go to the sports hall" if (seenhall03 == False) and (williequest == True):
        jump SportsHallDay03
    "Go to the school bathroom" if (seenbathroom03 == False):
        jump SchoolBathroom01Day03
    "Leave the school and go the Burbs":
        jump BurbsDay03

label DetentionDay03:
scene detention01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Kate and [name], You both have detention for one hour. During that time, I want to see you studying hard, is that clear?"
p "Damn, this is going to be so boring... I wonder what I could do to pass the time?..."
p "Mmh, Kate is looking great in that schoolgirl outfit... But it would be better if she was naked..."
menu:
    "Daydream about Kate":
        jump KateDayDreamDay03
    "Pretend you're studying":
        jump EndDetentionDay03

label KateDayDreamDay03:
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

label EndDetentionDay03:
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
        $ katephotoplanned = True
        k "Ooh, yeah, yippee! I'll DEFINITELY be there!"
        jump SchoolChoiceDay03
    "Ok, see you tomorrow Kate!":
        k "Ooh, yeah, see you tomorrow [name], hee hee!"
        play sound "Sounds/katehihi.mp3"
        jump SchoolChoiceDay03

label PrincipalGuidanceDay03:
scene guidance01 with dissolve
$ renpy.pause(1.0, hard=True)
so "Do you know why I called you in [name]?"
p "Err, no..."
so "Because despite my strict orders, you FUCKED ONE OF OUR GIRLS YESTERDAY!"
menu:
    "Yeah, so? I'm DA MAN, I fuck whoever I want!":
        so "(sigh) Once again, you leave me no choice... Get undressed and get that cock of yours hard NOW!"
        jump PrincipalGuidance02Day03
    "This is FAKE NEWS! There was no collision between my cock and any schoolgirl's pussy, believe me.":
        so "Well, I DON'T believe you! My sources are reliable. You're a liar and you must pay for this. Get undressed and get that cock of yours hard NOW!"
        $ lust_points[20] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.7 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        jump PrincipalGuidance02Day03

label PrincipalGuidance02Day03:
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
call screen principalfootjob02
screen principalfootjob02:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("FootJobFast02Day03")

label FootJobFast02Day03:
stop movie
hide faster
play music "Sounds/principalfast02.mp3"
show guidancefast
show cum
call screen footjobfaster02
screen footjobfaster02:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PrincipalCum02Day03")

label PrincipalCum02Day03:
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
p "I heard you were looking for volunteers to help you in your senate seat election campaign."
so "Yes, that is correct. A boy like you could put posters up downtown, are you interested in helping?"
p "What do I get in return?"
so "Humpf... Normally, people volunteer because they adhere to a political ideal! But fine, I will suspend your guidance session for a day if you spend an hour of your time putting posters up downtown."
menu:
    "Deal!":
        so "Welcome aboard! The posters are in the corner over there. Take a stack of them on your way out."            
        $ principaldeal = True
        so "Now off you go, I need to call Willie our janitor to clean that mess you made... I'd better not see you again because you fucked yet ANOTHER of our girls!"
        jump SchoolChoiceDay03
    "Not interested, sorry, I'll be rooting for your opponent anyway!":
        so "Then you'll be on the losing side! Now get out of here, I need to call Willie our janitor to clean that mess you made!"
        jump SchoolChoiceDay03
    
label RooftopDay03:
scene rooftop01 with dissolve
play music "Sounds/wind.mp3"
$ renpy.pause(1.0, hard=True)
p "Ah, here's Quentin's telescope..."
if (blacktop == True):
    scene rooftop02black with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop02Day03
else:
    scene rooftop02 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop02Day03

label Rooftop02Day03:
p "Let's see what the neighbors are up to..."
$ renpy.pause(1.0, hard=True)
p "Mr Anderson is doing some gardening... BORING!"
p "Hang on a minute, his wife and daughter are on the upper deck jacuzzi..."
scene voyeur01 with dissolve
$ renpy.pause(1.0, hard=True)
p "And there's some muscular redhead boy proudly displaying his massive dong to them. That could become interesting..."
menu:
    "Continue watching (+1 stamina and +1hr)":
        jump Rooftop03Day03
    "Leave, this is bordering on NTR and my fragile ego can't take it!":
        jump SchoolChoiceDay03

label Rooftop03Day03:
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
if (blacktop == True):
    scene rooftop02black with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop04Day03
else:
    scene rooftop02 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Rooftop04Day03

label Rooftop04Day03:
$ hour += 1
$ stamina += 1
show stamina01:
    xalign 0.7 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide stamina01
jump SchoolChoiceDay03


label Library01Day03:
stop music
play music "Sounds/coughing.mp3"
if (wenttojail == True):
    scene marialibrary02 with dissolve
    $ renpy.pause(1.0, hard=True)
    ma "Ah, it's you... The child molester."
    p "I'll have you know that I was cleared by the justice system! Your accusation amounts to defamation!"
    ma "OK, OK, calm down. I'm here to work in the library and help students. So, what can I do for you?"
    jump Library02Day03

if (wenttojail == False) and (lollyseen == True):
    scene marialibrary01 with dissolve
    $ renpy.pause(1.0, hard=True)
    ma "Oh, hello [name]! I'm glad to see you here, it means you truly are a student dedicated to acquiring knowledge through the wonders of book reading!"
    p "Err...Yeah, sure."
    ma "So, what can I do for you?"
    jump Library02Day03

if (wenttojail == False) and (lollyseen == False):
    scene marialibrary01 with dissolve
    $ renpy.pause(1.0, hard=True)
    ma "Hello, I don't think I've seen you here before. I'm Maria, the school's library assistant. What can I do for you?"
    jump Library02Day03

label Library02Day03:
scene marialibrary04 with dissolve
$ renpy.pause(1.0, hard=True)
menu:
    "I was wondering if you had any books about the native plants of Veri-Bosti..." if (spokemaria == False):
        jump Library03Day03
    "Wanna take a look at my hardcover?":
        scene marialibrary03 with dissolve
        $ renpy.pause(1.0, hard=True)
        ma "I'd rather not, it might not live up to my Great Expectations..."
        jump Library02Day03
    "I don't need any help, I know what I'm doing...":
        ma "Fine. Come back here though if you want to borrow a book."
        label LibraryChoiceDay03:
        menu:
            "Talk to Maria":
                jump Library02Day03
            "Look for Frieda" if (spokefriedalibraryday03 == False):
                jump Library04Day03
            "Look for a book on native plants" if (spokenerdy == False):
                jump Library05Day03
            "Learn how to use the hypnosis pendulum" if (pendulum == True) and (pendulumactive == False):
                jump LibraryPendulumDay03
            "Read the book about Goths that Laura gave you" if (book == True) and (bookread == False):
                jump LibraryGothDay03
            "Leave the library":
                jump SchoolChoiceDay03

label Library03Day03:
stop music
$ spokemaria = True
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
ma "It almost became extinct because so many rich people overseas wanted one until our President-Governor put an ban on its export."
scene marialibrary07 with dissolve
$ renpy.pause(1.0, hard=True)
ma "I still don't get the craze for this plant. It stinks of rotten milk, because there's a putrid white liquid that oozes from its flower tip, see?"
p "Ah, very interesting. Where could you find these plants on the island?"
ma "It says here that they grow in very humid tropical forests, or possibly near waterfalls."
ma "You might be lucky to see one tomorrow on your schooltrip! I'll be accompanying your class."
ma "Of course, you can't pick one up, it's illegal. So if you see one, make sure to let me know so the whole class can have a look at it."
p "Of course, I'll look out for them and I'll call you if I spot one."
$ plantknowledge = True
$ lust_points[15] += 1
$ score += 1
show lust01:
    xalign 0.45 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
ma "That's a good boy! Until then, you can borrow this book and study it for your essay. Here!"
p "Thanks...(shit, now she expects me to study this godamn book... What a waste of time.)"
if (blacktop == True):
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
$ lust_points[15] += 1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
jump Library02Day03


label Library05Day03:
stop music
scene nerdy00 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, this library has too many books, I'll never find what I'm looking for..."
menu:
    "Go back and talk to Maria":
        jump Library02Day03
    "Talk to the nerdy girl with glasses" if (spokenerdy == False):
        jump Library06Day03

label Library06Day03:
$ spokenerdy = True
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
                jump Library02Day03

            "Just tell me where the section is already!":
                play sound "Sounds/gasping.mp3"
                ne "It's behind you. Don't move, I'll get that book for you..."
                if (blacktop == True):
                    scene nerdy05black with dissolve
                else:
                    scene nerdy05 with dissolve
                $ renpy.pause(1.0, hard=True)
                ne "There you are... Sorry, I need to go, my panties are all wet!"
                scene nerdy03 with dissolve
                $ renpy.pause(1.0, hard=True)                
                p "Err, sure... Thanks... See you around..."
                if (blacktop == True):
                    scene nerdy06black with dissolve
                else:
                    scene nerdy06 with dissolve
                p "Ah, there's a picture of the \"Bostiboobicus Gigantus\". It says it stinks of rotten milk..."
                p "..Because there's a putrid white liquid that oozes from its flower tip... I see, interesting..."
                $ plantknowledge = True
                jump Library02Day03                
    "Ah, I see, you're crazy.":
        ne "Oh no, the only boy who ever spoke to me thinks I'm crazy, AAARGH!"
        scene nerdy03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Hey, where are you going, come back, you didn't tell me where the section on native plants was!"
        p "Shit...Now I have to go back and ask Maria..."
        jump Library02Day03
    "You talk like you've never seen a cock in your life.":
        ne "What? A COCK? Oh my God, do you have ONE?"
        p "Err, Yeah, I have one."
        ne "Show me, show me, show me!"
        p "What, like here right now?"
        ne "Yes, show me right now and I'll tell you where the section on native plants is!"
        menu:
            "Pull your shorts down...":
                if (blacktop == True):
                    scene nerdy04black with dissolve
                else:
                    scene nerdy04 with dissolve                    
                $ renpy.pause(1.0, hard=True)
                ne "Oh, it's so beautiful! I want to touch it..."
                menu:
                    "Be my guest...":
                        if (blacktop == True):
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
                                jump Library02Day03
                            "Now that you've touched it, show me where that book I'm looking for is...":
                                ne "It's behind you. Don't move, I'll get it for you..."
                                play sound "Sounds/gasping.mp3"
                                if (blacktop == True):
                                    scene nerdy05black with dissolve
                                else:
                                    scene nerdy05 with dissolve
                                $ renpy.pause(1.0, hard=True)
                                ne "There you are... Sorry, I need to go, my panties are all wet!"
                                p "Err, sure... Thanks... See you around..."
                                if (blacktop == True):
                                    scene nerdy06black with dissolve
                                else:
                                    scene nerdy06 with dissolve
                                p "Ah, there's a picture of the \"Bostiboobicus Gigantus\". It says it stinks of rotten milk..."
                                p "...Because there's a putrid white liquid that oozes from its flower tip... I see, interesting..."
                                $ plantknowledge = True
                                jump Library02Day03
                    "First, tell me where the section on native plants is...":
                        ne "It's behind you. Don't move, I'll get that book for you..."
                        play sound "Sounds/gasping.mp3"
                        if (blacktop == True):
                            scene nerdy05black with dissolve
                        else:
                            scene nerdy05 with dissolve
                        $ renpy.pause(1.0, hard=True)
                        ne "There you are... Sorry, I need to go, my panties are all wet!"
                        p "Err, sure... Thanks... See you around..."
                        if (blacktop == True):
                            scene nerdy06black with dissolve
                        else:
                            scene nerdy06 with dissolve 
                        p "Ah, there's a picture of the \"Bostiboobicus Gigantus\". It says it stinks of rotten milk..."
                        p "...Because there's a putrid white liquid that oozes from its flower tip... I see, interesting..."
                        $ plantknowledge = True
                        jump Library02Day03
            "First, tell me where the section on native plants is...":
                ne "It's behind you. Don't move, I'll get that book for you..."
                play sound "Sounds/gasping.mp3"
                if (blacktop == True):
                    scene nerdy05black with dissolve
                else:
                    scene nerdy05 with dissolve
                $ renpy.pause(1.0, hard=True)
                ne "There you are... Sorry, I need to go, my panties are all wet!"
                p "Err, sure... Thanks... See you around..."
                if (blacktop == True):
                    scene nerdy06black with dissolve
                else:
                    scene nerdy06 with dissolve 
                p "Ah, there's a picture of the \"Bostiboobicus Gigantus\". It says it stinks of rotten milk..."
                p "...Because there's a putrid white liquid that oozes from its flower tip... I see, interesting..."
                $ plantknowledge = True
                jump Library02Day03                
            "Ah, I see, you're crazy.":
                ne "Oh no, the only boy who ever spoke to me thinks I'm crazy, AAARGH!"
                scene nerdy03 with dissolve
                $ renpy.pause(1.0, hard=True)
                p "Hey, where are you going, come back, you didn't tell me where the section on native plants was!"
                p "Shit...Now I have to go back and ask Maria..."
                jump Library02Day03

label Library04Day03:
scene friedalibrary01day03 with dissolve
$ renpy.pause(1.0, hard=True)
$ spokefriedalibraryday03 = True
p "Hi Frieda, what's up? You seem to be studying hard... Again."
fr "I can think a bit more clearly now with those new clothes... But it's still tough.... I really need an A or my parents vill kill me."
label FriedaChoiceDay03:
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
        jump FriedaChoiceDay03
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
            jump FriedaFuckDay03            
        menu:
            "Use the pendulum on her" if (pendulumactive == True) and (lust_points[8] >=8):
                jump FriedaPendulumDay03
            "Spray yourself with some pheromones" if (pheromone == True) and (lust_points[8] >=8):
                play sound "Sounds/spray.mp3"
                $ renpy.pause(1.0, hard=True)
                jump FriedaPheromonesDay03 
            "Say she's welcome":
                p "You're welcome. Hopefully, this will lead to a growing relationship between us. Mine is definitely growing right now."
                jump FriedaChoiceDay03            
        p "You're welcome. Hopefully, this will lead to a growing relationship between us. Mine is definitely growing right now."
        jump FriedaChoiceDay03
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
        jump FriedaChoiceDay03
    "OK, I'll leave you alone to study then...":
        jump LibraryChoiceDay03

label FriedaPendulumDay03:
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
jump FriedaFuckDay03
    
label FriedaPheromonesDay03:
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
jump FriedaFuckDay03

label FriedaFuckDay03:
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
label FriedaCockRubDay03:
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
        jump FriedaCockRubDay03
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
label FriedaFuckChoiceDay03:
menu:
    "Let her ride you" if (friedaride == False):
        jump FriedaFuckRideDay03
    "Take her up the arse" if (friedaarse == False):
        jump FriedaFuckArseDay03
    "Tell her to finish you off with a blowjob" if (friedaarse == True) and (friedaride == True):
        jump FriedaFuckBlowjobDay03


label FriedaFuckRideDay03:
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
        jump FriedaFuckArseDay03
    "Tell her to finish you off with a blowjob" if (friedaarse == True) and (friedaride == True):
        jump FriedaFuckBlowjobDay03

label FriedaFuckArseDay03:
scene friedafuck10 with dissolve
$ friedaarse = True
$ renpy.pause(1.0, hard=True)
fr "You are stretching my poor little anus zo much! AAAAH!"
p "That's nothing, I'm not even halfway in. Let me stretch it a bit more..."
scene friedafuck10b with dissolve
$ renpy.pause(1.0, hard=True)
p "There. That's better. A solid ten inches of my ramrod up your arse!"
fr "Be caref.."
label FriedaFuckArseDay03b:
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
        jump FriedaFuckArseDay03b        
    "Let her ride you" if (friedaride == False):
        jump FriedaFuckRideDay03
    "Tell her to finish you off with a blowjob" if (friedaarse == True)and (friedaride == True):
        jump FriedaFuckBlowjobDay03

label FriedaFuckBlowjobDay03:
stop music
play music "Sounds/friedaslow.mp3"
show friedafuckslow
show faster
call screen friedafuckslowday03
screen friedafuckslowday03:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("FriedaFuckFast")

label FriedaFuckFast:
hide faster
play music "Sounds/friedafast.mp3"
show friedafuckfast
show cum
call screen friedafuckfastday03
screen friedafuckfastday03:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FriedaFuckCum")

label FriedaFuckCum:
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
$ backdoor += 1
window hide
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
fr "But we need to get dressed. And cleaned up..."
p "Yes, that is probably a good idea. I mean, some people DO use the library sometimes."
$ friedafucked = True
if (friedajosewin == False):
    $ friedawin = True
    p "(José is going to be mightily pissed off when he gets the pic I'm sending him...)"
$ fuckedschoolgirlday03 = True
$ hour += 1
jump SchoolChoiceDay03

label LibraryPendulumDay03:
if (blacktop == True):
    scene ryanlibraryinternetblack with dissolve
else:
    scene ryanlibraryinternet with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/keyboard.ogg"
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump LibraryChoiceDay03

label LibraryGothDay03:
if (blacktop == True):
    scene ryanreadinglibraryblack with dissolve
else:
    scene ryanreadinglibraryinternet with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump LibraryChoiceDay03


label SchoolBathroom01Day03:
$ seenbathroom03 = True
$ d2rollbath=renpy.random.randint(0, 1)
if (d2rollbath == 0):
    jump SchoolBathroom01Day03b      
if (d2rollbath == 1):
    jump SchoolBathroom01Day03c   

label SchoolBathroom01Day03b:
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
                if (blacktop == True):
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
                jump SchoolChoiceDay03
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
                if (blacktop == True):
                    scene schoolbathroombrittany06black with dissolve
                    $ renpy.pause(1.0, hard=True)
                else:
                    scene schoolbathroombrittany06 with dissolve
                    $ renpy.pause(1.0, hard=True)
                br "Pff, pathetic! Now leave me alone little boy, I need to pamper myself."
                jump SchoolChoiceDay03


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
        jump SchoolChoiceDay03

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
        jump SchoolChoiceDay03
    "Walk past her and ignore her":
        if (blacktop == True):
            scene schoolbathroombrittany05black with dissolve
            $ renpy.pause(1.0, hard=True)
        else:
            scene schoolbathroombrittany05 with dissolve
            $ renpy.pause(1.0, hard=True)
        br "Hey you, look at me!"
        if (blacktop == True):
            scene schoolbathroombrittany06black with dissolve
            $ renpy.pause(1.0, hard=True)
        else:
            scene schoolbathroombrittany06 with dissolve
            $ renpy.pause(1.0, hard=True)
        p "Why? I prefer to look at myself. Yeah, I'm da man, I'm DA MAN!"
        br "Pff, pathetic! Now leave me alone little boy, I need to pamper myself."
        jump SchoolChoiceDay03

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
        jump SchoolChoiceDay03

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
        jump SchoolChoiceDay03
        
label SchoolBathroom01Day03c:
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
    "Stick your cock through the ouside wall and wait.":
        jump GloryholeDay03
    "Have a piss and leave.":
        play sound "Sounds/peeing.mp3"
        $ renpy.pause(10.0, hard=True)
        p "Aaah, I needed that."
        jump SchoolChoiceDay03

label GloryholeDay03:
$ d2rollglory=renpy.random.randint(0, 1)
if (d2rollglory == 0):
    jump GloryholeDay03b      
if (d2rollglory == 1):
    jump GloryholeDay03c 

label GloryholeDay03b:
if (blacktop == True):
    scene gloryhole01black with dissolve
    $ renpy.pause(1.0, hard=True)
else:
    scene gloryhole01 with dissolve
    $ renpy.pause(1.0, hard=True)
$ hour += 1
"I waited long enough. Nobody came to take the bait, I'm out of here."
scene schoolbathroom01 with dissolve
$ renpy.pause(1.0, hard=True)
jump SchoolChoiceDay03

label GloryholeDay03c:
$ seengloryhole03 = True
if (blacktop == True):
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
label GloryHoleSuckDay03:
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
        jump GloryHoleSuckDay03
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
br "Wow, what a cock... It can't possibly be José's, his bulge is not big enough..."
$ lust_pointsB[1] -=2
show challengerlustminus02:
    xalign 0.7 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/less.mp3"
$ renpy.pause(2, hard=True)
hide challengerlustminus02
$ hour += 1
if (blacktop == True):
    scene gloryholebrit06black with dissolve
    $ renpy.pause(1.0, hard=True)
else:
    scene gloryholebrit06 with dissolve
    $ renpy.pause(1.0, hard=True)
play sound "Sounds/footsteps.mp3"
p "Oooh, it was Brittany! What a slut! Then again, I'm a he-slut too..."
menu:
    "Call her and let her know it was you":
        jump GloryHoleEnd01Day03
    "Stay put and wait for her to leave":
        jump GloryHoleEnd02Day03
        
label GloryHoleEnd01Day03:
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
jump SchoolChoiceDay03
    
label GloryHoleEnd02Day03:
scene gloryholend with dissolve
$ renpy.pause(1.0, hard=True)
p "She's gone. Now I can do other stuff..."
jump SchoolChoiceDay03

label WillieCorridorDay03:
stop music
scene williecorridor with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/Willie.wav"
$ seenwillie03 = True
wi "Where do you think you're going lad?..."
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
            $ williequestdoneFshowerseen = True
            jump PrincipalSnoopingDay03
        if (vivianejosewin == False):
            p "OK, I'll get you your picture you fucking pervert! But I strongly condemn your immorality."
            wi "So says the lad who wants to sneak into Principal Titsworthy's office! Take a hike! And come back with a sexy picture of my Viviane..."
            $ williequest = True
            jump SchoolChoiceDay03
    "I have an appointment with Principal Titsworthy.":
        wi "Oh yeah? Well, she ain't there, so that's a wee bit suspicious."
        p "I'll wait for her then."
        wi "No you won't. Move it lad or Willie will report you to the Principal. And you wouldn't want to cross her, I tell ya!"
        jump SchoolChoiceDay03

label PrincipalSnoopingDay03:
scene principalsnooping with dissolve
play music "Sounds/snooping.mp3"
$ d2rolloffice=renpy.random.randint(0, 1)
if (d2rolloffice == 0):
    call screen officesnoop01
if (d2rolloffice == 1):
    call screen officesnoop02
$ renpy.pause(1.0, hard=True)
stop music
"I was too slow and didn't find the right folder... Now I have to leave or Willie will lock me up..."
jump SchoolChoiceDay03

label FoundFriedaGradeDay03:
scene principalsnooping
$ renpy.pause(1.0, hard=True)
stop music
p "Frieda...Frieda....Ah, there it is, now I'll change the F grade for an A. Piece of cake, I'm DA MAN!"
play sound "Sounds/Willie02.wav"
$ renpy.pause(2.0, hard=True)
$ friedachangedgrade = True
p "Let's get the hell out of here before the principal comes back..."
jump SchoolChoiceDay03

label SchoolGym01Day03:
$ seenschoolgym03 = True

if (d3rolls ==0):
    $ d2rolls=renpy.random.randint(0,1)
    if (d2rolls ==0):
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
                jump ChantelleRyanWorkoutDay03
            "Watch her for a while":
                jump SchoolGymChantelle02Day03
    if (d2rolls ==1):
        $ schoolgymmaddy = True
        jump SchoolGymMaddy01Day03

 
elif (d3rolls==1):
    $ d2rolls=renpy.random.randint(0,1)
    if (d2rolls ==0):
        $ schoolgymempty = True
        jump SchoolGymEmptyDay03
    if (d2rolls ==1):
        $ schoolgymmaddy = True
        jump SchoolGymMaddy01Day03
    
        
elif (d3rolls==2):
    $ d2rolls=renpy.random.randint(0,1)
    if (d2rolls ==0):
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
                jump ChantelleRyanWorkoutDay03
            "Watch her for a while":
                jump SchoolGymChantelle02Day03
    if (d2rolls ==1):
        $ schoolgymempty = True
        jump SchoolGymEmptyDay03

label SchoolGymEmptyDay03:
scene schoolgymempty with dissolve
$ renpy.pause(1.0, hard=True)
p "There's no one around, I could use this gym to train and get stronger..."
menu:
    "Do some heavy training, better equipment means I can cut on my routine time (+1hr)" if (workout == False):
        jump SchoolGymWorkoutDay03
    "Leave":
        jump SchoolChoiceDay03

label ChantelleRyanWorkoutDay03:
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
jump SchoolChoiceDay03

label SchoolGymChantelle02Day03:
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
        jump SchoolGymChantelle03Day03
    "Of course, I only use the biggest weights around all the time, piece of cake for me!":
        ch "Mmh, I want to see that..."
        jump SchoolGymChantelle04Day03
    "Actually, I was planning on a serious routine with barbells, but I need to concentrate...(+1hr)":
        ch "Sure, I'll continue my exercises and I'll leave you alone, don't worry..."
        p "Also, I like to train with my shorts and tank top off, hope you don't mind..."
        ch "Ooh? No... I don't mind..."
        jump ChantelleRyanWorkoutDay03
        
label SchoolGymChantelle03Day03:
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
        jump SchoolGymWorkoutDay03   
    "Leave": 
        jump SchoolChoiceDay03
 

label SchoolGymChantelle04Day03:
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
            jump SchoolGymWorkoutDay03
        "Leave":
            jump SchoolChoiceDay03
         
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
            jump SchoolGymWorkoutDay03
        "Leave":
            jump SchoolChoiceDay03
   
label SchoolGymWorkoutDay03:
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
jump SchoolChoiceDay03
    
label SchoolGymMaddy01Day03:
stop music
scene maddygym01 with dissolve
play music "Sounds/gymmusic02.mp3"
$ renpy.pause(1.0, hard=True)
p "Maddy is doing some gymnastics with a big ball..."
label SchoolGymMaddyChoiceDay03:
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
        jump SchoolChoiceDay03
    "Watch her for a while" if (maddygymwatchedDay03 == False):
        jump SchoolGymMaddy02Day03
    "Interrupt her to talk to her" if (maddygymtalkedDay03 == False):
        jump SchoolGymMaddy03Day03


label SchoolGymMaddy02Day03:
$ maddygymwatchedDay03 = True
scene maddygym02 with dissolve
$ renpy.pause(2.0, hard=True)
p "I can see her cleavage when she bends over...nice..."
md "What are you looking at? Stop looking at me like that FREAK!"
jump SchoolGymMaddyChoiceDay03

label SchoolGymMaddy03Day03:
$ maddygymtalkedDay03 = True
if (maddygymwatched == True):
    scene maddygym02 with dissolve
    $ renpy.pause(2.0, hard=True)

label SchoolGymMaddy03bDay03:
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
        jump SchoolGymMaddyChoiceDay03
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
                jump MaddyBalls01Day03
            "Sounds kinda girly...":
                md "Whatever... I'm done anyway, you can do your \"manly\" things on your own now..."
                jump SchoolGymEmptyDay03
    "What do you think about me hooking up with Frieda?":
        md "She's really busy with her studies, her parents put so much pressure on her, so I doubt she'll have time for a stupid boy like you..."
        p "Well, gee, thanks for putting it so mildly."
        jump SchoolGymMaddy03bDay03
        
label MaddyBalls01Day03:
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
        jump MaddyBalls02Day03
    "Easier said than done...":
        jump MaddyBalls02Day03

label MaddyBalls02Day03:
scene maddygym05 with dissolve
$ renpy.pause(1.0, hard=True)
md "How about this one then?"
menu:
    "I'm giving up, this is not for me...":
        md "Giving up that easily? Not so \"manly\" after all...(wink)..."
        p "It's too tough, I'm too muscular and not flexible enough for this kind of stuff..."
        md "Well, I'm off, I have to study a bit, I'll leave you to your \"muscular manly\" things..."
        $ hour +=1
        jump SchoolGymEmptyDay03
    "I'll give it a try but don't make fun of me...":
        scene maddygym06 with dissolve
        $ renpy.pause(1.0, hard=True)
        md "Here, I'll help you... Not bad, you're getting the hang of it! But you're still quite...stiff..."
        p "Thanks for showing me Maddy, you're a great friend. Maybe I can show you how I train with huge barbells?"
        md "Mmmh, I was going to leave... But fine, why not..."
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
        jump SchoolGymEmptyDay03


label LockerDay03:
$ seenlocker03 = True
$ d2rolllocker=renpy.random.randint(0, 1)
if (d3rollb == 0):
    if (d2rolllocker == 0):
        jump LockerEmpty02Day03  
    if (d2rolllocker == 1):
        jump BritLockerDay03  

elif (d3rollb == 1):
    if (d2rolllocker == 0):
        jump LockerKate01Day03  
    if (d2rolllocker == 1):
        jump BritLockerDay03  

elif (d3rollb == 2):
    if (d2rolllocker == 0):
        jump LockerEmpty02Day03  
    if (d2rolllocker == 1):
        jump LockerKate01Day03  
 
label LockerEmpty02Day03:
scene lockerempty with dissolve
$ renpy.pause(1.0, hard=True)
$ seenlockerempty = True
p "There's no one around... Like everyone left school or something. And I'm here, wasting my time in empty corridors like an idiot."
jump SchoolChoiceDay03

label LockerKate01Day03:
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
        jump LockerKate08Day03
    "Well pick it up then.":
        k "Uh...oh...OK."
        scene lockerkate02
        $ renpy.pause(1.0, hard=True)
        k "Oooh, it's too far, I can't reach it...Uuh..."
        menu:
            "Well, bend over some more...":
                jump LockerKate03Day03
            "Offer to help":
                k "No, I'm...OK....Ooh, I hope my panties aren't...like... showing.... Are they?"
                menu: 
                    "Not at all, I can't see a thing. You can bend more.":
                        jump LockerKate03Day03
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
                        jump LockerKate03Day03
 
label LockerKate03Day03:
scene lockerkate03 with dissolve
$ renpy.pause(1.0, hard=True)
k "Like that?... I still can't find my pen...Oooh, Where is it?"
menu:
    "It's right in front of you, you dumb bimbo.":
        k "Oooh, yes, I see it now...Hee...hee..."
        play sound "Sounds/katehihi.mp3"
        jump LockerKate07Day03
    "Look some more, meanwhile, I'll probe behind you, it might be stuck somewhere...":
        k "Ooh, OK...hee...hee..."
        play sound "Sounds/katehihi.mp3"
        if (blacktop == True):
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
                jump LockerKate08Day03
            "Don't mind me, I'm in control of the situation...":
                jump LockerKate07Day03

label LockerKate07Day03:
scene lockerkate06 with dissolve
$ renpy.pause(1.0, hard=True)
k "Uh...OK...I'll continue looking... Oh, look, I found my pen!"
label LockerKate08Day03:
scene lockerkate07 with dissolve
$ renpy.pause(1.0, hard=True)
p "Well done, you're such a smart girl! By the way, it's actually a pencil, not a pen."
label KateLockerEndDay03:
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
    jump SchoolChoiceDay03
menu:
    "How about this afternoon at 5 or 6pm at my place for our photoshoot session?" if (katephotoasked == True):
        $ katephotoplanned = True
        k "Ooh, yeah, yippee! I'll DEFINITELY be there!"
        jump SchoolChoiceDay03
    "Ok, see you tomorrow Kate!":
        k "Ooh, yeah, see you tomorrow [name], hee hee!"
        play sound "Sounds/katehihi.mp3"
        jump SchoolChoiceDay03
        

label BritLockerDay03:
scene
stop music
play sound "Sounds/footsteps.mp3"
$ renpy.movie_cutscene("Day2/britlocker.ogv")
scene lockerbritmovie
show slowmo
call screen britslowmoDay03
screen britslowmoDay03:
    modal True
    button:
        xpos .82
        ypos .9
        xysize(120, 50)
        action Jump ("BritSlowMoDay03")
label BritSlowMoDay03:
play sound "Sounds/britlockerslowmo.mp3"
$ renpy.movie_cutscene("Day2/britlockerslowmo.ogv")
scene lockerbritmovie
$ renpy.pause(1.0, hard=True)

label LockerBrit01Day03:
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
        jump LockerBritEavesdropDay03
    "Barge in on the conversation":
        jump LockerBrit02Day03
        
label LockerBrit02Day03:
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
        jump SchoolChoiceDay03
    "I might be a junior student, but I'm a senior in bed.":
        show lockerbrit02b
        br "So boring, another wannabe stud. I only date REAL studs."
        j "Yeah, like ME. Do you hear that [name]?"
        br "I don't recall saying YOU were a REAL stud either..."
        show lockerbrit02c
        j "But, babe, everyone knows I'm the school stud..."
        br "Well, maybe I should look OUTSIDE of this school... A goddess like me deserves the BEST..."
        jump BritLocker03Day03
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
        jump BritLocker03Day03

label BritLocker03Day03:
scene lockerbrit02 with dissolve
$ renpy.pause(1.0, hard=True)
br "I've wasted enough time talking to you. A true princess like me needs to spend more time pampering herself."
br "Do not disturb me until I grant you permission."
menu:
    "Sure ma'am, at your cervix your Magnificent Beautifulness! (snickers)":
        show lockerbrit02b
        br "Be gone!"
        jump SchoolChoiceDay03
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
        jump SchoolChoiceDay03
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
            jump SchoolChoiceDay03
        menu: 
            "José is lying. It was actually 4 dollars.":
                br "Oh my God, that's even worse!!! Be gone and keep your cheap wristband!"
                jump SchoolChoiceDay03
            "Oh, hang on a minute, I seem to have given you the wrong one. My bad, this one was meant for...err.. Kate.":
                br "That would indeed suit that cheap bimbo... Who dares try to claim my throne as bikini pageant queen this year again!"
                br "Come back with your \"proper\" present tomorrow then. Or else..."
                p "Yeah... Of course... Ahem... Thank you, your...err.. majesty."
                $ britpresentfail = True
                jump SchoolChoiceDay03

label LockerBritEavesdropDay03:
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
        jump LockerBrit02Day03
    "Leave, you are defeated, what's the point in arguing...":
        jump SchoolChoiceDay03


label GothsDay03:
stop music
$ seengoths03 = True
scene goth01 with dissolve
$ renpy.pause(1.0, hard=True)

if (seengoths == False):
    jump GothsFirstDay03
else:
    jump GothsSecondDay03

label GothsFirstDay03:
p "Apparently, this is where the goth kids hang out… Laura is here, with some douchebag dude and the local girl."
la "Hey [name], you decided to join us?"
go "What’s he doing here? Do you know him Laura?"
if (madelaurasmile == True):
    la "Yeah, he’s a new classmate, he’s kinda cool though."
elif (madelaurasmile == False):
    la "Yeah, he’s a new classmate, he’s kinda of a bore though."

label GothChoiceDay03:
menu:
    "What's the local chick doing with you?" if (gothmenu <= 1):
        go "She's black, so she must be a goth."
        menu:
            "That makes absolutely no sense at all...":
                $ gothmenu += 1
                jump GothChoiceDay03
            "Of course, silly me.":
                $ gothmenu += 1
                jump GothChoiceDay03
    "Can I join your club?" if (gothmenu <= 1):
        go "No fucking way dude. You ain't no goth."
        $ gothmenu += 1
        jump GothChoiceDay03
    "Talk to the black girl" if (gothmenu >= 2):
        show goth01d
        fc "Ou suis-je, que fais-je, dans quel état j’erre?"
        p "Hum... moi... non par-ley... frenchie."
        fc "Hein? Quoi?"
        p "Yeah, I think she got it..."
        hide goth01d
        jump GothChoiceDay03
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
                        jump GothChoiceDay03
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
                        jump GothChoiceDay03
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
                    jump SchoolChoiceDay03      
    "Talk to the goth kid" if (gothmenu >= 2):
        go "What’s your favorite band?"
        menu:
            "New Kids on the Block":
                go "What? Get the hell out of here!"
                la "So lame... I hate you."
                jump SchoolChoiceDay03
            "Pharell Williams":
                go "Someone please kill me... That's not even a band!"
                jump GothChoiceDay03
            "The Cure":
                go "Nice..."
                jump GothChoiceDay03
            "What's it to you dipshit?":
                go "What the fuck?..."
                la "Haha, he got you there..."
                go "He didn't answer the question..."
                la "Real goths don't have to answer questions..."
                jump GothChoiceDay03

label GothsSecondDay03:
if (blacktop == False):
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
    jump SchoolChoiceDay03
    
if (blacktop == True):
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
        $ lauraritual = True
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
            $ lauraritual = True
        if (bookread == False):
            p "I didn't have time. But I'm planning on reading it, I swear!"
            la "Well, come back to us when you have. Right now, Damian is right, you're not ready."
    p "Time to leave them and do something else."
    jump SchoolChoiceDay03

label SportsHallDay03:
$ seenhall03 = True
stop music
scene sportshall01 with dissolve
$ renpy.pause(1.0, hard=True)
p "The lockers are empty... But I can hear some sound from the girl's shower area..."
menu:
    "Go and have a peek":
        jump SportsHall02Day03
    "Don't do it, you might get caught...":
        jump SchoolChoiceDay03

label SportsHall02Day03:
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
        jump PrincipalBackDay03
    "Do something else":
        jump SchoolChoiceDay03

label PrincipalBackDay03:
stop music
$ d2principalback=renpy.random.randint(0,1)  
if (d2principalback == 0):
    scene williecorridor with dissolve
    $ renpy.pause(1.0, hard=True)
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
    jump PrincipalSnoopingDay03

if (d2principalback == 1):
    jump PrincipalOfficeBackDay03

label PrincipalOfficeBackDay03:
scene principalback01 with dissolve
$ renpy.pause(1.0, hard=True)
so "What are you doing here? Can't you see I'm busy?"
menu:
    "Ah. Yes, I got the wrong door sorry.":
        so "Apparently, you can't read. It says \"Principal's Office\" in huge letters on the door. Now get out!"
        jump SchoolChoiceDay03  
    "I'm interested in joining your campaign as a volunteer." if (principaldeal == False):
        so "That's great, I can always use some extra help in putting posters up! Welcome on board!"
        so "I need some posters to be put up downtown. The posters are in the corner over there. Take a stack of them on your way out." 
        p "Will do Senator Titsworthy!"
        $ principaldeal = True
        jump SchoolChoiceDay03

label BurbsDay03:
stop music
if (hour == 7):
    p "Time to jog back home, I think I might have missed breakfast."
    jump Breakfast02jDay03

scene burbsday with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_34
    $ lustaddedB = 1
    call Challenger from _call_Challenger_35
    $ challengercalls += 2

if (hour == 20):
    p "Just in time to head back home for dinner!"
    jump DinnerDay03
if (hour == 19) and (teagangrocery == True) and (seenteaganhouse == False):
    p "Oops, it's 7pm. I promised Miss Cocque to fetch her groceries for her..."
    jump BurbsChoiceDay03
if (hour == 18 or hour == 19):
    p "I don't have time for much at this time of the day... Dinner is at 8pm."
    jump BurbsChoiceDay03

p "The burbs are so quiet during the day. I guess everyone is at work. Except me!"

label BurbsChoiceDay03:
if (hour == 20):
    p "Damn, it's 8pm already, I should really head back home for dinner..."
    jump DinnerDay03
p "What should I do?"
menu:
    "Explore the Burbs" if (discoverstore == False):
        jump BurbsExploreDay03
    "Go to the convenience store" if (discoverstore == True) and (evictedfromstore == False):
        jump StoreDay03
    "Go back home":
        jump HomeDay03
    "Go to Debby's house" if (auntdebbyseen == False):
        jump AuntDebbyHouseDay03
    "Take the bus to the beach" if (hour <= 17):
        $ busbeach = True
        jump BusDriveDay03
    "Take the bus heading downtown" if (hour <= 17):
        $ bustown = True
        jump BusDriveDay03
    "Go to the school" if (hour <= 15):
        scene lockerempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump SchoolChoiceDay03

label BurbsExploreDay03:
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
jump BurbsChoiceDay03

label BusStopDay03:
scene busdrive with dissolve
play sound "Sounds/busidle.mp3"
$ renpy.pause(1.0, hard=True)
p "Here it is finally..."
jump BusDriveDay03

label BusDriveDay03:
stop music
scene busdrive with dissolve
play music "Sounds/busidle.mp3"
$ renpy.pause(1.0, hard=True)
p "Here's the bus. Let's get on."
if (d2rollb == 0):
    jump BusEndDay03
else:
    jump OldWomanDay03

label OldWomanDay03:
stop music
scene oldwomanbus01 with dissolve
play music "Sounds/busdrive.mp3"
$ renpy.pause(1.0, hard=True)
ow "Well, here's a fine looking young man! Come and sit next to me boy."
menu:
    "Sit next to her":
        jump OldWoman02Day03
    "Ignore her":
        ow "What a rude boy!"
        jump BusEndDay03
  
label OldWoman02Day03:
if (blacktop == True):
    scene oldwomanbus02black with dissolve
else:
    scene oldwomanbus02 with dissolve
$ renpy.pause(1.0, hard=True)
ow "Did I tell you the story about the time I lost my cat Humphreys?"

menu:
    "I can't wait to hear it, I'm sure it's fascinating.":
        ow "Oh yes it is! You see, Humphreys normally eats his bowl of \"Crunchy Fishy Bits Deluxe\" at around 6am when I wake him up."
        ow "But the little rascal was not around and then...blah blah...blah...yadda yadda yadda..."
        jump Oldwoman03Day03    
    "Let me guess, you lost it, and then you found it.":
        ow "Oh no, there's much more to the story young man! The little rascal was not around at 6am when I normally wake him up..."
        ow "...for his bowl of \"Crunchy Fishy Bits Deluxe\" and then yadda yadda yadda..."
        jump Oldwoman03Day03

label Oldwoman03Day03:
if (blacktop == True):
    scene oldwomanbus03black with dissolve
else:
    scene oldwomanbus03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Oh God, she's gonna bore me to death..."
p "Wait, her wallet is right here on the side..."
menu:
    "Steal her wallet while she's rambling on":
        "You stole 20$ from a little old lady. Nice."
        $ money += 20
        jump BusEndDay03
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
        jump BusEndDay03

label BusEndDay03:
if (busbeach == True):
    $ hour += 1
    $ busbeach = False
    jump Beach01Day03
elif (bustown == True):
    $ hour += 1
    $ bustown = False
    jump DowntownDay03

label StoreDay03:
stop music
scene store01 with dissolve
play music "Sounds/storemusic.mp3"
$ renpy.pause(1.0, hard=True)

label StoreClerkDay03:
scene store01
if ((catchfrancine == True) or (catchbeer == True)) and (hour == 17):
    fa "Are you ready to start another shift today?"
    menu:
        "Yes, I'm ready.":
            jump StoreSecondWork01Day03
        "No, I'm too busy right now.":
            fa "Well, that's unfortunate... I could have really used your help again today..."
            jump ClerkChoiceDay03
    
if (storework == True) and (hour == 17) and (catchfrancine == False) and (catchbeer == False):
    fa "Are you ready to start your shift today?"
    menu:
        "Yes, I'm ready.":
            jump StoreWork01Day03
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
            jump ClerkChoiceDay03
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
    jump BurbsChoiceDay03   
elif (hour == 19) and (teagangrocery == True) and (seenteaganhouse == False):
    fa "Oh, you're just in time to pick up Miss Cocque's groceries. I was about to close."
    p "I'll get them to her right away!"
    jump TeaganHouse01Day03
elif (hour == 19):
    fa "Welcome to \"Seven Square\", your local shop that's opened from seven till... seven."
    fa "I'm sorry, but it is seven o'clock. The second seven. So we are closing."
    fa "Please come back tomorrow to your local convenience store \"Seven Square\" between 7am and... 7pm!"
    jump BurbsDay03    
else:
    fa "Welcome to \"Seven Square\", your local shop that's opened from seven till... seven."

label ClerkChoiceDay03:
if (catchfrancine == True) or (catchbeer == True):
    fa "So, how may I help you?"
else:
    fa "My name is Francine, how may I help you?"
menu:
    "Chat with her":
        jump StoreChatDay03 
    "Buy something":
        jump StoreBuyDay03
    "Leave":
        jump BurbsDay03

label StoreChatDay03:
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
                        jump StoreNoDealDay03
                    "It's a deal!":
                        $ halfprice = True
                        jump StoreDealDay03
            "It's a deal!":
                jump StoreDealDay03
    "Just thought I’d check a few things out, you being one of them...":
        scene store03
        fa "I can barely contain my laughter."
        jump StoreClerkDay03
    
label StoreDealDay03:
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
            jump StoreBuyDay03
        "No thanks.":
            fa "Alright, see you another day then."
            jump BurbsDay03
jump StoreClerkDay03

label StoreWork01Day03:
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
        jump CatchFrancineDay03
    "Catch the beer":
        jump CatchBeerDay03

label CatchFrancineDay03:
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
jump StoreTeagan01Day03

label CatchBeerDay03:
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
jump StoreTeagan01Day03

label StoreTeagan01Day03:
play music "Sounds/storemusic.mp3"
scene storeteagan01 with dissolve
$ renpy.pause(1.0, hard=True)
p "There's Miss Cocque doing her shopping, she hasn't noticed me yet."
menu:
    "Hide and hope she doesn't see you":
        jump StoreHideDay03
    "Greet her and ask her if you can help with anything":
        jump StoreTeagan02Day03

label StoreHideDay03:
scene storeteaganhide with dissolve
$ renpy.pause(1.0, hard=True)
p "Phew, she almost saw me but I'm think I managed to avoid her... And she's on her way out."
p "At the same time, watching that arse... Maybe I should have greeted her..."
p "Oh well, only a few more minutes of hard labour and my shift ends. I'll just stack these bubble gums once she's out of the store."
jump StoreShiftEndDay03

label StoreTeagan02Day03:
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
            jump StoreParkDay03
    "Sure Miss Cocque, let me help you with these heavy items, it'll be easy for me!":
        jump StoreTeagan05Day03

label StoreTeagan05Day03:
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

label StoreParkDay03:
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
        jump StoreShiftEndDay03
    "I don't know, I don't think I'll have time for that extra job...":
        t "Uh... OK, just think about it... Have a nice evening [name], I'll see you tomorrow at class, 9am sharp!"
        jump StoreShiftEndDay03

label StoreSecondWork01Day03:
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
if (deliveryboy == True):
    fa "Now go and deliver Miss Cocque's groceries if you please [name]."
    p "Sure thing, boss! (anything to get me out of this sordid place)"
    jump TeaganHouse01Day03
else:
    fa "Now let's go and pack some shelves in the front room!"
    p "Sure thing, boss! (anything to get me out of this sordid place)"
    scene storepacking with dissolve
    $ renpy.pause(1.0, hard=True)
    fa "Isn't that fun [name]? Us working together for our parent company \"Seven Square\"!"
    p "(She's fucking nuts. But she's got big tits...)"
    jump StoreShiftEndSecondDay03

label StoreShiftEndSecondDay03:
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
jump HalfPriceDay03

label StoreShiftEndDay03:
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
    jump StoreShiftEnd02Day03
if (catchfrancine == True):
    fa "Here's five dollars for your hard work [name]! I hope you come back again to work here. Goodbye."
    $ money += 5
    p "Yeah, maybe, I'll see..."
    jump StoreShiftEnd02Day03
    
label StoreShiftEnd02Day03:
if (halfprice == True):
    p "Hey, I can buy something half-price remember?"
    fa "Ah yes, silly me for not remembering..."
    jump HalfPriceDay03

label HalfPriceDay03:
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
        jump StoreShiftEnd03Day03
        
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
        jump StoreShiftEnd03Day03

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
        jump StoreShiftEnd03Day03

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
        jump StoreShiftEnd03Day03
    
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
        jump StoreShiftEnd03Day03

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
        jump StoreShiftEnd03Day03
    
    "Nothing actually...":
        jump StoreShiftEnd03Day03
        
label StoreShiftEnd03Day03:
scene store01 with dissolve
fa "That's it, you bought your item, now I have to close the store... Come back anytime to \"Seven Square\", your local shop that's opened from seven till... seven."
jump BurbsDay03
    
label StoreNoDealDay03:
scene store03 with dissolve
fa "That's a pity... Think about it, the job offer will be on all week."
jump StoreClerkDay03

label StoreBuyDay03:
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
        jump StoreClerkDay03

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
        jump StoreClerkDay03

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
        jump StoreClerkDay03

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
        jump StoreClerkDay03
    
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
        jump StoreClerkDay03

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
        jump StoreClerkDay03
    "Nothing actually...":
        jump StoreClerkDay03
        
label TeaganHouse01Day03:
scene teaganhouse01 with dissolve
stop music
play sound "Sounds/debbydoorbell.mp3"
$ renpy.pause(1.0, hard=True)
$ seenteaganhouse = True
p "Mmh... No one's answering the doorbell..."
menu:
    "Try again":
        play sound "Sounds/debbydoorbell.mp3"
        $ renpy.pause(1.0, hard=True)
        p "Nope. I guess I'll just leave her groceries in front of her doorstep. This place is not like New Major City, it should be fine."
        jump BurbsDay03
    "Go round the back of the house":
        jump TeaganHouse02Day03
        
label TeaganHouse02Day03:
scene teaganhouse02 with dissolve
play music "Sounds/gardensound.mp3"
play sound "Sounds/swimming.mp3"
$ renpy.pause(1.0, hard=True)
p "Oh, there she is, that explains why she didn't hear me..."
t "Hello [name], you brought my groceries? How nice of you! Let me get out of the pool and I'll be right with you."
stop sound
scene teaganhouse03 with dissolve
$ renpy.pause(1.0, hard=True)
t "It's so sunny today, I couldn't help but relax a bit in my swimming pool."
p "(Ho-Ho, I can feel my cock twitching... She's giving me an instant boner!)"
scene teaganhouse04 with dissolve
$ renpy.pause(1.0, hard=True)
t "I'll just dr... Ooh."
window hide
$ lust_points[22] +=2
$ score += 2
show lust02:
    xalign 0.35 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
t "Err, dry off, yes, that's what I'll do."
scene teaganhouse05 with dissolve
$ renpy.pause(1.0, hard=True)
p "(Well that sight isn't helping to keep my hardon in check... What an arse! I bet she did it on purpose...)"
t "Could you pass me another towel please [name]? This one's too small..."
p "Sure Miss Cocque... There you are."
t "Thank you, now I think I'm done. Let me show you to the kitchen..."
scene teaganhouse06 with dissolve
$ renpy.pause(1.0, hard=True)
t "Thanks so much for being my grocery delivery boy! Here's five bucks for bringing over all those items. I hope it wasn't too heavy walking all the way up to my house with them?"
$ money += 5
p "I didn't break a sweat, piece of cake for me, Miss Cocque!"
t "Ah ah, you're such a brag [name]! Then again, you DO have the muscles to brag about... (wink)"
t "Now off you go, I won't keep you any longer, I'll see you tomorrow morning for our schooltrip though!"
if (workedseconddaystore == True):
    jump StoreShiftEndSecondDay03
else:
    jump BurbsDay03

label AuntDebbyHouseDay03:
stop music
if (blacktop == True):
    scene debbyentranceblack with dissolve
else:
    scene debbyentrance with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/debbydoorbell.mp3"
p "Maybe I could ask Debby if I could wash her car for her and get a bit of money..."
if (hour >=18):
    scene debbyhouse01 with dissolve
    d "Well, look who came to visit me. What brings you here [name]?"
    $ auntdebbyseen = True
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
        d "That's better... So what brings you here?"
        scene debbyhouse01 with dissolve
    jump AuntDebbyHouseMenuDay03
if (hour <=17):
    p "She doesn't seem to be in at the moment."
    jump BurbsDay03

label AuntDebbyHouseMenuDay03:
menu:
    "I wanted to see you model some more bikinis for me." if (debbybikini == False):
        d "Well, that's bold of you young man!"
        d "But you're in luck, I just received a new swimsuit which I haven't tested yet... Come on in..."
        $ debbybikini03 = True
        jump AuntDebbyInsideDay03
    "I was wondering if your car needed washing?" if (debbycarwashed == False) or (debbycarunwashed == False):
        d "Oh, I see, you want to make a bit of money do ya? Fair enough."
        d "I'll give you five dollars... But I want to be able to watch and you have to be bare-chested...(wink)"
        menu:
            "It's a deal!":
                jump AuntCarWashDay03
            "Five dollars? It will take me at least one hour to wash it... Not interested.":
                d "Your choice mr I'm-too-important-to-wash-a-car-for-five-dollars!..."
                d "Anything else?"
                jump AuntDebbyHouseMenuDay03
    "Nancy needs some...sugar." if (debbysugar == False):
        d "Oh, alright, come on in then."
        $ debbysugar03 = True
        jump AuntDebbyInsideDay03

label AuntDebbyNewBikiniDay03:
d "Where should I model this new bikini for you?"
menu:
    "Why not in your bedroom?":
        d "No, that's my special place. You can't go there ever, you hear me?"
        p "Alright, alright. How about the backyard then?"
        d "Yes, that will do, go and sit outside and wait for me, I'll be back in a minute."
        d "Get down to your underwear, I might need you... to do something for me."
        p "(Well, that's an unusual request... I hope it leads to something...)"
        jump DebbyHouseBikini01Day03
    "The outside light will better reveal every detail of your hot bo...swimsuit.":
        d "Yes, you're right, you are a fine connoisseur. Go and sit outside then, I'll be back in a sec." 
        d "Get down to your underwear, I might need you... to do something for me."
        p "(Well, that's an unusual request... I hope it leads to something...)"
        jump DebbyHouseBikini01Day03

label AuntCarWashDay03:
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
            jump DinnerDay03
        jump AuntDebbyMoneyDay03
    "Stop and sneak inside to get the money anyway":
        $ debbycarunwashed = True
        jump AuntDebbyMoneyDay03
    
label AuntDebbyInsideDay03:
scene debbyhouse02 with dissolve    
$ renpy.pause(1.0, hard=True)
play sound "Sounds/footsteps.mp3"
d "This way to the living room..."
p "Wow, Debby has such a huge house... And such a tight ass..."
jump AuntDebbyLivingRoomDay03

label AuntDebbyLivingRoomDay03:
scene debbyhouse03 with dissolve    
$ renpy.pause(1.0, hard=True)
if (debbysugar03 == True):
    d "I'll go and fetch some sugar from the kitchen. You can wait for me here. But don't touch anything, these sculptures are worth thousands of dollars!"
    p "Sure Debby. I won't move."
    play sound "Sounds/debbydooropenclose.mp3"
    jump DebbySnoopDay03
if (debbybikini03 == True):
    jump AuntDebbyNewBikiniDay03
    
label DebbySnoopDay03:
scene debbysnooping with dissolve    
$ renpy.pause(1.0, hard=True)
menu:
    "Snoop around":
        jump DebbySnoopingDay03
    "Wait patiently for Debby to return":
        jump DebbySugarDay03

label DebbySnoopingDay03:
play music "Sounds/snooping.mp3"
$ d2rolldebby=renpy.random.randint(0, 1)
if (d2rolldebby == 0):
    call screen debbysnoop01Day03
if (d2rolldebby == 1):
    call screen debbysnoop02Day03
$ renpy.pause(1.0, hard=True)
stop music
"You were too slow and didn't find anything. Debby is coming back..."
jump DebbySugarDay03

label FoundAudaciousPassDay03:
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

label DebbySugarDay03:
scene debbyhouse04 with dissolve    
$ renpy.pause(1.0, hard=True)
d "Here you are. I hope your landlady does some nice cakes with it! Tell her to invite me when she's done."
p "Thanks Debby... I'll be sure to let her know..."
$ hour += 1
jump BurbsDay03
    
label DebbyHouseBikini01Day03:
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
jump BurbsDay03

label AuntDebbyMoneyDay03:
stop music
scene debbymoney with dissolve    
$ renpy.pause(1.0, hard=True)
p "Here's the money."
play sound "Sounds/auntviolent.mp3"
p "What's that sound? It seems to be coming from upstairs where Debby's bedroom is..."
menu:
    "Go investigate":
        jump AuntDebbyStairsDay03
    "Take the money and leave":
        $ money += 5
        jump BurbsDay03

label AuntDebbyStairsDay03:
scene debbystairway with dissolve
play sound "Sounds/auntwhip01.mp3"
$ renpy.pause(1.0, hard=True)
p "Jeezus, this sounds violent, I'd better hurry up!"

label AuntDebbyBedroomDay03:
scene debbybedroom01 with dissolve    
play sound "Sounds/auntwhip02.mp3"
$ renpy.pause(1.0, hard=True)
p "WTF? That masked naked guy is brutalizing Debby!"
menu:
    "Leave quietly and take the money on the way out":
        $ money += 5 
        jump BurbsDay03
    "Get involved":
        p "Hey you, stop this immediately or...I swear I'll beat you up!"
        jump AuntDebbyBondage01Day03

label AuntDebbyBondage01Day03:
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
        jump BurbsDay03
    "You deserve a good cock slapping, get on your knees bitch!":
        d "Wh...what?..But..."
        p "You heard me. Remove your mask and ON YOUR KNEES BITCH!"
        d "Y..yes master..."        
        jump DebbyCockSlapDay03
    "OK, I didn't see a thing. I won't say a word. I'll just erase everything from my memory.":
        d "Oh Thank you [name], I owe you big time. Here's your twenty bucks. Now get out of here and don't say a word to anyone!"
        $ money += 20
        jump BurbsDay03

label DebbyCockSlapDay03:
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
        jump BurbsDay03
    "Now I'm gonna cock-slap that tight arse of yours filthy slut!":
        d "Oooh, yes master, I deserve it..."
        jump ArseCockSlapDay03

label ArseCockSlapDay03:
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
d "It's enough for now [name], here's 10 dollars, don't say a word to your landlady and we might do something like that again (wink...)."
menu:
    "Sure, nice doing business with you Debby...":
        $ money += 10
        d "I feel so...cheap...so dirty...I love it, thank you [name]...Just go now..."
        p "I feel like...10 dollars worth apparently. See you another time Debby!"
        if (debbycarunwashed == True):
            $ hour +=1
        jump BurbsDay03
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
        jump BurbsDay03

label HomeDay03:
stop music
scene livingroom01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah, home sweet home..."

if (hour == 17 or hour == 18) and (katephotoplanned == True) and (katephotoshoot == False) and (katephotoshootleft == False):
    p "I think Kate should arrive anytime now for our little photoshoot session... I hope it gets steamy fast..."
    jump KateShoot01Day03  
    
if (hour == 20):
    p "Just in time for dinner..."
    jump DinnerDay03

label Home02Day03:
stop music
scene livingroom01 with dissolve
if (hour == 20):
    p "Time for dinner..."
    jump DinnerDay03

p "What should I do?"
menu:
    "Go to my room":
       jump RyanBedroomDay03
    "Go to the bathroom":
        jump BathRoomDay03
    "Go to Nancy's room" if (momroomseen03 == False):
        jump MomRoomDay03
    "Go to the swimming pool" if (locswimmingpool == False):
        jump SwimmingPoolDay03
    "Leave the house":
        jump BurbsDay03

label SwimmingPoolDay03:
$ locswimmingpool = True
if (hour <= 18):
    scene poolempty with dissolve
    play music "Sounds/gardensound.mp3"
    $ renpy.pause(1.0, hard=True)
    p "There's no one around, I can't even, like, perv on Nancy or sis in a bikini right now. SAD."
    $ locswimmingpool = False
    jump Home02Day03
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
    jump DinnerDay03

label RyanBedroomDay03:
stop music
$ locroom = True
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
if (hour >= 20):
    $ hour = 20
    p "Oh, it's time for dinner, I'd better hurry downstairs..."
    jump DinnerDay03
if (hour == 17 or hour == 18) and (katephotoplanned == True) and (katephotoshoot == False) and (katephotoshootleft == False):
    p "I think Kate should arrive anytime now for our little photoshoot session... I hope it gets steamy fast..."
    jump KateShoot01Day03  

p "What to do, what to do..."
menu:
    "Turn the computer on":
        jump ComputerDay03
    "Do some heavy bodybuilding (+2hrs)" if (hour <= 18):
        if (workout == True):
            "You already trained today."
            jump RyanBedroomDay03
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
            jump RyanBedroomDay03        
    "Admire my own body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump RyanBedroomDay03
    "Go the living room":
        jump Home02Day03
    "Go to the bathroom" if (showerseen03 == False):
        jump BathRoomDay03
    "Go to Nancy's room" if (momroomseen03 == False):
        jump MomRoomDay03
    "Read the book Laura gave you (+1hr)" if (book == True) and (bookread == False):
        jump RyanReadingDay03

label RyanReadingDay03:
scene ryanreading with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump RyanBedroomDay03

label ComputerDay03:
scene ryancomputerday with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label Computer02Day03:
scene ryancomputerday
menu:
    "Check the map":
        jump MapDay03
    "Check the stats":
        jump StatsDay03
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump Computer02Day03
    "Learn how to use the pendulum" if (pendulum == True) and (pendulumactive ==False):
        jump CompPendulumDay03
    "Play a smutty game (+1hr)":
        jump CompGameDay03
    "Turn the computer off":
        jump RyanBedroomDay03

label CompPendulumDay03:
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump Computer02Day03

label MapDay03:
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
jump Computer02Day03

label StatsDay03:
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
jump Computer02Day03

label CompGameDay03:
scene ryancomputergameday
$ renpy.pause(1.0, hard=True)
p "This game is tough. My fingers hurt like hell from so much clicking..."
$ hour += 1
jump Computer02Day03

label MomRoomDay03:
scene nancybedroomday with dissolve
$ renpy.pause(1.0, hard=True)
$ momroomseen03 = True
p "Nancy's room is so clean and tidy. Not like mine."
menu:
    "Snoop around" if (dildo == False):
        jump MomBedroomSnoopDay03  
    "Go back to my room":
        jump RyanBedroomDay03
    "Put the dildo back in its drawer" if (dildo == True):
        show dildo
        show square
        play sound "Sounds/lost.mp3"
        "You relinquish a giant black dildo. Yes, that's right, \"relinquish\". Look it up in the dictionary."
        hide square
        hide dildo
        $ dildo = False
        jump RyanBedroomDay03

label MomBedroomSnoopDay03:
p "There might be an interesting item hidden somewhere... Time to snoop around..."
p "But I have a limited amount of time to look for it, Nancy might come back from work anytime for all I know."
play music "Sounds/snooping.mp3"
call screen mombedroomsnoopDay03
stop music
"You were too slow and didn't find anything."
jump RyanBedroomDay03

label FoundDildoDay03:
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
jump RyanBedroomDay03

label BathRoomDay03:
stop music
if (hour <= 17):
    jump EmptyBathRoomDay03
if (hour == 18) or (hour == 19):
    jump MomShowerDay03

label EmptyBathRoomDay03:
scene bathroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "No one is around right now, I could take a shower if I wanted to."
menu:
    "Take a shower":
        jump ShowerDay03
    "Leave":
        jump RyanBedroomDay03

label ShowerDay03:
scene shower with dissolve
stop music
play music "Sounds/shower.mp3"
$ renpy.pause(1.0, hard=True)
p "That's nice and relaxing..."
if (stamina <= 4) and (showerseen03 == False):
    window hide
    $ stamina += 1
    show stamina01:
        xalign 0.4 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide stamina01
$ showerseen03 = True
jump RyanBedroomDay03

label MomShowerDay03:
play music "Sounds/shower.mp3"
$ locroom = False
scene bathroomdoorclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "Someone's taking a shower..."
menu:
    "Use lubricant on the door hinges" if (wd69 == True) and (squeakfixed == False):
        "The door should not squeak anymore."
        $ squeakfixed = True
        jump MomShowerDay03        
    "Have a peek":
        jump MomPeekBathroomDay03
    "Leave":
        jump RyanBedroomDay03

label MomPeekBathroomDay03:
if (squeakfixed == False):
    play sound "Sounds/doorsqueak.mp3"
    scene bathroomdooropen with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Shit, the door is squeaking..."
    m "I'm in the shower sweetie, don't get in!"
    p "Ah, sorry Nancy...I'm leaving..."
    p "Damn, I should try and find a way of stopping that door from squeaking if I want to spy on Nancy or Nikki in the shower like every other MC..."
    jump RyanBedroomDay03
if (squeakfixed == True):
    scene nancyshower01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Cool, she didn't hear me come in, I can see her naked in the shower now..."
    p "Fuck yeah, look at those huge titties... How I would love to rub my pud between them..."
menu:
        "Watch a little longer...":
            jump MomShower02Day03
        "Leave before she turns round and catches me":
            jump RyanBedroomDay03
    
label MomShower02Day03:
if (momshowerpeep == False):
    $ peeping += 1
$ momshowerpeep = True
scene nancyshower02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, her arse was made for fucking a great big cock. MY giant cock!"
menu:
        "Watch a little longer still...":
            jump MomShower03Day03
        "Leave before she turns round and catches me":
            jump RyanBedroomDay03
 
label MomShower03Day03:
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
jump RyanBedroomDay03

label KateShoot01Day03:
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
    $ katephotoshootleft = True
    scene livingroom01 with dissolve
    $ renpy.pause(1.0, hard=True)
    jump Home02Day03

if (camera == True):
    p "Hi Kate, alright, everything is set up and we are ready to roll...the roll."
    scene katehouse03 with dissolve
    $ renpy.pause(1.0, hard=True)
    k "Oooh, I'm so excited! I'm gonna get to see myself in a bikini!"
    p "Yeah, that's right, the wonders of modern technology... Why don't you change into your first outfit and come by the pool, I'll be waiting for you."
    jump KateShoot02Day03

label KateShoot02Day03:
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
$ katephotoshoot = True

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
    jump RyanBedroomDay03

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
        jump KateBehindDay03
    "Push her down and place the head near her pussy":
        jump KatePussyDay03
    "Push her down and stick your rod between her tits":
        jump KateTitsDay03

label KateBehindDay03:
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
label KateBehindDay03b:
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
        jump KateBehindDay03b
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
        jump KatePussyDay03
    "Push her down and stick your rod between her tits" if (katetits == False):
        jump KateTitsDay03
    "Lift her up and fuck her sweet hole" if (katelegs == True) and (katepussy == True) and (katetits == True):
        jump KateLiftDay03

label KatePussyDay03:
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
label KatePussyDay03b:
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
        jump KatePussyDay03b
    "Stick your pud between her legs from behind" if (katelegs == False):
        jump KateBehindDay03
    "Push her down and stick your rod between her tits" if (katetits == False):
        jump KateTitsDay03
    "Lift her up and fuck her sweet hole" if (katelegs == True) and (katepussy == True) and (katetits == True):
        jump KateLiftDay03

label KateTitsDay03:
scene katepool20 with dissolve
$ katetits = True
$ renpy.pause(1.0, hard=True)
p "I think those big jugs of yours are a perfect match for my massive erection!"
k "Uuhh, oooh, you think so?"
p "For sure, I'm dripping precum all over the place cos they make me so horny!"
k "Oooh, I'm so glad you like them..."
menu:
    "Stick your pud between her legs from behind" if (katelegs == False):
        jump KateBehindDay03
    "Push her down and place the head near her pussy" if (katepussy == False):
        jump KatePussyDay03
    "Lift her up and fuck her sweet hole" if (katelegs == True) and (katepussy == True) and (katetits == True):
        jump KateLiftDay03

label KateLiftDay03:
scene katepool17 with dissolve
$ renpy.pause(1.0, hard=True)
k "Uuhh, what? You're lifting me up on your COCK? God, it's ssooo powerful!"
p "Ready for a wild ride Kate?"

stop music
play music "Sounds/kateslow.mp3"
show katefuckslow
show faster
call screen katefuckscreen03
screen katefuckscreen03:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("KateFuckFastDay03")

label KateFuckFastDay03:
stop movie
hide faster
play music "Sounds/kate04.mp3"
show katefuckfast
show cum
call screen katefuckscreen03b
screen katefuckscreen03b:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("KateFuckCumDay03")

label KateFuckCumDay03:
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
$ fuckedschoolgirlday03 = True
$ hour += 1

if (hour == 18):
    k "We should take a dip in the pool to clean ourselves of all this cum you've unloaded everywhere! Hee hee!"
    p "I'd better clean the deck, you go in the pool."
    k "Oooh, OK."
    scene katepoolend with dissolve
    $ renpy.pause(1.0, hard=True)
    k "The pool water is so great..."
    p "(It's so nice to see poor Kate so happy. Especially after she got detention again today.)"
    k "I'm clean now, I'd better get going. See you tomorrow [name]!"
    p "Yep, see you at school for our trip to Bigdong Falls Kate!"
    jump RyanBedroomDay03    
if (hour == 19):
    scene katepoolcum03 with dissolve
    $ renpy.pause(1.0, hard=True)
    m "What on earth is going on here? [name], who is this girl you're fucking in MY house?"
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
            jump RyanBedroomDay03
        "Ah... Let me introduce you to my new classmate Kate. Kate, my landlady and her daughter.":
            m "Who the hell do you think you're kidding? Get dressed and get this \"Kate\" girl out of here, you are GROUNDED this evening [name]!"
            $ ryangrounded = True
            jump RyanBedroomDay03
        "Well, a man's got to do what a man's got to do, right?":
            m "Not HERE in our garden! Now get dressed both of you, I don't want to see  such a lewd display in MY house any longer!"
            jump RyanBedroomDay03

label Beach01Day03:
stop music
play music "Sounds/oceanwaves.mp3"
scene beach with dissolve
$ renpy.pause(1.0, hard=True)
p "Ah! Here's Tini-Wini-Bikini beach, as sunny as always... I should probably head for the beach bar first..."
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_43
    $ lustaddedB = 1
    call Challenger from _call_Challenger_44
    $ challengercalls += 2

label BeachBar01c:
stop music
play music "Sounds/tropicalmusic.mp3"
scene beachbar01 with dissolve
$ renpy.pause(1.0, hard=True)
bb "Aloha, welcome to Tini-Wini-Bikini Beach bar! Again..."
label BeachBar02c:
scene beachbar01
menu:
    "Chat with her":
        jump ChatBeachBarDay03    
    "Leave":
        jump ExploreBeachDay03

label ChatBeachBarDay03:
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
    
p "I'm drowning in your big blue eyes. I need the kiss of life."
scene beachbar03 with dissolve
bb "Well Mister Charmer, maybe you should join the lifeguard corps, that'll stop you from drowning..."
bb "The lifeguard tower is just behind you..."
$ lifeguarddiscovered = True
show addedlocation:
    xalign 0.3 yalign 0.3
    linear 1.0 yalign 0.1
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide addedlocation
jump BeachBar02c

label ExploreBeachDay03:
stop music
play music "Sounds/oceanwaves.mp3"
p "Hum... Where should I go?"
menu:
    "Go to the beach bar":
        jump BeachBar01c
    "Walk along the beach" if (walkbeachseen == False) or (beachswimday03 == False):
        jump BeachWalkDay03
    "Go to Randy Beach" if ((discoverrandybeach == True) and (randybeachseen03 == False)):
        jump RandyBeachDay03
    "Go to the lifeguard tower" if (lifeguarddiscovered == True):
        jump Lifeguard01Day03
    "Take the Bus to town":
        jump BusBeachTownDay03
    "Take the Bus back home":
        jump BusBeachHomeDay03

label BusBeachTownDay03:
scene beach with dissolve
$ renpy.pause(1.0, hard=True)   
p "Bye bye Tini-Wini-Bikini beach!"
p "Ah, here's the bus going to town..."
$ hour += 1
jump DowntownDay03
    
label BusBeachHomeDay03:
scene beach with dissolve
$ renpy.pause(1.0, hard=True)
p "Bye bye Tini-Wini-Bikini beach!"
p "Ah, here's the bus going back home..."
$ hour += 1
jump BurbsDay03

label BeachWalkDay03:
$ walkbeachseen = True
if (boughthallebikini == True):
    jump HalleBeachDay03

else:
    scene beachempty with dissolve
    $ renpy.pause(1.0, hard=True)  
    "This secluded part of the beach is empty... I could always go for a swim I guess."
    menu:
        "Go for a swim":
            jump BeachSwimDay03
        "Don't go for a swim":
            jump ExploreBeachDay03

label BeachSwimDay03:
$ beachswimday03 = True
play music "Sounds/randybeachsound.mp3"
scene beachswim01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I can see some coral reefs below. Let's dive and have a look!"        
scene beachswim02 with dissolve
play music "Sounds/underwater.mp3"
$ renpy.pause(1.0, hard=True)
p "What the hell is that thing swimming towards me?"
jump Mermaid01Day03

label HalleBeachDay03:
$ walkbeachseen = True 
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
        jump Underwater01bDay03
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
        jump Underwater01bDay03

label Underwater01bDay03:
scene hallebeach03 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Come on, this way! You'll see, it's gonna be ssoo much fun!"

label Underwater02Day03:
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
        jump Mermaid01Day03
    "Sneak under her":
        scene underwater03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Bingo, she's smiling at me... I wonder what a kiss underwater feels like..."
        scene underwater03b with dissolve
        p "What's wrong, she seems to be scared of something..."
        scene underwater04 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "She's darting off... OMG, what the fuck is that?..."
        jump Mermaid01Day03

label Mermaid01Day03:
scene mermaid01 with dissolve
$ renpy.pause(1.0, hard=True)
p "This mermaid is captivating... OK, she has a fish tail and all that but... Mmmh, those tits..."
scene mermaid02 with dissolve
$ renpy.pause(1.0, hard=True)
p "She seems to be signalling me to follow her..."
menu:
    "Follow her":
        jump Mermaid02Day03
    "Get the hell out of here and re-join Halle" if (beachswimday03 == False):
        $ underwaterleft = True
        jump Underwater03Day03
    "Get the hell out of here" if (beachswimday03 == True):
        scene beachswim01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Phew, that was close!I'm still shaking. Better go back to the beach..." 
        scene beachempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ExploreBeachDay03

label Mermaid02Day03:
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
        jump Mermaid03Day03
    "Get the hell out of here and re-join Halle" if (beachswimday03 == False):
        jump Underwater03Day03
    "Get the hell out of here" if (beachswimday03 == True):
        scene beachswim01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Phew, that was close!I'm still shaking. Better go back to the beach..." 
        scene beachempty with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ExploreBeachDay03
        
label Mermaid03Day03:
scene mermaid08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Here we go, it's tough to aim underwater but once I'm in, it shouldn't move too much..."
show mermaidfuckslow
show faster
call screen mermaidfuckslow
screen mermaidfuckslow:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MermaidFuckFast")
label MermaidFuckFast:
hide faster
show mermaidfuckfast
show cum
call screen mermaidfuckfast
screen mermaidfuckfast:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MermaidFuckCum")
label MermaidFuckCum:
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
if (beachswimday03 == False):
    jump Underwater03Day03
if (beachswimday03 == True):
    scene beachswim01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "The sea is getting rough. I'd better go back to the beach..." 
    scene beachempty with dissolve
    $ renpy.pause(1.0, hard=True)
    jump ExploreBeachDay03

label Underwater03Day03:
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
            jump HalleBackBeach01Day03
        else:
            scene hallesea04 with dissolve
            $ renpy.pause(1.0, hard=True)
            ha "Ha ha! You boys really are all the same... A pair of tits, that's all that counts!"
            ha "Let's get back to the beach, the sea is getting rough..."
            p "Great idea..."
            jump HalleBackBeach01Day03
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
        jump HalleBackBeach01Day03        
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
        jump HalleBackBeach01Day03
        
label HalleBackBeach01Day03:
stop music
play music "Sounds/oceanwaves.mp3"
scene hallebeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "Well, that was fun, apart from this vile creature... I think I'd better head back to the university, I need to study."
menu:
    "Okay, I hope to see you again Halle...":
        ha "You will, don't worry... If you come back to the beach, I'll be here..."
        jump ExploreBeachDay03
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True) and (lust_points[9] >=8):
        jump HallePendulumDay03
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
        jump ExploreBeachDay03

label HallePendulumDay03:
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
    jump HalleFuckDay03
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
    jump HalleFuckDay03   

label HalleFuckDay03:
scene hallebeach04 with dissolve
$ renpy.pause(1.0, hard=True)
ha "I think I changed my mind... I would rather spend some \"quality\" time with you after all..."
ha "And by \"quality\", I mean some hot, steamy SEX!"
p "Alright, I'm in baby!"
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
label HallePrefuckDay03:
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
        jump HallePrefuckDay03
    "Spread her legs and fuck her pussy slowly":
        ha "You want to fuck me some more stud? Yeah, I 'm ready for your great big horsecock, come and ram that monstercock home!"
        jump HalleFuckMovie

label HalleFuckMovie:
stop music
play sound "Sounds/oceanwaves.mp3"
play music "Sounds/hallefuckslow.mp3"
show hallefuckslow
show faster
call screen hallefuckslow
screen hallefuckslow:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("HalleFuckFast")
label HalleFuckFast:
show hallefuckfast
hide faster
play music "Sounds/hallefuckfast.mp3"
show cum
call screen hallefuckfast
screen hallefuckfast:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("HalleFuckCum")

label HalleFuckCum:
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
$ hour +=1
$ hallefucked = True
if (hallejosewin == False):
    p "(She didn't notice I took a picture of us... Now I'll send it to José)."
    $ hallewin = True
jump ExploreBeachDay03

label Lifeguard01Day03:
stop music
scene tower01 with dissolve
$ renpy.pause(1.0, hard=True)
if (hour == 16) and (wonarmwrestling == True):
    pa "Hi again [name]. So, you wanna start working today?"
    menu:
        "Sure, I'm in!":
            jump LifeGuardWorkDay03
        "Maybe another day...":
            pa "Fine, your choice, hope to see you back here at 4pm another day..."
            jump ExploreBeachDay03
if (hour >=17) and (wonarmwrestling == True):
    pa "It's a bit late to start a workshift. We're almost done here. Come back tomorrow at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay03
if (hour <=15) and (wonarmwrestling == True):
    pa "It's a bit early to start a workshift. Come back at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay03

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
        jump ArmWrestlingDay03

    "This guy looks too strong, bail out":
        p "Err... Maybe another time... I need to...train."
        scene tower05 with dissolve
        $ renpy.pause(1.0, hard=True)
        mb "Oooooh! Little boy scared... Once again, Mitch Bigcannon is the winner! Choo-chooo!"
        $ lifeguardbail = True
        jump ExploreBeachDay03


label ArmWrestlingDay03:
$ clicked = True
$ points=20
if (strength <= 7):
    jump WrestlingStrength07Day03
if (strength == 8):
    jump WrestlingStrength08Day03
if (strength >= 9):
    jump WrestlingStrength09Day03

label WrestlingStrength07Day03:
$ plus=0
$ max_point=40
scene arm01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Ready guys? On your marks...set.. and go!"
play music "Sounds/grunt.mp3"
scene arm01b with dissolve
centered "Click on the hand!{w=1}{nw}"
call screen clicker7
screen clicker7:
    modal True
    timer .2 repeat True action [If(points <= 0, true=Jump("Lostwrestling"), false=SetVariable("points", points - 1))]
    button:
        xpos .35
        ypos .3
        xysize(200, 200)
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("Wonwrestling"), false=SetVariable("points", points + plus))]
    bar value StaticValue(points, max_point):
        xalign 0.45 yalign 0.0
        xmaximum 400 
        ymaximum 15

label WrestlingStrength08Day03:
$ plus=1
$ max_point=40
scene arm01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Ready guys? On your marks...set.. and go!"
play music "Sounds/grunt.mp3"
scene arm01b with dissolve
centered "Click on the hand!{w=1}{nw}"
call screen clicker8
screen clicker8:
    modal True
    timer .3 repeat True action [If(points <= 0, true=Jump("Lostwrestling"), false=SetVariable("points", points - plus))]
    button:
        xpos .35
        ypos .3
        xysize(200, 200)
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("Wonwrestling"), false=SetVariable("points", points + plus))]
    bar value StaticValue(points, max_point):
        xalign 0.45 yalign 0.0
        xmaximum 400 
        ymaximum 15

label WrestlingStrength09Day03:
$ plus=2
$ max_point=40
scene arm01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Ready guys? On your marks...set.. and go!"
play music "Sounds/grunt.mp3"
scene arm01b with dissolve
centered "Click on the hand!{w=1}{nw}"
call screen clicker9
screen clicker9:
    modal True
    timer .5 repeat True action [If(points <= 0, true=Jump("Lostwrestling"), false=SetVariable("points", points - plus))]
    button:
        xpos .35
        ypos .3
        xysize(200, 200)
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("Wonwrestling"), false=SetVariable("points", points + plus))]
    bar value StaticValue(points, max_point):
        xalign 0.45 yalign 0.0
        xmaximum 400 
        ymaximum 15

label Lostwrestling:
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
jump ExploreBeachDay03

label Wonwrestling:
stop music
play music "Sounds/oceanwaves.mp3"
play sound "Sounds/thump.mp3"
scene armwon with dissolve
$ renpy.pause(1.0, hard=True)
p "I win JERK! I'm da man, I'm DA MAN!"
scene tower06 with dissolve
$ renpy.pause(1.0, hard=True)
if  (strength >=9):
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
            jump LifeGuardWorkDay03
        "Maybe another day...":
            pa "Fine, your choice, hope to see you back here at 4pm another day..."
            jump ExploreBeachDay03
if (hour >=17) and (wonarmwrestling == True):
    pa "It's a bit late to start a workshift. We're almost done here. Come back tomorrow at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay03
if (hour <=15) and (wonarmwrestling == True):
    pa "It's a bit early to start a workshift. Come back at 4pm if you want to make a bit of money as a lifeguard."
    jump ExploreBeachDay03

label LifeGuardWorkDay03:
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
        jump LifeGuardWork02Day03
    "Oh yeah, I'll get one too!":
        pa "No you won't, you're too young. Your turn on the binoculars anyway."
        jump LifeGuardWork02Day03
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
        jump LifeGuardWork02Day03    

label LifeGuardWork02Day03:
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
        jump LifeguardSmall01Day03
    "The tall woman on the right. (Sandy)":
        jump LifeguardsBig01Day03


label LifeguardSmall01Day03:
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
        jump TowerEndDay03
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
        jump TowerEndDay03
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
        jump TowerEndDay03

label LifeguardsBig01Day03:
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
        jump TowerEndDay03
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
        jump TowerEndDay03

label TowerEndDay03:
scene tower01 with dissolve
stop music
play music "Sounds/oceanwaves.mp3"
$ renpy.pause(1.0, hard=True)
pa "Ok, you did well for your first day [name]. It's almost 6pm so I'll pay you now cos... we're heading for the beach bar."
$ money += 20
pa "Use your remaining time to clean up this filthy place!"
scene towerend with dissolve
$ renpy.pause(1.0, hard=True)
p "More goddam cleaning to do..."
$ hour += 1
label TowerEndChoiceDay03:
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
        jump TowerEndChoiceDay03     
    "Go and meet Pamela at the beach bar":
        jump BeachPamela01Day03 
    "Leave":
        jump ExploreBeachDay03
                
label BeachPamela01Day03:
stop music
play music "Sounds/tropicalmusic.mp3"
scene beachbarpamela01 with dissolve
$ renpy.pause(1.0, hard=True)
mb "...And then, the medics had to check her heart and I got to see her huge boobs, he he..."
pa "Ha ha! You're such a (hips)... perv Mitch!"
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
        jump ExploreBeachDay03
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
        jump ExploreBeachDay03
    "Talk to Pamela about working some more as a lifeguard":
        scene beachbarpamela02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "Yeah, I guess we could use your help some more. You can come back anytime to work for us..."
        mb "Humpf..."
        jump ExploreBeachDay03

label RandyBeachDay03:
stop music
scene randybeach01 with dissolve
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
$ randybeachseen03 = True
if (randybeachseen == True) or (randybeachseen02 == True):
    p "Finally back here again. I'd better take my speedos off."
else:
    p "I guess that's it. I'd better take my speedos off."
$ randybeachseen = True
window hide
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)

label RandyBeachDay03b:
p "I see three parasols but I can't see the people behind them...Which one should I go to?"
menu:
    "Go to the closest red parasol on the right" if (seenparasolc01 == False):
        jump RandyBeachParasolc01
    "Go to the middle orange parasol" if (seenparasolc02 == False):
        jump RandyBeachParasolc02
    "Go to the furthest red parasol on the left" if (seenparasolc03== False):
        jump RandyBeachParasolc03
    "Leave Randy Beach":
        if (seenparasolc03 == True):
            $ hour += 1
        jump ExploreBeachDay03

label RandyBeachParasolc01:
$ seenparasolc01 = True
scene baba01
show randybeachparasol01
$ renpy.pause(2.0, hard=True)
p "Just a leg and an arm... This means a pussy not too far away..."
window hide
hide randybeachparasol01 with moveoutright
$ renpy.pause(1.0, hard=True)
p "Wow, now that's what I call a muscular chick... She must be like 7ft tall or something too... Almost scary."
scene baba02 with dissolve
$ renpy.pause(1.0, hard=True)
ba "Who's disturbing Baba?"
p "WHAT THE FUCK? Jeezus f*cking Christ, she has a giant dick that would put mine to shame! Now THAT is scary."
ba "Baba is horny. You horny too?"
p "NOOOO! I'm not horny at all with Baba, RUN, RUN FOR YOUR LIFE!"
jump Parasol01cout

label Parasol01cout:
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeachDay03b

label RandyBeachParasolc02:
$ seenparasolc02 = True
scene fatguyparasol01
show randybeachparasol02
$ renpy.pause(2.0, hard=True)
p "Please God, make it so it's not that old hag hiding behind this parasol this time..."
window hide
hide randybeachparasol02 with moveoutleft
$ renpy.pause(1.0, hard=True)
p "Oh no! It's that fat ugly cuckolding guy from all those other games!"
p "Well, at least he has a tiny wiener, so he won't be forcing me to watch him fuck Nancy or sis anytime soon..."
scene fatguyparasol02 with dissolve
$ renpy.pause(1.0, hard=True)
om "Well maybe I will, maybe I will..."
p "No fucking way, I'll carve you up like a squealing pig if you get anywhere near them you mothafucker!"
scene fatguyparasol03 with dissolve
$ renpy.pause(1.0, hard=True)
om "Calm down boy... If I'm not mistaken, you're an aspiring \"motherfucker\" yourself..."
$ eyesore += 1
jump Parasol02cout

label Parasol02cout:
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeachDay03b
 
label RandyBeachParasolc03:
$ seenparasolc03 = True
scene chiyorandy01
show randybeachparasol03
$ renpy.pause(1.0, hard=True)
p "Ah, something nice it seems..."
window hide
hide randybeachparasol03 with moveoutright
$ renpy.pause(1.0, hard=True)
if (chiyoseen == True):
    p "It's that teasing Asian lady I met the other day sunbathing topless... Today, she's sunbathing in the nude."
    scene chiyorandy02 with dissolve
    $ renpy.pause(1.0, hard=True)
    cy "Oh, you again big boy... This time, you can't tell me off for not wearing a top! Hee hee..."
    cy "Don't you know it's rude to sneak on naked ladies like that?"
else:
    p "It's a nice Asian lady with large firm breasts sunbathing in the nude... Now that's what I come to see on Randy Beach!"
    scene chiyorandy02 with dissolve
    $ renpy.pause(1.0, hard=True)
    cy "Oh, hello there boy. Don't you know it's rude to sneak on naked ladies like that?"
menu:
    "Sorry, I didn't mean to intrude or anything...":
        cy "Well, it's too late, you've already intruded... But now that you're here, you might as well stay...I was about to put some sunblock on..."
        jump RandyBeachChiyoDay03
    "I'm the suncream guy. Best hands on the island to protect you from nasty UVs.":
        cy "Oh, is that so Mr suncream guy? Well, I didn't ask for your services..."
        if (lust_points[3] >= 1):
            $ lust_points[3] -= 1
            $ score -= 1
            show lustminus01:
                xalign 0.1 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
        if (lust_points[3] == 0):
            pass
        cy "But you're right, I should put some sunblock on..."
        jump RandyBeachChiyoDay03
    "Come on, you were asking for it, you were barely hiding behind that parasol...":
        cy "What if I were? I can tease all I want... It's the boys that get teased that have themselves to blame.... hee hee..."
        $ lust_points[3] += 1
        $ score += 1
        show lust01:
            xalign 0.1 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01

label RandyBeachChiyoDay03:
scene chiyorandy03 with dissolve
$ renpy.pause(1.0, hard=True)
cy "See how this cream glistens on my skin? Do you think I put enough on or not?"
menu:
    "Yeah, but not on your back. You might catch a sunstroke.":
        cy "But I can't reach my back... Maybe you get to be useful after all... (wink)"
        jump ChiyoBeachBack01Day03
    "No, your tits are so huge you need the whole bottle.":
        cy "Oh, you think so? You think I should rub my breasts more in front of a naked boy sporting a huge hardon?"
        $ lust_points[3] += 1
        $ score += 1
        show lust01:
            xalign 0.4 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump ChiyoBeachFront01Day03

label ChiyoBeachBack01Day03:
scene chiyorandy04 with dissolve
$ renpy.pause(1.0, hard=True)
cy "Yes, that's nice, rub it in all over my back you naughty boy... And now move to my arse..."
scene chiyorandy05 with dissolve
$ renpy.pause(1.0, hard=True)
cy "Mmh, I like your strong hands..."
$ lust_points[3] += 1
$ score += 1
show lust01:
    xalign 0.5 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
menu:
    "Stick a finger in her anus":
        scene chiyorandy06 with dissolve
        $ renpy.pause(1.0, hard=True)
        cy "What?... No, naughty boy!"
        $ lust_points[3] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.4 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        cy "That's enough, I'll take it from there. You can go now, hee hee..."
        jump Parasol03cout
    "Rub the cream on her arse with your cock":
        scene chiyorandy07 with dissolve
        $ renpy.pause(1.0, hard=True)
        scene chiyorandy08 with dissolve
        $ renpy.pause(0.3, hard=True)
        scene chiyorandy07 with dissolve
        $ renpy.pause(0.3, hard=True)
        scene chiyorandy08 with dissolve
        $ renpy.pause(0.3, hard=True)
        scene chiyorandy07 with dissolve
        $ renpy.pause(0.3, hard=True)
        scene chiyorandy08 with dissolve
        $ renpy.pause(0.3, hard=True)
        scene chiyorandy07 with dissolve
        $ renpy.pause(0.3, hard=True)
        scene chiyorandy08 with dissolve
        $ renpy.pause(0.3, hard=True)
        scene chiyorandy07 with dissolve
        $ renpy.pause(0.3, hard=True)
        cy "What's this I feel on my back? Are you being a naughty boy and using your great big horsecock to rub my back instead of your hands? You're such a filthy boy..."
        $ lust_points[3] += 1
        $ score += 1
        show lust01:
            xalign 0.3 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        cy "I'll finish putting more cream on my huge titties now..."
        jump ChiyoBeachFront01Day03
    
label ChiyoBeachFront01Day03:
scene chiyorandy03b with dissolve
$ renpy.pause(1.0, hard=True)
cy "Like that, is that enough glistening cream covering my huge tits for you horny boy?"
p "Fuck yeah, now I'm sporting a massive hardon..."
cy "Yeah, I can see that... It sure looks yummy..."
scene chiyorandy09 with dissolve
$ renpy.pause(1.0, hard=True)
cy "See how wet my pussy is for that donkey dick? Let me rub it for you..."
play sound "Sounds/clitrub.mp3"
$ renpy.pause(8.0, hard=True)
$ lust_points[3] += 1
$ score += 1
show lust01:
    xalign 0.3 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
cy "Mmh, that was good. Oh well, I got off, so now you can go, you're useless to me. Hee hee..."
p "What? You can't leave me like that!"
cy "Of course I can. You'll just have to jerk off somewhere else naughty boy..."
p "AAARGGH! Such a tease!"
jump Parasol03cout

label Parasol03cout:
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeachDay03b

label DowntownDay03:
stop music
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"
$ renpy.pause(1.0, hard=True)
p "The bus left me right in front of the main downtown plaza."

if (hour >= 19):
    p "It's getting late, I should really take the bus and get home now."
    jump BusDowntownHomeDay03
else:
    jump DowntownChoiceDay03b

label BusDowntownHomeDay03:
p "Ah, here's the bus heading to the Burbs, I'd better take it..."
$ hour += 1
jump BurbsDay03

label DowntownChoiceDay03b:
scene downtown01 with dissolve
play music "Sounds/downtown.mp3"
if (challengercalls <= 8):
    $ lustaddedB = 2
    call Challenger from _call_Challenger_38
    $ lustaddedB = 1
    call Challenger from _call_Challenger_39
    $ lustaddedB = 1
    call Challenger from _call_Challenger_40
    $ challengercalls += 2

if (hour >= 19):
    p "It's getting late, I should really take the bus and get home now."
    jump BusDowntownHomeDay03

p "Where should I go?"
menu:
    "Go to Audacious HQ" if (discoveraudacious == True):
        jump AudaciousHQDay03
    "Go shopping":
        jump ShopDay03
    "Go to the massage parlour" if (discovermassage == True) and (parlourseen03 == False):
        jump Parlour01Day03
    "Take the bus home":
        jump BusDowntownHomeDay03
    "Take the bus to the beach" if (hour <= 17):
        jump BusDowntownBeachDay03
    "Go to the downtown gym" if (discovergym == True):
        jump Gym01Day03
    "Put some posters up for Miss Titsworthy's campaign (+1hr)" if (principaldeal == True):
        jump PosterDay03

label PosterDay03:
scene downtownposter with dissolve
$ renpy.pause(1.0, hard=True)
$ hour += 1
p "That's done. I almost feel ashamed, this slogan is so cheesy..."
# slogan is: Simply the Breasts
$ posterup = True
jump DowntownChoiceDay03b

label BusDowntownBeachDay03:
p "Ah, here's the bus heading for the beach, I'd better take it..."
$ hour += 1
jump Beach01Day03

label AudaciousHQDay03:
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
            jump AudaciousOffice01Day03

        "Let me through, my fake aunt is the CEO of this company.":
            hide security01
            show security02
            se "And I'm the pope's daughter. Get out of here kid."
            $ audacioustried = True
            jump DowntownChoiceDay03b

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
                if (blacktop == True):
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
                jump DowntownChoiceDay03b

if (audacioustried == True):
    p "I already tried getting into this building today. And I failed miserably. I should probably leave."
    jump DowntownChoiceDay03b

label ShopDay03:
if (evictedfromshop == True):
    "You are banned from entering this boutique until tomorrow. Bad boy. VERY bad boy."
    jump DowntownChoiceDay03b
if (shoppingseen03 == True):
    "You already went shopping today. Looks like you might be a shopaholic..."
    jump DowntownChoiceDay03b
else:
    stop music
    scene shop with dissolve
    play music "Sounds/shopmusic.mp3"
    $ renpy.pause(1.0, hard=True)
    p "This boutique looks very expensive..."
    p "There's a nice-looking clerk standing behind the counter and one customer looking at a skimpy swimsuit..."
    jump Shop01Day03

label Shop01Day03:
$ shoppingseen03 = True
scene shop with dissolve
$ renpy.pause(1.0, hard=True)

label Shop01Day03b:
menu:
    "Go talk to the clerk":
        jump ShopClerkDay03
    "Go talk to the customer":
        jump ShopCustomerDay03
    "Leave":
        stop music
        jump DowntownChoiceDay03b

label ShopClerkDay03:
scene shop01 with dissolve
sc "How may I help you?"
menu:
    "Talk to her":
        jump ShopTalkDay03
    "Buy something":
        jump ShopBuyDay03   
    "Leave the counter":
        jump Shop01Day03

label ShopTalkDay03:
menu:
    "You know what would look good on you? Me.":
        scene shop03
        sc "Mmh, lemme think... Yes, it's the worst pick-up line ever."
        jump ShopClerkDay03
    "What's the word on the street downtown?":
        if (downtowntipgiven == True):
            sc "I already gave you a tip today. Stop pestering me."
            jump ShopClerkDay03
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
            jump ShopClerkDay03
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
            jump ShopClerkDay03

label ShopBuyDay03:
menu:
    "Buy swimsuit for customer (40$ - pay 20$ from your own pocket)" if (money >= 20) and(seenhallebikini == True) and (boughthallebikini == False):
        scene shop02
        play sound "Sounds/cashregister.wav"
        sc "Here you are. That's for one lucky girl!"        
        $ money -= 20
        $ boughthallebikini = True
        jump HalleGiftDay03

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
        jump ShopClerkDay03

    "Nothing actually":
        jump ShopClerkDay03

    "I don't have enough money to buy anything here." if (money <=9):
        sc "We don't do credit. We don't trust poor people like you."
        p "I feel like... dirt..."
        jump ShopClerkDay03

label ShopCustomerDay03:
scene halleshop01 with dissolve
$ renpy.pause(1.0, hard=True)
if (boughthallebikini == True) and (seenhallebikini == True):
    p "Hey, Halle, why are you still here? I bought you this swimsuit already!"
    show halleshop01b
    ha "Yeah, I know, but the dev is too lazy to remove me from this image..."
    ha "Remember, I'm ACTUALLY at the beach."
    jump Shop01Day03
elif (boughthallebikini == False) and (seenhallebikini == True):
    p "You're still staring at this swimsuit..."
    show halleshop01b
    ha "And I'll keep staring at it until you chip in 20 bucks to buy it for me!"
    jump Shop01Day03

else:
    menu:
        "May I help you with anything miss? Would you like to try this item in one of our cabins?":
            show halleshop01b
            ha "Oh...hum.. Sorry, I didn't realize you worked here... Well, I don't know, it's quite expensive..."
            p "Well, try it on, that's free anyway..."
            ha "Yeah, I guess you're right, I might as well try it on..."
            $ pretendshop = True
            jump HalleChangeDay03
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
                    jump HalleChangeDay03
                "That's too bad, cos I'm sure you would be a hit with that thing on...":
                    ha "(sigh)... Yes, it's too bad..."
                    jump Shop01Day03

label HalleChangeDay03:
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
            jump DowntownChoiceDay03b
        "Wait for her to come out":
            jump HalleBikini01Day03
else:
    ha "Hang on a minute, I'm almost ready..."

label HalleBikini01Day03:
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
        jump HalleBikini02Day03
    "Yeah, really hot... Turn around now...":
        ha "Like...that?"
        jump HalleBikini02Day03

label HalleBikini02Day03:
    scene hallebikini02 with dissolve
$ renpy.pause(1.0, hard=True)
if (pretendshop == True):
    p "Yes, that is a definitive perfect fit..."
    ha "Would...you..consider giving me a discount? I'm twenty bucks short to buy it and I really need a new bikini to go to the beach!"
    "The bikini is marked at 40 dollars..."
    menu:
        "Sure, for a girl like you, half-price! Give it to me and I'll make all the arrangements" if (money >= 20):
            ha "Oh, thank you sssoo much. My name is Halle by the way and I'll be wearing this at the beach if you ever fancy joining me (wink)!"
            jump ShopClerkDay03
        "Mmh, you'll have to show me more to get such a discount price miss...":
            jump HalleTopOffDay03
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
            jump Shop01Day03

else:
    p "Wow, you look really hot...err..."
    ha "The name's Halle. So, since you like it so much, time to chip in 20 bucks like you promised so I can buy it!"
    menu:
        "Ah... About that.. I just realized I don't have enough money." if (money <= 19):
            ha "But..You promised me!"
            p "OK, OK, as soon as I get the money, I'll come back I swear!"
            ha "I'll be here every afternoon, lamenting as to why I can't own this lovely bikini!"
            "Well at least, I know where to find her..."
            jump Shop01Day03
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
            jump Shop01Day03
        "Well, sure...sure... But a little incentive wouldn't hurt... If you know what I mean...":
            ha "I know what you mean...You boys are all the same..."
            jump HalleTopOffDay03
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
            jump ShopClerkDay03
            
label HalleTopOffDay03:
    scene halletopoff with dissolve
$ renpy.pause(1.0, hard=True)  
ha "So... Now that you've seen my big sumptuous tits... Time to cough up the money!"
p "Let me regain my breath first... WOW! I'll pay the difference for you baby!"
jump ShopClerkDay03

label HalleGiftDay03:
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
jump Shop01Day03

label Parlour01Day03:
scene parlour01
$ parlourseen03 = True
$ renpy.pause(1.0, hard=True)
play music "Sounds/parlourmusic.mp3"
ka "Welcome big American boy to \"Misohawny Massage Parlour\"! Me Katsumi, you want massage?"
menu:
    "I was told you did \"full-body massage\"...":
        ka "Yes, sucky sucky 50 dolla."
        p "Ah, I see. Sucky sucky indeed. That's quite expensive for just sucky sucky."
        ka "Me love you long time. For you, more than sucky sucky."
        p "Oh, the conversations we could have my dear..."
        jump ParlourChoiceDay03
    "Yes, how much is it?":
        ka "Normal massage? 10 dolla. More massage, 50 dolla."
        p "And what do I get for 50 dollars exactly?"
        ka "Sucky sucky 50 dolla."
        p "That's a lot of inflation since the Vietnam War..."
        jump ParlourChoiceDay03
    "Nope, not interested...":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceDay03b

label ParlourChoiceDay03:
menu:
    "Get a normal massage (10 $)" if (money >=10):
        jump NormalMassageDay03
    "Choose the \"full-body massage\" experience... (50 $)" if (money >=50) and (stamina >=1):
        jump FullMassageDay03
    "Mmh...I don't seem to have enough money at the moment." if (money <=9):
        ka "You poor. Hah hah. Me not poor. Come back when you not poor."
        p "I certainly will, if just for the highly stimulating conversations."
        jump DowntownChoiceDay03b
    "Mmh, I don't seem to have enough stamina at the moment." if(stamina == 0):
        ka "Ah! You not man enough. You leave and come back when you can cum."
        jump DowntownChoiceDay03b
    "Actually, I don't want anything right now.":
        ka "You waste my time. Come back when you not waste my time."
        jump DowntownChoiceDay03b

label NormalMassageDay03:
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
                jump Parlour05Day03
            "Forget it. Just give me a normal massage.":
                ka katsumi "Ok, me gonna massage your cock because ssooo BIG."
                jump Parlour05Day03
    "OK, OK, I'll pay the difference for a sucky sucky..." if (money >=40) and (stamina >=1):
        $ suckysucky = True
        $ fuckyfucky = True
        $ money -= 40
        jump Parlour05Day03
    "Why don't you just massage it then like if it was one of my big tense muscles?...":
        ka "Oooh, boy very smart. OK, me gonna massage big American cock. But no sucky sucky, you not pay."
        jump Parlour05Day03

label FullMassageDay03:
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
        jump Parlour05Day03        
    "That's cos all Asian men have small penises.":
        ka "Not true. Some Asian men big penis. You like Trump, you racist."
        ka "Me only do sucky sucky. No fucky fucky. Because you bad boy."
        $ fuckyfucky = False
        jump Parlour05Day03

label Parlour05Day03:
scene parlour05 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Big American monster boycock so big and hard!"
p "Yeah, play with it Katsumi! It's all yours!"

label Parlour06Day03:
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
                jump Parlour07Day03
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
                jump DowntownChoiceDay03b
    
label Parlour07Day03:  
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

label Parlour08Day03:  
scene parlour08 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Reaching top of monstercock take me so long... Me love you long time!"
p "Keep going, you still have quite a few inches to go..."

label Parlour09Day03:  
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
                window hide
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
                jump DowntownChoiceDay03b

label Parlour10Day03:  
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
        
label ParlourFuckDay03:
stop music
play music "Sounds/katsumifuck.mp3"
show movieparlourfuck
show cum
call screen parlourfuckcumday03
screen parlourfuckcumday03:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("ParlourCumDay03")

label ParlourCumDay03:
stop music
hide movieparlourfuck
scene parlourcum01
stop music
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
ka "You filling me up with so much boyjuice! You so incredible!"


label ParlourCum02Day03:
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
jump DowntownChoiceDay03b

label Gym01Day03:
stop music
scene gym01 with dissolve
play music "Sounds/gymreception.mp3"
$ renpy.pause(1.0, hard=True)
da "Welcome to \"Jerk n' Clean Fitness Club \". My name is Daniella, how may I help you?"
label Gym01bDay03:
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
                jump Gym03Day03
            "Mmh, I'll think about it.":
                jump Gym01bDay03
    "I'm a member already. A LONG-STANDING \"member\" if you catch my drift...":
        show gym02 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "I tried to catch it but then it flew away..."
        jump Gym01bDay03
    "Why should I pay to join your gym when there are free gyms around the island?":
        da "Because our gym has the best equipment you can find on the island, that's why."
        p "I'm not convinced. You need to prove it."
        show gym03 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "Alright Mr-Big-Shot. Follow me and I'll prove it!"
        jump Gym02Day03
    "Leave the gym":
        jump DowntownChoiceDay03b

label Gym02Day03:
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
        $ money -= 5
        da "Alright! You are free to use any room today then... Except the women's locker room that is."
        jump Gym03Day03
    "OK, I'm sold here's 50 bucks for a monthly pass." if (money >=50):
        if (katsumiwin == True) or (money >= 100):
            da "Mmmh, I wonder how a boy your age managed to accumulate that much money..."
            da "Perhaps you robbed a bank? The Console Bank of Cheats?..."
            p "Err... No, I can explain!"
            da "Bye bye cheat..."
            return
        da "Alright, new member it is!... And don't forget you can invite a friend twice..."
        $ gymmember = True
        $ money -= 50
        $ lust_points[4] +=1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump Gym03Day03
    "Great, I'll try out the equipment straight away then. See you in a bit.":
        da "Err...Sure... I think..."
        jump Gym03Day03
    "Not convinced, I'll give it a pass for today.":
        da "Your choice, but you're missing out on some great fitness fun!"
        jump DowntownChoiceDay03b

label Gym03Day03:
$ wenttogymday03 = True
scene dorisgym01 with dissolve
play music "Sounds/gymabience.mp3"
$ renpy.pause(1.0, hard=True)
"There's only one \"interesting\" customer in the gym at this time."
menu:
    "Do some heavy training (+1hr)" if (workout == False):
        jump GymWorkoutDay03
    "Approach the woman":
        jump GymDorisDay03

label GymWorkoutDay03:
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
        jump SaunaDorisDay03
    "I don't have time right now I'm afraid, it's getting late...":
        do "Too bad boy, we could have had some good time..."
        jump DowntownChoiceDay03b

label SaunaDorisDay03:
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
jump DowntownChoiceDay03b

label GymDorisDay03:
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
label DorisGymTrainDay03:
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
        jump DorisGymTrainDay03

    "Leave and do some heavy training (+1hr)" if (workout == False):
        jump GymWorkoutDay03
    
    "Leave the gym":
        jump DowntownChoiceDay03b

label AudaciousOffice01Day03:
$ seenaudaciousday03 = True
stop music
play sound "Sounds/liftsound.mp3"
scene secretary01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I think I'm on the corporate floor..."
label AudaciousOffice01Day03b:
scene secretary01 with dissolve
st "How may I help you?"
menu:
    "Where's the CEO's office?" if (debbyofficeseen == False):
        st "Do you have an appointment?"
        p "Err... Yeah, sure, I'm a big time swimwear buyer, I need to sign a contract with her."
        scene secretary04 with dissolve
        $ renpy.pause(1.0, hard=True)
        st "Alright, it's down the hallway on your right..."
        p "Well thank you. (That was easy...)"
        jump DebbyOffice01Day03
    "I'm a photographer. Nudge nudge, wink wink." if (hour <=18):
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
        jump Shoot01Day03
    "A receptionist needs good oral skills. Let me test yours...":
        scene secretary02 with dissolve
        $ renpy.pause(1.0, hard=True)
        st "Quit it cowboy, I ain't falling for that...."
        jump AudaciousOffice01Day03b
    "Leave the building":
        jump DowntownChoiceDay03b
    "Look for Nancy's office" if (seenmomofficeday03 == False):
        jump MomOffice01Day03

label Shoot01Day03:
$ seenshoot03 = True
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

label Shoot02Day03:
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
        jump Shoot03Day03
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
        jump AudaciousEscapeDay03

label Shoot03Day03:
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
        jump EndShootDay03

    "The gangbang scene with ten men.":
        aj "Nothing like a bukkake session with tons of cum plastering my huge breasts..."
        p "Well I'm a bukkake machine all by myself..."
        scene shoot08 with dissolve
        $ renpy.pause(1.0, hard=True)
        aj "Is that so? I demand some proof Mr Hank..."
        p " Sure thing, I'll offer you ounces of proof...."
        aj "Mmh, such devotion to your job mr photographer... Bring that crank over here then..."
        jump ShootFuckDay03

    "The scene with the amateur fan.":
        aj "Yes, that was tons of fun. The poor sod was so worried at first, but he gained confidence and then pounded me just as hard as a veteran pornstar."
        scene shoot08 with dissolve
        $ renpy.pause(1.0, hard=True)
        aj "Too bad there isn't someone like him right here... I'm so horny..."
        p "I can volunteer... I'm a major fan myself..."
        aj "Mmh, such devotion to your job mr photographer... Bring that crank over here then..."
        jump ShootFuckDay03


label ShootFuckDay03:
stop music
scene shoot09 with dissolve
$ renpy.pause(1.0, hard=True)
aj "Damn kid, that's the biggest \"crank\" I've ever seen and I've seen hundreds of pornstar dongs!"
p "Enough talking, put that mouth to good use and gobble my shaft as deep as you can!"
aj "I'll try..."
label ShootFuckMouthDay03:
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
        jump ShootFuckMouthDay03
    "Move on":
        pass

label ShootFuckPussyDay03:
p "You're doing good. Not many girls can gobble up my monster dong like that!"
aj "I'm not the winner of \"Pornstar Mouth of the Year\" five years in a row for nothing Mr Hank!"
p "Let's test your \"Pornstar Pussy of the Year\" then..."
aj "Ok, but be caref....."
scene shoot12 with dissolve
$ renpy.pause(1.0, hard=True)
aj "AAAH, You're going ssooo deep! Yes, I want more, pound that pussy, I'm creaming all over that giant cock!!!"
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
        jump ShootFuckPussyDay03
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
$ stamina -=1
show staminaminus01:
    xalign 0.2 yalign 0.4
    linear 1.0 yalign 0.6
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
$ extras += 1
$ hour += 1
aj "Damn boy, you truly are a bukkake machine! Now I have to get cleaned up, I'm caked in semen..."
scene shootend with dissolve
$ renpy.pause(1.0, hard=True)
aj "I have a porn shoot this afternoon and I'm not sure I'll be able to feel my partner's rod this time... You've stretched me so much...."
p "Hank the Crank at your service ma'am!"
p "SHHHIIIT, I forgot to put the timer on! I can't send José any pic of the deed... What a missed opportunity..."

label EndShootDay03:
scene secretary06 with dissolve
$ renpy.pause(1.0, hard=True)
p "Let's just walk nonchalantly past the receptionist, I want to keep that camera to myself, it could be handy..."
play sound "Sounds/whistling.mp3"
$ renpy.pause(2.0, hard=True)
scene downtownaudacious with dissolve
play music "Sounds/downtown.mp3"
$ renpy.pause(1.0, hard=True)
$ stolecamera = True
p "Pfew, I managed to get out of the building..."
jump DowntownChoiceDay03b


label AudaciousEscapeDay03:
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
jump DowntownChoiceDay03b



label DebbyOffice01Day03:

if (hour <= 18):
    jump DebbyOffice01bDay03
if (hour > 18):
    scene debbyoffice02 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Looks like Debby isn't in her office. She must have gone home, it's getting quite late actually... I should leave too."
    jump DowntownChoiceDay03b

label DebbyOffice01bDay03:    
scene debbyoffice01 with dissolve
$ renpy.pause(1.0, hard=True)
$ debbyofficeseen = True
d "Well, if it isn't my favorite sister's tenant! What brings you here?"
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
        jump DowntownChoiceDay03b
    "I just wanted to see where you and Nancy work.":
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
        jump AudaciousOffice01Day03b
    "I would like to offer my services as a critique of your lovely swimsuits.":
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
                jump DebbyOffice02Day03
            "I wouldn't want to intrude. Maybe you have a hot.. I mean a model for this kind of work?":
                show debbyofficeneutral
                d "Of course, but I always beta-test the new swimsuits first... since I'm the CEO. So take it or lose it!"
                p "I'll take it of course!"
                d "Then go and wait in the corridor and I'll call you back in once I'm ready..."
                jump DebbyOffice02Day03

label DebbyOffice02Day03:
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
        jump DebbyOffice04Day03
    "Wow, Debby, you look fabulous in it!":
        d "Well, that's very nice of you to say, but you're supposed to be a critique for the BIKINI, not me..."
        d "I guess you don't have what it takes to be a swimsuit critique, you are too easily distracted by the person wearing in it... (sigh)"
        p "Well...err... I didn't mean to..."
        d "It's best if you leave the building now [name], since your services are not required, you have now become \"unauthorized\" personnel..."
        scene downtownaudacious with dissolve
        p "I don't think I'm gonna be allowed back in today. I really pissed her off..."
        jump DowntownChoiceDay03b
    "Feel up her breasts":
        if (blacktop == True):
            scene debbyoffice06black with dissolve
        else:
            scene debbyoffice06 with dissolve            
        $ renpy.pause(1.0, hard=True)
        d "Come on [name], I know you're a horny boy but this is too bold, I'm your landlady's sister!"
        p "Sorry, I got carried away by those...err...funbags."
        d "I guess you don't have what it takes to be a swimsuit critique, you are too easily distracted by the person wearing in it... (sigh)"
        p "Well...err... I didn't mean to..."
        d "It's best if you leave the building now [name], since your services are not required, you have now become \"unauthorized\" personnel..."
        scene downtownaudacious with dissolve
        p "I don't think I'm gonna be allowed back in today. I really pissed her off..."
        jump DowntownChoiceDay03b

label DebbyOffice04Day03:
scene debbyoffice07 with dissolve
$ renpy.pause(2.0, hard=True)
p "Mmm.... It feels soft yet sturdy..."
d "I'm impressed, you really sound like you know what you're talking about [name]..."
$ lust_points[5] +=1
$ score += 1
show lust01:
    xalign 0.8 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
menu:
    "pull the string up":
        if (blacktop == True):
            scene debbyoffice08black with dissolve
        else:
            scene debbyoffice08 with dissolve            
        $ renpy.pause(2.0, hard=True)
        d "Oops, pull it down now [name], you've \"inspected\" the fabric enough now..."
        $ lust_points[5] +=1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        d "Thanks for your help [name], but now I have a lot of work to do..."
        p "Sure Debby, I'll leave you to it then."
        jump AudaciousOffice01Day03b
        
    "Feel up her breasts":
        scene debbyoffice06 with dissolve
        $ renpy.pause(2.0, hard=True)
        d "Come on [name], I know you're a horny boy but this is too bold, I'm your landlady's sister!"
        p "Sorry, I got carried away by those...err...funbags."
        d "I guess you don't have what it takes to be a swimsuit critique, you are too easily distracted by the person wearing in it... (sigh)"
        p "Well...err... I didn't mean to..."
        d "It's best if you leave the building now [name], since your services are not required, you have now become \"unauthorized\" personnel..."
        scene downtownaudacious with dissolve
        p "I don't think I'm gonna be allowed back in today. I really pissed her off..."
        jump DowntownChoiceDay03b
        
label MomOffice01Day03:
if (hour <= 17):
    scene momwork01 with dissolve
    $ renpy.pause(1.0, hard=True)
    m "[name]! How the hell did you get in here??? You should really leave sweetie, I'm busy with work."
    p "I just wanted to see where you work Nancy!"
    m "Well now you've seen. Get back home before a security guard finds you, I don't want any trouble from you here!"
    p "Ok Nancy, I'm sorry... (I'd better leave)."
    $ seenmomofficeday03 = True
    jump AudaciousOffice01Day03b

if (hour >= 18):
    scene momofficeempty with dissolve
    $ renpy.pause(1.0, hard=True)
    p "Looks like Nancy isn't in her office. She must have gone home, it's getting quite late actually... I should leave too."
    jump DowntownChoiceDay03b

label DinnerDay03:
stop music
if (blacktop == True):
    scene dinnerday03ablack with dissolve
else:
    scene dinnerday03a with dissolve
$ renpy.pause(1.0, hard=True)
m "Enjoy your meal kids!"
s "Thanks mom, it looks delicious as always! I'm glad I decided to go to Chantelle's after dinner!"
if (blacktop == True):
    scene dinnerday03bblack with dissolve
else:
    scene dinnerday03b with dissolve
m "Oh Nikki, you are ever so sweet to say that! I'm sure Chantelle's mom is a good cook too!"
p "What are you talking about?"
if (blacktop == True):
    scene dinnerday03ablack with dissolve
else:
    scene dinnerday03a with dissolve
m "Nikki has a slumber party at her new best friend's house, isn't that great [name]?"
p "Err... I guess so."
show dinnerday03c with dissolve
s "I think you're jealous cos you're not invited!"
if (seenmomofficeday03 == True):
    if (blacktop == True):
        scene dinnerday03bblack with dissolve
    else:
        scene dinnerday03b with dissolve
    m "[name] is so bored, he even came to see me at work! Didn't you [name]?"
    s "Hee hee... Poor [name]!"
    p "Gee, I made the effort of going all the way downtown to see you..."
    if (blacktop == True):
        scene dinnerday03ablack with dissolve
    else:
        scene dinnerday03a with dissolve
    m "Sorry [name], I was just making a joke, I shouldn't have... I appreciated you coming over, my sweet little pumpkin!"
    $ lust_points[16] +=1
    $ score +=1
    show lust01:
        xalign 0.6 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide lust01
    
if (blacktop == True):
    scene dinnerday03ablack with dissolve
else:
    scene dinnerday03a with dissolve
    p "I'll do tons of fun stuff tonight! So there."
m "Ok, eat up or it's going to get cold. [name], you'll do the dishes with me while Nikki packs her sleeping bag."

"You finish cleaning up the dishes with your landlady."
$ hour += 1

label EveningDay03:
stop music
if (blacktop == True):
    scene nikkileavingblack with dissolve
else:
    scene nikkileaving with dissolve
$ renpy.pause(1.0, hard=True)
m "Bye Nikki, enjoy your slumber party, and you girls don't forget to wake up on time for school tomorrow!"
s "Of course mom, don't worry. Bye mom, see you tomorrow after your school trip [name]!"
menu:
    "See you Nikki, say hi to Chantelle for me!":
        s "Humpf, I don't think so, this is a girl's night, I don't want her rambling on about you..."
        if (lust_points[17] <=9):
            $ lust_points[17] -=1
            $ score -=1
            show lustminus01:
                xalign 0.85 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
    "See you Nikki, have a good time with Chantelle!":
        s "I sure will!"

scene eveningmom01 with dissolve
$ renpy.pause(1.0, hard=True)
m "So [name], it's just you and me tonight, isn't that exciting? Do you want to watch a movie with mummy?"
menu:
    "Sure Nancy, if it's an action-packed movie!":
        m "Humpf, I was thinking more of a romantic comedy type of movie... But boys will be boys I guess..."
        m "Choose what you want from GetFlix while I go and change into something more comfortable."
        if (blacktop == True):
            p "Sure Nancy! And I'll change into my white top since you hate the black one so much..."
        jump EveningMovieDay03
    "I'm sorry Nancy, but I'm also invited for..err... a school gathering at the local beach. (Go and meet Laura at the local beach)" if (lauraritual == True):
        m "What? That's unusual. Are you lying to me? Are you seeing someone?"
        window hide
        $ lust_points[16] -=1
        $ score -=1
        show lustminus01:
            xalign 0.35 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        p "No, I swear! There will be several of us, around a campfire just hanging out for a couple of hours, nothing wrong with that! And no alcohol or drugs I promise!"
        if (ryangrounded == True):
            m "May I remind you that you are GROUNDED. For fucking a girl in our backyard in broad daylight! Go back to your room."
            jump EveningChoiceDay03
        m "Alright then. I guess I can't keep you locked in the house anymore, you're a big boy now... (sigh)."
        jump Campfire01Day03
    "I'm sorry Nancy, but I'm invited at... err... a friend's house. (Go to Tanya's House)" if (discovertanya == True):
        if (ryangrounded == True):
            m "May I remind you that you are GROUNDED. For fucking a girl in our backyard in broad daylight! Go back to your room."
            jump EveningChoiceDay03
        m "Oh... Well, you didn't mention that before, is it a slumber party too?"
        p "No, we'll just be playing video games I think..."
        m "Ok, but be back before 11pm, I don't want you walking around the Burbs so late at night, it could be dangerous..."
        p "Yes, don't worry Nancy!"
        jump TanyaHouse01Day03        
    "I really need to train tonight, I haven't trained today and I want to get stronger..." if (workout == False):
        m "Oh, I see, I wouldn't want to stop my boy from getting big and strong, that's for sure!"
        p "I'll go back to my room then..."
        jump EveningChoiceDay03

label EveningMovieDay03:
scene eveningtvmom01 with dissolve
$ renpy.pause(1.0, hard=True)
m "I'm ready! So, what movie did you end up choosing to entertain us tonight?"
menu:
    "Conan the Barbarian":
        m "Alright, I've never seen it before."
        jump MovieConanDay03
    "Alien":
        m "Alright, I've never seen it before."
        jump MovieAlienDay03

label MovieConanDay03:
scene eveningconan with dissolve
play music "Sounds/conan.mp3"
$ renpy.pause(2.0, hard=True)
$ hour += 1
m "This movie is terrible, but that foreign actor... Mmmh, he sure has huge muscles...everywhere... Whoever he is."
label MovieChoiceDay03b:
menu:
    "It's Schwarzenpecker, everybody knows him Nancy, he's super-famous... You've got to go out more often.":
        m "I DO go out, but not to watch that kind of drivel! I'm tired, I'll leave you with your \"super-famous\" actor with a weird accent then!"
        jump MovieMomLeftDay03
    "He's got nothing on me, I bet I have bigger muscles than him!":
        m "If you want to go around pretending that, you need to walk the walk and not just talk the talk, [name]..."
        p "I could pose in my jockstrap and flex my biceps so you can compare with him on the screen! Then, you'll be convinced!"
        m "Alright [name]. Let's see what you've got mister. This is going to be more entertaining than this drivel of a movie!"
        menu: 
            "Do it!":
                jump MovieConan02Day03
            "Do it but use one stamina point to really flex your muscles hard":
                jump MovieConan03Day03
            "Don't do it, Arnie is clearly bigger than you...":
                m "See? Don't brag if you can't follow up, there's a life lesson for you."
                m "I'm tired, I'll leave you to your silly barbarian..."
                jump MovieMomLeftDay03
            "First, drink some white bull because it looks like it might become interesting...." if (stamina == 0) and (whitebull == True):
                show whitebull
                show square
                play sound "Sounds/lost.mp3"
                "You gulped down your White Bull energy drink."
                hide square
                hide whitebull
                $ whitebull = False
                $ stamina += 2
                jump MovieChoiceDay03b
            "Shit, Nancy looks horny enough but I'm not, my stamina is too low...." if (stamina == 0) and (whitebull == False):
                m "See? Don't brag if you can't follow up, there's a life lesson for you."
                m "I'm tired, I'll leave you to your silly barbarian..."
                jump MovieMomLeftDay03

label MovieAlienDay03:
scene eveningalien with dissolve
play music "Sounds/alien.mp3"
$ renpy.pause(2.0, hard=True)
$ hour += 1
m "This movie is really scary. I don't think I can finish watching it. I'll leave you to it son."
p "But Nancy.... The alien is about to kill everyone, you're missing the best bit!"
jump MovieMomLeftDay03

label MovieMomLeftDay03:
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
        jump EveningChoiceDay03
    "Go and meet Laura at the local beach" if (lauraritual == True):
        jump Campfire01Day03
    "Go to Tanya's House" if (discovertanya == True):
        jump TanyaHouse01Day03            
    "Go to your room":
        jump EveningChoiceDay03

label MovieConan02Day03:
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
    jump MomEvening03Day03
if (strength <=7):
    m "Mmh, you're really big, but not quite as big as what I'm seeing on the screen... But with a bit more training, I'm sure you'll be just as big as your favorite actor honey!"
    p "(Well that's disappointing... I could have sworn I was bigger than him...)"
    m "Anyway, I'm tired, I'll leave you to your silly barbarian..."
    jump MovieMomLeftDay03

label MovieConan03Day03:
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
m "Oh, sweetie, you're right, you really are MUCH BIGGER than this actor! I'm is so proud of you!"
$ lust_points[16] +=2
$ score += 2
show lust02:
    xalign 0.9 yalign 0.6
    linear 1.0 yalign 0.4
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
jump MomEvening03Day03

label MomEvening03Day03:
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
    jump MomFuck01Day03
if (lust_points[16] == 9) or (lust_points[16] == 8):
    menu:
        "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
            jump MomPendulumDay03            
        "Spray yourself with pheromones" if (pheromone == True):
            jump MomPheromoneDay03
        "Hold your cock through your jockstrap to show how big it is":
            jump MomStrapDay03
if (lust_points[16] <= 7):
    jump MomStrapDay03

label MomFuck01Day03:
stop music
scene ryanconanposing02 with dissolve
$ renpy.pause(1.0, hard=True)
p "That's right Nancy, you're the one who allowed that thing into your home!"
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
menu:
    "I need to stick my cock between those big jugs...":
        jump MomTitfuckDay03
    "I don't know but I'm about to explode!":
        jump MomBlowjobDay03
        
label MomStrapDay03:
scene ryanconanposing02 with dissolve
$ renpy.pause(1.0, hard=True)
p "That's right Nancy, you're the one who allowed that thing into your home!"
m "It looks so big.... and not even hard. But this is wrong [name], what am I doing? I should leave, I don't want to be a bad landlady who corrupts her sweet tenant's innocent mind!"
p "Noooo... I'm not a sweet tenant! I'm a bad, BAD TENANT! Come back Nancy! AAARGH!"
jump EveningChoiceDay03

label MomPendulumDay03:
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
    jump MomFuck01Day03
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
    jump MomFuck01Day03   
    
    
label MomPheromoneDay03:
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
    jump MomFuck01Day03
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
    jump MomFuck01Day03

label MomTitfuckDay03:
$ momtitfuck = True
scene momtitfuck01 with dissolve
m "Of course [name]. I will take care of that monster with my huge jugs, you just relax and let me do all the work."
label MomTitfuckDay03b:
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
        jump MomTitfuckDay03b
    "Move on":
        pass
if (stamina >=2):
    menu: 
        "Cum, you've got another load for later":
            jump MomTitfuckCumDay03            
        "Don't cum yet and tell her you're about to explode":
            m "Oh sweetie, your huge cock looks like it's ready to explode!"
            if (momblowjob == False):
               m "Bring that massive fuckstick to my mouth [name]!"
               jump MomBlowjobDay03
            else: 
                m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
                jump MomPussyLickDay03
if (stamina <=1):
    m "Oh sweetie, your huge cock looks like it's ready to explode!"
    if (momblowjob == False):
        m "Bring that massive fuckstick to my mouth [name]!"
        jump MomBlowjobDay03
    else: 
        m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
        jump MomPussyLickDay03            

label MomTitfuckCumDay03:
scene momtitfuckcum01 with dissolve
play sound "Sounds/ryancumming.mp3"            
$ renpy.pause(2.0, hard=True)
scene momtitfuckcum02 with dissolve
# play sound "Sounds/momtitfuckcum.mp3"            
$ renpy.pause(11.0, hard=True)
$ stamina -=1
show staminaminus01:
    xalign 0.8 yalign 0.4
    linear 1.0 yalign 0.6
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
m "Damn [name], you really had a lot of pent-up cum stored in those huge balls..."
if (momblowjob == False):
    m "Bring that massive fuckstick to my mouth!"
    jump MomBlowjobDay03
else: 
    m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
    jump MomPussyLickDay03

label MomBlowjobDay03:
$ momblowjob = True
scene momblowjob01 with dissolve
# play sound "Sounds/momlick01.mp3"  
$ renpy.pause(1.0, hard=True)
m "My God, your cock... It's just GIGANTIC! I can't even wrap my fingers around its incredible girth..."
scene momblowjob01b with dissolve
# play sound "Sounds/momlick02.mp3"  
$ renpy.pause(1.0, hard=True)         
m "Mmmh... And those balls... So HEAVY, I just have to taste them..."         
label MomBlowjobDay03b:
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
        jump MomBlowjobDay03b
    "Move on":
        pass

m "Oh sweetie, your huge cock looks like it's ready to explode!"
if (momtitfuck == False):
    m "Why don't you stick your pud between my big tits?"
    jump MomTitfuckDay03
if (momtitfuck == True):
    m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
    jump MomPussyLickDay03            
 
label MomPussyLickDay03:
scene eveningmomclit with dissolve
#play sound "Sounds/momclit.mp3"
$ renpy.pause(1.0, hard=True)
m "Mmmh, you do that so well sweetie! You really know what you're doing! AAAH!"
m "Now it's time for me to reward you... With my pussy!"
jump MomFullFuckDay03

label MomFullFuckDay03:
scene eveningmomready with dissolve
#play sound "Sounds/momready.mp3"
$ renpy.pause(1.0, hard=True)
m "See my tender pink pussy? It's wet and ready for you my studly tenant! Come and pound it!"
#play music "Sounds/momslowfuck.mp3"
show momfuckslow
show faster
call screen momfuckslowday03
screen momfuckslowday03:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MomFuckFastDay03")
label MomFuckFastDay03:
hide faster
stop music
#play music "Sounds/momfastfuck.mp3"
show momfuckfast
show cum
call screen momfuckfastday03
screen momfuckfastday03:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MomFuckCum")

label MomFuckCum:
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
m "I should go and take a shower, since I'm covered in your red-hot spunk... We'll keep this...incident... between us sweetie."
if (nancyjosewin == False):
    p "Sure Nancy! (She didn't notice I took a picture of us... Now I'll send it to José)."
    $ nancywin = True
if (nancyjosewin == True):
    p "Sure Nancy! (Although everyone already knows you fucked José you slut...)"
$ nancyfucked = True
jump EveningChoiceDay03

label TanyaHouse01Day03:
$ seentanyaday03 = True
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
                jump TanyaHouse02Day03
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay03
    "I'm out of here, you guys are crazy!":
        ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
        jump EveningChoiceDay03
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
                jump TanyaHouse02Day03
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay03
    "Err, I wasn't expecting anything sexual and I'm not ready... I'm... exhausted." if (stamina == 0):
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
        jump EveningChoiceDay03
    "My name is [name] and I ain't playing the cuck you'll find out... (+ drink some White Bull)" if (stamina == 0) and (whitebull == True):
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
                jump TanyaHouse02Day03
            "I'm out of here, you guys are crazy!":
                ta "Your loss, I'll find another young stud to replace you, I've already spotted a few on this island!"
                jump EveningChoiceDay03

label TanyaHouse02Day03:
play music "Sounds/tanyamusic.mp3"
$ tanyawebcamday03 = True
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
call screen tanyawankslow
screen tanyawankslow:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("TanyaWankFast")
label TanyaWankFast:
hide faster
show tanyawankfast
show cum
call screen tanyawankfast
screen tanyawankfast:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TanyaWankCum")

label TanyaWankCum:
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
        jump EveningChoiceDay03
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
                jump EveningChoiceDay03
            "Go and meet Laura at the local beach" if (lauraritual == True) and (seencampfireday03 == False):
                jump Campfire01Day03

label Campfire01Day03:
$ seencampfireday03 = True
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
        jump CampfireLeftDay03
    "Whisper the words":
        p "Evil, live, live, evil... Evil, live, live, evil..."
        $ ritualwords = True
        jump Campfire02Day03
    "Just continue watching":
        $ ritualwords = False
        jump Campfire02Day03

label Campfire02Day03:
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
            jump DamianCurseDay03
        "Curse José":
            jump JoseCurseDay03
        "Don't curse anyone, this is too satanic":
            jump NoCurseDay03

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
            jump EveningChoiceDay03
        "Go to Tanya's House" if (discovertanya == True) and (seentanyaday03 == False):
            jump TanyaHouse01Day03
    
label DamianCurseDay03:
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
jump CampfireLaura01Day03

label JoseCurseDay03:
p "I curse thee, José!"
"Choose a girl to go with José's curse (-3 challenger lust points for her):"
label ChooseGirlCurseDay03:
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
        jump ChooseGirlCurseDay03
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
        jump CampFireEndDay03
    "Maddy":
        show maddysprite at CampfirePosition
        $ lust_pointsB[14] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay03        
    "Nikki":
        show nikkisprite at CampfirePosition
        $ lust_pointsB[17] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay03
    "Frieda":
        show friedasprite at CampfirePosition
        $ lust_pointsB[8] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay03
    "Kate":
        show katesprite at CampfirePosition
        $ lust_pointsB[11] -=3
        show challengerlustminus03:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustminus03
        jump CampFireEndDay03
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
        jump CampFireEndDay03


label NoCurseDay03:
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
jump EveningChoiceDay03

label CampFireEndDay03:
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
        jump EveningChoiceDay03        
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
        jump CampfireLaura01Day03
                
label CampfireLaura01Day03:
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
    jump LauraFuck01Day03

label LauraCampFireChoiceDay03:
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
                jump EveningChoiceDay03
            "Go to Tanya's House" if (discovertanya == True) and (seentanyaday03 == False):
                jump TanyaHouse01Day03
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
                jump EveningChoiceDay03
            "Go to Tanya's House" if (discovertanya == True) and (seentanyaday03 == False):
                jump TanyaHouse01Day03
    "Use the pendulum on her" if (pendulumactive == True) and (pendulum == True):
        jump LauraPendulumDay03
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
        p "Err, okay, I hope to see you again Laura..."
        la "You will, don't worry..."
        jump LauraCampFireChoiceDay03

label LauraPendulumDay03:
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
    jump LauraFuck01Day03
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
    jump LauraFuck01Day03  

label LauraFuck01Day03:
stop music
scene campfire13 with dissolve
$ renpy.pause(1.0, hard=True)
la "I... have an uncontrollable urge to... get close to you... Don't resist, it's futile..."
p "Oh, I won't resist, don't worry Laura! (Bingo!)"
la "Take those shorts off... I want to see your demonic pillar of lust!"
scene campfire14 with dissolve
$ renpy.pause(1.0, hard=True)
la "Sweet Belzebuth! This thing is HUGE, like... out of this world!"
p "Yes, do something about it Laura, I am possessed by a satanic desire to fuck you so hard!"
la "Alright [name], let me take care of that bad boy..."
label LauraFuck01Day03b:
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
        jump LauraFuck01Day03b
    "Move on":
        pass

scene campfire15 with dissolve
play sound "Sounds/laura01.mp3"    
$ renpy.pause(8.0, hard=True)
la "You seem to have liked that... Your cock has turned into a steel-hard pole!"
menu:
    "Make it spew its evil load with your hands!" if (stamina >=2):
        jump LauraFuck03Day03
    "I need to put it into something soft and warm!":
        jump LauraFuck02Day03
    "Tease it with your fingernails!" if (stamina ==1):
        jump LauraFuck03Day03

label LauraFuck03Day03:
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
label LauraFuck03Day03b:
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
        jump LauraFuck03Day03b
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
    jump LauraFuck02Day03b
if (stamina == 1):
    p "Enough, I can't take much more of that teasing, I need to put my cock into something soft and warm! And very deep preferably..."    
    la "Such eagerness... Alright, I will ride that horsecock cowboy!"
    jump LauraFuck02Day03b
label LauraFuck02Day03:
if (lauratease == False):
    la "I think I should first tease that throbbing cock with my fingernails..."
    p "Ah, err. Ok."
    jump LauraFuck03Day03
    
label LauraFuck02Day03b:
stop music
play sound "Sounds/campfire.mp3"
play music "Sounds/laurafuckslow.mp3"
show laurafuckslow
show faster
call screen laurafuckslowday03
screen laurafuckslowday03:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("LauraFuckFastDay03")

label LauraFuckFastDay03:
stop movie
hide faster
play music "Sounds/laurafuckfast.mp3"
show laurafuckfast
show cum
call screen laurafuckfastday03
screen laurafuckfastday03:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("LauraFuckCumDay03")
    
label LauraFuckCumDay03:
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
la "Kiss me while I'm covered in your sticky spunk... This was so amazing [name]!"
play sound "Sounds/kissing.mp3"
$ renpy.pause(1.0, hard=True)
if (laurajosewin == False):
    $ laurawin = True
$ fuckedschoolgirlday03 = True
$ hour += 1
la "I should go back home now, after an evening dip in the sea to clean myself of your MASSIVE load (giggles). See you tomorrow [name]!"
p "Good night Laura, see you tomorrow!"
menu:
    "Go back home":
        jump EveningChoiceDay03
    "Go to Tanya's House" if (discovertanya == True) and (seentanyaday03 == False):
        jump TanyaHouse01Day03

label EveningChoiceDay03:
stop music
scene ryanbedroomnight with dissolve
$ locroom = True
$ renpy.pause(1.0, hard=True)

if (hour >= 24):
    if (challengercalls <= 10):
        $ lustaddedB = 2
        call Challenger from _call_Challenger_41
        $ lustaddedB = 1
        call Challenger from _call_Challenger_42
        $ challengercalls += 2        
    p "I should really go to sleep now, tomorrow is a school day..."
    jump SleepDay03
p "mmmh, what should I do?"
menu:
    "Do some heavy bodybuilding (+2hrs)" if (hour <= 22):    
        if (workout == True):
            "You already trained today."
            jump EveningChoiceDay03
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
            jump EveningChoiceDay03
    "Check the computer":
        jump ComputerEveningDay03
    "Admire my body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump EveningChoiceDay03
    "Read the book Laura gave you (+1hr)" if (book == True) and (bookread == False):
        jump RyanReadingEveningDay03
    "Go to Nancy's room" if (nightmomroomseen02 == False) and (nightmomroomseen03 == False) and (hour >=22):
        jump MomUndressingDay03
        
label ComputerEveningDay03:
scene ryancomputer with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
label ComputerEveningDay03b:
scene ryancomputer
$ renpy.pause(1.0, hard=True)
menu:
    "Check the map":
        jump MapEveningDay03
    "Check the stats":
        jump StatsEveningDay03
    "Check the character sheets":
        hide screen statsbackground
        hide screen inventorybutton
        hide screen calendar
        call screen charactersheets
        hide exitcharactersheets
        show screen statsbackground
        show screen inventorybutton
        show screen calendar
        jump ComputerEveningDay03b
    "Learn how to use the pendulum" if (pendulum == True) and (pendulumactive ==False):
        jump CompPendulumEveningDay03
    "Play a smutty game (+1hr)":
        jump CompGameEveningDay03
    "Turn the computer off":
        jump EveningChoiceDay03
    
label RyanReadingEveningDay03:
scene ryanreading with dissolve
$ renpy.pause(1.0, hard=True)
"You read the book Laura gave you. The preface is by Kim-Jong-Un."
ki "I fully embrace the goth movement. I wear black all the time, I'm always gloomy and I hate the whole world."
ki "Also, I killed my uncle and my brother. So I'm, like, the ultimate goth really. Enjoy this book. Or actually, don't."
$ bookread = True
$ hour += 1
jump EveningChoiceDay03

label CompPendulumEveningDay03:
"You look up how to use the pendulum on the internet. Apparently, you have to wiggle it in front of your target. Who would have known?"
$ pendulumactive = True
$ hour += 1
jump ComputerEveningDay03b

label MapEveningDay03:
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
jump ComputerEveningDay03b

label StatsEveningDay03:
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
jump ComputerEveningDay03b       

label CompGameEveningDay03:
scene ryancomputergame with dissolve
$ renpy.pause(1.0, hard=True)
p "This game is tough. My fingers hurt like hell from so much clicking..."
$ hour +=1
jump ComputerEveningDay03b 
        
label MomUndressingDay03:
stop music
$ nightmomroomseen03 = True
$ locroom = False
scene nancybedroomclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "The door is locked but I can see some light poking through the keyhole."
menu:
    "Look through the keyhole":
        jump MomUndressingDay03b
    "Leave and go back to my room":
        jump EveningChoiceDay03
        
label MomUndressingDay03b:
scene nancyundressing01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Nnacy is sitting on her bed. She looks like she's thinking about doing something..."
p "More landlady blueballing on the way for you guys it seems... What should I do?"
menu:
    "Why do you even ask? Look on of course!":
        jump MomUndressing02Day03
    "I feel dirty watching Nancy like that. Go back to my room and cry into my pillow":
        jump EveningChoiceDay03

label MomUndressing02Day03:
play music "Sounds/sneaky.mp3"
scene momundressing02 with dissolve
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
    jump EveningChoiceDay03

scene nancyundressing07 with dissolve
$ seenmomundressingfullday03 = True
$ renpy.pause(1.0, hard=True)
p "Ah, I see, her \"suitor\" is called mr Big Black Dildo..."

scene nancyundressing08a with dissolve
$ renpy.pause(1.0, hard=True)
p "She's sticking it right up her poop chute..."
play sound "Sounds/katewank.ogg"
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene momundressing08a
$ renpy.pause(0.5, hard=True)
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene momundressing08a
$ renpy.pause(0.5, hard=True)
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene momundressing08a
$ renpy.pause(0.5, hard=True)
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene momundressing08a
$ renpy.pause(0.5, hard=True)
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene momundressing08a
$ renpy.pause(0.5, hard=True)
scene nancyundressing08b
$ renpy.pause(0.5, hard=True)
scene momundressing08a
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
jump EveningChoiceDay03    

label SleepDay03:
scene ryansleeping with dissolve
play music "Sounds/ryansnoring.mp3"
$ renpy.pause(1.0, hard=True)
"You fall asleep and dream of your adventures to come..."
$ renpy.pause(2.0, hard=True)

"Your current score (not that it matters) is: {b}[score]{/b}"
if (score <=65):
    "Your ranking: {b}Douchebag{/b}"
elif (score <=75):
    "Your ranking: {b}Noob{/b}"
elif (score <=85):
    "Your ranking: {b}Average Joe{/b}"
elif (score <=95):
    "Your ranking: {b}Hunk{/b}"
else:
    "Your ranking: {b}Babe Magnet{/b}"
stop music
window hide
jump Day04
 




                
                
                
                
                
        
                
                                                      
        
        
    
            
    







 








