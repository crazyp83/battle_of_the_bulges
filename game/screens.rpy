################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.95
    ypos 500
    yanchor 0.8

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("CREDITS") action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)

        imagebutton idle "Icons/epicidle.png" hover "Icons/epichover.png" xpos 0 ypos 0 focus_mask True action OpenURL("https://www.patreon.com/epiclust")

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Please follow me on my blog {a=https://epicsizefetish.blogspot.com}Epic Lust{/a} and my {a=https://timdonehy200.deviantart.com}Deviant Art{/a} page")
            text _("")
            text _("Special credits go the following kind women who lent their sexy voices to characters in the game:")
            text _("")
            text _("Principal Sophia Titsworthy's voice: {a=https://www.reddit.com/user/sweetcarolinekisses}SweetCarolineKisses{/a}")
            text _("Nancy's voice: {a=https://www.reddit.com/user/Blonde_Bimbo_Brianna}Blonde_Bimbo_Brianna{/a}")
            text _("Maria's voice: {a=https://twitter.com/@ScarletMoonVA}Karissa Presents{/a}")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600

################################################################################
## Unique Game Screens
################################################################################

     
screen statsbackground():
    zorder 100
    add "Icons/statsbackground.png"
    text "[money]" color "#006600" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at MoneyPosition
    text "[strength]" color "#660000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at StrengthPosition
    text "[stamina]" color "#141452" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at StaminaPosition

screen calendar():
    zorder 99
    add "Icons/timer.png"
    if (day==1):
        add "Icons/day01.png"
    if (day==2):
        add "Icons/day02.png"
    if (day==3):
        add "Icons/day03.png"
    if (day==4):
        add "Icons/day04.png"
    if (day==5):
        add "Icons/day05.png"
    if (day==6):
        add "Icons/day06.png"
    if (day==7):
        add "Icons/day07.png"
    if (day==8):
        add "Icons/day08.png"
    text "[hour]:00" color "#000000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at TimerPosition

screen statsscreen():
    text "[money]" color "#006600" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at MoneyPositionStat    
    text "[strength]" color "#660000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at StrengthPositionStat
    text "[stamina]" color "#141452" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at StaminaPositionStat
    vbar value StaticValue(lust_points[0], 10):
        xpos 65
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[0], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 171
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_points[1], 10):
        xpos 215
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[1], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 321
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_points[2], 10):
        xpos 365
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[2], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 471
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_points[3], 10):
        xpos 515
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[3], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 621
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_points[4], 10):
        xpos 665
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[4], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 771
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_points[5], 10):
        xpos 815
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[5], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 921
        ypos 31
        xysize(15, 100)
    vbar value StaticValue(lust_points[6], 10):
        xpos 65
        ypos 181
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[6], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 171
        ypos 181
        xysize(15, 100)
    vbar value StaticValue(lust_points[7], 10):
        xpos 215
        ypos 181
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[7], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 321
        ypos 181
        xysize(15, 100)
    vbar value StaticValue(lust_points[8], 10):
        xpos 365
        ypos 181
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[8], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 471
        ypos 181
        xysize(15, 100)
    vbar value StaticValue(lust_points[9], 10):
        xpos 515
        ypos 181
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[9], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 621
        ypos 181
        xysize(15, 100)
    vbar value StaticValue(lust_points[10], 10):
        xpos 665
        ypos 181
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[10], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 771
        ypos 181
        xysize(15, 100)
    vbar value StaticValue(lust_points[11], 10):
        xpos 815
        ypos 181
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[11], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 921
        ypos 181
        xysize(15, 100)    
    vbar value StaticValue(lust_points[12], 10):
        xpos 65
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[12], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 171
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_points[13], 10):
        xpos 215
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[13], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 321
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_points[14], 10):
        xpos 365
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[14], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 471
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_points[15], 10):
        xpos 515
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[15], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 621
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_points[16], 10):
        xpos 665
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[16], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 771
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_points[17], 10):
        xpos 815
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[17], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 921
        ypos 331
        xysize(15, 100)
    vbar value StaticValue(lust_points[18], 10):
        xpos 65
        ypos 481
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[18], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 171
        ypos 481
        xysize(15, 100)
    vbar value StaticValue(lust_points[19], 10):
        xpos 215
        ypos 481
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[19], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 321
        ypos 481
        xysize(15, 100)
    vbar value StaticValue(lust_points[20], 10):
        xpos 365
        ypos 481
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[20], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 471
        ypos 481
        xysize(15, 100)
    vbar value StaticValue(lust_points[21], 10):
        xpos 515
        ypos 481
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[21], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 621
        ypos 481
        xysize(15, 100)
    vbar value StaticValue(lust_points[22], 10):
        xpos 665
        ypos 481
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[22], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 771
        ypos 481
        xysize(15, 100)
    vbar value StaticValue(lust_points[23], 10):
        xpos 815
        ypos 481
        xysize(15, 100)
    vbar value StaticValue(lust_pointsB[23], 10):
        bottom_bar "#ff0000"
        top_bar "#FFB6C1"
        xpos 921
        ypos 481
        xysize(15, 100)
    if annajosewin:
        add "Icons/failsmall.png" pos(55,40)
    if brittanyjosewin:
        add "Icons/failsmall.png" pos(205,40)
    if chantellejosewin:
        add "Icons/failsmall.png" pos(355,40)
    if chiyojosewin:
        add "Icons/failsmall.png" pos(505,40)
    if daniellajosewin:
        add "Icons/failsmall.png" pos(655,40)
    if debbyjosewin:
        add "Icons/failsmall.png" pos(805,40)
    if dorisjosewin:
        add "Icons/failsmall.png" pos(55,190)
    if francinejosewin:
        add "Icons/failsmall.png" pos(205,190)
    if friedajosewin:
        add "Icons/failsmall.png" pos(355,190)
    if hallejosewin:
        add "Icons/failsmall.png" pos(505,190) 
    if jenniferjosewin:
        add "Icons/failsmall.png" pos(655,190) 
    if katejosewin:
        add "Icons/failsmall.png" pos(805,190) 
    if katsumijosewin:
        add "Icons/failsmall.png" pos(55,340)
    if laurajosewin:
        add "Icons/failsmall.png" pos(205,340) 
    if maddyjosewin:
        add "Icons/failsmall.png" pos(355,340)
    if mariajosewin:
        add "Icons/failsmall.png" pos(505,340)
    if nancyjosewin:
        add "Icons/failsmall.png" pos(655,340)
    if nikkijosewin:
        add "Icons/failsmall.png" pos(805,340) 
    if pamelajosewin:
        add "Icons/failsmall.png" pos(55,490)
    if sandyjosewin:
        add "Icons/failsmall.png" pos(205,490)
    if sophiajosewin:
        add "Icons/failsmall.png" pos(355,490)
    if tanyajosewin:
        add "Icons/failsmall.png" pos(505,490)
    if teaganjosewin:
        add "Icons/failsmall.png" pos(655,490) 
    if vivianejosewin:
        add "Icons/failsmall.png" pos(805,490)

    if annawin:
        add "Icons/winsmall.png" pos(50,10)
    if brittanywin:
        add "Icons/winsmall.png" pos(200,10)
    if chantellewin:
        add "Icons/winsmall.png" pos(350,10)
    if chiyowin:
        add "Icons/winsmall.png" pos(500,10)
    if daniellawin:
        add "Icons/winsmall.png" pos(650,10)
    if debbywin:
        add "Icons/winsmall.png" pos(800,10)
    if doriswin:
        add "Icons/winsmall.png" pos(50,160)
    if francinewin:
        add "Icons/winsmall.png" pos(200,160)
    if friedawin:
        add "Icons/winsmall.png" pos(350,160)
    if hallewin:
        add "Icons/winsmall.png" pos(500,160) 
    if jenniferwin:
        add "Icons/winsmall.png" pos(650,160) 
    if katewin:
        add "Icons/winsmall.png" pos(800,160) 
    if katsumiwin:
        add "Icons/winsmall.png" pos(50,310)
    if laurawin:
        add "Icons/winsmall.png" pos(200,310) 
    if maddywin:
        add "Icons/winsmall.png" pos(350,310)
    if mariawin:
        add "Icons/winsmall.png" pos(500,310)
    if nancywin:
        add "Icons/winsmall.png" pos(650,310)
    if nikkiwin:
        add "Icons/winsmall.png" pos(800,310) 
    if pamelawin:
        add "Icons/winsmall.png" pos(50,460)
    if sandywin:
        add "Icons/winsmall.png" pos(200,460)
    if sophiawin:
        add "Icons/winsmall.png" pos(350,460)
    if tanyawin:
        add "Icons/winsmall.png" pos(500,460)
    if teaganwin:
        add "Icons/winsmall.png" pos(650,460) 
    if vivianewin:
        add "Icons/winsmall.png" pos(800,460)
    

################################################################################
## Snooping Game Screens
################################################################################


screen sisbedroomsnoop:
    add "Day1/nikkibedroom01.jpg"
    modal True
    default time_left = 10.0
    default coversnothing = False
    default pillowsnothing = False
    default drawernothing = False
    default sidetablenothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/coversidle.png"
        hover "Snooping/covershover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('coversnothing', True)]
    if (coversnothing == True):
        add "Snooping/coversnothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/pillowsidle.png"
        hover "Snooping/pillowshover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('pillowsnothing', True)]
    if (pillowsnothing == True):
        add "Snooping/pillowsnothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/draweridle.png"
        hover "Snooping/drawerhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('drawernothing', True)]
    if (drawernothing == True):
        add "Snooping/drawernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/sidetableidle.png"
        hover "Snooping/sidetablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('sidetablenothing', True)]
    if (sidetablenothing == True):
        add "Snooping/sidetablenothing.png"
    
    bar value StaticValue(time_left, 10.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10
    
screen debbysnoop01:
    add "Snooping/debbysnooping.jpg"
    modal True
    default time_left = 8.0
    default buffetnothing = False
    default lowtablenothing = False
    default smalltablenothing = False
    default shelfnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/buffetidle.png"
        hover "Snooping/buffethover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('buffetnothing', True)]
    if (buffetnothing == True):
        add "Snooping/buffetnothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/smalltableidle.png"
        hover "Snooping/smalltablehover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundAudaciousPass")]

    imagebutton:
        focus_mask True
        idle "Snooping/lowtableidle.png"
        hover "Snooping/lowtablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('lowtablenothing', True)]
    if (lowtablenothing == True):
        add "Snooping/lowtablenothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/shelfidle.png"
        hover "Snooping/shelfhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('shelfnothing', True)]
    if (shelfnothing == True):
        add "Snooping/shelfnothing.png"
    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen debbysnoop02:
    add "Snooping/debbysnooping.jpg"
    modal True
    default time_left = 8.0
    default buffetnothing = False
    default lowtablenothing = False
    default smalltablenothing = False
    default shelfnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/buffetidle.png"
        hover "Snooping/buffethover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundAudaciousPass")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/smalltableidle.png"
        hover "Snooping/smalltablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('smalltablenothing', True)]
    if (smalltablenothing == True):
        add "Snooping/smalltablenothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/lowtableidle.png"
        hover "Snooping/lowtablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('lowtablenothing', True)]
    if (lowtablenothing == True):
        add "Snooping/lowtablenothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/shelfidle.png"
        hover "Snooping/shelfhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('shelfnothing', True)]
    if (shelfnothing == True):
        add "Snooping/shelfnothing.png"
    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen debbysnoop01Day03:
    add "Snooping/debbysnooping.jpg"
    modal True
    default time_left = 8.0
    default buffetnothing = False
    default lowtablenothing = False
    default smalltablenothing = False
    default shelfnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/buffetidle.png"
        hover "Snooping/buffethover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('buffetnothing', True)]
    if (buffetnothing == True):
        add "Snooping/buffetnothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/smalltableidle.png"
        hover "Snooping/smalltablehover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundAudaciousPassDay03")]

    imagebutton:
        focus_mask True
        idle "Snooping/lowtableidle.png"
        hover "Snooping/lowtablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('lowtablenothing', True)]
    if (lowtablenothing == True):
        add "Snooping/lowtablenothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/shelfidle.png"
        hover "Snooping/shelfhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('shelfnothing', True)]
    if (shelfnothing == True):
        add "Snooping/shelfnothing.png"
    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen debbysnoop02Day03:
    add "Snooping/debbysnooping.jpg"
    modal True
    default time_left = 8.0
    default buffetnothing = False
    default lowtablenothing = False
    default smalltablenothing = False
    default shelfnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/buffetidle.png"
        hover "Snooping/buffethover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundAudaciousPassDay03")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/smalltableidle.png"
        hover "Snooping/smalltablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('smalltablenothing', True)]
    if (smalltablenothing == True):
        add "Snooping/smalltablenothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/lowtableidle.png"
        hover "Snooping/lowtablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('lowtablenothing', True)]
    if (lowtablenothing == True):
        add "Snooping/lowtablenothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/shelfidle.png"
        hover "Snooping/shelfhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('shelfnothing', True)]
    if (shelfnothing == True):
        add "Snooping/shelfnothing.png"
    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen debbysnoop01Day04:
    add "Snooping/debbysnooping.jpg"
    modal True
    default time_left = 8.0
    default buffetnothing = False
    default lowtablenothing = False
    default smalltablenothing = False
    default shelfnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/buffetidle.png"
        hover "Snooping/buffethover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('buffetnothing', True)]
    if (buffetnothing == True):
        add "Snooping/buffetnothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/smalltableidle.png"
        hover "Snooping/smalltablehover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundAudaciousPassDay04")]

    imagebutton:
        focus_mask True
        idle "Snooping/lowtableidle.png"
        hover "Snooping/lowtablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('lowtablenothing', True)]
    if (lowtablenothing == True):
        add "Snooping/lowtablenothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/shelfidle.png"
        hover "Snooping/shelfhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('shelfnothing', True)]
    if (shelfnothing == True):
        add "Snooping/shelfnothing.png"
    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen debbysnoop02Day04:
    add "Snooping/debbysnooping.jpg"
    modal True
    default time_left = 8.0
    default buffetnothing = False
    default lowtablenothing = False
    default smalltablenothing = False
    default shelfnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/buffetidle.png"
        hover "Snooping/buffethover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundAudaciousPassDay04")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/smalltableidle.png"
        hover "Snooping/smalltablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('smalltablenothing', True)]
    if (smalltablenothing == True):
        add "Snooping/smalltablenothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/lowtableidle.png"
        hover "Snooping/lowtablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('lowtablenothing', True)]
    if (lowtablenothing == True):
        add "Snooping/lowtablenothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/shelfidle.png"
        hover "Snooping/shelfhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('shelfnothing', True)]
    if (shelfnothing == True):
        add "Snooping/shelfnothing.png"
    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen debbysnoop01Day05:
    add "Snooping/debbysnooping.jpg"
    modal True
    default time_left = 8.0
    default buffetnothing = False
    default lowtablenothing = False
    default smalltablenothing = False
    default shelfnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/buffetidle.png"
        hover "Snooping/buffethover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('buffetnothing', True)]
    if (buffetnothing == True):
        add "Snooping/buffetnothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/smalltableidle.png"
        hover "Snooping/smalltablehover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundAudaciousPassDay05")]

    imagebutton:
        focus_mask True
        idle "Snooping/lowtableidle.png"
        hover "Snooping/lowtablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('lowtablenothing', True)]
    if (lowtablenothing == True):
        add "Snooping/lowtablenothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/shelfidle.png"
        hover "Snooping/shelfhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('shelfnothing', True)]
    if (shelfnothing == True):
        add "Snooping/shelfnothing.png"
    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen debbysnoop02Day05:
    add "Snooping/debbysnooping.jpg"
    modal True
    default time_left = 8.0
    default buffetnothing = False
    default lowtablenothing = False
    default smalltablenothing = False
    default shelfnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/buffetidle.png"
        hover "Snooping/buffethover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundAudaciousPassDay05")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/smalltableidle.png"
        hover "Snooping/smalltablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('smalltablenothing', True)]
    if (smalltablenothing == True):
        add "Snooping/smalltablenothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/lowtableidle.png"
        hover "Snooping/lowtablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('lowtablenothing', True)]
    if (lowtablenothing == True):
        add "Snooping/lowtablenothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/shelfidle.png"
        hover "Snooping/shelfhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('shelfnothing', True)]
    if (shelfnothing == True):
        add "Snooping/shelfnothing.png"
    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10
            
            
screen debbysnoop01Day06:
    add "Snooping/debbysnooping.jpg"
    modal True
    default time_left = 8.0
    default buffetnothing = False
    default lowtablenothing = False
    default smalltablenothing = False
    default shelfnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/buffetidle.png"
        hover "Snooping/buffethover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('buffetnothing', True)]
    if (buffetnothing == True):
        add "Snooping/buffetnothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/smalltableidle.png"
        hover "Snooping/smalltablehover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundAudaciousPassDay06")]

    imagebutton:
        focus_mask True
        idle "Snooping/lowtableidle.png"
        hover "Snooping/lowtablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('lowtablenothing', True)]
    if (lowtablenothing == True):
        add "Snooping/lowtablenothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/shelfidle.png"
        hover "Snooping/shelfhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('shelfnothing', True)]
    if (shelfnothing == True):
        add "Snooping/shelfnothing.png"
    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen debbysnoop02Day06:
    add "Snooping/debbysnooping.jpg"
    modal True
    default time_left = 8.0
    default buffetnothing = False
    default lowtablenothing = False
    default smalltablenothing = False
    default shelfnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/buffetidle.png"
        hover "Snooping/buffethover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundAudaciousPassDay06")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/smalltableidle.png"
        hover "Snooping/smalltablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('smalltablenothing', True)]
    if (smalltablenothing == True):
        add "Snooping/smalltablenothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/lowtableidle.png"
        hover "Snooping/lowtablehover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('lowtablenothing', True)]
    if (lowtablenothing == True):
        add "Snooping/lowtablenothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/shelfidle.png"
        hover "Snooping/shelfhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('shelfnothing', True)]
    if (shelfnothing == True):
        add "Snooping/shelfnothing.png"
    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10
            
screen nursesnoop01:
    add "Snooping/nursesnooping.jpg"
    modal True
    default time_left = 10.0
    default drawer01nothing = False
    default drawer02nothing = False
    default drawer03nothing = False
    default drawer04nothing = False
    default cupboardnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/drawer01idle.png"
        hover "Snooping/drawer01hover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundPendulum")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/drawer02idle.png"
        hover "Snooping/drawer02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('drawer02nothing', True)]
    if (drawer02nothing == True):
        add "Snooping/drawer02nothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/drawer03idle.png"
        hover "Snooping/drawer03hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('drawer03nothing', True)]
    if (drawer03nothing == True):
        add "Snooping/drawer03nothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/drawer04idle.png"
        hover "Snooping/drawer04hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('drawer04nothing', True)]
    if (drawer04nothing == True):
        add "Snooping/drawer04nothing.png"
     
    imagebutton:
        focus_mask True
        idle "Snooping/cupboardidle.png"
        hover "Snooping/cupboardhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('cupboardnothing', True)]
    if (cupboardnothing == True):
        add "Snooping/cupboardnothing.png"
 
    bar value StaticValue(time_left, 10.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10
        
screen nursesnoop02:
    add "Snooping/nursesnooping.jpg"
    modal True
    default time_left = 10.0
    default drawer01nothing = False
    default drawer02nothing = False
    default drawer03nothing = False
    default drawer04nothing = False
    default cupboardnothing = False
   
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/drawer01idle.png"
        hover "Snooping/drawer01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('drawer01nothing', True)]
    if (drawer01nothing == True):
        add "Snooping/drawer01nothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/drawer02idle.png"
        hover "Snooping/drawer02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('drawer02nothing', True)]
    if (drawer02nothing == True):
        add "Snooping/drawer02nothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/drawer03idle.png"
        hover "Snooping/drawer03hover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundPendulum")]
        
    imagebutton:
        focus_mask True
        idle "Snooping/drawer04idle.png"
        hover "Snooping/drawer04hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('drawer04nothing', True)]
    if (drawer04nothing == True):
        add "Snooping/drawer04nothing.png"
     
    imagebutton:
        focus_mask True
        idle "Snooping/cupboardidle.png"
        hover "Snooping/cupboardhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('cupboardnothing', True)]
    if (cupboardnothing == True):
        add "Snooping/cupboardnothing.png"
 
    bar value StaticValue(time_left, 10.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen mombedroomsnoop:
    add "Snooping/mombedroomsnooping.jpg"
    modal True
    default time_left = 8.0
    default mompillownothing = False
    default momleftdrawernothing = False
    default momrightdrawernothing = False
    default momdressernothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/mompillowidle.png"
        hover "Snooping/mompillowhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('mompillownothing', True)]
    if (mompillownothing == True):
        add "Snooping/mompillownothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerleftidle.png"
        hover "Snooping/momdrawerlefthover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdrawerleftnothing', True)]
    if (momleftdrawernothing == True):
        add "Snooping/momdrawerleftnothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/momdresseridle.png"
        hover "Snooping/momdresserhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdressernothing', True)]
    if (momdressernothing == True):
        add "Snooping/momdressernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerrightidle.png"
        hover "Snooping/momdrawerrighthover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundDildo")]

    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10
        
screen officesnoop01:
    add "Snooping/principalsnooping.jpg"
    modal True
    default time_left = 8.0
    default principaldrawer01nothing = False
    default principaldrawer02nothing = False
    default principalfoldernothing = False
    default principalsheet01nothing = False
    default principalsheet02nothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer01idle.png"
        hover "Snooping/principaldrawer01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principaldrawer01nothing', True)]
    if (principaldrawer01nothing == True):
        add "Snooping/principaldrawer01nothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer02idle.png"
        hover "Snooping/principaldrawer02hover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundFriedaGradeDay03")]

    imagebutton:
        focus_mask True
        idle "Snooping/principalfolderidle.png"
        hover "Snooping/principalfolderhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalfoldernothing', True)]
    if (principalfoldernothing == True):
        add "Snooping/principalfoldernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet01idle.png"
        hover "Snooping/principalsheet01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet01nothing', True)]
    if (principalsheet01nothing == True):
        add "Snooping/principalsheet01nothing.png"
     
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet02idle.png"
        hover "Snooping/principalsheet02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet02nothing', True)]
    if (principalsheet02nothing == True):
        add "Snooping/principalsheet02nothing.png"
 
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10
        
screen officesnoop02:
    add "Snooping/principalsnooping.jpg"
    modal True
    default time_left = 8.0
    default principaldrawer01nothing = False
    default principaldrawer02nothing = False
    default principalfoldernothing = False
    default principalsheet01nothing = False
    default principalsheet02nothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer01idle.png"
        hover "Snooping/principaldrawer01hover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundFriedaGradeDay03")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer02idle.png"
        hover "Snooping/principaldrawer02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principaldrawer02nothing', True)]
    if (principaldrawer02nothing == True):
        add "Snooping/principaldrawer02nothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/principalfolderidle.png"
        hover "Snooping/principalfolderhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalfoldernothing', True)]
    if (principalfoldernothing == True):
        add "Snooping/principalfoldernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet01idle.png"
        hover "Snooping/principalsheet01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet01nothing', True)]
    if (principalsheet01nothing == True):
        add "Snooping/principalsheet01nothing.png"
     
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet02idle.png"
        hover "Snooping/principalsheet02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet02nothing', True)]
    if (principalsheet02nothing == True):
        add "Snooping/principalsheet02nothing.png"
 
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen officesnoop01day04:
    add "Snooping/principalsnooping.jpg"
    modal True
    default time_left = 8.0
    default principaldrawer01nothing = False
    default principaldrawer02nothing = False
    default principalfoldernothing = False
    default principalsheet01nothing = False
    default principalsheet02nothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer01idle.png"
        hover "Snooping/principaldrawer01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principaldrawer01nothing', True)]
    if (principaldrawer01nothing == True):
        add "Snooping/principaldrawer02nothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer02idle.png"
        hover "Snooping/principaldrawer02hover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundFriedaGradeDay04")]

    imagebutton:
        focus_mask True
        idle "Snooping/principalfolderidle.png"
        hover "Snooping/principalfolderhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalfoldernothing', True)]
    if (principalfoldernothing == True):
        add "Snooping/principalfoldernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet01idle.png"
        hover "Snooping/principalsheet01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet01nothing', True)]
    if (principalsheet01nothing == True):
        add "Snooping/principalsheet01nothing.png"
     
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet02idle.png"
        hover "Snooping/principalsheet02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet02nothing', True)]
    if (principalsheet02nothing == True):
        add "Snooping/principalsheet02nothing.png"
 
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10
        
screen officesnoop02day04:
    add "Snooping/principalsnooping.jpg"
    modal True
    default time_left = 8.0
    default principaldrawer01nothing = False
    default principaldrawer02nothing = False
    default principalfoldernothing = False
    default principalsheet01nothing = False
    default principalsheet02nothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer01idle.png"
        hover "Snooping/principaldrawer01hover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundFriedaGradeDay04")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer02idle.png"
        hover "Snooping/principaldrawer02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principaldrawer02nothing', True)]
    if (principaldrawer02nothing == True):
        add "Snooping/principaldrawer02nothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/principalfolderidle.png"
        hover "Snooping/principalfolderhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalfoldernothing', True)]
    if (principalfoldernothing == True):
        add "Snooping/principalfoldernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet01idle.png"
        hover "Snooping/principalsheet01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet01nothing', True)]
    if (principalsheet01nothing == True):
        add "Snooping/principalsheet01nothing.png"
     
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet02idle.png"
        hover "Snooping/principalsheet02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet02nothing', True)]
    if (principalsheet02nothing == True):
        add "Snooping/principalsheet02nothing.png"
 
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen officesnoop01day05:
    add "Snooping/principalsnooping.jpg"
    modal True
    default time_left = 8.0
    default principaldrawer01nothing = False
    default principaldrawer02nothing = False
    default principalfoldernothing = False
    default principalsheet01nothing = False
    default principalsheet02nothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer01idle.png"
        hover "Snooping/principaldrawer01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principaldrawer01nothing', True)]
    if (principaldrawer01nothing == True):
        add "Snooping/principaldrawer02nothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer02idle.png"
        hover "Snooping/principaldrawer02hover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundFriedaGradeDay05")]

    imagebutton:
        focus_mask True
        idle "Snooping/principalfolderidle.png"
        hover "Snooping/principalfolderhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalfoldernothing', True)]
    if (principalfoldernothing == True):
        add "Snooping/principalfoldernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet01idle.png"
        hover "Snooping/principalsheet01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet01nothing', True)]
    if (principalsheet01nothing == True):
        add "Snooping/principalsheet01nothing.png"
     
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet02idle.png"
        hover "Snooping/principalsheet02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet02nothing', True)]
    if (principalsheet02nothing == True):
        add "Snooping/principalsheet02nothing.png"
 
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10
        
screen officesnoop02day05:
    add "Snooping/principalsnooping.jpg"
    modal True
    default time_left = 8.0
    default principaldrawer01nothing = False
    default principaldrawer02nothing = False
    default principalfoldernothing = False
    default principalsheet01nothing = False
    default principalsheet02nothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer01idle.png"
        hover "Snooping/principaldrawer01hover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundFriedaGradeDay05")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer02idle.png"
        hover "Snooping/principaldrawer02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principaldrawer02nothing', True)]
    if (principaldrawer02nothing == True):
        add "Snooping/principaldrawer02nothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/principalfolderidle.png"
        hover "Snooping/principalfolderhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalfoldernothing', True)]
    if (principalfoldernothing == True):
        add "Snooping/principalfoldernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet01idle.png"
        hover "Snooping/principalsheet01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet01nothing', True)]
    if (principalsheet01nothing == True):
        add "Snooping/principalsheet01nothing.png"
     
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet02idle.png"
        hover "Snooping/principalsheet02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet02nothing', True)]
    if (principalsheet02nothing == True):
        add "Snooping/principalsheet02nothing.png"
 
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen officesnoop01day06:
    add "Snooping/principalsnooping.jpg"
    modal True
    default time_left = 8.0
    default principaldrawer01nothing = False
    default principaldrawer02nothing = False
    default principalfoldernothing = False
    default principalsheet01nothing = False
    default principalsheet02nothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer01idle.png"
        hover "Snooping/principaldrawer01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principaldrawer01nothing', True)]
    if (principaldrawer01nothing == True):
        add "Snooping/principaldrawer02nothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer02idle.png"
        hover "Snooping/principaldrawer02hover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundFriedaGradeDay06")]

    imagebutton:
        focus_mask True
        idle "Snooping/principalfolderidle.png"
        hover "Snooping/principalfolderhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalfoldernothing', True)]
    if (principalfoldernothing == True):
        add "Snooping/principalfoldernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet01idle.png"
        hover "Snooping/principalsheet01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet01nothing', True)]
    if (principalsheet01nothing == True):
        add "Snooping/principalsheet01nothing.png"
     
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet02idle.png"
        hover "Snooping/principalsheet02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet02nothing', True)]
    if (principalsheet02nothing == True):
        add "Snooping/principalsheet02nothing.png"
 
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10
        
screen officesnoop02day06:
    add "Snooping/principalsnooping.jpg"
    modal True
    default time_left = 8.0
    default principaldrawer01nothing = False
    default principaldrawer02nothing = False
    default principalfoldernothing = False
    default principalsheet01nothing = False
    default principalsheet02nothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer01idle.png"
        hover "Snooping/principaldrawer01hover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundFriedaGradeDay06")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/principaldrawer02idle.png"
        hover "Snooping/principaldrawer02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principaldrawer02nothing', True)]
    if (principaldrawer02nothing == True):
        add "Snooping/principaldrawer02nothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/principalfolderidle.png"
        hover "Snooping/principalfolderhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalfoldernothing', True)]
    if (principalfoldernothing == True):
        add "Snooping/principalfoldernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet01idle.png"
        hover "Snooping/principalsheet01hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet01nothing', True)]
    if (principalsheet01nothing == True):
        add "Snooping/principalsheet01nothing.png"
     
    imagebutton:
        focus_mask True
        idle "Snooping/principalsheet02idle.png"
        hover "Snooping/principalsheet02hover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('principalsheet02nothing', True)]
    if (principalsheet02nothing == True):
        add "Snooping/principalsheet02nothing.png"
 
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen mombedroomsnoopDay03:
    add "Snooping/mombedroomsnooping.jpg"
    modal True
    default time_left = 8.0
    default mompillownothing = False
    default momleftdrawernothing = False
    default momrightdrawernothing = False
    default momdressernothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/mompillowidle.png"
        hover "Snooping/mompillowhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('mompillownothing', True)]
    if (mompillownothing == True):
        add "Snooping/mompillownothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerleftidle.png"
        hover "Snooping/momdrawerlefthover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdrawerleftnothing', True)]
    if (momleftdrawernothing == True):
        add "Snooping/momdrawerleftnothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/momdresseridle.png"
        hover "Snooping/momdresserhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdressernothing', True)]
    if (momdressernothing == True):
        add "Snooping/momdressernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerrightidle.png"
        hover "Snooping/momdrawerrighthover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundDildoDay03")]

    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen mombedroomsnoopDay04:
    add "Snooping/mombedroomsnooping.jpg"
    modal True
    default time_left = 8.0
    default mompillownothing = False
    default momleftdrawernothing = False
    default momrightdrawernothing = False
    default momdressernothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/mompillowidle.png"
        hover "Snooping/mompillowhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('mompillownothing', True)]
    if (mompillownothing == True):
        add "Snooping/mompillownothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerleftidle.png"
        hover "Snooping/momdrawerlefthover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdrawerleftnothing', True)]
    if (momleftdrawernothing == True):
        add "Snooping/momdrawerleftnothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/momdresseridle.png"
        hover "Snooping/momdresserhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdressernothing', True)]
    if (momdressernothing == True):
        add "Snooping/momdressernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerrightidle.png"
        hover "Snooping/momdrawerrighthover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundDildoDay04")]

    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen mombedroomsnoopDay05:
    add "Snooping/mombedroomsnooping.jpg"
    modal True
    default time_left = 8.0
    default mompillownothing = False
    default momleftdrawernothing = False
    default momrightdrawernothing = False
    default momdressernothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/mompillowidle.png"
        hover "Snooping/mompillowhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('mompillownothing', True)]
    if (mompillownothing == True):
        add "Snooping/mompillownothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerleftidle.png"
        hover "Snooping/momdrawerlefthover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdrawerleftnothing', True)]
    if (momleftdrawernothing == True):
        add "Snooping/momdrawerleftnothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/momdresseridle.png"
        hover "Snooping/momdresserhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdressernothing', True)]
    if (momdressernothing == True):
        add "Snooping/momdressernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerrightidle.png"
        hover "Snooping/momdrawerrighthover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundDildoDay05")]

    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen mombedroomsnoopDay06:
    add "Snooping/mombedroomsnooping.jpg"
    modal True
    default time_left = 8.0
    default mompillownothing = False
    default momleftdrawernothing = False
    default momrightdrawernothing = False
    default momdressernothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/mompillowidle.png"
        hover "Snooping/mompillowhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('mompillownothing', True)]
    if (mompillownothing == True):
        add "Snooping/mompillownothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerleftidle.png"
        hover "Snooping/momdrawerlefthover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdrawerleftnothing', True)]
    if (momleftdrawernothing == True):
        add "Snooping/momdrawerleftnothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/momdresseridle.png"
        hover "Snooping/momdresserhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdressernothing', True)]
    if (momdressernothing == True):
        add "Snooping/momdressernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerrightidle.png"
        hover "Snooping/momdrawerrighthover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundDildoDay06")]

    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10
            
screen mombedroomsnoopDay07:
    add "Snooping/mombedroomsnooping.jpg"
    modal True
    default time_left = 8.0
    default mompillownothing = False
    default momleftdrawernothing = False
    default momrightdrawernothing = False
    default momdressernothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/mompillowidle.png"
        hover "Snooping/mompillowhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('mompillownothing', True)]
    if (mompillownothing == True):
        add "Snooping/mompillownothing.png"
    
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerleftidle.png"
        hover "Snooping/momdrawerlefthover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdrawerleftnothing', True)]
    if (momleftdrawernothing == True):
        add "Snooping/momdrawerleftnothing.png"

    imagebutton:
        focus_mask True
        idle "Snooping/momdresseridle.png"
        hover "Snooping/momdresserhover.png"
        action [SetScreenVariable('time_left', time_left-1), SetScreenVariable('momdressernothing', True)]
    if (momdressernothing == True):
        add "Snooping/momdressernothing.png"
        
    imagebutton:
        focus_mask True
        idle "Snooping/momdrawerrightidle.png"
        hover "Snooping/momdrawerrighthover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("FoundDildoDay07")]

    
    bar value StaticValue(time_left, 8.0):
        xalign 0.45 yalign 0.05
        xmaximum 800 
        ymaximum 10

screen drugday05:
    add "Snooping/dealer02.jpg"
    modal True
    default time_left = 3.0
    default redpillnothing = False
    default bluepillnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/redpillidle.png"
        hover "Snooping/redpillhover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("DrugRedDay05")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/bluepillidle.png"
        hover "Snooping/bluepillhover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("DrugBlueDay05")]

    bar value StaticValue(time_left, 3.0):
        xalign 0.45 yalign 0.05
        xmaximum 600 
        ymaximum 10

screen drugday06:
    add "Snooping/dealer02.jpg"
    modal True
    default time_left = 3.0
    default redpillnothing = False
    default bluepillnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/redpillidle.png"
        hover "Snooping/redpillhover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("DrugRedDay06")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/bluepillidle.png"
        hover "Snooping/bluepillhover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("DrugBlueDay06")]

    bar value StaticValue(time_left, 3.0):
        xalign 0.45 yalign 0.05
        xmaximum 600 
        ymaximum 10
    
screen drugday07:
    add "Snooping/dealer02.jpg"
    modal True
    default time_left = 3.0
    default redpillnothing = False
    default bluepillnothing = False
    
    # text "[time_left]" align .5, .5
    
    if time_left <= 0:
        timer .001 action Return # Whatever action you want to happen when timer runs out!
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
    
    imagebutton:
        focus_mask True
        idle "Snooping/redpillidle.png"
        hover "Snooping/redpillhover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("DrugRedDay07")]
    
    imagebutton:
        focus_mask True
        idle "Snooping/bluepillidle.png"
        hover "Snooping/bluepillhover.png"
        action [SetScreenVariable('time_left', time_left-1), Jump ("DrugBlueDay07")]

    bar value StaticValue(time_left, 3.0):
        xalign 0.45 yalign 0.05
        xmaximum 600 
        ymaximum 10

################################################################################
## Inventory Screens
################################################################################

screen inventorybutton:
    vbox xalign 0.0 yalign 0.28:
        imagebutton:
            idle "Icons/inventoryidleb.png"
            hover "Icons/inventoryhoverb.png"
            action ui.callsinnewcontext("InventoryShow")

label InventoryShow:
    call screen inventory
    stop sound
    return

