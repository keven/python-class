from time import sleep
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)

w = (255, 255, 255)
b = (0, 0, 0)
y = (255, 255, 0)
picture = [
    w, w, y, y, y, y, w, w,
    w, y, y, y, y, y, y, w,
    b, b, b, b, b, b, b, b,
    y, b, b, y, y, b, b, y,
    y, y, y, y, y, y, y, y,
    y, y, b, y, y, b, y, y,
    w, y, y, b, b, y, y, w,
    w, w, y, y, y, y, w, w,
]

sense.set_pixels(picture)
sleep(2)
