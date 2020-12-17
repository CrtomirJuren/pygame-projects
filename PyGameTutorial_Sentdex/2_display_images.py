import pygame

pygame.init()


#---------display-------------
display_width = 800
display_height = 600
#color var
black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
#set title
pygame.display.set_caption('Race Game')

clock = pygame.time.Clock()

carImg = pygame.image.load('race_car_transp_v2.png')

#function to display a car
def car(x,y):
	gameDisplay.blit(carImg,(x,y)) #we blit car image to a surface

x = display_width*0.45
y = display_height*0.8
#for computers (x=0,y=0) is top left corner

#------------main game loop---------
chrashed = False
while not chrashed:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			chrashed = True

	#------------------------------------
	#first draw background, dont paint over car
	gameDisplay.fill(white)	
	car(x,y)
	pygame.display.update()

	clock.tick(60)	
#------------------------------------
pygame.quit()
quit()