screen inventory:
    add "Inventory/inventorybackground.png"
    add "Icons/exit.png"
    $ renpy.music.play('Sounds/pigeon.mp3')
  
    if (wd69):
        imagebutton:
            focus_mask True
            idle "Inventory/wd69idle.png"
            hover "Inventory/wd69hover.png"
            action NullAction
            
    if (dildo):
        imagebutton:
            focus_mask True
            idle "Inventory/dildoidle.png"
            hover "Inventory/dildohover.png"
            action NullAction 
        
    if (pendulum):
        imagebutton:
            focus_mask True
            idle "Inventory/pendulumidle.png"
            hover "Inventory/pendulumhover.png"
            action NullAction

    if (condoms):
        imagebutton:
            focus_mask True
            idle "Inventory/megacondomsidle.png"
            hover "Inventory/megacondomshover.png"
            action NullAction

    if (wristband):
        imagebutton:
            focus_mask True
            idle "Inventory/wristbandidle.png"
            hover "Inventory/wristbandhover.png"
            action NullAction

    if (book):
        imagebutton:
            focus_mask True
            idle "Inventory/bookidle.png"
            hover "Inventory/bookhover.png"
            action NullAction

    if (pheromone):
        imagebutton:
            focus_mask True
            idle "Inventory/pheromoneidle.png"
            hover "Inventory/pheromonehover.png"
            action NullAction

    if (audaciouspass):
        imagebutton:
            focus_mask True
            idle "Inventory/audaciouspassidle.png"
            hover "Inventory/audaciouspasshover.png"
            action NullAction

    if (knife):
        imagebutton:
            focus_mask True
            idle "Inventory/knifeidle.png"
            hover "Inventory/knifehover.png"
            action NullAction

    if (camera):
        imagebutton:
            focus_mask True
            idle "Inventory/cameraidle.png"
            hover "Inventory/camerahover.png"
            action NullAction

    if (whitebull):
        imagebutton:
            focus_mask True
            idle "Inventory/whitebullidle.png"
            hover "Inventory/whitebullhover.png"
            action NullAction

    if (tanktop):
        imagebutton:
            focus_mask True
            idle "Inventory/tanktopidle.png"
            hover "Inventory/tanktophover.png"
            action NullAction

    if (goldcoin):
        imagebutton:
            focus_mask True
            idle "Inventory/goldcoinidle.png"
            hover "Inventory/goldcoinhover.png"
            action NullAction
    
    if (flower):
        imagebutton:
            focus_mask True
            idle "Inventory/floweridle.png"
            hover "Inventory/flowerhover.png"
            action NullAction

    if (redpill == 1):
        imagebutton:
            focus_mask True
            idle "Inventory/redpillx1.png"
            hover "Inventory/redpillx1.png"
            action NullAction
    if (redpill == 2):
        imagebutton:
            focus_mask True
            idle "Inventory/redpillsx2.png"
            hover "Inventory/redpillsx2.png"
            action NullAction

    if (bluepill == 1):
        imagebutton:
            focus_mask True
            idle "Inventory/bluepillx1.png"
            hover "Inventory/bluepillx1.png"
            action NullAction
    if (bluepill == 2):
        imagebutton:
            focus_mask True
            idle "Inventory/bluepillsx2.png"
            hover "Inventory/bluepillsx2.png"
            action NullAction
    if beercase:
        imagebutton:
            focus_mask True
            idle "Inventory/beercaseidle.png"
            hover "Inventory/beercasehover.png"
            action NullAction()
    button:
        xpos .83
        ypos .9
        xysize(100, 50)        
        action [renpy.music.stop, Return()]
        
################################################################################
## Timed Menu Screens
################################################################################

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.1 xmaximum 400 at alpha_dissolve # This is the timer bar.

################################################################################
## Character Sheet Screen
################################################################################

screen charactersheets:    
    
    add "Sheets/charactersheets.jpg"
    add "Icons/exit.png"
    button:
        xpos .82
        ypos .92
        xysize(120, 40)      
        action [renpy.music.stop, Return()]

    imagebutton:
        focus_mask True
        idle "Sheets/annaidle.png"
        hover "Sheets/annahover.png"
        action ui.callsinnewcontext ("Annasheet")
    
    imagebutton:
        focus_mask True
        idle "Sheets/brittanyidle.png"
        hover "Sheets/brittanyhover.png"
        action ui.callsinnewcontext ("Brittanysheet")
    
    imagebutton:
        focus_mask True
        idle "Sheets/chantelleidle.png"
        hover "Sheets/chantellehover.png"
        action ui.callsinnewcontext ("Chantellesheet")
    
    imagebutton:
        focus_mask True
        idle "Sheets/chiyoidle.png"
        hover "Sheets/chiyohover.png"
        action ui.callsinnewcontext ("Chiyosheet")
    
    imagebutton:
        focus_mask True
        idle "Sheets/daniellaidle.png"
        hover "Sheets/daniellahover.png"
        action ui.callsinnewcontext ("Daniellasheet")
    
    imagebutton:
        focus_mask True
        idle "Sheets/debbyidle.png"
        hover "Sheets/debbyhover.png"
        action ui.callsinnewcontext ("Debbysheet")
    
    imagebutton:
        focus_mask True
        idle "Sheets/dorisidle.png"
        hover "Sheets/dorishover.png"
        action ui.callsinnewcontext ("Dorissheet")
    
    imagebutton:
        focus_mask True
        idle "Sheets/francineidle.png"
        hover "Sheets/francinehover.png"
        action ui.callsinnewcontext ("Francinesheet")
    
    imagebutton:
        focus_mask True
        idle "Sheets/friedaidle.png"
        hover "Sheets/friedahover.png"
        action ui.callsinnewcontext ("Friedasheet")
    
    imagebutton:
        focus_mask True
        idle "Sheets/halleidle.png"
        hover "Sheets/hallehover.png"
        action ui.callsinnewcontext ("Hallesheet")
    
    imagebutton:
        focus_mask True
        idle "Sheets/jenniferidle.png"
        hover "Sheets/jenniferhover.png"
        action ui.callsinnewcontext ("Jennifersheet")
    
    imagebutton:
        focus_mask True
        idle "Sheets/kateidle.png"
        hover "Sheets/katehover.png"
        action ui.callsinnewcontext ("Katesheet") 
            
    imagebutton:
        focus_mask True
        idle "Sheets/katsumiidle.png"
        hover "Sheets/katsumihover.png"
        action ui.callsinnewcontext ("Katsumisheet") 

    imagebutton:
        focus_mask True
        idle "Sheets/lauraidle.png"
        hover "Sheets/laurahover.png"
        action ui.callsinnewcontext ("Laurasheet") 

    imagebutton:
        focus_mask True
        idle "Sheets/maddyidle.png"
        hover "Sheets/maddyhover.png"
        action ui.callsinnewcontext ("Maddysheet") 

    imagebutton:
        focus_mask True
        idle "Sheets/mariaidle.png"
        hover "Sheets/mariahover.png"
        action ui.callsinnewcontext ("Mariasheet") 

    imagebutton:
        focus_mask True
        idle "Sheets/nancyidle.png"
        hover "Sheets/nancyhover.png"
        action ui.callsinnewcontext ("Nancysheet") 

    imagebutton:
        focus_mask True
        idle "Sheets/pamelaidle.png"
        hover "Sheets/pamelahover.png"
        action ui.callsinnewcontext ("Pamelasheet") 

    imagebutton:
        focus_mask True
        idle "Sheets/sandyidle.png"
        hover "Sheets/sandyhover.png"
        action ui.callsinnewcontext ("Sandysheet") 

    imagebutton:
        focus_mask True
        idle "Sheets/nikkiidle.png"
        hover "Sheets/nikkihover.png"
        action ui.callsinnewcontext ("Nikkisheet") 

    imagebutton:
        focus_mask True
        idle "Sheets/sophiaidle.png"
        hover "Sheets/sophiahover.png"
        action ui.callsinnewcontext ("Sophiasheet") 

    imagebutton:
        focus_mask True
        idle "Sheets/tanyaidle.png"
        hover "Sheets/tanyahover.png"
        action ui.callsinnewcontext ("Tanyasheet") 

    imagebutton:
        focus_mask True
        idle "Sheets/teaganidle.png"
        hover "Sheets/teaganhover.png"
        action ui.callsinnewcontext ("Teagansheet") 

    imagebutton:
        focus_mask True
        idle "Sheets/vivianeidle.png"
        hover "Sheets/vivianehover.png"
        action ui.callsinnewcontext ("Vivianesheet") 

label Annasheet:    
    scene
    show anna02
    show exitbrown:
        xpos 0.37 ypos 0.9
    if lust_points[0] >=5:
        show topbrown:
            xpos 0.02 ypos 0.9
    call screen annasheetb
    hide anna02
    hide topbrown
    hide exitbrown
    return

screen annasheetb:
    add annablinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("AnnaTopoff")

label AnnaTopoff:
    hide topbrown
    call screen annasheetc
    return

screen annasheetc:
    add annablinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()
                
label Brittanysheet:    
    scene
    show brittany02
    show exitred:
        xpos 0.37 ypos 0.9
    if lust_points[1] >=5:
        show topred:
            xpos 0.02 ypos 0.9
    call screen brittanysheetb
    hide brittany02
    hide topred
    hide exitred
    return

screen brittanysheetb:
    add brittanyblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("BrittanyTopoff")

label BrittanyTopoff:
    hide topred
    call screen brittanysheetc
    return

screen brittanysheetc:
    add brittanyblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()
    
label Chantellesheet:    
    scene
    show chantelle02
    show exityellow:
        xpos 0.37 ypos 0.9
    if lust_points[2] >=5:
        show topyellow:
            xpos 0.02 ypos 0.9
    call screen chantellesheetb
    hide chantelle02
    hide topyellow
    hide exityellow
    return

screen chantellesheetb:
    add chantelleblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("ChantelleTopoff")

label ChantelleTopoff:
    hide topyellow
    call screen chantellesheetc
    return

screen chantellesheetc:
    add chantelleblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()
    
label Chiyosheet:    
    scene
    show chiyo02
    show exitgreen:
        xpos 0.37 ypos 0.9
    if lust_points[3] >=5:
        show topgreen:
            xpos 0.02 ypos 0.9
    call screen chiyosheetb
    hide chiyo02
    hide topgreen
    hide exitgreen
    return

screen chiyosheetb:
    add chiyoblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("ChiyoTopoff")

label ChiyoTopoff:
    hide topgreen
    call screen chiyosheetc
    return

screen chiyosheetc:
    add chiyoblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Daniellasheet:    
    scene
    show daniella02
    show exitgrey:
        xpos 0.37 ypos 0.9
    if lust_points[4] >=5:
        show topgrey:
            xpos 0.02 ypos 0.9
    call screen daniellasheetb
    hide daniella02
    hide topgrey
    hide exitgrey
    return

screen daniellasheetb:
    add daniellablinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("DaniellaTopoff")

label DaniellaTopoff:
    hide topgrey
    call screen daniellasheetc
    return

screen daniellasheetc:
    add daniellablinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Debbysheet:    
    scene
    show debby02
    show exitgrey:
        xpos 0.37 ypos 0.9
    if lust_points[5] >=5:
        show topgrey:
            xpos 0.02 ypos 0.9
    call screen debbysheetb
    hide debby02
    hide topgrey
    hide exitgrey
    return

screen debbysheetb:
    add debbyblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("DebbyTopoff")

label DebbyTopoff:
    hide topgrey
    call screen debbysheetc
    return

screen debbysheetc:
    add debbyblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Dorissheet:    
    scene
    show doris02
    show exitorange:
        xpos 0.37 ypos 0.9
    if lust_points[6] >=5:
        show toporange:
            xpos 0.02 ypos 0.9
    call screen dorissheetb
    hide doris02
    hide toporange
    hide exitorange
    return

screen dorissheetb:
    add dorisblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("DorisTopoff")

label DorisTopoff:
    hide toporange
    call screen dorissheetc
    return

screen dorissheetc:
    add dorisblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Francinesheet:    
    scene
    show francine02
    show exitred:
        xpos 0.37 ypos 0.9
    if lust_points[7] >=5:
        show topred:
            xpos 0.02 ypos 0.9
    call screen francinesheetb
    hide francine02
    hide topred
    hide exitred
    return

screen francinesheetb:
    add francineblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("FrancineTopoff")

label FrancineTopoff:
    hide topred
    call screen francinesheetc
    return

screen francinesheetc:
    add francineblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Friedasheet:    
    scene
    show frieda02
    show exitblue:
        xpos 0.37 ypos 0.9
    if lust_points[8] >=5:
        show topblue:
            xpos 0.02 ypos 0.9
    call screen friedasheetb
    hide frieda02
    hide topblue
    hide exitblue
    return

screen friedasheetb:
    add friedablinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("FriedaTopoff")

label FriedaTopoff:
    hide topblue
    call screen friedasheetc
    return

screen friedasheetc:
    add friedablinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Hallesheet:    
    scene
    show halle02
    show exitred:
        xpos 0.37 ypos 0.9
    if lust_points[9] >=5:
        show topred:
            xpos 0.02 ypos 0.9
    call screen hallesheetb
    hide halle02
    hide topred
    hide exitred
    return

screen hallesheetb:
    add halleblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("HalleTopoff")

label HalleTopoff:
    hide topred
    call screen hallesheetc
    return

screen hallesheetc:
    add halleblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Jennifersheet:    
    scene
    show jennifer02
    show exitgrey:
        xpos 0.37 ypos 0.9
    if lust_points[10] >=5:
        show topgrey:
            xpos 0.02 ypos 0.9
    call screen jennifersheetb
    hide jennifer02
    hide topgrey
    hide exitgrey
    return

screen jennifersheetb:
    add jenniferblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("JenniferTopoff")

label JenniferTopoff:
    hide topgrey
    call screen jennifersheetc
    return

screen jennifersheetc:
    add jenniferblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Katesheet:    
    scene
    show kate02
    show exitblue:
        xpos 0.37 ypos 0.9
    if lust_points[11] >=5:
        show topblue:
            xpos 0.02 ypos 0.9
    call screen katesheetb
    hide kate02
    hide topblue
    hide exitblue
    return

screen katesheetb:
    add kateblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("KateTopoff")

label KateTopoff:
    hide topblue
    call screen katesheetc
    return

screen katesheetc:
    add kateblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Katsumisheet:    
    scene
    show katsumi02
    show exitblue:
        xpos 0.37 ypos 0.9
    if lust_points[12] >=5:
        show topblue:
            xpos 0.02 ypos 0.9
    call screen katsumisheetb
    hide katsumi02
    hide topblue
    hide exitblue
    return

screen katsumisheetb:
    add katsumiblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("KatsumiTopoff")

label KatsumiTopoff:
    hide topblue
    call screen katsumisheetc
    return

screen katsumisheetc:
    add katsumiblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Laurasheet:    
    scene
    show laura02
    show exitgrey:
        xpos 0.37 ypos 0.9
    if lust_points[13] >=5:
        show topgrey:
            xpos 0.02 ypos 0.9
    call screen laurasheetb
    hide laura02
    hide topgrey
    hide exitgrey
    return

screen laurasheetb:
    add laurablinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("LauraTopoff")

label LauraTopoff:
    hide topgrey
    call screen laurasheetc
    return

screen laurasheetc:
    add laurablinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Maddysheet:    
    scene
    show maddy02
    show exitgrey:
        xpos 0.37 ypos 0.9
    if lust_points[14] >=5:
        show topgrey:
            xpos 0.02 ypos 0.9
    call screen maddysheetb
    hide maddy02
    hide topgrey
    hide exitgrey
    return

screen maddysheetb:
    add maddyblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("MaddyTopoff")

label MaddyTopoff:
    hide topgrey
    call screen maddysheetc
    return

screen maddysheetc:
    add maddyblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Mariasheet:    
    scene
    show maria02
    show exitorange:
        xpos 0.37 ypos 0.9
    if lust_points[15] >=5:
        show toporange:
            xpos 0.02 ypos 0.9
    call screen mariasheetb
    hide maria02
    hide toporange
    hide exitorange
    return

screen mariasheetb:
    add mariablinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("MariaTopoff")

label MariaTopoff:
    hide toporange
    call screen mariasheetc
    return

screen mariasheetc:
    add mariablinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Nancysheet:    
    scene
    show nancy02
    show exitgrey:
        xpos 0.37 ypos 0.9
    if lust_points[16] >=5:
        show topgrey:
            xpos 0.02 ypos 0.9
    call screen nancysheetb
    hide nancy02
    hide topgrey
    hide exitgfrey
    return

screen nancysheetb:
    add nancyblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("NancyTopoff")

label NancyTopoff:
    hide topgrey
    call screen nancysheetc
    return

screen nancysheetc:
    add nancyblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Nikkisheet:    
    scene
    show nikki02
    show exitred:
        xpos 0.37 ypos 0.9
    if lust_points[17] >=5:
        show topred:
            xpos 0.02 ypos 0.9
    call screen nikkisheetb
    hide nikki02
    hide topred
    hide exitred
    return

screen nikkisheetb:
    add nikkiblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("NikkiTopoff")

label NikkiTopoff:
    hide topred
    call screen nikkisheetc
    return

screen nikkisheetc:
    add nikkiblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Pamelasheet:    
    scene
    show pamela02
    show exitorange:
        xpos 0.37 ypos 0.9
    if lust_points[18] >=5:
        show toporange:
            xpos 0.02 ypos 0.9
    call screen pamelasheetb
    hide pamela02
    hide toporange
    hide exitorange
    return

screen pamelasheetb:
    add pamelablinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("PamelaTopoff")

label PamelaTopoff:
    hide toporange
    call screen pamelasheetc
    return

screen pamelasheetc:
    add pamelablinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Sandysheet:    
    scene
    show sandy02
    show exitred:
        xpos 0.37 ypos 0.9
    if lust_points[19] >=5:
        show topred:
            xpos 0.02 ypos 0.9
    call screen sandysheetb
    hide sandy02
    hide topred
    hide exitred
    return

screen sandysheetb:
    add sandyblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("SandyTopoff")

label SandyTopoff:
    hide topred
    call screen sandysheetc
    return

screen sandysheetc:
    add sandyblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Sophiasheet:    
    scene
    show sophia02
    show exitred:
        xpos 0.37 ypos 0.9
    if lust_points[20] >=5:
        show topred:
            xpos 0.02 ypos 0.9
    call screen sophiasheetb
    hide sophia02
    hide topred
    hide exitred
    return

screen sophiasheetb:
    add sophiablinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("SophiaTopoff")

label SophiaTopoff:
    hide topred
    call screen sophiasheetc
    return

screen sophiasheetc:
    add sophiablinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Tanyasheet:    
    scene
    show tanya02
    show exityellow:
        xpos 0.37 ypos 0.9
    if lust_points[21] >=5:
        show topyellow:
            xpos 0.02 ypos 0.9
    call screen tanyasheetb
    hide tanya02
    hide topyellow
    hide exityellow
    return

screen tanyasheetb:
    add tanyablinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("TanyaTopoff")

label TanyaTopoff:
    hide topyellow
    call screen tanyasheetc
    return

screen tanyasheetc:
    add tanyablinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Teagansheet:    
    scene
    show teagan02
    show exitorange:
        xpos 0.37 ypos 0.9
    if lust_points[22] >=5:
        show toporange:
            xpos 0.02 ypos 0.9
    call screen teagansheetb
    hide teagan02
    hide toporange
    hide exitorange
    return

screen teagansheetb:
    add teaganblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("TeaganTopoff")

label TeaganTopoff:
    hide toporange
    call screen teagansheetc
    return

screen teagansheetc:
    add teaganblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

label Vivianesheet:    
    scene
    show viviane02
    show exitred:
        xpos 0.37 ypos 0.9
    if lust_points[23] >=5:
        show topred:
            xpos 0.02 ypos 0.9
    call screen vivianesheetb
    hide viviane02
    hide topred
    hide exitred
    return

screen vivianesheetb:
    add vivianeblinking
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action [renpy.music.stop, Return()]
    button:
        xpos .02
        ypos .9
        xysize(120, 40)      
        action ui.callsinnewcontext("VivianeTopoff")

label VivianeTopoff:
    hide topred
    call screen vivianesheetc
    return

screen vivianesheetc:
    add vivianeblinkingb
    button:
        xpos .37
        ypos .9
        xysize(120, 40)      
        action Return()

################################################################################
## Achievement Screens
################################################################################

label display_achievement_menu:
    call screen achievement_menu
    return

screen achievement_menu():
    add "Achievements/achievementbackground.jpg"
    add "Icons/exit.png"
    $ renpy.music.play('Sounds/factory.mp3')

    if achievement.has("milehigh"):
        imagebutton:
            focus_mask True
            idle "Achievements/milehighidle.png"
            hover "Achievements/milehighhover.png"
            action [Jump ("AchievementMileHigh")]

    if achievement.has("mfucker"):
        imagebutton:
            focus_mask True
            idle "Achievements/mfuckeridle.png"
            hover "Achievements/mfuckerhover.png"
            action [Jump ("AchievementFucker")]

    if achievement.has("classroom"):
        imagebutton:
            focus_mask True
            idle "Achievements/classroomidle.png"
            hover "Achievements/classroomhover.png"
            action [Jump ("AchievementClassroom")]

    if achievement.has("asian"):
        imagebutton:
            focus_mask True
            idle "Achievements/asianidle.png"
            hover "Achievements/asianhover.png"
            action [Jump ("AchievementAsian")]

    if achievement.has("colonizer"):
        imagebutton:
            focus_mask True
            idle "Achievements/colonizeridle.png"
            hover "Achievements/colonizerhover.png"
            action [Jump ("AchievementColonizer")]

    if achievement.has("student"):
        imagebutton:
            focus_mask True
            idle "Achievements/studentidle.png"
            hover "Achievements/studenthover.png"
            action [Jump ("AchievementStudent")]

    if achievement.has("homesteader"):
        imagebutton:
            focus_mask True
            idle "Achievements/homeidle.png"
            hover "Achievements/homehover.png"
            action [Jump ("AchievementHomesteader")]

    if achievement.has("lawbreaker"):
        imagebutton:
            focus_mask True
            idle "Achievements/lawbreakeridle.png"
            hover "Achievements/lawbreakerhover.png"
            action [Jump ("AchievementLawbreaker")]

    if achievement.has("hunter"):
        imagebutton:
            focus_mask True
            idle "Achievements/hunteridle.png"
            hover "Achievements/hunterhover.png"
            action [Jump ("AchievementHunter")]

    if achievement.has("faculty"):
        imagebutton:
            focus_mask True
            idle "Achievements/facultyidle.png"
            hover "Achievements/facultyhover.png"
            action [Jump ("AchievementFaculty")]

    if achievement.has("cockblocker"):
        imagebutton:
            focus_mask True
            idle "Achievements/cockblockeridle.png"
            hover "Achievements/cockblockerhover.png"
            action [Jump ("AchievementCockblocker")]

    if achievement.has("cuckmaker"):
        imagebutton:
            focus_mask True
            idle "Achievements/cuckmakeridle.png"
            hover "Achievements/cuckmakerhover.png"
            action [Jump ("AchievementCuckmaker")]

    if achievement.has("king"):
        imagebutton:
            focus_mask True
            idle "Achievements/kingidle.png"
            hover "Achievements/kinghover.png"
            action [Jump ("AchievementKing")]

    if achievement.has("bosom"):
        imagebutton:
            focus_mask True
            idle "Achievements/bosomidle.png"
            hover "Achievements/bosomhover.png"
            action [Jump ("AchievementBosom")]

    if achievement.has("peeper"):
        imagebutton:
            focus_mask True
            idle "Achievements/peeperidle.png"
            hover "Achievements/peeperhover.png"
            action [Jump ("AchievementPeeper")]

    if achievement.has("grabber"):
        imagebutton:
            focus_mask True
            idle "Achievements/grabberidle.png"
            hover "Achievements/grabberhover.png"
            action [Jump ("AchievementGrabber")]

    if achievement.has("watersport"):
        imagebutton:
            focus_mask True
            idle "Achievements/wateridle.png"
            hover "Achievements/waterhover.png"
            action [Jump ("AchievementWatersport")]

    if achievement.has("banger"):
        imagebutton:
            focus_mask True
            idle "Achievements/bangeridle.png"
            hover "Achievements/bangerhover.png"
            action [Jump ("AchievementBanger")]
            
    if achievement.has("muscleman"):
        imagebutton:
            focus_mask True
            idle "Achievements/musclemanidle.png"
            hover "Achievements/musclemanhover.png"
            action [Jump ("AchievementMuscleman")]

    if achievement.has("threesomer"):
        imagebutton:
            focus_mask True
            idle "Achievements/threesomeridle.png"
            hover "Achievements/threesomerhover.png"
            action [Jump ("AchievementThreesome")]

    if achievement.has("brickhouse"):
        imagebutton:
            focus_mask True
            idle "Achievements/brickhouseidle.png"
            hover "Achievements/brickhousehover.png"
            action [Jump ("AchievementBrickhouse")]

    if achievement.has("conqueror"):
        imagebutton:
            focus_mask True
            idle "Achievements/conqueroridle.png"
            hover "Achievements/conquerorhover.png"
            action [Jump ("AchievementConqueror")]

    if achievement.has("ultimate"):
        imagebutton:
            focus_mask True
            idle "Achievements/ultimateidle.png"
            hover "Achievements/ultimatehover.png"
            action [Jump ("AchievementUltimate")]

    if achievement.has("extrasontheside"):
        imagebutton:
            focus_mask True
            idle "Achievements/extrasidle.png"
            hover "Achievements/extrashover.png"
            action [Jump ("AchievementExtras")]

    button:
        xpos .83
        ypos .9
        xysize(100, 50)        
        action [renpy.music.stop, Return()]
    

label AchievementMileHigh:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement01.ogv" loop
    show movie
    show exit
    call screen milehigh
    screen milehigh:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementFucker:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement02.ogv" loop
    show movie
    show exit
    call screen fucker
    screen fucker:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementClassroom:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement03.ogv" loop
    show movie
    show exit
    call screen classroom
    screen classroom:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementAsian:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement04.ogv" loop
    show movie
    show exit
    call screen asian
    screen asian:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementColonizer:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement05.ogv" loop
    show movie
    show exit
    call screen colonizer
    screen colonizer:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementStudent:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement06.ogv" loop
    show movie
    show exit
    call screen student
    screen student:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementHomesteader:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement07.ogv" loop
    show movie
    show exit
    call screen student
    screen student:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementLawbreaker:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement08.ogv" loop
    show movie
    show exit
    call screen lawbreaker
    screen lawbreaker:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return
    
label AchievementHunter:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement09.ogv" loop
    show movie
    show exit
    call screen milfhunter
    screen milfhunter:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return
    
label AchievementFaculty:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement10.ogv" loop
    show movie
    show exit
    call screen faculty
    screen faculty:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return
    
label AchievementCuckmaker:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement12.ogv" loop
    show movie
    show exit
    call screen cuckmaker
    screen cuckmaker:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return
    
label AchievementCockblocker:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement11.ogv" loop
    show movie
    show exit
    call screen cockblocker
    screen cockblocker:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return
    
label AchievementKing:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement13.ogv" loop
    show movie
    show exit
    call screen king
    screen king:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementBosom:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement14.ogv" loop
    show movie
    show exit
    call screen bosom
    screen bosom:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return
        
label AchievementPeeper:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement15.ogv" loop
    show movie
    show exit
    call screen bosom
    screen bosom:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementGrabber:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement16.ogv" loop
    show movie
    show exit
    call screen bosom
    screen bosom:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementWatersport:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement18.ogv" loop
    show movie
    show exit
    call screen bosom
    screen bosom:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementBanger:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement19.ogv" loop
    show movie
    show exit
    call screen bosom
    screen bosom:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementMuscleman:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement20.ogv" loop
    show movie
    show exit
    call screen musclemans
    screen musclemans:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementThreesome:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement21.ogv" loop
    show movie
    show exit
    call screen threesomes
    screen threesomes:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementConqueror:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement23.ogv" loop
    show movie
    show exit
    call screen conquerors
    screen conquerors:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementUltimate:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement24.ogv" loop
    show movie
    show exit
    call screen ultimates
    screen ultimates:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementExtras:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement17.ogv" loop
    show movie
    show exit
    call screen extrass
    screen extrass:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return

label AchievementBrickhouse:    
    stop music
    scene
    play music "Sounds/milehigh.mp3"
    play movie "Achievements/achievement22.ogv" loop
    show movie
    show exit
    call screen brickhouseb
    screen brickhouseb:
        modal True
        button:
            xpos .83
            ypos .9
            xysize(100, 50)      
            action [renpy.music.stop, Return()]
    return


################################################################################
## Gallery Screens
################################################################################


label display_gallery_menu:
    stop music
    scene CGbackground
    call screen gallery_menu
    return

label display_gallery_menu02:
    scene CGbackground
    call screen gallery_menu02
    return

screen gallery_menu():
    #add "Gallery/CGbackground.jpg"

    imagebutton:
        focus_mask True
        idle "Gallery/sex01hover.png"
        hover "Gallery/sex01hover.png"
        action ui.callsinnewcontext ("Sex01")
    imagebutton:
        focus_mask True
        idle "Gallery/sex02hover.png"
        hover "Gallery/sex02hover.png"
        action ui.callsinnewcontext ("Sex02")
    imagebutton:
        focus_mask True
        idle "Gallery/sex03hover.png"
        hover "Gallery/sex03hover.png"
        action ui.callsinnewcontext ("Sex03")
    imagebutton:
        focus_mask True
        idle "Gallery/sex04hover.png"
        hover "Gallery/sex04hover.png"
        action ui.callsinnewcontext ("Sex04")
    imagebutton:
        focus_mask True
        idle "Gallery/sex05hover.png"
        hover "Gallery/sex05hover.png"
        action ui.callsinnewcontext ("Sex05")
    imagebutton:
        focus_mask True
        idle "Gallery/sex06hover.png"
        hover "Gallery/sex06hover.png"
        action ui.callsinnewcontext ("Sex06")
    imagebutton:
        focus_mask True
        idle "Gallery/sex07hover.png"
        hover "Gallery/sex07hover.png"
        action ui.callsinnewcontext ("Sex07")
    imagebutton:
        focus_mask True
        idle "Gallery/sex08hover.png"
        hover "Gallery/sex08hover.png"
        action ui.callsinnewcontext ("Sex08")
    imagebutton:
        focus_mask True
        idle "Gallery/sex09hover.png"
        hover "Gallery/sex09hover.png"
        action ui.callsinnewcontext ("Sex09")
    imagebutton:
        focus_mask True
        idle "Gallery/sex10hover.png"
        hover "Gallery/sex10hover.png"
        action ui.callsinnewcontext ("Sex10")
    imagebutton:
        focus_mask True
        idle "Gallery/sex11hover.png"
        hover "Gallery/sex11hover.png"
        action ui.callsinnewcontext ("Sex11")
    imagebutton:
        focus_mask True
        idle "Gallery/sex12hover.png"
        hover "Gallery/sex12hover.png"
        action ui.callsinnewcontext ("Sex12")
    imagebutton:
        focus_mask True
        idle "Gallery/sex13hover.png"
        hover "Gallery/sex13hover.png"
        action ui.callsinnewcontext ("Sex13")
    imagebutton:
        focus_mask True
        idle "Gallery/sex14hover.png"
        hover "Gallery/sex14hover.png"
        action ui.callsinnewcontext ("Sex14")
    imagebutton:
        focus_mask True
        idle "Gallery/sex15hover.png"
        hover "Gallery/sex15hover.png"
        action ui.callsinnewcontext ("Sex15")
    imagebutton:
        focus_mask True
        idle "Gallery/sex16hover.png"
        hover "Gallery/sex16hover.png"
        action ui.callsinnewcontext ("Sex16")
    imagebutton:
        focus_mask True
        idle "Gallery/sex17hover.png"
        hover "Gallery/sex17hover.png"
        action ui.callsinnewcontext ("Sex17")
    imagebutton:
        focus_mask True
        idle "Gallery/sex18hover.png"
        hover "Gallery/sex18hover.png"
        action ui.callsinnewcontext ("Sex18")
    imagebutton:
        focus_mask True
        idle "Gallery/sex19hover.png"
        hover "Gallery/sex19hover.png"
        action ui.callsinnewcontext ("Sex19")
    imagebutton:
        focus_mask True
        idle "Gallery/sex20hover.png"
        hover "Gallery/sex20hover.png"
        action ui.callsinnewcontext ("Sex20")
    imagebutton:
        focus_mask True
        idle "Gallery/sex21hover.png"
        hover "Gallery/sex21hover.png"
        action ui.callsinnewcontext ("Sex21")
    imagebutton:
        focus_mask True
        idle "Gallery/sex22hover.png"
        hover "Gallery/sex22hover.png"
        action ui.callsinnewcontext ("Sex22")
    imagebutton:
        focus_mask True
        idle "Gallery/sex23hover.png"
        hover "Gallery/sex23hover.png"
        action ui.callsinnewcontext ("Sex23")
    imagebutton:
        focus_mask True
        idle "Gallery/sex24hover.png"
        hover "Gallery/sex24hover.png"
        action ui.callsinnewcontext ("Sex24")
    imagebutton:
        focus_mask True
        idle "Gallery/sex25hover.png"
        hover "Gallery/sex25hover.png"
        action ui.callsinnewcontext ("Sex25")
    imagebutton:
        focus_mask True
        idle "Gallery/sex26hover.png"
        hover "Gallery/sex26hover.png"
        action ui.callsinnewcontext ("Sex26")
    imagebutton:
        focus_mask True
        idle "Gallery/sex27hover.png"
        hover "Gallery/sex27hover.png"
        action ui.callsinnewcontext ("Sex27")
    imagebutton:
        focus_mask True
        idle "Gallery/sex28hover.png"
        hover "Gallery/sex28hover.png"
        action ui.callsinnewcontext ("Sex28")
    imagebutton:
        focus_mask True
        idle "Gallery/sex29hover.png"
        hover "Gallery/sex29hover.png"
        action ui.callsinnewcontext ("Sex29")
    imagebutton:
        focus_mask True
        idle "Gallery/sex30hover.png"
        hover "Gallery/sex30hover.png"
        action ui.callsinnewcontext ("Sex30")
    imagebutton:
        focus_mask True
        idle "Gallery/sex31hover.png"
        hover "Gallery/sex31hover.png"
        action ui.callsinnewcontext ("Sex31")
    imagebutton:
        focus_mask True
        idle "Gallery/sex32hover.png"
        hover "Gallery/sex32hover.png"
        action ui.callsinnewcontext ("Sex32")
    imagebutton:
        focus_mask True
        idle "Gallery/sex33hover.png"
        hover "Gallery/sex33hover.png"
        action ui.callsinnewcontext ("Sex33")
    imagebutton:
        focus_mask True
        idle "Gallery/sex34hover.png"
        hover "Gallery/sex34hover.png"
        action ui.callsinnewcontext ("Sex34")
    imagebutton:
        focus_mask True
        idle "Gallery/sex35hover.png"
        hover "Gallery/sex35hover.png"
        action ui.callsinnewcontext ("Sex35")
    imagebutton:
        focus_mask True
        idle "Gallery/sex36hover.png"
        hover "Gallery/sex36hover.png"
        action ui.callsinnewcontext ("Sex36")
    imagebutton:
        focus_mask True
        idle "Gallery/sex37hover.png"
        hover "Gallery/sex37hover.png"
        action ui.callsinnewcontext ("Sex37")
    imagebutton:
        focus_mask True
        idle "Gallery/sex38hover.png"
        hover "Gallery/sex38hover.png"
        action ui.callsinnewcontext ("Sex38")
    imagebutton:
        focus_mask True
        idle "Gallery/sex39hover.png"
        hover "Gallery/sex39hover.png"
        action ui.callsinnewcontext ("Sex39")
    imagebutton:
        focus_mask True
        idle "Gallery/sex40hover.png"
        hover "Gallery/sex40hover.png"
        action ui.callsinnewcontext ("Sex40")
    imagebutton:
        focus_mask True
        idle "Gallery/sex41hover.png"
        hover "Gallery/sex41hover.png"
        action ui.callsinnewcontext ("Sex41")
    imagebutton:
        focus_mask True
        idle "Gallery/sex42hover.png"
        hover "Gallery/sex42hover.png"
        action ui.callsinnewcontext ("Sex42")
    imagebutton:
        focus_mask True
        idle "Gallery/sex43hover.png"
        hover "Gallery/sex43hover.png"
        action ui.callsinnewcontext ("Sex43")
    imagebutton:
        focus_mask True
        idle "Gallery/sex44hover.png"
        hover "Gallery/sex44hover.png"
        action ui.callsinnewcontext ("Sex44")
    imagebutton:
        focus_mask True
        idle "Gallery/sex45hover.png"
        hover "Gallery/sex45hover.png"
        action ui.callsinnewcontext ("Sex45")
    imagebutton:
        focus_mask True
        idle "Gallery/sex46hover.png"
        hover "Gallery/sex46hover.png"
        action ui.callsinnewcontext ("Sex46")
    imagebutton:
        focus_mask True
        idle "Gallery/sex47hover.png"
        hover "Gallery/sex47hover.png"
        action ui.callsinnewcontext ("Sex47")
    imagebutton:
        focus_mask True
        idle "Gallery/sex48hover.png"
        hover "Gallery/sex48hover.png"
        action ui.callsinnewcontext ("Sex48")
    imagebutton:
        focus_mask True
        idle "Gallery/sex49hover.png"
        hover "Gallery/sex49hover.png"
        action ui.callsinnewcontext ("Sex49")
    imagebutton:
        focus_mask True
        idle "Gallery/sex50hover.png"
        hover "Gallery/sex50hover.png"
        action ui.callsinnewcontext ("Sex50")
    imagebutton:
        focus_mask True
        idle "Gallery/sex51hover.png"
        hover "Gallery/sex51hover.png"
        action ui.callsinnewcontext ("Sex51")
    imagebutton:
        focus_mask True
        idle "Gallery/sex52hover.png"
        hover "Gallery/sex52hover.png"
        action ui.callsinnewcontext ("Sex52")
    imagebutton:
        focus_mask True
        idle "Gallery/sex53hover.png"
        hover "Gallery/sex53hover.png"
        action ui.callsinnewcontext ("Sex53")
    imagebutton:
        focus_mask True
        idle "Gallery/sex54hover.png"
        hover "Gallery/sex54hover.png"
        action ui.callsinnewcontext ("Sex54")
    imagebutton:
        focus_mask True
        idle "Gallery/sex55hover.png"
        hover "Gallery/sex55hover.png"
        action ui.callsinnewcontext ("Sex55")
    imagebutton:
        focus_mask True
        idle "Gallery/sex56hover.png"
        hover "Gallery/sex56hover.png"
        action ui.callsinnewcontext ("Sex56")
    imagebutton:
        focus_mask True
        idle "Gallery/sex57hover.png"
        hover "Gallery/sex57hover.png"
        action ui.callsinnewcontext ("Sex57")
    imagebutton:
        focus_mask True
        idle "Gallery/sex58hover.png"
        hover "Gallery/sex58hover.png"
        action ui.callsinnewcontext ("Sex58")
    imagebutton:
        focus_mask True
        idle "Gallery/sex59hover.png"
        hover "Gallery/sex59hover.png"
        action ui.callsinnewcontext ("Sex59")
    imagebutton:
        focus_mask True
        idle "Gallery/sex60hover.png"
        hover "Gallery/sex60hover.png"
        action ui.callsinnewcontext ("Sex60")
    imagebutton:
        focus_mask True
        idle "Gallery/sex61hover.png"
        hover "Gallery/sex61hover.png"
        action ui.callsinnewcontext ("Sex61")
    imagebutton:
        focus_mask True
        idle "Gallery/sex62hover.png"
        hover "Gallery/sex62hover.png"
        action ui.callsinnewcontext ("Sex62")
    imagebutton:
        focus_mask True
        idle "Gallery/sex62hover.png"
        hover "Gallery/sex62hover.png"
        action ui.callsinnewcontext ("Sex62")
    imagebutton:
        focus_mask True
        idle "Gallery/sex63hover.png"
        hover "Gallery/sex63hover.png"
        action ui.callsinnewcontext ("Sex63")
    imagebutton:
        focus_mask True
        idle "Gallery/sex64hover.png"
        hover "Gallery/sex64hover.png"
        action ui.callsinnewcontext ("Sex64")
    imagebutton:
        focus_mask True
        idle "Gallery/exit.png"
        hover "Gallery/exit.png"
        action [renpy.music.stop, Return()]
    imagebutton:
        focus_mask True
        idle "Gallery/nextpage.png"
        hover "Gallery/nextpage.png"
        action [Jump ("display_gallery_menu02")]
 
