import pygame

pygame.init()

W_HEIGHT = 600
W_WIDTH = 600
BLOCK_SIZE = 15

R_VAL = 100
G_VAL = 100
B_VAL = 100
shapeColor = (R_VAL,G_VAL,B_VAL)

DISPLAYSURF = pygame.display.set_mode((W_WIDTH,W_HEIGHT))
pygame.display.update()

running = True

mousex = 0
mousey = 0
mouseClicked = False
colUp = True
colDown = False

font = pygame.font.Font(None, 25)

def drawShapeOnClick(shapeColor):
	pygame.draw.rect(DISPLAYSURF, shapeColor, [mousex,mousey,BLOCK_SIZE,BLOCK_SIZE])
	pygame.display.update()
	mouseClicked = False

def drawColorValues(val):
	if val == R_VAL:
		screen_text = font.render('Red Value: '+str(R_VAL), True, (255,255,255))
		DISPLAYSURF.blit(screen_text,[10,500])
	elif val == G_VAL:
		screen_text = font.render('Green Value: '+str(G_VAL), True, (255,255,255))
		DISPLAYSURF.blit(screen_text,[10,530])
	elif val == B_VAL:
		screen_text = font.render('Blue Value: '+str(B_VAL), True, (255,255,255))
		DISPLAYSURF.blit(screen_text,[10,560])

	
def replaceValOnScreen(val):
	if val == R_VAL:
		pygame.draw.rect(DISPLAYSURF, (0,0,0), [10, 500,125, 20])
	elif val == G_VAL:
		pygame.draw.rect(DISPLAYSURF, (0,0,0), [10,530,140,20])
	elif val == B_VAL:
		pygame.draw.rect(DISPLAYSURF, (0,0,0), [10, 560, 130, 20])


while running:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONUP:
			mousex, mousey = event.pos
			print(mousex)
			mouseClicked = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				colUp = True
				colDown = False
			if event.key == pygame.K_DOWN:
				colUp = False
				colDown = True
			if event.key == pygame.K_r:
				if colUp:
					R_VAL += 5
					replaceValOnScreen(R_VAL)
					drawColorValues(R_VAL)
				elif colDown:
					R_VAL += -5
					replaceValOnScreen(R_VAL)
					drawColorValues(R_VAL)
			if event.key == pygame.K_g:
				if colUp:
					G_VAL += 5
					replaceValOnScreen(G_VAL)
					drawColorValues(G_VAL)
				elif colDown:
					G_VAL += -5
					replaceValOnScreen(G_VAL)
					drawColorValues(G_VAL)

			if event.key == pygame.K_b:
				if colUp:
					B_VAL += 5
					replaceValOnScreen(B_VAL)
					drawColorValues(B_VAL)
				elif colDown:
					B_VAL += -5
					replaceValOnScreen(B_VAL)
					drawColorValues(B_VAL)



	if mouseClicked:
		shapeColor = (R_VAL,G_VAL,B_VAL)
		drawShapeOnClick(shapeColor)

pygame.quit()
quit()