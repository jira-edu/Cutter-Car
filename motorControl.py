from machine import Pin, PWM

class Motor:
    current_speed = 0
    
    def __init__(self, pwmPin, rl1, rl2):
        self.pin = pwmPin
        self.rl1 = Pin(rl1, Pin.OUT)
        self.rl1.value(0)
        self.rl2 = Pin(rl2, Pin.OUT)
        self.rl2.value(0)
        self.pwm = PWM(Pin(pwmPin), freq=25000, duty=0)
    
    def speed2duty(self, speed):        
        return int((speed/100)*1023)
    
    def softStart(self, speed):
        
        if (self.current_speed < speed):
            self.current_speed+=5
        elif (self.current_speed > speed):
            self.current_speed-=5

        if (self.current_speed < 0):
            self.current_speed = 0
        elif (self.current_speed > 100):
            self.current_speed = 100
            
        duty = self.speed2duty(self.current_speed)
        self.pwm.duty(duty)
    
    def forward(self, speed):
        self.rl1.value(1)
        self.rl2.value(0)
        
        self.softStart(speed)
        
    def backward(self, speed):
        self.rl1.value(0)
        self.rl2.value(1)
        
        self.softStart(speed)
    
    def stop(self):
        self.rl1.value(0)
        self.rl2.value(0)
        
        self.current_speed = 0
        self.pwm.duty(0)
