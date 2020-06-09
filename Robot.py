from gpiozero import Motor
from gpiozero import DistanceSensor
from time import sleep

motor = Motor(forward=12, backward=18)
motorb = Motor(forward=19, backward=13)
sensor = DistanceSensor(23, 24)

while True:
    if sensor.distance < 0.3:
        motor.forward()
        motorb.backward()
        sleep(0.2)
    else:
        motorb.forward()
        motor.forward()
        sleep(0.2)

  # https://gpiozero.readthedocs.io/en/stable/recipes.html#distance-sensor
