from pyqrcode import *
def qrgen(x):
    thing = create(x)
    thing.png(file="Desktop", scale=6)