screen gallery_menu02():

    imagebutton:
        focus_mask True
        idle "Gallery/sex65hover.png"
        hover "Gallery/sex65hover.png"
        action ui.callsinnewcontext ("Sex65")
    imagebutton:
        focus_mask True
        idle "Gallery/sex66hover.png"
        hover "Gallery/sex66hover.png"
        action ui.callsinnewcontext ("Sex66")
    imagebutton:
        focus_mask True
        idle "Gallery/sex67hover.png"
        hover "Gallery/sex67hover.png"
        action ui.callsinnewcontext ("Sex67")
    imagebutton:
        focus_mask True
        idle "Gallery/sex68hover.png"
        hover "Gallery/sex68hover.png"
        action ui.callsinnewcontext ("Sex68")
    imagebutton:
        focus_mask True
        idle "Gallery/sex69hover.png"
        hover "Gallery/sex69hover.png"
        action ui.callsinnewcontext ("Sex69")
    imagebutton:
        focus_mask True
        idle "Gallery/sex70hover.png"
        hover "Gallery/sex70hover.png"
        action ui.callsinnewcontext ("Sex70")
    imagebutton:
        focus_mask True
        idle "Gallery/sex71hover.png"
        hover "Gallery/sex71hover.png"
        action ui.callsinnewcontext ("Sex71")
    imagebutton:
        focus_mask True
        idle "Gallery/sex72hover.png"
        hover "Gallery/sex72hover.png"
        action ui.callsinnewcontext ("Sex72")
    imagebutton:
        focus_mask True
        idle "Gallery/sex73hover.png"
        hover "Gallery/sex73hover.png"
        action ui.callsinnewcontext ("Sex73")
    imagebutton:
        focus_mask True
        idle "Gallery/sex74hover.png"
        hover "Gallery/sex74hover.png"
        action ui.callsinnewcontext ("Sex74")
    imagebutton:
        focus_mask True
        idle "Gallery/sex75hover.png"
        hover "Gallery/sex75hover.png"
        action ui.callsinnewcontext ("Sex75")
    imagebutton:
        focus_mask True
        idle "Gallery/sex76hover.png"
        hover "Gallery/sex76hover.png"
        action ui.callsinnewcontext ("Sex76")
    imagebutton:
        focus_mask True
        idle "Gallery/sex77hover.png"
        hover "Gallery/sex77hover.png"
        action ui.callsinnewcontext ("Sex77")
    imagebutton:
        focus_mask True
        idle "Gallery/exit.png"
        hover "Gallery/exit.png"
        action [renpy.music.stop, Return()]
    imagebutton:
        focus_mask True
        idle "Gallery/previouspage.png"
        hover "Gallery/previouspage.png"
        action [Jump ("display_gallery_menu")]
 
label Sex01:    
stop music
scene plane03
$ renpy.pause(1.0, hard=True)
p "Damn, this hot stewardess made me hard!"
$ hostessfuckb = False
$ hostessblowjobb = False
play sound "Sounds/dooropen.mp3"
$ renpy.pause(1.0, hard=True)
scene plane04 with dissolve
$ renpy.pause(1.0, hard=True)
h "OMG, that's the biggest cock I've ever seen!"
h "What could I do to make it go down before we land?"
menu:
    "You could suck me and swallow my load!":
        jump HostessBlowjobb

    "You could bend over and take it deep in your pussy!":
        jump HostessFuckb

label HostessBlowjobb:
play music "Sounds/planetitfuck.mp3"
show movieplanetitfuck with dissolve
show cum
call screen planetitfuckb
screen planetitfuckb:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PlaneTitFuckCumb")
label PlaneTitFuckCumb:
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
$ hostessblowjobb = True

if hostessfuckb == False:
    h "Fuck, that was a GIANT load of cum!"
    h "Too bad, I would have loved to take that massive young piece of meat up my pussy..."
    p "Who says I can't go again?"
    h "What??? You're ready to pump me again so soon? Fuck me like the wild animal you are stud!"
    p "Sure thing, buckle up for a wild ride!"
    jump HostessFuckb
else:
    h "Wow, another GIANT load of cum that filled me up like a three-course meal!"
    h "You were amazing [name], but we'd better hurry back to our seats!"
    return

label HostessFuckb:
play music "Sounds/planefuck.mp3"
show movieplanefuckslow
show faster
call screen planefuckslowb
screen planefuckslowb:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("PlaneFuckFastb")
label PlaneFuckFastb:
hide faster
show movieplanefuckfast
show cum
call screen planefuckfastb
screen planefuckfastb:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("HostessFuckCumb")
label HostessFuckCumb:
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
$ hostessfuckb = True

if hostessblowjobb == False:
    h "Damn kid, you filled me up with a massive load of young virile cum and you're still cumming buckets all over my back!"
    h "Too bad, I would have loved to taste that lovely load in my mouth..."
    p "Who says I can't go again?"
    h "What??? You're ready to cum again so soon? Face-fuck me like the wild animal you are stud!"
    p "Of course, open wide and say \"AAAh!\""
    jump HostessBlowjobb
else:
    h "Damn kid, where do you store all that cum? I'm bloated with your second huge load!"
    h "You were amazing [name], but we'd better hurry back to our seats!"
    return

label Sex02:
stop music
scene randybeachsandy02
$ renpy.pause(1.0, hard=True)
sa"Isn't it wonderful? The curves of the waves as they rumble ashore..."
p "Oh yeah, the curves are beautiful..."
show randybeachsandy03 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/distantfuck.mp3"
sa"It's beautiful in the late afternoon, so quiet and peaceful..."
play sound "Sounds/distantfuck.mp3"
p "Hmm, not so quiet, some people seem to be having some raunchy fun not far away..."
sa"Oh God, these two have been at it for hours! I didn't even know it was possible..."
p "Oh, it's possible... If the guy is a total stud..."
sa"Oh, and you know that because..."
p "...I'm a total stud..."
scene randybeachsandy05 with dissolve
$ renpy.pause(1.0, hard=True)
sa"Well, you're certainly way bigger than my last boyfriend..."
sa"He was sssoo tiny, and spent his whole evenings being a whiny little bitch troll on f95zone.com..."
p "I decline all legal responsibility for what you just said."
sa"I want to see this monster get hard as a rock..."
scene randybeachsandy06 with dissolve
$ renpy.pause(1.0, hard=True)
sa"Damn [name], it's so big... You like it when I tease your cockhead with my fingers like that?"
p "Yes! It's so excruciating... Puff... Keep going, I'm gonna blow anytime now..."
sa"I want this to last a little bit longer... What would be the fun otherwise?"
p "Oh shit Sandy, I can't....This is too much..."
sa"OK, I'll jack that monstercock off until you get the release you deserve..."
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
sa"Mmmh, look at all that young spunk flying everywhere.. Gimme more, I want MORE..."
p "FUCKKKK...Still CUMMING!!!!"
sa"We're gonna need to get cleaned up with the mess you made!..."
scene randybeachsandy03b with dissolve
$ renpy.pause(1.0, hard=True)
sa"I should go now, it's getting late...I hope to see you again..."
sa"But before that, kiss me tenderly..."
play sound "Sounds/kissing.mp3"
scene randybeachsandykisscum with dissolve
p "Where will you be?"
sa"I'll be around...We'll meet again my Prince Charming..."
return

label Sex03:
stop music
scene randybeachcouple01
show randybeachparasol03
$ renpy.pause(1.0, hard=True)
p "Now let's see what's hiding behind this parasol..."
hide randybeachparasol03 with moveoutright
$ renpy.pause(1.0, hard=True)
rc"Hey, can't we have some privacy here? It's called \"Randy Beach\" for a reason!"
p "Your boyfriend has such a small dick, it's laughable."
rc"Yeah, as if. My boyfriend is a total stud and we'll prove it."
rb "Watch and learn boy as I fuck my girlfriend senseless with my young monstercock!"        
play music "Sounds/randybeachchickmoaning.mp3"
scene randybeachcouplefuck with dissolve
$ renpy.pause(1.0, hard=True)
rc"Oh God, you fuck me so good with that huge cock of yours!"
rb "Are you getting this, that's how you give a woman plenty of pleasure!"
rb "Now I'm gonna dump a massive load of my virile cum inside her and all over her back. Watch!"
stop music
play music "Sounds/randybeachsound.mp3"
scene randybeachcouplecum with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/randyboycumming.mp3"
rb "Ah FUCK, SSOO good!"
rc"Look at all those massive cumshots flying everywhere after he totally filled me with ounces of boycream already!"
rb "See how much I come? And you know what? I'm still HARD and READY to fuck my girlfriend some more!"
rc"Mmmh, such a STUD! Are you a stud? How about you come and fuck my arse and show me if you are?"
rb "How does that sound boy, ready for some threesome fun with my girlfriend?"
p "Yeah, count me in!"
scene randybeachcouplethreesome with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/threesomefuck.mp3"
rc"Oh Lord have mercy! Two GIANT young cocks in my holes... t...ttooo fucking much!"
p "Arse...gripping...so tight... can't..hold...BACK!"
scene randybeachcouplethreesomecum with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(2.0, hard=True)
p "FUCK, you made me cum in no time, can't stop spewing my sauce! AAAH!"
rc"Hey, watch out, I didn't say you could spew your filthy scum all over me!"
rb "Dude, you don't know how to treat girls with respect... "
rb "Learn from me, I'm still pounding her sweet pussy and I'll do it all afternoon until she comes over and over again on my giant boymeat..."
p "Damn, I'm totally spent, her arse was gripping too tight, she totally sucked the cum out of my balls!"
rc"Can't keep it up? Then you're useless to me, leave us alone while I ride my horse-hung boyfriend to countless orgasms!"
rb "Don't worry baby, I've got a few more loads in me, we can keep at it for hours!"
rc"Oh, I'm counting on it stud, I want to coax at least a dozen more massive loads of cum from that stallion cock of yours before the end of the day!"
p "Jeezus, what a crazy nympho, I'm out of here..."
return

label Sex05:
stop music
scene principal01
$ renpy.pause(1.0, hard=True)
p "(Holy cow! Sis wasn't kidding about her tits, they're huge!)"
so "[name] Johnson? Ah, yes, one of our new students from New Major City..."
p "Yeah, whatever."
so "Yes MA'AM. You will learn to show respect or you will not last long in our school."
scene principal02 with dissolve
$ renpy.pause(1.0, hard=True)
so "From what I read, you're a pretty average student..."
p "I've got a big sausage that's not average."
so "...in the academic department. This is a school, not a stripclub."
so "But perhaps you are indeed distracted by raging hormones and find it hard to concentrate on your studies?"
scene principal03 with dissolve
$ renpy.pause(1.0, hard=True)
so "For example, right now, I can see you eyeing out my generous bosom..."    
p "Well, they are kind of sticking out..."
so "These babies are what will get me elected in the senate... And what will get you to obey me..."
so "So here's the deal... You concentrate on your studies and you don't go around chasing all the girls to try and fuck them with that fat log I can see growing in your pants..."
so "Or you'll be stuck with me every afternoon, to get some GUIDANCE on how to improve your grades..."
p "I make no such promise, I'll fuck whoever I want! I'm da MAN!"
so "(sigh)... I see, I thought it would come down to this..."
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
scene principal07 with dissolve
$ renpy.pause(1.0, hard=True)
so "Now give that hard cock of yours a breather... The poor thing is straining against your shorts... And go and sit on the sofa while I get ready for your \"guidance\" session..."
scene principal08 with dissolve
$ renpy.pause(1.0, hard=True)
so "I don't recall telling you to put your hand on that thing, take it off!"
so "Just look at it, hard with lust, ready to explode and pump its mighty load all over my feet..."
so "Get ready slave boy!"
scene principal09 with dissolve
$ renpy.pause(1.0, hard=True)
so "Now focus on my legs and my feet as they tame your lusty shaft..."
stop music
play music "Sounds/principalslow01.mp3"
show moviefootjobslow
show faster
call screen principalfootjobb
screen principalfootjobb:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("FootJobFastb")

label FootJobFastb:
stop music
hide faster
play music "Sounds/principalfast01.mp3"
show moviefootjobfast
show cum
call screen footjobfasterb
screen footjobfasterb:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PrincipalCumb")

label PrincipalCumb:
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
so "I need to get cleaned up. Off you go, your next appointment is with nurse Bigguns down the hallway for your physical check-up."
return

label Sex04:
stop music
scene nurse01
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
je "I would like you to... get hard and give me a sperm sample. Can you do that for me?"
scene nurse07b with dissolve
$ renpy.pause(1.0, hard=True)
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
p "Wank me if you want my cum!"
je "God, you are so... demanding... I need a free hand to hold the cup, so I'll just hold your cockhead, but you wank that monster yourself."
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
scene nurse16 with dissolve
$ renpy.pause(1.0, hard=True)
je "Hum, I must say, it tastes... good... Oh God, I'm so ashamed of myself..."
je "Err, thanks for filling the cup... to overflowing... I'll be sending it to the lab for analysis... Off you go, lunch time is soon."
return

label Sex08:
stop music
scene parlour01
$ renpy.pause(1.0, hard=True)
play music "Sounds/parlourmusic.mp3"
ka "Welcome big American boy to \"Misohawny Massage Parlour\"! Me Katsumi, you want massage?"
p "I was told you did \"full-body massage\"..."
ka "Yes, sucky sucky 50 dolla."
p "Ah, I see. Sucky sucky indeed. That's quite expensive for just sucky sucky."
ka "Me love you long time. For you, more than sucky sucky."
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
ka "Oooh, cock getting VERY BIG. Bad boy."
p "Why don't you massage it then like if it was one of my big tense muscles?..."
ka "Oooh, boy very smart. OK, me gonna massage big American cock."
ka "Big American boy! Take clothes off. Me come back sexy for you."
p "Can't wait to get some sucky sucky from her... I'd better get my phone camera ready..."
scene parlour04
$ renpy.pause(1.0, hard=True)
ka "Ooh, cock ssooo big... Me never seen cock so big before."
p "It's still soft, it gets much bigger...."
ka "Cock too big. Monster cock. Me only do sucky sucky."
p "We'll make it fit."
ka "No, you kill me with monster American boy cock!"
p "I'll be gentle..."
ka "Ok, me do sucky sucky and then me see if fucky fucky good."
scene parlour05 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Big American monster boycock so big and hard!"
p "Yeah, play with it Katsumi! It's all yours!"
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
scene parlour07 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Me gonna lick huge balls first... Sssoo tasty and spicy, like chicken Sichuan."
play sound "Sounds/lick.mp3"
p "Everything really DOES taste like chicken after all..."
scene parlour08 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Reaching top of monstercock take me so long... Me love you long time!"
p "Keep going, you still have quite a few inches to go..."
scene parlour09 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Oooh, lot of precum on monster boycock! You so virile!"
p "That's cos my balls are full... full of hot cum for you!"
scene parlour10 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Me take clothes off. Oooh, look at big American cock twitch!"
stop music
play music "Sounds/katsumifuck.mp3"
show movieparlourfuck
show cum
call screen parlourfuckcumx
screen parlourfuckcumx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("ParlourCum01x")

label ParlourCum01x:
stop music
hide movieparlourfuck
scene parlourcum01
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
ka "You filling me up with so much boyjuice! You so incredible!"
play sound "Sounds/ryancumming.mp3"
scene parlourcum02 with dissolve
$ renpy.pause(1.0, hard=True)
ka "Look! Cum flowing from my Asian pussy ssooo much! Cum everywhere! Me need to get cleaned up for next client now!"
p "Fuck, you rode me like a wild bronco... I'm exhausted!"
return

label Sex06:
stop music
play music "Sounds/gymmusic.mp3"
scene chantellegym01
$ renpy.pause(1.0, hard=True)
p "Chantelle is doing some curls... She hasn't seen me come in."
scene chantellegym02 with dissolve
$ renpy.pause(2.0, hard=True)
p "Wow, Chantelle has such a fine body, nice big round arse and huge firm tits..."
scene chantellegym03 with dissolve
$ renpy.pause(2.0, hard=True)
ch "Do you like what you see [name]?"
p "Err, yeah, I was looking for some heavy curls..."
ch "The heaviest curls are over there... I assume these are the ones you plan to use to impress me right?"
p "Of course, I only use the biggest weights around all the time, piece of cake for me!"
ch "Mmh, I want to see that..."        
scene chantellegym04b
stop music
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
ch "Mmmh, this looks a bit too easy for a muscle stud like you... I'll make it a tad harder..."
scene chantellegym05b
$ renpy.pause(1.0, hard=True)
p "AAAH, need to concentrate..."
ch "ooh, I can feel something stirring underneath me, what could it be? I'd better check by rubbing my arse against it..."
scene chantellegym06b
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
ch "Wow, even with my teasing and me distracting you, you still managed to go through your routine with those massive dumbbells..."
ch "I'm really impressed little muscle stud..."
p "You almost got me, and now I've got a massive tent in my strap..."
ch "Well I'm not taking care of it here!... Show me how strong you are some more!"
stop music
scene
play music "Sounds/workoutgroan.mp3"
$ renpy.movie_cutscene("Day2/schoolgymworkout.ogv", delay=-1, loops=-1, stop_music=False)
stop music
scene schoolgymworkout01
play sound "Sounds/panting.mp3"
$ renpy.pause(2, hard=True)
p "That was great, I can feel my muscles getting bigger and stronger already..."
scene schoolgymworkout02 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Sorry, I couldn't help but watch... Damn, you're so strong [name]!"
p "Yeah? You like my huge muscles?"
ch "Yes, I do, this made me...horny... I need to kiss you!"
scene schoolgymworkout03 with dissolve
$ renpy.pause(1.0, hard=True)
p "What next?"
ch "This..is going too fast...maybe...I don't want to lose your sister's friendship...sorry...I shouldn't have..."
p "But...What did I do wrong? It's not fair!"
ch "Another time maybe [name]... Let's leave it at that for now...I...should go now..."
return

label Sex07:
stop music
scene maddygym01
play music "Sounds/gymmusic02.mp3"
$ renpy.pause(1.0, hard=True)
p "Maddy is doing some gymnastics with a big ball..."
scene maddygym02 with dissolve
$ renpy.pause(2.0, hard=True)
p "I can see her cleavage when she bends over...nice..."
p "Hi Maddy, what are you doing exactly? I've never seen this before."
md "It's called a yoga ball. It helps improve strength and balance and it's great fun too!..."
p "Oh... Can I try?"
md "OK, I'll show you if you want, it's nice to see a boy who takes interest in this..."
scene maddygym03 with dissolve
$ renpy.pause(1.0, hard=True)
md "Here's a good exercise to stretch as many muscles as possible..."
md "Your turn..."
p "Okay, I'll try..."
scene maddygym04 with dissolve
$ renpy.pause(1.0, hard=True)
md "You're too stiff, you have to relax a bit..."
p "Easier said than done..."
scene maddygym05 with dissolve
$ renpy.pause(1.0, hard=True)
md "How about this one then?"
p "I'll give it a try but don't make fun of me..."
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
scene maddygym07 with dissolve
$ renpy.pause(1.0, hard=True)
md "I didn't realize you were so... manly..."        
md "I shouldn't have watched... It's not like me... I should leave now."        
p "But... I didn't mind!..."
return

label Sex09:
stop music
scene lesbians01
show randybeachparasol03
$ renpy.pause(1.0, hard=True)
p "What depravity will I find behind this parasol?..."
hide randybeachparasol03 with moveoutright
$ renpy.pause(1.0, hard=True)
play sound "Sounds/lesbians.mp3"
p "Nice, two hot chicks going at it..."
show lesbians01b
l01 "Hey, who do you think you are?"
p "God's gift to women."
l01 "Well, we're strictly lesbians. And you're not invited to the club."
p "What if I show you my own club? He's called \"Billy\"..."
l02 "You're kind of funny. We could let him watch..."
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
        jump LesbiansNoCumx
    "Cum anyway, you've got your male urges to satisfy":
        jump LesbiansCumx

label LesbiansCumx:
stop sound
scene lesbianscum with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "Oh boy, I'm spewing my load, RHHHAAA..."
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
scene randybeach01 with dissolve
show ryanrandybeach with dissolve
$ renpy.pause(1.0, hard=True)
return

label LesbiansNoCumx:
stop sound
$ renpy.pause(1.0, hard=True)
p "Need...to...hold back... Pfeew, that was sssoo close."
show lesbian02happy
l02 "I'm impressed, usually our show makes every cock spew its filthy load in no time..."
show lesbian01happy
l01 l"A man with self-control? That'll be a first. Now get the fuck out of here boy."
p "Sure... Such a pleasure meeting you lovely ladies..."
return

label Sex10:
stop music
scene randyanna01
show randybeachparasol03
$ renpy.pause(1.0, hard=True)
p "I hope it won't be another major disappointment..."
hide randybeachparasol03 with moveoutright
$ renpy.pause(1.0, hard=True)
p "Shit, that's Anna, José's mum!"
scene randyanna02
an "[name]! I didn't expect you to come to this beach, this is so embarrassing!"
p "And I didn't expect you to be here either, sorry to have exposed myself by mistake to you Ms Longrod..."
an "Well... It's not your fault... I didn't see a thing... Even though it was hard not to notice your... huge thingy..."
p "It was hard not to notice your gorgeous breasts too Ms Longrod."
an "Please don't talk like that... Anyway, I didn't see any stirring down there when you saw them..."
p "Ah, so you DID see a thing. A HUGE thingy as you rightfully call it."
an "I meant... Damn, who am I kidding. Yes, I saw your massive pecker. You must be very proud of it I imagine..."
p playersrite "Yes, it's the biggest dong on this island I'm sure of it."
an "Well that's a rather bold statement for such a young boy..."
an "Let me...see it a bit more... and a bit longer..."
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
p "Maybe it's time for you to show me yours..."
an "Yeah, I guess you deserve it..."
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
return

label Sex11:
stop music
$ sisallx = 0
$ sisanalx = False
$ sisblowjobx = False
$ sispussyx = False
stop music
scene nikkibedroomhelp
$ renpy.pause(1.0, hard=True)
p "I came to help you find your earrings sis."
s "Oh goody! Are you going to lift that dresser then so we can have a look if they fell behind it?"
p "Sure, I'll try anyway. Be ready to sneak underneath and look for your earrings!"
p "Here we go..."
scene nikkibedroomhelpdresser with dissolve
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
scene nikkibedroomhelpdresserwin with dissolve
$ renpy.pause(1.0, hard=True)
p "Yes, I did it! Quick, look for your earrings Nikki, I don't know how long I can keep the dresser up in the air like that!"
scene nikkibedroomearring with dissolve
$ renpy.pause(1.0, hard=True)
s "Oh, here they are! I found them, yippee!!!"
p "Great, I can put the dresser back down again!"
scene nikkibedroomhappy with dissolve
$ renpy.pause(1.0, hard=True)
s "Thank you, I found my earrings, I found my earrings!"
scene nikkibedroomkiss with dissolve
play sound "Sounds/kissing.mp3"
$ renpy.pause(1.0, hard=True)
p "(Wow, she kissed me on the mouth... Time to make a move?)"
scene nikkibedroomsultry with dissolve
$ renpy.pause(1.0, hard=True)
s "Well, that was your reward... I think you liked it..."
s "Maybe you deserve a bigger reward little brother... I've noticed how you... seem to lust after me..."  
scene nikkiundress01 with dissolve
$ renpy.pause(1.0, hard=True)
s "That's what you've been dying to see, my huge tits, haven't you? They've grown ssoo much in the last couple of years!"
p "Oh, sis, they are simply sumptuous, so large and round and firm..."
scene nikkiundress02 with dissolve
$ renpy.pause(1.0, hard=True)
s "Now it's your turn to show me that great big monster cock I know you're hiding down there..."
p "Sure, my hardon is about to tear a hole through my shorts! Let me carry you over to the bed Nikki..."
scene nikkiundress03 with dissolve
play sound "Sounds/sisomg.mp3"
$ renpy.pause(1.0, hard=True)
s "Mmmh, you're so strong... and hung... What are you going to do to poor little me?"
label SisFuckChoicesx:
menu:
    "Maybe we should start off with a gentle blowjob." if (sisblowjobx == False):
        jump SisBlowjobx
    "How about I lick your pussy to get it nice and wet?" if (sispussyx == False):
        jump SisPussyx
    "I'm gonna pound that arse of yours to oblivion!" if (sisanalx == False):
        jump SisAnalx
    "Let's fuck, like, for real!" if (sisallx == 3):
        jump SisRealFuckx

label SisPussyx:
scene nikkilick01 with dissolve
$ sisallx += 1
play music "Sounds/lick.mp3"
$ renpy.pause(1.0, hard=True)
$ sispussyx = True
s "Oh, God, you're so good at this, I'm cumming!, AAAHH!"
s "Thanks little bro, I really needed that... Now it's my turn to pleasure that rock-hard donkey-sized cock of yours!"
stop music
jump SisFuckChoicesx

label SisBlowjobx:
scene nikkiblowjob01 with dissolve
$ sisallx += 1
$ renpy.pause(1.0, hard=True)
$ sisblowjobx = True
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
scene nikkiblowjobcum01 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "Fuck, it's streaming out like a faucet!"
s "Mmmh, yes, cover my body in your hot sticky load [name]!"
scene nikkiblowjobcum02 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
s "Wow, I've never seen that much cum in my life, I'm totally drenched in it! Will you be able to go again after such a massive load little brother???"
p "Sure, I'm still hard as rock, let's move on to the main course!"
jump SisFuckChoicesx

label SisAnalx:
scene nikkianal01 with dissolve
$ sisallx += 1
play sound "Sounds/threesomefuck.mp3"
$ renpy.pause(1.0, hard=True)
$ sisanalx = True
s "Be gentle little brother, you're too rough!"
p "Sorry, I got carried away, your arse is so warm and tight... Let's switch position."
stop sound
jump SisFuckChoicesx

label SisRealFuckx:
stop music
play music "Sounds/sisfuck.mp3"
show movienikkifuck
show cum
call screen sisfuckcumx
screen sisfuckcumx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("SisFuckCum01x")

label SisFuckCum01x:
stop music
hide movienikkifuck
scene nikkifuckcum01
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
s "OMG, you're filling my pussy to overcapacity! Pull it out and cover my body with your giant load!"
scene nikkifuckcum02 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "SSooo good... I really busted a nut there sis, you were great..."
s "I'm gonna need to take a shower and clean my sheets without mom noticing all your sticky mess... Mmmh, it's so delicious..."
s "You'd better leave [name], we don't want to get caught by mom..."
return

label Sex12:
stop music
scene nancybedroomclosed
$ renpy.pause(1.0, hard=True)
p "The door is locked but I can see some light poking through the keyhole."
scene nancyundressing01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Mom is sitting on her bed. She looks like she's thinking about doing something..."
p "More mother blueballing on the way for you guys it seems..."
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
scene nancyundressing07 with dissolve
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
p "I think I heard her say my name while she was creaming all over her huge dildo... Wish it was my cock instead."
p "Probably best to leave now, I don't want to be seen peeping through mom's keyhole like that."    
stop music
return  

label Sex13:
stop music
scene classroom01day03
$ renpy.pause(1.0, hard=True)
p "Why don't I spend my time more efficiently by daydreaming about hot chicks?"
menu:
    "Daydream about the teacher":
        jump DayDreamTeaganDay03x
    "Daydream about Kate":
        jump DayDreamKateDay03x
    "Daydream about Laura":
        jump DayDreamLauraDay03x
    "Daydream about Frieda and Maddy":
        jump DayDreamFriedaMaddyDay03x
        
label DayDreamTeaganDay03x:
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
return

label DayDreamLauraDay03x:
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
return

label DayDreamKateDay03x:
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
return

label DayDreamFriedaMaddyDay03x:
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
fr "Ooh, JA! Das is so gut! Komm fick mich mit deinem reisen Schwanz [name]!"
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
return
        
label Sex15:
stop music
scene guidance01
$ renpy.pause(1.0, hard=True)
so "Do you know why I called you in [name]?"
p "Err, no..."
so "Because despite my strict orders, you FUCKED ONE OF OUR GIRLS YESTERDAY!"
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
stop music
play music "Sounds/principalslow02.mp3"
show guidanceslow
show faster
call screen principalfootjob02x
screen principalfootjob02x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("FootJobFast02Day03x")

label FootJobFast02Day03x:
stop movie
hide faster
play music "Sounds/principalfast02.mp3"
show guidancefast
show cum
call screen footjobfaster02x
screen footjobfaster02x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PrincipalCum02Day03x")

label PrincipalCum02Day03x:
hide guidancefast
hide guidanceslow
stop music
play sound "Sounds/ryancumming.mp3"
scene guidancecum01 with dissolve
$ renpy.pause(1.0, hard=True)
so "Yes, that's a good boy, empty those massive balls of all their filthy cum..."
play sound "Sounds/principalcum02.mp3"
scene guidancecum02 with dissolve
$ renpy.pause(8.0, hard=True)
so "Every time you fuck one of our girls, you will get some guidance from me until you LEARN to control your fuckstick, understood?"
p "Yes Principal Titsworthy... I get it now."
return

label Sex17:
stop music
scene rooftop02
$ renpy.pause(1.0, hard=True)
p "Let's see what the neighbors are up to..."
$ renpy.pause(1.0, hard=True)
p "Mr Anderson is doing some gardening... BORING!"
p "Hang on a minute, his wife and daughter are on the upper deck jacuzzi..."
scene voyeur01 with dissolve
$ renpy.pause(1.0, hard=True)
p "And there's some muscular redhead boy proudly displaying his massive dong to them. That could become interesting..."
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
return

label Sex14:
stop music
$ friedaarsex = False
$ friedaridex = False
scene friedalibrary01day03
p "Well, guess what? I switched your grades! You now have an A!"
scene friedalibrary03day03 with dissolve
fr "Mein Gott, you did it! Sank you sssooo much..."
fr "ESS MEINE SCHEISSE DU SCHWEIN!"
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
label FriedaCockRubDay03x:
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
        jump FriedaCockRubDay03x
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
label FriedaFuckChoiceDay03x:
menu:
    "Let her ride you" if (friedaridex == False):
        jump FriedaFuckRideDay03x
    "Take her up the arse" if (friedaarsex == False):
        jump FriedaFuckArseDay03x
    "Tell her to finish you off with a blowjob" if (friedaarsex == True) and (friedaridex == True):
        jump FriedaFuckBlowjobDay03x


label FriedaFuckRideDay03x:
scene friedaup with dissolve
$ renpy.pause(1.0, hard=True)
fr "Let me insert that cum-missile myself..."
p "Sure, do as you please Frieda, it's all yours!"
fr "OOOOh, it's zzooo big... (puff)... Ein bißchen mehr...."
scene friedafuck09 with dissolve
$ friedaridex = True
$ renpy.pause(1.0, hard=True)
fr "Mein Gott! I can feel your huge cock so deep inside of me... I can touch it with my hands from outside!"
p "Well, it does have a certain volume..."
fr "It is ENORMOUS! (puff) I don't think I can take much more of it zat way..."
p "Let's switch position then..."
menu:
    "Take her up the arse" if (friedaarsex == False):
        jump FriedaFuckArseDay03x
    "Tell her to finish you off with a blowjob" if (friedaarsex == True) and (friedaridex == True):
        jump FriedaFuckBlowjobDay03x

label FriedaFuckArseDay03x:
scene friedafuck10 with dissolve
$ friedaarsex = True
$ renpy.pause(1.0, hard=True)
fr "You are stretching my poor little anus zo much! AAAAH!"
p "That's nothing, I'm not even halfway in. Let me stretch it a bit more..."
scene friedafuck10b with dissolve
$ renpy.pause(1.0, hard=True)
p "There. That's better. A solid ten inches of my ramrod up your arse!"
fr "Be caref.."
label FriedaFuckArseDay03bx:
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
        jump FriedaFuckArseDay03bx        
    "Let her ride you" if (friedaridex == False):
        jump FriedaFuckRideDay03x
    "Tell her to finish you off with a blowjob" if (friedaarsex == True)and (friedaridex == True):
        jump FriedaFuckBlowjobDay03x

label FriedaFuckBlowjobDay03x:
stop music
play music "Sounds/friedaslow.mp3"
show friedafuckslow
show faster
call screen friedafuckslowday03x
screen friedafuckslowday03x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("FriedaFuckFastx")

label FriedaFuckFastx:
hide faster
play music "Sounds/friedafast.mp3"
show friedafuckfast
show cum
call screen friedafuckfastday03x
screen friedafuckfastday03x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FriedaFuckCumx")

label FriedaFuckCumx:
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
fr "But we need to get dressed. And cleaned up..."
p "Yes, that is probably a good idea. I mean, some people DO use the library sometimes."
return

label Sex16:
stop music
scene gloryhole01
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
label GloryHoleSuckDay03x:
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
        jump GloryHoleSuckDay03x
    "Cum":
        pass
p "Haa... She's sucking me sssoo good, I'm gonna blow my load!"
play sound "Sounds/ryancumming.mp3"
scene gloryholebrit05 with dissolve
$ renpy.pause(1.0, hard=True)
br "Glurb... (swallow).... mmmpf... (swallow)...."
p "Pfeeeww... She sucked me dry... Whoever she is, she's a pro..."
br "Wow, what a cock... It can't possibly be José's, his bulge is not big enough..."
scene gloryholebrit06 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/footsteps.mp3"
p "Oooh, it was Brittany! What a slut! Then again, I'm a he-slut too..."
scene gloryholebrit07 with dissolve
$ renpy.pause(1.0, hard=True)
p "Hey Brittany, that giant cock you sucked... It was mine! Ta-daa!"
br "Eek, you broke the unwritten rule that you should never reveal yourself to your gloryhole partner you moron!"
p "But, I thought..."
br "Shut up already twerp! Get out of my sight!"
scene gloryholend with dissolve
$ renpy.pause(1.0, hard=True)
p "She's gone. Good thing I didn't mention she had some of my cum dripping out of her mouth..."
return

label Sex21:
stop music
$ katelegsx = False
$ katepussyx = False
$ katetitsx = False
play music "Sounds/gardensound.mp3"
scene katepool01
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
k "And the back. It doesn't cover much, I feek almost naked..."
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
p "How about I pose like He-man and you look at me from below?"
k "Uuh... Ok."
scene katepool09 with dissolve
$ renpy.pause(1.0, hard=True)
k "Can I touch it? I've never seen anything that big before!"
p "Sure, I'll let a pint of blood flow into it so it's even bigger for you..."
play sound "Sounds/katehihi.mp3"
k "Oh fuck [name], it's so big..."
window hide
play sound "Sounds/kate01.mp3"
$ renpy.pause(4.0, hard=True)
p "Of course Kate. It's all for you..."
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
        jump KateBehindDay03x
    "Push her down and place the head near her pussy":
        jump KatePussyDay03x
    "Push her down and stick your rod between her tits":
        jump KateTitsDay03x

label KateBehindDay03x:
stop music
scene katepool13 with dissolve
$ katelegsx = True
$ renpy.pause(1.0, hard=True)
k "Oooh... It's sticking straight out way past my tummy. It's like I have a huge cock of my own, hee hee!"
p "And what would you do if it was yours?..."
k "Uuuh... I'd probably...."
scene katepool18 with dissolve
$ renpy.pause(1.0, hard=True)
k "Hold it like that and tug hard on it like I was wanking my big hard shaft..."
scene katepoolwank01 with dissolve
$ renpy.pause(1.0, hard=True)
label KateBehindDay03bx:
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
        jump KateBehindDay03bx
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
    "Push her down and place the head near her pussy" if (katepussyx == False):
        jump KatePussyDay03x
    "Push her down and stick your rod between her tits" if (katetitsx == False):
        jump KateTitsDay03x
    "Lift her up and fuck her sweet hole" if (katelegsx == True) and (katepussyx == True) and (katetitsx == True):
        jump KateLiftDay03x

label KatePussyDay03x:
scene katepool14 with dissolve
$ katepussyx = True
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
label KatePussyDay03bx:
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
        jump KatePussyDay03bx
    "Stick your pud between her legs from behind" if (katelegsx == False):
        jump KateBehindDay03x
    "Push her down and stick your rod between her tits" if (katetitsx == False):
        jump KateTitsDay03x
    "Lift her up and fuck her sweet hole" if (katelegsx == True) and (katepussyx == True) and (katetitsx == True):
        jump KateLiftDay03x

label KateTitsDay03x:
scene katepool20 with dissolve
$ katetitsx = True
$ renpy.pause(1.0, hard=True)
p "I think those big jugs of yours are a perfect match for my massive erection!"
k "Uuhh, oooh, you think so?"
p "For sure, I'm dripping precum all over the place cos they make me so horny!"
k "Oooh, I'm so glad you like them..."
menu:
    "Stick your pud between her legs from behind" if (katelegsx == False):
        jump KateBehindDay03x
    "Push her down and place the head near her pussy" if (katepussyx == False):
        jump KatePussyDay03x
    "Lift her up and fuck her sweet hole" if (katelegsx == True) and (katepussyx == True) and (katetitsx == True):
        jump KateLiftDay03x

label KateLiftDay03x:
scene katepool17 with dissolve
$ renpy.pause(1.0, hard=True)
k "Uuhh, what? You're lifting me up on your COCK? God, it's ssooo powerful!"
p "Ready for a wild ride Kate?"

