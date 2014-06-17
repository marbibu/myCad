from PointGUI import PointGUI
from PathGUI import PathGUI

from Tkinter import Canvas
class Desk:
      def __init__(s,master):
            #Dane:
            s.__master=master
            #Definicje:
            s.__draw()
      def __draw(s):#Rysuje kontrolke
            s.__C=Canvas(s.__master,highlightthickness=0,bg="gray80")
            s.__C.pack(side="top",expand=1,fill="both")
      def getC(s):#Zwraca id Canvasu
            return s.__C
      def addPoint(s,point):#Dodaje punkt do Desk
            PointGUI(s.__C,point)
      def addPath(s,path):#Dodaje sciezke do Desk
            PathGUI(s.__C,path)
      