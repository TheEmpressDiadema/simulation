from abc import ABC

from constants.properties import (
    PREDATOR_HEALTH_POINTS, PREDATOR_DAMAGE, PREDATOR_MOVE_SPEED,
    HERBIVORE_HEALTH_POINTS, HERBIVORE_MOVE_SPEED
)

class CreatureAttributes(ABC):

    health_points: int
    move_speed: int


class PredatorAttributes(CreatureAttributes):

    health_points = PREDATOR_HEALTH_POINTS
    move_speed = PREDATOR_MOVE_SPEED
    damage = PREDATOR_DAMAGE


class HerbivoreAttributes(CreatureAttributes):

    health_points = HERBIVORE_HEALTH_POINTS
    move_speed = HERBIVORE_MOVE_SPEED