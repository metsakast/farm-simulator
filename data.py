from item import *
from soil import *

global inventory
global soils
global selected_item
global money

inventory = [Item("Sickle"), Item("Watercan"), Item("Carrot"), Item("Wheat")]
soils = [Soil(i) for i in range(36)]

selected_item = 0
money = 1000
workers = 0
