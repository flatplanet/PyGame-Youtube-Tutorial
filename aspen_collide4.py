import pygame
import random

# Pygame Setup Stuff
pygame.init()
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Codemy.com - Aspen Classes')
clock = pygame.time.Clock()
running = True

dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Define a Game Class
class Game():
	def __init__(self, aspen_group, food_group):
		self.aspen_group = aspen_group
		self.food_group = food_group
		self.score = 0

	def update(self):
		self.check_collisions()
		self.draw()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_p]:
			self.pause_game()

	def draw(self):
		pygame.draw.rect(screen, "#003660", (0,100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 4)





	def pause_game(self):
		global running 

		is_paused = True
		# Create pause loop
		while is_paused:
			# Account For Hitting Enter to unPause
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						is_paused = False
				# Account for clicking the X to quit
				if event.type == pygame.QUIT:
					is_paused = False
					running = False
					#pygame.quit()





	def check_collisions(self):
		if pygame.sprite.groupcollide(self.aspen_group, self.food_group, False, True):
			#print(len(self.food_group))
			self.score +=1
			print(self.score)

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
		self.velocity = 5
		# Add food group to aspen class
		# self.food_group = food_group

	def update(self):
		self.move()
		#self.check_collisions()

	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.rect.x -= self.velocity
		if keys[pygame.K_RIGHT]:
			self.rect.x += self.velocity
		if keys[pygame.K_UP]:
			self.rect.y -= self.velocity
		if keys[pygame.K_DOWN]:
			self.rect.y += self.velocity


	#def check_collisions(self):
	#	if pygame.sprite.spritecollide(self, self.food_group, True):
	#		print(len(self.food_group))




# Define an Food Class
class Food(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		# Define our image
		self.image = pygame.image.load("images/food2.png")
		# Get Rect
		self.rect = self.image.get_rect()
		# Position the image
		self.rect.topleft = (x,y)
		# Move the image
		self.velocity = random.randint(1, 5)
		# Create Random Motion
		self.dx = random.choice([-1,1])
		self.dy = random.choice([-1,1])

	def update(self):
		#self.rect.y += self.velocity
		self.rect.x += self.dx * self.velocity
		self.rect.y += self.dy * self.velocity

		# Keep from leaving the screen
		if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
			self.dx = -1 * self.dx
		if self.rect.top <= 100 or self.rect.bottom >= 500:
			self.dy = -1 * self.dy


# Create an food group
food_group = pygame.sprite.Group()

# Create 5 aspens
for i in range(8):
	food = Food(i*100, 200)
	food_group.add(food)

# Create aspen group
aspen_group = pygame.sprite.Group()
# Create and position aspen
aspen = Aspen(200,510)
# Add aspen to the group
aspen_group.add(aspen)

# Create Game Object
our_game = Game(aspen_group, food_group)


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

	# Draw and Move Food and Aspen sprite
	food_group.update()
	food_group.draw(screen)

	aspen_group.update()
	aspen_group.draw(screen)

	# Update Game Instance
	our_game.update()
	

	# flip the display to output our work to the screen
	pygame.display.flip()


	# Set the clock stuff / delta time in seconds since the last frame
	# used for framerate independent physics
	dt = clock.tick(60) / 1000




pygame.quit()