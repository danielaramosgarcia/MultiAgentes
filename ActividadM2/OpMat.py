import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


import math
import numpy as np

class OpMat:
    def __init__(self):
        self.T = np.identity(4)
        self.R = np.identity(4)
        self.S = np.identity(4)
        self.A = np.identity(4)
        
    def translate(self, tx, ty, tz):
        self.T[0][3] = tx
        self.T[1][3] = ty
        self.T[2][3] = tz
        self.A = self.T @ self.A
    
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

        self.R[0][0] = x*x*(1-c) + c
        self.R[0][1] = x*y*(1-c) - z*s
        self.R[0][2] = x*z*(1-c) + y*s
        self.R[1][0] = y*x*(1-c) + z*s
        self.R[1][1] = y*y*(1-c) + c
        self.R[1][2] = y*z*(1-c) - x*s
        self.R[2][0] = x*z*(1-c) - y*s
        self.R[2][1] = y*z*(1-c) + x*s
        self.R[2][2] = z*z*(1-c) + c
        
        self.A = self.R @ self.A
        
    def scale(self,sx,sy,sz):
        self.S = np.identity(4)
        self.S[0][0] = sx
        self.S[1][1] = sy
        self.S[2][2] = sz
        self.A = self.S @ self.A    
    
    def mult_Points(self, points):
        pointsR = (self.A @ points.T).T
        for i in range(0, pointsR.shape[1] + 1):
            for j in range(0,4):
                points[i][j] = pointsR[i][j]
                
    def loadIdentity(self):
        self.A = np.identity(4)
           
       