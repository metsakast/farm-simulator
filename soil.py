import pygame

class Soil:
    def __init__(self, index):
        self.fertilization = 0
        self.rect = pygame.Rect((index%6)*105, 3+(index//6)*105, 100, 100)
        self.current_crop = None
        pass

    def add_crop(self, crop):
        self.current_crop = crop

    def remove_crop(self):
        self.current_crop = None
