import time
import machine

LED = machine.Pin(16, machine.Pin.OUT)
PB = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)

nPress = 0

def onPress(pin):
    global nPress
    nPress += 1
    LED.toggle()
    time.sleep(0.2)
    LED.toggle()
    time.sleep(0.2)
    LED.toggle()
    time.sleep(0.2)
    LED.toggle()
    time.sleep(0.2)

PB.irq(trigger=machine.Pin.IRQ_FALLING, handler=onPress)  

while True:
    if(nPress % 3 == 0):
        LED.value(0)
        time.sleep(0.1)
    elif(nPress % 3 == 1):
        LED.toggle()
        time.sleep(2)
    elif(nPress % 3 == 2):
        LED.toggle()
        time.sleep(0.5)
    
        