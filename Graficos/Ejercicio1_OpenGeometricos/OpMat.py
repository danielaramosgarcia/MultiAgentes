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
    def rotateX(self, deg):
        self.R = np.identity(4)
        radians = np.radians(deg)
        self.R[1][1] = np.cos(radians)
        self.R[1][2] = np.sin(radians)
        self.R[2][1] = -1 * np.sin(radians)
        self.R[2][2] = np.cos(radians)
        self.A = self.R @ self.A
        

    def rotateY(self, deg):
        self.R = np.identity(4)
        radians = np.radians(deg)
        self.R[0][0] = np.cos(radians)
        self.R[0][2] = np.sin(radians)
        self.R[2][0] = -1 * np.sin(radians)
        self.R[2][2] = np.cos(radians)
        self.A = self.R @ self.A
        
    def rotateZ(self, deg):
        self.R = np.identity(4)
        radians = np.radians(deg)
        self.R[0][0] = np.cos(radians)
        self.R[0][1] = -1 * np.sin(radians)
        self.R[1][0] = np.sin(radians)
        self.R[1][1] = np.cos(radians)
        self.A = self.R @ self.A
        
    def rotate(self, theta, x, y, z):
        self.R = np.identity(4)
        radians = np.radians(theta)
        c = np.cos(radians)
        s = np.sin(radians)
        self.R[0][0] = x*x*(1-c)+c
        self.R[0][1] = x*y*(1-c)-z*s
        self.R[0][2] = x*z*(1-c)+y*s
        self.R[1][0] = y*x*(1-c)+z*s
        self.R[1][1] = y*y*(1-c)+c
        self.R[1][2] = y*z*(1-c)-x*s
        self.R[2][0] = x*z*(1-c)-y*s
        self.R[2][1] = y*z*(1-c)+x*s
        self.R[2][2] = z*z*(1-c)+c
        self.A = self.R @ self.A
    
    #va a tomar la matriz de modelado y multiplicarla por los putnos del pligono
    #para calcular los resultado finales de los vertices del poligono a utilizar
    def mult_Points(self, points):
        #no se limpia matriz para utilizar los datos acumulados
        pointsR = (self.A @ points.T).T
        for i in range(0, pointsR.shape[1] + 1):
            for j in range (0,4):
                points[i][j] = pointsR[i]
        
