import pygame
import sys
import os

from shobu import Tablero

def main():
    # windows  position 
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
    # inicializar pygame 
    pygame.init()
    # generar la ventana
    size = 600, 620
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Shobu")
    clock = pygame.time.Clock()

    FPS = 120
    clock.tick(FPS)

    color_fondo = (49, 55, 59)

    # bucle 
    run = True

    # componentes 
    tabl = Tablero()

    while run:
        #dibujando componentes
        #screen.fill((240, 240, 240))#pintar pantalla 
        screen.fill(color_fondo)#pintar pantalla 
        tabl.dibujar_all(screen)
        # espara
        pygame.time.delay(10)
        pygame.display.update()

        #leer eventos
        for event in pygame.event.get():
            #...
            # evento de mouse
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                tabl.selecionar_pieza(pos[0],pos[1])
            # evento de salida
            if event.type == pygame.QUIT:
                run = False
    # Finalizar pygame
    pygame.quit()
#    screen.blit()
    pygame.display.flip()

if __name__ == '__main__':
    main()
