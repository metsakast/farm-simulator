import pygame

class Soil:
    def __init__(self, index):
        self.fertilization = 0
        self.rect = pygame.Rect((index%6)*105, 3+(index//6)*105, 100, 100)
        self.current_crop = None
        self.growth_timer = 0

    def add_crop(self, crop):
        self.current_crop = crop
        self.growth_timer = crop.grow_time

    def remove_crop(self):
        self.current_crop = None
