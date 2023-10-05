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


while running:
	# poll for events
	# pygame.QUIT event means that the user clicked the X to close the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Pick the screen color
	screen.fill("silver")

	# UNDERSTAND CO-ORDINATES
	# Top Left Corner is 0,0
	# as we move -> X increases, as you go down Y increases

	# Draw a line
	# (screen, color, starting point (x,y), ending point(x,y), thickness)
	pygame.draw.line(screen, "black", (0,50), (800,50), 2)

	# Draw a circle
	# (screen, color, center(x,y), radius, thickness: 0=fill)
	pygame.draw.circle(screen, "black", (WINDOW_WIDTH/2, WINDOW_HEIGHT/2), 100, 5)

	# Draw a rectangle
	# (screen, color, (top-left x, top-left y, width, height))
	pygame.draw.rect(screen, "red", (100, 200, 100, 100))



	# flip the display to output our work to the screen
	pygame.display.flip()


	# Set the clock stuff / delta time in seconds since the last frame
	# used for framerate independent physics
	dt = clock.tick(60) / 1000




pygame.quit()