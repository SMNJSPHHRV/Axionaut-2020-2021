import Adafruit_PCA9685
import time

servo = Adafruit_PCA9685.PCA9685()
servo.set_pwm_freq(60)

while True: 
    servo.set_pwm(2,0,150)
    time.sleep(1)
    servo.set_pwm(2,0,175)
    time.sleep(1)
    servo.set_pwm(2,0,200)
    time.sleep(1)
    servo.set_pwm(2,0,225)
    time.sleep(1)
    servo.set_pwm(2,0,250)
    time.sleep(1)
    servo.set_pwm(2,0,275)
    time.sleep(1)
    servo.set_pwm(2,0,300)
    time.sleep(1)
    servo.set_pwm(2,0,325)
    time.sleep(1)
    servo.set_pwm(2,0,350)
    time.sleep(1)
    servo.set_pwm(2,0,375)
    time.sleep(1)
    servo.set_pwm(2,0,400)
    time.sleep(1)
    servo.set_pwm(2,0,350)
    time.sleep(1)
    servo.set_pwm(2,0,300)
    time.sleep(1)
    #print("3")
    #servo.set_pwm(0,0,307)
    #time.sleep(1)
    #print("4")
    time.sleep(5)
