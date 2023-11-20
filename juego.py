import time
import pygame 
import sys
from rdkit import Chem
import random
from repositorio_quimica import elementos_quimicos

#función para iniciar pygame
pygame.init()

# (largo, altura)
size = (1000, 650)
run = False

# con este comando se crea la ventana donde ejecutara el comando
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Juego química')

#Esta es la clase que puede crear objetos de tipo boton
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

#Cargo las imagenes de los botones
play_img = pygame.image.load('boton_play.png').convert_alpha()
exit_img = pygame.image.load('boton_exit.png').convert_alpha()

#Declaro los objetos tipo boton
pausa_button = Button(275, 250, play_img, 0.28)
exit_button = Button(600, 285, exit_img, 0.15)
#este boton de salida en realidad funciona más como una pausa
exit_button1 = Button(15, 10, exit_img,0.15)


puntaje = 0
claves = []
def Random_Elementos():
    
    
    for x in range(8):
        clave = random.choice(list(elementos_quimicos.keys()))
        claves.append(clave)

#inicializo las claves
Random_Elementos()
print (claves)

#diccionario para las claves de quimicos con su respectivo índice
teclas_a_claves = {
    pygame.K_a: [claves[0], 0], pygame.K_w: [claves[1], 1], pygame.K_s: [claves[2], 2], pygame.K_d: [claves[3], 3],
    pygame.K_LEFT: [claves[4], 4], pygame.K_UP: [claves[5], 5], pygame.K_DOWN: [claves[6], 6], pygame.K_RIGHT: [claves[7], 7],
}

tiempo_restante = 101

def temporizador(tiempo_restante):
    tiempo_restante -= 1
    return tiempo_restante


#fuentes para escribir texto en la consola
text_font = pygame.font.SysFont(None , 25)
text_font1 = pygame.font.Font(None , 20)
text_font2 = pygame.font.SysFont(None , 40,True)

def draw_text(text, font, color, X, Y):
    #renderiza texto en una superficie donde el segundo parametro indica si debe haber antialising
    img = font.render(text,True, color)
    #esta imagen renderizada se copiara en la screen
    screen.blit(img,(X,Y))


#funcion para determinar el tipo de enlace(si acierta varias veces el tipo de enlace entonces obtendra una racha)
enlace_io = 0
enlace_cov = 0
#funcion para determinar la logica del juego
def Determinar_ValenciayEnlace(val1,val2,EN1,EN2,n,m,excepcion):
    global puntaje
    global claves
    global enlace_io
    global enlace_cov
    if(abs(EN1-EN2)< 1.7 or excepcion == 3 or excepcion != 6): 
        ##aplico la condicion de la suma de 8 para la excepcion de H y F pues su electronegatividad es mayor a 1.7 pero sigue siendo un 
        #enlace covalente y funciona porque 
        if (abs(val1-8)== abs(val2-8) or val1+val2==8 ):
            #covalente
            enlace_cov += 1
            enlace_io = 0
            claves[n] = random.choice(list(elementos_quimicos.keys()))
            claves[m] = random.choice(list(elementos_quimicos.keys()))
            print("enlace_cov")
            puntaje += (50*enlace_cov)
    elif(abs(EN1-EN2)>= 1.7 or excepcion == 6):
        if (val1 + val2 )== 8:
            #ionico
            enlace_io += 1
            enlace_cov = 0
            claves[n] = random.choice(list(elementos_quimicos.keys()))
            claves[m] = random.choice(list(elementos_quimicos.keys()))
            print("enlace_io")
            puntaje += (50*enlace_io)
   
    
        
    

Negro=(0,0,0)
Blanco=(255,255,255)
Plomo = (169, 169, 169)



#loop para la interfaz grafica
run_1 = True
def interfaz_entrada():
    global run_1
    global run
    while run_1:

        screen.fill((202, 228, 241))
        draw_text("ENLAZADOS, EL JUEGO", text_font2, Negro,325,10)
        
        if pausa_button.draw(screen):
            run_1 = False
            run = True
            
        if exit_button.draw(screen):
            run_1 = False
            print('EXIT')

        #event handler
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                run_1 = False

        pygame.display.update()

interfaz_entrada()
 
