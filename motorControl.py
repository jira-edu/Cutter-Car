from machine import Pin, PWM

class Motor:
    current_duty = 0
    
    def __init__(self, pwmPin, rl1, rl2):
        self.pin = pwmPin
        self.rl1 = Pin(rl1, Pin.OUT)
        self.rl1.value(0)
        self.rl2 = Pin(rl2, Pin.OUT)
        self.rl2.value(0)
        self.pwm = PWM(Pin(self.pin), freq=25000, duty=0)
    
    def speed2duty(self, speed):        
        return int((speed/100)*1023)
    
    def softStart(self, speed):
        duty = self.speed2duty(speed)
        
        if (self.current_duty < duty):
            self.current_duty+=50
        elif (self.current_duty > duty):
            self.current_duty-=50

        if (self.current_duty < 0):
            self.current_duty = 0
        elif (self.current_duty > 1023):
            self.current_duty = 1023
            
        self.pwm.duty(self.current_duty)
    
    def forward(self, speed):
        self.rl1.value(1)
        self.rl2.value(0)
        
        softStart(speed)
        
    def backward(self, speed):
        self.rl1.value(0)
        self.rl2.value(1)
        
        softStart(speed)
    
    def stop(self):
        self.rl1.value(0)
        self.rl2.value(0)
        
        self.current_duty = 0
        self.pwm.duty(self.current_duty)
