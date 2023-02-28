import settings
import entities
import random
import pygame
def get_end_point(coords1: tuple[int, int], coords2: tuple[int, int]):
    """
    Returns the coords of the where a line drawn through both points
    will intersect the border of the window. This line starts from point1.
    
    Precondition: assumes the given points are within the window's dimensions.
    """
    left_border = 0
    right_border = settings.SCREEN_WIDTH
    top_border = 0
    bottom_border = settings.SCREEN_HEIGHT
    
    slope = get_slope(coords1, coords2)
    x1 = coords1[0]
    y1 = coords1[1]
    
    if (slope == "up"):
        y1 = top_border
    elif (slope == "down"):
        y1 = bottom_border 
    else:
        # Go until one coordinate from the first point hits the window border
        while (left_border <= x1 <= right_border and top_border <= y1 <= bottom_border):
            if (coords2[0] - coords1[0] > 0): # Decides whether to go backward or forward
                x1 += 1
                y1 -= slope
            else:
                x1 -= 1
                y1 += slope
                
    return(x1, y1)
        

def get_all_lines(point_list: list) -> list:
    i = 0
    line_list = []
    
    for i in range(len(point_list)-1):
        for point in point_list[i+1:]:
            line = entities.Line(point_list[i], point)
            line_list.append(line)
            
    return line_list
    
def is_out_of_bounds_x(point):
    
    return not (0 < point.get_coords()[0] < settings.SCREEN_WIDTH)

def is_out_of_bounds_y(point):
            
    return not (0 < point.get_coords()[1] < settings.SCREEN_HEIGHT)


def get_slope(coords1: tuple[int, int], coords2: tuple[int, int]):
    
    x1 = coords1[0]
    y1 = coords1[1]
    x2 = coords2[0]
    y2 = coords2[1]
    
    rise = y1 - y2
    run = x2 - x1

    if (run != 0):
        slope = rise/run
        return slope
                
    # Default up if points match, to adhere to the window intersection.
    else:
        if (rise >= 0):
            inf = "up"
        else:
            inf = "down"

        return inf
    
def randomize_coords(entity) -> None:
    '''
    sets entities coords to random values within 100 pixels of each border
    '''
    y_max = settings.SCREEN_HEIGHT - 100
    x_max = settings.SCREEN_WIDTH - 100
    y_min = 100
    x_min = 100
    
    random_x = random.uniform(x_min, x_max)
    random_y = random.uniform(y_min, y_max)
    entity.set_x(random_x)
    entity.set_y(random_y)

def fire(turret, cursor, target_list) -> list:
    '''
    scans each target in target list to detect if they are intersected and "hit"
    by the line drawn from the turret to the cursor to the end of the screen
    
    Returns a list of all targets hit
    '''
    hit_list = []
    slope = get_slope(turret.get_coords(), cursor.get_coords())
    turret_x, turret_y = turret.get_coords()
    cursor_x = cursor.get_coords()[0]
    
    left_border = 0
    right_border = settings.SCREEN_WIDTH
    top_border = 0
    bottom_border = settings.SCREEN_HEIGHT    
    
    for target in target_list:
        target_border_left = target.get_coords()[0]
        target_border_right = target_border_left + target.get_width()
        target_border_top = target.get_coords()[1]
        target_border_bottom = target_border_top + target.get_height()
        
        
        # Check directly up
        if slope == "up":
            if (target_border_top <= turret_y and
                target_border_left <= turret_x <= target_border_right):
                hit_list.append(target)
                
        # Check directly down
        elif slope == "down":
            if (target_border_bottom >= turret_y and
                target_border_left <= turret_x <= target_border_right):
                hit_list.append(target)
                
        # Check with slope, looking for intersection until reaching the border
        else:
            cur_x = turret_x
            prev_y = turret_y
            
            # Check to the right           
            if (turret_x < cursor_x):
                cur_y = prev_y - slope
                while (cur_x < right_border and top_border < cur_y < bottom_border):
                    # Check at each x if the top or bottom border of the target
                    # is between the current and previous y
                    # or if cur y is between top and bottom
                    if (target_border_left <= cur_x <= target_border_right and 
                        (prev_y >= target_border_top >= cur_y or 
                        prev_y <= target_border_top <= cur_y or
                        prev_y >= target_border_bottom >= cur_y or
                        prev_y <= target_border_bottom <= cur_y or
                        target_border_bottom >= cur_y >= target_border_top)):
                        
                        hit_list.append(target)
                        break
                    
                    cur_x += 1
                    prev_y = cur_y
                    cur_y -= slope                    
                    
            # Check to the left
            else:
                cur_y = prev_y + slope
                while (left_border < cur_x and top_border < cur_y < bottom_border):
                    # Ditto the one above
                    if (target_border_left <= cur_x <= target_border_right and 
                        (prev_y >= target_border_top >= cur_y or 
                        prev_y <= target_border_top <= cur_y or
                        prev_y >= target_border_bottom >= cur_y or
                        prev_y <= target_border_bottom <= cur_y or
                        target_border_bottom >= cur_y >= target_border_top)):
                        
                        hit_list.append(target)
                        break
                        
                    cur_x -= 1
                    prev_y = cur_y
                    cur_y += slope
    return hit_list

def gen_box():
    '''
    generates a new box at a random position within the borders of the screen
    by 100 pixels
    '''
    y_max = settings.SCREEN_HEIGHT - 100
    x_max = settings.SCREEN_WIDTH - 100
    y_min = 100
    x_min = 100
    
    random_x = random.uniform(x_min, x_max)
    random_y = random.uniform(y_min, y_max)
    box = entities.Box(random_x, random_y, 50, 50)
    
    return box

def randomize_coords(entity) -> None:
    '''
    moves entitiy to a random location within 100 pixels of each border
    '''
    y_max = settings.SCREEN_HEIGHT - 100
    x_max = settings.SCREEN_WIDTH - 100
    y_min = 100
    x_min = 100
    
    random_x = random.uniform(x_min, x_max)
    random_y = random.uniform(y_min, y_max)
    entity.set_x(random_x)
    entity.set_y(random_y)

def move_active(point) -> None:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        point.move(0, 2) 
    if keys[pygame.K_s]:
        point.move(0, -2) 
    if keys[pygame.K_a]:
        point.move(-2, 0) 
    if keys[pygame.K_d]:
        point.move(2, 0)     
