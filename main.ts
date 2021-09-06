input.onButtonPressed(Button.A, function () {
    my_temp += -1
    basic.showNumber(my_temp)
})
input.onButtonPressed(Button.B, function () {
    my_temp += 1
    basic.showNumber(my_temp)
})
let my_temp = 0
my_temp = 20
basic.showNumber(my_temp)
basic.forever(function () {
    if (input.temperature() < my_temp) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        pins.digitalWritePin(DigitalPin.P1, 0)
    } else if (input.temperature() > my_temp) {
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
})
