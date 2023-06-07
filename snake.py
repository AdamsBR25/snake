import pygame

# setup vars
windowWidth = 400
windowHeight = 400
backgroundColor = "black"
gridColor = "white"
playerColor = "green"

# directions
direction = "stop"

# pygame setup
pygame.init
pygame.display.set_caption("brady's snake")
screen = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()
running = True

# initial player position
player = pygame.Rect((windowWidth / 2), (windowHeight / 2), 20, 20)

# create a grid
def drawGrid():
	blockSize = 20
	for x in range(0, windowWidth, blockSize):
		for y in range(0, windowHeight, blockSize):
			rect = pygame.Rect(x, y, blockSize, blockSize)
			pygame.draw.rect(screen, gridColor, rect, 1)
	

# game loop
while running:
	# poll for events
	# pygame.QUIT event means the user closed window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(backgroundColor)

	# RENDER YOUR GAME HERE	
	drawGrid()
	pygame.draw.rect(screen, playerColor, player, 20)

	# gets keypresses
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		direction = "up"
	if keys[pygame.K_DOWN]:
		direction = "down"
	if keys[pygame.K_RIGHT]:
		direction = 'right'
	if keys[pygame.K_LEFT]:
		direction = 'left'

	# moves snake in a direction
	if direction == "up":
		player.y -= 2
	elif direction == "down":
		player.y += 2
	elif direction == "right":
		player.x += 2
	elif direction == "left":
		player.x -= 2

	

	# flip() the display to put your work on screen
	pygame.display.flip()	
	clock.tick(60)  # limits FPS to 60

pygame.quit()