destecleador = []

excepcion = 0

while run:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
        if events.type == pygame.KEYDOWN:
           if events.key in teclas_a_claves:
               clave_presionada, indice = teclas_a_claves[events.key]
               if clave_presionada in elementos_quimicos:
                  
                destecleador.append(events.key)
                       
                if "valorE" not in locals():
                        valorE = elementos_quimicos[clave_presionada]["electroN"]
                        valorV = elementos_quimicos[clave_presionada]["electroV"]
                        indice1 = indice
                        if elementos_quimicos[clave_presionada]["nombre"] == 'Hydrogen' :
                            excepcion = 1
                        elif elementos_quimicos[clave_presionada]["nombre"] == 'Fluorine':
                            excepcion = 2
                        elif elementos_quimicos[clave_presionada]["nombre"] == 'Nitrogen':
                            excepcion = 4
                        elif elementos_quimicos[clave_presionada]["nombre"] == 'Aluminium':
                            excepcion = 5
                        print(valorV)
                        print(valorE)
                        print("a")
                    #si te das cuenta si es que no libro el valor principal que le di a valorE entonces solo ejecutara el else
               

                if len(destecleador) == 2:
                    
                    if destecleador[0] != destecleador[1]:
                            valorE1 = elementos_quimicos[clave_presionada]["electroN"]
                            valorV1 = elementos_quimicos[clave_presionada]["electroV"]
                            indice2 = indice
                            if elementos_quimicos[clave_presionada]["nombre"] == 'Hydrogen' and excepcion == 2:
                                excepcion = 3
                            elif elementos_quimicos[clave_presionada]["nombre"] == 'Fluorine' and excepcion == 1:
                                excepcion = 3
                            elif elementos_quimicos[clave_presionada]["nombre"] == 'Nitrogen' and excepcion == 5:
                                excepcion = 6
                            elif elementos_quimicos[clave_presionada]["nombre"] == 'Aluminium' and excepcion == 4:
                                excepcion = 6
                            print("b")
                            print(valorE1)
                            print(valorV1)
                            Determinar_ValenciayEnlace(valorV,valorV1,valorE,valorE1,indice1,indice2,excepcion)
                            excepcion = 0
                            del valorE
                            del valorV
                    
                    if destecleador[0] == destecleador[1]:
                            print("c")
                            del valorE
                            del valorV
                    destecleador = []
                                        
                                        
    tiempo_restante = temporizador(tiempo_restante)
    
    

    screen.fill(Blanco)
    #en este espacio se dibuja
    
    if exit_button1.draw(screen):
        run = False
        run_1 = True
        interfaz_entrada()
        puntaje = 0
        tiempo_restante = 101
        print('EXIT')
    
    x_botones = [200, 400, 600, 800]
    botones = [ "A", "W", "S", "D"]
    botones1 = ["left", "up", "down", "right"]
    
    for i in range(4):
        x_boton = x_botones[(i+4)%4]
        boton = botones[(i+4)%4]
        
        y_boton = 250
        
        
        pygame.draw.rect(screen,Negro,(x_boton, y_boton, 25, 25))
        pygame.draw.rect(screen, Plomo,((x_boton+2), y_boton+2, 21, 21))
        draw_text(boton, text_font, Negro, x_boton+6, 250+4)
        
    for i in range(4):
        x_boton = x_botones[(i+4)%4]
        boton1 = botones1[(i+4)%4]
        
        pygame.draw.rect(screen,Negro,(x_boton, 500, 35, 25))
        pygame.draw.rect(screen, Plomo,((x_boton+2), 500+2, 32, 21))
        draw_text(boton1, text_font1, Negro, x_boton+2, 500+4)

    draw_text("score: " + str(puntaje),text_font,Negro,900,1)
    
    draw_text(str(tiempo_restante), text_font, Negro, 470, 1)
    for i in range(0,4):
        draw_text(claves[i],text_font,Negro,200*(i+1), 200)
    
    for i in range(4,8):
        draw_text(claves[i],text_font,Negro,200*(i-3), 450)
        
    #aqui termina el dibujo
    if tiempo_restante == 0:
        run = False
        
    pygame.display.flip()
    time.sleep(1)
    
            