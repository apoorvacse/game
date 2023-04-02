import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)   #(font type, font size) 

for_surface = pygame.image.load('assests\images\kalu.jpg').convert()
ground_surface = pygame.image.load('assests\images\kk.jpg').convert()
text_surface = test_font.render('MY GAME', False,'Black') #(text,aa,color)

deer_surf= pygame.image.load('assests\images\deer.jpg').convert_alpha()
deer_rect= deer_surf.get_rect(bottomright =(600,450))
player_surf = pygame.image.load('assests\images\player_1.jpg')
player_rect = player_surf.get_rect(topright = (200,200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(for_surface,(50,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(200,20))
    deer_rect.x -= 4
    if deer_rect.right <= 0: deer_rect.left = 600
    screen.blit(deer_surf,deer_rect)
    screen.blit(player_surf,player_rect)
    # if player_rect.colliderect(deer_rect):
    #     print('collision')

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print('collision')

    pygame.display.update()
    clock.tick(60)
