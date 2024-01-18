from codrone_edu.drone import *
import math
import time

x = 0

drone = Drone()
drone.pair()
drone.set_drone_LED(255,255,255,255)
drone.takeoff()
alive = True
while alive == True:
    x += 1
    drone.set_pitch(math.sin(x * 100))
    drone.move(math.sin(x * 100))
drone.move(1)
drone.land()
