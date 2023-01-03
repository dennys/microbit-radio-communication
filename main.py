def on_button_pressed_a():
    radio.send_string("GOOD MORNING")
    music.play_melody("C C G G A A G G ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
    basic.show_icon(IconNames.YES)
    basic.clear_screen()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("hihi")
    music.play_melody("F F E E D D C C ", 120)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
""")
radio.set_group(1)