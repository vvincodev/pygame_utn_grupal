import pygame
import constantes
import random

class Pelota(): #creamos la pelota
    def __init__ (self, x,y): #asigno forma
        self.shape = pygame.Rect(x, y, constantes.WIDTH_P, constantes.HEIGHT_P)
        self.color = constantes.PELOTA_COLOR
        self.velocidad_x = constantes.VELOCIDAD_PELOTA_X * random.choice([1, -1])
        self.velocidad_y = constantes.VELOCIDAD_PELOTA_Y * random.choice([1, -1])

    def movimiento(self): #funcion para definir el movimiento la pelota
        self.shape.x += self.velocidad_x
        self.shape.y += self.velocidad_y

        #para que rebote verticalmente
        if self.shape.top < 0 or self.shape.bottom >= constantes.HEIGHT:
            self.velocidad_y = -self.velocidad_y

    def anotacion(self):
        #para que arranque de nuevo al anotar
        pass
    

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, self.color, self.shape)
