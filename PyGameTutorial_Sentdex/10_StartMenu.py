import pygame
import time
import random

pygame.init()
#---------game constants variables-------------


display_width = 800
display_height = 600
#RGB color constants
black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
#------------------------------------------------------
#create main display window
gameDisplay = pygame.display.set_mode((display_width,display_height))
#set main display window title
pygame.display.set_caption('Race Game')

clock = pygame.time.Clock()
#-------------------load images-----------------------------------
# load image
carImg = pygame.image.load('race_car_transp_v2.png')
#get image size in pixels. for colision detection
carImg_width = carImg.get_rect().size[0]
carImg_height = carImg.get_rect().size[1]

#-------------------FUNCTIONS------------------------------------
def things_dodged(count):
	#1. set type font
	font = pygame.font.SysFont(None,25)
	#2. render it
	text = font.render("dodged: " + str(count),True,black)
	#3. blit = draw
	gameDisplay.blit(text,(0,0))

#creating things that move towards car
def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect((gameDisplay),color,[thingx,thingy,thingw,thingh])

#function to display a car
def car(x,y):
	gameDisplay.blit(carImg,(x,y)) #we blit car image to a surface

def text_objects(text,font):
	textSurface = font.render(text, True, black)
	return	textSurface, textSurface.get_rect()

def message_display(text):
	#define look of the writing
	largeText = pygame.font.Font('freesansbold.ttf',100)
	#create a custom function for message box display
	TextSurf, TextRect = text_objects(text, largeText)
	#center the message box display on of the middle screen
	TextRect.center =((display_width/2),(display_height/2))
	#draw image with blit
	gameDisplay.blit(TextSurf,TextRect)
	#update display
	pygame.display.update()
	time.sleep(2)
	game_loop()

def crash():
	message_display('You Chrashed')

def game_loop():
	x = display_width*0.45
	y = display_height*0.8
	#for computers (x=0,y=0) is top left corner

def game_intro():
 	intro = True

 	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)
		##SAME CODE AS message_display()
		#define look of the writing
		largeText = pygame.font.Font('freesansbold.ttf',100)
		#create a custom function for message box display
		TextSurf, TextRect = text_objects(text, largeText)
		#center the message box display on of the middle screen
		TextRect.center =((display_width/2),(display_height/2))
		#draw image with blit
		gameDisplay.blit(TextSurf,TextRect)
		pygame.display.update()
		clock.tick(15)	#show for 15 sec

#--------------------main game loop--------------------
	x_change = 0
	cnt = 0
	dodged = 0
	#objects apear randomly on x axis
	thing_startx = random.randrange(0,display_width)
	#start object off the screen-above
	thing_starty = -600
	thing_speed = 6   # 7 default
	thing_width = 100 #pixles
	thing_height = 100
	car_move_speed = 10

	gameExit = False
	while not gameExit:

		#------------key press game logic-------------
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				#gameExit = True
				pygame.quit()
				quit()

				#if key pressed start moving
			if event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_LEFT:
			    	x_change = -car_move_speed
			    elif event.key == pygame.K_RIGHT:
			    	x_change = car_move_speed

				#if key released stop moving
			if event.type == pygame.KEYUP:
			    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			    	x_change = 0

		x += x_change

		#------------graphics and logic----------------------
		#draw background
		gameDisplay.fill(white)
		#draw things
		things(thing_startx, thing_starty,thing_width,thing_height,black)
		#move things
		thing_starty += thing_speed
		#draw car
		car(x,y)
		#draw dodged count
		things_dodged(dodged)	#score is always last. so we never cover it
		#----------check boundaries for chrash----------
		if x > display_width - carImg_width or x < 0:
			crash()
			gameExit = True
		#---WHEN THING FALLS OF THE SCREEN, START AGAIN FROM TOP------
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)

			#--------this code is to increase difficulty of the game
			dodged += 1		 #increase count dodged of things
			thing_speed += 0.3 #increase speed of things
			if thing_width > 300:
					thing_width	+= (dodged*1.05)
			#------------------------------------------------------------

		#start is 600 off the screen
		#start is 600 off the screen
		#------------chrash logic-----------------
		#crash_flag = False
		#chrash COULD happen if bottom of box is lower than racecar
		#must also be x
		#check Y boundaries

		car_crash_y = False
		car_crash_x_right = False
		car_crash_y_left = False
		car_crash = False
		cnt = cnt + 1;


		#check if TOP OF CAR TOUCHES BOT OF THING BOUNDARY
		if y < thing_starty + thing_height:
			car_crash_y = True

		#check if RIGHT CAR BOUNDARY touches left THING boundaries
		if x+carImg_width > thing_startx and x+carImg_width < thing_startx + thing_width:
			car_crash_x_right = True

		#check if LEFT CAR BOUNDARY touches right THING boundaries
		if x > thing_startx and x < thing_startx + thing_width:
			car_crash_y_left = True

		#MAIN CHRASH LOGIC
		if car_crash_y and (car_crash_x_right or car_crash_y_left):
			car_crash = True
			crash()

			#print(f'car_crash_y: {car_crash_y}')
			#print(f'car_crash_x_right: {car_crash_x_right}')
			#print(f'car_crash_y_left: {car_crash_y_left}')
			#print(f'car_crash: {car_crash}')

		#------------------------------------------
		pygame.display.update() #update all changes to display
		clock.tick(60)
#------------------------------------
game_intro()
game_loop()		#game is running here, until pygame.QUIT
#pygame.quit()
#quit()