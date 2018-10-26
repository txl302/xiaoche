import pygame
import time
import socket

speed = 0
s_c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if __name__ == '__main__': 
	pygame.init() 
	screen = pygame.display.set_mode((600,600)) 

	while True: 
		print speed 
		s_c.sendto(str(speed), ("192.168.1.143", 9901))
		
		for event in pygame.event.get(): 
			if event.type==pygame.QUIT: 
				exit() 
			if event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_UP: 
					speed = speed + 1
				elif event.key == pygame.K_DOWN: 
					speed = speed - 1

		key_pressed = pygame.key.get_pressed()

		if bool(key_pressed[pygame.K_UP]):
			speed = speed + 1
		if bool(key_pressed[pygame.K_DOWN]):
			speed = speed - 1

		time.sleep(0.03)
