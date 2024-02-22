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
	def __init__(self, aspen_group, food_group, bone_group):
		self.bone_group = bone_group
		self.aspen_group = aspen_group
		self.food_group = food_group
		self.score = 0
		self.lives = 5
		# Define Fonts
		self.small_font = pygame.font.SysFont("impact", 24)
		self.big_font = pygame.font.SysFont("impact", 60)

		# Define our food images
		self.blue_food = pygame.image.load("images/food2.png")
		self.red_food = pygame.image.load("images/food.png")

		# Add food to our food group
		# Food Type: 0=blue, 1=red
		#self.food_group.add(Food((random.randint(0,800)),(random.randint(100,200)), self.red_food, 1))
		for i in range(8):
			self.food_group.add(Food(i*100,200, self.blue_food, 0))

		# Define our sounds
		self.score_sound = pygame.mixer.Sound('sounds/dog.mp3')
		self.die_sound = pygame.mixer.Sound('sounds/aww.mp3')
		self.game_over_sound = pygame.mixer.Sound('sounds/game_over.mp3')


	def update(self):
		self.check_collisions()
		self.draw()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_p]:
			self.pause_game()

	def draw(self):
		pygame.draw.rect(screen, "#003660", (0,100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 4)

		# Text
		title_text = self.big_font.render("FEED ASPEN!", True, "#003660")
		title_rect = title_text.get_rect()
		title_rect.centerx = WINDOW_WIDTH/2
		title_rect.top = 5

		win_text = self.big_font.render("YOU WIN!", True, "red")
		win_rect = win_text.get_rect()
		win_rect.centerx = WINDOW_WIDTH/2
		win_rect.centery = WINDOW_HEIGHT/2 - 100

		lose_text = self.big_font.render("YOU LOSE!", True, "red")
		lose_rect = lose_text.get_rect()
		lose_rect.centerx = WINDOW_WIDTH/2
		lose_rect.centery = WINDOW_HEIGHT/2 - 100

		restart_text = self.big_font.render("Press Enter To Play Again", True, "red")
		restart_rect = restart_text.get_rect()
		restart_rect.centerx = WINDOW_WIDTH/2
		restart_rect.centery = WINDOW_HEIGHT/2

		score_text = self.small_font.render("Score: " + str(self.score), True, "#003660")
		score_rect = score_text.get_rect()
		score_rect.topleft = (5,5)
		
		lives_text = self.small_font.render("Lives: " + str(self.lives), True, "#003660")
		lives_rect = lives_text.get_rect()
		lives_rect.topright = (WINDOW_WIDTH - 5, 5)

		# Blit The Text
		screen.blit(title_text, title_rect)
		screen.blit(score_text, score_rect)
		screen.blit(lives_text, lives_rect)

		if self.score == 8:
			# Add Game over Text
			screen.blit(win_text, win_rect)
			screen.blit(restart_text, restart_rect)
			# Restart Game
			self.game_over()

		if self.lives == 0:
			# Add Game over Text
			screen.blit(lose_text, lose_rect)
			screen.blit(restart_text, restart_rect)
			# Remove Any remaining Food
			self.food_group.remove(food_group)
			# Restart Game
			self.game_over()

	def game_over(self):
		self.aspen_group.reset()
		# Check For Restart Enter
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RETURN]:
			# Reset numbers
			self.score = 0
			self.lives = 5
			# Add new food to the screen
			#self.food_group.add(Food((random.randint(0,800)),(random.randint(100,200)), self.red_food, 1))
			for i in range(8):
				self.food_group.add(Food(i*100,200, self.blue_food, 0))

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
		if pygame.sprite.groupcollide(self.bone_group, self.food_group, True, True):
			# Increase the score
			self.score += 1
			# Play the score sound
			self.score_sound.play()

		'''
		caught_food = pygame.sprite.spritecollideany(self.aspen_group, self.food_group)
		if caught_food:
			# Check type of food, red/blue
			if caught_food.type == 0:
				# Blue
				# Play Die Sound
				self.die_sound.play()
				# Lose a life
				self.lives -= 1
				# Move Aspen Back Under Box
				self.aspen_group.reset()
				# Play Game Over Sound
				if self.lives == 0:
					# Play sound
					self.game_over_sound.play()
			else:

				# Play Score sound
				self.score_sound.play()
				caught_food.remove(self.food_group)
				# Increase the score
				self.score += 1
				
				# Logic to remove blue and add red
				if len(self.food_group) > 0:
					# Randomly Remove Blue Food From Sprites in Food Group
					random.choice(self.food_group.sprites()).kill()

					if len(self.food_group) >=1:
						# Add a new red food
						self.food_group.add(Food((random.randint(0,800)),(random.randint(100,200)), self.red_food, 1))
					else:
						self.aspen_group.reset()
						self.game_over_sound.play()
		'''

