import pygame
import random
import math
from pygame import mixer #permite reproducir musica y sonidos
import io

def fuente_bytes(fuente):
    with open(fuente, "rb") as f:
        ttf_bytes = f.read()
        return io.BytesIO(ttf_bytes)
    



#INICIALIZAAR PYGAME
pygame.init()

#CREAR LA VENTANA
screen = pygame.display.set_mode((600, 800)) 

#TITULO E ICONO
pygame.display.set_caption("HIGHAWAY")      #Cual es el titulo de la ventana
icon = pygame.image.load("icono.ico")       #cargar una imagen de icono
pygame.display.set_icon(icon)               #mostrar y establecer el icono

#Puntaje
puntaje = 0
fuente_como_bytes = fuente_bytes("28_Days_Later.ttf")
fuente = pygame.font.Font("28_Days_Later.ttf", 32)  #cargar una fuente de https://www.1001freefonts.com archivo .ttf
texto_X = 10
texto_Y = 10

#texto final de juego
fuente_final = pygame.font.Font("28_Days_Later.ttf", 40)  #cargar una fuente de https://www.1001freefonts.com archivo .ttf
def texto_final():
    texto_fin = fuente_final.render(f"FIN DEL CAMINO", True, (255, 0, 0)) # color de texto (255, 255, 255)
    screen.blit(texto_fin, (200, 400))  #dibujar el texto en la pantalla
 
 
#funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"PUNTAJE: {puntaje} ", True, (10, 9, 102)) # color de texto (255, 255, 255)
    screen.blit(texto, (x, y))  #dibujar el texto en la pantalla

#fondo
fondo = pygame.image.load("fondo_2.jpg")   #cargar imagen de fondo

#agregar musica
mixer.music.load("sonido_fondo.mp3") #cargar la musica
mixer.music.set_volume(0.5) #establecer el volumen de la musica
mixer.music.play(-1) #reproducir la musica en bucle con -1
#jugador
jugador = pygame.image.load("car.png")   #cargar imagen del jugador
jugador_x = 350                          #posicion inicial del jugador
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0

#coche amarillo
img_coche_amarillo = []
coche_amarillo_x = []                      
coche_amarillo_y = []
coche_amarillo_x_cambio = []
coche_amarillo_y_cambio = []
cantidad_coche_amarillo = 4

for i in range(cantidad_coche_amarillo):
    img_coche_amarillo.append(pygame.image.load("car_y.png"))
    coche_amarillo_x.append(random.randint(50, 400))                     
    coche_amarillo_y.append(random.randint(0, 100) )
    coche_amarillo_x_cambio.append(50)
    coche_amarillo_y_cambio.append(0.2)

#bala
bala = pygame.image.load("bala.png")   
bala_x = 0                       
bala_y = 500

bala_x_cambio = 0
bala_y_cambio = 2

bala_visible = False

#JUGADOR FUNCION------------------------------------------------------------------------
def jugador_(X,Y):
    screen.blit(jugador, (X, Y)) #dibujar la imagen del jugador

#COCHE FUNCION------------------------------------------------------------------------
def Auto_amarillo(X,Y, coche):
    screen.blit(img_coche_amarillo[coche], (X, Y)) #dibujar la imagen del auto amarillo
 
#bala FUNCION------------------------------------------------------------------------
def disparar_bala(X,Y):
    global bala_visible
    bala_visible = True
    screen.blit(bala, (X + 16, Y + 10)) #aparezcan al centro de la imagen

#funcion para detectar colision
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow((x_1 - x_2),2) + math.pow((y_1 - y_2),2))
    if distancia < 27:
        return True 
    else:
        return False

