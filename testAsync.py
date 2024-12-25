from machine import Pin
import asyncio

led = Pin(2, Pin.OUT)
sw1 = Pin(16, Pin.IN, Pin.PULL_UP)
sw2 = Pin(17, Pin.IN, Pin.PULL_UP)
sw3 = Pin(18, Pin.IN, Pin.PULL_UP)
sw4 = Pin(19, Pin.IN, Pin.PULL_UP)

async def blink1():
    while True:
        led.value(1)
        await asyncio.sleep(0.2)
        led.value(0)
        await asyncio.sleep(0.2)
        
async def print1():
    while True:
        print('Hello World!')
        await asyncio.sleep(2)

async def readInput():
   while True:
       LF = sw1.value()
       LB = sw2.value()
       RF = sw3.value()
       RB = sw4.value()
#       print(LF,LB,RF,RB)
       await asyncio.sleep(1)
       

async def main():
    asyncio.create_task(blink1())
    asyncio.create_task(print1())
    asyncio.create_task(readInput())

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()