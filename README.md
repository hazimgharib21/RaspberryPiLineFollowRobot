# Raspberry Pi Line Follow Robot

This robot is develop for TVET Line Follow Competition. We did't win anything but we learn a lot from it

## Getting Started

This code only work with the hardware that we have right now. If you want to use it, just clone this repo and change where you need to.

### Hardware

Here are the hardware that we use for this robot

* [30:1 Micro Metal Gearmotor](https://www.cytron.io/c-84-dc-motor/c-91-dc-geared-motor/c-292-spg10-xx/p-spg10-30k)
* [Auto Calibrating Line Sensor](https://www.cytron.io/c-85-sensor/c-101-photoelectric-line-sensor/p-lss05https://www.cytron.io/c-85-sensor/c-101-photoelectric-line-sensor/p-lss05)
* [Cytron 2x10A Motor Driver HAT for RPI](https://www.cytron.io/p-hat-mdd10)
* [DC-DC Mobile Charger 5V3A](https://www.cytron.io/c-87-power/c-508-switching-module/p-dc-dc-5v3a) - to power up raspberry pi from lipo battery
* [Raspberry Pi Zero W](https://www.cytron.io/c-442-raspberry/c-445-main-board/p-rpi-zero-w)
* [LIPO Battery 7.4vV 900mAH](https://www.cytron.io/c-87-power/c-97-lipo-rechargeable-battery-and-charger/p-lip-7.4-900)


### Installing

There are no installation required since python 2.7 is already install in the latest Rapsbian release. Just download the code and run the main program.

### Wiring

You can refer [here](https://pinout.xyz/pinout/pin3_gpio2) for raspberry pi pinout in BCM layout.

BCM pin 11, 9, 10, 22 and 27 use for line sensor.
BCM pin 26 and 24 for motor direction and BCM pin 12 and 13 for motor PWM.
BCM pin 5 for pushbutton.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Here are various links we refer for programming this robot.

* [Line position calculation for digital line sensor](http://waihung.net/pid-line-following-robot/)
* [Implementation of PID control in python](https://github.com/ivmech/ivPID/blob/master/PID.py)
* Lecturers, alumni, seniors and teammates that give great inputs in perfecting this robot.
