from simulation.config.config import (
    GRASS_PROBABILITY, TREE_PROBABILITY, ROCK_PROBABILITY,
    HERBIVORE_PROBABILITY, PREDATOR_PROBABILITY,
    HERBIVORE_HP, HERBIVORE_SPEED,
    PREDATOR_HP, PREDATOR_SPEED, PREDATOR_DAMAGE
)
from simulation.entities.creatures import (
    Herbivore, Predator
)
from simulation.entities.entity import (
    Grass, Rock, Tree
)

class EntityCreator:

    _entities = {
        GRASS_PROBABILITY : Grass(),
        TREE_PROBABILITY : Tree(),
        ROCK_PROBABILITY : Rock(),
        HERBIVORE_PROBABILITY : Herbivore(),
        PREDATOR_PROBABILITY : Predator(),
    }

    def create_entity(self):
        return 