se_ejecuta = True
while se_ejecuta:
    # cerrar ventana revisando la ejecucion de cada evento
    #screen.fill((0, 0, 0))              #rellenar la pantalla con el color 

    #imagen de fondo
    screen.blit(fondo, (0, 0))

    #ITERAR  EVENTOS
    for evento in pygame.event.get(): 
        

        #EVENTO CERRAR VENTANA
        if evento.type == pygame.QUIT: #cerrar ventana
            se_ejecuta = False
    
        #EVENTO TECLAS PRESIONADAS
        if evento.type == pygame.KEYDOWN:  #si se presiona una tecla
            
            if evento.key == pygame.K_LEFT:  #si se presiona la tecla izquierda  
                jugador_x_cambio = -0.5         #mover el jugador hacia la izquierda
            if evento.key == pygame.K_RIGHT:    #si se presiona la tecla derecha
                jugador_x_cambio = 0.5    
            if evento.key == pygame.K_UP:       #si se presiona la tecla arriba
                jugador_y_cambio = -0.5        #mover el jugador hacia arriba
            if evento.key == pygame.K_DOWN:    #si se presiona la tecla abajo
                jugador_y_cambio = 0.5        #mover el jugador hacia abajo
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")  #reproducir sonido de disparo
                sonido_bala.set_volume(0.5)  #establecer volumen del sonido
                sonido_bala.play()  #reproducir el sonido de disparo
                if not bala_visible:
                    bala_x = jugador_x
                    bala_y = jugador_y
                    disparar_bala(bala_x, bala_y)   #disparar la bala


        #EVENTO TECLAS SOLTADAS
        if evento.type == pygame.KEYUP:         #si se soltar una tecla
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:     #si se soltar la tecla izquierda
                jugador_x_cambio = 0                                            #si se soltar la tecla derecha
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:       #si se soltar la tecla arriba
                jugador_y_cambio = 0        
            
                                                  #si se soltar la tecla abajo
        
        
    #MODIFICAR LA POSICION DEL JUGADOR
    jugador_x += jugador_x_cambio             #mover el jugador
    jugador_y += jugador_y_cambio             #mover el jugador


    #MANTENER AL JUGADOR DENTRO DE LA PANTALLA
    if jugador_x < 0:                         #si el jugador sale del eje x
        jugador_x = 0                        #moverlo al inicio de la pantalla
    elif jugador_x > 536:                    #si el jugador sale del eje x
        jugador_x =    536                   #moverlo al final de la pantalla
    elif jugador_y < 0:                         #si el jugador sale del eje y
        jugador_y = 0                        #moverlo al inicio de la pantalla
    elif jugador_y > 736:                    #si el jugador sale del eje y
        jugador_y = 736                      #moverlo al final de la pantalla

    for e in range(cantidad_coche_amarillo):

        # FIN DE JUEGO 
        if coche_amarillo_y[e] > 700:
            for i in range(cantidad_coche_amarillo):
                coche_amarillo_y[i] = 1000  
            sonido_explosion = mixer.Sound("explosion.mp3")  #reproducir sonido de colision
            sonido_explosion.set_volume(0.2)  #establecer volumen del sonido
            sonido_explosion.play()  #reproducir el sonido de colision
            texto_final()
            break

        coche_amarillo_y[e] += coche_amarillo_y_cambio[e]
    #MANTENER AL COCHE AMARILLO DENTRO DE LA PANTALLA
        if coche_amarillo_y[e] < 0:                         
            coche_amarillo_y[e] = 1     
            coche_amarillo_x[e] += coche_amarillo_x_cambio[e]                  

        elif coche_amarillo_y[e] > 736:                    
            coche_amarillo_y[e] = -1                     
            coche_amarillo_x[e] += coche_amarillo_x_cambio[e] 
    
        elif coche_amarillo_x[e] > 736:                    
            coche_amarillo_x[e] = random.randint(50, 500)   

        #verificar colision
        colision = hay_colision(coche_amarillo_x[e], coche_amarillo_y[e], bala_x, bala_y)
        if colision:
            sonido_explosion = mixer.Sound("explosion.mp3")  #reproducir sonido de colision
            sonido_explosion.set_volume(0.5)  #establecer volumen del sonido
            sonido_explosion.play()  #reproducir el sonido de colision
            bala_y = 500
            bala_visible = False
            puntaje += 1
                        
            coche_amarillo_x[e] = random.randint(50, 400)                        
            coche_amarillo_y[e] = random.randint(0, 100)         

        Auto_amarillo(coche_amarillo_x[e] , coche_amarillo_y[e], e)   #dibujar la imagen del jugador
        
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    #MOVIMIENTO BALA
    if bala_visible:
        disparar_bala(bala_x, bala_y)   #disparar la bala
        bala_y -= bala_y_cambio


    jugador_(jugador_x, jugador_y)                             #dibujar la imagen del jugador
    mostrar_puntaje(texto_X, texto_Y)                          #mostrar el puntaje en la pantalla

    pygame.display.update()                #actualizar la pantalla y ya muestra el color elegido
