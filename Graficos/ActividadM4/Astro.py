import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math
# import numpy as np

class Astro:
    def __init__(self, dist: float , esc: float, color: list[float], v_ang: float):
        self.deg = 0.0
        self.dist = dist
        self.esc = esc
        self.color = color.copy()
        self.v_ang = v_ang
        self.sphere = gluNewQuadric()
        self.moons: list[Astro] = []
        
    def update(self):
        self.deg += self.v_ang
        if self.deg >= 360.0:
            self.deg = 0
    
    def draw(self):
        glPushMatrix()
        #definir el color de la esfera
        glColor3fv(self.color)
        #rotar el sistema sobre el eje Y
        glRotatef(self.deg, 0.0, 1.0, 0.0)
        #tras el sistema de ref con respecto al eje X
        glTranslatef(self.dist, 0.0, 0.0)
        #cambiar la escala del sistema de referencia
        glScalef(self.esc, self.esc, self.esc)
        gluSphere(self.sphere, 1.0, 16, 16)
        gluSphere(self.sphere, 1.0, 16, 16)
        glRotatef(90, 1, 0, 0)
        
        for moon in self.moons:
            moon.draw()
            
        glPopMatrix()
        self.update()
        
    def addMoon(self, moon: "Astro"):
            self.moons.append(moon)
            