# Define an Aspen Class
class Aspen(pygame.sprite.Sprite):
	def __init__(self, x, y, bone_group):
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
		# Define the bone group
		self.bone_group	= bone_group

	# Fire the bones
	def fire(self):
		# Restrict number of shots fired
		#if len(self.bone_group) < 2:

		# Fire the bone
		AspenBone(self.rect.centerx, self.rect.top, self.bone_group)

	def update(self):
		self.move()
		#self.check_collisions()

	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and self.rect.x >= 10:
			self.rect.x -= self.velocity
		if keys[pygame.K_RIGHT] and self.rect.x <= WINDOW_WIDTH - 95:
			self.rect.x += self.velocity
		'''
		if keys[pygame.K_UP] and self.rect.y >= 110:
			self.rect.y -= self.velocity
		if keys[pygame.K_DOWN] and self.rect.y <= WINDOW_HEIGHT - 95:
			self.rect.y += self.velocity
		'''
		
	# Reset Aspen back below the box
	def reset(self):
		self.rect.topleft = (200, 510)

	#def check_collisions(self):
	#	if pygame.sprite.spritecollide(self, self.food_group, True):
	#		print(len(self.food_group))

# Create Aspen Bone Class
class AspenBone(pygame.sprite.Sprite):
	def __init__(self, x, y, bone_group):
		super().__init__()
		# Define our image
		self.image = pygame.image.load("images/bone.png")
		# Create Rect
		self.rect = self.image.get_rect()
		# X Y coordinates
		self.rect.centerx = x
		self.rect.centery = y
		# velocity of moving bone
		self.velocity = 10
		bone_group.add(self)

	def update(self):
		# Move the bone after shooting
		self.rect.y -= self.velocity
		# Delete the bone when it reaches the top of the blue box
		if self.rect.top < 100:
			self.kill()
			# Lose a life
			our_game.lives -= 1
			# Die sound
			our_game.die_sound.play()


# Define an Food Class
class Food(pygame.sprite.Sprite):
	def __init__(self, x, y, image, food_type):
		super().__init__()
		# Define our image
		self.image = image
		# Get Rect
		self.rect = self.image.get_rect()
		# Position the image
		self.rect.topleft = (x,y)
		# Move the image
		self.velocity = random.randint(1, 5)

		# Food Type: 0=blue, 1=red
		self.type = food_type

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
#for i in range(8):
#	food = Food(i*100, 200)
#	food_group.add(food)

# Create bone group
bone_group = pygame.sprite.Group()

# Create aspen group
aspen_group = pygame.sprite.Group()
# Create and position aspen
aspen = Aspen(200,510, bone_group)
# Add aspen to the group
aspen_group.add(aspen)

# Create Game Object
our_game = Game(aspen, food_group, bone_group)


while running:
	# poll for events
	# pygame.QUIT event means that the user clicked the X to close the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		# Fire the bone with space bar
		if our_game.lives > 0:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					aspen.fire()

	# Pick the screen color
	screen.fill("silver")

		
	# Blit (copy) screen object at a given coordinates
	# screen.blit(aspen, aspen_rect)

	# Draw and Move Food and Aspen sprite and bone group
	food_group.update()
	food_group.draw(screen)

	aspen_group.update()
	aspen_group.draw(screen)

	bone_group.update()
	bone_group.draw(screen)

	# Update Game Instance
	our_game.update()
	

	# flip the display to output our work to the screen
	pygame.display.flip()


	# Set the clock stuff / delta time in seconds since the last frame
	# used for framerate independent physics
	dt = clock.tick(60) / 1000




pygame.quit()