import pygame
pygame.init()
screen=pygame.display.set_mode((800,400))

clock=pygame.time.Clock()
platform_surface=pygame.image.load("images/platform.png").convert_alpha()
platform_surface=pygame.transform.scale(platform_surface,(800,200))
yellow=(220, 193, 185)

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.fill(yellow)
    screen.blit(platform_surface,(0,300))
    clock.tick(60)

    pygame.display.update()