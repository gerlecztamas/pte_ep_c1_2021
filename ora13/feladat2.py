import easygui
from easygui import *

a=buttonbox("Gondoljon egy számra 1 és 99 között, 6 próbálkozása van",choices=["Induljon a játék"])
b=int(easygui.enterbox("Adja le a tippjét!",ok_button="Tipp"))