stop music
play music "Sounds/kateslow.mp3"
show katefuckslow
show faster
call screen katefuckscreenx
screen katefuckscreenx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("KateFuckFastDay03x")

label KateFuckFastDay03x:
stop movie
hide faster
play music "Sounds/kate04.mp3"
show katefuckfast
show cum
call screen katefuckscreen02x
screen katefuckscreen02x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("KateFuckCumDay03x")

label KateFuckCumDay03x:
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
k "We should take a dip in the pool to clean ourselves of all this cum you've unloaded everywhere! Hee hee!"
p "I'd better clean the deck, you go in the pool."
k "Oooh, OK."
scene katepoolend with dissolve
$ renpy.pause(1.0, hard=True)
k "The pool water is so great..."
p "(It's so nice to see poor Kate so happy. Especially after she got detention again today.)"
k "I'm clean now, I'd better get going. See you tomorrow [name]!"
p "Yep, see you at school for our trip to Bigdong Falls Kate!"
return

label Sex20:
stop music
scene beachempty
$ renpy.pause(1.0, hard=True)  
p "This secluded part of the beach is empty... I could always go for a swim I guess."
play music "Sounds/randybeachsound.mp3"
scene beachswim01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I can see some coral reefs below. Let's dive and have a look!"        
scene beachswim02 with dissolve
play music "Sounds/underwater.mp3"
$ renpy.pause(1.0, hard=True)
p "What the hell is that thing swimming towards me?"
scene mermaid01 with dissolve
$ renpy.pause(1.0, hard=True)
p "This mermaid is captivating... OK, she has a fish tail and all that but... Mmmh, those tits..."
scene mermaid02 with dissolve
$ renpy.pause(1.0, hard=True)
p "She seems to be signalling me to follow her..."
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
p "Well, a hole is a hole, let's fuck!"
scene mermaid08 with dissolve
$ renpy.pause(1.0, hard=True)
p "Here we go, it's tough to aim underwater but once I'm in, it shouldn't move too much..."
show mermaidfuckslow
show faster
call screen mermaidfuckslowx
screen mermaidfuckslowx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MermaidFuckFastx")
label MermaidFuckFastx:
hide faster
show mermaidfuckfast
show cum
call screen mermaidfuckfastx
screen mermaidfuckfastx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MermaidFuckCumx")
label MermaidFuckCumx:
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
p "I'd better get back to the surface before I run out of air again..."
scene mermaid12 with dissolve
$ renpy.pause(1.0, hard=True)
p "Shame I couldn't take a picture with my phone and send it to José... Then again, it might be best that way since this was bordering on bestiality..."
return

label Sex19:
stop music
play music "Sounds/oceanwaves.mp3"
scene hallebeach04
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
window hide
play sound "Sounds/hallesuck01.mp3"
ha "Gllur---mmmm!"
p "And then..."
scene hallesuck03 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/hallesuck02.mp3"
p "The main course! RHHAAA, Open that throat if you want to take it!"
window hide
play sound "Sounds/hallesuck02.mp3"
$ renpy.pause(3.0, hard=True)
p "Yeah... That's a good girl... You said you could hold your breath for a very long time, now prove it, AAHHH!"
window hide
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
label HallePrefuckDay03x:
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
        jump HallePrefuckDay03x
    "Spread her legs and fuck her pussy slowly":
        ha "You want to fuck me some more stud? Yeah, I 'm ready for your great big horsecock, come and ram that monstercock home!"
        jump HalleFuckMoviex

label HalleFuckMoviex:
stop music
play music "Sounds/hallefuckfast.mp3"
play sound "Sounds/oceanwaves.mp3"
show hallefuckslow
show faster
call screen hallefuckslowx
screen hallefuckslowx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("HalleFuckFastx")
label HalleFuckFastx:
hide faster
show hallefuckfast
show cum
call screen hallefuckfastx
screen hallefuckfastx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("HalleFuckCumx")

label HalleFuckCumx:
hide hallefuckfast
hide hallefuckfast
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
ha "Well you did REAL good [name]... Now I have to go back into the ocean to clean myself of the tons of cum you've covered me with!"
ha "Don't wait for me, I'll be a WHILE cos you came SSSOOO MUCH!"
p "See you Halle, thanks for that hot steamy sex!"
return

label Sex18:
stop music
scene chiyorandy01
show randybeachparasol03
$ renpy.pause(1.0, hard=True)
p "Ah, something nice it seems..."
hide randybeachparasol03 with moveoutright
$ renpy.pause(1.0, hard=True)
cy "Oh, hello there boy. Don't you know it's rude to sneak on naked ladies like that?"
p "Come on, you were asking for it, you were barely hiding behind that parasol..."
cy "What if I were? I can tease all I want... It's the boys that get teased that have themselves to blame.... hee hee..."
scene chiyorandy03 with dissolve
$ renpy.pause(1.0, hard=True)
cy "See how this cream glistens on my skin? Do you think I put enough on or not?"
p "Yeah, but not on your back. You might catch a sunstroke."
cy "But I can't reach my back... Maybe you get to be useful after all... (wink)"
scene chiyorandy04 with dissolve
$ renpy.pause(1.0, hard=True)
cy "Yes, that's nice, rub it in all over my back you naughty boy... And now move to my arse..."
scene chiyorandy05 with dissolve
$ renpy.pause(1.0, hard=True)
cy "Mmh, I like your strong hands..."
scene chiyorandy06 with dissolve
$ renpy.pause(1.0, hard=True)
cy "What?... No, naughty boy!"
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
cy "I'll finish putting more cream on my huge titties now..."
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
cy "Mmh, that was good. Oh well, I got off, so now you can go, you're useless to me. Hee hee..."
p "What? You can't leave me like that!"
cy "Of course I can. You'll just have to jerk off somewhere else naughty boy..."
p "AAARGGH! Such a tease!"
return

label Sex23:
stop music
scene dorissauna01
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
do "Well, that was pretty amazing kid... But you still have some more training to do if you want to win. I'll be happy to help... Right now, I need a hot shower."
p "(pant)... Thanks for that, your hands were amazing.... I'm pretty sure I'll be coming back for MORE!"
return

label Sex22:
stop music
scene preshoot01
$ renpy.pause(1.0, hard=True)
aj "Ah, there you are, you're late! I HATE waiting!"
p "Sorry Ms Jolly. Traffic..."
scene preshoot03 with dissolve
$ renpy.pause(1.0, hard=True)
aj "That's a lousy excuse! Don't you have a chauffeur to drive you around?"
p "Of course, but he called in sick this morning. Now let's get the show rolling shall we?"
aj "Well since you were late, I already put on the swimwear I'm supposed to use for the shoot."
p "Perfect, now let's move to the studio area, the lights are all set and my camera is ready!"
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
p "Hold that big banana."
aj "Oh, I see, that's the plan then hey?..."
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
p "The scene with the amateur fan."
aj "Yes, that was tons of fun. The poor sod was so worried at first, but he gained confidence and then pounded me just as hard as a veteran pornstar."
scene shoot08 with dissolve
$ renpy.pause(1.0, hard=True)
aj "Too bad there isn't someone like him right here... I'm so horny..."
p "I can volunteer... I'm a major fan myself..."
aj "Mmh, such devotion to your job mr photographer... Bring that crank over here then..."
stop music
scene shoot09 with dissolve
$ renpy.pause(1.0, hard=True)
aj "Damn kid, that's the biggest \"crank\" I've ever seen and I've seen hundreds of pornstar dongs!"
p "Enough talking, put that mouth to good use and gobble my shaft as deep as you can!"
aj "I'll try..."
label ShootFuckMouthDay03x:
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
        jump ShootFuckMouthDay03x
    "Move on":
        pass

label ShootFuckPussyDay03x:
p "You're doing good. Not many girls can gobble up my monster dong like that!"
aj "I'm not the winner of \"Pornstar Mouth of the Year\" five years in a row for nothing Mr Hank!"
p "Let's test your \"Pornstar Pussy of the Year\" then..."
aj "Ok, but be caref....."
label ShootFuckPussyDay03bx:
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
        jump ShootFuckPussyDay03bx
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
aj "Damn boy, you truly are a bukkake machine! Now I have to get cleaned up, I'm caked in semen..."
scene shootend with dissolve
$ renpy.pause(1.0, hard=True)
aj "I have a porn shoot this afternoon and I'm not sure I'll be able to feel my partner's rod this time... You've stretched me so much...."
p "Hank the Crank at your service ma'am!"
p "SHHHIIIT, I forgot to put the timer on! I can't send José any pic of the deed... What a missed oportunity..."
return

label Sex24:
stop music
$ momblowjobx = False
$ momtitfuckx = False
scene eveningtvmom01
$ renpy.pause(1.0, hard=True)
m "I'm ready! So, what movie did you end up choosing to entertain us tonight?"
p "Conan the Barbarian"
m "Alright, I've never seen it before."
scene eveningconan with dissolve
play music "Sounds/conan.mp3"
$ renpy.pause(2.0, hard=True)
m "This movie is terrible, but that foreign actor... Mmmh, he sure has huge muscles...everywhere... Whoever he is."
p "He's got nothing on me, I bet I have bigger muscles than him!"
m "If you want to go around pretending that, you need to walk the walk and not just talk the talk, son..."
p "I could pose in my jockstrap and flex my biceps so you can compare with him on the screen! Then, you'll be convinced!"
m "Alright [name]. Let's see what you've got mister. This is going to be more entertaining than this drivel of a movie!"
scene ryanconanposing01b with dissolve
stop music
play music "Sounds/conan02.wav"
$ renpy.pause(1.0, hard=True)
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(2.0, hard=True)
m "Oh, sweetie, you're right, you really are MUCH BIGGER than this actor! Mommy is so proud of you!"
scene eveningmomconan with dissolve
$ renpy.pause(1.0, hard=True)
m "And it's not just your muscles that are bigger than this actor... Your bulge puts his to shame, and I thought his was really huge!"
stop music
scene ryanconanposing02 with dissolve
$ renpy.pause(1.0, hard=True)
p "That's right mom, you're the one who gave birth to that thing!"
m "It looks so big.... and not even hard. I know it's wrong but mommy NEEDS to feel up that monster!"
scene eveningmomstrap with dissolve
$ renpy.pause(1.0, hard=True)
m "Mmmh, honey, this is the biggest thing I've ever felt in my life... My tiny hands can't even wrap around your giant boycock. Let mommy see it please, I beg you!"
p "I'm getting really hard mom watching you worshipping my bulge like that... FUCK!"
scene eveningmomrip with dissolve
play sound "Sounds/rip.mp3"
$ renpy.pause(1.0, hard=True)
m "Oh my God! Your massive rock-hard cock just ripped right through your jockstrap!"
p "That's cos you're making me so horny mom... Please take off your blouse... I'll turn the lights on..."
m "I don't know... It's just so wrong... Just a peek for my horse-hung muscle stud then!"
scene eveningmomfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
m "You like what you see [name]? What would you like mommy to do next my studly son?"
menu:
    "I need to stick my cock between those big jugs...":
        jump MomTitfuckDay03x
    "I don't know but I'm about to explode!":
        jump MomBlowjobDay03x
        
label MomTitfuckDay03x:
$ momtitfuckx = True
scene momtitfuck01 with dissolve
m "Of course son. Mommy will take care of that monster with her huge jugs, you just relax and let mommy do all the work."
label MomTitfuckDay03bx:
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
        jump MomTitfuckDay03bx
    "Move on":
        pass
m "Oh sweetie, your huge cock looks like it's ready to explode!"
scene momtitfuckcum01 with dissolve
play sound "Sounds/ryancumming.mp3"            
$ renpy.pause(2.0, hard=True)
scene momtitfuckcum02 with dissolve
play sound "Sounds/momtitfuckcum.mp3"            
$ renpy.pause(11.0, hard=True)
m "Damn [name], you really had a lot of pent-up cum stored in those huge balls..."
if (momblowjobx == False):
    m "Bring that massive fuckstick to my mouth son!"
    jump MomBlowjobDay03x
else: 
    m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
    jump MomPussyLickDay03x

label MomBlowjobDay03x:
$ momblowjobx = True
scene momblowjob01 with dissolve
play sound "Sounds/momlick01.mp3"  
$ renpy.pause(5.0, hard=True)
m "My God son, your cock... It's just GIGANTIC! Mommy can't even wrap her fingers around its incredible girth..."
scene momblowjob01b with dissolve
play sound "Sounds/momlick02.mp3"  
$ renpy.pause(19.0, hard=True)         
m "Mmmh... And those balls... So HEAVY, I just have to taste them..."         
label MomBlowjobDay03bx:
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
        jump MomBlowjobDay03bx
    "Move on":
        pass

m "Oh sweetie, your huge cock looks like it's ready to explode!"
if (momtitfuckx == False):
    m "Why don't you stick your pud between mommy's big tits?"
    jump MomTitfuckDay03x
if (momtitfuckx == True):
    m "Lick my pussy to get it ready for a heavy pounding from your gigantic pole!"
    jump MomPussyLickDay03x            
 
label MomPussyLickDay03x:
scene eveningmomclit with dissolve
play sound "Sounds/momclit.mp3"
$ renpy.pause(9.0, hard=True)
m "Mmmh, you do that so well sweetie! You really know what you're doing! AAAH!"
m "Now it's time for mommy to reward you... With her pussy!"
scene eveningmomready with dissolve
play sound "Sounds/momready.mp3"
$ renpy.pause(18.0, hard=True)
m "See my tender pink pussy? It's wet and ready for you my studly son! Come and pound it!"
play music "Sounds/momslowfuck.mp3"
show momfuckslow
show faster
call screen momfuckslowday03x
screen momfuckslowday03x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MomFuckFastDay03x")
label MomFuckFastDay03x:
hide faster
stop music
show momfuckfast
play music "Sounds/momfastfuck.mp3"
show cum
call screen momfuckfastday03x
screen momfuckfastday03x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MomFuckCumx")

label MomFuckCumx:
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
m "Damn [name], you really had a lot of pent-up cum stored in those huge balls..."
m "It's mommy's duty to make sure you empty them regularly so you don't get blue balls and it hurts..."
m "I should go and take a shower, since I'm covered in your red-hot spunk... We'll keep this...incident... between us sweetie."
return

label Sex26:
stop music
play music "Sounds/tanyamusic.mp3"
scene webcam01
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
call screen tanyawankslowx
screen tanyawankslowx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("TanyaWankFastx")
label TanyaWankFastx:
hide faster
show tanyawankfast
show cum
call screen tanyawankfastx
screen tanyawankfastx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TanyaWankCumx")

label TanyaWankCumx:
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
scene webcam14 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Damn, I'm caked in your cream... Well, what do you think guys? Who came the most between hubby and the newbie?"
play sound "Sounds/beep.mp3"
$ renpy.pause(1.0, hard=True)
ta "DanSubmissive79 claims hubby's load wasn't even a tenth of the mega-spunk shower the white boy delivered... I think he might be right."
dl "This is going too far Tanya, I'm being humiliated! I'm gonna beat the crap out of this kid you brought in!"
p "So who's the cuck now? I'm da man, I'm DA MAN!"
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
return

label Sex25:
stop music
scene campfire13
$ renpy.pause(1.0, hard=True)
la "I... have an uncontrollable urge to... get close to you... Don't resist, it's futile..."
p "Oh, I won't resist, don't worry Laura! (Bingo!)"
la "Take those shorts off... I want to see your demonic pillar of lust!"
scene campfire14 with dissolve
$ renpy.pause(1.0, hard=True)
la "Sweet Belzebuth! This thing is HUGE, like... out of this world!"
p "Yes, do something about it Laura, I am possessed by a satanic desire to fuck you so hard!"
la "Alright [name], let me take care of that bad boy..."
label LauraFuck01Day03bx:
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
        jump LauraFuck01Day03bx
    "Move on":
        pass

scene campfire15 with dissolve
play sound "Sounds/laura01.mp3"    
$ renpy.pause(8.0, hard=True)
la "You seem to have liked that... Your cock has turned into a steel-hard pole!"
p "Make it spew its evil load with your hands!"
scene campfiretease01 with dissolve
$ renpy.pause(1.0, hard=True)
la "How about I scratch it like that.... all the way up..."
play sound "Sounds/lauratease01.mp3"
scene campfiretease02 with dissolve
$ renpy.pause(2.0, hard=True)
scene campfiretease01 with dissolve
$ renpy.pause(2.0, hard=True)
la "And down again... Yes, you like that, your cock is trembling..."
label LauraFuck03Day03bx:
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
        jump LauraFuck03Day03bx
    "Cum":
        pass
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
p "I hope you are too, because I'm still rock-hard and needing a soft and warm pussy!"
la "My pussy is ready for that demonic pole of yours... Let me ride it!"

stop music
play sound "Sounds/campfire.mp3"
play music "Sounds/laurafuckslow.mp3"
show laurafuckslow
show faster
call screen laurafuckslowday03x
screen laurafuckslowday03x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)  
        action Jump ("LauraFuckFastDay03x")

label LauraFuckFastDay03x:
stop movie
hide faster
play music "Sounds/laurafuckfast.mp3"
show laurafuckfast
show cum
call screen laurafuckfastday03x
screen laurafuckfastday03x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("LauraFuckCumDay03x")
    
label LauraFuckCumDay03x:
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
la "Kiss me while I'm covered in your sticky spunk... This was so amazing [name]!"
return

label Sex30:
$ principaltitsx = False
$ principalbackx = False
stop music
scene principalfuck01
$ renpy.pause(1.0, hard=True)
so "That's it young man, get undressed, I NEED to see that monster hard and ready on the spot!"
scene principalfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
so "And as a treat, I'll show you my breasts. Aren't they just spectacular?"
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
label PrincipalStartFuckDay04x:
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
        jump PrincipalStartFuckDay04x
    "Move on":
        pass
so "NNOO! too... too much.... I can't take it anymore, AAAAHH!"
p "Giving up already principal? You're gonna screw the people as a senator, now it's time for the people to screw YOU!"
label PrincipalFuckChoiceDay04x:
menu:
    "I want to stick my cock between your huge jugs..." if (principaltitsx == False):
        jump PrincipalTitfuckDay04x
    "Let's switch position, get on your back!" if (principalbackx == False):
        jump PrincipalBackFuckDay04x
    "Time to finish me off with your arse muscles!" if ((principaltitsx == True) and (principalbackx == True)):
        jump PrincipalArseFuckDay04x
    
label PrincipalTitfuckDay04x:
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
label PrincipalTitFuckDay04bx:
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
$ principaltitsx = True
menu:
    "Repeat":
        jump PrincipalTitFuckDay04bx
    "Move on":
        pass
jump PrincipalFuckChoiceDay04x

label PrincipalBackFuckDay04x:
scene principalback02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready for a good pussy pounding principal?..."
so "Oh yeah, you've made me addicted to that monster cock of yours [name], fuck me hard, as hard as you want!"
label PrincipalBackFuckDay04bx:
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
$ principalbackx = True
menu:
    "Repeat":
        jump PrincipalBackFuckDay04bx
    "Move on":
        pass
so "Oooh, my poor pussy! I'll never recover from such a pounding.... (puff)"
p "Then it's time to try something else..."
jump PrincipalFuckChoiceDay04x

label PrincipalArseFuckDay04x:
scene principalarse01 with dissolve
$ renpy.pause(1.0, hard=True)
so "You can't be serious! My arse is too tiny for your massive piece of teenage meat!"
p "We're about to find out..."
scene principalarse02 with dissolve
$ renpy.pause(1.0, hard=True)
so "Oh my God, you're stretching me ssooo much!"
p "Just hang in there, there's quite a few more inches to go..."
so "What? Wait...AAAH!"

label PrincipalMainFuckDay04x:
play music "Sounds/sophiaslowfuck.mp3"
show sophiafuckslow
show faster
call screen sophiafuckslowday04x
screen sophiafuckslowday04x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("SophiaFuckFastDay04x")
label SophiaFuckFastDay04x:
hide faster
stop music
play music "Sounds/sophiafastfuck.mp3"
show sophiafuckfast
show cum
call screen sophiafuckfastday04x
screen sophiafuckfastday04x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("SophiaFuckCumDay04x")

label SophiaFuckCumDay04x:
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
so "I don't think I'll call Willie this time, I prefer to clean up your mess myself... with my MOUTH!"
so "Hopefully, you have emptied your giant balls and our girls are safe for the day..."
so "It will take me a while so get dressed and get back to your studies! Not a word to anyone about this..."
p "Of course Principal Titsworthy, my lips are sealed! And my balls are drained..."
return

label Sex27:
$ teagantitsx = False
$ mariamilkx = False
$ mariapussyx = False
$ teaganpussyx = False
scene bigdongteagan02
stop music
$ renpy.pause(1.0, hard=True)
t "There we are, look at the endownments on this statue, one of many in this gorge. Now you get why it's called \"Bigdong Falls\" [name]?"
scene bigdongteagan03 with dissolve
$ renpy.pause(1.0, hard=True)
ma "The natives lived in matriarchal tribes where boys were selected at a young age for breeding based on their physical attributes..."
ma "It is believed that this system led to extraordinarily well-endowed muscle boys to be born and worshipped by the tribe women..."
t "It's such a shame that the French ended up killing all those natives... (sigh)."
p "Well, they would have worshipped me for sure... What about the female statue? She has huge knockers..."
ma "Ah, yes... They were also \"breeders\" and selected for their physical attributes... And then mated with the horse-hung boys."
t "The ones who truly were equipped with a massive penis, not the ones who just bragged about it..."
scene bigdongteagan05 with dissolve
$ renpy.pause(1.0, hard=True)
p "Look at me, I'm posing just like that statue!"
t "What the hell are you doing [name]?"
p "Proving to you that I would have fitted right into that tribe!"
ma "Wow, what a HUGE cock! My ex-husband was so tiny compared to that monster..."
t "Yeah, OK, you have a huge cock, I said it, are you happy now?"
p "You can do better than that teach..."
t "And what do you expect me to say about your...thing?"
p "Pretend you're a tribeswoman and worship it."
t "Why would I want to do such a thing?"
p "Cos your knockers are really awesome, so you could definitely have been in their breeding program..."
t "Awesome? That's the word you use to describe them? That's pretty lame worshipping boy... I'll show you what proper worshipping sounds like..."
ma "Oh, I'm in too!"
scene bigdongdouble01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Now, with my sumptuous, heavy breasts right in your face, do you have any better words that come to mind [name]?"
p "mm..hummmuuummmm..."
t "Say again?"
ma "What about if I worship your giant, thick, veiny, beautiful, godlike cock, stud?"
window hide
show doubledelight:
    xalign 0.4 yalign 0.2
    zoom 0.5
    linear 2.0 zoom 1.0
play sound "Sounds/delight.mp3"
$ renpy.pause(4.0, hard=True)
ma "Let's move to a shallower part of the gorge, I want to be able to admire your pole AND your nuts!"
t "Good idea... I want to see everything too..."
p "(Jackpot! I'm gonna get me some double-poontang!)"
scene bothprefuck with dissolve
$ renpy.pause(1.0, hard=True)
t "I can tell my huge tits are really getting your huge cock hard [name]..."
ma "So, what would you like us to do to get that massive love pole down before anyone sees us?"
label BothFuckChoiceDay04x:
menu:
    "Come and worship my muscles ladies!":
        jump BothMuscles01x
    "Why don't you play with each other for a while...":
        jump BothPlay01x
    "I'd like to titfuck your giant tits as a good sloppy workout teach!" if (teagantitsx == False):
        jump BothTeaganTitFuck01x
    "I'm thirsty... for some milk! Let me suck on your huge nipples Maria!" if (mariamilkx == False):
        jump BothMariaMilk01x
    "Let me fuck your tender pussy Maria while teach sucks on my heavy nuts!" if (mariapussyx == False):
        jump BothMariaFuck01x
    "Get ready for a heavy pounding Teagan while Maria jacks my crank!" if (teaganpussyx == False):
        jump BothTeaganFuck01x
    "Open your mouth and get ready to receive my load both of you!" if (teaganpussyx == True) and (mariapussyx == True) and (mariamilkx == True) and (teagantitsx == True):
        jump BothTeaganBlowx

label BothMuscles01x:
scene bothworship01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Mmh, your biceps are so big [name]... They must be at least 20 inches around fully flexed..."
scene bothworship02 with dissolve
$ renpy.pause(1.0, hard=True)
t "Which is about the size of that monstrous rod... I'm sorry I didn't believe a boy your age could be such a super-stud..."
jump BothFuckChoiceDay04x

label BothMariaFuck01x:
$ mariapussyx = True
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
label BothMariaFuck01bx:
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
            jump BothMariaFuck01bx
        "Move on":
            ma "You made me cum ssooo much..."
            p "Let's switch position and I'll make you cum even more..."
            jump BothMariaFuck02x

label BothMariaFuck02x:
scene mariafuck03 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Please be gentle with that monstrous thing, you're at least five times longer and thicker than my ex-husband..."
p "What a pindick, time for you to feel a REAL man. Me, DA MAN!"
scene mariafuck04 with dissolve
$ renpy.pause(1.0, hard=True)
ma "You're stabbing me in the womb with your giant love muscle!"
t "Fuck her harder! I want to see her pussy creaming over that fat shaft!"
label BothMariaFuck02bx:
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
        jump BothMariaFuck02bx
    "Move on":
        ma "Too... Too much..."
        jump BothFuckChoiceDay04x

label BothTeaganTitFuck01x:
$ teagantitsx = True
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
label BothTeaganTitFuck01bx:
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
        jump BothTeaganTitFuck01bx
    "Move on":
        scene teagantitfuck03 with dissolve
        play sound "Sounds/teagantitfuck03.mp3"
        $ renpy.pause(4.0, hard=True)
        t "Damn, I'm all sticky with your abundant precum [name]!"
        jump BothFuckChoiceDay04x

label BothMariaMilk01x:
$ mariamilkx = True
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
label BothMariaMilk01bx:
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
        jump BothMariaMilk01bx
    "Move on":
        ma "I don't think I have any milk left... You sucked me dry, you were more hungry than my daughter Lolly ever was!"
        jump BothFuckChoiceDay04x

label BothTeaganFuck01x:
$ teaganpussyx = True
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
label BothTeaganFuck01bx:
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
        jump BothTeaganFuck01bx
    "Move on":
        t "I am ready to receive that great big monster cock [name]!"
        jump BothTeaganFuck02x
        
label BothTeaganFuck02x:
p "Maria, get a hold of my shaft while I ram it inside Teagan and claim her pussy as mine!"
scene teaganfuck01b with dissolve
$ renpy.pause(1.0, hard=True)
t "What? No, my pussy is my property!"
p "You sure about that?"
scene teaganfuck02b with dissolve
$ renpy.pause(1.0, hard=True)
t "AAH, FUCK, it's sssoo DEEP! AAAH!"
ma "Sounds like your pussy is [name]'s property after all..."
label BothTeaganFuck02bx:
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
            jump BothTeaganFuck02bx
        "Move on":
            t "My pussy has turned into a mush from so many orgasms..."
            ma "I can see that, my hand is caked in your cream Teagan... I bet it's real tasty too, especially mixed with [name]'s copious precum!"
            jump BothFuckChoiceDay04x

label BothPlay01x:
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
jump BothFuckChoiceDay04x

label BothTeaganBlowx:
scene teaganslap01 with dissolve
$ renpy.pause(1.0, hard=True)
p "You start first teach, open that mouth wide..."
stop music
play music "Sounds/teaganslow.mp3"
show teaganslow
show faster
call screen bothteaganslowx
screen bothteaganslowx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("BothTeaganFastx")
label BothTeaganFastx:
hide faster
play music "Sounds/teaganfast.mp3"
show teaganfast
show next
call screen bothteaganfastx
screen bothteaganfastx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("BothMariaBlowx")

label BothMariaBlowx:
hide teaganfast
hide teaganslow
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
call screen bothmariablowslowx
screen bothmariablowslowx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("BothMariaBlowFastx")
label BothMariaBlowFastx:
hide faster
play music "Sounds/hardsucking.mp3"
show mariablowfast
show cum
call screen bothmariablowfastx
screen bothmariablowfastx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("BothFuckCumx")

label BothFuckCumx:
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
scene bothcum03
$ renpy.pause(3.0, hard=True)
t "Damn, [name], you came like a true stallion. We're are covered from head to toes in your warm cream.... Mmmh!"
ma "Yeah, suck it up Teagan, and feed me some too please! It's so tasty and there's so much of it!"
play sound "Sounds/bothplay01.mp3"
$ renpy.pause(3.0, hard=True)
t "Let's get back to the others, it's getting late..."
ma "And they might wonder why we took so long..."
return

label Sex29:
stop music
$ mariapussyx = False
$ mariamilkx = False
scene mariabigdong01
$ renpy.pause(1.0, hard=True)
ma "So you are a  breast man [name] it seems?"
p "Yeah, and an ass man too. A titass-man is what I am."
scene mariabigdong02 with dissolve
$ renpy.pause(1.0, hard=True)
ma "And what do you think about MY tits and MY arse?"
p "Statues should be devoted to their perfection!"
ma "Such a charmer! Let's do someting naughty while the others are busy..."
scene mariaprefuck with dissolve
$ renpy.pause(1.0, hard=True)
ma "So, what would you like me to do to get that massive love pole down before anyone sees us?"
label MariaFuckChoiceDay04x:
menu:
    "Come and worship my muscles Maria!":
        jump MariaMuscles01x
    "I'm thirsty... for some milk! Let me suck on your huge nipples Maria!" if (mariamilkx == False):
        jump MariaMilk01x
    "Let me fuck your tender pussy Maria!" if (mariapussyx == False):
        jump MariaPussyFuck01x
    "Open your mouth and get ready to receive my load Maria!" if (mariapussyx == True) and (mariamilkx == True):
        jump MariaBlow01x

label MariaMuscles01x:
scene mariaworship with dissolve
$ renpy.pause(1.0, hard=True)
ma "Mmh, your biceps are so big [name]... They must be at least 20 inches around fully flexed..."
p "Way more after a heavy workout!"
ma "Mmh, so powerful... Time to show me what you can do with those muscles... Especially the one sticking straight up from your groin..."
jump MariaFuckChoiceDay04x

label MariaPussyFuck01x:
$ mariapussyx = True
scene mariaplay01 with dissolve
play sound "Sounds/mariaprefuck.mp3"
$ renpy.pause(15.0, hard=True)
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
label MariaPussyFuck01bx:
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
        jump MariaPussyFuck01bx
    "Move on":
        ma "You made me cum ssooo much..."
        p "Let's switch position and I'll make you cum even more..."
        jump MariaPussyFuck02x

label MariaPussyFuck02x:
scene mariafuck03 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Please be gentle with that monstrous thing, you're at least five times longer and thicker than my ex-husband..."
p "What a pindick, time for you to feel a REAL man. Me, DA MAN!"
scene mariafuck04 with dissolve
$ renpy.pause(1.0, hard=True)
ma "You're stabbing me in the womb with your giant love muscle!"
ma "Fuck me harder! I want to feel my pussy creaming over that fat shaft!"
label MariaPussyFuck02bx:
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
        jump MariaPussyFuck02bx
    "Move on":
        ma "Too... Too much..."
        jump MariaFuckChoiceDay04x
        
label MariaMilk01x:
$ mariamilkx = True
scene mariasuck01 with dissolve
play sound "Sounds/sucking.mp3"
$ renpy.pause(1.0, hard=True)
ma "You're in luck, Lolly was such a hungry kid that I am still lactating..."
p "Nothing like drinking directly from the source!"
scene mariasuck02 with dissolve
play sound "Sounds/sucking02.mp3"
$ renpy.pause(3.0, hard=True)
ma "Ooooh, I'm feeling so strange feeding you... But I love it, keep suckling!"
label MariaMilk01bx:
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
        jump MariaMilk01bx
    "Move on":
        ma "I don't think I have any milk left... You sucked me dry, you were more hungry than my daughter Lolly ever was!"
        jump MariaFuckChoiceDay04x
        
label MariaBlow01x:
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
call screen mariablowslowx
screen mariablowslowx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MariaBlowFastx")
label MariaBlowFastx:
hide faster
play music "Sounds/hardsucking.mp3"
play movie "Day4/mariablowfast.ogv" loop
show cum
call screen mariablowfastx
screen mariablowfastx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MariaFuckCumx")

label MariaFuckCumx:
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
ma "Thank you for giving me SO MUCH cream [name] It's delicious... My ex-husband could never come like that..."
ma "Let's get back to the others, it's getting late, and they might wonder why we took so long..."
return

label Sex28:
stop music
$ teagantitsx = False
$ teaganpussyx = False
scene teaganprefuck
$ renpy.pause(1.0, hard=True)
t "Now that my sumptuous breasts have gotten you rock-hard, what do you want to do [name]?"
label TeaganFuckChoiceDay04x:
menu:
    "Come and worship my muscles Teagan!":
        jump TeaganMuscles01x
    "I'd like to titfuck your giant tits as a good sloppy workout teach!" if (teagantitsx == False):
        jump TeaganTitFuck01x
    "Lick my balls and make them shiny with your spit!":
        jump TeaganLick01x
    "Get ready for a heavy pounding teach!" if (teaganpussyx == False):
        jump TeaganPussyFuck01x
    "Open your mouth and get ready to receive my load teach!" if (teaganpussyx == True) and (teagantitsx == True):
        jump TeaganBlow01x
        
label TeaganMuscles01x:
scene teaganworship with dissolve
$ renpy.pause(1.0, hard=True)
t "Wow, you're so muscular [name]... ALL OVER. I'm sorry I didn't believe a boy your age could be such a super-stud..."
p "Now you'll stop accusing me of bragging Teagan. Fuck yeah, I'm da man, I'm DA MAN!"
t "Mmmh, well show me what you can do with it then mister DA MAN!"
jump TeaganFuckChoiceDay04x
    
label TeaganTitFuck01x:
$ teagantitsx = True
scene teagantitfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Incredible, your cock is so big, I can see the head poking through my massive cleavage! That's never happened before!"
p "Wait till I pummel your titflesh and it will stick far enough for you to suck on it too!"
play sound "Sounds/teagantitfuck01.mp3"
$ renpy.pause(5.0, hard=True)
t "Yes, fuck my tits and my mouth you horse-hung stud!"
p "Ah? So you acknowledge that I wasn't bragging? That's good teach, you're learning!"
p "Now learn to worship my monster cock with your lips!"
label TeaganTitFuck01bx:
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
        jump TeaganTitFuck01bx
    "Move on":
        scene teagantitfuck03 with dissolve
        play sound "Sounds/teagantitfuck03.mp3"
        $ renpy.pause(4.0, hard=True)
        t "Damn, I'm all sticky with your abundant precum [name]!"
        jump TeaganFuckChoiceDay04x

label TeaganLick01x:
scene teaganlick01 with dissolve
play sound "Sounds/teaganlick01.mp3"
$ renpy.pause(4.0, hard=True)
p "Yeah, that's it, roll your tongue all over my massive seedmakers teach!"
t "They are each ssoo big, I can't even fit one in my mouth!"
scene teaganlick02 with dissolve
$ renpy.pause(1.0, hard=True)
p "You're doing good, AAHH!"
label TeaganLick01bx:
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
        jump TeaganLick01bx
    "Move on":
        t "I hope I serviced your balls well [name]! And that you'll give me a nice big fat juicy load in exchange..."
        p "Don't worry about that! I have an endless supply of teenage spunk in there!"
        jump TeaganFuckChoiceDay04x

label TeaganPussyFuck01x:
$ teaganpussyx = True
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
label TeaganPussyFuck01bx:
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
        jump TeaganPussyFuck01bx
    "Move on":
        t "I am ready to receive that great big monster cock [name]!"
        jump TeaganPussyFuck02x

label TeaganPussyFuck02x:
scene teaganfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
t "What? No, my pussy is my property!"
p "You sure about that?"
scene teaganfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
t "AAH, FUCK, it's sssoo DEEP! AAAH!"
ma "Sounds like your pussy is [name]'s property after all..."
label TeaganPussyFuck02bx:
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
            jump TeaganPussyFuck02bx
        "Move on":
            t "My pussy has turned into a mush from so many orgasms..."
            jump TeaganFuckChoiceDay04x
            
label TeaganBlow01x:
scene teaganslap01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Time to get your creamy reward teach, open that mouth wide..."
stop music
play music "Sounds/teaganslow.mp3"
show teaganslow
show faster
call screen teaganblowslowx
screen teaganblowslowx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("TeaganBlowFastx")
label TeaganBlowFastx:
hide faster
play music "Sounds/teaganfast.mp3"
show teaganfast
show cum
call screen teaganblowfastx
screen teaganblowfastx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TeaganFuckCumx")

label TeaganFuckCumx:
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
hide staminaminus01
t "Damn, [name], you came like a true stallion. I'm covered from head to toes in your warm cream.... Mmmh!"
t "Let's get back to the others, it's getting late..."
return

label Sex35:
stop music
scene pole07
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
fa "I... couldn't resist doing a bit of pole-dancing... Do't tell anyone please!"
p "Don't worry Francine. My lips are sealed (and yours will be soon on my cock!)"
fa "How did it go at the till?"
p "Err... Fine, only satisfied customers, but it's empty now, so I came to check on you..."
scene pole11 with dissolve
$ renpy.pause(1.0, hard=True)
fa "Well, that's nice of you... Did you enjoy the show?"
p "Of course! Although it was cut short too fast..."
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
return

label Sex38:
stop music
scene debbycockslap01 
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
p "You liked that didn't you aunt Debby?"
d "Yes... But don't call me aunt Debby... Call me \"filthy slut\"... That's what I am..."
p "Now I'm gonna cock-slap that tight arse of yours filthy slut!"
d "Oooh, yes master, I deserve it..."
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
d "I'm such a dirty whore for your great big cock Master... Please, do whatever you want with my filthy body!"
scene debbybed01 with dissolve
play sound "Sounds/debbyprefuck01.mp3"
$ renpy.pause(10.0, hard=True)
d "I am ready to be treated like the cheap whore that I am Master..."
$ debbyfrontfuckx = False
$ debbybackx = False
$ debbytitfuckx = False
$ debbydoggy01x = False
label DebbyFuckChoiceDay04bx:
scene debbybed01 with dissolve
menu:
    "Let me titfuck your massive tits filthy slut!" if (debbytitfuckx == False):
        jump DebbyTitfuckDay04x
    "On the bed on your back slave!" if (debbybackx == False):
        jump DebbyBackFuckDay04x
    "I want to lick your hard nipples and maul your tits!":
        jump DebbyNippleDay04x
    "A cheap whore like you deserves a good pussy-pounding!" if (debbyfrontfuckx == False):
        jump DebbyFrontFuckDay04x
    "Be a good bitch and get on all fours for this horny dog!" if (debbydoggy01x == False):
        jump DebbyDoggyFuckDay04x        
    "Time to finish me off slave!" if (debbyfrontfuckx == True) and (debbybackx == True) and (debbytitfuckx == True):
        jump DebbyBedMovie04x

