import pygame, random, data
from constants import *
from item import *
from ui import *

pygame.display.set_caption("Farm Simulator")

screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

soil_texture = pygame.image.load("assets\\soiltexture.png").convert()
soil_texture = pygame.transform.scale(soil_texture, (100, 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            for index, soil in enumerate(data.soils):
                if soil.rect.collidepoint(mouse_pos):
                    if data.selected_item in range(len(data.inventory)):
                        if data.inventory[data.selected_item].name == "Watercan":
                            soil.fertilization = min(soil.fertilization + 15, 90)
                            watercan.play()
                            break
                        elif data.inventory[data.selected_item].name == "Sickle":
                            if soil.current_crop:
                                soil.remove_crop()
                                sickle.play()
                            break
                        elif data.inventory[data.selected_item].type == "Crop":
                            if not soil.current_crop:
                                soil.add_crop(data.inventory[data.selected_item])
                                plant.play()
                            break

            for index, inventory_slot in enumerate(inventory_slots):
                if inventory_slot.collidepoint(mouse_pos):
                    data.selected_item = index
                    break
            
            for button, name in marketplace_buttons:
                if button.collidepoint(mouse_pos):
                    if len(data.inventory) >= 27: break
                    if data.money >= market_prices[name]:
                        data.money -= market_prices[name]
                        data.inventory.append(Item(name))
                        purchase.play()
                    break

    screen.fill(grass_color)
    
    for soil in data.soils:
        soil.fertilization = max(0, soil.fertilization - fertilization_decay)
        fertilization_layer = pygame.Surface((100, 100))
        fertilization_layer.set_alpha(soil.fertilization)
        screen.blit(soil_texture, (soil.rect.x, soil.rect.y))
        screen.blit(fertilization_layer, (soil.rect.x, soil.rect.y))

        if soil.current_crop:
            crop_texture = pygame.image.load("assets\\carrot1.png").convert_alpha()
            crop_texture = pygame.transform.scale(crop_texture, (100, 100))
            screen.blit(crop_texture, (soil.rect.x, soil.rect.y))
    
    loadUI(screen)

    pygame.display.flip()
    clock.tick(30)
