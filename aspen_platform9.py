import pygame

# Define a 2d Vector
vector = pygame.math.Vector2

#Initialize the game
pygame.init()

# Set display surface (divisible by 32 tile size)
WINDOW_WIDTH = 960 # 30 columns
WINDOW_HEIGHT = 640 # 20 rows
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Aspen Platformer - Codemy.com")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Tile Class
class Tile(pygame.sprite.Sprite):
	# Read and Create tiles and put em on the screen
	def __init__(self, x, y, image_integer, main_group, sub_group=""):
		super().__init__()
		# Load image and add to the tile subgroups
		if image_integer == 1:
			self.image = pygame.image.load('images/tiles/dirt.png')
		elif image_integer == 2:
			self.image = pygame.image.load('images/tiles/grass.png')
			# Create a mask for the grass
			self.mask = pygame.mask.from_surface(self.image)
			sub_group.add(self)
		elif image_integer == 3:
			self.image = pygame.image.load('images/tiles/water.png')
			sub_group.add(self)

		# add every tile to main tile group
		main_group.add(self)

		# Get rect of images and position within the grid
		self.rect = self.image.get_rect()
		self.rect.topleft = (x,y)

# Create a Bullet Class
class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, bullet_group, player):
		super().__init__()

		# set velocity
		self.velocity = 10
		self.range = 450 # Pixels before the bullet destroys

		# Load image, get rect, based on player direction
		if player.velocity.x > 0:  # facing right
			self.image = pygame.transform.scale(pygame.image.load("images/bullet.png"), (30,14))
		else:
			# Facing Left
			self.image = pygame.transform.scale(pygame.transform.flip(pygame.image.load("images/bullet.png"), True, False), (30,14)) # flip takes image, horizontal T/F, vertical T/F
			# make our velocity negative
			self.velocity = -1*self.velocity

		# rect stuff
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)

		# get our starting position for the range stuff
		self.starting_x = x

		# Add bullet group 
		bullet_group.add(self)

	def update(self):
		# Move our bullet
		self.rect.x += self.velocity

		# Destroy the bullet after it passes the range of 450
		if abs(self.rect.x - self.starting_x) > self.range:
			self.kill()






# Apsen Player Class
class Aspen(pygame.sprite.Sprite):
	def __init__(self, x, y, grass_tiles, water_tiles, bullet_group):
		super().__init__()
		# Define our aspen image
		# self.image = pygame.image.load("images/aspen2.png")

		# Set the current image
		self.current_sprite = 0 # Sprite list index number

		# Animation lists
		self.move_right_sprites = []
		self.move_left_sprites = []
		self.idle_right_sprites = []
		self.idle_left_sprites = []

		# Define our moving right sprite images
		self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Walk1.png"), (85,74)))
		self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Walk2.png"), (85,74)))
		self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Walk3.png"), (85,74)))
		self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Walk4.png"), (85,74)))
		self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Walk5.png"), (85,74)))
		self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Walk6.png"), (85,74)))
		self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Walk7.png"), (85,74)))
		self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Walk8.png"), (85,74)))
		self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Walk9.png"), (85,74)))
		self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Walk10.png"), (85,74)))

		# Define Left Moving sprites and flip em
		for sprite in self.move_right_sprites:
			self.move_left_sprites.append(pygame.transform.flip(sprite, True, False)) # Image, horizonta T/F, veritcal T/F

		# Define Idle Right
		self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Idle1.png"), (85,74)))
		self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Idle2.png"), (85,74)))
		self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Idle3.png"), (85,74)))
		self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Idle4.png"), (85,74)))
		self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Idle5.png"), (85,74)))
		self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Idle6.png"), (85,74)))
		self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Idle7.png"), (85,74)))
		self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Idle8.png"), (85,74)))
		self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Idle9.png"), (85,74)))
		self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("images/cat2/Idle10.png"), (85,74)))

		# Define Idle Left - flip em
		for sprite in self.idle_right_sprites:
			self.idle_left_sprites.append(pygame.transform.flip(sprite, True, False)) # Image, horizonta T/F, veritcal T/F


		# Set our image
		self.image = self.move_right_sprites[self.current_sprite]

		# Get rect
		self.rect = self.image.get_rect()
		# Postion aspen
		self.rect.bottomleft = (x,y)

		# Reset Aspen If She falls into the Water
		self.start_x = x
		self.start_y = y

		# Define our grass and water and bullets
		self.grass_tiles = grass_tiles
		self.water_tiles = water_tiles
		self.bullet_group = bullet_group

		# Kinematic Vectors (x,y)
		self.position = vector(x,y)
		self.velocity = vector(0,0) # Don't move to start 0,0
		self.acceleration = vector(0,0) # no speeding up or slowing down to start 0,0

		# Kinematic Constants
		self.HORIZONTAL_ACCELERATION = .5 #How quick player speeds up
		self.HORIZONTAL_FRICTION = 0.10 # friction
		self.VERTICAL_ACCELERATION = 0.5 # Gravity
		self.VERTICAL_JUMP_SPEED = 15 # Going to determine how high we can jump

	def jump(self):
		# Only want to jump when aspen is on grass 
		if pygame.sprite.spritecollide(self, self.grass_tiles, False):
			self.velocity.y = -1 * self.VERTICAL_JUMP_SPEED # jumping up so negative

	def shoot(self):
		# Create a Bullet Instance
		Bullet(self.rect.centerx, self.rect.centery, self.bullet_group, self) # x,y,bullet_group, player


	def update(self):
		# Draw a rect around our player
		# pygame.draw.rect(display_surface, "blue", self.rect, 1)

		# Create a mask
		self.mask = pygame.mask.from_surface(self.image)

		# Draw Mask (points surrounding player)
		mask_outline = self.mask.outline()
		#pygame.draw.lines(self.image, "red", True, mask_outline)


		# set the initial acceleration to 0,0 to start
		self.acceleration = vector(0, self.VERTICAL_ACCELERATION)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.acceleration.x = -1 * self.HORIZONTAL_ACCELERATION
			# Run our Animations left
			self.animate(self.move_left_sprites, .4)

		elif keys[pygame.K_RIGHT]:
			self.acceleration.x = self.HORIZONTAL_ACCELERATION
			# Run our Animations
			self.animate(self.move_right_sprites, .4)
		else:
			# Check velocity (if positive=right, if negative=left)
			if self.velocity.x > 0: # right
				self.animate(self.idle_right_sprites, .2)
			else:
				self.animate(self.idle_left_sprites, .2)

		# Calculate new Kinematics
		self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
		self.velocity += self.acceleration # (1,2) + (3,4) = (4,6)
		self.position += self.velocity + 0.5 * self.acceleration

		# Set up wraparound
		if self.position.x < 0:  #x value of position on the left side of screen
			self.position.x = WINDOW_WIDTH
		if self.position.x > WINDOW_WIDTH:  # Right side of the screen	
			self.position.x = 0

		# update rect
		self.rect.bottomleft = self.position

		# Check for collisions with Grass
		touched_platforms = pygame.sprite.spritecollide(self, self.grass_tiles, False, pygame.sprite.collide_mask) # Return a python list of tiles we touched
		if touched_platforms:
			# Only want to adjust our position on the way down, not up
			if self.velocity.y > 0:
				self.position.y = touched_platforms[0].rect.top + 1
				self.velocity.y = 0

		# Check for collisions with Water
		if pygame.sprite.spritecollide(self, self.water_tiles, False):
			print("You Died!")
			# Reset Aspen to the top of the screen - starting position
			self.position = vector(self.start_x, self.start_y)
			# Reset Velocity
			self.velocity = vector(0,0)

	def animate(self, sprite_list, speed):
		if self.current_sprite < len(sprite_list) - 1:
			self.current_sprite += speed
		else:
			self.current_sprite = 0

		# Update our image
		self.image = sprite_list[int(self.current_sprite)]






