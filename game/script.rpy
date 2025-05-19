# The script of the game goes in this file.


# Movies
image movie = Movie(size=(1280,720), xpos=0, ypos=0, xanchor=0, yanchor=0)
init:

    define fastdissolve = Dissolve(0.2)
    define flash = Fade(0.1, 0.05, .2, color="#fff")
    style say_dialogue2:
        size 30
        font "gui/Boogaloo-Regular.ttf"
        xpos 200
        ypos 1
        xmaximum 1020
        bold False
        color "#e2edff"
        justify True
        line_spacing 2

    style say_dialogue1:
        size 30
        font "gui/Boogaloo-Regular.ttf"
        xpos 200
        ypos 1
        xmaximum 1020
        bold False
        color "#feedff"
        justify True
        line_spacing 2

init python:
    def blink(trans, st, at):
        global blink_timer

        if st >= blink_timer:
            blink_timer = renpy.random.random()
            return None
        else:
            return 0

    # Define function to open the menu
    def show_achievement_menu():
        renpy.call_in_new_context("display_achievement_menu")

    # Add key to 'open_achievement_menu', this case is 'a' on keyboard
    config.keymap["open_achievement_menu"] = ["a"]
    
    # When key is pressed at anytime, open custom screen.
    config.underlay.append(renpy.Keymap(open_achievement_menu=show_achievement_menu))

    # Define function to open the menu
    def show_gallery_menu():
        renpy.call_in_new_context("display_gallery_menu")

    # Add key to 'open_achievement_menu', this case is 'a' on keyboard
    config.keymap["open_gallery_menu"] = ["c"]
    
    # When key is pressed at anytime, open custom screen.
    config.underlay.append(renpy.Keymap(open_gallery_menu=show_gallery_menu))

# The game starts here.
label start:
show screen statsbackground
scene black with dissolve
play music "Sounds/airplane.mp3"
"Press c at any time during the game to access the CG gallery."
p "I'm so excited, I'm on a private jet flying to my new life."
scene plane01 with dissolve
$ renpy.pause(1.0, hard=True)
p "This is my landlady Nancy and her daughter Nikki... I decided to move with them because of Patreon rules."
p "Nancy's sister, Debby already lives on the tropical island we're going to call home soon." 
p "She found the perfect job and a new house for Nancy since her divorce."
play sound "Sounds/fastenbelt.mp3"
c "This is your captain speaking, we are making our final approach to Veri-Bosti Island. Please prepare for landing."
scene plane02 with dissolve
$ renpy.pause(1.0, hard=True)
h "Buckle up, we're about to land... You too, nice young boy, what's your name?"
$ name = renpy.input("My name is...")
$ name = name.strip()
h "Well [name], time for you to put on your seatbelt, if you can maneuver it over that...BIG...bulge of yours (wink)." 
window hide
show lust05:
    xalign 0.6 yalign 0.3
    linear 1.0 yalign 0.1
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust05
menu:
    "I need to use the restroom first!":
        h "OK, but be quick!"
        jump Restroom01
    "Sure, thanks for reminding me ma'am.":
        h "Have a nice trip young man!"
        jump Landing    
    "Why don't you buckle me up and find out for yourself how huge it really is?":
        h "(blush) Oh, well, I don't know...I..."
        m "What on earth is wrong with you?"
        window hide
        $ lust_points[16] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.2 yalign 0.6
            linear 1.0 yalign 0.8
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        s "God, you're such a pervert [name]..."
        window hide
        $ lust_points[17] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.8 yalign 0.6
            linear 1.0 yalign 0.8
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        h "I think I'd better go back to the cock...pit."
        jump Landing
        
label Restroom01: 
scene plane03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Damn, this hot stewardess made me hard!"
window hide
play sound "Sounds/knock.mp3"
$ renpy.pause(1.0, hard=True)
h "Is everything okay in there?"

menu:
    "Hum, yeah, I'm almost done!":
        p "Damn, I need to piss fast and get back to my seat."
        jump Landing
    "Well, I could use some help in here.":
        jump Restroom02

label Restroom02:
$ extras += 1
play sound "Sounds/dooropen.mp3"
$ renpy.pause(1.0, hard=True)
scene plane04 with dissolve
$ renpy.pause(1.0, hard=True)
h "OMG, that's the biggest cock I've ever seen!"
show lust05:
    xalign 0.5 yalign 0.25
    linear 1.0 yalign 0.05
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust05
show epiclust:
    xalign 0.5 yalign 0.1
    zoom 0.5
    linear 2.0 zoom 1.0
play sound "Sounds/epiclust.mp3"
$ renpy.pause(4.0, hard=True)
hide epiclust
h "What could I do to make it go down before we land?"

menu:
    "You could suck me and swallow my load!":
        jump HostessBlowjob

    "You could bend over and take it deep in your pussy!":
        jump HostessFuck

label HostessBlowjob:
play music "Sounds/planetitfuck.mp3"
show movieplanetitfuck with dissolve
show cum
call screen planetitfuck
screen planetitfuck:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PlaneTitFuckCum")
label PlaneTitFuckCum:
hide cum
hide movieplanetitfuck
scene hostessblowcum01
stop music
play music "Sounds/airplane.mp3"
play sound "Sounds/imcumming02.mp3"
$ renpy.pause(1.0, hard=True)
h "Gllrbb... mmmggg..."
scene hostessblowcum with dissolve
$ renpy.pause(1.0, hard=True)
$ hostessblowjob = True
$ stamina -=1
show staminaminus01:
    xalign 0.3 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01

if hostessfuck == False:
    h "Fuck, that was a GIANT load of cum!"
    h "Too bad, I would have loved to take that massive young piece of meat up my pussy..."
    p "Who says I can't go again?"
    h "What??? You're ready to pump me again so soon? Fuck me like the wild animal you are stud!"
    menu:
        "Sure thing, buckle up for a wild ride!":
            jump HostessFuck
        "Why would I want to waste all my stamina on a cheap whore like you?":
            h "I'm not a cheap whore! Well, OK, I am a cheap whore...I'll go back to the cock... pit."
            jump Landing
else:
    h "Wow, another GIANT load of cum that filled me up like a three-course meal!"
    h "You were amazing [name], but we'd better hurry back to our seats!"
    jump Landing

label HostessFuck:
play music "Sounds/planefuck.mp3"
show movieplanefuckslow
show faster
call screen planefuckslow
screen planefuckslow:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("PlaneFuckFast")
label PlaneFuckFast:
hide faster
show movieplanefuckfast
show cum
call screen planefuckfast
screen planefuckfast:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("HostessFuckCum")
label HostessFuckCum:
hide cum
hide movieplanefuckfast
hide movieplanefuckslow
scene hostessfuckcum01
stop music
play music "Sounds/airplane.mp3"
play sound "Sounds/imcumming.mp3"
$ renpy.pause(1.0, hard=True)
p "Fuck, cumming sssoo hard!"
scene hostessfuckcum with dissolve
$ renpy.pause(1.0, hard=True)
$ hostessfuck = True
$ stamina -=1
show staminaminus01:
    xalign 0.1 yalign 0.2
    linear 1.0 yalign 0.4
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
show achievement01:
    xalign 0.5 yalign 0.2
    zoom 0.5
    linear 2.0 zoom 1.0
play sound "Sounds/achievement.mp3"
$ renpy.pause(4.0, hard=True)
hide achievement01
$ achievement.grant("milehigh")
"Press a at any time during the game to access the achievements screen."

if hostessblowjob == False:
    h "Damn kid, you filled me up with a massive load of young virile cum and you're still cumming buckets all over my back!"
    h "Too bad, I would have loved to taste that lovely load in my mouth..."
    p "Who says I can't go again?"
    h "What??? You're ready to cum again so soon? Face-fuck me like the wild animal you are stud!"
    menu:
        "Of course, open wide and say \"AAAh!\"":
            jump HostessBlowjob
        "Why would I want to waste all my stamina on a cheap whore like you?":
            h "I'm not a cheap whore! Well, OK, I am a cheap whore...I'll go back to the cock..pit."
            jump Landing
else:
    h "Damn kid, where do you store all that cum? I'm bloated with your second huge load!"
    h "You were amazing [name], but we'd better hurry back to our seats!"
    jump Landing


