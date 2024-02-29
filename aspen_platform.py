import pygame

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
			sub_group.add(self)
		elif image_integer == 3:
			self.image = pygame.image.load('images/tiles/water.png')
			sub_group.add(self)

		# add every tile to main tile group
		main_group.add(self)

		# Get rect of images and position within the grid
		self.rect = self.image.get_rect()
		self.rect.topleft = (x,y)



# Define our sprite groups
main_tile_group = pygame.sprite.Group()
grass_tile_group = pygame.sprite.Group()
water_tile_group = pygame.sprite.Group()


# Create a tile map, nested python list: 0=no tile, 1=dirt, 2=grass, 3=water
tile_map = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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







# Game Loop
running = True
while running:
	# Check to quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# fill the display
	display_surface.fill("black")

	# Draw the Tiles
	main_tile_group.draw(display_surface)


	# Update Display
	pygame.display.update()
	clock.tick(FPS)

# End the game
pygame.quit()