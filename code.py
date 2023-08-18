import analogio 
import digitalio
import time
import board
import config


# voltage meter (12v/4v)
def get_voltage(pin):
    return ((pin.value * 3.3) / 65536) + 10.6 + 0.7

# voltage adc
analog_in = analogio.AnalogIn(board.GP27)

# configure LEDs
pwrLED = digitalio.DigitalInOut(board.GP9)
pwrLED.direction = digitalio.Direction.OUTPUT
pwrLED.value = True

relay = digitalio.DigitalInOut(board.GP20)
relay.direction = digitalio.Direction.OUTPUT
relay.value = False

while True:
    voltage = get_voltage(analog_in)
    if config.TriggerHigh is True:
        if voltage > config.Voltage:
            if relay.value is False:
                print("Triggered High")
                relay.value = True
                time.sleep(10)
        else:
            if relay.value is True:
                relay.value = False
                time.sleep(10)
    else:
        if voltage < config.Voltage:
            if relay.value is False:
                print("Triggered Low")
                relay.value = True
                time.sleep(10)
        else:
            if relay.value is True:
                relay.value = False
                time.sleep(10)
    time.sleep(0.05)