label Landing:
scene jetlanding with dissolve
stop music
play music "Sounds/airplanelanding.mp3"
$ renpy.pause(1.0, hard=True)

p "We finally land on Veri-Bosti island under clear blue skies."
p "After a short taxi ride, we arrive at our new house..."

stop music
scene house01 with dissolve
m "Let's unpack our bags. You two can go and settle down in your rooms."
p "Sure Nancy, I can't wait to see it and explore the whole house!"
s "This place is amazing mom!"
m "Yes, we have your aunt Debby to thank for that. We should call her up later in the afternoon."

label RyanRoom01:
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "Nice, I have a bed to sleep in, a computer to do like... geeky stuff... and some weights for training."
label RyanRoom01b:
menu:
    "Turn the computer on":
        p "The computer is now turned on and some funny icons appear on the screen. I should check back later this evening."
        jump RyanRoom01b
    "Do some heavy bodybuilding (+2hrs)":
        p "That would take at least two hours, I don't have time for that right now..."
        jump RyanRoom01b
    "Unpack and explore the rest of the house":
        jump HouseChoice01
    "Admire my own body in the mirror.":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump RyanRoom01b

label HouseChoice01:
p "Where should I go?"
menu:
    "Go to the living room":
       jump LivingRoom01
    "Go to the swimming pool" if (housepoolseen01 == False):
        jump HousePool01
    "Go to Nikki' room" if (sisroomseen01 == False):
        jump NikkiRoom01
    "Go to the bathroom" if (showerseen01 == False):
        jump BathRoom01
    "Go to Nancy's room" if (momroomseen01 == False):
        jump NancyRoom01

label HousePool01:
$ housepoolseen01 = True
scene housepool01 with dissolve
stop music
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
p "Nancy is relaxing by the pool in a hot swimsuit."
m "Oh, hi sweetie, did you unpack all your stuff already?"
menu:
    "Yes, I got all my weightlifting equipment set up, that's the most important!":
        m "Ooh, that's nice, so you'll be able to get even bigger muscles."
        $ lust_points[16] += 1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        p "Yeah, and get stronger too!"
        m "Mmh, I like my tenant to be big and strong...Now I'm gonna relax a bit by the pool, meet me later in the living room."
    "Sure, all my clothes are neatly stored in the wardrobe.":
        m "That's a good boy. Now I'm gonna relax a bit by the pool, meet me later in the living room."
jump HouseChoice01

label NancyRoom01:
stop music
$ momroomseen01 = True
scene nancybedroomclosed with dissolve
$ renpy.pause(1.0, hard=True)
p "The door is locked and no one's answering."
p "Nancy must be somewhere else then. I'm so smart."
jump HouseChoice01

label NikkiRoom01:
stop music
$ sisroomseen01 = True
scene nikkibedroom01 with dissolve
show nikkiunpacking
$ renpy.pause(1.0, hard=True)
p "Nikki is still unpacking her stuff."
menu:
    "Hey Nikki, do you need help with those weights?":
        s "I'm strong enough to deal with them myself [name]..."
    "Fancy a dip in the swimming pool with me?":
        s "Can't you see I'm busy unpacking?"
        p "Well...I meant..like...later."
jump HouseChoice01

label BathRoom01:
stop music
$ showerseen01 = True
scene bathroomday with dissolve
$ renpy.pause(1.0, hard=True)
p "This is our bathroom, no one is around right now."
menu:
    "Take a shower":
        jump Shower01
    "Leave":
        jump HouseChoice01
    
label Shower01:
scene shower with dissolve
stop music
play music "Sounds/shower.mp3"
$ renpy.pause(1.0, hard=True)
p "That's nice and relaxing..."
if (stamina <= 4):
    $ stamina += 1
    show stamina01:
        xalign 0.4 yalign 0.4
        linear 1.0 yalign 0.2
    play sound "Sounds/more.mp3"
    $ renpy.pause(2, hard=True)
    hide stamina01
jump HouseChoice01

label LivingRoom01:    
stop music
if (showerseen01 == True) and (housepoolseen01 == True) and (momroomseen01 == True) and (sisroomseen01 == True):
    jump Decision01
else:
    scene livingroom01 with dissolve
    $ renpy.pause(1.0, hard=True)
    p "That's our living room. But no one's around..."
    jump HouseChoice01

label Decision01:
stop music
scene decision with dissolve
$ renpy.pause(1.0, hard=True)
m "So, how are you two settling into your new home?"
s "I love my room and the swimming pool!"
p "Same here, although I didn't have time to try out the swimming pool."
m "I should call Debby and invite her over..."
s "Can't we go to the beach first, it's so sunny outside and we'll catch up with aunt Debby later?..."
menu:
    "Side with Nancy":
        p "Nancy's right, I think we should call Debby before heading for the beach..."
        m "Good, that's settled then, I'll call her and we'll wait for her to come over."
        $ auntfirst = True
        jump AuntDebby01
    "Side with Nikki":
        s "Yeah, we're going to the beach! Thank you [name]! Lemme get my swimsuit..."
        m "Oh well, you guys win...Kids..."
        jump TravelBeach01

label AuntDebby01:
play sound "Sounds/doorbell.mp3"
scene adebby01 with dissolve
$ renpy.pause(1.0, hard=True)
m "Oh, my dear sister, how nice it is to see you again!"
d "I'm thrilled to have you living here Nancy! I hope you enjoy your new house."
d " I don't live far, just round the corner on Longpole Street."
$ discoveraunthouse = True
show addedlocation:
    xalign 0.6 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide addedlocation
m "It is simply amazing Debby! Nikki and [name] both love it too."
d "Oh my, look at how they have grown! They are so...muscular..."
m "Well, you know they were both diagnosed with a lack of myostatin at birth..."
m "The doctors said the best way to avoid any complication was for them to bulk up."
d "I see. It seems that other parts of their bodies have grown too... Nikki is already busty enough to be a model for \"Audacious\" I would say!"
s "What's that?"
m "It's Debby's company. I told you she had founded a swimwear brand, it's called \"Audacious\", you didn't see the billboards on the way from the airport?"
p "Oh yeah, I noticed...All those busty models..."
d "Raging hormones already [name]? Come and give your fake aunt a big hug!"
scene adebby02 with dissolve
$ renpy.pause(1.0, hard=True)
d "Good lord, look at all those muscles on top of muscles! At such a young age..."
p "(Those tits in my face...I'm getting a boner...)"
d "Oh, watch out with that huge log down there boy, you could poke someone's eye out with it!"
$ lust_points[5] +=2
$ score += 2
show lust02:
    xalign 0.35 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
p "oh, sorry Debby...I didn't mean to..."
d "No need to apologize... I understand... (wink)"

scene adebby03 with dissolve
d "I brought some of our new swimsuit products. Remember, while you will be my top exec, we both have to do our bit for the company and save money by being models too..."
m "Yes, I understand... But in front of Nikki and [name]?"
d "Why not, they can give us their opinion, all the better!"
p "Oh yeah, that sounds like a great idea!"
s "I knew he would say that, [name] is a total pervert."
p "That's not true, I'm just trying to help out, that's all!"
m "OK, calm down you two. Go and sit in the backyard, aunt Debby and I will change into some of these swimsuits and come and join you."
scene housepoolempty with dissolve
stop music
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
p "I can't wait to see Nancy and Debby in some skimpy swimsuit..."
d "I'll come out first with a new swimsuit from our \"Audacious MILF\" bikini line..."
window hide
show debbybikini01:
    xalign 0.9
    linear 4.0 xalign 0.5
$ renpy.pause(6, hard=True)
hide debbybikini01
show debbybikini02 with dissolve
$ renpy.pause(3, hard=True)
d "So, what do you guys think of this bikini?"
s "I like it a lot. It's audacious but it's not too skimpy."
menu:
    "Mmmh, maybe it would be better if it was a bit more revealing though...":
        d "Oh, is that so, you want to see me in a skimpier bikini do you? (wink)"
        $ lust_points[5] +=1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
    "Yes, I agree with Nikki, it's a perfect balance between audacity and...sexiness...":
        d "Glad to hear that from both of you. We do have skimpier bikinis too of course."    
d "Your turn Nancy. This is the \"Navy Girl\" line."
hide debbybikini02
window hide
show nancybikini01:
    xalign 1.0 yalign 0.0
    linear 4.0 xalign 0.5
