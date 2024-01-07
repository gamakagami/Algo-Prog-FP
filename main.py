#import pygame library and mixer for sound effects
import pygame
from pygame.locals import *
from pygame import mixer
import sys

#initialize pygame and mixer
mixer.init()
pygame.init()

#function to display text in the game
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = (x, y)
    screen.blit(text_surface, text_rect)

#function for handling quit event in pygame
def quit_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#function to reset level
def reset_level(level):
	#initialize player location
	player.reset(100, screen_height - 130)
	#empties group data
	blob_group.empty()
	platform_group.empty()
	heart_group.empty()
	lava_group.empty()
	exit_group.empty()

	#level data for each level
	if level == 0:
		world_data = [
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,7,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0,0,1,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 7, 0, 0, 2, 0, 0, 0, 0, 7, 0, 4, 0, 0,0,1,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0,0,1,0,0,1], 
			[1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1,0,0,1], 
			[1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1,0,0,1], 
			[1, 2, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1,0,0,1], 
			[1, 0, 0, 0, 2, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7, 0, 0, 0, 0, 0, 0,0,1,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7, 0, 0, 0,0,1,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7,0,1,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,0,1,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1,0,8,1], 
			[1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,2,1,2,2,1], 
			[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1]
					]
	elif level == 1:
		world_data = [
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 2, 2, 0, 0, 0, 2, 2, 1,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1,0,0,0,0,1], 
			[1, 0, 0, 0, 2, 2, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1,0,0,0,0,1], 
			[1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0,0,0,0,1], 
			[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 1,0,0,0,0,1], 
			[1, 0, 2, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0,0,0,0,1], 
			[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,0,0,0,0,1], 
			[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,0,0,0,8,1], 
			[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1]
					]
	elif level == 2:
		world_data = [
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 7, 0, 7, 0, 0,2,0,0,8,1], 
			[1, 0, 0, 5, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 2, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 1, 2, 0, 0, 0, 0, 0, 0, 4, 0, 0, 7, 0, 0, 4, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 1, 1, 2, 0, 0, 2, 6, 6, 6, 6, 2, 2, 2, 6, 6, 6, 6, 2, 2,2,0,0,0,1], 
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,5,0,1], 
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,1], 
			[1, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0,0,0,0,7,1], 
			[1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0,0,0,0,2,1], 
			[1, 0, 0, 0, 0, 2, 1, 0, 0, 2, 0, 0, 0, 2, 1, 0, 0, 2, 0, 0,0,0,2,1,1], 
			[1, 0, 0, 0, 2, 1, 1, 0, 0, 3, 0, 0, 2, 1, 1, 0, 0, 0, 3,0, 0,2,1,1,1], 
			[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1]
					]
		                 
	world = World(world_data)
	#create heart for showing the score in the top
	score_heart_image = Block(heart_img,tile_size // 2, tile_size // 2,(tile_size // 2, tile_size // 2),2)
	heart_group.add(score_heart_image)
	#return level data to the function
	return world

class Cloud():

	#initialize cloud image and coordinate
	def __init__(self,x,y,value):
		self.image = pygame.image.load("cloud.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		#determine cloud speed
		if value == "a":
			self.rect.x+=ca
		elif value == "b":
			self.rect.x+=cc
		elif value == "c":
			self.rect.x+=ce
		
		#display clouds
		screen.blit(self.image,(self.rect.x,self.rect.y))

class Player():

	def __init__(self, x, y):
		#initialize player coordinate (x,y) and call reset function which contains all the inital values
		self.reset(x, y)

	def update(self, game_over):
		#Player movement and collision logic

		#initialize variables
		dx = 0
		dy = 0
		walk_cooldown = 5
		cd = 20

		if game_over == 0:
			#handling keypresses
			key = pygame.key.get_pressed()
			if key[pygame.K_w] and self.jumped == False and self.in_air == False:
				jump_fx.play()
				self.vel_y = -15
				self.jumped = True

			if key[pygame.K_w] == False:
				self.jumped = False

			if key[pygame.K_a]:
				dx -= 5
				self.counter += 1
				self.direction = -1

			if key[pygame.K_d]:
				dx += 5
				self.counter += 1
				self.direction = 1
				
			if key[pygame.K_d] == False and key[pygame.K_a] == False:
				self.counter = 0
				self.index = 0

			#changes image animation depending on direction
			if self.direction == 1:
					self.image = self.images_right[self.index]
			if self.direction == -1:
					self.image = self.images_left[self.index]

			#handle animation
			if self.counter > walk_cooldown:
				self.counter = 0	
				self.index += 1

				#if index exceeds number of images
				if self.index >= len(self.images_right):
					self.index = 0

			#add gravity
			self.vel_y += 1
			if self.vel_y > 10:
				self.vel_y = 10
			dy += self.vel_y

			#collision detection
			self.in_air = True
			for tile in world.tile_data:

				#collision detection in x direction
				if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
					dx = 0

				#collision detection in y direction
				if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):

					#check if below the ground i.e. jumping
					if self.vel_y < 0:
						dy = tile[1].bottom - self.rect.top
						self.vel_y = 0

					#check if above the ground i.e. falling
					elif self.vel_y >= 0:
						dy = tile[1].top - self.rect.bottom
						self.vel_y = 0
						self.in_air = False

			#check for collision with enemies
			if pygame.sprite.spritecollide(self, blob_group, False):
				game_over = -1
				game_over_fx.play()

			#check for collision with lava
			if pygame.sprite.spritecollide(self, lava_group, False):
				game_over = -1
				game_over_fx.play()

			#check for collision with exit
			if pygame.sprite.spritecollide(self, exit_group, False):
				game_over = 1

			#check for collision with platforms
			for platform in platform_group:

				#collision in the x direction
				if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
					dx = 0
				
				#collision in the y direction
				if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):

					#check if below platform
					if abs((self.rect.top + dy) - platform.rect.bottom) < cd:
						self.vel_y = 0
						dy = platform.rect.bottom - self.rect.top

					#check if above platform
					elif abs((self.rect.bottom + dy) - platform.rect.top) < cd:
						self.rect.bottom = platform.rect.top - 1
						self.in_air = False
						dy = 0
						
					#move sideways with the platform
					if platform.move_x != 0:
						self.rect.x += platform.move_direction

			#update player coordinates
			self.rect.x += dx
			self.rect.y += dy

		#player has died
		elif game_over == -1:
			self.image = self.dead_image
			draw_text('YOU DIED!', font, red, (screen_width // 2) - 150, screen_height // 2)
			self.rect.y -= 5

		#draw player onto screen
		screen.blit(self.image, self.rect)

		return game_over

	#resetting the player to initial value
	def reset(self, x, y):
		#image list initialization
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		
		#load image and transformation
		for num in range(1, 9):
			img_right = pygame.image.load(f'Idle 0{num}.png').convert_alpha()
			img_left = pygame.transform.scale(img_right, (40, 80))
			img_right = pygame.transform.flip(img_left, True, False)

			#adding each image to their respective list
			self.images_right.append(img_right)
			self.images_left.append(img_left)

		#load dead image
		self.dead_image = pygame.image.load('Pink_Monster_Death_8.png').convert_alpha()

		#setting initial image and get rect
		self.image = self.images_right[self.index]
		self.rect = self.image.get_rect()

		#setting initial coordinates
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()

		#reset state variable
		self.vel_y = 0
		self.jumped = False
		self.direction = 0
		self.in_air = True

class World():

	def __init__(self, data):
		#store data for each tile
		self.tile_data = []

		#setting variables for world data
		dirt = 1
		grass = 2
		enemy = 3
		plat_x = 4
		plat_y = 5
		lavas = 6
		hearts = 7
		exitp = 8

		#loop through each row and column of data
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				
				#create dirt tile
				if tile == dirt:
					#scale image
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))

					#set rectangle and coordinate
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)

					#add tile into list
					self.tile_data.append(tile)

				#create grass tile
				if tile == grass:
					#scale image
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))

					#set rectangle and coordinate
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)

					#add tile into list
					self.tile_data.append(tile)

				#create enemy tile
				if tile == enemy:
					blob = Movement(enemy_img,col_count * tile_size, row_count * tile_size + 5,1,0,1)
					blob_group.add(blob)

				#create platform horizontal tile
				if tile == plat_x:
					platform = Movement(platform_img,col_count * tile_size, row_count * tile_size, 1, 0,2)
					platform_group.add(platform)

				#create  platform vertical tile
				if tile == plat_y:
					platform = Movement(platform_img,col_count * tile_size, row_count * tile_size, 0, 1,2)
					platform_group.add(platform)

				#create lava tile
				if tile == lavas:
					lava = Block(lava_img,col_count * tile_size, row_count * tile_size + (tile_size // 2),(tile_size, tile_size // 2),3)
					lava_group.add(lava)

				#create heart tile
				if tile == hearts:
					heart = Block(heart_img,col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2),(tile_size // 2, tile_size // 2),2)
					heart_group.add(heart)

				#create exit tile
				if tile == exitp:
					exits = Block(door_img,col_count * tile_size, row_count * tile_size - (tile_size // 2),((tile_size, int(tile_size * 1.5))),3)
					exit_group.add(exits)

				col_count += 1
			row_count += 1

	def draw(self):
		#render and blit world to the screen
		for tile in self.tile_data:
			screen.blit(tile[0], tile[1])

class Movement(pygame.sprite.Sprite):

	#initialize image, coordinates and movement
	def __init__(self,image, x, y, move_x, move_y,value):

		#inherits functionality and attributes from the Sprite class
		pygame.sprite.Sprite.__init__(self)
		img = image

		#to determine to scale or not for enemies and platform
		if value == 1:
			self.image = img
		elif value == 2:
			self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))

		#set rectangle of an image and initial position
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		#values for movement
		self.move_counter = 0
		self.move_direction = 1
		self.move_x = move_x
		self.move_y = move_y

	def update(self):
		#movement for x and y coordinates
		self.rect.x += self.move_direction * self.move_x
		self.rect.y += self.move_direction * self.move_y
		self.move_counter += 1

		#to reverse platform movement if it reaches a certain point
		if abs(self.move_counter) > move_limit:
			self.move_direction *= -1
			self.move_counter *= -1
			
class Block(pygame.sprite.Sprite):
	
	#initialize image, coordinates and scale value
	def __init__(self,image, x, y,scale,value):

		#inherits functionality and attributes from the Sprite class
		pygame.sprite.Sprite.__init__(self)
		img = image
		self.image = pygame.transform.scale(img, scale)

		#set rectangle of an image and initial position
		self.rect = self.image.get_rect()
		if value == 3:
			self.rect.x = x
			self.rect.y = y
		elif value == 2:
			self.rect.center = (x, y)

class Button():

	def __init__(self, x, y, image):
		#initialize button image and position
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		#to track if the button has been clicked or not
		self.clicked = False

	def draw(self):
		#to indicate if the button has been clicked or not
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):

			#check if the left mouse button is pressed and the button hasn't been clicked before
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:

				#set action to True to indicate that button is clicked
				action = True

				#set clicked value to true to prevent multiple clicks
				self.clicked = True

		#reset clicked value if left mouse button is not pressed
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		screen.blit(self.image, self.rect)

		#return action value
		return action
	
#function to return sound
def load_sound(sound_path):
    sound = pygame.mixer.Sound(sound_path)
    return sound

#function to play background music
def play_music(music_path, loop=-1):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(loop,start=5.0)

#fps for the game
clock = pygame.time.Clock()
fps = 60

#set and display screen width and height
screen_width = 1000
screen_height = 760
screen = pygame.display.set_mode((screen_width, screen_height))

#display icon and title for the game
pygame.display.set_caption("Heart Eater")
icon = pygame.image.load("Idle 01.png").convert_alpha()
pygame.display.set_icon(icon)

#define fonts
main_font = pygame.font.SysFont('Bauhaus 93', 120)
font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 30)

#define colours
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0,0,255)

