import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable_group = pygame.sprite.Group()
	drawable_group = pygame.sprite.Group()
	asteroid_group = pygame.sprite.Group()
	shot_group = pygame.sprite.Group()

	Player.containers = (updatable_group, drawable_group)
	Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
	AsteroidField.containers = (updatable_group)
	Shot.containers = (shot_group, updatable_group, drawable_group)

	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	asteroidfield = AsteroidField()

	d_time = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill('black')

		for sprite in updatable_group:
			sprite.update(d_time)

		for asteroid in asteroid_group:
			if player.collides_with(asteroid):
				print("Game over!")
				exit()
			for shot in shot_group:
				if asteroid.collides_with(shot):
					shot.kill()
					asteroid.split()

		for sprite in drawable_group:
			sprite.draw(screen)
		
		pygame.display.flip()

		# limit to 60 FPS
		d_time = clock.tick(60) / 1000


if __name__ == "__main__":
	main()

