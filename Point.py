from Sender import Sender
class Point(Sender):
      def __init__(s,x,y):
            #Dane:
            Sender.__init__(s)
            s.__x,s.__y=x,y
            s.__X,s.__Y=x,y
            s.__visible=1
            s.__exist=1
            s.__selected=0
            #Definicje:
            s.create()
            s.show()
            s.select()
      def getXY(s):#Zwraca wspolrzedne globalne
            return s.__X,s.__Y
      def getX(s):#Zwraca wspolrzedna globalna X
            return s.__X
      def getY(s):#Zwraca wspolrzedna globalna Y
            return s.__Y
      def getxy(s):#Zwraca wspolrzedne lokalne
            return s.__x,s.__y
      def getx(s):#Zwraca wspolrzedna lokalna x
            return s.__x
      def gety(s):#Zwraca wspolrzedna lokalna y
            return s.__x
      def getVisible(s):#Zwraca parametr widocznosci
            return s.__visible
      def getExist(s):#Zwraca parametr istnienia
            return s.__exist
      def getSelected(s):#Zwraca parametr zaznaczenia
            return s.__selected
      
      #Definicje ktore beda wysylaly sygnaly do sluchaczy
      def create(s):#Tworzy punkt
            s.__exist=1
            s.sendSignal()
      def destroy(s):#Niszczy punkt
            s.__exist=0
            s.sendSignal()
      def show(s):#Wyswietla punkt
            s.__visible=1
            s.sendSignal()
      def hide(s):#Ukrywa punkt
            s.__visible=0
            s.sendSignal()
      def select(s):#Zaznacza punkt
            s.__selected=1
            s.sendSignal()
      def deselect(s):#Odznacza punkt
            s.__selected=0
            s.sendSignal()