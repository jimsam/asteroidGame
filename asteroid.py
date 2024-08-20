import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "red", pygame.Vector2(self.position), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            rnd_angle = random.randint(20, 50)
            angled_V1 = pygame.Vector2(self.velocity).rotate(rnd_angle)
            angled_V2 = pygame.Vector2(self.velocity).rotate(-rnd_angle)
            smaller_radius = self.radius - ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x, self.position.y, smaller_radius)
            split2 = Asteroid(self.position.x, self.position.y, smaller_radius)
            split1.velocity = angled_V1 * 1.2
            split2.velocity = angled_V2 * 1.2
            self.kill()
