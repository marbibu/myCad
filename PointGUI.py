class PointGUI:
      __r=6
      def __init__(s,C,point):
            #Dane:
            s.__C=C
            s.__point=point
            #Definicje:
            s.__draw()
      def __draw(s):#Rysuje punkt:
            x,y=s.__point.getXY()
            s.__tag=s.__C.create_oval(x-s.__r,y-s.__r,x+s.__r,y+s.__r,fill="gold",outline="orange")