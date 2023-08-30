from machine import Pin
import utime

button1 = Pin(16, Pin.IN)   #connect Button 1 on GP16

led1 = Pin(18, Pin.OUT)     #connect Led 1 on GP18
led2 = Pin(19, Pin.OUT)     #connect Led 2 on GP19
led3 = Pin(20, Pin.OUT)     #connect Led 3 on GP20
led4 = Pin(21, Pin.OUT)     #connect Led 4 on GP21

buz = Pin(17, Pin.OUT)      #connect Buzzer 4 on GP17

while 1:
    b1 = button1.value()    # Button Button Pressed = 1
    
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
