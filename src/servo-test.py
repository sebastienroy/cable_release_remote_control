import time
from servo import Servo
my_servo = Servo(pin=1)
my_servo.move(0)
time.sleep(2.0)
my_servo.move(60)
time.sleep(2.0)
my_servo.move(90)