import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    
  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
  def update(self, dt):
    self.position += self.velocity * dt
  
  def split(self):
    self.kill()
    if self.radius < ASTEROID_MIN_RADIUS:
      return []
    
    angle = random.uniform(20, 50)
    new_velocity1 = self.velocity.rotate(angle)
    new_velocity2 = self.velocity.rotate(-angle)
    new_radius = self.radius / 2
    
    new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid1.velocity = new_velocity1 * 1.2
    
    new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid2.velocity = new_velocity2 * 1.2
    
    return [new_asteroid1, new_asteroid2]
  
  