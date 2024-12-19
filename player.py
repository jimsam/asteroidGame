import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOTING_RATE,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.shooting_cd = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation + 180)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90)
        right = right.normalize() * self.radius
        a = self.position + (forward * self.radius)
        b = self.position - (forward * self.radius) - (right)
        c = self.position - (forward * self.radius) + (right)
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.shooting_cd > -1:
            self.shooting_cd -= dt

        if keys[pygame.K_a]:
            self.horizontal_move(-dt)
        if keys[pygame.K_d]:
            self.horizontal_move(dt)
        if keys[pygame.K_w]:
            self.vertical_move(-dt)
        if keys[pygame.K_s]:
            self.vertical_move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def vertical_move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def horizontal_move(self, dt):
        side = pygame.Vector2(1, 0).rotate(self.rotation)
        self.position += side * PLAYER_SPEED * dt

    def shoot(self):
        if self.shooting_cd > 0:
            return
        self.shooting_cd = PLAYER_SHOOTING_RATE
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = (
            pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        )
