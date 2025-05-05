import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	player = Player(x, y)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.collision(player) is True:
				print("Game over!")
				sys.exit()

			for shot in shots:
				if asteroid.collision(shot) is True:
					asteroid.split()
					shot.kill()

		screen.fill("black")
		for object in drawable:
			object.draw(screen)
		pygame.display.flip()

		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
