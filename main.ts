//  A megnyomasara iranyt valt a forgas
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (irany > 0) {
        if (sebesseg == 1) {
            irany = -1
        } else {
            irany = -2
        }
        
    } else if (sebesseg == 1) {
        irany = 1
    } else {
        irany = 2
    }
    
})
function forgat(num: number) {
    if (num == 1) {
        basic.showLeds(`
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            `)
    }
    
    if (num == 3) {
        basic.showLeds(`
            # . . . .
            . # . . .
            . . # . .
            . . . # .
            . . . . #
            `)
    }
    
    if (num == 5) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            . . . . .
            . . . . .
            `)
    }
    
    if (num == 7) {
        basic.showLeds(`
            . . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            `)
    }
    
    if (irany > 0) {
        if (num == 2) {
            basic.showLeds(`
                . # . . .
                . # . . .
                . . # . .
                . . . # .
                . . . # .
                `)
        }
        
        if (num == 4) {
            basic.showLeds(`
                . . . . .
                # . . . .
                . # # # .
                . . . . #
                . . . . .
                `)
        }
        
        if (num == 6) {
            basic.showLeds(`
                . . . . .
                . . . # #
                . . # . .
                # # . . .
                . . . . .
                `)
        }
        
        if (num == 8) {
            basic.showLeds(`
                . . . # .
                . . # . .
                . . # . .
                . . # . .
                . # . . .
                `)
        }
        
    } else {
        if (num == 2) {
            basic.showLeds(`
                . # . . .
                . . # . .
                . . # . .
                . . # . .
                . . . # .
                `)
        }
        
        if (num == 4) {
            basic.showLeds(`
                . . . . .
                # # . . .
                . . # . .
                . . . # #
                . . . . .
                `)
        }
        
        if (num == 6) {
            basic.showLeds(`
                . . . . .
                . . . . #
                . # # # .
                # . . . .
                . . . . .
                `)
        }
        
        if (num == 8) {
            basic.showLeds(`
                . . . # .
                . . . # .
                . . # . .
                . # . . .
                . # . . .
                `)
        }
        
    }
    
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (irany > 0) {
        if (sebesseg == 1) {
            irany = 2
        } else {
            irany = 1
        }
        
    } else if (sebesseg == 1) {
        irany = -2
    } else {
        irany = -2
    }
    
})
let sebesseg = 0
let irany = 0
let forgas = 1
irany = 2
sebesseg = 2
basic.showIcon(IconNames.Heart)
basic.pause(1000)
basic.forever(function on_forever() {
    
    while (true) {
        basic.pause(100)
        forgat(forgas)
        basic.pause(100)
        forgas += irany
        if (forgas > 9) {
            forgas = 1
        }
        
        if (forgas < 1) {
            forgas = 9
        }
        
    }
})
