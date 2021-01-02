def on_button_pressed_a():
    global irany
    if irany > 0:
        irany = -1
    else:
        irany = 1
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
    if num == 2:
        basic.show_leds("""
            # . . . .
            . # . . .
            . . # . .
            . . . # .
            . . . . #
            """)
    if num == 3:
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            . . . . .
            . . . . .
            """)
    if num == 4:
        basic.show_leds("""
            . . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            """)

def on_button_pressed_b():
    basic.show_icon(IconNames.HEART)
    basic.pause(500)
input.on_button_pressed(Button.B, on_button_pressed_b)

irany = 0
forgas = 1
irany = 1
basic.show_icon(IconNames.HEART)
basic.pause(1000)

def on_forever():
    global forgas
    while True:
        basic.pause(100)
        forgat(forgas)
        basic.pause(100)
        forgas += irany
        if forgas > 4:
            forgas = 1
        if forgas < 1:
            forgas = 4
basic.forever(on_forever)
