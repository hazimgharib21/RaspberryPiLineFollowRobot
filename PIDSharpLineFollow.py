# Import and setup for our shutdown button
import RPi.GPIO as GPIO
import os
buttonPin = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
input_state = True

# All the variable use for line follow
# Most of this variable will be re-initialize later
# So, every change must not be done here.
Kp = 25.0
Kd = 50.0
Ki = 0.0

lost = False
previousAvgSensor = 0.0
set_point = 4.0
error = 0.0
previousError = 0.0
totalError = 0.0

pwmLeft = 0.0
pwmRight = 0.0

maxSpeed = 30

# Import and initialize our robot library
import motor
import irSensor
import PID

motor = motor.motor()
lineSensor = irSensor.irSensor(11,9,10,22,27)
lineSensor.setSampleTime(0.01)
pid = PID.PID(Kp,Ki,Kd)
pid.setPoint(4.0)
pid.setSampleTime(0.01)

try:
    while input_state:

        input_state = GPIO.input(buttonPin) # Check the button state

        # use for line position calculation
        # we use digital sensor
        activeSensor = 0.0
        totalSensor = 0
    
        #Get sensor data
        lineSensor.update()
        sensors = lineSensor.output

        #loop through the sensor
        i = 0
        for sensor in sensors:
            i += 1
            if sensor == 1:
                activeSensor += 1
            totalSensor += sensor * (i+1)

        # if the sensor detect black line
        if activeSensor != 0:

            # re-initialize speed,PID and setPoint for normal line follow
            maxSpeed = 70
            pid.setKp(25.0)
            pid.setKd(50.0)
            set_point = 4.0

            # The position of the line
            avgSensor = totalSensor/activeSensor

            # Keep track when the sensor lost the line
            lost = False

        # if the sensor doesn't detect any line
        else:
            
            # Check if we lose the line before
            # we check because we want our robot to spin in one
            # direction when searching for the line. Thus, this
            # conditional part must run only once when the robot
            # first lost the line.
            if lost == False:

                # Changing the setpoint so that our robot will turn to where
                # the it last lost the line. If before it lost, it detect the line on the left
                # the robot will turn left to find the line back.
                if previousError < 0:
                    set_point = 4.0
                else:
                    set_point = -4.0

                # Re-initialize speed and PID for searching line.
                # This part is very important because of the hardware of our robot.
                # The robot was too heavy and the tire is not that grip.
                # the robot will lost the line everytime at the 90 degree turn.
                maxSpeed = 20
                pid.setKp(5.0)
                pid.setKd(00.0)

                # Keep track when the sensor lost the line
                lost = True
            
            # the average become zero when there are no line detected
            avgSensor = 0
        
        # Calculation in this part necessary for the 90 degree turn eventhought
        # the calculation of the pid is done inside of the pid class.
        previousError = error # save previous error for differential
        error = avgSensor - set_point # Count how much robot deviate from center
            
        # Calculation of the pid from the pid class
        pid.setPoint(set_point)
        pid.update(avgSensor)
        power = pid.output

        # set the speed of both motor according to the value from pid
        if(power<0):
            pwmRight = maxSpeed - abs(power)
            pwmLeft = maxSpeed + abs(power)
        else:
            pwmRight = maxSpeed + power
            pwmLeft = maxSpeed - power
    
        # A little correction if the robot doesn't move straight if both motor
        # turn the same speed
        pwmRight = pwmRight + 3

        # Constraint the speed between -100 and 100.
        if(pwmRight > 100):
            pwmRight = 100
        elif(pwmRight < -100):
            pwmRight = -100
        if(pwmLeft > 100):
            pwmLeft = 100
        elif(pwmLeft < -100):
            pwmLeft = -100

        # set the motor speed 
        motor.setLeftMotorSpeed(pwmLeft)
        motor.setRightMotorSpeed(pwmRight)

        # move the motor according to the speed given
        motor.move()

finally:
    # This part will run when the user push the button
    # it will stop the script and shutdown the pi.
    print "Goodbye :)"
    motor.clear()
    os.system('sudo halt')
