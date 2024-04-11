input.onButtonPressed(Button.A, function () {
    p1 = randint(0, 4)
    if (p1 == 0) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (p1 == 1) {
        basic.showIcon(IconNames.Scissors)
    } else if (p1 == 2) {
        basic.showIcon(IconNames.Square)
    } else if (p1 == 3) {
        basic.showIcon(IconNames.Cow)
    } else if (p1 == 4) {
        basic.showLeds(`
            . # # # #
            . # # . .
            . # # # #
            . # # . .
            . # # . .
            `)
    }
})
input.onButtonPressed(Button.AB, function () {
    if (p1 != 5 && p2 != 5) {
        if (p1 == 0 && p2 == 4) {
            basic.clearScreen()
            basic.showString("p1 win!")
        } else if (p1 == 0 && p2 == 1) {
            basic.clearScreen()
            basic.showString("p1 win!")
        } else if (p1 == 1 && p2 == 2) {
            basic.clearScreen()
            basic.showString("p1 win!")
        } else if (p1 == 1 && p2 == 4) {
            basic.clearScreen()
            basic.showString("p1 win!")
        } else if (p1 == 2 && p2 == 0) {
            basic.clearScreen()
            basic.showString("p1 win!")
        } else if (p1 == 2 && p2 == 3) {
            basic.clearScreen()
            basic.showString("p1 win!")
        } else if (p1 == 3 && p2 == 1) {
            basic.clearScreen()
            basic.showString("p1 win!")
        } else if (p1 == 3 && p2 == 0) {
            basic.clearScreen()
            basic.showString("p1 win!")
        } else if (p1 == 4 && p2 == 2) {
            basic.clearScreen()
            basic.showString("p1 win!")
        } else if (p1 == 4 && p2 == 3) {
            basic.clearScreen()
            basic.showString("p1 win!")
        } else if (p2 == 0 && p1 == 4) {
            basic.clearScreen()
            basic.showString("p2 win!")
        } else if (p2 == 0 && p1 == 1) {
            basic.clearScreen()
            basic.showString("p2 win!")
        } else if (p2 == 1 && p1 == 2) {
            basic.clearScreen()
            basic.showString("p2 win!")
        } else if (p2 == 1 && p1 == 4) {
            basic.clearScreen()
            basic.showString("p2 win!")
        } else if (p2 == 2 && p1 == 0) {
            basic.clearScreen()
            basic.showString("p2 win!")
        } else if (p2 == 2 && p1 == 3) {
            basic.clearScreen()
            basic.showString("p2 win!")
        } else if (p2 == 3 && p1 == 1) {
            basic.clearScreen()
            basic.showString("p2 win!")
        } else if (p2 == 3 && p1 == 0) {
            basic.clearScreen()
            basic.showString("p2 win!")
        } else if (p2 == 4 && p1 == 2) {
            basic.clearScreen()
            basic.showString("p2 win!")
        } else if (p2 == 4 && p1 == 3) {
            basic.clearScreen()
            basic.showString("p2 win!")
        } else if (p1 == p2) {
            basic.clearScreen()
            basic.showString("draw!")
        }
    } else {
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.B, function () {
    p2 = randint(0, 4)
    if (p2 == 0) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (p2 == 1) {
        basic.showIcon(IconNames.Scissors)
    } else if (p2 == 2) {
        basic.showIcon(IconNames.Square)
    } else if (p2 == 3) {
        basic.showIcon(IconNames.Cow)
    } else if (p2 == 4) {
        basic.showLeds(`
            . # # # #
            . # # . .
            . # # # #
            . # # . .
            . # # . .
            `)
    }
})
input.onGesture(Gesture.Shake, function () {
    p1 = 5
    p2 = 5
})
let p2 = 0
let p1 = 0
p1 = 5
p2 = 5
