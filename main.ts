input.onButtonPressed(Button.A, function () {
    radio.sendString("GOOD MORNING")
    music.playMelody("C C G G A A G G ", 120)
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
    basic.showIcon(IconNames.Yes)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("hihi")
    music.playMelody("F F E E D D C C ", 120)
})
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    `)
radio.setGroup(1)
