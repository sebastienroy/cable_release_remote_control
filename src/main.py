from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(1))
pwm.freq(50)
led = Pin("LED")

while True:
    led.toggle()
    pwm.duty_u16(1000)
    sleep(1)
    pwm.duty_u16(9000)
    sleep(1)

    
while(True):    
    for position in range(1000,9000,200):
        pwm.duty_u16(position)
        sleep(0.01)
    for position in range(9000,1000,-200):
        pwm.duty_u16(position)
        sleep(0.01)
        