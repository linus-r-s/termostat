def on_button_pressed_a():
    global my_temp
    my_temp += -1
    basic.show_number(my_temp)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global my_temp
    my_temp += 1
    basic.show_number(my_temp)
input.on_button_pressed(Button.B, on_button_pressed_b)

my_temp = 0
my_temp = 20
basic.show_number(my_temp)

def on_forever():
    if input.temperature() < my_temp:
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 0)
    elif input.temperature() > my_temp:
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever)
