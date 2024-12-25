from machine import Pin
import asyncio
import motorControl as motor
import time

led = Pin(2, Pin.OUT)
sw1 = Pin(16, Pin.IN, Pin.PULL_UP)
sw2 = Pin(17, Pin.IN, Pin.PULL_UP)
sw3 = Pin(18, Pin.IN, Pin.PULL_UP)
sw4 = Pin(19, Pin.IN, Pin.PULL_UP)
emerSw = Pin(4, Pin.IN, Pin.PULL_UP)

motor1 = motor.Motor(23, 25, 26)
motor1.stop()
motor2 = motor.Motor(27, 32, 33)
motor2.stop()

async def blink1():
    while True:
        led.value(1)
        await asyncio.sleep(0.5)
        led.value(0)
        await asyncio.sleep(0.5)

async def readInput():
   while True:
       if (emerSw.value() == 0):
           loop.stop()
           
       await asyncio.sleep(0.2)
       
async def controlTask():
    print('Start')
    while True:
#         motor2.forward(100)
        if (sw1.value() == 0):
            motor1.forward(50)
        elif (sw2.value() == 0):
            motor1.backward(50)
        else:
            motor1.stop()
            
        if (sw3.value() == 0):
            motor2.forward(50)
        elif (sw4.value() == 0):
            motor2.backward(50)
        else:
            motor2.stop()
            
        await asyncio.sleep(0.1)   
        
async def main():
    asyncio.create_task(blink1())
    asyncio.create_task(readInput())
    asyncio.create_task(controlTask())

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()

motor1.stop()
motor2.stop()
led.value(1)
while True:
    print('Emergency Stop!!!')
    time.sleep(1)

