import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('a bit racey')

clock = pygame.time.Clock()

chrashed = False
while not chrashed:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			chrashed = True

		print(event)

	pygame.display.update()

	clock.tick(60)¸#frames per second

pygame.quit()
quit()