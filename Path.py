from Sender import Sender
class Path(Sender):
      def __init__(s):
            #Dane:
            Sender.__init__(s)
            s.__points=[]
            s.__current=None
      def selectPoint(s,point):#Zaznacza punkt
            if s.__current==None:
                  pass
            else:
                  s.__current.select()
            s.__current=point
            s.__current.deselect()
      def getCurrentPointIndex(s):#Zwraca indeks biezacego punktu
            return s.__points.index(s.__current)
      def hasPointWithXY(s,point):#Sprawdza czy punkt z podanymi wspolrzednymi istnieje i jezeli tak to go zwraca
            result=0
            X,Y=point.getXY()
            for i in s.__points:
                  x,y=i.getXY()
                  if x==X and y==Y:
                        return i
            return None
      def __addPoint(s,point):#Dodaje punkt do listy
            if s.__current==None:
                  s.__points.append(point)
            else:
                  index=s.getCurrentPointIndex()
                  if index==len(s.__points)-1:
                        s.__points.append(point)
                  else:
                        s.__points.insert(index+1,point)
      def addPoint(s,point):#Dodaje punkt
            new=s.hasPointWithXY(point)
            if new==None:
                  pass
            else:
                  point=new
            s.__addPoint(point)
            s.selectPoint(point)
      def getCoords(s):#Zwraca liste wspolrzednych
            result=[]
            for i in s.__points:
                  result.extend(list(i.getXY()))
            return result
      def getPoints(s):#Zwraca liste punktow
            return s.__points
      #najpierw sprawdzamy czy punkt o podanych wspolrzednych istnieje