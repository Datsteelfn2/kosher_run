import pygame
pygame.init()
screen=pygame.display.set_mode((800,400))

clock=pygame.time.Clock()
platform_surface=pygame.image.load("images/platform.png").convert_alpha()
platform_surface=pygame.transform.scale(platform_surface,(800,200))
yellow=(220, 193, 185)

player_surface=pygame.image.load("images/blp.png")
player_surface=pygame.transform.scale(player_surface,(300,150))
player_rect=player_surface.get_rect(midbottom=(50,336))



run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.fill(yellow)
    screen.blit(platform_surface,(0,300))
    screen.blit(player_surface,player_rect)
    
    clock.tick(60)

    pygame.display.update()