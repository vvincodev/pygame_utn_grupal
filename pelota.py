import pygame
import constantes
import random
import math

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
        self.shape.x = constantes.WIDTH // 2 - constantes.WIDTH_P // 2
        self.shape.y = constantes.HEIGHT // 2 - constantes.HEIGHT_P // 2
        self.velocidad_x = constantes.VELOCIDAD_PELOTA_X * random.choice([1, -1])
        self.velocidad_y = constantes.VELOCIDAD_PELOTA_Y * random.choice([1, -1])

    def rebotar(self, barra):
        if self.shape.colliderect(barra.shape):

            # Hace coincidiar a los bordes de la pelota y la barra para que no la traspase
            if self.velocidad_x > 0:
                self.shape.right = barra.shape.left
            elif self.velocidad_y < 0:
                self.shape.left = barra.shape.right

            # Cambia la direccion de la pelota
            self.velocidad_x *= (-1)
            
            # Varia la velocidad vertical dependiendo del punto donde impacta la pelota
            diferencia_centro = (self.shape.centery - barra.shape.centery) / (barra.shape.height / 2)
            self.velocidad_y += diferencia_centro * 4

            # Se limita la velocidad de y
            max_velocidad_y = 15
            self.velocidad_y = max(-max_velocidad_y, min(max_velocidad_y, self.velocidad_y))

            #print(f'sale x={self.velocidad_x}')
            #print(f'sale y={self.velocidad_y}')

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, self.color, self.shape)
    