import pygame
import operations
import math
import settings

class Point:
    def __init__(self, coords: tuple[int, int]):
        
        self.x = coords[0]
        self.y = coords[1]
        self.velocity_x = 0
        self.velocity_y = 0
        
    def __def__(self):
        print("Point deleted")

    def get_coords(self) -> tuple[int, int]:
        return (self.x, self.y)
    
    def set_x(self, num: int):
        self.x = num
    
    def set_y(self, num: int):
        self.y = num
    
    def show(self, surface):
        pygame.draw.circle(surface, "white", self.get_coords(), 5, 1)
        
    def move(self, x_vel, y_vel):
        ''' takes an x value and a y value and changes the point's position
        by each value. X pos is right, Y pos is up.
        '''
        self.x += x_vel
        self.y -= y_vel
        # Keep within borders
        if self.x < 0:
            self.x = 0
        elif self.x > settings.SCREEN_WIDTH:
            self.x = settings.SCREEN_WIDTH
        if self.y < 0:
            self.y = 0
        elif self.y > settings.SCREEN_HEIGHT:
            self.y = settings.SCREEN_HEIGHT
        
    def move_and_bounce(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        if operations.is_out_of_bounds_x(self):
            if self.x >= settings.SCREEN_WIDTH:
                self.x = 2*settings.SCREEN_WIDTH - self.x
            else:
                self.x = -1*self.x
            self.velocity_x *= -1
            
        if operations.is_out_of_bounds_y(self):
            if self.y >= settings.SCREEN_HEIGHT:
                self.y = 2*settings.SCREEN_WIDTH - self.y
            else:
                self.y = -1*self.y
            self.velocity_y *= -1
            
    def set_velocity_x(self, new_vel: int):
        self.velocity_x = new_vel
    
    def set_velocity_y(self, new_vel: int):
        self.velocity_y = new_vel
                        
class Line:
    def __init__(self, point1: Point, point2: Point):
        
        self.point1 = point1
        self.point2 = point2
        self.rotate_rad = math.pi/180
        
    def __del__(self):
        print("Line deleted")
        
    def get_length(self) -> float:
        
        dist_x = self.point2.get_coords()[0] - self.point1.get_coords()[0]
        dist_y = self.point1.get_coords()[1] - self.point2.get_coords()[1]
        
        return (dist_x**2 + dist_y**2)**(1/2)
        
    def get_slope(self): # Slope, or "up" or "down"
        return operations.get_slope(self.point1.get_coords(), self.point2.get_coords())
    
    def show_to_end1(self, surface):
        
        end_point = operations.get_end_point(self.point1.get_coords(), 
                                             self.point2.get_coords())
        pygame.draw.line(surface, "orange", self.point1.get_coords(), end_point)
        
    def show_to_end2(self, surface):
        end_point = operations.get_end_point(self.point2.get_coords(), 
                                             self.point1.get_coords())
        pygame.draw.line(surface, "blue", self.point2.get_coords(), end_point)        
        
    def show(self, surface):
        pygame.draw.line(surface, "green", self.point1.get_coords(), self.point2.get_coords())
        
class Box:
    def __init__(self, x, y, width, height):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def get_coords(self):
        return (self.x, self.y)
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
        
    def show(self, surface):
        pygame.draw.rect(surface, "crimson", (self.x, self.y, self.width, self.height), 1)
        
    def set_x(self, num: int):
        self.x = num
    
    def set_y(self, num: int):
        self.y = num
        
    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        if operations.is_out_of_bounds_x(self):
            self.velocity_x *= -1
        if operations.is_out_of_bounds_y(self):
            self.velocity_y *= -1
            
    def set_velocity_x(self, new_vel: int):
        self.velocity_x = new_vel
    
    def set_velocity_y(self, new_vel: int):
        self.velocity_y = new_vel
    
    def __del__(self):
        print("Target deleted")
        
class TextBox:
    
    def __init__(self, text, size, font_colour, background_colour, x, y):
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.text = text
        self.font_colour = font_colour
        self.background_colour = background_colour
        self.x = x
        self.y = y
        
    def set_text(self, text):
        self.text = text
        
    def set_colours(self, font_colour, background_colour):
        self.font_colour = font_colour
        self.background_colour = background_colour
        
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
        
    def get_text(self):
        return self.text
    
    def get_colours(self):
        return (self.font_colour, self.background_colour)
        
    def get_text_so():
        text_so = font.render(text, True, font_colour, background_color)
    
    def get_coords():
        return (x, y)
    
    def show(self, surface):
        text_so = self.font.render(self.text, True, self.font_colour, self.background_colour)
        text_rect = text_so.get_rect()
        text_rect.topright = (self.x, self.y)
        surface.blit(text_so, text_rect)