label DebbyDoggyFuckDay04x:
$ debbydoggy01x = True
scene debbydoggy01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Open wide for your Master's cock, bitch!"
d "Yes, I'm a bitch... IN HEAT!"
scene debbydoggy02 with dissolve
window hide
play sound "Sounds/debbydoggy01.mp3"
$ renpy.pause(2.0, hard=True)
d "Oh, FUCK, master's cock is ssoo HUGE!"
label DebbyDoggyFuckDay04bx:
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
        jump DebbyDoggyFuckDay04bx
    "Move on":
        p "You did good slave, it's now time to move on to something else..."
        jump DebbyFuckChoiceDay04bx
            
label DebbyTitfuckDay04x:
$ debbytitfuckx = True
scene debbytitfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
d "Let me lick your bull-sized balls while you pleasure yourself between my tits Master!"
p "Fuck yeah! That's a good little slut! I want my heavy seedmakers to be shiny with your filthy spit your hear me?"
d "Of course Master..."
scene debbytitfuck02 with dissolve
window hide
play sound "Sounds/debbytitfuck01.mp3"
$ renpy.pause(6.0, hard=True)
d "Of course Master... Are my tits good enough for your giant fuckstick?"
p "Mmh, yes, but I'm gonna pummel them faster now! SO keep up with your ball-licking slave!"
label DebbyTitFuckDay04bx:
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
        jump DebbyTitFuckDay04bx
    "Move on":
        p "You did good slave, it's now time to move on to something else..."
        jump DebbyFuckChoiceDay04bx

label DebbyBackFuckDay04x:
$ debbybackx = True
scene debbyback01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Offer your gaping slut-hole to my massive teenage cock slave!"
d "My filthy hole belongs to you Master... Do as you please with it!"
label DebbyBackFuckDay04bx:
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
$ debbybackx = True
menu:
    "Repeat":
        p "Your pussy needs some more destroying!"
        jump DebbyBackFuckDay04bx
    "Move on":
        p "I've punished your dirty hole enough for the moment slave... I'm giving you a respite..."
        d "Thank you Master, I am not worthy of such generosity..."
        jump DebbyFuckChoiceDay04bx

label DebbyNippleDay04x:
scene debbybed02 with dissolve
play sound "Sounds/sucking.mp3"
$ renpy.pause(2.0, hard=True)
d "Ooh, you suck on my nipples ssoo good! Maul my tits Master!"
p "They look red and erect now, it's time for something else slave..."
jump DebbyFuckChoiceDay04bx

label DebbyFrontFuckDay04x:
$ debbyfrontfuckx = True
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
label DebbyFrontFuckDay04bx:
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
        jump DebbyFrontFuckDay04bx
    "Move on":
        p "Your dirty hole is creaming all over the place, let's switch position whore!"
        jump DebbyFuckChoiceDay04bx

label DebbyBedMovie04x:
scene debbyballs with dissolve
$ renpy.pause(1.0, hard=True)
d "I can feel your balls are ready to unleash their massive store of pent-up young and yummy cum Master!"
p "Fuck yeah! I'm close to bursting a nut, finish me off slave!"
play music "Sounds/debbybedslow.mp3"
show debbybedslow
show faster
call screen debbyfuckslowday04x
screen debbyfuckslowday04x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("DebbyFuckFastDay04x")
label DebbyFuckFastDay04x:
hide faster
stop music
play music "Sounds/debbybedfast.mp3"
show debbybedfast
show cum
call screen debbyfuckfastday04x
screen debbyfuckfastday04x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("DebbyFuckCumDay04x")

label DebbyFuckCumDay04x:
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
return

label Sex31:
stop music
scene clinic03
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
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
dr "That is indeed an exceptional load... Please bring the receptacle over to the lab for analysis once the boy is done cumming like a firehose into the extractor nurse Racks..."
ra "Of course doctor, I believe he is almost done now..."
p "Oh fuck! My balls.... Hurts so much... I'm drained... FUCK!"
stop music
scene clinic04 with dissolve
$ renpy.pause(1.0, hard=True)
dr "Well done boy. You gave us a large enough quantity of sperm to finish our analysis. You can come back anytime to make a sperm donation..."
p "My pleasure doctor. Can I have nurse Racque's phone number?"
dr "That bimbo? Trust me, you don't want to get anywhere near her, she's got more venereal diseases than a president who fucks pornstars for a living."
je "I am very disappointed by your non-commitment to this scientific endeavor!"
dr "Now off you go, I have some patients with tiny useless noodle dicks to attend to."
return   

label Sex32:
stop music
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
p "I have a present for you Brittany."
scene britbeach05 with dissolve
$ renpy.pause(1.0, hard=True)        
br "Oh really? What is it? It'd better be a present that befits a princess like me!"
p "Yes it is, look!"
scene britbeach07 with dissolve
br "Oh my God, it's beautiful, it must have cost ssoo much too since it's golden!"
p "Yes, I spent all my money on this for you, but it was worth it your Magnificient Beautifulness."
br "Well, thank you [name]? Is that right? Why don't you sit next to me for a while..."
scene britbeach06 with dissolve
$ renpy.pause(1.0, hard=True)
br "So... [name], right? I can't imagine you would vote for anyone else but me on Friday, right?"
p "I don't know, I'll have to decide on Friday really..."
br "But surely, you can be persuaded to make up your mind already..."
scene britbeach09 with dissolve
$ renpy.pause(1.0, hard=True)
br "Aren't these breasts simply the most succulent you've ever seen?"
p "They sure are VERY nice...."
br "Much better than Kate's weird-looking fake tits, don't you think [name]?"
p "Err... Yeah, sure..."
scene britbeach10 dissolve
$ renpy.pause(1.0, hard=True)
br "And how about my arse? What man could resist such perfectly defined buttocks and thighs?"
p "I don't know... A blind man?"
br "I hope you understand now... There is no other choice than casting your vote for me."
p "Ga..ga...ga..."
br "I'm sure you are a busy boy, so shoo, go and do whatever you pervy boys do."
return

label Sex33:
scene sandybeach01
stop music
play music "Sounds/oceanwaves.mp3"
$ sandytitsx = False
$ sandysidex = False
$ sandydoggyx = False
sa"Oh, my Prince Charming, what a beautifully romantic place you found, far from the madding crowd!"
p "Yes, it's the perfect spot for us to get...more intimate..."
sa"And to get back to our natural human state without constraints by being naked...In total communion with Mother Nature."
p "Yes, only the best for you my princess..."
sa"Let's get naked, I want to be in total communion with Mother Nature... and you!"
label SandyFuckDay04x:
scene sandyfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
sa"First, my top, so you can admire my large, firm and TOTALLY NATURAL breasts."
p "Yep, entirely believable, especially in a 3D game."
scene sandyfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
sa"And then, the bottom, so you can admire my toned legs and firm buttocks..."
p "Your body is spectacular Sandy, you must really take good care of it..."
sa"Your turn lover, show me the humongous cock that will soon ravish my body..."
scene sandyfuck03 with dissolve
$ renpy.pause(1.0, hard=True)
sa"Yes, just as I remember it... Rock-hard and fully engorged with lust... Clearly in need of some luscious lips to love it and worship it..."
scene sandyfuck04 with dissolve
play sound "Sounds/sandysuck01.mp3"
$ renpy.pause(1.0, hard=True)
p "You can read its mind my Prin..."
scene sandyfuck04b with dissolve
play sound "Sounds/ryanmoan.mp3"
$ renpy.pause(3.0, hard=True)
p "AAAH...cess!"
label SandyBlowDay04x:
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
        jump SandyBlowDay04x
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa"And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay04x

label SandyFuckChoiceDay04x:
menu:
    "Spoon her from the side" if (sandysidex == False):
        jump SandySideDay04x
    "Stick your cock between her huge jugs" if (sandytitsx == False):
        jump SandyTitsDay04x
    "Take her from behind like a bitch in heat" if (sandydoggyx == False):
        jump SandyDoggyDay04x
    "Watch her bounce up and down your giant crank" if (sandysidex == True) and (sandytitsx == True) and (sandydoggyx == True):
        jump SandyFinalDay04x

label SandySideDay04x:
$ sandysidex = True
scene sandyside01 with dissolve
play sound "Sounds/sandyside01.mp3"
$ renpy.pause(4.0, hard=True)
sa"Oooh... You're so muscular. And that cock... It's so fucking big..."
p "It's not even half-way in yet..."
scene sandyside02 with dissolve
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
p "Now it is..."
label SandySideDay04bx:
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
        jump SandySideDay04bx
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa"And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay04x

label SandyTitsDay04x:
$ sandytitsx = True
scene sandytits01 with dissolve
play sound "Sounds/sandytitfuck01.mp3"
$ renpy.pause(2.0, hard=True)
sa"OOoh, my Prince Charming, my huge tits can't even bury that massive fuckstick, the head is sticking out..."
p "It will be sticking out way more once I do this..."
scene sandytits02 with dissolve
sa"It's so fucking big... Ssooo fucking big..."
label SandyTitsDay04bx:
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
        jump SandyTitsDay04bx
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa"And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay04x

label SandyDoggyDay04x:
$ sandydoggyx = True
scene sandydoggy01 with dissolve
$ renpy.pause(1.0, hard=True)
sa"My hole is all yours my Prince! Ram it in as deep as you like!"
p "Sure will do!"
scene sandydoggy01 with dissolve
play sound "Sounds/sandydoggy01.mp3"
$ renpy.pause(3.0, hard=True)
sa"AAAAH, it's so good feeling your giant teenage cock stretching my tiny fuckhole!"
label SandyDoggyDay04bx:
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
        jump SandyDoggyDay04bx
    "Move on":
        scene sandyfuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        sa"And what would you like us to do next my Prince Charming?"
        jump SandyFuckChoiceDay04x

label SandyFinalDay04x:
scene sandybeachkiss with dissolve
play sound "Sounds/sandyslut.mp3"
$ renpy.pause(3.0, hard=True)
sa"I'm going to bounce up and down your shaft and make you feel sssoo good my Prince... You'll pop in no time!"
stop music
play sound "Sounds/oceanwaves.mp3"
play music "Sounds/sandyfuckslow.mp3"
show sandyfuckslow
show faster
call screen sandyfuckslowday04x
screen sandyfuckslowday04x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("SandyFuckFastday04x")
label SandyFuckFastday04x:
hide faster
play music "Sounds/sandyfuckfast.mp3"
show sandyfuckfast
show cum
call screen sandyfuckfastday04x
screen sandyfuckfastday04x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("SandyFuckCumday04x")

label SandyFuckCumday04x:
hide sandyfuckfast
hide sandyfuckslow
stop music
play music "Sounds/oceanwaves.mp3"
scene sandycum01
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
p "FUUUCKK! Your bouncing arse is making me cum so HARD!"
sa"Yes, YES, I can feel it filling up my hole! SSSOO much cum for your Princess baby!"
sa"Damn, you're filling me up to bursting point, pull it out, pull it out!"
scene sandycum02 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
sa"Let me get hold of that cum-cannon! I want you to keep cumming like a stallion and cover my tits!"
scene sandycum03 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
sa"Mmmh, yeah, that's it, keep cumming and cover my big titties with your splooge... Sssoo, so much of it!"
p "You're making me cum buckets, AAAH!"
sa"Well you did REAL good [name]... Now I have to go back into the ocean to clean myself of the tons of cum you've covered me with!"
sa"Don't wait for me, I'll be a WHILE cos you came SSSOOO MUCH!"
p "See you Princess, I'll come back to... err... save you anytime!"
return

label Sex34:
$ maddyblowjobx = False
$ maddyarsex = False
scene cabin02
stop music
$ renpy.pause(1.0, hard=True)
md "Help me [name]! I'm all tied up, I was kidnapped!"
p "Of course Maddy, I'm here to save you."
scene cabin03 with dissolve
p "Here, let me untie you... Were you... raped?"
md "No, but he was about to, he threatened me, it was horrible..."
p "You're safe now, let's get out of here before he comes back."
md "Thank you so much, you saved my life! You are my hero..."
scene cabin04 with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
md "How did you find me?..."
p "I ran into your rapi... I mean kidnapper and fought with him. And I beat him, he was no match for my strength! I'm DA MAN!"
md "You sure are... And I can see why you beat him, your muscles are so... AWESOME!"
p "I've got another muscle that's huge and hard... You wanna feel its awesome power?"
md "Yes, I'm ready! Fuck me with that giant love muscle of yours [name]!"
p "I spotted a small secluded bay on the way here, let's go there, I'm so horny, I can't wait!"
label MaddyFuckDay04x:
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
label MaddyFootDay04bx:
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
        jump MaddyFootDay04bx
    "Cum quickly (no stamina penalty)":
        scene maddyfoot03 with dissolve
        play sound "Sounds/ryancumming.mp3"
        $ renpy.pause(2.0, hard=True)
        p "Fuck, your feet are so good on my knob, RHHAAA!"
        md "Wow, I didn't expect you to cum like a stallion so soon [name]...."
        p "Don't worry, it was just a tiny premature load, let's move on to the main dish of the day!"
        jump MaddyFuckChoiceDay04x

label MaddyFuckChoiceDay04x:
scene maddybeach04 with dissolve
$ renpy.pause(1.0, hard=True)
md "I'm ready for anything, what are you ready for...?"
menu:
    "How about some anal to really get our juices going?" if (maddyarsex == False):
        jump MaddyArseDay04x
    "How about a blowjob, and I'll lick your pussy at the same time?" if (maddyblowjobx == False):
        jump MaddyBlowjobDay04x
        
label MaddyArseDay04x:
$ maddyarsex = True
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
label MaddyArseDay04bx:
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
        jump MaddyArseDay04bx
    "Move on":
        scene maddyarse02 with dissolve
        $ renpy.pause(1.0, hard=True)
        md "This is too much, my stomach is so full of cock! Please let's switch position!"
        menu:
            "Alright, how about a blowjob, and I'll lick your pussy at the same time?" if (maddyblowjobx == False):
                jump MaddyBlowjobDay04x
            "Fuck her sweet pussy" if ((maddyarsex == True) and (maddyblowjobx == True)):
                jump MaddyEndFuckDay04x

label MaddyBlowjobDay04x:
$ maddyblowjobx = True
scene maddyfuck05 with dissolve
$ renpy.pause(1.0, hard=True)
scene maddyfuck05b with dissolve
play sound "Sounds/maddyblow01.mp3"
$ renpy.pause(5.0, hard=True)
md "I've never sucked a cock this huge before... But I don't care, I want to choke on it!"
label MaddyBlowjobDay04bx:
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
        jump MaddyBlowjobDay04bx
    "Move on":
        scene maddybeach04 with dissolve
        $ renpy.pause(1.0, hard=True)
        md "My jaws are starting to tire, your cock is just too gigantic! Please let's switch position!"
        menu:
            "Alright, how about some anal to really get our juices going?" if (maddyarsex == False):
                jump MaddyArseDay04x
            "Fuck her sweet pussy" if ((maddyarsex == True) and (maddyblowjobx == True)):
                jump MaddyEndFuckDay04x


label MaddyEndFuckDay04x:
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
call screen maddyfuckslowx
screen maddyfuckslowx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MaddyFuckFastx")
label MaddyFuckFastx:
hide faster
play music "Sounds/maddyfuckfast.mp3"
show maddyfuckfast
show cum
call screen maddyfuckfastx
screen maddyfuckfastx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MaddyFuckCumx")

label MaddyFuckCumx:
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
md "Good thing this cove is secluded, I can go and clean myself in the sea. Fancy coming along [name]?"
p "Phew, yeah, a nice cooling-off in the ocean would be good!"
scene maddyafterfuck with dissolve
$ renpy.pause(1.0, hard=True)
md "Don't tell Frieda you had sex with me, she looks up to me, I don't want to disappoint her..."
p "Sure, absolutely nobody will ever know, I swear... (fingers crossed)."
return

label Sex36:
stop music
play sound "Sounds/dooropen.mp3"
scene shopcabin03
$ rightcabinseen = True
cy "How rude, I'm all naked and your barge in here just as I was about to put on this bikini..."
p "Sorry but all the stalls are taken and I wanted to try on these new mega-sized briefs."
cy "Mega-sized briefs? Well maybe I could make some room for you in here then... But no touching naughty boy..."
cy "But first, let me put on this bikini..."
scene shopcabin03b with dissolve
$ renpy.pause(1.0, hard=True)
cy "What do you think? Will you be having problems putting on your briefs over that hardening rod, hee hee..."
p "I'll...try anyway if you don't mind..."
$ chiyoblowjobx = False
$ chiyopussyx = False
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
scene chiyofuck01 with dissolve
$ renpy.pause(1.0, hard=True)
cy "What would get me really horny now is a big dildo so I could play with my little arsehole and stretch it out for... that giant thing."
p "How about this one lady? Big enough for you?"
cy "Yes! And black too... My favorite color... Gimme me that, boy, and watch while you jerk your fat donkey-dick!"
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
cy "Mmh, I know and it DOES look tasty... What would you want to do with it naughty naughty boy?"
menu:
    "If it looks tasty, then give me a blowjob!":
        jump ChiyoBlowjobDay04x
    "Your pussy looks tasty... And ready for a good pounding!":
        jump ChiyoPussyDay04x
cy "I think you've seen enough naughtiness for the day. I came here to buy a bikini, not to get fucked by some random horse-hung boy. So you can leave now..."
p "AAARGH! She's doing it to me again!"
play sound "Sounds/doorclosing.mp3"
scene shopcabin01 with dissolve
$ renpy.pause(1.0, hard=True)
jump ShopCabinChoiceDay04bx
label ChiyoBlowjobDay04x:
$ chiyoblowjobx = True
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
label ChiyoBlowjobDay04bx:
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
$ chiyoblowjobx = True
stop sound
menu:
    "Repeat":
        jump ChiyoBlowjobDay04bx
    "Your pussy looks tasty... And ready for a good pounding!" if (chiyopussyx == False):
         jump ChiyoPussyDay04x
    "It's time to stretch that gaping anus even more than that puny dildo you used!" if (chiyoblowjobx == True) and (chiyopussyx == True):
        jump ChiyoArseDay04x

label ChiyoPussyDay04x:
scene chiyopussy01 with dissolve
play sound "Sounds/chiyopussy01.mp3"
$ renpy.pause(7.0, hard=True)
p "That's nothing, I'm not even half-way in!"
scene chiyopussy02 with dissolve
play sound "Sounds/chiyopussy02.mp3"
$ renpy.pause(11.0, hard=True)
cy "Oh my God, you're so deep!"
label ChiyoPussyDay04bx:
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
$ chiyopussyx = True
stop sound
menu:
    "Repeat":
        jump ChiyoPussyDay04bx
    "If it looks tasty, then give me a blowjob!" if (chiyoblowjobx == False):
        jump ChiyoBlowjobDay04x
    "It's time to stretch that gaping anus even more than that puny dildo you used!" if (chiyoblowjobx == True) and (chiyopussyx == True):
        jump ChiyoArseDay04x

label ChiyoArseDay04x:
scene chiyoarse01 with dissolve
$ renpy.pause(0.3, hard=True)
cy "I'm ready to have my little arsehole stretched by your naughty prick!"
play music "Sounds/chiyofuckslow.mp3"
show chiyofuckslow
show faster
call screen chiyofuckslowx
screen chiyofuckslowx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("ChiyoFuckFastx")
label ChiyoFuckFastx:
hide faster
play music "Sounds/chiyofuckfast.mp3"
show chiyofuckfast
show cum
call screen chiyofuckfastx
screen chiyofuckfastx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("ChiyoFuckCumx")

label ChiyoFuckCumx:
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
cy "I'm gonna stay here for a while... I need to empty the ounces of cum you dumped inside me!"
cy "I think the whole shop will smell of your seed for the rest of the afternoon, hee hee!"
p "I love filthy girls like you Chiyo, but I have to get going!"
return

label Sex37:
stop music
play music "Sounds/policesound.mp3"
scene audaciouscop02
$ renpy.pause(1.0, hard=True)
co "So, into \"photography\" are we?"
p "Yeah. Is there a law against that?"
co "Shut up and get undressed NOW!"
p "What???"
co "You heard me! You're into photography, let's see how YOU like to get photographed NAKED IN A JAIL!"
p "This is outrageous, I want it to be entered into the record that I am showing you my giant schlong under duress!"
co "Quit the bragging and quit the pants!"
scene audaciouscop03 with dissolve
$ renpy.pause(1.0, hard=True)
co "Damn boy, quite the truncheon you're carrying there... I... didn't expect this."
p "I always carry a loaded weapon on me."
co "Is that so, funny boy? Let's see how much ammunition you've got there then..."
co "I'll open the door, don't do anything silly or I'll tase you..."
scene copblow01 with dissolve
$ renpy.pause(1.0, hard=True)
co "First, you are going to unload that weapon down my throat! And you'd better be quick!"
scene copblow02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Alright!"
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
co "That was good, my belly is full and my tits are covered in your sticky cum..."
co "Now you'd better stay hard so I can get a ride on that fat truncheon."
p "No worries officer, spread your legs and my mighty lovepole will deliver!"
scene copfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
co "That's it, MY way, nice and slow, I want it DEEP!"
scene copfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
p "My God, her pussy is so tight, she's gonna milk me in no time!"
co "That's right, I want a nice big fat load sloshing around inside me, get it boy?"
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
co "Yeah, dump that load inside me, give me everything you've got stud!"
p "Fuck, I'm getting totally drained! AAAH"
scene copfuckcum02 with dissolve
play sound "Sounds/ryancumming.mp3"
co "You did good, my legs are numb, now you can go..."
p "This looks like a crime scene. A SEX crime scene... I'd better get the hell out of here..."
return

label Sex39:
stop music
$ debbychairx = False
$ debbydoggyx = False
$ debbyblowx = False
$ debbymaulx = False
scene debbyoffice02
$ renpy.pause(2.0, hard=True)
d "Ready! You can open the door now [name]..."
scene debbyoffice03 with dissolve
$ renpy.pause(1.0, hard=True)
p "(Damn, she looks so fine in that micro-bikini)"
d "So...What do you think? Maybe I should turn round first so you can inspect it in more details..."
scene debbyoffice04 with dissolve
$ renpy.pause(1.0, hard=True)
p "Yes, yes I see... Interesting design, innovative... May I feel the fabric?"
d "Yes of course, the fabric quality is indeed very important..."
scene debbyoffice07 with dissolve
$ renpy.pause(2.0, hard=True)
p "Mmm.... It feels soft yet sturdy..."
d "I'm impressed, you really sound like you know what you're talking about [name]..."
d "Why don't you pull the string up and see your auntie's big old titties?"
scene debbyoffice08 with dissolve            
d "Oops... See what a dirty whore I am... I guess I have no choice but to pull my bottom down too now... So you can FUCK ME MY STUD NEPHEW!"
scene debbyofficeprefuck01 with dissolve
play sound "Sounds/debbyprefuck01.mp3"
$ renpy.pause(10.0, hard=True)
d "I am ready to be treated like the cheap whore that I am Master..."

label OfficeDebbyFuckChoiceDay04bx:
scene debbyofficeprefuck01 with dissolve
menu:
    "Let me fuck your dirty hole nice and slow!" if (debbychairx == False):
        jump OfficeDebbyChairFuckDay04x
    "Give me a nice sloppy blowjob slave!" if (debbyblowx == False):
        jump OfficeDebbyBlowDay04x
    "I want to maul your hard nipples with my teeth!" if (debbymaulx == False):
        jump OfficeDebbyNippleDay04x
    "A cheap whore like you deserves a good pussy-pounding!" if (debbydoggyx == False):
        jump OfficeDebbyDoggyDay04x
    "Time to finish me off slave!" if (debbymaulx == True) and (debbydoggyx == True) and (debbyblowx == True) and (debbychairx == True):
        jump OfficeDebbyMoviex
    
label OfficeDebbyBlowDay04x:
$ debbyblowx = True
scene debbyblowoffice01 with dissolve
$ renpy.pause(1.0, hard=True)
d "Let me lick your bull-sized balls while you pleasure yourself between my tits Master!"
scene debbyblowoffice02 with dissolve
$ renpy.pause(1.0, hard=True)
label OfficeDebbyBlowDay04bx:
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
        jump OfficeDebbyBlowDay04bx
    "Move on":
        p "You did good slave, it's now time to move on to something else..."
        jump OfficeDebbyFuckChoiceDay04bx

label OfficeDebbyChairFuckDay04x:
$ debbychairx = True
scene debbyofficefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Offer your gaping slut-hole to my massive teenage cock slave!"
d "My filthy hole belongs to you Master... Do as you please with it!"
label OfficeDebbyChairFuckDay04bx:
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
        jump OfficeDebbyChairFuckDay04bx
    "Move on":
        p "I've punished your dirty hole enough for the moment slave... I'm giving you a respite..."
        d "Thank you Master, I am not worthy of such generosity..."
        jump OfficeDebbyFuckChoiceDay04bx

label OfficeDebbyNippleDay04x:
scene debbyofficenipple with dissolve      
play sound "Sounds/sucking.mp3"
$ renpy.pause(1.0, hard=True)
d "Ooh, you suck on my nipples ssoo good! Maul my tits Master!"
p "They look red and erect now, it's time for something else slave..."
$ debbymaulx = True
jump OfficeDebbyFuckChoiceDay04bx

label OfficeDebbyDoggyDay04x:
$ debbydoggyx = True
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
label OfficeDebbyDoggyDay04bx:
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
        jump OfficeDebbyDoggyDay04bx
    "Move on":
        p "Your dirty hole is creaming all over the place, let's switch position whore!"
        jump OfficeDebbyFuckChoiceDay04bx


label OfficeDebbyMoviex:
stop music
play music "Sounds/debbyslow.mp3"
show debbyofficeslow
show faster
call screen officedebbyfuckslowday04x
screen officedebbyfuckslowday04x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("OfficeDebbyFuckFastDay04x")

label OfficeDebbyFuckFastDay04x:
hide faster
play music "Sounds/debbyfast.mp3"
show debbyofficefast
show cum
call screen officedebbyfuckfastday04x
screen officedebbyfuckfastday04x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("OfficeDebbyFuckCumDay04x")

label OfficeDebbyFuckCumDay04x:
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
p "I'd better get going, it's getting quite late!"
return

label Sex40:
stop music
$ tanyablowx = False
$ tanyaridex = False
scene tanyabed01
play music "Sounds/tanyamusic.mp3"
$ renpy.pause(1.0, hard=True)
ta "Oh, look at poor little Darryl... All tied up and with his cock constrained in his tight briefs..."
dl "Untie me for fuck's sake Tanya! Wh... Why is this boy here again? I told you I never wanted to see him again in MY house!"
ta "He's here to get us lots of money... I'm sorry honeypot, but I read our viewers' requests last night on twatter and they all wanted to see me handle his young monster cock!"
dl "No please, don't do this to me, I'm all tied up, this is so humiliating!"
ta "Well that's the idea darling... Now hush, showtime is in a few seconds, [name], can you go and turn the webcam on please?"
p "Sure Tanya!"
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
p "Oh yeah, let the viewers (and me) see those firm globes Tanya!"
ta "Of course, meanwhile, pop one of your mega-sized condoms on that beast!"
scene tanyabed07 with dissolve
$ renpy.pause(1.0, hard=True)
ta "My God, will you look at that hubby? I didn't even know they made condoms that size!"
play sound "Sounds/tanya01.mp3"
$ renpy.pause(3.0, hard=True)
p "It's a tight fit but it will hold, it says they are made from extra-strong latex."
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
label TanyaBed04Day04bx:
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
        jump TanyaBed04Day04bx
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
    "Get a blowjob" if (tanyablowx == False):
        ta "Good idea, and let's do it right in front of Darryl's face, you don't mind do you hubby?"
        dl "Of course I fucking mind! Don't do this to me!"
        ta "Sorry, but that's what our viewers want and that's what we'll give them..."
        jump TanyaBlowjobDay04x
    "Fuck her above Darryl" if (tanyaridex == False):
        jump TanyaRideDay04x

label TanyaBlowjobDay04x:
$ tanyablowx = True
scene tanyabed11 with dissolve    
$ renpy.pause(1.0, hard=True)
ta "Just the tip is filling up my mouth entirely. Can you see that hubby?"
dl "Stop it Tanya, you're torturing me!"
scene tanyabed11b with dissolve    
$ renpy.pause(1.0, hard=True)
ta "It's so big Darryl, I can barely take a third of his young monster dong! And I can deepthroat you easily..."
dl "I beg you to stop comparing me to this stu... I mean little prick!"
ta "Just watch me blow this STUD! That's what you were going to say hubby, right?"
label TanyaBlowjobDay04bx:
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
        jump TanyaBlowjobDay04bx
    "Get her to take MORE of your cock!":
        p "I think you can take more Tanya, come on, do it! AAAH!"
        scene tanyabed11c with dissolve    
        play sound "Sounds/hallesuck02.mp3"
        $ renpy.pause(3.0, hard=True)
        dl "I can't watch this! This is too humiliating!"
        jump TanyaBlowjobDay04bx
    "Fuck her above Darryl" if (tanyaridex == False):
        jump TanyaAboveDay04x
    "Let her ride you like a wild bronco" if (tanyaridex == True) and (tanyablowx == True):
        jump TanyaRideDay04x
        
label TanyaAboveDay04x:
$ tanyaridex = True
scene tanyabed12 with dissolve
play sound "Sounds/tanya04.mp3"
$ renpy.pause(3.0, hard=True)
ta "Come and stick that big fucking cock in me!"
scene tanyabed13 with dissolve
$ renpy.pause(3.0, hard=True)
p "Ready to have your pussy ruined for your hubby by a way bigger cock than his?"
ta "Ooh, fuck yeah!"
label TanyaAboveDay04bx:
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
        jump TanyaAboveDay04bx
    "Get a blowjob" if (tanyablowx == False):
        ta "Good idea, and let's do it right in front of Darryl's face, you don't mind do you hubby?"
        dl "Of course I fucking mind! Don't do this to me!"
        ta "Sorry, but that's what our viewers want and that's what we'll give them..."
        jump TanyaBlowjobDay04x
    "Let her ride you like a wild bronco" if (tanyaridex == True) and (tanyablowx == True):
        jump TanyaRideDay04x
    
label TanyaRideDay04x:
scene tanyabed15 with dissolve
$ renpy.pause(1.0, hard=True)
ta "Let me ride that donkey-dick stud! I can't wait to feel that monstrous rock-hard member deep inside of me while my helpless hubby watches on!"
dl "No, don't fuck him please Tanya!"
ta "Stop pretending you don't like it honey, I can see your erection distending your tight briefs... Just watch and enjoy the ride, I sure will!"
play music "Sounds/tanyafuckslow.mp3"
show tanyafuckslow
show faster
call screen tanyafuckslowx
screen tanyafuckslowx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("TanyaFuckFastx")
label TanyaFuckFastx:
hide faster
play music "Sounds/tanyafuckfast.mp3"
show tanyafuckfast
show cum
call screen tanyafuckfastx
screen tanyafuckfastx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TanyaFuckCumx")

label TanyaFuckCumx:
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
scene tanyacum04 with dissolve
ta "Damn boy, what a fucking load! I'm covered in spunk.... Darryl is too, and I can tell he came in his tight briefs...."
dl "I DID NOT! I... thought this was disgusting! I'm gonna kill that son of a bitch, untie me Tanya!"
ta "Shhush honey, let this boy go home now and... I'll let you lick his creampie out of me."
dl "What? What makes you think I want to do such a filthy thing?"
ta "Your spoilt briefs don't lie, you enjoyed it, I can tell... Let the show go on!"
p "I don't think I ever came that much in my life... Phew! I'd better get going now..."
$ renpy.pause(1.0, hard=True)
ta "Well, my horny viewers, I hope you enjoyed the show tonight, I did for sure, I came ssooo many times on that massive love muscle..."
ta "Say goodbye to our viewers hubby, I'll get your handcuffs off so you can help me clean those semen-stained sheets... My way!"
return

label Sex41:
stop music
play sound "Sounds/dooropen.mp3"
scene randyshop01
$ renpy.pause(1.0, hard=True)
p "Oh, it's that couple I saw on the beach on the first day I arrived!"
rc"Mmmh, I can see that got you horny!"
rb "Fuck yeah baby, let's do it right here... Hey, there's someone watching us!"
scene randyshop02 with dissolve
$ renpy.pause(1.0, hard=True)
rb "What are you looking at? Never seen a huge thick pre-teen monstercock before or what?"
rc"I doubt it honey, your young giant penis is the biggest ever! I bet he wants to watch, isn't that right boy?"
p "Ok, why not, I'm bored anyway. (50\%\ chance of +1 stamina)"
rc"First, I'll get my pussy wet to take my boyfriend's behemoth! It's important since he's so gigantic..."
rb "Watch this buddy. I'm gonna pound her sweet pussy till she's begging for me to stop!"
scene randyshop03 with dissolve
$ renpy.pause(1.0, hard=True)
rc"Oh fuck baby, you're stretching me ssoo good... And you're so deep inside me!"
rb "I'm not even half-way in, open wide to take in another ten inches!"
scene randyshop04 with dissolve
$ renpy.pause(0.3, hard=True)
rc"AAAH! Such a fucking megadong! Give me more baby!"
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
rc"Cum inside me baby, I want to feel my stomach bloat with your tenth giant load of the day!"
scene randyshop05 with dissolve
stop music
play sound "Sounds/randyboycumming.mp3"
$ renpy.pause(1.0, hard=True)
rb "RHHAAA, yes, I 'm cumming.... AAAH!"
rc"Oh, my stomach is about to burst from being overfilled with your young spunk! Come all over me baby!"
scene randyshop06 with dissolve
play sound "Sounds/randyboycumming02.mp3"
$ renpy.pause(1.0, hard=True)
rc"Look at all those massive cumshots flying everywhere after he totally filled me with ounces of boycream already!"
scene randyshop07 with dissolve
play sound "Sounds/randyboycumming.mp3"
$ renpy.pause(1.0, hard=True)
rc"That's it, you've seen enough, we're far from done but this is our special arse time now."
rb "Oh yeah, I'm gonna stretch that arse nice and good, let me just finish unloading and I'll stay rock-hard for you! Hope you learnt a thing or two buddy, now leave us alone."
return

label Sex42:
stop music
$ vivianepussyx = False
$ vivianeblowx = False
$ vivianeanalx = False
scene vivianefuck01
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

label VivianeFuckChoiceDay05x:
scene vivianechoice with dissolve
$ renpy.pause(1.0, hard=True)
vi "So... What are you going to do to me now [name]?"
menu:
    "I want to take you up the arse and work my hip muscles!" if (vivianeanalx == False):
        vi "Great idea! They really help improve the speed of your legs underwater..."
        jump VivianeAnalDay05x
    "I'll hold you up while I pummel my great pile-driver in your mouth!" if (vivianeblowx == False):
        vi "Mmh, that sounds so hot! Lift me up in your muscular arms and lick my pussy!"
        jump VivianeBlowDay05x
    "Let's get on the floor so you can ride my huge dong!" if (vivianepussyx == False):
        vi "So I'll be doing all the work? I guess you deserve it STUD!"
        jump VivianePussyDay05x
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (vivianepussyx == True) and (vivianeblowx == True) and (vivianeanalx == True):
        vi "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump VivianeMovieDay05x

label VivianeAnalDay05x:
$ vivianeanalx = True
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
vi "FUCK! YOu're sssooo BIG! I feel like I'm getting impaled on a giant spike!"
p "Hang on in there, I'm gonna spike your arse some more..."
scene vivianeanal02 with dissolve
$ renpy.pause(0.3, hard=True)
vi "YES! Fuck my arse [name]! FUCK ME HARD!"
label VivianeAnalDay05bx:
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
        jump VivianeAnalDay05bx
    "Move on":
        pass
scene vivianeanal03 with dissolve
$ renpy.pause(1.0, hard=True)
vi "My God, it feels like my arse is nothing more than a gaping hole now..."
p "It sure looks like it from where I'm standing..." 
jump VivianeFuckChoiceDay05x

label VivianeBlowDay05x:
$ vivianeblowx = True
scene vivianeoral01 with dissolve
play sound "Sounds/vivianeblow01.mp3"
$ renpy.pause(10.0, hard=True)
vi "Mmh, you're so strong holding me like that!"
p "That's cos I need to lick that tasty pussy of yours!"
vi "While I suck on that giant shaft of yours! It's a deal!"
label VivianeBlowDay05bx:
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
        jump VivianeBlowDay05bx
    "Move on":
        pass    
vi "I think I dislocated my jaw..."
p "It happens...Let's move on to something else." 
jump VivianeFuckChoiceDay05x    

label VivianePussyDay05x:
$ vivianepussyx = True
scene vivianecowgirl01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Keep steady mustang! This cowgirl is going to ride you into submission!"
p "Oh fuck, I think I'm in for a wild ride!" 
label VivianePussyDay05bx:
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
        jump VivianePussyDay05bx
    "Move on":
        pass    
vi "How was it for you stallion?"
p "Damn, I feel like I rode all the way to California..." 
jump VivianeFuckChoiceDay05x   

label VivianeMovieDay05x:
scene vivianeprefuck with dissolve
p "I've pinned you down against the lockers... Time to smash the padlock on your uterus with my sledgehammer!"
vi "OOOh, you have the worse lines [name], but I forgive you because you're about to give me what I want, that fat young bullcock of yours! FUCK ME!"
play music "Sounds/vivianefuck.mp3"
show vivianefuck
show cum
call screen vivianefuckday05x
screen vivianefuckday05x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("VivianeFuckCumDay05x")

label VivianeFuckCumDay05x:
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
vi "Now kiss me stud! And come with me in the showers so we can get cleaned up!"
scene vivianecum04 with dissolve
play music "Sounds/shower.mp3"
$ renpy.pause(1.0, hard=True)
vi "Mmh, I love your body... And that MONSTERCOCK! Can you get hard again and fuck me?"
p "Sure I could, but I'm afraid I have to go Viviane. You know, training and getting ready for the swimming competition..."
vi "I understand stud... I wouldn't want to drain all your energy this week! (wink)"
stop music
return