$ renpy.pause(6, hard=True)
d "Smile more Nancy and turn around so they can see the back, it's important."
m "Hum...Okay..."
hide nancybikini01
show nancybikini02 with dissolve
$ renpy.pause(3, hard=True)
s "This bikini really suits you mom!"
p "I prefer the one you were wearing earlier this afternoon."
d "Boy do we have a critique. My turn for a more naughty look, from our new \"Cougar\" line."
window hide
hide nancybikini02
show debbybikini03:
    xalign 0.9
    linear 4.0 xalign 0.5
play sound "Sounds/wolfwhistle.mp3"
$ renpy.pause(6, hard=True)
hide debbybikini03
show debbybikini04 with dissolve
$ renpy.pause(3, hard=True)
d "Is that maybe more to your liking [name]?"
p "Yes Debby, yes it is..."
s "[name] is getting a boner, GROSS."
p "No I'm not! That's my normal...ahem...size."
d "Let's have a look at Nancy wearing our regular \"Big Bust\" swimwear..."
hide debbybikini04
window hide
show nancybikini03:
    xalign 1.0 yalign 0.0
    linear 4.0 xalign 0.5
$ renpy.pause(6, hard=True)
d "Turn around and bend over..."
hide nancybikini03
show nancybikini04 with dissolve
$ renpy.pause(3, hard=True)
m "Like...that?"
d "Perfect, hold it there..."
p "ggg...gggg...."
s "[name] can't even think anymore, all the blood went to his dick!"
d "That means it's a good bikini. The aim is to make heads turn, we succeeded."
hide nancybikini04
m "Well Thanks Debby, that was fun at the end of the day."
d "You're welcome, there's more swimsuits to try, I might be back soon (wink)."
d "But for now, I'd better leave you guys, I have some more designing work to do! See ya!"
if (auntfirst == True):
    m "Ok, now we can go to the beach Nikki..."
    s "Yeah! I'll get my bikini and I'll be down in a minute!"
    stop music
    jump TravelBeach01
if (auntfirst == False):
    m "Ok, time for dinner, good think I prepared it before aunt Debby came..."
    $ hour += 1
    stop music
    jump Dinner01
    
label TravelBeach01:
scene cardrive01 with dissolve
play music "Sounds/cardrive.mp3"
$ renpy.pause(1.0, hard=True)
m "I hear the island has several beaches but this one's the best."
s "What's it called?"
m "Tini-Wini-Bikini beach."
p "I like that name for some reason..."
stop music
play music "Sounds/oceanwaves.mp3"
scene beach with dissolve
$ renpy.pause(1.0, hard=True)
show beachnancysprite
$ renpy.pause(1.0, hard=True)
m "There it is kids, Tini-Wini-Bikini Beach... Let's find a nice spot and relax for a while..."
hide beachnancysprite

scene tiniwini01 with dissolve
$ renpy.pause(1.0, hard=True)
m "This place is nice, next to the sea, let's settle here..."
p "Hey Nikki, let's go for a swim!"
s "Not right now [name], I need to work on my tan."
m "Mmmh, I wouldn't mind a nice refreshing drink right now, but I forgot to bring anything..."

label BeachChoice:
menu:
    "Ask Nikki if she wants help putting lotion on her back":
        show tiniwiniryannikki      
        p "Hey Nikki, I could help you put some lotion on your back if you want..."
        s "Hmm, OK, But don't get any funny ideas you perv!"
        jump NikkiLotion
    "Ask Nancy if she wants you to get her a drink from the beach bar" if (momdrink == False):
        show tiniwiniryanmom
        p "Nancy, I could get you something from the beach bar I saw when we arrived..."
        m "Yes, that would be lovely [name], thanks."
        jump BeachBar01
    "Well, I'm not sitting here doing nothing. I'll explore the beach.":
        jump ExploreBeach


label BeachBar01:
play music "Sounds/tropicalmusic.mp3"
label BeachBar02:
scene beachbar01 with dissolve
$ renpy.pause(1.0, hard=True)
bb "Aloha, welcome to Tini-Wini-Bikini Beach bar!"
menu:
    "Chat with her":
        jump ChatBeachBar
    "Buy something":
        jump BuyBeachBar        
    "Leave":
        jump NancyDrink

label ChatBeachBar:
menu:    
    "Hey, fancy some sex on the beach, it's on the house!":
        scene beachbar03
        bb "Oh, I never heard this joke, like never...really."
        jump BeachBar02
    "I'm new in town and I don't know my way around that much.":
        scene beachbar03
        bb "There's a nudist beach further down the coast, it's called Randy Beach."
        bb "A boy in your shape... You're sure to be a hit with the ladies!"
        $ discoverrandybeach = True
        show addedlocation:
            xalign 0.3 yalign 0.3
            linear 1.0 yalign 0.1
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide addedlocation
        jump BeachBar02

label BuyBeachBar:
menu:    
    "Non-alcoholic juice cocktail (3$)" if (money >= 3):
        scene beachbar02
        $ money -= 3
        bb "Here you are, enjoy our refreshing drink!"
        $ momnonalcoholic = True
        jump BeachBar02
    "Alcoholic juice cocktail (6$)" if (money >= 6):
        bb "Aren't you a bit too young to buy that?"
        menu:            
            "It's not for me, it's for my landlady.":
                if momboughtdrink == True:
                    bb "Your landlady already came and bought a drink..."
                    jump BeachBar02
                scene beachbar02
                bb "Alright, hope she enjoys our \"Cock on the Rock\" cocktail then!"
                $ money -= 6
                $ momalcoholic = True
                jump BeachBar02
            "I'm, like, 18 or something (just like every character in this game), I swear!":
                bb "Yeah, right. Come back when you grow some pubic hair!"
                jump BeachBar02
    "I don't have enough money to buy anything here." if (money <=2):
        bb "Be gone, poor peasant!"
        p "Gee, what a bitch..."
        jump BeachBar02
    "I don't want to buy anything after all...":
        bb "Pfff, another customer who's wasting my time..."
        jump BeachBar02

label NikkiLotion:
scene nikkilotion01 with dissolve
$ renpy.pause(1.0, hard=True)
label SisLotion01:
$ sislotionmiddlefirst = False
p "Where should I start?"
menu:
    "Her arse":
        jump SisLotionbad
    "Her middle back":
        $ sislotionmiddlefirst = True
        jump SisLotion03
    "Her upper back" if (sislotionmiddlefirst == False):
        jump SisLotion02

label SisLotion02:
play sound "Sounds/moaning.mp3"
scene nikkilotion02 with dissolve
$ renpy.pause(1.0, hard=True)
s "Yeah, just like that...Mmhh..."
p "Where should I put lotion next?"
menu:
    "Her arse":
        jump SisLotionbad
    "Her middle back" if (sislotionmiddlefirst == False):
        jump SisLotion03
    "Tell her you're done" if (sislotionmiddlefirst == True):
        jump SisLotion05
            
label SisLotion03:
play sound "Sounds/moaning.mp3"
scene nikkilotion03 with dissolve
$ renpy.pause(1.0, hard=True)
s "Yeah, just like that...Mmhh..."
p "Where should I put lotion next?"
menu:
    "Her arse":
        if (sislotionmiddlefirst == True):
            jump SisLotionbad
        if (sislotionmiddlefirst == False):
            jump SisLotionGood
    "Tell her you're done" if (sislotionmiddlefirst == False):
        jump SisLotion05
    "Her upper back" if (sislotionmiddlefirst == True):
        jump SisLotion02

label SisLotionbad:
scene nikkilotionbad with dissolve
$ renpy.pause(1.0, hard=True)
s "What the hell do you think you're doing?"
if (sislotionattempt == False):
    p "Sorry, my hands slipped..."
    s "Try again and don't screw up this time!"
    $ sislotionattempt = True
    jump SisLotion01
else:
    s "That's it, I 'm done with this, you can't do anything right! Go away!"
    $ lust_points[17] -=1
    $ score -=1
    show lustminus01:
        xalign 0.6 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/less.mp3"
    $ renpy.pause(2, hard=True)
    hide lustminus01
    p "But...What..?"
    jump ExploreBeach

