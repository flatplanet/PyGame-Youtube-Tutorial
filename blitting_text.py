import pygame

# Pygame Setup Stuff
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Codemy.com Pygame Tutorial')
clock = pygame.time.Clock()
running = True


dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Display All Our Fonts
fonts = pygame.font.get_fonts()
#for font in fonts:
	#print(font)

# Define the fonts
system_font = pygame.font.SysFont('imapct', 80)
downloaded_font = pygame.font.Font('DangerNightPersonalUse-owdl4.otf', 80)

# Render the text (as surfave) Text, boolean for antialiasing, text color, bg color
system_font = system_font.render("This is Impact!", True, "blue", "silver")
downloaded_font = downloaded_font.render("This is Danger!!", True, "blue", "silver")

# Get Rect
system_font_rect = system_font.get_rect()
downloaded_font_rect = downloaded_font.get_rect()

# Position the text
system_font_rect.center = (WINDOW_WIDTH//2, 100)
downloaded_font_rect.center = (WINDOW_WIDTH//2, 200)


# load our images
hero_right = pygame.image.load("hero_right.png")
hero_left = pygame.image.load("hero_left.png")

# get rect surrounding our images
hero_right_rect = hero_right.get_rect()
hero_left_rect = hero_left.get_rect()

# Position our images
hero_right_rect.topleft = (0,0)
hero_left_rect.topright = (WINDOW_WIDTH, 0)



while running:
	# poll for events
	# pygame.QUIT event means that the user clicked the X to close the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Pick the screen color
	screen.fill("silver")

	# RENDER OUR GAME HERE
	# pygame.draw.circle(screen, "#033660", player_pos, 40)

	# Blit text onto screen
	screen.blit(system_font, system_font_rect)
	screen.blit(downloaded_font, downloaded_font_rect)

	# Blit (copy) screen object at a given coordinates
	screen.blit(hero_right, hero_right_rect)
	screen.blit(hero_left, hero_left_rect)

	

	# Move our circle
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		hero_right_rect.y -= 300 * dt
	if keys[pygame.K_DOWN]:
		hero_right_rect.y += 300 * dt

	if keys[pygame.K_LEFT]:
		hero_right_rect.x -= 300 * dt
	if keys[pygame.K_RIGHT]:
		hero_right_rect.x += 300 * dt
		
	# flip the display to output our work to the screen
	pygame.display.flip()


	# Set the clock stuff / delta time in seconds since the last frame
	# used for framerate independent physics
	dt = clock.tick(60) / 1000




pygame.quit()