label Sex43:
stop music
$ mariablow05x = False
$ mariastandingx = False
$ mariapussy05x = False
scene mariapre01
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
    
label MariaFuckChoiceDay05x:
scene mariapre05 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Well, that's all good... But what are you going to do now STUD?"
menu:
    "Your pussy looks so tasty... I wanna have a scoop. Or two scoops, cos I'm bigly the best!" if (mariapussy05x == False):
        ma "Right, as long as you don't pretend to be an orang-utan..."            
        jump MariaPussyDay05x
    "I'm gonna show how strong I am! Get ready for lift-off!" if (mariastandingx == False):
        ma "Ooh, yes, I've also noticed your giant MUSCLES..."            
        jump MariaStandingDay05x
    "Let's make sweet love on the floor." if (mariablow05x == False):
        ma "Good thing the floor was cleaned this morning by Willie then..."            
        jump MariaBlowDay05x
    "I want to fuck that tender pussy of yours till I blow my load!" if (mariablow05x == True) and (mariastandingx == True) and (mariapussy05x == True):
        jump MariaMovieDay05x

label MariaPussyDay05x:
$ mariapussy05x = True
scene mariapussylick with dissolve
play sound "Sounds/mariapussylick01.mp3"
$ renpy.pause(6.0, hard=True)
ma "Does my pussy taste good? Mmmh, I can feel your balls tightening already, they feel so heavy..."            
p "Get on the desk, I'm really going to dive into the abyss this time!"
scene mariadesk01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Are you good with tongue-twisters Maria?"
ma "Mmh, I don't know, but I bet YOU are! Show me STUD!"
label MariaPussyLickDay05bx:
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
        jump MariaPussyLickDay05bx
    "Move on":
        pass
ma "I'll give you a stellar report for your work [name]..."
p "Alright! Let me show something else then..."
jump MariaFuckChoiceDay05x

label MariaStandingDay05x:
$ mariastandingx = True
scene mariastanding01 with dissolve
play sound "Sounds/mariastanding01.mp3"
$ renpy.pause(12.0, hard=True)
ma "Ooh, I love it in that position, your massive tool gets so deep! AAAH! Yes, plunge it as far it will go!"
scene mariastanding02 with dissolve
$ renpy.pause(1.0, hard=True)
ma "Ouch, let me adjust my pussy... to this giant... intruder... Yeah, that's better now..."
label MariaStandingDay05bx:
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
        jump MariaStandingDay05bx
    "Move on":
        pass    
ma "Damn boy, you really know how to ful-FILL a woman's deepest desires!"
p "Yep, that's me, the biggest stud on the island! Let me show something else now."
jump MariaFuckChoiceDay05x    

label MariaBlowDay05x:
$ mariablow05x = True
scene mariasuckb01 with dissolve
play sound "Sounds/mariapreblow.mp3"
$ renpy.pause(9.0, hard=True)
ma "Oh my, what do ye have here? That's the biggest cock I've ever seen, it's gonna take me forever to lick... all the way to the tip ..."
p "Take your time... But not too long!"
scene mariasuckb02 with dissolve
$ renpy.pause(1.0, hard=True)
ma "I'm sure you... gggllr... prefer to have my... warm mouth... mmmh... around it..."
p "Damn, you've got the whole apple-sized head in already!"
scene mariasuckb03 with dissolve
$ renpy.pause(1.0, hard=True)
label MariaBlowDay05bx:
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
        jump MariaBlowDay05bx
    "Move on":
        pass    
scene mariasuckb01 with dissolve
$ renpy.pause(1.0, hard=True)
ma "I think your cock liked that... It's twitching in my hands..."
p "WOW! Is all I can say. And let's do something else too." 
jump MariaFuckChoiceDay05x    

label MariaMovieDay05x:
ma "I'm ready to get impaled by your huge dong and plastered in cum [name]!"
p "Well, that's good, cos it's exactly what's going to happen." 
play music "Sounds/mariafuckslow02.mp3"
show mariafuckslow02
show faster
call screen mariafuckslow02day05x
screen mariafuckslow02day05x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MariaFastFuckDay05x")

label MariaFastFuckDay05x:
stop music
hide faster
play music "Sounds/mariafuckfast02.mp3"
show mariafuckfast02
show cum
call screen mariafuckfast02day05x
screen mariafuckfast02day05x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("MariaCumDay05x")

label MariaCumDay05x:
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
return

label Sex44:
stop music
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
p "Yeah, I'll show you, I'm da man, I'm DA MAN!"
do "Good, I like your spirits! We'll start with an easy weight, just 100 pounds..."
scene randydoris05 with dissolve
do "Now flex that mighty rock-hard dong and lift up the weight with it..."
play sound "Sounds/workoutgroan.mp3"
$ renpy.pause(1.0, hard=True)
scene randydoris06 with dissolve
play sound "Sounds/workoutgroan.mp3"
do "Now keep it flexed and hold it..."
do "Hold it... Good. Well done, we can try a heavier weight now."
play sound "Sounds/panting.mp3"
$ renpy.pause(1.0, hard=True)
p "Fuck yeah, let's try 200 pounds"
do "Oooh, nice, that's a LOT... I wanna see that..."
show randydoris07
play sound "Sounds/workoutgroan.mp3"
do "Now keep it flexed and hold it..."
scene randydoris06b
show randydoris07b
p "Ah... Shit, can't hold it..."
do "Well, you still managed to hold it for a while... So train some more and I think you might get there boy!"
return

label Sex45:
stop music
scene gymdaniella02
$ renpy.pause(1.0, hard=True)
da "Hello there, do you need any help with our wonderful state-of-the-art equipment?"
p "I was wondering, how do I join the \"Muscle Stud Competition\"?"
scene gymdaniella03 with dissolve
$ renpy.pause(1.0, hard=True)
da "You just turn up on Saturday at 2pm."
da "But are you sure you want to do that? It's very competitive, and you might get humiliated..."
p "Me, humiliated? No way, I'll win for sure!"
scene gymdaniella04 with dissolve
$ renpy.pause(1.0, hard=True)
da "Let me be the judge of that... I'm gonna check how well you're faring so far..."
da "Take your shirt off and get on that machine over there in the corner..."
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
da "And from the looks of things, you get teased quite easily... YOu'd better work on that kiddo..."
da "But I'll allow you into the competition, you sure are strong enough for it..."
da "And you also seem to have a great big whopper of a cock... Mmmh..."
return

label Sex46:
stop music
$ francinegroundx = False
$ francinedoggyx = False
$ francineblowx = False
scene francinepole04
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
p "You turn pole-dancing into an art!"
fa "Well, it IS an art actually..."
p "Of course, but you elevate it to something subliminal... Since your body is a work of art itself..."
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
label FrancineFuckChoiceDay05x:
scene francineprefuck with dissolve
$ renpy.pause(1.0, hard=True)
fa "I'm ready when you are!"
menu:
    "Well, I'm ready to facefuck your mouth then! Get on your knees." if (francineblowx == False):
        fa "I hope my mouth can stretch enough to take on THAT monster..."
        jump FrancineBlowDay05x
    "Hold on to the pole, I'm gonna fuck you from behind!" if (francinedoggyx == False):
        fa  "Ooh, I LOVE that idea!"
        jump FrancineDoggyDay05x
    "Let's make sweet love on the floor." if (francinegroundx == False):
        fa "I hope not TOO sweet... My pussy wants a good pounding (wink)."
        p "Yeah, don't worry about it, just get on board for starters..."
        jump FrancineGroundDay05x
    "I'm ready to blow anytime now, do something Francine!" if (francineblowx == True) and (francinedoggyx == True) and (francinegroundx == True):
        fa  "I know exactly what to do... Double-handed monstercock handjob it is!"
        jump FrancineMovieDay05x

label FrancineBlowDay05x:
$ francineblowx = True
scene francineblow01 with dissolve
play sound "Sounds/francinefuck02.mp3"
$ renpy.pause(3.0, hard=True)
p "Easy...Open wide..."
fa "Mmmm, ggglll..."
scene francineblow02 with dissolve
$ renpy.pause(1.0, hard=True)
p "And your throat now... Wider, wider! Aah, this feels good!"
label FrancineBlowDay05bx:
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
        jump FrancineBlowDay05bx
    "Move on":
        pass
fa "Gaaa gaaa, I think... my jaw... is dislocated..."
p "Never mind that, it will get back to normal soon, let's switch position!"
jump FrancineFuckChoiceDay05x

label FrancineDoggyDay05x:
$ francinedoggyx = True
scene francinefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
fa "Oh fuck, FUCK! Give it to me [name]"
p "No problemo. Get ready, set, GO!"
scene francinefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
fa "AAAOUUW, FUCK it hurts! But it's so good! Do it again, please!"
label FrancineDoggyDay05bx:
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
        jump FrancineDoggyDay05bx
    "Move on":
        pass    
fa "That was the best pole-dancing workout I ever got!"
p "My pole sure did give you a workout! Let's do something else now."
jump FrancineFuckChoiceDay05x   

label FrancineGroundDay05x:
$ francinegroundx = True
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
label FrancineGroundbDay05bx:
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
        jump FrancineGroundbDay05bx
    "Move on":
        pass    
fa "My pussy is creaming all over the place..."
p "My cock needs a good cleaning then, let's think of another position shall we?" 
jump FrancineFuckChoiceDay05x    

label FrancineMovieDay05x:
fa "You'll see, my hands will milk a huge load straight out of that cum-cannon!"
play music "Sounds/francinefuckmovie.mp3"
show francinefuckslow
show faster
call screen francineslowfuckday05x
screen francineslowfuckday05x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FrancineFastFuckDay05x")

label FrancineFastFuckDay05x:
stop music
hide faster
play music "Sounds/francinefuckmovie.mp3"
show francinefuckfast
show cum
call screen francinefastfuckday05x
screen francinefastfuckday05x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("FrancineCumDay05x")

label FrancineCumDay05x:
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
fa "I'm always happy to lend a hand... Now, le'ts get cleaned up before someone else arrives..."
return

label Sex47:
stop music
scene gymboy01
$ renpy.pause(1.0, hard=True)
p "What is going on here? Looks like a young horse-hung muscle stud being serviced by a couple of dykes..."
scene gymboy02 with dissolve
$ renpy.pause(1.0, hard=True)
rb "Came to watch how a real stud fucks again?"

p "And what if I told your girlfriend you fuck behind her back all the time?"
rb "She knows and she doesn't care. I give it to her a dozen times a day and then she can't take it anymore."
rb "She understands I need to unload my bloated nuts some more every day...."
p "(Damn, it does look like this guy is serious competition... I hope he's not going to enter the Muscle Stud challenge.)"
rb "And anyway, this is part of my training to retain my title as Muscle Stud saturday."
rb "I heard you might be competing too, although you have no chance against me, I've been winning this competition three years in a row already!"
p "Well, you're about to lose your crown dumbass!"
l01 "Why don't you shut the hell up and make yourself useful by fisting me, I need to have my pussy loosened up for this young stud's monstercock!"
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
label GymBoy03Day05bx:
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
        jump GymBoy03Day05bx
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
        jump GymBoy04Day05x

label GymBoy04Day05x:
scene gymboy04 with dissolve    
$ renpy.pause(1.0, hard=True)
p "Hey, what about you, how about you give me a blowjob or something?"
scene gymboy04b with dissolve    
$ renpy.pause(1.0, hard=True)
l02 "How about you go fuck yourself? I'm busy gulping down the huge amount of nutjuice this super-stud plastered me with, I have no time for you boy!"
l01 "Oh damn, daddy! Your thingie is so massive! I'm gonna cum in no time! AAAAH!"
rb "There's more where that came from!"
label GymBoy04Day05bx:
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
        jump GymBoy04Day05bx
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
        return

label Sex48:
stop music
$ teaganpussyx = False
$ teaganfeetx = False
$ teagananalday05x = False
scene teagan01day05
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
p "Sure, thanks for the offer Ms Cocque!"
scene teagan03day05 with dissolve
$ renpy.pause(1.0, hard=True)
p "I can see her ogling my bulge... Good thing I got a semi while admiring her, it must look even bigger than usual..."
t "Wow... [name], you really have an incredible body for such a young boy..."
p "And you have an incredible body too Ms Cocque for...err... a schoolteacher."
t "Come into the pool clumsy boy. I'll let you get a closer look at it if you like it so much..."
scene teagan04day05 with dissolve
$ renpy.pause(1.0, hard=True)
t "You know, it's highly inappropriate for a teacher to be spending time like this with a student..."
t "So let's just pretend you are only my delivery boy today... and not a boy in the class I teach."
p "Sure Ms Cocque, I don't mind role-playing!"
t "So... What do you have for me Mr grocery boy? (wink)"

p "I do pick-ups and deliveries. Right now, I'm picking you up..."        
t "Ooh? And when will the delivery be?"
scene teagan05day05 with dissolve
$ renpy.pause(1.0, hard=True)
p "In a while... I first need to unpack those heavy bags..."
t "You like them don't you... And I KNOW you liked fucking them with your huge, young, hard COCK!"
p "What can I say, I can't resist such lovely MILF knockers..."
t "Let's move out of the pool, I want to see that monstercock of yours again!"
label TeaganFuckChoiceDay05x:
stop music
scene teaganchoiceday05 with dissolve
$ renpy.pause(1.0, hard=True)
t "So, now that you are here, proudly displaying your gigantic erection to your schoolteacher, what would you like us to do [name]?"
menu:
    "I think anal is in order. Yes, anal." if (teagananalday05x == False):
        t "That massive fuckstick up my arse? You can't be serious..."
        p "I am serious and I'll prove it!"        
        jump TeaganAnalDay05x
    "My studcock is sore from so much fucking. It needs a nice foot massage." if (teaganfeetx == False):
        t "Mmh, you're a footboy are you? Then get ready for the best footjob in town stud!"
        jump TeaganFeetDay05x
    "Get in the lounge chair, I'm gonna pound that sweet teacher pussy of yours!" if (teaganpussyx == False):
        t "It's ready to receive your massive teenage pussy-pleaser!"
        jump TeaganPussyDay05x
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (teaganpussyx == True) and (teaganfeetx == True) and (teagananalday05x == True):
        t "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump TeaganMovieDay05x

label TeaganAnalDay05x:
$ teagananalday05x = True
scene teagananal01 with dissolve
$ renpy.pause(1.0, hard=True)
p "How do you like your student's cock up your your fuckhole teach?"
t "I'm such a dirty slut... Pound me with your massive fuckstick I beg you!"
scene teagananal02 with dissolve
$ renpy.pause(1.0, hard=True)
t "AAAH, it's so fucking deep!"
label TeaganAnalDay05bx:
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
        jump TeaganAnalDay05bx
    "Move on":
        t "Have mercy on my poor arse [name]!"
        p "Ok Teagan, I'll give you a respite. FOR NOW."
        jump TeaganFuckChoiceDay05x

label TeaganFeetDay05x:
$ teaganfeetx = True
scene teaganfeet01 with dissolve
$ renpy.pause(1.0, hard=True)
t "Ready? Cos my feet are going to make your dick extra-hard and extra-HUGE, guaranteed!"
p "Let's see if you're better than Sophia then shall we?"
t "Oh? A competition with the principal? I'm in!"
label TeaganFeetDay05bx:
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
        jump TeaganFeetDay05bx
    "Move on":
        pass    
t "Ooh, look at all that precum flowing from your tip...You're ready to pop aren't you? So, was it better than Sophia's footjobs?"
p "Y...Yes... So it's best if we move on to something else." 
jump TeaganFuckChoiceDay05x    

label TeaganPussyDay05x:
$ teaganpussyx = True
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
label TeaganPussyDay05bx:
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
        jump TeaganPussyDay05bx
    "Move on":
        jump TeaganFuckChoiceDay05x    

label TeaganMovieDay05x:
scene teaganfuckmovieday05 with dissolve
p "Bounce up and down on my dong teach! I want to be buried balls-deep inside you!"
t "OOOh, I don't know if I can take that much cock [name], but I sure as hell will try!"
play music "Sounds/teaganfuckslow02.mp3"
show teaganfuckslow02
show faster
call screen teaganfuckslowday05x
screen teaganfuckslowday05x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TeaganFuckFastDay05x")

label TeaganFuckFastDay05x:
stop music
hide faster
play music "Sounds/teaganfuckfast02.mp3"
show teaganfuckfast02
show cum
call screen teaganfuckfastday05x
screen teaganfuckfastday05x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("TeaganFuckCumDay05x")

label TeaganFuckCumDay05x:
hide teaganfuckslow02
hide teaganfuckfast02
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
t "Jeezus! How long ago was it that you busted a nut [name]? You came sssooo much!"
p "Not that long ago Teagan... I just replenish my balls super-fast..."
t "Wow, that's incredible... A true alpha teen-stud!"
t "While I would love to have another go on that still rock-hard donkey-dick of yours, I have a faculty appointment with Principal Titsworthy I can't miss..."
t "So off you go, I'll see you tomorrow and don't say a word about this to anyone [name]!"
p "What about some money for bringing your groceries?"
t "You're kidding right? Tell me you're kidding..."
p "Err.. I guess so..."
return

label Sex49:
stop music
scene annaroom01
$ renpy.pause(1.0, hard=True)
an "Who is that? Oh, it's you..."
an "I was expecting you... Come in, naughty boy."
$ annablowx = False
$ annacrankx = False
$ annatitsx = False
$ annabedx = False
scene annaroom02 with dissolve
$ renpy.pause(1.0, hard=True)
an "Let me first get more comfortable by getting rid of this bathrobe. So you can admire my curves..."
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
label AnnaFuckChoiceDay05x:
menu:
    "Let me lift you up on my crank!" if (annacrankx == False):
        jump AnnaCrankDay05x
    "How about giving me a nice blowjob?" if (annablowx == False):
        jump AnnaBlowDay05x
    "Your boobs seem ideal for a titfuck..." if (annatitsx == False):
        jump AnnaTitfuckDay05x
    "Let's get on the bed and fuck like wild animals!" if (annabedx == False):
        jump AnnaBedDay05x
    "I need to get my rocks off SOON! In YOUR ARSE!" if (annacrankx == True) and (annablowx == True) and (annatitsx == True) and (annabedx == True):
        an "WHat? But... You're way too big for that! On the other hand, you're my guest so I'll let you do it, naughty boy!"
        jump AnnaMovieDay05x

label AnnaCrankDay05x:
$ annacrankx = True
scene annaroom11 with dissolve
play sound "Sounds/annacrank01.mp3"
$ renpy.pause(4.0, hard=True)
an "Mmh, I like how POWERFUL that giant tool feels! Please IMPALE me on it [name]!"
scene annaroom12b with dissolve
$ renpy.pause(1.0, hard=True)
an "OOOH, FUCK! It's so fucking thick and DEEP!"
p "Hang on, I'll drill even deeper!"
label AnnaCrankDay05bx:
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
        an "Ooh, yes please, STUD! YOu go way DEEPER than my son too!"
        jump AnnaCrankDay05bx
    "Move on":
        p "That was a nice workout. Let's do something else..."
        an "The best workout my fuckhole ever got... Phew... What would you like to do next [name]?"        
        jump AnnaFuckChoiceDay05x

label AnnaBlowDay05x:
$ annablowx = True
scene annaroom13 with dissolve
play sound "Sounds/annablow01.mp3"
$ renpy.pause(7.0, hard=True)
an "Let me lick it first... God, it's so fucking big and beautiful!"
label AnnaBlowDay05bx:
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
        an "Of course, your massive cock tastes so good. There's way more precum flowing from it than José..."
        jump AnnaBlowDay05bx
    "Move on":
        scene annaroom13 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "That's good, now my cock is nice and shiny with your spit..."
        an "I was choking on it, it's so massive!"
        jump AnnaFuckChoiceDay05x

label AnnaTitfuckDay05x:
$ annatitsx = True
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
label AnnaTitfuckDay05bx:
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
        an "And your horsecock feels so good pummelling between them...More so than my son..."       
        jump AnnaTitfuckDay05bx
    "Move on":
        p "I've creamed my precum all over your tits, so that's marked, let's do something else!"
        jump AnnaFuckChoiceDay05x

label AnnaBedDay05x:
$ annabedx = True
scene annaroom08 with dissolve
play sound "Sounds/annabed01.mp3"
$ renpy.pause(5.0, hard=True)
an "Mmh, I can't wait to feel this big dick in my tight little pussy..."
scene annaroom08b with dissolve
$ renpy.pause(1.0, hard=True)
an "AAh, you're stretching me wide open!"
label AnnaBedDay05bx:
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
        an "Ooh, yes please! You fuck me so much better than my son I have to admit..."    
        jump AnnaBedDay05bx
    "Move on":
        p "Let's do something else!"
        jump AnnaFuckChoiceDay05x


label AnnaMovieDay05x:
scene annafuckmovie with dissolve
p "As I said, I'll finish off by ramming my pole up your tight arse!"
an "I'm ready, just be gentle will you? No one has ever gone up my backside before... Even my ex-husband."
p "Cool, I'll take your arse virginity then!"
play music "Sounds/annafuckslow.mp3"
show annafuckslow
show faster
call screen annaslowfuckday05x
screen annaslowfuckday05x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("AnnaFastFuckDay05x")

label AnnaFastFuckDay05x:
stop music
hide faster
play music "Sounds/annafuckfast.mp3"
show annafuckfast
show cum
call screen annafastfuckday05x
screen annafastfuckday05x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("AnnaCumDay05x")

label AnnaCumDay05x:
hide annafuckslow
hide annafuckfast
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
an "Damn, you're cumming so much! Way more sperm than my son! Yes, give it to me [name]!"
$ renpy.pause(2.0, hard=True)
scene annacum03 with dissolve
play sound "Sounds/cumming.mp3" 
$ renpy.pause(1.0, hard=True)
p "Damn! That was an intense orgasm! Phew!"
return

label Sex50:
stop music
$ jenniferanalx = False
$ jenniferpussyx = False
$ jenniferdoggyx = False
scene insemination01
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
ra "I'll show you how to get the best out of that huge dick. By having a go on it myself for a while..."
je "Don't make him cum, his sperm belongs to me!"
ra "Don't worry Mrs Anonymous. I know how to control my pussy muscles to bring men to the edge and maintain them there..."
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
ra "Well, you wanted a huge load of virile, he's a stud who can deliver just that. Who cares he's a student of yours, no one will ever know."
je "But... It's so wrong!"
ra "I think you can come out now [name]: Show Jennifer your full muscled body to convince her, she's already horny as hell."
je "Well... Yes, actually, my pussy is soaking wet but.."
scene insemination10g
$ renpy.pause(1.0, hard=True)
ra "Now look at him! You want a physically-superior baby? His seed will give you one Jennifer..."
p "Come on, I'll be gentle and I won't tell anyone, I promise!"
je "You'd better... I can't let my husband know I sucked off a student..."
je "OK, fuck me [name]! Fill me with your nasty teenage cum, I don't care anymore, I'm too horny!"
ra "That's my girl.."

label JenniferFuckChoiceDay05x:
scene insemination13 with dissolve
$ renpy.pause(1.0, hard=True)
je "Get on with it, I need your sweet cum!"
menu:
    "Get on your back, I'll drill you slowly to stretch your fuckhole!" if (jenniferpussyx == False):
        je "Yes, I think that's in order. Since you're so big..."
        jump JenniferPussyDay05x
    "Spread those legs, I'm gonna pound you from behind!" if (jenniferdoggyx == False):
        je  "Of course, pummel me like a ragdoll [name]!"
        jump JenniferDoggyDay05x
    "Yeah, OK, but I want your sweet arse!" if (jenniferanalx == False):
        je "What? But you can't impregnate me that way!"
        p "It's to get my cock really hard and ready to explode in your other hole. Come on, you know you want it!"
        je "I definitely DON'T want it, but if it's for a good cause..."
        jump JenniferAnalDay05x
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (jenniferpussyx == True) and (jenniferdoggyx == True) and (jenniferanalx == True):
        je  "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump JenniferMovieDay05x

label JenniferPussyDay05x:
$ jenniferpussyx = True
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
label JenniferPussyDay05bx:
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
        jump JenniferPussyDay05bx
    "Move on":
        pass
je "Now I'm totally stretched out!"
ra "I can see that, your hole is gaping wide open Jennifer!"
p "Good, so we can move on to another position then..."
jump JenniferFuckChoiceDay05x

label JenniferDoggyDay05x:
$ jenniferdoggyx = True
scene insemination12 with dissolve
play sound "Sounds/jennifer02.mp3"
$ renpy.pause(12.0, hard=True)
je "Oh God, oh God! I'm gonna take the biggest fattest cock I've ever seen! I'm dripping wet, shove it in [name] I beg you!"
p "Sure, Here I come, ten inches in one swift go!"
scene insemination12b with dissolve
$ renpy.pause(1.0, hard=True)
je "Damn it, you're so fucking deep!"
label JenniferDoggyDay05bx:
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
        jump JenniferDoggyDay05bx
    "Move on":
        pass    
je "I feel like a hog on a spitfire!"
p "My dick sure took some heat, I'm red-hot and ready for more action!"
jump JenniferFuckChoiceDay05x    

label JenniferAnalDay05x:
$ jenniferanalx = True
scene insemination18 with dissolve
$ renpy.pause(1.0, hard=True)
ra "Show the naysayers that a woman is also perfectly capable of taking well over a foot of fat hosepipe up her backside [name]!"
je "What? No, please, show instead some restraint when you plunge that massive pole int....!"
scene insemination18b with dissolve
play sound "Sounds/jenniferanal01.mp3"
$ renpy.pause(1.0, hard=True)
je "... MEEEE! FUCK! AAAH!"
label JenniferAnalDay05bx:
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
        jump JenniferAnalDay05bx
    "Move on":
        pass    
je "Thank God you didn't waste your virile spunk in that hole..."
p "I know where to aim... Let me show you." 
jump JenniferFuckChoiceDay05x    

label JenniferMovieDay05x:
scene insemination14 with dissolve
p "Ok, you want my sperm Jennifer? I want to hear you SAY IT!"
je "YES! Breed me [name], I want to have your baby!"
play music "Sounds/jenniferfuckslow.mp3"
show jenniferslowfuck
show faster
call screen jenniferslowfuckday05x
screen jenniferslowfuckday05x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("JenniferFastFuckDay05x")

label JenniferFastFuckDay05x:
stop music
hide faster
play music "Sounds/jenniferfuckfast.mp3"
show jenniferfastfuck
show cum
call screen jenniferfastfuckday05x
screen jenniferfastfuckday05x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("JenniferCumDay05x")

label JenniferCumDay05x:
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
ra "I'd better go and collect all that virile spunk into a jar for Dr.Stains before it goes off... I'll leave you two lovebirds to it."
p "(Shit, I didn't have time to take a pic of her!)"
scene insemination20a with dissolve
$ renpy.pause(1.0, hard=True)
p "(Jennifer looks so fulfilled and contented. I wonder what she's thinking about right now...)"
scene insemination20b with dissolve
play sound "Sounds/dreaming.mp3"
$ renpy.pause(1.0, hard=True)
je "Can you feel the baby kicking inside me honey? He seems to be so vigorous already!"
scene insemination20c with dissolve
$ renpy.pause(1.0, hard=True)
je "Ooh, there he goes again, giving great big kicks with his tiny feet... So cute!"
p "I should get cleaned up and leave this hall of utter depravity..."
return

label Sex52:
stop music
scene classroomday05
menu:
    "Daydream about Brittany":
        jump DayDreamBritDay06x
    "Daydream about Chantelle":
        jump DayDreamChantelleDay06x
    "Daydream about Kate":
        jump DayDreamKateDay06x
    "Daydream about Sophia":
        jump DayDreamSophiaDay05x
    "Daydream about Viviane":
        jump DayDreamVivianeDay05x
    "Daydream about Maria":
        jump DayDreamMariaDay05x

label DayDreamSophiaDay05x:
play sound "Sounds/dreaming.mp3"
scene dreamsophia01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
so "There's only thing you can do to stop me from expelling you from this school [name]..."
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
return

label DayDreamVivianeDay05x:
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
return

label DayDreamMariaDay05x:
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
return

label DayDreamBritDay06x:
play sound "Sounds/dreaming.mp3"
scene dreambrit01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
br "Court Stud [name]! Your Queen needs servicing..."
p "I'm at full mast your Divine Majesty..."
scene dreambrit02 with dissolve
$ renpy.pause(3.0, hard=True)
br "Bring that cum cannon over to my quarters to defend your Goddess!"
p "And my love sword, don't forget my love sword your Beautiful Perfectiveness..."
scene dreambrit03 with dissolve
$ renpy.pause(3.0, hard=True)
br "How could I? It's the BIGGEST in the Realm... It makes your queen so wet..."
p "That's right. The Court Stud is coming thr..."
stop music
scene lesson01 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
p "Not AGAIN! Right in the middle of my stride!"
return

label DayDreamChantelleDay06x:
play sound "Sounds/dreaming.mp3"
scene dreamchantelle01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
ch "I really shouldn't do what I'm doing [name]. You're my best friend's brother..."
p "Yeah, So? She'll never know."
scene dreamchantelle02 with dissolve
$ renpy.pause(3.0, hard=True)
ch "You won't tell her? You won't tell her I'm so horny for her little brother?"
p "I swear. On my oversensitive glans."
scene dreamchantelle03 with dissolve
$ renpy.pause(3.0, hard=True)
ch "Then COME and FUCK ME! I want IT, I NEED IT I BEG YOU!"
p "Happy to oblige Chantelle... Open w..."
stop music
scene lesson01 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
p "AAARGH! When will I ever get to score in my head in this game???"
return

label DayDreamKateDay06x:
play sound "Sounds/dreaming.mp3"
scene dreamkate01 with dissolve
$ renpy.pause(2.0, hard=True)
play music "Sounds/teacherstrip.mp3"
$ renpy.pause(2.0, hard=True)
k "OOh, [name]! Are you here to help me decide on a bikini for tonight?"
p "Yeah! Show me and my cock will decide..."
scene dreamkate02 with dissolve
$ renpy.pause(3.0, hard=True)
k "Would it be a good idea if I showed my big boobies on stage?"
p "A damn good idea Kate, a damn good idea..."
scene dreamkate03 with dissolve
$ renpy.pause(3.0, hard=True)
k "What if I stretched my pink pussylips like that so you could come and fuck me in front of everyone?"
p "I would be up there in a seco..."
stop music
scene lesson01 with dissolve
play sound "Sounds/schoolrecess.mp3"
$ renpy.pause(1.0, hard=True)
p "DAMN IT! I'll do it for REAL tonight, I swear to God!"
return

label Sex53:
stop music
$ pameladoggyx = False
$ pamelastandx = False
$ pamelaanalx = False
$ pamelablowx = False
scene pamelaprefuck02
$ renpy.pause(1.0, hard=True)
pa "I'm totally naked and dripping wet, come and get me stud!"
p "I would cross water, big water, like ocean water to get you Pamela! And this island is surrounded by it too!"
scene pamelaprefuck03 with dissolve
play sound "Sounds/pamela01.mp3"
$ renpy.pause(3.0, hard=True)
pa "Mmmh, your cock is just as HUGE as that kid we saw! What do they feed you boys?"
p "I don't know but what I can feed YOU are 18 inches of prime beef right there...."
pa "And what should we do with this thing and my dripping wet pussy?"
label PamelaFuckChoiceDay06x:
menu:
    "I need to see that scrumptious arse of yours while I fuck you!" if (pameladoggyx == False):
        pa "I'm guessing doggy then, right?"
        p "Correct answer. You've just won... 18 inches of boymeat up your twat!"
        jump PamelaDoggyDay06x
    "Let's fuck in the water!" if (pamelastandx == False):
        pa "What? That sounds dangerous.... but so adventurous too, I'm in!"
        jump PamelaStandDay06x
    "There's a cave that still needs exploring..." if (pamelaanalx == False):
        pa "Wh... What do you mean?"
        p "I mean, I'm going to bang your backside!"        
        jump PamelaAnalDay06x
    "Why don't you kneel in front of my giant prong and worship it?" if (pamelablowx == False):
        pa "It certainly is big enough to warrant worshipping!"
        jump PamelaBlowDay06x
    "Let me lift you up on my shaft for the grand finale..." if (pamelastandx == True) and (pameladoggyx == True) and (pamelaanalx == True) and (pamelablowx == True):
        jump PamelaMovieDay06x

label PamelaDoggyDay06x:
$ pameladoggyx = True
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
label PamelaDoggyDay06bx:
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
        jump PamelaDoggyDay06bx
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaFuckChoiceDay06x

label PamelaStandDay06x:
$ pamelastandx = True
scene pamelastand01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Just the tip of your monster cock is already filling me up like never before!"
p "Wait till you get another fifteen inches of it..."
label PamelaStandDay06bx:
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
        jump PamelaStandDay06x
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaFuckChoiceDay06x

label PamelaAnalDay06x:
$ pamelaanalx = True
scene pamanal01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "I don't know... It doesn't look your mammoth dong could possibly fit inside my tiny backdoor..."
p "We'll soon find out..."
pa "My God, those balls are so FULL! And that shaft is so THICK!"
scene pamanal02 with dissolve
$ renpy.pause(1.0, hard=True)
p "See, it fits..."
pa "OK, then pile-drive into me and show me how you really fuck an arse stud!"
label PamelaAnalDay06bx:
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
        jump PamelaAnalDay06bx
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaFuckChoiceDay06x

label PamelaBlowDay06x:
$ pamelablowx = True
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
label PamelaBlowDay06bx:
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
        jump PamelaBlowDay06bx
    "Move on":
        p "Time out... Until the next position."
        scene pamelaprefuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        pa "And what do you have in mind for the next position [name]?"        
        jump PamelaFuckChoiceDay06x

label PamelaMovieDay06x:
scene pamelafuckmovie with dissolve
$ renpy.pause(1.0, hard=True)
p "Yeah, grind your pussy on my shaft and get it nice and wet..."
pa "I'm ready... FUCK ME!"
play music "Sounds/pamelafuckslow.mp3"
show pamfuckslow
show faster
call screen pamfuckslowday06x
screen pamfuckslowday06x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PamelaFuckFastDay06x")

label PamelaFuckFastDay06x:
stop music
hide faster
play music "Sounds/pamelafuckfast.mp3"
show pamfuckfast
show cum
call screen pamfuckfastday06x
screen pamfuckfastday06x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PamelaCumDay06x")

label PamelaCumDay06x:
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
p "Then lie down and I'll plaster your body of the rest of my load!"
scene pamelacum03 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "Fuck, it's blasting non-stop! RHAAA!"
pa "Yes, cover me in your thick spunk [name]!"
pa "Incredible, you totally covered my body on your heavy dose..."
p "Yep, I told you i was a STUD, even better than that boy we saw earlier..."
pa "We should head back to the beach... Mitch might get worried and send a party for us..."
scene pamelasea01 with dissolve
play music "Sounds/boatengine.mp3"
$ renpy.pause(1.0, hard=True)
pa "And try to wipe that smirk off your face [name]... I don't want Mitch being jealous and all..."
p "Alright, I'll try..."
return

label Sex54:
stop music
play music "Sounds/pageantbikini.mp3"
scene chantelleprep01
$ renpy.pause(1.0, hard=True)
p "Oh, there's Chantelle doing some turns in a tiny bikini and oiled-up body.... HOT!"
scene chantelleprep01a with dissolve
$ renpy.pause(1.0, hard=True)
p "Oh yeah, look at that hot arse..."
scene chantelleprep03 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Oh, it's naughty you again, bargin on me while I'm preparing for the pageant..."
p "Err... I came to use the gym, sorry, didn't want to bother me."
scene chantelleprep05 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Well, you could always train while I continue practising my turns. Or you could watch and give me your opinion..."
p "Sure, I'd be happy to help."
ch "Great! I'll do a few more moves and you tell me what you think...."
scene chantelleprep04a with dissolve
$ renpy.pause(1.0, hard=True)
p "Nice Chantelle, very nice..."
scene chantelleprep04b with dissolve
$ renpy.pause(1.0, hard=True)
p "Good balance, you'll rock tonight!"
scene chantelleprep05 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Damn, you're getting so strong [name]!"
p "Yeah? You like my huge muscles?"
scene chantellegymday06b with dissolve
$ renpy.pause(1.0, hard=True)
ch "Yes, I do, this made me...horny... Please come and fuck me [name]!"
p "I can't wait to see that hard body of yours in all its glory!"
scene chantelleprefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Is that what you wanted to see [name]?"
p "FUCK ME! They're perfect Chantelle! So nice and firm and round..."
scene chantelleprefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Have a good HARD look at those funbags. And show that huge log you're hiding in your shorts in return! (wink)"
p "I will, I will... Let me get those shorts down...."

$ chantelleballx = False
$ chantelleblowx = False
$ chantellelickx = False
$ chantellefloorx = False
stop music
scene chantellechoice01 with dissolve
$ renpy.pause(1.0, hard=True)
ch "I LOVE how you play with my big titties with your strong muscular arms [name]. So, what do you have in store for us?"

label ChantelleGymChoiceDay06x:
menu:
    "Why don't you show me your oral skills in preparation for the pageant..." if (chantelleblowx == False):
        ch "It's true, it's not just a beauty pageant, what comes out of the girl's mouth is also important (giggles)"
        p "Or in this case, what goes INTO her mouth..."
        jump ChantelleGymblowDay06x
    "Let me prep your bikini line and make it all shiny..." if (chantellelickx == False):
        ch "Ooh, what do you have in mind? You wanna lick my sweet pussy naughty boy?"
        jump ChantelleGymlickDay06x
    "Let's see how flexible your body is for the dance routine..." if (chantellefloorx == False):
        ch "What do you have in mind?"
        p "A particular position... Lie down on the yoga mat, you'll see..."        
        jump ChantelleGymFuckDay06x
    "Let's fuck on a yoga ball!" if (chantelleballx == False):
        ch "Well, that's original for sure..."
        jump ChantelleBallGymDay06x
    "Let's move on to the last bit, I want to see you animated..." if (chantelleblowx == True) and (chantellelickx == True) and (chantellefloorx == True) and (chantelleballx == True):
        jump ChantelleGymMovieDay06x

