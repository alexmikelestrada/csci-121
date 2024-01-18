from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()
drone.set_drone_LED(255,255,255,255)
drone.drone_buzzer(Note.E4, 200)
drone.drone_buzzer(Note.E4, 200)
drone.drone_buzzer(Note.E4, 250)

drone.drone_buzzer(Note.C4, 250)
drone.drone_buzzer(Note.E4, 350)
drone.drone_buzzer(Note.G4, 350)
drone.drone_buzzer(Note.G3, 400)
time.sleep(.5)

drone.drone_buzzer(Note.C4, 300)
drone.drone_buzzer(Note.G3, 300)
drone.drone_buzzer(Note.E3, 300)
time.sleep(.25)

drone.drone_buzzer(Note.A3, 300)
drone.drone_buzzer(Note.B3, 300)
drone.drone_buzzer(Note.B2, 150)
drone.drone_buzzer(Note.A3, 150)

drone.drone_buzzer(Note.G3, 165)
drone.drone_buzzer(Note.E4, 165)
drone.drone_buzzer(Note.G4, 165)
drone.drone_buzzer(Note.A4, 165)

drone.drone_buzzer(Note.F4, 200)
drone.drone_buzzer(Note.G4, 175)
drone.drone_buzzer(Note.E4, 200)
drone.drone_buzzer(Note.C4, 200)
drone.drone_buzzer(Note.D4, 150)
drone.drone_buzzer(Note.B3, 150)
time.sleep(.5)

drone.drone_buzzer(Note.G4, 200)
drone.drone_buzzer(Note.F5, 200)
drone.drone_buzzer(Note.F4, 200)
drone.drone_buzzer(Note.D4, 200)
drone.drone_buzzer(Note.E4, 200)
time.sleep(.2)
drone.drone_buzzer(Note.G3, 200)
drone.drone_buzzer(Note.A3, 200)
drone.drone_buzzer(Note.C4, 200)

drone.drone_buzzer(Note.A4, 200)
drone.drone_buzzer(Note.C4, 200)
drone.drone_buzzer(Note.D4, 200)

drone.drone_buzzer(Note.G4, 200)
drone.drone_buzzer(Note.F3, 200)
drone.drone_buzzer(Note.F4, 200)
drone.drone_buzzer(Note.D4, 200)
drone.drone_buzzer(Note.E4, 200)

drone.drone_buzzer(Note.C5, 200)
time.sleep(.2)
drone.drone_buzzer(Note.C5, 200)
drone.drone_buzzer(Note.C5, 200)

drone.close()
