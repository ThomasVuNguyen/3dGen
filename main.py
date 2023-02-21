import pyttsx3
import openpyscad as ops
from datetime import datetime
import os

name = input("What object do you want to create? ")
engine = pyttsx3.init()
engine.say("What object do you want to create? ")
engine.runAndWait()




def name_file():
    return "cadfile"

if name == "cube":
    c1=ops.Cube([10,20,12])
    name=name_file()
    print(name)
    c1.write(name+".scad")
    os.system('openscad -o 3dprint.stl '+name+'.scad')
    

    
    
