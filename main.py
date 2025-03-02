import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  print("Starting Asteroids!")
  print ("Screen width:", SCREEN_WIDTH)
  print ("Screen height:", SCREEN_HEIGHT)
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  asteroidfield = AsteroidField()
  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    
    dt = clock.tick(60) / 1000
    updatable.update(dt)
    # Check if player collides with asteroids
    for asteroid in asteroids:
      if asteroid.check_collision(player):
        print("Game over!")
        exit()
    # Check if shots hit asteroids
    for asteroid in asteroids:
      for shot in shots:
        if asteroid.check_collision(shot):
          print("Shot hit asteroid!")
          shot.kill()
          asteroid.kill()
          new_asteroids = asteroid.split()
          if new_asteroids:
            asteroids.add(new_asteroids)
    
    screen.fill((0, 0, 0))
    for entity in drawable:
        entity.draw(screen)
    pygame.display.flip()
    pygame.display.set_caption(f"FPS: {clock.get_fps():.2f}")

if __name__ == "__main__":
    main()