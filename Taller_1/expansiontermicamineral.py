import matplotlib.pyplot as plt
import numpy as np


#Clase Mineral
class Mineral:
    def __init__ (self, nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino):
        self.nombre = nombre
        self.dureza = float(dureza)
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = float(specific_gravity)
        
    def silicato (self):
        
        return ("Si" in self.composicion) and ("O" in self.composicion)
            
    def densidad (self):
        self.specific_gravity= self.specific_gravity*1000
        print(self.specific_gravity)
        
    def mostrar_color (self):
        rgb = tuple(int(self[i:i+2], 16) for i in (1, 3, 5))
        print(rgb)
        color = np.full((1, 1, 3), rgb)
    
        plt.imshow(color)
        plt.axis('off')
        plt.show()
        
    def imprimir_dureza (self):
        
        print(self.dureza)
        print(self.rompimiento_por_fractura)
        print(self.sistema_cristalino)

class ExpansionTermicaMineral(Mineral):
    
    def __init__(self, nombre, archivo):
        self.temperatura= []
        self.volumen= []
        
        with open(archivo) as file:
            lineas= file.read()
            elementos=lineas.split('\n')
            #print(elementos)
            lista= []
            
            
            for i in elementos:
                x= i.split(',')
                lista.append(x)

            for i in lista:
            
                self.temperatura.append(i[0])
                self.volumen.append(i[1])  
                
            self.temperatura.pop(0)
            self.volumen.pop(0)
            
            self.temperatura = list(map(float, self.temperatura))
            self.volumen = list(map(float, self.volumen))
            #print(self.temperatura)
            #print(self.volumen) 
            
    def coeficiente_expansion (self):
        d = 0
        x= self.temperatura
        y= self.volumen
        h= x[1]-x[0]
        derivative= []
        
        if h != 0:
            i=0
            while i<= len(x):
                if ((x[i] + h) in x) and ((x[i] - h) in x):
                    pos_xmash= self.temperatura.index(x[i]+h)
                    f_xmash= y[pos_xmash]
                    f_xmenosh= self.temperatura.index(x[i]-h)

                    d= (f_xmash - f_xmenosh)/(2*h)
                    derivative.append(d)
                    i+= 1
            
        print(derivative)
        
        return derivative
             
            
classe= ExpansionTermicaMineral(Mineral, 'olivine_angel_2017.csv')
print(classe.coeficiente_expansion())