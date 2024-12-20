import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "yellow", pygame.Vector2(self.position), SHOT_RADIUS, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt
