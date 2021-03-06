from microbit import * #importing packages
import radio


radio.config(queue=5, length=32, channel=7, power=6, address=0x75626974, group=0, data_rate=radio.RATE_1MBIT) #setting radio's settings
radio.on() #radio is on

while True: #pretty much while microbit is on

    display.scroll("A for send B for receive", delay=200, wait=True, monospace=False) #display info

    if button_a.was_pressed(): #tests if button A was pressed and if it is sends a string to other radio's in same channel
            radio.send("Msg from ID:01")

    if button_b.was_pressed(): #tests if button B was pressed and displays the msg received
        msg = radio.receive()
        display.scroll(msg, delay=200, wait=True, monospace=False)
