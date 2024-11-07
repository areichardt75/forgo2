# A megnyomasara iranyt valt a forgas

def on_button_pressed_a():
    global irany
    if irany > 0:
        if sebesseg == 1:
            irany = -1
        else:
            irany = -2
    else:
        if sebesseg == 1:
            irany = 1
        else:
            irany = 2
input.on_button_pressed(Button.A, on_button_pressed_a)

def forgat(num: number):
    if num == 1:
        basic.show_leds("""
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            """)
    if num == 3:
        basic.show_leds("""
            # . . . .
            . # . . .
            . . # . .
            . . . # .
            . . . . #
            """)
    if num == 5:
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            . . . . .
            . . . . .
            """)
    if num == 7:
        basic.show_leds("""
            . . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            """)
    if irany > 0:
        if num == 2:
            basic.show_leds("""
                . # . . .
                . # . . .
                . . # . .
                . . . # .
                . . . # .
                """)
        if num == 4:
            basic.show_leds("""
                . . . . .
                # . . . .
                . # # # .
                . . . . #
                . . . . .
                """)
        if num == 6:
            basic.show_leds("""
                . . . . .
                . . . # #
                . . # . .
                # # . . .
                . . . . .
                """)
        if num == 8:
            basic.show_leds("""
                . . . # .
                . . # . .
                . . # . .
                . . # . .
                . # . . .
                """)
    else:
        if num == 2:
            basic.show_leds("""
                . # . . .
                . . # . .
                . . # . .
                . . # . .
                . . . # .
                """)
        if num == 4:
            basic.show_leds("""
                . . . . .
                # # . . .
                . . # . .
                . . . # #
                . . . . .
                """)
        if num == 6:
            basic.show_leds("""
                . . . . .
                . . . . #
                . # # # .
                # . . . .
                . . . . .
                """)
        if num == 8:
            basic.show_leds("""
                . . . # .
                . . . # .
                . . # . .
                . # . . .
                . # . . .
                """)

def on_button_pressed_b():
    global irany
    if irany > 0:
        if sebesseg == 1:
            irany = 2
        else:
            irany = 1
    else:
        if sebesseg == 1:
            irany = -2
        else:
            irany = -2
input.on_button_pressed(Button.B, on_button_pressed_b)

sebesseg = 0
irany = 0
forgas = 1
irany = 2
sebesseg = 2
basic.show_icon(IconNames.HEART)
basic.pause(1000)

def on_forever():
    global forgas
    while True:
        basic.pause(100)
        forgat(forgas)
        basic.pause(100)
        forgas += irany
        if forgas > 9:
            forgas = 1
        if forgas < 1:
            forgas = 9
basic.forever(on_forever)
