from circleshape import CircleShape
import pygame
import constants
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt): 
        self.position += self.velocity * dt
            
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        first_vector = pygame.math.Vector2.rotate(self.velocity, random_angle)
        second_vector = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        split_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_a.velocity = first_vector * 1.2
        split_asteroid_b.velocity = second_vector * 1.2

