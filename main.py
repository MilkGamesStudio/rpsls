def on_button_pressed_a():
    global p1
    p1 = randint(0, 4)
    if p1 == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif p1 == 1:
        basic.show_icon(IconNames.SCISSORS)
    elif p1 == 2:
        basic.show_icon(IconNames.SQUARE)
    elif p1 == 3:
        basic.show_icon(IconNames.COW)
    elif p1 == 4:
        basic.show_leds("""
            . # # # #
            . # # . .
            . # # # #
            . # # . .
            . # # . .
            """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if p1 != 5 and p2 != 5:
        if p1 == 0 and p2 == 4:
            basic.clear_screen()
            basic.show_string("p1 win!")
        elif p1 == 0 and p2 == 1:
            basic.clear_screen()
            basic.show_string("p1 win!")
        elif p1 == 1 and p2 == 2:
            basic.clear_screen()
            basic.show_string("p1 win!")
        elif p1 == 1 and p2 == 4:
            basic.clear_screen()
            basic.show_string("p1 win!")
        elif p1 == 2 and p2 == 0:
            basic.clear_screen()
            basic.show_string("p1 win!")
        elif p1 == 2 and p2 == 3:
            basic.clear_screen()
            basic.show_string("p1 win!")
        elif p1 == 3 and p2 == 1:
            basic.clear_screen()
            basic.show_string("p1 win!")
        elif p1 == 3 and p2 == 0:
            basic.clear_screen()
            basic.show_string("p1 win!")
        elif p1 == 4 and p2 == 2:
            basic.clear_screen()
            basic.show_string("p1 win!")
        elif p1 == 4 and p2 == 3:
            basic.clear_screen()
            basic.show_string("p1 win!")
        elif p2 == 0 and p1 == 4:
            basic.clear_screen()
            basic.show_string("p2 win!")
        elif p2 == 0 and p1 == 1:
            basic.clear_screen()
            basic.show_string("p2 win!")
        elif p2 == 1 and p1 == 2:
            basic.clear_screen()
            basic.show_string("p2 win!")
        elif p2 == 1 and p1 == 4:
            basic.clear_screen()
            basic.show_string("p2 win!")
        elif p2 == 2 and p1 == 0:
            basic.clear_screen()
            basic.show_string("p2 win!")
        elif p2 == 2 and p1 == 3:
            basic.clear_screen()
            basic.show_string("p2 win!")
        elif p2 == 3 and p1 == 1:
            basic.clear_screen()
            basic.show_string("p2 win!")
        elif p2 == 3 and p1 == 0:
            basic.clear_screen()
            basic.show_string("p2 win!")
        elif p2 == 4 and p1 == 2:
            basic.clear_screen()
            basic.show_string("p2 win!")
        elif p2 == 4 and p1 == 3:
            basic.clear_screen()
            basic.show_string("p2 win!")
        elif p1 == p2:
            basic.clear_screen()
            basic.show_string("draw!")
    else:
        basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global p2
    p2 = randint(0, 4)
    if p2 == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif p2 == 1:
        basic.show_icon(IconNames.SCISSORS)
    elif p2 == 2:
        basic.show_icon(IconNames.SQUARE)
    elif p2 == 3:
        basic.show_icon(IconNames.COW)
    elif p2 == 4:
        basic.show_leds("""
            . # # # #
            . # # . .
            . # # # #
            . # # . .
            . # # . .
            """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global p1, p2
    p1 = 5
    p2 = 5
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

p2 = 0
p1 = 0
p1 = 5
p2 = 5