label SisLotion05:
scene nikkilotiondone with dissolve
$ renpy.pause(1.0, hard=True)
p "See, I'm not like, a total perv like you keep saying."
s "That hard bulge in your trunks says otherwise....(wink)"
p "Oooh...That thing has a mind of its own..."
s "Ok, thanks [name]... You did OK I guess."
jump ExploreBeach

label SisLotionGood:
play sound "Sounds/moaning.mp3"
scene nikkilotion04 with dissolve
s "Ooh, yes...that's nice...Mmhh..."
p "She doesn't seem to mind... Wow, her arse is so tight and muscular..."
s "Ok, that's enough, you put enough lotion everywhere... Thanks [name]!"
$ lust_points[17] +=1
$ score +=1
show lust01:
    xalign 0.6 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
scene nikkilotionhappy with dissolve
$ renpy.pause(1.0, hard=True)
p "See, I'm not like, a total perv like you keep saying."
s "That hard bulge in your trunks says otherwise....(wink)"
p "Oooh...That thing has a mind of its own..."
s "But you did well [name]...I like how you...well, you know..."
jump ExploreBeach

label BeachMeet01:
stop music
play music "Sounds/oceanwaves.mp3"
scene beachnancydrink with dissolve
$ renpy.pause(1.0, hard=True)
m "Oh, there you are!"
m "Now be both on your best behavior Nikki and [name]. The head of the parents' association is coming to have a chat with me."
scene beachmeet01 with dissolve
$ renpy.pause(1.0, hard=True)
m "She contacted me when aunt Debby told her we had arrived. We arranged to meet here at 5pm. I think it's them arriving..."
scene beachmeet02 with dissolve
$ renpy.pause(1.0, hard=True)
an "Ms Johnson? I'm Anna, nice to meet you and welcome to Veri-Bosti Island!"
m "You can call me Nancy. Nice to meet you too, Anna."
scene beachmeet03 with dissolve
$ renpy.pause(1.0, hard=True)
an "I wanted to give you the head's up on the school your children will be attending..."
an "Hardcox High is the only private school on the island so it is important you understand... yadda...yadda...yadda...blablabla..."
s "Wow, that boy is at our school? Mmmh, he looks like a total hunk."
p "Pfff, he looks like a complete douchebag I'd say."
j "Hey you, BOY..."
p "Who are you calling \"boy\", BOY?"
scene beachchallenger01 with dissolve
$ renpy.pause(1.0, hard=True)
j "Oh, you think you're so tough don't you. Well, I'm the school stud, so show some goddam RESPECT or I'll beat you up!"
scene beachchallenger02
$ renpy.pause(1.0, hard=True)
p "You don't scare me, I'll beat the crap out of you!"
j "Oh Yeah, gimme me a break, you pathetic little boy!"
p "No, you're the boy here, I'm da man!"
j "What? I'm DA MAN! You're nuthing you worm!"
window hide
show beachchallengernikki with vpunch
play sound "Sounds/scream.mp3"
$ renpy.pause(2, hard=True)
s "Hey, you two morons, stop it, I can't even hear myself thinking!"
scene beachchallengernikki01 with dissolve
$ renpy.pause(1.0, hard=True)
j "Well hello there... I'm José, we'll be in the same class, anything you need, I am your servant melady..."
scene beachchallengernikki02
$ renpy.pause(1.0, hard=True)
s "Ooh, that's so nice of you, I'm Nikki, sssooo glad to meet you José! (wink)"
$ lust_pointsB[17] +=2
show challengerlustplus02:
    xalign 0.55 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide challengerlustplus02
scene beachchallengernikki03
$ renpy.pause(1.0, hard=True)
p "You talking to my landlady's daughter? You talking to my landlady's daughter?"
scene beachchallengernikki04
$ renpy.pause(1.0, hard=True)
j "Yeah, I'm talking to your charming landlady's daughter so shut the fuck up boy!"
p "That's it, I'm gonna beat the shit out of you!"
scene beachchallengernikki05
$ renpy.pause(1.0, hard=True)
s "Stop it you two, settle your differences some other way! I'm leaving, I can't stand all this bickering!"
scene beachchallenger01 with dissolve
$ renpy.pause(1.0, hard=True)
j "OK, OK... How about that then. You and I, boy..."
show beachchallenger01b
p "I'm not a boy!"
hide beachchallenger01b
show beachchallenger01c
j "You and I... a duel..."
j "Whoever wins is the school stud for the rest of the year and the loser has to bow down to the winner's superior virility."
hide beachchallenger01c
show beachchallenger01b
p "Fine, I'll show you who the REAL stud is!"
hide beachchallenger01b
show beachchallenger01c
j "(chuckle)... Same time, same place next week, I will be crowned the winner, mark my words [name]!"
j "Because I will have fucked FIRST more girls than you this week!"
hide beachchallenger01c
show beachchallenger01b
p "Yeah, whatever, I'm up for your stupid challenge! I'll fuck them all, I'll conquer the island with my dong!"
hide beachchallenger01b
show beachchallenger01c
j "Remember, you must be the FIRST of us two to fuck a girl for it to count, boy."
j "We'll send each other a pic from our phones to prove the deed has been done..."
show screen calendar
hide beachchallenger01c
show beachchallenger01b
p "Hey, why did a calendar just appear above your head???"
hide beachchallenger01b
show beachchallenger01c
j "That's because the clock is now TICKING. See you next Sunday LOSER! AH AH AH!"
scene beachmeet04 with dissolve
$ renpy.pause(1.0, hard=True)
an "...So there you are Nancy, it's everything you need to know. Don't hesitate to call me if you have any question."
m "Thank you very much Anna, this was very helpful. I think your son will be in my daughter's class, is that right?"
j "Yes ma'am, and I'll take good care of her, I promise..."
m "What a nice polite boy you have raised Anna... He must be very popular with the girls..."
$ lust_pointsB[16] +=1
show challengerlustplus01:
    xalign 0.15 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide challengerlustplus01
an "Yes, and I can assure you that this can be more than a handful sometimes...Ah ah...But I love him, he's my big strong boy..."
an "Speaking of which... Your son has a very impressive physique for his age I must say..."
$ score += 1
$ lust_points[0] +=1
show lust01:
    xalign 0.35 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
menu:
    "I train a lot Ms Longrod. My body and my soul.":
            an "I see. A bodybuilding intellectual."
    "Yeah, I'm already bigger than that pindick son of yours!":
            an "Don't you dare call my son a pindick!"
            $ lust_points[0] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.35 yalign 0.2
                linear 1.0 yalign 0.4
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            m "I must apologize for my son's behavior... His hormones are out of control lately..."
an "Well, enjoy your stay on the island. Best of luck settling in!"
m "Thank you ssoo much for coming by before the start of the school week tomorrow, that was very kind of you."
an "Oh that was nothing, I love hanging out on Tini-Wini-Bikini Beach on weekends anyway. Bye!"
m "OK, kids, it's getting late, time to go home."
jump TravelBeachBack01
    
label NancyDrink:
stop music
play music "Sounds/oceanwaves.mp3"
scene beachnancydrink with dissolve
$ renpy.pause(1.0, hard=True)
m "Oh, there you are!"
if (momboughtdrink == True) and ((momnonalcoholic == True) or (momalcoholic == True)):
    p "I bought you a drink Nancy!"
    m "Oh, sweetie, I already bought myself a nice \"Cock on the Rock\" cocktail... So you can have your drink."
    if (momnonalcoholic == True):
        p "Ah...eh...OK. (damn, I just wasted 5 bucks...)"
    if (momalcoholic == True):
        p "Ah...eh...OK. (damn, I just wasted 10 bucks...)"    
    jump ExploreBeach
elif (momnonalcoholic == True):
    p "I bought you a drink Nancy!"
    m "Oh, thank you sweetie, that will be very refreshing indeed..."
    p "What, no lust point added for that? What a rip-off!"
    jump ExploreBeach
elif (momalcoholic == True):
    p "I bought you a drink Nancy!"
    m "Oh, thank you sweetie, that will be very enjoyable indeed.."
    m "Mmmh, it has alcohol in it... I love it... Hips..."
    menu:
        "Hang around":
            scene beachnancydrunk with dissolve
            $ renpy.pause(1.0, hard=True)
            p "Damn, Nancy is losing all her inhibition..."
            p "Too bad Nikki is around, I'd better not hang around too long..."
            jump ExploreBeach
        "Don't hang around and explore the beach":
            jump ExploreBeach

