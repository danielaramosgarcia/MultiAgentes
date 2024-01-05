import pygame
from pygame.locals import *

# se carga las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import numpy as np

class OpMat:
    def __init__(self, ):
        #matriz de traslacion 
        self.T = np.identity(4)
        #matriz de rotacion
        self.R = np.identity(4)
        #matriz de acumulacion
        self.A = np.identity(4)
        
    #se esta trasladando el objeto, la funcion acepta la matriz y el vector
    def translate(self,tx,ty,tz):
        #limpiando matriz de translacion
        self.T = np.identity(4)
        self.T[0][3] = tx
        self.T[1][3] = ty
        self.T[2][3] = tz
        self.A = self.T @ self.A
        
    #se rota sobre el ejeX, es con la matriz de la diapo del prof
    #se toma la matriz y los grados a rotar
    def rotateX(self,deg):
        #limpiando matriz de rotacion
        self.R = np.identity(4)
        radians = np.radians(deg)
        self.R[1][1] = np.cos(radians)
        self.R[1][2] =  -1 * np.sin(radians)
        self.R[2][1] = np.sin(radians)
        self.R[2][2] = np.cos(radians)
        self.A = self.R @ self.A
    
    #va a tomar la matriz de modelado y multiplicarla por los putnos del pligono
    #para calcular los resultado finales de los vertices del poligono a utilizar
    def mult_Points(self, points):
        #no se limpia matriz para utilizar los datos acumulados
        pointsR = (self.A @ points.T).T
        for i in range(0, pointsR.shape[1] + 1):
            for j in range (0,4):
                points[i][j] = pointsR[i][j]
        
