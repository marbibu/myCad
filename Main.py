from Window import Window
from Desk import Desk

from Point import Point
from Path import Path

class Main:
      def __init__(s):
            #Dane:
            win=Window("Point",0,0,600,600)
            master=win.getMaster()
            desk=Desk(master)
            C=desk.getC()
            
            
            p1=Point(100,100)
            p2=Point(200,100)
            p3=Point(200,200)
            p4=Point(100,200)
            
            desk.addPoint(p1)
            desk.addPoint(p2)
            desk.addPoint(p3)
            desk.addPoint(p4)
            
            path=Path()
            path.addPoint(p1)
            path.addPoint(p2)
            path.addPoint(p3)
            path.addPoint(p4)
            
            desk.addPath(path)
            
            
            win.loop()
Main()
#Pytania
#Gdzie bedziemy tworzyc obiekty GUI? moze w Desk?