label ChantelleGymblowDay06x:
$ chantelleblowx = True
scene chantellepreblow with dissolve
$ renpy.pause(1.0, hard=True)
ch "I don't know [name], that love muscle of yours is just so... GIGANTIC!!!"
p "Well, good, cos you need to do some mouth muscle exercises for the pageant. Open your mouth wide and say AAAH!"
ch "AAAH!"
scene chantelleblow01 with dissolve
#play sound "Sounds/chantelleblow01.mp3"
$ renpy.pause(1.0, hard=True)
p "That's nice. Now project your chest forward and say OOOH!"
scene chantelleblow02 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Ggg...mm...OOOH!"
p "Good. But you need to practice some more..."
label ChantelleGymblowDay06bx:
play sound "Sounds/chantelleblow02.mp3"
scene chantelleblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleblow02
$ renpy.pause(0.3, hard=True)
scene chantelleblow01
$ renpy.pause(0.3, hard=True)
scene chantelleblow02
$ renpy.pause(0.3, hard=True)
scene chantelleblow01
$ renpy.pause(0.3, hard=True)
scene chantelleblow02
$ renpy.pause(0.3, hard=True)
scene chantelleblow01
$ renpy.pause(0.3, hard=True)
scene chantelleblow02
$ renpy.pause(0.3, hard=True)
scene chantelleblow01
$ renpy.pause(0.3, hard=True)
scene chantelleblow02
$ renpy.pause(0.3, hard=True)
scene chantelleblow01
$ renpy.pause(0.3, hard=True)
scene chantelleblow02
$ renpy.pause(0.3, hard=True)
scene chantelleblow01
$ renpy.pause(0.3, hard=True)
scene chantelleblow02
$ renpy.pause(0.3, hard=True)
p "Come on, take more of it, you can do it!"
scene chantelleblow03 with dissolve
$ renpy.pause(1.0, hard=True)
p "YES! I want to feel your breath on my balls!"
ch "GGGlllggg!"
scene chantellepreblow with dissolve
$ renpy.pause(1.0, hard=True)
ch "M..Ma... Jo.. A can't... speak...!"
menu:
    "Repeat":
        p "Never mind that, your mouth needs some more stretching!"
        jump ChantelleGymblowDay06bx
    "Move on":
        p "Don't worry, it will pass... Especially if we move on to another hole..."
        scene chantellechoice01 with dissolve
        $ renpy.pause(1.0, hard=True)
        jump ChantelleGymChoiceDay06x

label ChantelleGymlickDay06x:
$ chantellelickx = True
scene chantellelick01 with dissolve
play sound "Sounds/sucking02.mp3"
$ renpy.pause(3.0, hard=True)
ch "Oooh, the way you're twisting the tip of your tongue..."
label ChantelleGymlickDay06bx:
play sound "Sounds/chantellelick01.mp3"
scene chantellelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick03 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellelick02 with dissolve
$ renpy.pause(0.3, hard=True)
stop sound
menu:
    "Repeat":
        p "That was so tasty... I want seconds!"
        jump ChantelleGymlickDay06bx
    "Move on":
        scene chantellechoice01 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Now that your pussy is nice and wet, you're ready for something else..."
        ch "So, what would you like to do next [name]?"        
        jump ChantelleGymChoiceDay06x

label ChantelleGymFuckDay06x:
$ chantellefloorx = True
p "Before we commence, we need to make my seedmakers shiny with your spit..."
ch "Understood [name], I'll get right to it..."
scene chantellelickballs with dissolve
play sound "Sounds/chantelleballs.mp3"
$ renpy.pause(5.0, hard=True)
p "Yeah, that's good... Suck them and lick them everywhere Chantelle..."
ch "But they are so big [name]!"
p "And full of yummy cream for you! Now lie on your head with your arse sitcking high up in the air."
ch "What? That sounds uncomfortable..."
p "It's to work your shoulder muscles, you'll see..."
scene chantellefloor01 with dissolve
$ renpy.pause(1.0, hard=True)
p "See? How are those muscles working out Chantelle?"
ch "Fuck! That massive pole... It's turning my pussy inside out!"
scene chantellefloor02 with dissolve
$ renpy.pause(1.0, hard=True)
p "You've got to work hard to play hard..."
ch "AAH! Okay, okay, time out PLEASE!"
p "You can't quit now Chantelle, here I go!"
label ChantelleGymFuckDay06bx:
scene chantellefloor01 with dissolve
play sound "Sounds/chantellefloor02.mp3"
$ renpy.pause(0.3, hard=True)
scene chantellefloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantellefloor02
$ renpy.pause(0.3, hard=True)
scene chantellefloor01
$ renpy.pause(0.3, hard=True)
scene chantellefloor02
$ renpy.pause(0.3, hard=True)
scene chantellefloor01
$ renpy.pause(0.3, hard=True)
scene chantellefloor02
$ renpy.pause(0.3, hard=True)
scene chantellefloor01
$ renpy.pause(0.3, hard=True)
scene chantellefloor02
$ renpy.pause(0.3, hard=True)
scene chantellefloor01
$ renpy.pause(0.3, hard=True)
scene chantellefloor02
$ renpy.pause(0.3, hard=True)
scene chantellefloor01
$ renpy.pause(0.3, hard=True)
menu:
    "Repeat":
        p "I think we need to work those muscles a bit more..."
        ch "Please have mercy on my poor pussy!" 
        jump ChantelleGymFuckDay06bx
    "Move on":
        p "Now you'll be as flexible as a cheetah on stage..."
        ch "Either that or I have a broken back from that relentless pounding you gave me..."        
        scene chantellechoice01 with dissolve
        $ renpy.pause(1.0, hard=True)
        ch "So, what shall we do next [name]?"        
        jump ChantelleGymChoiceDay06x

label ChantelleBallGymDay06x:
$ chantelleballx = True
scene chantelleball01 with dissolve
#play sound "Sounds/annabed01.mp3"
$ renpy.pause(1.0, hard=True)
ch "Mmh, I can't wait to feel this big dick in my tight little pussy..."
scene chantelleball02 with dissolve
$ renpy.pause(1.0, hard=True)
ch "AAh, you're stretching me wide open!"
label ChantelleBallGymDay06bx:
scene chantelleball01 with dissolve
play sound "Sounds/chantelleball02.mp3"
$ renpy.pause(0.3, hard=True)
scene chantelleball02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball02 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball01 with dissolve
$ renpy.pause(0.3, hard=True)
scene chantelleball02
$ renpy.pause(0.3, hard=True)
scene chantelleball01
$ renpy.pause(0.3, hard=True)
scene chantelleball02
$ renpy.pause(0.3, hard=True)
scene chantelleball01
$ renpy.pause(0.3, hard=True)
scene chantelleball02
$ renpy.pause(0.3, hard=True)
scene chantelleball01
$ renpy.pause(0.3, hard=True)
scene chantelleball02
$ renpy.pause(0.3, hard=True)
scene chantelleball01
$ renpy.pause(0.3, hard=True)
scene chantelleball02
$ renpy.pause(0.3, hard=True)
scene chantelleball01
$ renpy.pause(0.3, hard=True)
scene chantelleball02
$ renpy.pause(0.3, hard=True)
scene chantelleball01
$ renpy.pause(0.3, hard=True)
scene chantelleball02
$ renpy.pause(0.3, hard=True)
scene chantelleball01
$ renpy.pause(0.3, hard=True)
stop sound
scene chantelleball03
$ renpy.pause(1.0, hard=True)
ch "Damn, it's like I'm sitting on a border fence. The steel slab kind."
menu:
    "Repeat":
        p "Well, you need to work that pussy harder if you want to get me over the edge of that wall!"
        jump ChantelleBallGymDay06bx
    "Move on":
        p "Let's move onto something else shall we Chantelle?"
        scene chantellechoice01 with dissolve
        $ renpy.pause(1.0, hard=True)
        ch "Sure, thanks for the pussy muscle exercises. What shall we do next [name]?"        
        jump ChantelleGymChoiceDay06x

label ChantelleGymMovieDay06x:
scene chantellefuckmovie with dissolve
$ renpy.pause(1.0, hard=True)
p "You need to learn to keep good balance. Try and stay steady on that yoga while I pound your tender pussy."
ch "Oooh, thanks so much [name] for helping out... You're stretching me so much already!"
p "not quite enough for this exercise..."
play music "Sounds/chantellefuckslow.mp3"
show chantellefuckslow
show faster
call screen chantelleslowfuckgymday06x
screen chantelleslowfuckgymday06x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("ChantelleFastFuckGymDay06x")

label ChantelleFastFuckGymDay06x:
stop music
hide faster
play music "Sounds/chantellefuckfast.mp3"
show chantellefuckfast
show cum
call screen chantellefastfuckgymday06x
screen chantellefastfuckgymday06x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("ChantelleCumGymDay06x")

label ChantelleCumGymDay06x:
hide chantellefuckslow
hide chantellefuckfast
stop music
scene chantellecumfill
window hide
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
ch "Damn, you're blasting your cream non-stop inside my overfilled pussy!"
p "I'm... trying to remove it, but you're so tight..."
ch "Let me squirt and push it out..."
scene chantellecum01 with dissolve
play sound "Sounds/cumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "Shit, I'm spraying everywhere now! RHAAA!"
scene chantellecum02 with dissolve
play sound "Sounds/ryancumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "There's MOOOOREE!"
ch "Oh my God, I'm bloated with a quart of your cum and you're still spewing heavy shots on my back!"
scene chantellecum03 with dissolve
play sound "Sounds/cumming.mp3" 
$ renpy.pause(2.0, hard=True)
p "Phew, that was a huge load, even by my standards..."
ch "The next person to use this gym will need to wear rock-climbing shoes to avoid slipping on the puddles of cum you've covered the floor with... (giggles)"
return

label Sex55:
stop music
scene britprefuck02
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
$ britupx = False
$ britdoggyx = False
$ britfloorx = False
$ britanalx = False
label BrittanyFuckChoiceDay06x:
menu:
    "Let me lift you up on my scepter!" if (britupx == False):
        jump BritUpDay06x
    "Let me show you how peasants like me fuck like wild animals!" if (britdoggyx == False):
        br "Ooh, that's so dirty!"
        jump BritdoggyDay06x
    "Let's get dirty on the floor..." if (britfloorx == False):
        br "You are so filthy... I name you Knight of the Scum!"
        p "I'll soon become Knight of the Cum..."        
        jump BritFloorDay06x
    "Your royal backside needs a good pounding!" if (britanalx == False):
        br "My... Royal backside? No one has ever fucked me there, and your scepter is too big for it!"
        p "Na, it will fit. And anyway, a true beauty queen needs to know how to take it every which way... Get on the floor and expose that royal rump!"
        jump BritAnalDay06x
    "Let's fuck sideways. For the viewer that is..." if (britupx == True) and (britdoggyx == True) and (britfloorx == True) and (britanalx == True):
        jump BritMovieDay06x

label BritUpDay06x:
$ britupx = True
scene britfuckup04 with dissolve
$ renpy.pause(1.0, hard=True)
p "Get ready for lift-off!"
br "Yes, hold me in your massively-muscled arms my Knight in shining armor!"
scene britfuckup02 with dissolve
$ renpy.pause(1.0, hard=True)
br "OOOH, FUCK! It's so fucking thick and DEEP!"
p "Hang on, I'll drill even deeper!"
label BritUpDay06bx:
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
        jump BritUpDay06bx
    "Move on":
        p "Time to show you some other uses to my scepter..."
        br "What would you like to do next [name]?"        
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        jump BrittanyFuckChoiceDay06x

label BritdoggyDay06x:
$ britdoggyx = True
scene britdoggy03 with dissolve
play sound "Sounds/britwet.mp3"
$ renpy.pause(6.0, hard=True)
br "Just the tip of your monster cock is already filling me up like never before!"
if (brittanyjosewin == True):
    p "So I'm much bigger than that dickhead José then?"
    br "Oh yes, MUCH bigger! Fuck me hard and deep and prove me you deserve my royal fuckhole more than him!"
label BritdoggyDay06bx:
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
        jump BritdoggyDay06x
    "Move on":
        p "Time to show you some other uses to my scepter..."
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What would you like to do next [name]?"        
        jump BrittanyFuckChoiceDay06x

label BritFloorDay06x:
$ britfloorx = True
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
label BritFloorDay06bx:
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
        jump BritFloorDay06bx
    "Move on":
        p "Time to show you some other uses to my scepter..."
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What would you like to do next [name]?"        
        jump BrittanyFuckChoiceDay06x

label BritAnalDay06x:
$ britanalx = True
scene britanal01 with dissolve
$ renpy.pause(1.0, hard=True)
br "Aah, be careful my loyal subject!"
p "Just relax Brittany, open your arse to the people!"
label BritAnalDay06bx:
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
        jump BritAnalDay06bx
    "Move on":
        p "Time to show you some other uses to my scepter..."
        scene britprefuck04 with dissolve
        $ renpy.pause(1.0, hard=True)
        br "What would you like to do next [name]?"        
        jump BrittanyFuckChoiceDay06x

label BritMovieDay06x:
scene britfuckpremovie with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready your Sumptuous Highness?"
br "I'm ready... FUCK ME!"
play music "Sounds/britfuckmovie.mp3"
show britfuckmovie
show cum
call screen britfuckmovieday06x
screen britfuckmovieday06x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("BritCumDay06x")

label BritCumDay06x:
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
br "So how does it feel having fucked the most beautiful girl on the island [name]?"
p "I feel like the King of the World!"
br "It doesn't work that way. I'm the Queen and you're NOTHING. Now leave me to pamper myself and DON'T TELL ANYONE!"
p "But... Surely, I deserve something in return for my loyal servicing of your royal fuckholes?!"
br "You are hereby knighted and allowed to service my royal holes at my leisure... Now shoo!"
p "Oh thank you so much your Magnanimous Kindness (snickers)..."
return

label Sex56:
stop music
scene debbytopless01
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
p "OOh, it WAS worth it after all... I can see aunt Debby topless coming out of the pool."
p "But I'm quite far, I should squint my eyes to see better. It always works right?"
scene debbytopless02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Yeah, that's better, I can see in more details the action now..."
scene debbytopless03 with dissolve
$ renpy.pause(1.0, hard=True)
p "She hasn't seen me, I'm too far away..."
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
p "Well, that was something everyone should see at least once in their lives... But it's getting late, I should move on."
return

label Sex57:
stop music
scene bothhouse01
$ renpy.pause(1.0, hard=True)
s "Now [name], you'd better make this wothwhile for US!"
ch "We'll certainly make it worthwhile for YOU!"
scene bothhouse02 with dissolve
$ renpy.pause(1.0, hard=True)
s "First, by getting that cock of yours HARD and READY to go!"
p "Jeezus sis... AAAH!"
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
s "Wow, you tore apart your jockstrap little brother! How are you going to explain that to mommy? (giggles)"
p "It's not the first time it happens..."
scene bothhouse06 with dissolve
play sound "Sounds/threesome01.mp3"
$ renpy.pause(3.0, hard=True)
ch "So, are you going to wave that flagpole at full mast all evening or do you want us to do something about it?"
p "I want you to do something about it."
ch "I thought you might. Nikki, why don't we show your brother how it feels to have four huge jugs wrapped around his monster shaft?"
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
p "Of course sis, I'm still raging hard for your amazing bodies!"
scene bothhouse06 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Wow, what a real STUD! So, what would you like to do next then [name]?"
$ bothoralx = False
$ bothhouseplayx = False
$ bothnikkipussyx = False
$ bothchantellepussyx = False

label BothFuckChoiceDay06x:
menu:
    "Why don't you play with each other for a while, like best pals and all that..." if (bothhouseplayx == False):
        s "I'm so horny I don't even mind..."
        ch "Me neither Nikki, let's do it!"
        jump BothPlayDay06x
    "I want some oral action!" if (bothoralx == False):
        ch "Ooh, I can't wait to blow that massive log AGAIN!"
        p "First, I wanna lick Nikki's pussy..."
        jump BothOralDay06x
    "OK, time for some incest fun with Nikki's tight pussy!" if (bothnikkipussyx == False):
        s "I can't wait to feel that log in me again [name]!"
        jump BothNikkiFuckDay06x
    "I've had it earlier, but I want it AGAIN! I'm talking Chantelle's sweet hole..." if (bothchantellepussyx == False):
        ch "I'm honored... Getting fucked TWICE in a day by the island's ultimate STUD!"
        jump BothChantelleFuckDay06x
    "Lie on the bed and get ready to receive my load both of you!" if (bothhouseplayx == True) and (bothoralx == True) and (bothchantellepussyx == True) and (bothnikkipussyx == True):
        jump BothFuckCumDay06x

label BothPlayDay06x:
$ bothhouseplayx = True
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
p "Why don't you lick my sister's pussy Chantelle?"
s "Everything in due time [name]... Watch and learn about foreplay little brother..."
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
jump BothFuckChoiceDay06x

label BothOralDay06x:
$ bothoralx = True
scene bothoral01 with dissolve
$ renpy.pause(1.0, hard=True)
s "You're learning fast little brother...."
window hide
play sound "Sounds/moaning.mp3"
$ renpy.pause(2.0, hard=True)
p "My expert tongue has no match on this island!"
ch "Always bragging... It's part of your charm....But now WE are in charge, aren't we Nikki? (wink)"
s "That's right! Lie down [name] and we'll show you how we handle... DA MAN!"
scene bothoral02 with dissolve
$ renpy.pause(1.0, hard=True)
p "GGl... Mmmm..."
s "Hush little brother... Let Chantelle take care of that monstercock of yours..."
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
label BothOral06bx:
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
        jump BothOral06bx
    "Move on":
        s "How was that little brother? It sure looked good for you from where I'm standing... Your body was convulsing..."
        p "Phew... That was cos I couldn't breathe... Let's do something that doesn't involve me almost dying please..."        
        scene bothhouse06 with dissolve
        $ renpy.pause(1.0, hard=True)
        s "Like what?"        
        jump BothFuckChoiceDay06x

label BothChantelleFuckDay06x:
$ bothchantellepussyx = True
scene bothchantelle01 with dissolve
$ renpy.pause(1.0, hard=True)
ch "Fuck me hard again like you did this afternoon [name]!"
scene bothchantelle02 with dissolve
$ renpy.pause(1.0, hard=True)
ch  "Oh, FUCK! That's so DEEP!"
p "Hold on steady Chantelle, I'm gonna take full fifteen-inch strokes now!"
label BothChantelleFuckDay06bx:
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
        jump BothChantelleFuckDay06bx
    "Move on":
        s "I think you've fucked her enough brother, give her a break..."
        p "Sure, I have other plans anyway..."
        scene bothhouse06 with dissolve
        $ renpy.pause(1.0, hard=True)
        s "Which are?"        
        jump BothFuckChoiceDay06x
                
label BothNikkiFuckDay06x:
$ bothnikkipussyx = True
scene bothsisfuck01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Open that tender pussy wide sis..."
ch "I don't even know how it's going to fit..."
s "Be caref..."
scene bothsisfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
p "That's how it fits! By rammming it in HARD!"
label BothNikkiFuckDay06bx:
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
        s "You want more? You want more of your sister's pussy, hey [name]?"
        play sound "Sounds/more.mp3"
        p "Fuck YEAH!"
        jump BothNikkiFuckDay06bx
    "Move on":
        scene bothsisfuck03
        $ renpy.pause(1.0, hard=True)
        s "Oh my God, that was so good little brother... You really pounded that bull-dick in me this time..."
        p "I aim to please..."
        s "Kiss me..."
        scene bothsisfuck04
        $ renpy.pause(1.0, hard=True)
        ch "Wow, that's so hot... But I want in on the action now, you're making me jealous! (wink)"
        scene bothhouse06 with dissolve
        $ renpy.pause(1.0, hard=True)        
        ch "What would you like to do next [name]?"
        jump BothFuckChoiceDay06x

label BothFuckCumDay06x:
scene bothsiscum01 with dissolve
$ renpy.pause(1.0, hard=True)
p "I'm about to launch some massive cum missiles!"
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(3.0, hard=True)
s "Go on, we want the BIGGEST load you can muster little brother!"
scene bothsiscum02 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(2.0, hard=True)
ch "MMmh, look at all that cum flying everywhere!"
scene bothsiscum03 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(3.0, hard=True)
s "YES, cover us in your warm cream [name]!"
ch "Damn, your brother is shooting cum non-stop all over us!"
p "RHAAA! Phew, I think that's the last of it girls..."
s "I need a shower now, to clean up all that sticky mess you made [name]..."
ch "And I'd better go back to my place, my parents might wonder where I disappeared..."
scene bothsiscum04 with dissolve
$ renpy.pause(1.0, hard=True)
ch "But first... Let's exchange some of that yummy cum with our mouths Nikki..."
p "Wow, that's so NASTY! Have a very NICE evening Chantelle!"
ch "Oh, don't worry [name], I KNOW I'll have sweet dreams! (wink)"
return

label Sex58:
stop music
scene randyred01
play sound "Sounds/dooropen.mp3"
$ renpy.pause(1.0, hard=True)
p "Not AGAIN! That redhead boy with the giant cock is about to bang YET ANOTHER HOT CHICK!"
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
p "You don't impress me! Prepare to lose your crown tomorrow!"
rb "Ignorance is bliss. Now if you'll excuse us, I still have a raging hardon and gallons of cum to unload..."
return

label Sex59:
$ morningfeetx = False
$ morningblowx = False
$ morningplayx = False
$ morningdpx = False
$ sisfirstx = False
$ momfirstx = False
stop music
scene morningfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
m "Since we all agree, what would you like to do for family morning fun [name]?" 
label MorningChoiceDay07x:
menu:
    "My cock is rock-hard and ready to burst, cool it down please!" if (morningfeetx == False):
        s "My feet are exactly what you need..."
        m "And my tits will help too..."
        jump MorningFeetDay07x
    "How about some lesbian fun... I'll watch." if (morningplayx == False):
        s "Great idea... I've always wanted to play with your fat funbags mom!"
        jump MorningPlayDay07x
    "A family that sucks together is a family that sticks together!" if (morningblowx == False):
        s "I volunteer to blow you first!"
        m "But don't make him pop too soon Nikki, I want him to fuck my mouth next..."
        jump MorningBlowDay07x
    "I can't decide which pussy to fuck!" if (morningdpx == False):
        s "Then we should let you test-drive both."
        jump MorningDoubleDay07x
    "I'm about to burst a nut!" if (morningplayx == True) and (morningblowx == True) and (morningdpx == True) and (morningfeetx == True):
        jump MorningCumDay07x

label MorningFeetDay07x:
$ morningfeetx = True
scene morningfeet01 with dissolve
$ renpy.pause(1.0, hard=True)
m "That's it, lick mommy's feet...."
s "... while I rub this great big hard dong of yours!"
scene morningfeet02 with dissolve
play sound "Sounds/morningsisbig.mp3"
$ renpy.pause(2.0, hard=True)
s "Are you ready to get teased little brother?"
p "Y... yeah..."
label MorningFeetDay07bx:
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
        p "Yeah, keep going sis, I'm close..."
        s "Oooh, you're gonna give us a great big load of pearly white cum [name]?"
        m "I can't wait to get my tits covered in your spunk son!"
        jump MorningFeetDay07bx
    "Cum (no stamina penalty)":
        scene morningfeet04 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "FUCK, I'm bursting! AAAH!"
        m "Wow, that was a HUGE shot of cum son..."
        scene morningfeet05 with dissolve
        $ renpy.pause(1.0, hard=True)
        m "Damn, you've covered my breasts with a TON of cum! Mommy is so proud of her son!"
        s "But you're still ROCK-HARD and ready for more, aren't you little brother?"
        scene morningfuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        m "Indeed, so what would you like to do next [name]?"
        jump MorningChoiceDay07x

label MorningPlayDay07x:
$ morningplayx = True
scene morningbothplay01 with dissolve
$ renpy.pause(1.0, hard=True)
s "Mom... Your tits are so big and soft...."
m "You were always tugging at them when you were a suckling baby. Do it again... I have some milk for you my sweet child."
p "Fuck yeah!"
label MorningPlayDay07bx:
scene morningbothplay02 with dissolve
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
p "Yeah, sis, twist those nipples and get some milk out!"
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
        jump MorningPlayDay07bx
    "Move on":
        s "I'm not sure I'll need breakfast anymore today...(giggles)"
        scene morningfuck02 with dissolve
        $ renpy.pause(1.0, hard=True)
        m "What would you like to do next [name]?"
        jump MorningChoiceDay07x

label MorningBlowDay07x:
$ morningblowx = True
scene morningsisblow03 with dissolve
play sound "Sounds/morningsisperfect.mp3"
$ renpy.pause(1.0, hard=True)
s "Mmh, your cock is so perfect..."
p "There you go sis, rockhard for you..."
s "MMMh, it's so tasty, I can't ever get enough of your cock little bro."
scene morningsisblow01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Then prepare to take it down your throat. DEEP!"
label MorningBlowDay07bx:
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
        jump MorningBlowDay07bx
    "Move on":
        scene morningsisblow03 with fastdissolve
        play sound "Sounds/morningsisperfect.mp3"
        s "I think I've sucked about a pint of precum from that monstrous rod..."
        p "I'm always VERY bloated in the morning..."
        m "My turn! Please fuck my mouth my sweet little pumpkin!"
        jump BothMomMorningSuckDay07x
                
label BothMomMorningSuckDay07x:
scene morningmomblow01
$ renpy.pause(1.0, hard=True)
p "Open wide Nancy. I'll pile-drive my shaft down your throat..."
m "MMM, gggllr..."
scene morningmomblow02
$ renpy.pause(1.0, hard=True)
p "There. Hold it..."
s "This is so hot, you're really fucking her mouth without mercy little brother]."
p "She asked for it, didn't she?"
label BothMomMorningSuckDay07bx:
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
        jump BothMomMorningSuckDay07bx
    "Move on":
        scene morningmomblow03 with fastdissolve
        $ renpy.pause(1.0, hard=True)
        m "*cough* Thank you son, that was so kind of you."
        p "Get up mom, and let's move on to something else, I'm still horny."
        m "Of course my sweet little pumpkin!"
        jump MorningChoiceDay07x

label MorningDoubleDay07x:
$ morningdpx = True
scene morningdp01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Mmh, which pussy to choose... Tough decision..."
m "I'm your landlady and I ORDER you to fuck me first!"
s "Hey! I'm your landlady's daughter and I REQUIRE some tenant love right now!"
menu:
    "Fuck mom first":
        p "Mom's pussy is so warm and inviting, I'll do her first!"
        m "That's a good boy! Now come and give mommy the fuck of her lifetime. AGAIN!"
        s "Be quick, my pussy is DRIPPING WET!"
        $ momfirstx = True
        jump MorningMomFirstDay07x
    "Fuck sis first":
        p "Nikki's pussy is so tight and tempting, I'll do her first!"
        s "Yeah! I'm ready, pound it hard little brother! I'll stand against the wall for you."
        m "Be quick, mommy NEEDS that cock!"
        $ sisfirstx = True
        jump MorningSisFirstDay07x
    
label MorningMomFirstDay07x:
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
if (sisfirstx == True):
    jump MorningDoubleEndDay07x
s "Let's switch now, my turn!"
jump MorningSisFirstDay07x

label MorningSisFirstDay07x:
scene morningdppresis with dissolve
$ renpy.pause(1.0, hard=True)
s "Just shove your meatpole in [name], I can't wait any longer! I WANT IT!"
p "I like your enthusiasm sis."
play music "Sounds/morningsisslow.mp3"
show morningsisslow
show faster
call screen morningsisslowday07x
screen morningsisslowday07x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)
        action Jump ("MorningSisFastDay07x")
label MorningSisFastDay07x:
hide faster
stop music
play music "Sounds/morningsisfast.mp3"
show morningsisfast
show next
call screen morningsisfastday07x
screen morningsisfastday07x:
    modal True
    button:
        xpos .82
        ypos .9
        xysize(100, 50)        
        action Jump ("MorningSisEndDay07x")

label MorningSisEndDay07x:
hide morningsisslow
hide morningsisfast
stop music
scene morningdppresis
$ renpy.pause(1.0, hard=True)
p "Phew, I pulled out just in time. I was about to burst a nut there, your pussy is so TIGHT sis!"
if (momfirstx == True):
    s "That's cos your dong is so fucking HUGE little brother! *giggles*"
    m "Now, since your cock is still hard and ready, what should we do next my stud son?"
    jump MorningDoubleEndDay07x
m "I can't wait any longer either, my turn!"
jump MorningMomFirstDay07x

label MorningDoubleEndDay07x:
scene morningfuck02 with dissolve
$ renpy.pause(1.0, hard=True)
m "What would you like to do next [name]?"
jump MorningChoiceDay07x

label MorningCumDay07x:
scene morningbothcum01 with dissolve
$ renpy.pause(1.0, hard=True)
p "There it goes, get ready for some cum flying your way! AAAH!"
window hide
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(3.0, hard=True)
m "Let it all out sweetie, mommy doesn't want you to have blueballs today."
scene morningbothcum02 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(2.0, hard=True)
s "[name]! You're blowing your load all over ME! Yummy!"
p "There's more sis, wait for it, RHAAA!"
m "What about me? I hope you kept some for me..."
scene morningbothcum03 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(3.0, hard=True)
p "Of course mom, here you go, half a pint to cover your sumptuous tits! FUCK YEAH, I'm DA MAN!"
m "Ooooh, I'm ssoo proud of you [name], you really had a HUGE supply of warm boycum for your mommy didn't you?"
s "And after he TOTALLY covered me from head to toe in spunk too..."
scene morningbothcumend with dissolve
$ renpy.pause(1.0, hard=True)
s "Now I'm going to have to take ANOTHER shower."
m "So do I. Mind if I join you Nikki?"
s "Of course not mom!"
p "What about me, mind if I join you?"
m "There's not enough space in the shower cubicle for THREE people, sweetie."
p "Oh, that's just great. I give you my most prized and sacred reproductive fluids, and this is all the gratitude I get in return."
s "Your reproductive fluids are soon to become sewer filth... See you at breakfast little brother!"
return

label Sex60:
stop music
scene saturdayyoga01 with dissolve
$ renpy.pause(1.0, hard=True)
m "Ah there you are my sweet little pumpkin. Just watch mommy and try and do exactly as she does, alright?"
p "Sure mom, I'll try."
scene saturdayyoga02 with dissolve
$ renpy.pause(1.0, hard=True)
m "First, we'll start by stretching our arms, like so..."
p "(Damn, she's weary a see-through body.... What a tease my mom is, don't you guys agree?)"
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
m "Well, stop looking at mommy's big tits for starters. What if you pop a boner during the competition? That would be most embarrassing."
p "Sure, it would..."
scene saturdayyoga07 with dissolve
$ renpy.pause(1.0, hard=True)
m "So let's finish off with the lotus position, which is great to help you in your concentration and brings positive energy into your body. Just breath in..."
m "And breath out."
m "And breath in...."
m "And breathe out."
p "This is working mom, I can feel... More focused and full of energy."
scene saturdayyoga08 with dissolve
$ renpy.pause(1.0, hard=True)
m "Well, that's great honey pot! You can thank me later tonight when you bring back home the trophy and make mommy proud... *wink*"
p "Sure mom, thanks a lot for your help, now I'm gonna win FOR SURE!"
p "I'd better get going, see you tonight."
m "Have a great day my sweet little pumpkin!"
return

label Sex61:
stop music
scene debbynewbikinipool with dissolve
show secretarybikini01 at left
show debbynewbikini01 at right
$ renpy.pause(1.0, hard=True)
d "This is Gwendoline. Maybe you've met her?"
p "Err... Yeah, maybe I did. I don't recall. Err... I plead the fifth."
st "I think I DO remember you. You STOLE a camera from Audacious HQ!"
d "All is forgiven Gwendoline. He is my guest today..."
st "Sure boss..."
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
p "Very nice Aunt Debby. I feel like I'm in 2022 now."
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
play sound "Sounds/auntphone.mp3"
with dissolve
$ renpy.pause(1.0, hard=True)
d "Sorry, I need to go and answer my phone in private. It's probably an important business call."
d "You two can continue posing. Maybe [name] can join you Gwendoline. I'll be back in a short while."
st "Okay boss, I'll take care of your nephew!"
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
label SecretaryHandjobDay07x:
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
        jump SecretaryHandjobDay07x
    "Blast your semen over her":
        jump SecretaryCumDay07x

label SecretaryCumDay07x:
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
scene debbyseccum04 with dissolve
$ renpy.pause(1.0, hard=True)
d "What the hell is going on here?"
p "Err. We got carried away."
d "Gwendoline! I told you to take care of [name], not to make him blast his cum all over my patio floor!"
st "I'm so sorry boss, but his cock... Did you see how HUGE it is?"
d "Yeah, well... It's still no excuse. Now go and clean yourself so we can continue this modelling session without CUM ALL OVER YOU."
d "And you, [name]. Get out of my house, you are nothing but a disturbance everywhere you carry that massive fuckstick of yours!"
return

label Sex62:
stop music
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
p "Okay, I'm in."
da "The l000lbs barbell we'll use for the competition is over there. Get in your jockstrap, as you have to perform half-naked under pressure..."
p "I'm comfortable performing in my XXXL jockstraps, no worries..."
da "You certainly have the confidence to win..."
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
da "I think... I want to see it ROCKHARD!"
scene daniellagym11 with dissolve
$ renpy.pause(1.0, hard=True)
da "Now we're talking! This thing is already well over a foot long... Max is going to have some STIFF competition by the looks of it."
p "Who's Max?"
da "Your main opponent... The current title holder. An alpha-preteen STUD like you've rarely seen one."
p "I'll beat him!"
da "Yeah? You think so? Prove it to me then."
scene daniellagym12 with dissolve
$ renpy.pause(1.0, hard=True)
da "I see, you want to impress me with your MASSIVE dong by getting ROCKHARD in front of me... And drooling TONS of precum all over my arm."
p "That's right. I'm the biggest STUD on the island. I'm da man, I'm DA MAN!"
da "And are your loads as big as your package suggests?"
p "Sure, and with unlimited capacity! I'll show you in no time if you keep pumping it!"
da "Now THAT is something I'd like to see. RIGHT NOW!"
scene daniellagym13 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
da "YES! BLAST that hot cum all over the place! I don't care if it's my gym and customers will be complaining about the sticky mess you've made!"
p "I should get going... Thanks for the hand. Job."
return

label Sex63:
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
da "Preteen defending champion Max!"
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
scene stud16c with dissolve
play sound "Sounds/gasp.mp3"
$ renpy.pause(1.0, hard=True)
da "Looks like [name] also managed to lift 2000lbs! It's a TIE!"
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
scene studcomp02 with dissolve
$ renpy.pause(1.0, hard=True)
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
rc "My boyfriend is 18 inches long fully erect from base to tip! ANd he's still growing since he's only 12."
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
scene studcomp02 with dissolve
$ renpy.pause(1.0, hard=True)
ar "The final round is always the toughest for the contestants since they need to ejaculate and prove their virility."
scene stud03 with dissolve
$ renpy.pause(1.0, hard=True)
da "Exactly Arnie, you should know, you designed the rules when you first launched the Mr Muscle Stud contests worlwide twenty years ago."
da "And so what we'll happen is that we'll measure the volume of cum that each of our studs can produce. Who can cum the most? First, we'll take a short break."
scene studbreak01 with fade
da "You can all have some energy drinks, courtesy of the gym."
scene dorisbreak with dissolve
$ renpy.pause(1.0, hard=True)
do "So, [name], are you going to pump out an EXTRA-BIG load for me today?"
p "I sure will Doris. You'll fucking drown in it, I promise!"
do "I'm glad to hear that, I want you to WIN this competition, you hear me?"
p "You can count on me Doris!"
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
scene josewanked03 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(1.0, hard=True)
da "There you go, keep pumping that ball-batter José... Mmmh, I can feel the warmth from where I'm kneeling... It's SCOLDING!"
scene josewanked04 with dissolve
$ renpy.pause(1.0, hard=True)
da "Nice fat load there José, a very impressive 300ml of spunk. Your competitors are going to have to churn up an extra-big load to beat you for sure!"
j "And they won't, I'm quite confident. Especially [name], he's just a junior wimp!"
p "Yeah? We'll see about that douchebag!"
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
scene redheadfuck04 with dissolve
$ renpy.pause(1.0, hard=True)
rc "Then cum for me Max! Blast as many fat ropes of preteen cum as you can muster!"
scene redheadfuck04cum with dissolve
play sound "Sounds/randyboycumming.mp3"
$ renpy.pause(1.0, hard=True)
rb "That's it, I'm CUMMING! Sooo fucking strong!"
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
do "Well, counting the full glass and the cum that's everywhere else, I estimate the volume at a FULL LITER of preteen spunk."
ar "That's astounding, I don't recall seeing a competitor deliver that much cum in all my travels to various competitions worldwide."
da "Veri-Bosti rules! But we still have a final contestant, will he be able to surpass this incredible amount of virile spunk with HIS load?"    
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
do "That was the point. Getting a MONSTER LOAD out of your giant balls!"
da "That looked like it was a LOT of cum, but was it enough to beat the current champ? Doris, what's the tally?"
play sound "Sounds/drumroll.mp3"
$ renpy.pause(3.0, hard=True)
stop sound
do "We have well OVER 1 full liter of sperm here, counting the overflowing jar and the ENORMOUS puddles of cum on the floor!"
da "Damn, [name] definitely wins this round then!"
da "We have a clear winner today. And it's a NEW title holder..."
scene compwinmc01 with dissolve
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
da "[name] wins the crown and is officially Veri Bosti's Muscle Stud 2020! Congrats to the winner!"
ar "Here is your trophy, boy. I predict a HUGE future for you. Maybe even the title of Mister World Muscle Stud."
return

label Sex64:
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
label DorisTitDay07bx:
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
        jump DorisTitDay07bx
    "Move on":
        scene doristits01 with dissolve
        $ renpy.pause(1.0, hard=True)
        do "Had enough? Scared you might cum too early perhaps?"
        p "N..No, it's just that... I need a... pause..."
        do "So what do you want to do next?"

$ dorisanalx = False
$ dorisdoggyx = False

