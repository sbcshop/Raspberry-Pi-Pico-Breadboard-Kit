# Raspberry Pi Pico Breadboard Kit

Raspberry Pi Pico Breadboard Kit is a multi-purpose Kit that consists of a “400 points half-size breadboard” on top,  a Programmable Buzzer, 4 Programmable LEDs, 4 Push buttons, and dedicated 5V, 3v3, and GND pins at a single place. 
<img src="https://cdn.shopify.com/s/files/1/1217/2104/files/3_34.jpg?v=1727091986" />

Kit is compatible with all Raspberry Pi Pico variants - [Pico](https://shop.sb-components.co.uk/collections/latest-collections/products/raspberry-pi-pico-board-with-header), [Pico W](https://shop.sb-components.co.uk/products/raspberry-pi-pico-wh?variant=40047914090579) and latest [Pico 2](https://shop.sb-components.co.uk/products/raspberry-pi-pico-2-with-header?_pos=3&_sid=fbb911a5d&_ss=r)

### Requirements

* Raspberry Pi Pico Breadboard Kit (Buy it from : https://shop.sb-components.co.uk/collections/latest-collections/products/pico-breadboard-kit )
OR
* Raspberry Pi Pico 2 Breadboard Kit (Buy it from : https://shop.sb-components.co.uk/products/raspberry-pi-pico-2-breadboard-kit )
* USB Cable
* Few Jumper Cables
  
## How to use ?

### Board Details :

* Push buttons :  Not pressed = Logic 0 , Pressed = Logic 1 (INPUT)
* Led          :  LED On = 1, LED Off = 0 (OUTPUT)
* Buzzer       :  Buzzer On = 1, Buzzer Off = 0 (OUTPUT)

### Steps 1 : How to Install Boot Firmware in Pico
- If your Pico is already loaded with boot firmware, you can skip this and proceed to [step 2](https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/tree/main#steps-2--run-examples) for testing examples.
- To determine whether firmware is already present, simply connect your Pico to your laptop without pushing the boot button; if no additional device is detected and only some sound is heard, firmware is present.
- If you connect the pico to a laptop without pushing the boot button and it displays a mass storage device named "RPI-RP2" as seen below, the firmware is not installed.
- If BOOT firmware missing, then you will have to add **MicroPython firmware** in Pico of Breadboard kit. Select and download suitable firmware for your corresponding pico board,
  - For Pico => [Pico_firmware.uf2](https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/Pico_firmware.uf2)
  - For Pico W => [PicoW_firmware.uf2](https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/Pico_firmware.uf2)
  - For Pico 2 => [Pico2_Firmware.uf2](https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/Pico_firmware.uf2)  
- First, you need to *Press and Hold* the **BOOT** button, and then, without releasing the button, connect it to PC/laptop using micro usb. Check below image for reference,

  <img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/pico_bootmode.gif" width="340" height="228">

- Now your device is in boot mode, and you will see a new mass storage device named "RPI-RP2" as shown in the below figure.
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>  
- Drag and drop the MicroPython UF2 - ["Firmware.uf2"]() file downloaded previously for pico from this github onto the RPI-RP2 volume. Reference image shown below how to transfer any UF2 file or you can copy paste as well. Device will reboot and you are now running MicroPython. 
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/firmware_installation.gif" />
- Once Boot Firmware loaded now we can proceed to test sample example scripts on breadboard kit with Pico, please below steps for these.
  
### Steps 2 : Run Examples

* Connect Raspberry Pi Pico on female header of Pico Breadboard Kit.
* Connect USB cable on Raspberry Pi Pico USB port.
* Use jumper cables to connect Switches , Led's and Buzzer with Raspberry Pi Pico GPIO headers.
  
  <img src="https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/images/pico_breadboard_example.jpg" />

  Connections used here, GP0 -> LED 1 , GP4 -> Button 1 & GP8 -> Buzzer
  
* Now use example code "main.py" from pico breadboard kit's github repository in any micropython supported ide (preferred thonny ide). Find more codes in [examples folder](https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/tree/main/examples)
* Download and open code in Thonny IDE, transfer [main.py](https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/main.py) and [PicoBreadboard.py](https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/PicoBreadboard.py) file into Pico/Pico W.
* Similarly you can try other [examples](https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/tree/main/examples) just make sure to save whatever script using as main.py into Pico for standalone execution.
  
  <img src="https://github.com/sbcshop/Raspberry-Pi-Pico-Breadboard-Kit/blob/main/images/file_view.png" />
  
* Choose interpreter as MicroPython (Raspberry Pi pico) with suitable com port shown.
* Click on green play button to run example on Pico Breadboard Kit.

Note: External components can be connected with Pico Breadboard kit via 400 points breadboard. 

## Other Resources
  * [MicroPython getting started for RPi Pico boards](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Getting Started with Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)
  * [Pico/Pico W - RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)
  * [Pico 2 - RP2350 Datasheet](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf)


## Related Products
 ![3vPicoRelayBoard](https://cdn.shopify.com/s/files/1/1217/2104/products/3vPicoRelayBoard.png?v=1617884866&width=200)
 
 * [2 Channel Relay Board](https://shop.sb-components.co.uk/products/pico-3v-relay-hat?_pos=1&_sid=82fa60545&_ss=r) - Compatible Relay Hat for PiCoder 
 
 ![1.14” LCD HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/6_c64376c7-a257-43a3-bb5f-0a9471741a7d.png?v=1624017126&width=200)

 * [2 Channel Relay Board](https://shop.sb-components.co.uk/products/pico-3v-relay-hat?_pos=1&_sid=82fa60545&_ss=r) - Compatible Relay Hat for PiCoder 

 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