label ExploreBeach:
$ momboughtdrink = True
p "Where should I go?"
menu:
    "Go to the beach bar":
        jump BeachBar01
    "Walk along the beach" if (chiyoseen == False):
        jump ChiyoBeach01
    "Go to Randy Beach" if ((discoverrandybeach == True) and (randybeachseen == False)):
        jump RandyBeach01
    "Go back to Nancy and Nikki" if (beachstuffseen >=2):
        jump BeachMeet01

label ChiyoBeach01:
stop music
play music "Sounds/oceanwaves.mp3"
scene chiyobeach01 with dissolve
$ renpy.pause(1.0, hard=True)
$ chiyoseen = True
$ beachstuffseen += 1
p "There's a secluded part of the beach where a woman is lying sunbathing topless."
menu:
    "Hum (cough)...":
        jump ChiyoBeach02
    "I don't think it's allowed to be topless on this beach ma'am!...":
        jump ChiyoBeach03
    "Spectacular view, I wish more women like you would go topless...":
        jump ChiyoBeach04

label ChiyoBeach02:
scene chiyobeach02 with dissolve
$ renpy.pause(1.0, hard=True)
cy "What? Oh, hello there boy."
p "Do you need anything? With this sun, you need more sunscreen on you..."
cy "Well, thank you, I was just about to put on some more lotion ..."
jump ChiyoLotion

label ChiyoBeach03:
scene chiyobeach03 with dissolve
$ renpy.pause(1.0, hard=True)
cy "Please don't tell anyone! My... top went missing during a swim...."
menu:
    "Yeah, right, who's gonna believe that story!":
        cy "I'll give you ten dollars to shut up!"
        menu:
            "ok, deal!":
                $ money += 10
                jump ExploreBeach
            "No deal. I'm telling the lifeguards...Unless":
                cy "Unless what?"
                p "Unless I can see you pour some lotion on those fat titties of yours."
                cy "You filthy pervert... OK, I accept... Because you're such a pervert."
                $ lust_points[3] += 2
                $ score += 2
                show lust02:
                    xalign 0.25 yalign 0.4
                    linear 1.0 yalign 0.2
                play sound "Sounds/more.mp3"
                $ renpy.pause(2, hard=True)
                hide lust02
                jump ChiyoLotion
    "I don't care, I'm telling the authorities...unless...":
        cy "Unless what?"
        p "Unless I can see you pour some lotion on those fat titties of yours."
        cy "You filthy pervert... OK, I accept...Because you're such a pervert."
        $ lust_points[3] += 2
        $ score += 2
        show lust02:
            xalign 0.25 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
        jump ChiyoLotion
    "Fair enough, I'll leave you alone then...":
            cy "Thank you for being so understanding... Maybe next time...We can do something together..."
            jump ExploreBeach

label ChiyoBeach04:
scene chiyobeach04 with dissolve
$ renpy.pause(1.0, hard=True)
cy "Oh, hello there... You think so? They're not too big?"
p "Of course not, they're perfect! Round and firm, so yummy..."
$ lust_points[3] += 1
$ score += 1
show lust01:
     xalign 0.3 yalign 0.4
     linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
cy "Well, don't get too cocky young man. I was just about to put on some more lotion on them. Wanna watch?"
p "Of course!"
jump ChiyoLotion

label ChiyoLotion:
scene chiyobeach05 with dissolve
$ renpy.pause(1.0, hard=True)
cy "Mmh, I love the feel of this lotion sliding down my breasts..."
cy "You like watching me play with my big tits don't ya?"
menu:
    "Let me help you spread that cream all over your body...":
        cy "You can watch but you can't touch...That's the rule..."
        jump ChiyoLotion02
    "I'm gonna add my own cream to that if you don't mind. Let me get my hardening dong out for you...":
        cy "No fucking way, keep that thing out of my sight! Who do you think I am?"
        $ lust_points[3] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.3 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        cy "But you can watch... While your cock gets painfully hard..."
        jump ChiyoLotion02
    "Yeah, you're making me so horny!":
        cy "That's good, I like making boys horny... Especially BIG boys like you!"
        $ lust_points[3] += 1
        $ score += 1
        show lust01:
            xalign 0.25 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        jump ChiyoLotion02

label ChiyoLotion02:
play sound "Sounds/chiyolotion.mp3"
scene chiyolotion with dissolve
$ renpy.pause(1.0, hard=True)
cy "Watch those shiny big tits... I love showing off my body to horny boys..."
p "I'm getting a massive boner watching you, please let me feel them..."
cy "NO...BAD boy! No touching, you can only watch...a bit longer..."
$ renpy.pause(2.0, hard=True)
cy "That's it, I'm done... Off you go... Hee hee hee..."
p "WTF? What a teasing bitch!"
jump ExploreBeach

label RandyBeach01:
stop sound
stop music
scene randybeach01 with dissolve
play music "Sounds/randybeachsound.mp3"
$ renpy.pause(1.0, hard=True)
$ randybeachseen = True
$ beachstuffseen += 1
p "I guess this is it. I'd better take my speedos off."
window hide
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)

label RandyBeach01b:
p "I see three parasols but I can't see the people behind them...Which one should I go to?"
menu:
    "Go to the closest red parasol on the right" if (seenparasol01 == False):
        jump RandyBeachParasol01
    "Go to the middle orange parasol" if (seenparasol02 == False):
        jump RandyBeachParasol02
    "Go to the furthest red parasol on the left"if (seenparasol03== False):
        jump RandyBeachParasol03
    "Leave Randy Beach":
        jump ExploreBeach

label RandyBeachParasol01:
$ seenparasol01 = True
scene randybeacholdbackground with dissolve
show randybeacholdwoman01
show randybeachparasol01
$ renpy.pause(2.0, hard=True)
p "Mmmh, legs spread wide..."
window hide
hide randybeachparasol01 with moveoutright
play sound "Sounds/smoochykiss.mp3"
$ renpy.pause(0.3, hard=True)
hide randybeacholdwoman01
show randybeacholdwoman02
$ renpy.pause(0.3, hard=True)
hide randybeacholdwoman02
show randybeacholdwoman01
$ renpy.pause(0.3, hard=True)
hide randybeacholdwoman01
show randybeacholdwoman02
$ renpy.pause(0.3, hard=True)
hide randybeacholdwoman02
show randybeacholdwoman01
$ renpy.pause(0.3, hard=True)
play sound "Sounds/smoochykiss.mp3"
hide randybeacholdwoman01
show randybeacholdwoman02
$ renpy.pause(0.3, hard=True)
hide randybeacholdwoman02
show randybeacholdwoman01
$ renpy.pause(0.3, hard=True)
hide randybeacholdwoman01
show randybeacholdwoman02
$ renpy.pause(0.3, hard=True)
hide randybeacholdwoman02
show randybeacholdwoman01
$ renpy.pause(0.3, hard=True)
ow "Come to mama boy!"
p "OMG, run for your life, run for your LIFE!"
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
jump RandyBeach01b

label RandyBeachParasol02:
$ seenparasol02 = True
scene randybeachsandy01
show randybeachparasol02
$ renpy.pause(2.0, hard=True)
p "Someone's on their back, hope it's a nice arse..."
window hide
hide randybeachparasol02 with moveoutleft
$ renpy.pause(1.0, hard=True)
sa "Hi there, sorry but I'm busy reading a book..."
menu:
    "Please don't mind me, I'm just admiring that sumptuous arse of yours":
        sa "What??? That's disgusting! Go away boy!"
        jump Parasol02out
    "Oh, and what are you reading may I inquire?":
        sa "War and Peace..."
        menu:
            "...By Leon Tolstoy. Yes, an epic historical masterpiece I must say.":
                jump RandyBeachSandyChat
            "Well, this place is peaceful but I could certainly wage war on that fat arse of yours.":
                sa "What??? That's disgusting! Go away boy!"
                jump Parasol02out
    "BORING! Why don't do you enjoy the view with me by your side?":
        sa "Because my book is more interesting than your pointless chitchat. Go away."
        $ seenparasol02 = False
        jump Parasol02out    

