from PicoBreadboard import LED,BUZZER,BUTTON
import time

LED1 = LED(0)
LED2 = LED(1)
LED3 = LED(2)
LED4 = LED(3)

BT1 = BUTTON(4)
BT2 = BUTTON(5)
BT3 = BUTTON(6)
BT4 = BUTTON(7)

buzzer = BUZZER(8)

while 1:
   if BT1.read() == 1:
       LED1.on()   #led 1 on
       buzzer.on() # buzzer on
       print("LED 1 ON")

   elif BT2.read() == 1:
       LED2.on()   #led 2 on
       buzzer.on() # buzzer on
       print("LED 2 ON")

   elif BT3.read() == 1:
       LED3.on()   #led 3 on
       buzzer.on() # buzzer on
       print("LED 3 ON")

   elif BT4.read() == 1:
       LED4.on()   #led 4 on
       buzzer.on() # buzzer on
       print("LED 4 ON")
       
   else:
       LED1.off() #led 1 off
       LED2.off() #led 2 off
       LED3.off() #led 3 off
       LED4.off() #led 4 off
       buzzer.off() #buzzer off
       
   time.sleep(0.05) # delay 50ms
   
