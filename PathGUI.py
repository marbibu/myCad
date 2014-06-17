class PathGUI:
      def __init__(s,C,path):
            #Dane:
            s.__C=C
            s.__path=path
            #Definicje:
            s.__draw()
      def __draw(s):#Rysuje sciezke
            coords=s.__path.getCoords()
            s.__C.create_line(*coords)#zalezy od warstwy