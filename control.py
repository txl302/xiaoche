import pygame
import sys
from pygame.locals import *

pygame.init()

speed = 0
move = 0

while True:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			print "hh"
			if event.key == K_UP:
				move = +1
				print "fff"
			elif event.key == K_DOWN:
				move = -1
		elif event.type == KEYUP:
			move = 0
	speed+=move
	print speed 