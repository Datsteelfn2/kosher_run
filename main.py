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

enemy_surface=pygame.transform.scale(enemy_surface,(75,125))
enemy_rect=enemy_surface.get_rect(midbottom=(700,346))
platform_x1=0
platform_x2=WIDTH
platform_speed=5

gravity=0




#font
font=pygame.font.Font(None,50)
menu_font=pygame.font.Font(None,40)
def display_score():
    if game_activity and not game_over:
        time=int(pygame.time.get_ticks()/1000)-start_time
        text=font.render(f"SCORE:{time}",0,"Black")
        text_rect=text.get_rect(center=(WIDTH/2,50))
        screen.blit(text,text_rect)
        return time
start_time=0
#menu screen 
def menu():
    menu_text=font.render("Welcome to Kosher run",0,"Black")
    context_game_text1=menu_font.render("The objective of the game is to play as blp kosher",0,"Black")
    context_game_text2=menu_font.render("and jump on the approaching german Flag",0,"Black")
    
    menu_rect1=menu_text.get_rect(center=(WIDTH/2,50))#just centering the menu text
    context_game_rect1=context_game_text1.get_rect(center=(WIDTH/2,150))
    context_game_rect2=context_game_text2.get_rect(center=(WIDTH/2,200))

    start_text=font.render("Press Space to start",0,"Red")
    start_rect=start_text.get_rect(center=(WIDTH/2,250))

    screen.blit(menu_text,menu_rect1)
    screen.blit(context_game_text1,context_game_rect1)
    screen.blit(context_game_text2,context_game_rect2)
    screen.blit(start_text,start_rect)

def losing_screen(final_score):
    screen.fill("White")
    time=final_score
    losing_text=font.render("Thanks for playing,You lost",0,"Black")
    score_text=font.render(f"Your Score:{time}",0,"Red")
    play_text=font.render("Press Space to play again!",0,"Black")
    play_rect=play_text.get_rect(center=(WIDTH/2,150))

    losing_rect=losing_text.get_rect(center=(WIDTH/2,50))
    score_rect=score_text.get_rect(center=(WIDTH/2,100))
    screen.blit(losing_text,losing_rect)
    screen.blit(score_text,score_rect)
    screen.blit(play_text,play_rect)
game_activity=False
game_over=False
final_score=0


run=True
while run:
    screen.fill(yellow)
    if not game_activity and not game_over:
        menu()
   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if game_activity:

            if player_rect.bottom==336:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        gravity=-25
        if not game_activity and not game_over:
            
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    
                    game_activity=True
                    start_time=int(pygame.time.get_ticks()/1000)
        if game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_activity = True
                game_over = False
                final_score=0
                start_time = int(pygame.time.get_ticks() / 1000)
                gravity = 0
                player_rect.midbottom = (150, 346)
                enemy_rect.midbottom = (700, 346)
    #intitial menu screen

    #gravity
    if game_activity:
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
        final_score=display_score()
        # enemy logic
        enemy_rect.x-=7
        screen.blit(enemy_surface,enemy_rect)
        if enemy_rect.x<=0:
            enemy_rect.x=800
            screen.blit(enemy_surface,enemy_rect)

        #collision detecttion
        if player_rect.colliderect(enemy_rect):
            game_activity=False
            game_over=True
    
        
        
            
    if game_over:
        losing_screen(final_score)
    clock.tick(60)
    pygame.display.update()