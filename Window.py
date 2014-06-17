from Tkinter import Tk
class Window:
      def __init__(s,title,x,y,w,h):
            #Dane:
            s.__title=title
            s.__x,s.__y=x,y
            s.__w,s.__h=w,h
            #Definicje:
            s.__draw()
      def __draw(s):#Rysuje okno
            s.__master=Tk()
            s.__master.geometry("%sx%s+%s+%s"%(s.__w,s.__h,s.__x,s.__y))
            s.__master.title(s.__title)
      def getMaster(s):#Zwraca id okna
            return s.__master
      def loop(s):#Zapetla wyswietlanie okna
            s.__master.mainloop()
            