label RandyBeachSandyChat:
sa "Oh, wow, you're like really smart! On top of having a gorgeous body..."
sa "My name is Sandy...Nice to meet you...?"
p "[name]. My pleasure Sandy. \"There once was a girl named Sandy, who liked to go topless on Randy...Beach.\""
sa "Hee hee, you're a poet too..."
$ lust_points[19] +=1
$ score += 1
show lust01:
    xalign 0.2 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
sa "Come and sit next to me and let's admire the view..."
scene  randybeachsandy02 with dissolve
$ renpy.pause(1.0, hard=True)
sa "Isn't it wonderful? The curves of the waves as they rumble ashore..."
p "Oh yeah, the curves are beautiful..."
menu:
    "Hold her hand":
        jump SandyHoldHands
    "Feel up her breast":
        jump SandyFeelBreast

label SandyHoldHands:
show randybeachsandy03 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/distantfuck.mp3"
sa "It's beautiful in the late afternoon, so quiet and peaceful..."
play sound "Sounds/distantfuck.mp3"
p "Hmm, not so quiet, some people seem to be having some raunchy fun not far away..."
sa "Oh God, these two have been at it for hours! I didn't even know it was possible..."
menu:
    "Yeah, this is outrageous. These youngsters, no respect for their elders I tell you!":
        sa "Calm down now, this place is called Randy Beach after all...Let them be..."
        jump SandyLateChat01
    "Oh, it's possible... If the guy is a total stud...":
        sa "Oh, and you know that because..."
        p "...I'm a total stud..."
        scene randybeachsandy05 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa "Well, you're certainly way bigger than my last boyfriend..."
        $ lust_points[19] +=1
        $ score += 1
        show lust01:
            xalign 0.6 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust01
        sa "He was sssoo tiny, and spent his whole evenings being a whiny little bitch troll on f95zone.com..."
        p "I decline all legal responsibility for what you just said."
        sa "I want to see this monster get hard as a rock..."
        if (stamina >= 1):
            jump SandyTease
        else:
            p "I...I can't...Get a hardon.... NNOOOOO!"
            sa "That's a pity...And quite offensive actually."
            $ lust_points[19] -=1
            $ score -= 1
            show lustminus01:
                xalign 0.8 yalign 0.4
                linear 1.0 yalign 0.2
            play sound "Sounds/less.mp3"
            $ renpy.pause(2, hard=True)
            hide lustminus01
            jump SandyLateChat01
     
label SandyFeelBreast:
show randybeachsandy04 with dissolve
$ renpy.pause(1.0, hard=True)
sa "What are you doing? You're going...too fast... Why do men always have to spoil romantic moments?"
$ lust_points[19] -=1
$ score -= 1
show lustminus01:
    xalign 0.6 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/less.mp3"
$ renpy.pause(2, hard=True)
hide lustminus01
menu:
    "Don't be so prude, this is a nudist beach after all...":
        sa "I'm not \"prude\"! You don't even know me... I need to go, it's getting late. I'll see you around."
        p "But...I was about to get a hardon...! It's not fair...."
        jump Parasol02out
    "I'm so sorry Sandy...Here, let's hold hands and admiring the view.":
        sa "That's better..."
        jump SandyHoldHands
  
