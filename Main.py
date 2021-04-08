import pygame
import sys

from shobu import Tablero

def main():
    # inicializar pygame 
    pygame.init()
    # generar la ventana
    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Shobu")
    clock = pygame.time.Clock()

    FPS = 120
    clock.tick(FPS)


    # bucle 
    run = True

    # componentes 
    tabl = Tablero()

    while run:
        #dibujando componentes
        screen.fill((240, 240, 240))#pintar pantalla 
        tabl.dibujar_all(screen)
        # espara
        pygame.time.delay(10)
        pygame.display.update()

        #leer eventos
        for event in pygame.event.get():
            #...
            # evento de salida
            if event.type == pygame.QUIT:
                run = False
    # Finalizar pygame
    pygame.quit()
#    screen.blit()
    pygame.display.flip()

if __name__ == '__main__':
    main()
