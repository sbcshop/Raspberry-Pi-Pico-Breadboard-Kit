# Raspberry Pi Pico Breadboard Kit

Raspberry Pi Pico Breadboard Kit is a multi-purpose Kit that consists of a “400 points half-size breadboard” on top,  a Programmable Buzzer, 4 Programmable LEDs, 4 Push buttons, and dedicated 5V, 3v3, and GND pins at a single place.
<img src="https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/images/product-pic1.png" />
## How to use ?

### Board Details :

* Push buttons :  Not pressed = Logic 0 , Pressed = Logic 1 (INPUT)
* Led          :  LED On = 1, LED Off = 0 (OUTPUT)
* Buzzer       :  Buzzer On = 1, Buzzer Off = 0 (OUTPUT)

### Requirements

* Raspberry Pi Pico Breadboard Kit (Buy it from : https://shop.sb-components.co.uk/collections/latest-collections/products/pico-breadboard-kit )
* Raspberry Pi Pico (Buy it from : https://shop.sb-components.co.uk/collections/latest-collections/products/raspberry-pi-pico-board-with-header )
* USB Cable
* Jumper Cables

### Steps :

* Connect Raspberry Pi Pico on female header of Pico Breadboard Kit.
* Connect USB cable on Raspberry Pi Pico USB port.
* Use jumper cables to connect Switches , Led's and Buzzer with Raspberry Pi Pico GPIO headers.
  
  <img src="https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/images/pico_breadboard_example.jpg" />

  Connections used here, GP0 -> LED 1 , GP4 -> Button 1 & GP8 -> Buzzer
  
* Now use example code "main.py" from pico breadboard kit's github repository in any micropython supported ide (preferred thonny ide). Find more codes in [examples folder](https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/tree/main/examples)
* Download and open code in Thonny IDE, transfer [main.py](https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/main.py) and [PicoBreadboard.py](https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/PicoBreadboard.py) file into Pico/Pico W.
  
  <img src="https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/images/file_view.png" />
  
* Choose interpreter as MicroPython (Raspberry Pi pico) with suitable com port shown.
* Click on green play button to run example on Pico Breadboard Kit.

Note: External components can be connected with Pico Breadboard kit via 400 points breadboard. 