label SandyTease:
scene randybeachsandy06 with dissolve
$ renpy.pause(1.0, hard=True)
sa "Damn [name], it's so big... You like it when I tease your cockhead with my fingers like that?"
p "Yes! It's so excruciating... Puff... Keep going, I'm gonna blow anytime now..."
sa "I want this to last a little bit longer... What would be the fun otherwise?"
p "Oh shit Sandy, I can't....This is too much..."
sa "OK, I'll jack that monstercock off until you get the release you deserve..."
scene
play sound "Sounds/jackoff.mp3"
scene randybeachsandywank01 with dissolve
$ renpy.pause(1.0, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank02
$ renpy.pause(0.5, hard=True)
scene randybeachsandywank01
$ renpy.pause(0.5, hard=True)
p "Goddamn...I'm CUMMING!!!!"
play sound "Sounds/cumming.mp3"
scene randybeachsandycum
$ renpy.pause(1.0, hard=True)
sa "Mmmh, look at all that young spunk flying everywhere.. Gimme more, I want MORE..."
p "FUCKKKK...Still CUMMING!!!!"
$ lust_points[19] +=2
$ score += 2
show lust02:
    xalign 0.6 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
sa "We're gonna need to get cleaned up with the mess you made!..."
$ stamina -=1
show staminaminus01:
    xalign 0.3 yalign 0.6
    linear 1.0 yalign 0.8
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
hide staminaminus01
jump SandyLateChat02

label SandyLateChat01:
scene randybeachsandy03 with dissolve
$ renpy.pause(1.0, hard=True)
sa "I should go now, it's getting late...I hope to see you again..."
sa "But before that, kiss me tenderly..."
play sound "Sounds/kissing.mp3"
scene randybeachsandykiss with dissolve
$ renpy.pause(1.0, hard=True)
$ lust_points[19] +=1
$ score += 1
show lust01:
    xalign 0.8 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
p "Where will you be?"
sa "I'll be around...We'll meet again my Prince Charming..."
jump Parasol02out

label SandyLateChat02:
scene randybeachsandy03b with dissolve
$ renpy.pause(1.0, hard=True)
sa "I should go now, it's getting late...I hope to see you again..."
sa "But before that, kiss me tenderly..."
play sound "Sounds/kissing.mp3"
scene randybeachsandykisscum with dissolve
$ renpy.pause(1.0, hard=True)
$ lust_points[19] +=1
$ score += 1
show lust01:
    xalign 0.8 yalign 0.4
    linear 1.0 yalign 0.2
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust01
p "Where will you be?"
sa "I'll be around...We'll meet again my Prince Charming..."
jump Parasol02out

label Parasol02out:
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeach01b
 
label RandyBeachParasol03:
$ seenparasol03 = True
scene randybeachcouple01
show randybeachparasol03
$ renpy.pause(1.0, hard=True)
p "Now let's see what's hiding behind this parasol..."
window hide
hide randybeachparasol03 with moveoutright
$ renpy.pause(1.0, hard=True)
rc "Hey, can't we have some privacy here? It's called \"Randy Beach\" for a reason!"
menu:
    "Well, I'm randy too!":
        jump RandyBeachCouple02
    "Sorry ma'am, please continue your sexual activities with that young boy undisturbed.":
        rc "Whatever, fuck off pervert!"
        jump Parasol03out
    "Your boyfriend has such a small dick, it's laughable.":
        rc "Yeah, as if. My boyfriend is a total stud and we'll prove it."
        rb "Watch and learn boy as I fuck my girlfriend senseless with my young monstercock!"
        jump RandyBeachCoupleFuck
        
label RandyBeachCouple02:
rc "Mmh, well maybe you could prove yourself useful..."
rb "What do you have in mind baby?"
rc "I would never let anyone else other than you take my tight pussy, but he can stick his cock in my arse while I ride your donkey-dick..."
rb "How does that sound boy, ready for some threesome fun with my girlfriend?"
menu:
    "No, I don't settle for less than a warm pussy...":
        rc "No way, fuck off then!"
        jump Parasol03out
    "Yeah, count me in!":
        jump RandyBeachCoupleThreesome

label RandyBeachCoupleFuck:

play music "Sounds/randybeachchickmoaning.mp3"
scene randybeachcouplefuck with dissolve
$ renpy.pause(1.0, hard=True)
rc "Oh God, you fuck me so good with that huge cock of yours!"
rb "Are you getting this, that's how you give a woman plenty of pleasure!"
rb "Now I'm gonna dump a massive load of my virile cum inside her and all over her back. Watch!"
stop music
play music "Sounds/randybeachsound.mp3"
scene randybeachcouplecum with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/randyboycumming.mp3"
rb "Ah FUCK, SSOO good!"
rc "Look at all those massive cumshots flying everywhere after he totally filled me with ounces of boycream already!"
rb "See how much I come? And you know what? I'm still HARD and READY to fuck my girlfriend some more!"
rc "Mmmh, such a STUD! Are you a stud? How about you come and fuck my arse and show me if you are?"
rb "How does that sound boy, ready for some threesome fun with my girlfriend?"
menu:
    "Yeah, count me in!":
        jump RandyBeachCoupleThreesome
    "No, I don't settle for less than a warm pussy...":
        rc "No way you're touching my pussy, that's reserved for my STUD, fuck off then!"
        jump Parasol03out

label RandyBeachCoupleThreesome:
scene randybeachcouplethreesome with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/threesomefuck.mp3"
rc "Oh Lord have mercy! Two GIANT young cocks in my holes... t...ttooo fucking much!"
p "Arse...gripping...so tight... can't..hold...BACK!"

scene randybeachcouplethreesomecum with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(2.0, hard=True)
p "FUCK, you made me cum in no time, can't stop spewing my sauce! AAAH!"
rc "Hey, watch out, I didn't say you could spew your filthy scum all over me!"
rb "Dude, you don't know how to treat girls with respect... "
rb "Learn from me, I'm still pounding her sweet pussy and I'll do it all afternoon until she comes over and over again on my giant boymeat..."
p "Damn, I'm totally spent, her arse was gripping too tight, she totally sucked the cum out of my balls!"
$ backdoor += 1
if (stamina <=1):
    $ stamina -=1
    show staminaminus01:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus01
else:
    $ stamina -=2
    show staminaminus02:
        xalign 0.2 yalign 0.2
        linear 1.0 yalign 0.4
    play sound "Sounds/panting.mp3"
    $ renpy.pause(2, hard=True)
    hide staminaminus02
$ extras += 1
$ threesome += 1
rc "Can't keep it up? Then you're useless to me, leave us alone while I ride my horse-hung boyfriend to countless orgasms!"
rb "Don't worry baby, I've got a few more loads in me, we can keep at it for hours!"
rc "Oh, I'm counting on it stud, I want to coax at least a dozen more massive loads of cum from that stallion cock of yours before the end of the day!"
p "Jeezus, what a crazy nympho, I'm out of here..."
jump Parasol03out

label Parasol03out:
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
jump RandyBeach01b

label TravelBeachBack01:
scene cardrive01 with dissolve
$ renpy.pause(1.0, hard=True)
play music "Sounds/cardrive.mp3"
m "Well, did you two have fun at the beach?"
s "Yeah, thanks mom, I wished we could have stayed longer."
if (auntfirst == False):
    m "We had to get back to see your aunt."
else:
    m "It was getting late, I need to prepare dinner."
    p "How do we get back there without you driving us?"
    m "You can take the bus. There's a bus stop not far from our house and it's free to get anywhere on the island."
stop music 
$ hour += 1        
if (auntfirst == False):
    jump AuntDebby01
else:
    jump Evening01
    
label Evening01:
scene ryanbedroomday with dissolve
$ renpy.pause(1.0, hard=True)
$ locroom = True
p "Back home... What should I do?..."
label RyanRoom02b:
menu:
    "Go back to my room" if (locroom == False):
        jump Evening01
    "Do some heavy bodybuilding (+2hrs)" if (locroom == True):
        p "That would take at least two hours, I don't have time for that, dinner is at 8pm..."
        jump RyanRoom02b
    "Go to Nikki's room" if (eveningsisroomseen == False):
        jump NikkiRoom02
    "Go to Nancy's room" if (eveningmomroomseen == False):
        jump NancyRoom02
    "Go to the swimming pool":
        jump PoolNikki01
    "Admire my own body in the mirror."if (locroom == True):
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump RyanRoom02b

label NikkiRoom02:
$ eveningsisroomseen = True
$ locroom = False
scene nikkibedroom01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Nikki is not in her room... I wonder where she went..."
menu:
    "Snoop around":
        jump NikkiBedroomSnoop  
    "Go somewhere else":
        jump RyanRoom02b

label NikkiBedroomSnoop:
p "There might be an interesting item hidden somewhere... Time to snoop around..."
p "But I have a limited amount of time to look for it, Nikki might come back any minute."
p "Every time I search a hotspot that is empty (by clicking on it), I will lose additional time too, so I'd better be quick!"
play music "Sounds/snooping.mp3"
call screen sisbedroomsnoop
stop music
p "I didn't find anything..."
p "I guess Nikki doesn't have anything of interest in her room..."
p "This was just a test to get me acquainted with how \"snooping around\" works..."
p "Next time, I'll be like a thief in the night..."
jump RyanRoom02b

label NancyRoom02:
scene nancybedroomday with dissolve
$ renpy.pause(1.0, hard=True)
$ eveningmomroomseen = True
$ locroom = False
p "Nancy's room is so clean and tidy. Not like mine."
p "Nancy is not around cos she's preparing dinner. I'm not helping her at all like any normal teenage boy."
jump RyanRoom02b

label PoolNikki01:
stop music
play music "Sounds/gardensound.mp3"
play sound "Sounds/swimming.mp3"
scene poolnikki01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Nikki is in the pool...But I don't have my swimming trunks with me..."
s "Our pool is ssoo great! And swimming really helps develop muscles without stress on joints and bones..."
p "I prefer weight-lifting. That's for real men."
s "You know nothing [name]."
scene poolnikki02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Wow, Nikki is really hot... I really need to fuck her this week if I want to become the school stud..."
s "What was that? What were you saying?"
p "Hang on...When I think to myself, people can hear me???"
s "I hear you cos you're opening your mouth and actually speaking you idiot."
s "Maybe you should learn to train your head muscle a bit more and you'll be able to actually think inside your head..."
p "I'd better watch out. I think Nikki might be a witch or something... Anyway, it's getting late and it's time for dinner."
$ hour += 1
stop sound
jump Dinner01

label Dinner01:
stop music
scene dinner01 with dissolve
$ renpy.pause(1.0, hard=True)
m "Enjoy your meal kids!"
p "Thanks Nancy, that's my favourite!"
m "What's the matter Nikki, you seem preoccupied...?"
s "I can't find my earrings, I think I lost them, but I don't know where to look."
menu:
    "You don't need earrings, you look like a boy and boys don't wear them.":
        show nikkicrying
        "Nikki starts crying"
        $ lust_points[17] -=1
        $ score -= 1
        show lustminus01:
            xalign 0.35 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        m "What are you saying? Nikki is very feminine!"
        s "Sniff...I...I'll ask that...sniff...nice boy José to help me then!"
        $ lust_pointsB[17] +=1
        show challengerlustplus01:
            xalign 0.35 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide challengerlustplus01
    "Think about where you last saw them.":
        s "Mmh, I didn't have them on the beach, so they must be in my room somewhere..."
        p "Then we'll start there. I'll help you find them."
        show nikkihappy
        s "Really, that's so sweet of you [name]!"
        $ lust_points[17] += 2
        $ score += 2
        show lust02:
            xalign 0.35 yalign 0.4
            linear 1.0 yalign 0.2
        play sound "Sounds/more.mp3"
        $ renpy.pause(2, hard=True)
        hide lust02
        $ nikkihelp = True
    "If you can't remember where you lost them , it's pointless to look for them.":
        s "But I liked them so much."
        m "We'll get you some other earrings downtown Nikki. Now eat up your dinner before it gets cold."
"You finish cleaning up the dishes with Nancy and Nikki and head for your room."
$ hour += 1
$ lustaddedB = 3
call Challenger from _call_Challenger
call Challenger from _call_Challenger_1
$ lustaddedB = 2
call Challenger from _call_Challenger_2
call Challenger from _call_Challenger_3

label RyanRoom02:
stop music
scene ryanbedroomnight with dissolve
$ locroom = True
$ renpy.pause(1.0, hard=True)
if (hour == 23) and (nightbathroomseen == True) and (nightmomroomseen == True) and (computerchecked == True):
    $ hour += 1
if (hour == 24) or (hour == 1):
    p "I should really go to sleep now, tomorrow is my first day of school..."
    jump Sleep01
p "mmmh, what should I do?"
menu:
    "Go and help Nikki find her earrings" if (nikkihelp == True) and (nikkihelped == False) and (hour <= 22):
        jump NikkiRoom03
    "Do some heavy bodybuilding (+2hrs)":    
        if (workout == True):
            "You already trained today."
            jump RyanRoom02
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
            if (hour == 23):
                $ day = 2
                $ hour = 1 
            else:
                $ hour += 2 
            jump RyanRoom02
    "Check the computer":
        jump Computer
    "Admire my body in the mirror":
        scene ryanmirror
        p "Fuck yeah, I'm da man, I'm DA MAN."
        "Your confidence is boosted by +1. Too bad that's not an actual stat in the game."
        jump RyanRoom02
    "Go somewhere else" if (hour >= 22):
        jump HouseChoice02

label Computer:
scene ryancomputer with dissolve
play sound "Sounds/computeron.mp3"
$ renpy.pause(1.0, hard=True)
p "My computer downloaded two new Google apps..."
label Computer02:
scene ryancomputer
$ renpy.pause(1.0, hard=True)
menu:
    "Check the map":
        jump Map
    "Check the stats":
        jump Stats
    "Turn the computer off":
        jump RyanRoom02

label Map:
play sound "Sounds/mouseclick.mp3"
hide screen statsbackground
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
p "This shows all the places I know on Veri-Bosti Island..."
show screen statsbackground
jump Computer02

label Stats:
play sound "Sounds/mouseclick.mp3"
$ computerchecked = True
scene stats
hide screen statsbackground
show screen statsscreen
$ renpy.pause(1.0, hard=True)
p "This screen shows me some interesting stats. Google satellites must be spying on me to know so much stuff..."
p "On the left, all the babes I could bang on the island and how much they lust for me (green bars) and José (red bars)..."
p "Some I haven't met yet, so their lust for me is zero. I need to get lust up to 10 for a girl to be ready to fuck."
p "Looks like this dickhead of José is also getting some chicks' lust up. I'd better watch out for him."
p "On the right are my vital stats, my strength and my stamina."
p "Stamina is rebooted to 5 every morning."
if (stamina == 5):
    p "I didn't cum at all today so it's still 5. What a waste."
else:
    p "It's gone down because I've been busy emptying my balls today..."
hide screen statsscreen
show screen statsbackground
jump Computer02

label NikkiRoom03:
scene nikkibedroomhelp with dissolve
$ renpy.pause(1.0, hard=True)
$ locroom = False
$ nikkihelped = True
p "I came to help you find your earrings Nikki."
s "I can't find them...sniff...I looked everywhere already..."
p "Did you look under the bed?"
s "Yes, but I couldn't see much. It was too dark."
p "I'll lift the bed for you so you can have a better look..."
scene nikkibedroomhelpbed with dissolve
$ renpy.pause(1.0, hard=True)
p "Piece of cake with my strength, look at that..."
s "I'm looking for my earrings, not your muscles...No, not there...(sigh)."
p "How about the dresser? They might have fallen behind it."
s "It's too heavy, I can't move it. I've got all my clothes and weights in it."
p "Archimedes said the best way to move a piece of furniture is to lift it straight up in the air and not bother emptying it at all."
s "I don't think I had the same physics teacher as you did..."
menu:
    "Attempt to lift the wardrobe like He-man":
        scene nikkibedroomhelpdresser with dissolve
        $ renpy.pause(1.0, hard=True)
        play sound "Sounds/workoutgroan.mp3"
        p "Damn...Too heavy...Can't...lift it!"
        s "You're not as strong as you think you are... You'd better do some more training [name]..."
        $ lust_points[17] -= 1
        $ score -= 1
        show lustminus01:
                xalign 0.05 yalign 0.4
                linear 1.0 yalign 0.6
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        p "This is so humiliating...I'll go back to my room."
        s "I'm too tired to continue searching, I'll go and take a shower."
        jump RyanRoom02        
    "It looks too heavy, look elsewhere for the earrings":
        s "I've looked everywhere already I told you! I'm too tired to continue looking right now, I'm gonna take a shower..."
        p "Sorry we couldn't find them today, I promise to help you tomorrow."
        jump RyanRoom02

label HouseChoice02:
stop music
p "Where should I go at this time of the evening?..."
menu:
    "Go to Nancy's room" if (nightmomroomseen == False):
        jump NancyRoomEvening
    "Go to Nikki's room" if (nightsisroomseen == False):
        jump NikkiRoomEvening 
    "Go to the bathroom" if (nightbathroomseen == False):
        jump BathroomEvening
    "Go back to my room" if (locroom == False):
        jump RyanRoom02

label NikkiRoomEvening:
scene nikkibedroomnight with dissolve
$ renpy.pause(1.0, hard=True)
$ locroom = False
p "Nikki isn't in her room... I wonder where she went..."
$ nightsisroomseen = True
jump HouseChoice02

label NancyRoomEvening:
scene nancysleeping01 with dissolve
$ renpy.pause(1.0, hard=True)
$ locroom = False
$ nightmomroomseen = True
p "Nancy seems to be sound asleep. I guess this trip was tiring."
p "She has such a fine body... Look at that arse..."
menu:
    "Get closer":
        jump NancyRoomEvening02
    "Leave the room":
        jump RyanRoom02

label NancyRoomEvening02:
$ peeping += 1
scene nancysleeping02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Fuck...I can't help myself, I'm getting a boner looking at her hot bod..."
play sound "Sounds/womansigh.mp3"
m "Mmmh....[name]...no...don't....yes..."
p "Did she just say my name? And her hands are down her panties... They look soaking wet."
label NancyRoomEveningMenu:
menu:
    "Pull her panties to the side and finger her":
        jump NancyRoomEvening03
    "Whisper her name and slowly talk dirty to her":
        jump NancyRoomEvening04

label NancyRoomEvening03:
$ nightmomroomseen = True
scene nancysleeping03 with dissolve
$ renpy.pause(1.0, hard=True)
m "Wh..what are you doing [name]? Why are you here?"
menu:
    "I saw a spider crawl into your room and then into your bed...like...REALLY BIG.":
        m "Oh, get rid of it and let me sleep, I'm so...tired."
        p "Sure thing Nancy!"
        p "Phew, that was a close call..."
        $ hour += 1
        jump RyanRoom02
    "You were fingering yourself and whispering my name...":
        m "WHAT? That's...just crazy... I...would never do that!"
        m "Anyway, why are you in MY room at night? Go to your room immediately!"
        $ lust_points[16] -= 1
        $ score -= 1
        show lustminus01:
            xalign 0.6 yalign 0.2
            linear 1.0 yalign 0.4
        play sound "Sounds/less.mp3"
        $ renpy.pause(2, hard=True)
        hide lustminus01
        $ hour += 1
        jump RyanRoom02

label NancyRoomEvening04:
scene nancysleeping04 with dissolve
$ renpy.pause(1.0, hard=True)

p "Nancy...I love you...you want me... my huge cock is ready for you..."
play sound "Sounds/womansigh.mp3"
m "Yes [name]...fuck me...fuck me...with your giant cock...Aaaah..."
$ lust_points[16] +=2
$ score += 2
show lust02:
        xalign 0.7 yalign 0.8
        linear 1.0 yalign 0.6
play sound "Sounds/more.mp3"
$ renpy.pause(2, hard=True)
hide lust02
p "She seems to be enjoying this and dreaming about me... I'd better not push my luck though..."
$ hour += 1
jump RyanRoom02
        
label BathroomEvening:
play music "Sounds/shower.mp3"
scene bathroomdoorclosed with dissolve
$ renpy.pause(1.0, hard=True)
$ locbathroom = True
p "Someone's taking a shower..."
menu:
    "Have a peek":
        jump PeekBathroom
    "Leave":
        jump HouseChoice02

label PeekBathroom:
$ nightbathroomseen = True
$ locroom = False
play sound "Sounds/doorsqueak.mp3"
scene bathroomdooropen with dissolve
$ renpy.pause(1.0, hard=True)
p "Shit, the door is squeaking..."
s "Hey, I'm in the shower, don't get in!"
p "Ah, sorry Nikki...I'm leaving..."
p "Damn, I should try and find a way of stopping that door from squeaking if I want to spy on Nancy or Nikki in the shower like every other MC..."
jump HouseChoice02

label Sleep01:
scene ryansleeping with dissolve
play music "Sounds/ryansnoring.mp3"
$ renpy.pause(1.0, hard=True)
"You fall asleep and dream of your adventures to come..."
$ renpy.pause(2.0, hard=True)

"Your current score (not that it matters) is: {b}[score]{/b} / 20"
if (score <=6):
    "Your ranking: {b}Douchebag{/b}"
elif (score <=10):
    "Your ranking: {b}Noob{/b}"
elif (score <=14):
    "Your ranking: {b}Average Joe{/b}"
elif (score <=17):
    "Your ranking: {b}Hunk{/b}"
else:
    "Your ranking: {b}Babe Magnet{/b}"
stop music

jump Day02

