import pygame
import math
from pygame import mixer
pygame.init()

# WINDOW SIZE
width = 800
height = 600


# COLORS
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
pink = (255, 0, 255)
blue = (0, 0, 255)
gold = (245, 242, 66)
red = (245, 66, 66)

# WINDOW
win = pygame.display.set_mode((width, height))

background = pygame.image.load('ironman_back.jpg').convert()

# GAME NAME
pygame.display.set_caption('MARVEL FIGHT')

# GAME ICON
icon = pygame.image.load('Avengers.png')
pygame.display.set_icon(icon)

# HERO SIZE
hero_x = 10
hero_y = 525

# HERO SPEED
hero_x_speed = 0
hero_y_speed = 0

# HERO IMAGE
hero_img = pygame.image.load('ironman.png')

# ENEMY IMAGE
enemy_img = pygame.image.load('thanos.png')

# ENEMY SIZE
enemy_x = 730
enemy_y = 525

# ENEMY SPEED
enemy_x_speed = 0
enemy_y_speed = 0

# BULLET IMAGE
bullet_img = pygame.image.load('hammer.png')

# BULLET SIZE
bullet_x = 10
bullet_y = 525
bullet_state = 'ready'
bullet_x_change = 3
bullet_y_change = 3

# ENEMY WEPON IMAGE
enemy_wepon_img = pygame.image.load('sword.png')

# ENEMY WEPON SIZE
enemy_wepon_x = 730
enemy_wepon_y = 525
enemy_wepon_state = 'ready'
enemy_wepon_x_change = 3
enemy_wepon_y_change = 3

# HERO SCORE
hero_score = 0
enemy_score = 0

font = pygame.font.Font('freesansbold.ttf', 25)

hero_text_x = 10
hero_text_y = 10

enemy_text_x = 635
enemy_text_y = 10

def hero_show_score(x, y):
	score = font.render("IRONMAN: " + str(hero_score), True, (red))
	win.blit(score, (x, y))

def enemy_show_score(x, y):
	score = font.render("THANOS: " + str(enemy_score), True, (blue))
	win.blit(score, (x, y))


def fire_bullet(x, y):
	global bullet_state
	bullet_state = 'fire'
	win.blit(bullet_img, (x + 10, y + 15))

def enemy_fire_bullet(a, b):
	global enemy_wepon_state
	enemy_wepon_state = 'fire'
	win.blit(enemy_wepon_img, (a + 10, b + 15))


def enemy_is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
	distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2)) 
	if distance < 27:
		return True
	else:
		return False

def hero_is_collision(hero_x, hero_y, enemy_wepon_x, enemy_wepon_y):
	distance = math.sqrt(math.pow(hero_x - enemy_wepon_x, 2) + math.pow(hero_y - enemy_wepon_y, 2)) 
	if distance < 27:
		return True
	else:
		return False

# BACKGROUND MUSIC
mixer.music.load('background.mp3')
mixer.music.play(-1)

run = False

FPS = 60
clock = pygame.time.Clock()

# GAME LOOP
while not run:
	win.blit(background, (0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = True

# HERO MOVEMENT

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				hero_y_speed -= 3

			if event.key == pygame.K_LEFT:
				hero_y_speed += 3


		if event.type == pygame.KEYUP:
			 if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
			 	hero_y_speed = 0

# ENEMY MOVEMENT

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				enemy_y_speed -= 3

			if event.key == pygame.K_DOWN:
				enemy_y_speed += 3	

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
			 	enemy_y_speed = 0

# BULLET MOVEMENT

			if event.key == pygame.K_SPACE:
				if bullet_state == 'ready':
					bullet_y = hero_y
					fire_bullet(bullet_x, bullet_y)

			if event.key == pygame.K_w:
				if enemy_wepon_state == 'ready':
					enemy_wepon_y = enemy_y
					enemy_fire_bullet(enemy_wepon_x, enemy_wepon_y)

# HERO BOUNDARY CHECK

	if hero_y < 0:
		hero_y = 0
	elif hero_y >= 525:
		hero_y = 525

# ENEMY BOUNDARY CHECK

	if enemy_y < 0:
		enemy_y = 0
	elif enemy_y >= 525:
		enemy_y = 525

# HERO SPEED SET

	hero_x += hero_x_speed
	hero_y += hero_y_speed

# ENEMY SPEED SET

	enemy_x += enemy_x_speed
	enemy_y += enemy_y_speed

# BULLET BOUNDARY CHECK

	if bullet_x >= 730:
		bullet_x = 10
		bullet_state = 'ready'

	if bullet_state == 'fire':
		fire_bullet(bullet_x, bullet_y)
		bullet_x += bullet_x_change

	if enemy_wepon_x <= 10:
		enemy_wepon_x = 730
		enemy_wepon_state = 'ready'

	if enemy_wepon_state == 'fire':
		enemy_fire_bullet(enemy_wepon_x, enemy_wepon_y)
		enemy_wepon_x -= enemy_wepon_x_change


# COLLISION CHECK

	enemy_collision = enemy_is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
	if enemy_collision:
		bullet_x = 10
		bullet_state = 'ready'
		hero_score += 1
		
	enemy_collision = enemy_is_collision(hero_x, hero_y, enemy_wepon_x, enemy_wepon_y)
	if enemy_collision:
		enemy_wepon_x = 10
		enemy_wepon_state = 'ready'
		enemy_score += 1

# PUT SCORE ON THE SCREEN

	hero_show_score(hero_text_x, hero_text_y)
	enemy_show_score(enemy_text_x, enemy_text_y)
	win.blit(hero_img, (hero_x, hero_y))
	win.blit(enemy_img, (enemy_x, enemy_y))
	
	# clock.tick(FPS)
		
	pygame.display.update()
pygame.quit()