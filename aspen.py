import pygame
import random

# Pygame Setup Stuff
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Codemy.com - Feed Aspen')
clock = pygame.time.Clock()
running = True
# Create Variables to keep track of score and lives
score = 0
lives = 5
speed = 5
playsound = True

dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Define Backgound Music
pygame.mixer.music.load('sounds/bg.wav')

# Play Background Music
pygame.mixer.music.play(-1, 0.0)

# Define Sound Effects
hit_sound = pygame.mixer.Sound('sounds/dog.mp3')
miss_sound = pygame.mixer.Sound('sounds/aww.mp3')
game_over_sound = pygame.mixer.Sound('sounds/game_over.mp3')


# Define the fonts
title_font = pygame.font.SysFont('impact', 40)
score_font = pygame.font.SysFont('impact', 25)
lives_font = pygame.font.SysFont('impact', 25)
game_over_font = pygame.font.SysFont('impact', 75)
restart_game_font = pygame.font.SysFont('impact', 40)

# Render the text (as surface) Text, boolean for antialiasing, text color, bg color
title_text = title_font.render("Feed Aspen!", True, "#3d5f9f", "silver")
score_text = score_font.render(f"Score: {score}", True, "#3d5f9f", "silver")
lives_text = lives_font.render(f"Lives: {lives}", True, "#3d5f9f", "silver")
game_over_text = game_over_font.render("Game Over", True, "#3d5f9f", "silver")
restart_game_text = restart_game_font.render("Press 'p' To Play Again...", True, "#3d5f9f", "silver")

# Get Text Rect
title_text_rect = title_text.get_rect()
score_text_rect = score_text.get_rect()
lives_text_rect = lives_text.get_rect()
game_over_text_rect = game_over_text.get_rect()
restart_game_text_rect = restart_game_text.get_rect()


# Position the text
title_text_rect.center = (WINDOW_WIDTH/2, 30)
score_text_rect.topleft = (10,5)
lives_text_rect.topleft = ((WINDOW_WIDTH - lives_text.get_width() - 10), 5)
game_over_text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
restart_game_text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 90)


# load our images
aspen = pygame.image.load('images/aspen2.png') 
food = pygame.image.load('images/food2.png')

# get rect surrounding our images
aspen_rect = aspen.get_rect()
food_rect = food.get_rect()


# Position our images
aspen_rect.center = (60, WINDOW_HEIGHT/2)
food_rect.x = WINDOW_WIDTH + 100
food_rect.y = random.randint(65, (WINDOW_HEIGHT - food.get_height()))


while running:
	# poll for events
	# pygame.QUIT event means that the user clicked the X to close the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Pick the screen color
	screen.fill("silver")

	
	# Blit text onto screen
	screen.blit(title_text, title_text_rect)
	screen.blit(score_text, score_text_rect)
	screen.blit(lives_text, lives_text_rect)


	# Check if we're out of lives
	if lives == 0:
		# Game over text
		screen.blit(game_over_text, game_over_text_rect)
		screen.blit(restart_game_text, restart_game_text_rect)
		# Stop The Food From Moving again
		food_rect.x = WINDOW_WIDTH + 100
		#food_rect.y = 10000
		
		if playsound:
			# Play game over sound
			game_over_sound.play()
			# Turn off bg music
			pygame.mixer.music.stop()
			# Turn music loop off
			playsound = False

		# Check for p to restart game
		keys = pygame.key.get_pressed()
		if keys[pygame.K_p]:
			# Update game start variables
			score = 0
			lives = 5
			speed = 5
			playsound = True

			# re-render the score and lives
			score_text = score_font.render(f"Score: {score}", True, "#3d5f9f", "silver")
			lives_text = lives_font.render(f"Lives: {lives}", True, "#3d5f9f", "silver")

			# Play Background Music
			pygame.mixer.music.play(-1, 0.0)

	# Blit images onto screen
	screen.blit(aspen, aspen_rect)
	screen.blit(food, food_rect)

	# Draw Line at top of the screen
	pygame.draw.line(screen, "#3d5f9f", (0, 60), (WINDOW_WIDTH, 60), 2)


	# Move Our Images
	keys = pygame.key.get_pressed()
	
	# Move Aspen
	if keys[pygame.K_UP] and aspen_rect.y > 70:
		aspen_rect.y -= 300 * dt
	if keys[pygame.K_DOWN] and aspen_rect.y < WINDOW_HEIGHT - aspen.get_height() - 5:
		aspen_rect.y += 300 * dt
	
	# Move Food
	if food_rect.x < 0:
		# Aspen Missed the Food!
		# Play sound
		miss_sound.play()
		# Lose a life
		lives -= 1
		# Update Lives On Screen
		lives_text = lives_font.render(f"Lives: {lives}", True, "#3d5f9f", "silver")
		food_rect.x = WINDOW_WIDTH + 100
		food_rect.y = random.randint(65, (WINDOW_HEIGHT - food.get_height()))
	else:
		# Move The food to the left
		food_rect.x -= speed


	# Check for collisions
	if aspen_rect.colliderect(food_rect):
		# Play sound
		hit_sound.play()

		# Increase the score
		score += 1
		speed += 2

		# Update Score Text
		score_text = score_font.render(f"Score: {score}", True, "#3d5f9f", "silver")
		food_rect.x = WINDOW_WIDTH + 100
		food_rect.y = random.randint(65, (WINDOW_HEIGHT - food.get_height()))		

	

	# flip the display to output our work to the screen
	pygame.display.flip()


	# Set the clock stuff / delta time in seconds since the last frame
	# used for framerate independent physics
	dt = clock.tick(60) / 1000




pygame.quit()