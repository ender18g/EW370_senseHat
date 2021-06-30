from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.clear()
steps = 0


def get_rand_color():
    return [randint(1, 255), randint(1, 255), randint(1, 255)]


while True:
    accelerometer_data = sense.get_accelerometer_raw()
    x = accelerometer_data['x']
    y = accelerometer_data['y']
    z = accelerometer_data['z']

    print(f"{x:.2f} {y:.2f} {z:.2f}", end='\r')

    if x > .6:
        steps += 1
        sense.show_letter('+', text_colour=get_rand_color())
        sleep(.1)
        sense.clear()
        # sense.show_message(str(steps), text_colour=(
        #     randint(1, 255), randint(1, 255), randint(1, 255)))
        # steps += 1