#define game variables
tile_size = 40
dead = -1
alive = 0
win = 4
game_over = 0
main_menu = True
score_x = 880
score_y = 5
win_x = 380
win_y = 300
level = 0
max_levels = 2
score = 0
move_limit = 40
ca=1
cc=1.5
ce=2
clouda = 900
cloudb = 75
cloude = 500
cloudf = 225
cloudc = 700
cloudd = 150
cloud_end = 1060
cloud_start = -60
next_level = 1

#load images
bg_img = pygame.image.load('clo.jpeg').convert_alpha()
restart_img = pygame.image.load('restart_btn.png').convert_alpha()
start_img = pygame.image.load('aaa.png').convert_alpha()
exit_img = pygame.image.load('ex.png').convert_alpha()
exitsm_img = pygame.image.load("exitsm.png").convert_alpha()
cloud = pygame.image.load("cloud.png").convert_alpha()
door_img = pygame.image.load('exit.png').convert_alpha()
heart_img = pygame.image.load('heart.png').convert_alpha()
lava_img = pygame.image.load('lava.png').convert_alpha()
platform_img = pygame.image.load('platform.png').convert_alpha()
dirt_img = pygame.image.load('dirt.png').convert_alpha()
grass_img = pygame.image.load('new dirt.png').convert_alpha()
enemy_img = pygame.image.load('frog.png').convert_alpha()

