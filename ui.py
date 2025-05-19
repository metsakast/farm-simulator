import pygame, data
from constants import *
pygame.init()

inventory_slots = []
marketplace_buttons = []

#text_font = pygame.font.SysFont("Ariel", 45)
text_font = pygame.font.Font("assets\\alagard.ttf", 35)

def loadUI(screen):
    side_menu_frame = pygame.Rect(625, 0, 375, 1000)
    side_menu_innerframe = pygame.Rect(650, 25, 325, 1000)
    pygame.draw.rect(screen, (50, 50, 40), side_menu_frame)
    pygame.draw.rect(screen, (120, 115, 85), side_menu_innerframe)
    market_button = pygame.Rect(655, 30, 155, 40)
    upgrades_button = pygame.Rect(815, 30, 155, 40)
    pygame.draw.rect(screen, (50, 50, 40), market_button)
    pygame.draw.rect(screen, (50, 50, 40), upgrades_button)

    market_text = text_font.render("Market", True, (220, 220, 220))
    upgrades_text = text_font.render("Upgrades", True, (220, 220, 220))
    money_text = text_font.render(f"${data.money}", True, (220, 220, 220))
    screen.blit(market_text, (market_button.x + 5, market_button.y + 5))
    screen.blit(upgrades_text, (upgrades_button.x + 5, upgrades_button.y + 5))
    screen.blit(money_text, (655, 600))

    marketplace_buttons.clear()
    for i, item in enumerate(market_prices.items()):
        name, value = item
        item_frame = pygame.Rect(655, 75 + i*55, 315, 50)
        pygame.draw.rect(screen, (160, 150, 100), item_frame)

        name_text = text_font.render(name, True, (220, 220, 220))
        value_text = text_font.render(str(value), True, (220, 220, 220))
        screen.blit(name_text, (item_frame.x + 5, item_frame.y + 5))
        screen.blit(value_text, (item_frame.x + name_text.get_width() + 15 , item_frame.y + 5))

        marketplace_buttons.append((item_frame, name))

    worker_button_y = 75 + len(market_prices) * 55
    worker_button = pygame.Rect(655, worker_button_y, 315, 50)
    pygame.draw.rect(screen, (160, 150, 100), worker_button)
    worker_text = text_font.render("Buy Worker 100", True, (220, 220, 220))
    screen.blit(worker_text, (worker_button.x + 5, worker_button.y + 5))
    marketplace_buttons.append((worker_button, "Worker"))

    money_text = text_font.render(f"${data.money}", True, (220, 220, 220))
    workers_count_text = text_font.render(f"Workers: {data.workers}", True, (220, 220, 220))
    screen.blit(money_text, (655, 600))
    screen.blit(workers_count_text, (655 + money_text.get_width() + 30, 600))

    inventory_frame = pygame.Rect(0, 630, 1000, 370)
    inventory_innerframe = pygame.Rect(25, 655, 950, 320)
    pygame.draw.rect(screen, (50, 50, 40), inventory_frame)
    pygame.draw.rect(screen, (120, 115, 85), inventory_innerframe)

    if data.selected_item != None:
        outline = pygame.Rect(29 + (data.selected_item%9)*105, 659 + (data.selected_item//9)*105, 102, 102)
        pygame.draw.rect(screen, (255, 255, 255), outline)

    inventory_slots.clear()
    for j in range(3):
        for i in range(9):
            inventory_slot = pygame.Rect(30 + i*105, 660 + j*105, 100, 100)
            inventory_slots.append(inventory_slot)
            pygame.draw.rect(screen, (160, 150, 100), inventory_slot)

    for i, item in enumerate(data.inventory):
        item_texture = pygame.image.load(f"assets\\{item.image}").convert_alpha()
        item_texture = pygame.transform.scale(item_texture, (100, 100))
        screen.blit(item_texture, (inventory_slots[i].x, inventory_slots[i].y))