# Define our sprite groups
main_tile_group = pygame.sprite.Group()
grass_tile_group = pygame.sprite.Group()
water_tile_group = pygame.sprite.Group()
aspen_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()


# Create a tile map, nested python list: 0=no tile, 1=dirt, 2=grass, 3=water, 4=aspen
tile_map = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2],
	[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
	[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,2,2,2,2,2],
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,1,1,1,1,1]
]

# Create Tile objects from the tile map
# 2 for loops because tile map is nested. 20 i down
for i in range(len(tile_map)):
	# loop thru the 30 elements in each list, j across
	for j in range(len(tile_map[i])):
		# Check for 0,1,2,3
		if tile_map[i][j] == 1:
			# dirt
			Tile(j*32, i*32, 1, main_tile_group)
		elif tile_map[i][j] == 2:
			# grass
			Tile(j*32, i*32, 2, main_tile_group, grass_tile_group)
		elif tile_map[i][j] == 3:
			# water
			Tile(j*32, i*32, 3, main_tile_group, water_tile_group)
		elif tile_map[i][j] == 4:
			aspen = Aspen(j*32, i*32 + 32, grass_tile_group, water_tile_group, bullet_group)
			aspen_group.add(aspen)


# Add a background
bg_image = pygame.image.load('images/tiles/bg.png')
bg_image_rect = bg_image.get_rect()
bg_image_rect.topleft = (0,0)



# Game Loop
running = True
while running:
	# Check to quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		# Jump And Shoot
		if event.type == pygame.KEYDOWN:
			# Jump
			if event.key == pygame.K_SPACE:
				aspen.jump()
			# Shoot a bullet
			if event.key == pygame.K_UP:
				aspen.shoot()

	# fill the display or blit an image
	# display_surface.fill("black")
	display_surface.blit(bg_image, bg_image_rect)

	# Draw the Tiles
	main_tile_group.draw(display_surface)

	# Update and draw sprites
	aspen_group.update()
	aspen_group.draw(display_surface)

	# Update and draw the bullet sprites
	bullet_group.update()
	bullet_group.draw(display_surface)


	# Update Display
	pygame.display.update()
	clock.tick(FPS)

# End the game
pygame.quit()