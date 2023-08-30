from machine import Pin,PWM
from utime import sleep

#class to control onboard LED
class LED():
    def __init__(self, led_pin_number):
        self.led_pin = Pin(led_pin_number, Pin.OUT)
    
    def on(self):
        self.led_pin.on()
    
    def off(self):
        self.led_pin.off()
        
# class to control Buzzer
class BUZZER():
    def __init__(self,buzzer_pin_number):
        self.buzzer_pin = Pin(buzzer_pin_number, Pin.OUT)
    
    def on(self):
        self.buzzer_pin.on()
    
    def off(self):
        self.buzzer_pin.off()
 
# class to read onboard Buttons value 
class BUTTON():
    def __init__(self, button_pin_number):
        """Initialize BUTTON.
        """    
        self.button_pin = Pin(button_pin_number, Pin.IN) 
            
    def read(self):
        """ provides button status value
            -> 0 (for Not Pressed)
            -> 1 (for Pressed)
        """
        return self.button_pin.value()

