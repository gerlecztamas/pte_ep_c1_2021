from easygui import *

user_response=msgbox("Hello world", title="Hello", ok_button="hi", image="python_logo.png")
print(user_response)
"""
flavor=buttonbox("Melyik a kedvenc fagylaltod?", title="fagylalt",choices=["Vanilia","Csoki","Puncs"], images="python_logo.png",default_choice="Csoki")
print(flavor) """
"""
flavor=choicebox("Melyik a kedvenc fagylaltod?", title="fagylalt",choices=["Vanilia","Csoki","Puncs"], preselect= 1)
"""
flavor=enterbox("Melyik a kedvenc fagylaltod?", title="fagylalt", default="mentás csoki", image="python_logo.png")
if flavor is not None:
    msgbox("A válaszott fagylalt íz: "+flavor)
else:
    print("Nem választottál")