label DorisFuckChoiceDay07x:
menu:
    "I want to feel that tight arse wrapped around my monster pole!" if (dorisanalx == False):
        do "In my arse? I sure hope I can take something as COLOSSAL as your cock in there!"
        p "So do I. But I'm guessing that somehow the dev will make it fit."
        jump DorisAnalDay07x
    "Get on all fours, I'm gonna pound you from behind!!" if (dorisdoggyx == False):
        do "WARF, warf! I'll be a good BITCH in heat for you [name]!"
        jump DorisDoggyDay07x
    "Ride me like a bull... that's hung like a bull." if (dorisanalx == True) and (dorisdoggyx == True):
        do "A bull has nothing on YOU Mr MUSCLE STUD!"
        jump DorisCumDay07x

label DorisAnalDay07x:
$ dorisanalx = True
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
label DorisAnalDay07bx:
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
        jump DorisAnalDay07bx
    "Move on":
        do "Thank you so much for such an anal pounding. I feel like my butthole virginity has been taken away from me once again."
        p "Let's switch position then."
        do "What do you have planned for me next STUD?"
        jump DorisFuckChoiceDay07x

label DorisDoggyDay07x:
$ dorisdoggyx = True
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
label DorisDoggyDay07bx:
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
        jump DorisDoggyDay07bx
    "Move on":
        do "You've fucked my pussy raw...."
        p "That was the deal Doris, you knew what you were getting yourself into."
        do "And I LOVED IT. But let's do something else so it can recover a bit..."
        jump DorisFuckChoiceDay07x

label DorisCumDay07x:
scene dorispredoggy with dissolve
$ renpy.pause(1.0, hard=True)
do "I don't know how I'm ever going to take such a MASSIVE dong up my poor little fuckhole..."
p "You're going to have to be brave and open wide for it..."
do "Alright. I'll do my best."
show dorisfuckslow
play music "Sounds/dorisslow.mp3"
call screen dorisfuckslow07x
screen dorisfuckslow07x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("DorisFuckFastDay07x") 

label DorisFuckFastDay07x:
hide dorisfuckslow
show dorisfuckfast
stop music
play music "Sounds/dorisfast.mp3"
call screen dorisfuckfast07x
screen dorisfuckfast07x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("DorisFuckEndDay07x")

label DorisFuckEndDay07x:
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
p "Yeah, I wanted to PROVE that I fully deserved the island's title of Muscle Stud."
do "And you proved it well... Over and over again. A TRUE MUSCLE STUD!"
p "I'm definitely DA MAN!"
do "I'm gonna go to the shower now, no boys allowed in our locker room, remember!"
p "I'd better get going too then..."
return

label Sex65:
stop music
scene predaniella01 with dissolve
$ renpy.pause(1.0, hard=True)
da "So, what do you think? Can you handle THAT muscled body?"
p "Yeah, I can handle it, I'm da MAN! And now DA MUSCLE STUD!"
scene predaniella02 with dissolve
$ renpy.pause(1.0, hard=True)
da "Since you won the Mr Muscle Stud competition [name], you get to choose what we do next..."
$ daniellaoralx = False
$ daniellaanalx = False
$ daniellasidex = False
label DaniellaFuckChoiceDay07x:
menu:
    "Give me a blowjob as a reward for being DA MUSCLE STUD MAN!" if (daniellaoralx == False):
        da "Of course [name], it's fully deserved after all..."
        jump DaniellaOralDay07x
    "Anal is in order. I order anal please." if (daniellaanalx == False):
        play sound "Sounds/danielladestroyed.mp3"
        $ renpy.pause(1.0, hard=True)
        da "Oh my God, my tight little butthole is really going to take a pounding isn't it?"
        p "You got that right."
        jump DaniellaAnalDay07x
    "I'll spoon you and feed you... MY DONG!" if (daniellasidex == False):
        da "I can't wait to feel that log inside me [name]!"
        jump DaniellaSideDay07x
    "I'm gonna fuck you from behind until I blast my powerful load all over you!" if (daniellaoralx == True) and (daniellaanalx == True) and (daniellasidex == True):
        da "Of fuck, I'm in for a MASSIVE dose of teenage cum then, hey?"
        p "Yep, you sure are."
        jump DaniellaCumDay07x

label DaniellaOralDay07x:
$ daniellaoralx = True
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
label DaniellaOralDay07bx:
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
        jump DaniellaOralDay07bx
    "Move on":
        scene daniellabj01 with dissolve
        $ renpy.pause(1.0, hard=True)
        da "I sure had fun with that fat fuckstick filling up my belly with warm precum..."
        p "Every good thing must end. With an even BETTER thing starting!"
        da "And what BETTER thing do you have planned [name]?"
        jump DaniellaFuckChoiceDay07x

label DaniellaAnalDay07x:
$ daniellaanalx = True
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
label DaniellaAnalDay07bx:
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
p "Oh damn, you're gripping on my shaft so tight, I just can't hold back, I 've got some cum coming your backdoor way! AAAHH!!!!"
da "Wow, I'm so proud my arse is THAT irresistible to your young donkey-cock!"
stop music
menu:
    "Repeat":
        da "Oh, you want MORE of that tight arse don't you? Even after you just dumped a load in it? Then go for it [name]!"
        jump DaniellaAnalDay07bx
    "Move on":
        da "Ooh, my tender butthole is finally going to have a respite..."
        p "But some other hole isn't."
        da "What do you have planned for me next?"
        jump DaniellaFuckChoiceDay07x

label DaniellaSideDay07x:
$ daniellasidex = True
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
label DaniellaSideDay07bx:
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
        jump DaniellaSideDay07bx
    "Move on":
        da "Please give my poor pussy a break... Let's switch position."
        p "Sure, I can think of many other things we can do..."
        da "Like what?"        
        jump DaniellaFuckChoiceDay07x
                
label DaniellaCumDay07x:
scene daniellapremoviefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
da "I can feel your cock on my butt. It's so HEAVY! It must weigh a TON!"
p "Several pounds of boymeat for you Daniella!"
da "Fuck me hard with your monster pole [name] I want it in me NOW!"
scene daniellapremoviefuck02 with dissolve
$ renpy.pause(1.0, hard=True)
da "AAAH! It's so fucking BIG!"
p "You asked for it. And now you shall receive."
label DaniellaFuckSlowDay07x:
show daniellafuckslow
play music "Sounds/daniellafuckmovie.mp3"
call screen daniellafuckslow07x
screen daniellafuckslow07x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("DaniellaFuckFastDay07x") 

label DaniellaFuckFastDay07x:
hide daniellafuckslow
show daniellafuckfast
call screen daniellafuckfast07x
screen daniellafuckfast07x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("DaniellaFuckEndDay07x") 

label DaniellaFuckEndDay07x:
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
da "Well, you did... And you now have a LIVE membership to this fitness club [name]! And an open invitation to my pussy! (wink)"
da "I'm gonna go to the shower now, no boys allowed in our locker room, remember!"
p "I'd better get going too..."
return

label Sex66:
scene compwinmc02
$ renpy.pause(1.0, hard=True)
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

$ foursomeoralx = False
$ foursomedoggyx = False
$ foursomedorisx = False
$ foursomedaniellax = False
label GangBangChoiceDay07x:
menu:
    "Get sucked by Daniella while Arnie rams her from behind" if (foursomeoralx == False) and (foursomedoggyx == False):
        da "I hope I can open my mouth wide enough for that MONSTER log Mr Muscle Stud!"
        p "It will be tough but it will fit."
        jump GangBangOralDay07x
    "Now I'll be the one getting sucked by Daniella while Arnie rams her from behind" if (foursomeoralx == False) and (foursomedoggyx == True):
        da "I hope I can open my mouth wide enough for that MONSTER log Mr Muscle Stud!"
        p "It will be tough but it will fit."
        jump GangBangOralDay07x
    "Fuck Daniella doggy-style while Arnie rams his cock down her throat" if (foursomedoggyx == False)and (foursomeoralx == False):
        da "MMmh, a sandwich from both ends, just what I was craving for..."
        jump GangBangDoggyDay07x
    "Now I'll be the one fucking Daniella doggy-style while Arnie rams his cock down her throat" if (foursomedoggyx == False) and (foursomeoralx == True):
        da "MMmh, a sandwich from both ends, just what I was craving for..."
        jump GangBangDoggyDay07x
    "I want to have some one-on-one special time with Doris' backdoor!" if (foursomedorisx == False):
        do "My backdoor you said? Ooooh, I'm ready for your monstercock STUD!"
        jump GangBangDorisDay07x
    "I want to have some one-on-one special time with Daniella's pussy!" if (foursomedaniellax == False):
        da "I'm honored... Getting fucked by the island's ultimate STUD!"
        jump GangBangDaniellaDay07x
    "Get on with the grand gangbang finale!!" if (foursomedorisx == True) and (foursomeoralx == True) and (foursomedoggyx == True) and (foursomedaniellax == True):
        jump GangBangCumDay07x

label GangBangOralDay07x:
$ foursomeoralx = True
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
jump GangBangChoiceDay07x

label GangBangDoggyDay07x:
$ foursomedoggyx = True
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
label GangBangDoggyDay07bx:
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
        jump GangBangDoggyDay07bx
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
        jump GangBangChoiceDay07x
                
label GangBangDorisDay07x:
$ foursomedorisx = True
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
label DorisFoursomeDay07bx:
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
        jump DorisFoursomeDay07bx
    "Move on":
        do "Ooh, my tender butthole is finally going to have a respite..."
        p "That's cos my cock demands some other hole!"
        scene pregangbang02 with dissolve
        $ renpy.pause(1.0, hard=True)
        do "And what do you have planned for us next?"
        jump GangBangChoiceDay07x

label GangBangDaniellaDay07x:
$ foursomedaniellax = True
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
label DaniellaFoursomeDay07bx:
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
        jump DaniellaFoursomeDay07bx
    "Move on":
        da "Please give my poor pussy a break... Let's switch position."
        p "Sure, I can think of many other things we can do..."
        scene pregangbang02 with dissolve
        $ renpy.pause(1.0, hard=True)        
        da "Like what?"        
        jump GangBangChoiceDay07x

label GangBangCumDay07x:
scene pregangbang02 with dissolve
$ renpy.pause(1.0, hard=True)
da "And now for the Grand Finale. We want both of you to PLASTER us in your hot thick cum!"
ar "Are you ready for that [name]? Cos I'm dying to ERUPT all over those hotties!"
p "Of course, my dong is ready to conquer the island with my STUD cum!"
da "Then come and fuck me while Daniella sucks a thick load out of Arnie!"
label GangbangSlowDay07x:
show gangbangslow
play music "Sounds/foursomemovie.mp3"
call screen gangbangslow01x
screen gangbangslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("GangbangFastDay07x") 

label GangbangFastDay07x:
hide gangbangslow
show gangbangfast
call screen gangbangfast01x
screen gangbangfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("GangbangEndDay07x")

label GangbangEndDay07x:
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
da "We'll head for the locker room showers now, no boys allowed! (wink)..."
ar "I spotted some hot fitness MILF in the gym, so if you'll excuse me ladies..."
do "Come back and visit us anytime you want Arnie!"
ar "I'll BE BACK."
p "Hey, what about me?"
da "Of course, you now have a LIVE membership to this fitness club [name]! And an open invitation to our pussies! (wink)"
return

label Sex67:
$ nikkitopoffx = False
stop music
scene sleepover01 with fade
$ renpy.pause(1.0, hard=True)
s "Hey! Why are you here? This is a girls' sleepover!"
ch "I don't mind him being here Nikki. Maybe we can have some fun at his expense..."
show sleepover01b with dissolve
s "What do you have in mind?"
ch "A game of truth or dare..."
p "Okay, I'm in, I like a challenge!"
ch "Great, then let's all sit down on the floor in a circle."
p "A circle jerk?"
scene sleepover01 with dissolve
ch "No, not a circle jerk. (sigh)"
scene sleepover02 with dissolve
$ renpy.pause(1.0, hard=True)
ch "I start then, since I had the idea of playing this game..."
ch "Truth or dare [name]?"
p "Dare."
ch " Mmmh, Let me think... Kiss your sister on the mouth!"
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
scene sleepover02 with dissolve
play sound "Sounds/kissing.mp3"
$ renpy.pause(1.0, hard=True)
p "Now it's MY turn. Nikki, truth or dare?"
s "DARE!"
p "Alright. Why don't you..."
menu:
    "...take your top off.":
        show sleepovernikkishockedc with dissolve
        s "What? That's disgusting! Asking your sister to show you her tits!"
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
        $ nikkitopoffx = True
        jump Sleepover03x
    "...kiss Chantelle.":
        ch "It was to be expected. Boys just love watching women kiss."
        s "Cos they are such PERVERTS!"
        p "It's purely for educational purposes."
        scene sleepoverkissing with dissolve
        play sound "Sounds/kissing.mp3"
        $ renpy.pause(1.0, hard=True)
        s "There, happy now?"
        p "Yep."
        jump Sleepover03x

label Sleepover03x:
if nikkitopoffx:
    scene sleepover02
    show sleepovernikkitopoff
    with dissolve
if nikkitopoffx == False:
    scene sleepover02 with dissolve
$ renpy.pause(1.0, hard=True)
s "My turn. For Chantelle. Truth or dare?"
ch "Dare..."
if nikkitopoffx:
    show sleepovernikkishockedb with dissolve
    s "Since I'm half-naked, it's only fair that..."
    ch "I take MY top off? *wink*"
    s "That's right."
    scene sleepoverchantelle01
    show sleepovernikkitopoffb
    with dissolve
    $ renpy.pause(1.0, hard=True)
    ch "Alright then... I bet your brother is going to enjoy this."
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
    jump Sleepover04x
if nikkitopoffx == False:
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
    ch "Alright then... I bet your brother is going to enjoy this."
    p "Purely for educational purposes."
    scene sleepoverchantelle02 with dissolve
    $ renpy.pause(1.0, hard=True)
    ch "I'll slowly pull it up..."
    p "(Dang, what a fine arse she has...)"
    scene sleepoverchantelle03 with dissolve
    $ renpy.pause(1.0, hard=True)
    ch "To reveal my Triple-D boobies... Like what you see [name]?"
    p "Yes... Yes... I do. Thank you Chantelle."
    jump Sleepover04x

label Sleepover04x:
if nikkitopoffx:
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
    jump Sleepover04bx
if nikkitopoffx == False:
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
    jump Sleepover04bx
    
label Sleepover04bx:
if nikkitopoffx:
    scene sleepoverryanstrap01a
    show sleepoverryanstrap01b
    with dissolve
    $ renpy.pause(1.0, hard=True)
if nikkitopoffx == False:
    scene sleepoverryanstrap01a with dissolve
    $ renpy.pause(1.0, hard=True)
p "There. Amazed yet?"
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
s "Yes you did little brother. You managed to lure Chantelle and me into your den of depravity with that huge log you're hiding down there."
ch "And those huge muscles... Your brother is making me so horny..."
p "WOO-HOO! Double delight it is then!"
s "Let us get ready for a HOT night of love with you by getting into some sexy lingerie..."
jump Sex57

label Sex68:
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
p "She's hot, who cares if she sucked a whole bus?"
scene succubus02 with dissolve
$ renpy.pause(1.0, hard=True)
p "You have five minutes to show your appreciation lady..."
rc "That is PLENTY of time, don't worry."
q "No, what have you done [name]? She'll suck the life energy out of us!"
p "Na, we'll be fine. I can control myself, don't worry."
q "I think you fell into her TRAP!"
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
scene succubus16  with dissolve
play sound "Sounds/lotofcum.mp3"
$ renpy.pause(2.0, hard=True)
rc "Wow, that's a lot of cum... I'd better get going now, thank you boys for the fun time!"
q "She got us [name]. I already feel weaker."
p "Weaker than you already were??? Don't worry about it, I'll be swimming anyway."
q "I'm afraid not. You weren't registered in time except for the mixed relay."
p "Ah, shit. Let's go anyway, we're late."
return

label Sex69:
stop music
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
        jump CompKatex
    "Talk to Maddy":
        jump CompMaddyx
    "Talk to Brittany":
        jump CompBrittanyx

label CompKatex:
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
k "Alright, I got it. I think."
return

label CompMaddyx:
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
p "You're right, I feel better already."
md "Let's go to our team's bench, it's about to start."    
return

label CompBrittanyx:
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
return

label Sex70:
stop music
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
rb "Don't worry, when this competition is over, I'll plaster them with a TON of my preteen cum!"
hg "Mmmh, I can't WAIT!"
scene pamelacomp02 with dissolve
$ renpy.pause(1.0, hard=True)
pa "*cough* How about you do that somewhere else please, this is a SWIMMING COMPETITION."
play sound "Sounds/applause.mp3"
scene pamelacomp01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "And now for the final and deciding round... The mixed relay! Which we shall skip till the end where Max wins for the purpose of this CG gallery."
play music "Sounds/cheering.mp3"
scene relayend01
show relayend03
with dissolve
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
rb "You hear that [name]? By next week, your WHOLE SCHOOL will be just like them... Delirious with lust for my preteen ALPHA-BULLCOCK!"
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
rc "Cover us in your preteen MEGA-LOAD, Max!"
hg "And then, FUCK us and FILL us BOTH with ounces of your virile spunk!"
rb "Of course, I have plenty of cum in store for you girls... But we should first go and get my winner's belt back."
p "I'm outta here, this is getting too humiliating, I don't want to see this douchebag with his trophy belt."
stop sound
scene relayendmaxwin05 with fade
$ renpy.pause(1.0, hard=True)
q "It was tough... He got the trophy, proudly displaying his bulge in front of everyone... Viviane is furious with you too, I'm warning you."
p "Don't tell me anything more... I have more important things to do today. HUMILIATE JOSE!"
q "Oh yes, I remember now, it's the end of the competition today isn't it? I hope you beat him, I hate this arsehole!"
p "Leave me alone now. I'll take a shower and leave to finish off some things..."
return

label Sex71:
default vivianelockercx = False
default pamelapussycx = False
default vivianeoralcx = False
default bothupcx = False
default pamelagroundcx = False
stop music
scene showercomp01 with dissolve
play music "Sounds/shower.mp3"
p "Mmmh, a nice shower after this exhausting competition..."
scene showerfuckboth01 with dissolve
play music "Sounds/shower.mp3"
pa "Well, who do we have here taking a shower... The CHAMPION! In all his glorious naked GLORY!"
vi "The champion who deserves a sexy REWARD..."
window hide
show doubledelight:
    xalign 0.6 yalign 0.2
    zoom 0.5
    linear 2.0 zoom 1.0
play sound "Sounds/delight.mp3"
$ renpy.pause(4.0, hard=True)
hide doubledelight
p "Alright! A threesome coming my way! WOo-ooh!"
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
label ShowerThreesomeMouthFuckx:
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
        jump ShowerThreesomeMouthFuckx
    "Move on":
        scene showerfuckboth03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Let's move to the locker area, my cock DEMANDS some more attention!"
        vi "And we'll make sure you GET that attention [name]..."
        pass
        
label ThreesomeShowerFuckChoicex:
scene showerthreesomeprefuck01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "FUCK! Look at that MONSTER DONG! Already leaking pre-cum... Mmmh... What shall we do about it [name]?"
label ThreesomeShowerFuckChoicebx:
menu:
    "I want some special time with Viviane... Against the lockers!" if vivianelockercx == False:
        vi "The lockers will lose in that fight... But I' =m in!"
        jump VivianeThreesomefuckDay08x
    "Pamela, you're the type to ride me like a cowgirl!" if pamelapussycx == False:
        pa "you got that right, BULL-STUD!"
        jump PamelaBull08x
    "Viviane, your mouth on my cock sounds like a perfect patch!" if vivianeoralcx == False:
        vi "I have the perfect mouth for your perfect cock indeed!"
        jump VivianeOralc08x
    "I'll lift Pamela up in my strong arms while I power-fuck Viviane from behind!" if bothupcx == False:
        pa "you got that right, BULL-STUD!"
        jump BothUp08x
    "Get on the floor, Pamela. I'm gonna fuck your pussy into submission!" if pamelagroundcx == False:
        pa "you got that right, BULL-STUD!"
        jump PamelaGround08x
    "Time for me to come inside Pamela's pussy." if (pamelagroundcx and bothupcx and vivianeoralcx and pamelapussycx and vivianelockercx):
        pa "Oh, thank you so much, I'm going to get some CHAMPION CUM in me, yippee!"
        jump BothFinale08x

label VivianeThreesomefuckDay08x:
$ vivianelockercx = True
scene vivianeprefuck with dissolve
p "I've pinned you down against the lockers... Time to smash the padlock on your uterus with my sledgehammer!"
vi "OOOh, you have the worst lines [name], but I forgive you because you're about to give me what I want, that fat young bullcock of yours! FUCK ME!"
play music "Sounds/vivianefuck.mp3"
show vivianefuck
show cum
call screen vivianefuckday08bx
screen vivianefuckday08bx:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("VivianeThreesomeCumDay08x")

label VivianeThreesomeCumDay08x:
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
jump ThreesomeShowerFuckChoicebx

label PamelaBull08x:
$ pamelapussycx = True
scene pamelacowgirl01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Keep steady mustang! This cowgirl is going to ride you into submission!"
p "Oh fuck, I think I'm in for a wild ride!" 
label PamelaBull08bx:
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
        jump PamelaBull08bx
    "Move on":
        pass    
pa "How was it for you stallion?"
p "Damn, I feel like I rode all the way to California..." 
jump ThreesomeShowerFuckChoicebx   

label VivianeOralc08x:
$ vivianeoralcx = True
scene vivianeoral01 with dissolve
play sound "Sounds/vivianeblow01.mp3"
$ renpy.pause(10.0, hard=True)
vi "Mmh, you're so strong holding me like that!"
p "That's cos I need to lick that tasty pussy of yours!"
vi "While I suck on that giant shaft of yours! It's a deal!"
label VivianeOral08bx:
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
        jump VivianeOral08bx
    "Move on":
        pass    
vi "I think I dislocated my jaw..."
p "It happens...Let's move on to something else." 
jump ThreesomeShowerFuckChoicebx   

label BothUp08x:
$ bothupcx = True
scene showerup01 with dissolve
$ renpy.pause(1.0, hard=True)
vi "Damn, that's a POWERTOOL drilling inside me!"
pa "And some mighty powerful arms lifting me up like I weigh nothing!"
scene showerup03 with dissolve
$ renpy.pause(1.0, hard=True)
p "Don't forget my expert tongue on your pussy..."
vi "Stop talking and FUCK ME!"
label BothUp08bx:
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
        jump BothUp08bx
    "Move on":
        scene showerup03 with dissolve
        $ renpy.pause(1.0, hard=True)
        p "One final lick and we're good to go..."
        play sound "Sounds/lick.mp3"
        jump ThreesomeShowerFuckChoicebx
    
label PamelaGround08x:
$ pamelagroundcx = True
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
label PamelaGround08bx:
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
        jump PamelaGround08bx
    "Move on":
        scene bothpamprefuck with dissolve
        $ renpy.pause(1.0, hard=True)
        p "Good time to stop, I was on the verge of blowing my load... Phew..."
        vi "That means this a was a GOOD pussy Pamela."
        pa "Oooh, I'm so glad he liked it... My poor pussy..."
        jump ThreesomeShowerFuckChoicebx


label BothFinale08x:
scene showeranimb11 with dissolve
$ renpy.pause(1.0, hard=True)
p "There you go, impale yourself on my pole. And Viviane, make my balls shiny with your spit."
vi "Of course, I'll make sure you have a HUGE load for Pamela in your GIANT cum factories!"
pa "Oh my God, you're so BIG! I can't believe my poor little pussy can even take it..."
p "And it can take even more inches..."
show threesomeshoweranimslow
play music "Sounds/foursomemovie.mp3"
call screen threesomeshoweranimslow01x
screen threesomeshoweranimslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("ThreesomeShowerAnimfast08x") 

label ThreesomeShowerAnimfast08x:
hide threesomeshoweranimslow
show threesomeshoweranimfast
call screen threesomeshoweranimfast01x
screen threesomeshoweranimfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("ThreesomeShowerAnimEnd08x")

label ThreesomeShowerAnimEnd08x:
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
scene showerthreesomecum04 with dissolve
$ renpy.pause(1.0, hard=True)
pa "You did such a mess [name]. Both in my pussy and on Viviane's body..."
play sound "Sounds/lick.mp3"
vi "Yeah, I'm so happy to have such a STUD in my class..."
p "OK, girls, I'd love to continue fucking you all day, but I need to go. I have an old foe to meet... And I also have to eat something."
return

label Sex72:
default pamelaanalbx = False
default pamelablowbx = False
default pamelapussybx = False
stop music
scene showerfuckpamela01 with dissolve
play music "Sounds/shower.mp3"
pa "Well, who do we have here taking a shower... The CHAMPION! In all his glorious naked GLORY!"
pa "I see you for what you are now... A SEX GOD to ravish my body!"
p "Alright!"
pa "Let's move to the lockers area, Someone might see us and I like my sex DANGEROUS and ROUGH!"
scene pamelaprefuck02b with dissolve
$ renpy.pause(1.0, hard=True)
pa "Now come and RAVISH my body, CHAMPION!"
jump PamelaFuckChoiceDay08bx
label PamelaFuckChoiceDay08x:
scene pamelaprefuck02b with dissolve
$ renpy.pause(1.0, hard=True)
pa "So... What are you going to do to me now [name]?"
label PamelaFuckChoiceDay08bx:
menu:
    "I want to take you up the arse and work my hip muscles!" if (pamelaanalbx == False):
        pa "Great idea! They really help improve the speed of your legs underwater..."
        jump PamelaAnalDay08x
    "I'll hold you up while I pummel my great pile-driver in your mouth!" if (pamelablowbx == False):
        pa "Mmh, that sounds so hot! Lift me up in your muscular arms and lick my pussy!"
        jump PamelaBlowDay08x
    "Let's get on the floor so you can ride my huge dong!" if (pamelapussybx == False):
        pa "So I'll be doing all the work? I guess you deserve it STUD!"
        jump PamelaPussyDay08x
    "I'm going to turn your pussy inside out and spray a heavy dose a cum deep inside it!" if (pamelapussybx == True) and (pamelablowbx == True) and (pamelaanalbx == True):
        pa "Mmmh, I can't wait... My pussy is REAL thirsty right now!"
        jump PamelaMovieDay08x

label PamelaAnalDay08x:
$ pamelaanalbx = True
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
label PamelaAnalDay08bx:
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
        jump PamelaAnalDay08bx
    "Move on":
        pass
scene pamelaanal03 with dissolve
$ renpy.pause(1.0, hard=True)
pa "My God, it feels like my arse is nothing more than a gaping hole now..."
p "It sure looks like it from where I'm standing..." 
jump PamelaFuckChoiceDay08x

label PamelaBlowDay08x:
$ pamelablowbx = True
scene pamelaoral01 with dissolve
play sound "Sounds/vivianeblow01.mp3"
$ renpy.pause(10.0, hard=True)
pa "Mmh, you're so strong holding me like that!"
p "That's cos I need to lick that tasty pussy of yours!"
pa "While I suck on that giant shaft of yours! It's a deal!"
label PamelaBlowDay08bx:
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
        jump PamelaBlowDay08bx
    "Move on":
        pass    
pa "I think I dislocated my jaw..."
p "It happens...Let's move on to something else." 
jump PamelaFuckChoiceDay08x  

label PamelaPussyDay08x:
$ pamelapussybx = True
scene pamelacowgirl01 with dissolve
$ renpy.pause(1.0, hard=True)
pa "Keep steady mustang! This cowgirl is going to ride you into submission!"
p "Oh fuck, I think I'm in for a wild ride!" 
label PamelaPussyDay08bx:
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
        jump PamelaPussyDay08bx
    "Move on":
        pass    
pa "How was it for you stallion?"
p "Damn, I feel like I rode all the way to California..." 
jump PamelaFuckChoiceDay08x    

label PamelaMovieDay08x:
scene pamelaprefuck02b with dissolve
p "I've pinned you down against the lockers... Time to smash the padlock on your uterus with my sledgehammer!"
pa "OOOh, you have the worst lines [name], but I forgive you because you're about to give me what I want, that fat young bullcock of yours! FUCK ME!"
play music "Sounds/vivianefuck.mp3"
show pamelaanim
show cum
call screen pamelafuckday08x
screen pamelafuckday08x:
    modal True
    button:
        xpos .88
        ypos .9
        xysize(100, 50)        
        action Jump ("PamelaFuckCumDay08x")

label PamelaFuckCumDay08x:
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
return

label Sex73:
stop music
scene nikkisunbathing01 with dissolve
play music "Sounds/gardensound.mp3"
$ renpy.pause(1.0, hard=True)
p "Nikki is frigging herself on the lounge chair... I wonder what she's thinking about?"
play sound "Sounds/womansigh.mp3"
s "Ooh, [name]..."
p "Nice, she's thinking about ME!"
p "Maybe it's time to make a move..."
scene nikkisunbathing02 with dissolve
$ renpy.pause(1.0, hard=True)
p "Hey Nikki, guess who won the swimming competition for the school this morning?"
s "I don't need to guess, I already know! Congrats little brother!"
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
p "No way I'll lose to this douchebag! But yeah, I feel great, thanks a lot sis!"
s "Off you go now, see you tonight..."
return

label Sex74:
stop music
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
stop sound
return

label Sex75:
stop music
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
return

label Sex76:
stop music
scene finallose01 with dissolve
$ renpy.pause(1.0, hard=True)
j "And now... Prepare for your final humiliation. I'm gonna fuck your mother right here in front of you!"
m "Oooh, YES PLEASE!"
menu:
    "OK, I admit I've lost but I don't want to see this NTR shit.":
        j "COWARD!"
        return
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
j "With me, not with your lousy son, right?"
m "Of course! He's a wimp, I totally want to NTR him right now and then I'll kick him out of the house!"
an "Oh, you hear that [name]? Your mom really wants my son's HORSEDICK in her, doesn't she?"
scene finallose04 with dissolve
play sound "Sounds/womansigh.mp3"
$ renpy.pause(1.0, hard=True)
m "Oooh, it's sssoo BIG! He's drilling my pussy all the way to my womb! AAAh, I'm cumming already!!!"
j "The first of many cums... That's what studs do, make women come like crazy on their donkey-dicks. Watch and learn, WORM!"
an "Don't forget about your dear mommy, José!"
scene finallose05 with dissolve
$ renpy.pause(1.0, hard=True)
j "Of course not, mom, come and kiss me while I pound [name]'s mother's sweet pussy."
play sound "Sounds/kissing.mp3"
$ renpy.pause(1.0, hard=True)
m "Ooh, AAH, CUMMING AGAIN!"
an "And now, fill her up with a HUGE load José!"
j "Sure thing! Right in front of [name]..."
scene finallose06 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
j "FUCK YEAH! I'm dumping my load inside your mother's pussy, WORM!"
m "I can feel it José, your shots are ssooo POWERFUL!"
an "Pull your mammoth dong out my darling stud-son and cover us in your abundant cream! Show [name] what a CUM-MISSILE you have between your legs!"
scene finallose07 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
j "Alright, here you are, receive that hot dose of teenage spunk! RHAAA!"
m "Just look at that will you my sweet little pumpkin? This STUD is BLASTING the biggest cumshots ever!"
p "Nooo! I can cum WAY MORE than that, I swear!"
s "Not today clearly, you're the beta-weakling now, [name]..."
m "Ooh, I wish you were MY son instead of this lousy pindick I have under my roof..."
scene finallose07b with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
j "I ain't done yet, I'm gonna paint you both in my white scum!"
m "YES, you OWE us now José, my son is nothing but a wimp! YOU'RE THE SCHOOL STUD FOR LIFE!"
scene finallose09 with dissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
s "Did you hear that [name]? José is the TRUE school STUD... Big time."
an "I'm ssoo proud of you José! Keep pumping that fat load all over the place!"
scene finallose08 with dissolve
$ renpy.pause(2.0, hard=True)
j "FUCK YEAH! I'm finally done with your mom, [name]. I think it's time for you to come and clean up the mess I've made inside her pussy..."
m "Ooh, yes, that will definitely put him in his place. WAY BELOW YOU, STUD!"
scene finallose09 with dissolve
$ renpy.pause(1.0, hard=True)
s "You heard him... Now go and do your duty [name]. From now on, you're \"creampie cleaning boy\"!"
p "What??? But... I'm da man, I'm..."
s "No you're NOT. You're NOTHING BUT A WORM! Now OBEY your new MASTER!"
m "I'm waiting for you my sweet little pumpkin... Don't make José wait or he'll get angry and BEAT YOU UP. He's way more muscular that you are, you know that now, right?"
scene finallose10 with dissolve
$ renpy.pause(1.0, hard=True)
m "That's it... clean it up [name]. Lick all your rival's virile seed that's seeping from your mother's pussy..."
p "*slurp* *lick*"
j "I think you know your place now worm. I'll leave you to your \"family duties\", I have my own to fulfill back home. Not the same kind as you obviously..."
s "Can I come too José?"
j "Of course, there's plenty of inches and cumloads to go around for you Nikki..."
s "Oh goody! Bye [name]. LOSER!"
return

label Sex77:
stop music
scene finalwin01 with dissolve
$ renpy.pause(1.0, hard=True)
an "I'm sorry José, you're my son, but face it, you can't compete with [name], he's a REAL stud. I've been looking for one ever since we moved here and now I've FOUND HIM!"
j "No, mom! Please, don't do this to me!!!!"
p "BE QUIET, WIMP! Nikki, take care of this loudmouth and show him how you treat inferior beta-males like him."
s "With pleasure little bro. Take those trunks off José, we want to see how tiny your pindick is compared to my brother's MONSTER COCK."
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
p "Now you can come back Nikki, the first round is with my family... Anna, you can go and taunt your son in the meantime. Don't worry, your turn will come."
an "Of course stud, I can't wait to watch what you're made of. While humiliating José. Such a disappointing wimp of a son..."
scene finalwin01aa with dissolve
$ renpy.pause(1.0, hard=True)
an "You call THAT a cock? This pathetic thing is USELESS!"
j "Mother, please! *sob*"
an "Stop wimpering and WATCH the SHOW!"
p "Now, gather round my fair ladies and show him how you worship my HORSECOCK!"
m "Of course my sweet little pumpkin!"
scene finalwin01b with dissolve
$ renpy.pause(1.0, hard=True)
s "It's ssoo fucking HUGE little brother! My hand can't even get halfway around its incredible GIRTH!"
d "This fat cock was made for being pumped by THREE sets of hands!"
scene finalwin01c with dissolve
$ renpy.pause(1.0, hard=True)
p "Pump my fat shaft! Prep it up!"
label ShaftPumpingx:
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
        jump ShaftPumpingx
    "Move on":
        jump FinalWin02x
        
label FinalWin02x:
p "First, I'll fuck Nikki... While I finger both my mom's and aunt's pussies with my expert fingers. Spread your legs for me Nikki..."
s "Of course little brother!"
scene finalwinsis01 with dissolve
$ renpy.pause(1.0, hard=True)
p "Ready?"
m "Yes, we all are my stud son! Fuck your sister!"
label FinalFuckSisx:
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
        jump FinalFuckSisx
    "Cum all over her":
        p "I'm gonna dump my first load NOW!"
        m "Cover her tits in your warm spunk, my sweet studly son!"
        jump FinalFuckSisCumx
  
label FinalFuckSisCumx:
scene finalwinsis04 with fastdissolve
play sound "Sounds/cumming.mp3"
$ renpy.pause(1.0, hard=True)
p "RHAAA! Nutting BIG TIME!"
d "We can see that [name]! You're HOSING her down with your fat cumpipe!"
scene finalwinsis05 with fastdissolve
$ renpy.pause(1.0, hard=True)
s "Ooh, look at all that RED-HOT SPUNK! It's so warm... Mmmh, I love it... So tasty too! Thank you little bro..."
m "I hope you can still keep it up [name], your mother is really HORNY!"
p "Don't worry mom, you're NEXT. UP THE ARSE. NOW!"
d "Oh wow, my nephew is such a fucking SUPERSTUD..."
scene finalfuckmom01 with dissolve
$ renpy.pause(1.0, hard=True)
m "I can't believe I'm letting my son fuck me right here on a public beach, and RIGHT UP THE ARSE! But it feels sssooo good..."
p "Get ready to ride my dong, mom!"
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
d "Damn, your shots are STILL so ENORMOUS [name], where do you keep all that cream, my stud nephew? Your balls must have OUNCES of pent-up cum stored in them!"
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
m "Oh, you hear that José? Your mom really wants my son's HORSEDICK in her, doesn't she?"
scene finalwin03b with dissolve
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
p "It definitely fits, you were clearly made for taking MY dong, Anna!"
an "YES, I was, and your cock is now the ONLY one I'll fuck!"
show finalfuckannaslow
play music "Sounds/foursomemovie.mp3"
call screen finalfuckannaslow01x
screen finalfuckannaslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/faster.png"
        hover "Icons/faster.png"
        action Jump ("FinalFuckAnnaFast08x") 

label FinalFuckAnnaFast08x:
an "AAAH! Fuck me FASTER please, you GIANT-COCKED SUPERSTUD!"
hide finalfuckannaslow
show finalfuckannafast
call screen finalfuckannafast01x
screen finalfuckannafast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/next.png"
        hover "Icons/next.png"
        action Jump ("FinalFuckAnnaEnd08x")

label FinalFuckAnnaEnd08x:    
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
m "Let me kiss you my sweet studson, while you PUMMEL your fuckstick into your new cockslave..."
play sound "Sounds/kissing.mp3"
$ renpy.pause(1.0, hard=True)
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
m "Pull your mammoth dong out my sweet boy and cover us in your abundant cream! Show José what a CUM-MISSILE you have between your legs!"
scene finalwin06 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
p "Alright, here you are, receive that hot dose of teenage spunk! RHAAA!"
an "Just look at that will you José? This STUD is BLASTING the biggest cumshots ever!"
s "Each jet is probably more plentiful than a full orgasm from you pathetic prick, isn't it José?"
j "Nooooo! That's not true..."
an "YES IT IS! My little bro here can muster OUNCES of cum every time he unleashes a mighty orgasm!"
scene finalwin07 with dissolve
play sound "Sounds/ryancumming.mp3"
$ renpy.pause(2.0, hard=True)
p "I ain't done yet, I'm gonna paint you both in my white scum!"
an "YES, you OWE us now [name], my son is nothing but a wimp! YOU'RE THE SCHOOL STUD FOR LIFE!"
s "Did you hear that José? You've lost your title... Big time."
m "Mommy is ssoo proud of you [name]! Keep pumping that fat load all over the place!"
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
return


