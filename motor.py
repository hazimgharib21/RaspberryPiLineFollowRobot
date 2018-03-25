# -----------------------------------------------------------------------------
# This class is for HAT-MDD10
# https://www.cytron.io/p-hat-mdd10
# -----------------------------------------------------------------------------

import RPi.GPIO as GPIO
import time

class motor:

    def __init__(self, motorDir1=26, motorDir2=24, motorPWM1=12, motorPWM2=13):

        self.pwm1 = motorPWM1
        self.pwm2 = motorPWM2
        self.dir1 = motorDir1
        self.dir2 = motorDir2

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        time.sleep(1)

        GPIO.setup(4,GPIO.OUT)
        GPIO.setup(self.pwm2, GPIO.OUT)
        GPIO.setup(self.pwm1, GPIO.OUT)
        GPIO.setup(self.dir1, GPIO.OUT)
        GPIO.setup(self.dir2, GPIO.OUT)
        GPIO.output(4,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(4,GPIO.LOW)
    

        self.motorSpeedLeft = 0.0
        self.motorSpeedRight = 0.0

        self.motor1 = GPIO.PWM(self.pwm1, 100)
        self.motor1.start(0)
        self.motor1.ChangeDutyCycle(0)

        self.motor2 = GPIO.PWM(self.pwm2, 100)
        self.motor2.start(0)
        self.motor2.ChangeDutyCycle(0)


    # move the motor
    def move(self):
        
        if(self.motorSpeedLeft < 0):
            self.motorSpeedLeft = 0 - self.motorSpeedLeft
            GPIO.output(self.dir1, GPIO.HIGH)
            self.motor1.ChangeDutyCycle(self.motorSpeedLeft)
        elif(self.motorSpeedLeft >= 0):
            GPIO.output(self.dir1, GPIO.LOW)
            self.motor1.ChangeDutyCycle(self.motorSpeedLeft)

        if(self.motorSpeedRight < 0):
            self.motorSpeedRight = 0 - self.motorSpeedRight
            GPIO.output(self.dir2, GPIO.LOW)
            self.motor2.ChangeDutyCycle(self.motorSpeedRight)
        elif(self.motorSpeedRight >= 0):
            GPIO.output(self.dir2, GPIO.HIGH)
            self.motor2.ChangeDutyCycle(self.motorSpeedRight)

    # set left motor speed
    def setLeftMotorSpeed(self, leftSpeed):

        self.motorSpeedLeft = leftSpeed

    # set right motor speed
    def setRightMotorSpeed(self, rightSpeed):

        self.motorSpeedRight = rightSpeed

    # stop and cleanup pi GPIO
    def clear(self):
        self.motor1.ChangeDutyCycle(0)
        self.motor2.ChangeDutyCycle(0)
        GPIO.cleanup()




