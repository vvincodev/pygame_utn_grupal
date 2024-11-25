import pygame
import constantes

class Personaje(): #creamos nuestro primer personaje
    def __init__ (self, x,y ): #asigno forma
        self.shape = pygame.Rect(x, y, constantes.PERS_WIDTH, constantes.PERS_HEIGHT)
        self.color = constantes.PERS_COLOR

    def movimiento(self, delta_y): #funcion para definir el movimiento la paletga
        #act la posicion de la paleta 
        self.shape.y += delta_y

        #que no se vaya del mapa
        if self.shape.top < 0:
            self.shape.top = 0
        if self.shape.bottom > constantes.HEIGHT:
            self.shape.bottom = constantes.HEIGHT

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, self.color, self.shape)
