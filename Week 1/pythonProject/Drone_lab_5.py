from codrone_edu.drone import *


drone = Drone()
drone.pair()
drone.set_drone_LED(255,255,255,255)
drone.takeoff()

for x in range(0, 4, 1):
    drone.set_pitch(25)
    drone.move(1)
    drone.set_throttle(70)
    drone.move(.75)
    drone.set_throttle(-40)
    drone.move(.75)
    drone.set_throttle(-20)

drone.land()
