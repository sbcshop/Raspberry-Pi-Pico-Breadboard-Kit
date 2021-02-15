from machine import Pin
import utime

button1 = Pin(16, Pin.IN)

led1 = Pin(18, Pin.OUT)
led2 = Pin(19, Pin.OUT)
led3 = Pin(20, Pin.OUT)
led4 = Pin(21, Pin.OUT)

buz = Pin(17, Pin.OUT)

while 1:
    b1 = button1.value()
    
    led1.toggle()
    led2.toggle()
    led3.toggle()
    led4.toggle()
    
    buz.toggle()
    
    if b1:
        print('Button 1 pressed!')
        utime.sleep(0.5)
    else:
        print('Button 1 Released!')
        utime.sleep(0.5)
        
    utime.sleep(0.5)
