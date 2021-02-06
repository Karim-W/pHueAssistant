import tkinter as tk
from phue import Bridge
import math
b = Bridge('192.168.0.104')
b.connect()
r = tk.Tk()


def convertColor(hexCode):
    R = int(hexCode[:2], 16)
    G = int(hexCode[2:4], 16)
    B = int(hexCode[4:6], 16)

    total = R + G + B

    if R == 0:
        firstPos = 0
    else:
        firstPos = R / total

    if G == 0:
        secondPos = 0
    else:
        secondPos = G / total

    return [firstPos, secondPos]


def myFunc():
    b.set_light(1, 'on', True)


def turnOff():
    b.set_light(1, 'on', False)


def brit():
    b.set_light(1, 'bri', math.floor(254*0.25))


def brihalf():
    b.set_light(1, 'bri', math.floor(254*0.5))


def brit3q():
    b.set_light(1, 'bri', math.floor(254*0.75))


def britmax():
    b.set_light(1, 'bri', 254)


def redHue():
    #b.set_light(1, 'hue', 5300)
    b.set_light(1, 'xy', convertColor('E00031'))
# 552D9F


def blueHue():
    #b.set_light(1, 'hue', 5300)
    b.set_light(1, 'xy', convertColor('0000B8'))


def purpleHue():
    b.set_light(1, 'xy', convertColor('3C1361'))


r.title('Hue Controller')
onButton = tk.Button(r, text='turn on', width=25, command=myFunc)
onButton.pack()
offButton = tk.Button(r, text='turn off', width=25, command=turnOff)
offButton.pack()
fouthBrit = tk.Button(r, text='25%', width=25, command=brit)
fouthBrit.pack()
halfBrit = tk.Button(r, text='50%', width=25, command=brihalf)
halfBrit.pack()
threeBrit = tk.Button(r, text='75%', width=25, command=brit3q)
threeBrit.pack()
threeBrit = tk.Button(r, text='100%', width=25, command=britmax)
threeBrit.pack()
redButt = tk.Button(r, text='RED', width=25, command=redHue)
redButt.pack()

blueButt = tk.Button(r, text='Trypan Blue', width=25, command=blueHue)
blueButt.pack()
purpleButt = tk.Button(r, text='Purple', width=25, command=purpleHue)
purpleButt.pack()


r.mainloop()
