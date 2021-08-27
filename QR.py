from pyqrcode import *
def qrgen(x):
    thing = create(x)
    thing.png(x+'.png', scale=10)