#load sounds
bg_music = load_sound('the-last-piano-112677.mp3')
bg_music.set_volume(0.2)
bg_music.play(-1)
heart_fx = load_sound("nyam.mp3")
heart_fx.set_volume(2)
jump_fx = load_sound('jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = load_sound('game_over.wav')
game_over_fx.set_volume(0.5)

#initialize player location
player = Player(100, screen_height - 130)

#add groups
blob_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
heart_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

#load in level data and create world
world = reset_level(level)

#create buttons
restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 210, screen_height // 2 - 260, start_img)
exit_button = Button(screen_width // 2 - 210, screen_height // 2 + 50, exit_img)
back_button = Button(screen_width // 2 - 50, screen_height // 2 + 200, exitsm_img)

#loop the game
run = True
while run:

	clock.tick(fps)

	screen.blit(bg_img, (0, 0))

	#main menu
	if main_menu == True:
		draw_text("Heart Eater", main_font, white, 210,70)
		if exit_button.draw():
			#exit loop
			run = False
		if start_button.draw():
			#exit main menu
			main_menu = False
	else:
		#displays cloud
		Cloud(clouda,cloudb,"a")
		Cloud(cloudc,cloudd,"b")
		Cloud(cloude,cloudf,"c")

		#cloud movement
		clouda+=ca
		cloudc+=cc
		cloude+=ce

		#resetting cloud position if over the screen
		if clouda > cloud_end:
			clouda = cloud_start
		if cloudc > cloud_end:
			cloudc = cloud_start
		if cloude > cloud_end:
			cloude = cloud_start

		#draw world
		world.draw()

		#if player is still playing
		if game_over == alive:

			#to make the clouds move
			ca=1
			cc=1.5
			ce=2

			#update enemies and platform movement
			blob_group.update()
			platform_group.update()

			#display and update score and check if heart has been collected
			if pygame.sprite.spritecollide(player, heart_group, True):
				score += 1
				heart_fx.play()

			draw_text('X ' + str(score), font_score, white, tile_size -5 , 5)
		
		#displays groups in the screen
		blob_group.draw(screen)
		platform_group.draw(screen)
		lava_group.draw(screen)
		heart_group.draw(screen)
		exit_group.draw(screen)

		#check game over status
		game_over = player.update(game_over)
		
		#displays level text
		if level == 0:
			draw_text('Level: 1 ' , font_score, white, score_x, score_y)
		if level == 1:
			draw_text('Level: 2 ' , font_score, white, score_x, score_y)
		if level == 2:
			draw_text('Level: 3 ' , font_score, white, score_x, score_y)

		#if player has died
		if game_over == dead:

			#stop clouds from moving
			ca=0
			cc=0
			ce=0

			draw_text('X ' + str(score), font_score, white, tile_size -5 , 5)

			#displays restart button
			if restart_button.draw():
				world_data = []
				level = 0
				world = reset_level(level)
				game_over = alive
				score = 0

		#if player win
		if game_over == win:

			#display texts
			draw_text('X ' + str(score), font_score, white, tile_size - score_y , score_y)
			draw_text('Level: 3 ' , font_score, white, score_x, score_y)
			draw_text('You Win! ' , font, blue, win_x, win_y)

			#clouds stop moving
			ca=0
			cc=0
			ce=0

			#restart button
			if restart_button.draw():
				world_data = []
				level = 0
				world = reset_level(level)
				game_over = 0
				score = 0

			#exit button
			elif back_button.draw():
				run = False
			
		#if player has completed the level
		if game_over == next_level:

			#reset game and go to next level
			level += 1
			if level <= max_levels:

				#reset level
				world_data = []
				world = reset_level(level)
				game_over = 0
			else:
				#player win
				game_over = win

	#quit event handler
	quit_event()

	pygame.display.update()

pygame.quit()
