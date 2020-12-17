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

# load image
carImg = pygame.image.load('race_car_transp_v2.png')
#get image size in pixels. for colision detection
carImg_width = carImg.get_rect().size[0]
carImg_height = carImg.get_rect().size[1]

#function to display a car
def car(x,y):
	gameDisplay.blit(carImg,(x,y)) #we blit car image to a surface

def game_loop():
	x = display_width*0.45
	y = display_height*0.8
	#for computers (x=0,y=0) is top left corner

	#------------main game loop---------
	x_change = 0
	
	gameExit = False
	
	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

				#if key pressed start moving
			if event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_LEFT:
			    	x_change = -5
			    elif event.key == pygame.K_RIGHT:
			    	x_change = 5

				#if key released stop moving
			if event.type == pygame.KEYUP:
			    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			    	x_change = 0

		x += x_change

		#------------------------------------
		gameDisplay.fill(white)	#draw background
		car(x,y)				#draw car

		#check boundaries for chrash
		if x > display_width - carImg_width or x < 0:
			gameExit = True

		pygame.display.update() #update all changes to display
		clock.tick(60)	
#------------------------------------
game_loop()		#game is running here, until pygame.QUIT
pygame.quit()	
quit()