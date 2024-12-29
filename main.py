import pygame
pygame.init()
WIDTH,HEIGHT=800,400
screen=pygame.display.set_mode((WIDTH,HEIGHT))

clock=pygame.time.Clock()
platform_surface=pygame.image.load("images/platform.png").convert_alpha()
platform_surface=pygame.transform.scale(platform_surface,(800,200))
yellow=(220, 193, 185)

player_surface=pygame.image.load("images/blp.png")
player_surface=pygame.transform.scale(player_surface,(150,200))
player_rect=player_surface.get_rect(midbottom=(150,346))

enemy_surface=pygame.image.load("images/germany.png")

enemy_surface=pygame.transform.scale(enemy_surface,(150,200))
enemy_rect=enemy_surface.get_rect(midbottom=(700,346))
platform_x1=0
platform_x2=WIDTH
platform_speed=5

gravity=0
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if player_rect.bottom==336:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gravity=-20

    screen.fill(yellow)
    gravity+=1
    player_rect.y+=gravity

    if player_rect.bottom>336:
        player_rect.bottom=336
    #infinite movement
    platform_x1-=platform_speed#makes the platform move to the left
    platform_x2-=platform_speed
    # check and see if the platform moves off the screen
    if platform_x1 <= -WIDTH:  # if less than -800
        platform_x1 = 800  # Place platform 1 just after platform 2

# Check if platform 2 has moved completely off the screen
    if platform_x2 <= -WIDTH:
        platform_x2 = 800  # Place platform 2 just after platform 1

    #constantly drawing the platform, the platform changes because were constantly adding platform_speed to platform_x1 and platform_x2"
    screen.blit(platform_surface,(platform_x1,300))
    screen.blit(platform_surface,(platform_x2,300))
    screen.blit(player_surface,player_rect)
    screen.blit(enemy_surface,enemy_rect)
    
    clock.tick(60) 

    pygame.display.update()