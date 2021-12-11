import easygui
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from easygui import *
import math
"""
d=enterbox("Adja meg a kör átmérőjét! ", title="atmero")
d=int(d)
r=d/2
if d>0:

    ker=2*r*math.pi
    ter=r**2*math.pi


else:
    easygui.msgbox("Hibás adatot adtál meg!!!!!",title="Error")


c=plt.Circle((0,0),r)
show()
"""
try:
    diameter_str=easygui.enterbox("Átmérő(cm)",title="Adatbekérés")
    diameter=float(diameter_str)
    if diameter>0:
        radius=diameter/2
        ker = 2 * radius * math.pi
        ter = radius ** 2 * math.pi
        easygui.msgbox("A {} cm{:.3f} {:.3f}".format(diameter,ker,ter))
    else:
        easygui.msgbox("Nem jo",title="error")
except:
    easygui.msgbox("Nem megfelelő az érték",title="Error")



try:
    ev=int(easygui.enterbox("Évszám",title="év"))
    if ev % 4 ==0:
        if ev%100==0:
            if ev%400==0:
                easygui.msgbox("szövőév")
            else:
                easygui.msgbox("Nem szökőév")
        else:
            easygui.msgbox("szökőév")
    else:
        easygui.msgbox("Nem szökőév")
except:
    easygui.msgbox("Hibás bemenet")