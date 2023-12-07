import pygame
import random

# Pygame Setup Stuff
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Codemy.com - Aspen Classes')
clock = pygame.time.Clock()
running = True

dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Define an Aspen Class
class Aspen(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		# Define our image
		self.image = pygame.image.load("images/aspen2.png")
		# Get Rect
		self.rect = self.image.get_rect()
		# Position the image
		self.rect.topleft = (x,y)
		# Move the image
		self.velocity = random.randint(1, 5)

	def update(self):
		self.rect.y += self.velocity



# load our images
# aspen = pygame.image.load("images/aspen2.png")

# get rect surrounding our images
# aspen_rect = aspen.get_rect()

# Position our images
# aspen_rect.center = (60,WINDOW_HEIGHT/2)

# Create an aspen group
aspen_group = pygame.sprite.Group()

# Create 5 aspens
for i in range(5):
	aspen = Aspen(i*150, 10)
	aspen_group.add(aspen)






while running:
	# poll for events
	# pygame.QUIT event means that the user clicked the X to close the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Pick the screen color
	screen.fill("silver")

		
	# Blit (copy) screen object at a given coordinates
	# screen.blit(aspen, aspen_rect)

	# Draw and Move Aspen sprite
	aspen_group.update()
	aspen_group.draw(screen)
	

	# flip the display to output our work to the screen
	pygame.display.flip()


	# Set the clock stuff / delta time in seconds since the last frame
	# used for framerate independent physics
	dt = clock.tick(60) / 1000




pygame.quit()