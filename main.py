from PicoBreadboard import LED,BUZZER,BUTTON
import time

#create object for various class
LED1 = LED(0) #create object for LED class, LED connected at GP0
BT1 = BUTTON(4) # Button connected at GP4
buzzer = BUZZER(8) # Buzzer connected at GP8

while 1:
   if BT1.read() == 1: #button pressed
       LED1.on()   #led 1 on
       buzzer.on() # buzzer on
       print("LED 1 ON")
   else :
       LED1.off()
       buzzer.off()
       print("Press Button 1")
       
   time.sleep(0.5) # delay 500ms
   

