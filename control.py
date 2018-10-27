import pygame
import time
import socket

speed = [0, 0]

s_c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if __name__ == '__main__': 
	pygame.init() 
	screen = pygame.display.set_mode((600,600)) 

	while True: 
		a = str(speed[0]) + ' '+ str(speed[1])
		print a 
		s_c.sendto(a, ("192.168.1.143", 9901))
		
		for event in pygame.event.get(): 
			if event.type==pygame.QUIT: 
				exit() 
			if event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_UP: 
					if (speed[0] < 100 and speed[0] >= 0):
						speed[0] = speed[0] + 1
					if (speed[1] < 100 and speed[1] >= 0):
						speed[1] = speed[1] + 1

				elif event.key == pygame.K_DOWN: 
					if (speed[0] <= 100 and speed[0] >= 1):
						speed[0] = speed[0] - 1
					if (speed[1] <= 100 and speed[1] >= 1):
						speed[1] = speed[1] - 1

				elif event.key == pygame.K_LEFT:
					if (speed[0] <= 100 and speed[0] >= 1):
						speed[0] = speed[0] - 1
					if (speed[1] < 100 and speed[1] >= 0):
						speed[1] = speed[1] + 1

				elif event.key == pygame.K_RIGHT: 
					if (speed[0] < 100 and speed[0] >= 0):
						speed[0] = speed[0] + 1
					if (speed[1] <= 100 and speed[1] >= 1):
						speed[1] = speed[1] - 1


		key_pressed = pygame.key.get_pressed()

		if bool(key_pressed[pygame.K_UP]):
			if (speed[0] < 100 and speed[0] >= 0):
				speed[0] = speed[0] + 1
			if (speed[1] < 100 and speed[1] >= 0):
				speed[1] = speed[1] + 1


		elif bool(key_pressed[pygame.K_DOWN]):
			if (speed[0] <= 100 and speed[0] >= 1):
				speed[0] = speed[0] - 1
			if (speed[1] <= 100 and speed[1] >= 1):
				speed[1] = speed[1] - 1

		elif bool(key_pressed[pygame.K_LEFT]):
			if (speed[0] <= 100 and speed[0] >= 1):
				speed[0] = speed[0] - 1
			if (speed[1] < 100 and speed[1] >= 0):
				speed[1] = speed[1] + 1

		elif bool(key_pressed[pygame.K_RIGHT]):
			if (speed[0] < 100 and speed[0] >= 0):
				speed[0] = speed[0] + 1
			if (speed[1] <= 100 and speed[1] >= 1):
				speed[1] = speed[1] - 1


		elif (speed[0] <= 100 and speed[0] >= 1) and (speed[1] <= 100 and speed[1] >= 1):
			speed[0] = speed[0] - 1
			speed[1] = speed[1] - 1
		elif (speed[0] == 0) and (speed[1] <= 100 and speed[1] >= 1):
			speed[1] = speed[1] - 1
		elif (speed[1] == 0) and (speed[0] <= 100 and speed[0] >= 1):
			speed[0] = speed[0] - 1

		time.sleep(0.03)
