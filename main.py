import pygame
import settings
import entities
import operations

#Initialization
GAME_WINDOW = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Proj1")
running = True
CLOCK = pygame.time.Clock()

turret = entities.Point((settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2))
crosshair = entities.Point((2, 2))
line = entities.Line(turret, crosshair)

target1 = operations.gen_target()
target2 = operations.gen_target()
target_list = [target1, target2]


while running:
    pygame.draw.rect(GAME_WINDOW, "black", (0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    for target in target_list:
        target.show(GAME_WINDOW)
    
    mouse_coords = pygame.mouse.get_pos()
    crosshair.set_x(mouse_coords[0])
    crosshair.set_y(mouse_coords[1])
    
    turret.show(GAME_WINDOW)
    crosshair.show(GAME_WINDOW)
    
    line.show_to_end1(GAME_WINDOW)

    operations.move_active(turret)
     
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_SPACE:
                num_hit = operations.fire(turret, crosshair, target_list)
                
            
    pygame.display.update()
    CLOCK.tick(60)
            
pygame.quit()