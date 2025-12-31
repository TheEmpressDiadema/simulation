MAP_HEIGHT = 3
MAP_WIDTH = 3

FREE_CELL_ICON = "🟩"

TREE_ICON = "🌳"

ROCK_ICON = "⛰️\u200A"

GRASS_ICON = "🌿"

HERBIVORE_ICON = "🐇"
HERBIVORE_SPEED = 3
HERBIVORE_HP = 10

PREDATOR_ICON = "🦊"
PREDATOR_SPEED = 4
PREDATOR_HP = 10
PREDATOR_DAMAGE = 5

MAX_ENTITY_COUNT = {
    "Tree": (MAP_HEIGHT * MAP_WIDTH) // 10,
    "Rock": (MAP_HEIGHT * MAP_WIDTH) // 10,
    "Grass": max((MAP_HEIGHT * MAP_WIDTH) // 10, 1),
    "Predator": max((MAP_HEIGHT * MAP_WIDTH) // 15, 1),
    "Herbivore": max((MAP_HEIGHT * MAP_WIDTH) // 10, 1),
}
