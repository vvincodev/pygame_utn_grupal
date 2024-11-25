import pygame
import pygame.mixer as mixer
import constantes #constantes
from barras import Personaje #importo al jugador
from pelota import Pelota

def iniciar_juego():
    mixer.init()
    mixer.music.load('assets/sounds/retro_tenis.mp3')
    mixer.music.set_volume(0.1)
    mixer.music.play() # inicializamos la musica de fondo
    pygame.init()

    ventana = pygame.display.set_mode((constantes.WIDTH,
                                    constantes.HEIGHT)) #seteamos la ventana
    pygame.display.set_caption("Pong") #titulo del juego

    #confi tablero para el puntaje
    font = pygame.font.Font(None, constantes.PUNTAJE_SIZE)
    puntaje_izquierda = 0
    puntaje_derecha = 0


    #creamos instancias de las paletas
    paleta_izquierda = Personaje(50, constantes.HEIGHT // 2 - constantes.PERS_HEIGHT // 2) 
    paleta_derecha =  Personaje(constantes.WIDTH -70 , constantes.HEIGHT // 2 - constantes.PERS_HEIGHT // 2) 

    #creamos instancia de la pelota
    pelota = Pelota(constantes.WIDTH // 2)

    #definimos las variables de las paletas 
    mover_izquierda_arriba = False
    mover_izquierda_abajo = False
    mover_derecha_arriba = False
    mover_derecha_abajo= False

    run = True #para correr el juego
    reloj = pygame.time.Clock() #colntrolar el frame rate (fps)

    while run :
        for event in pygame.event.get(): #recorro los eventos del juego  
            if event.type == pygame.QUIT: 
                run = False #para cerrar el juego (cancela el while)

            if event.type == pygame.KEYDOWN:  #LE DAMOS MOVIMIENTO AL PERSONAJE
                if event.key == pygame.K_w:
                    mover_izquierda_arriba = True
                    #print("Izquierda arriba")
                if event.key == pygame.K_s:
                    mover_izquierda_abajo = True
                    #print("Izquierda abajo")
                if event.key == pygame.K_UP:
                    mover_derecha_arriba = True
                    #print("derecha arriba")
                if event.key == pygame.K_DOWN:
                    mover_derecha_abajo = True
                    #print("derecha abajo")
                if event.key == pygame.K_r:
                    iniciar_juego()

            if event.type == pygame.KEYUP: #controlamos cuando suelta la tecla

                if event.key == pygame.K_w:
                    mover_izquierda_arriba = False
                if event.key == pygame.K_s:
                    mover_izquierda_abajo = False
                if event.key == pygame.K_UP:
                    mover_derecha_arriba = False
                if event.key == pygame.K_DOWN:
                    mover_derecha_abajo = False


        delta_y_izquierda = 0 #cuanto de la posicion iniciar me muevo en el siguiente frame
        delta_y_derecha = 0  

        if mover_izquierda_arriba == True:
            delta_y_izquierda = -constantes.VELOCIDAD 
        if mover_izquierda_abajo == True:
            delta_y_izquierda = constantes.VELOCIDAD  
        if mover_derecha_arriba == True:  
            delta_y_derecha = -constantes.VELOCIDAD 
        if mover_derecha_abajo == True:
            delta_y_derecha = constantes.VELOCIDAD 

        reloj.tick(constantes.FPS) #limitamos los fps

        ventana.fill(constantes.COLOR_FONDO) #calculamos el movimiento

        #jugador.movimiento(delta_x,delta_y) #le mando el movimiento
        #jugador.dibujar(ventana) #dibujo al jugador en la ventana

        paleta_izquierda.movimiento(delta_y_izquierda) #mandamos el movimiento
        paleta_derecha.movimiento(delta_y_derecha) 
        #dibujamos el movimiento
        paleta_izquierda.dibujar(ventana)
        paleta_derecha.dibujar(ventana)
        #dibujamos el puntaje 
        puntaje_texto = font.render(f"{puntaje_izquierda} - {puntaje_derecha}", True, (255, 255, 255))
        ventana.blit(puntaje_texto, (constantes.WIDTH // 2 - puntaje_texto.get_width() // 2, 20))

        pygame.display.update() #actualiza la pantalla

        #verificamos si algun jugador gano
        if puntaje_izquierda >= 10 or puntaje_derecha >= 10:
            run = False
    
    pygame.quit()

    if puntaje_izquierda >= 10:
        print("¡Jugador Izquierdo Gana!") 
    elif puntaje_derecha >= 10: 
        print("¡Jugador Derecho Gana!")

iniciar_juego()