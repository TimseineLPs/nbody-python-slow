import pygame
import math
import random
import sys

#COLORS
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)
CYAN = (0,255,255)
YELLOW = (255,255,0)

width = 800
height = 500

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

def CalculateGravitationalPull(mass,xS,yS,xO,yO):
	

	try:
		a = mass/((xS-xO)**2+(yS-yO)**2)
	except:
		return 0
	return a
	
def VecToObj(xS,yS,xO,yO):
	Vec = Vector(-(xS-xO),-(yS-yO))
	return Vec 

def RandomObj():
	objekt = moveableObject(random.randint(0,width),random.randint(0,height),random.random()*10,Vector(0,0))
	return objekt

class Vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class moveableObject:
	def __init__(self,x,y,mass,vector):
		self.x = x
		self.y = y
		self.mass = mass
		if mass > 0:
			self.radius = int(mass)
		else:
			self.radius = 3
		self.vector = vector
	def move(self):
		self.x += self.vector.x*time_step
		self.y += self.vector.y*time_step
	def calculateVector(self,obj2):
		acceleration = CalculateGravitationalPull(obj2.mass,self.x,self.y,obj2.x,obj2.y)
		vectorToObject = VecToObj(self.x,self.y,obj2.x,obj2.y)
		self.vector.x += vectorToObject.x*acceleration*time_step
		self.vector.y += vectorToObject.y*acceleration*time_step

class static:
	def __init__(self,x,y,mass):
		self.x = x
		self.y = y
		self.mass = mass
		self.radius = 2
	def move(self):
		pass
	def calculateVector(a,b):
		pass

objects = []#[static(500,500,4)]


for x in range(int(20)):
	for y in range(int(10)):
		print(x)
		obj = moveableObject(x*20+200,y*20+200,1,Vector(0,0))
		objects.append(obj)

delta_t = 1
time_step = 0

while True:
	screen.fill((100,100,100))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			elif event.key == pygame.K_DOWN:
				time_step -= 0.1
			elif event.key == pygame.K_UP:
				time_step += 0.1
			elif event.key == pygame.K_LEFT:
				screen.fill((10,10,10))

	for o in objects:
		for o2 in objects:
			o.calculateVector(o2)
		o.move()
		pygame.draw.circle(screen , CYAN , (int(o.x),int(o.y)), o.radius , 0)
	#delta_t = clock.tick()/16
	print(delta_t)
	pygame.display.flip()
