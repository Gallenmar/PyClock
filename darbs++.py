import pygame
import math
pygame.init()

#initialising some values important for program's propper function
RUNNING = True
FRAMERATE = 30
clock = pygame.time.Clock()

#drawing a screen
WIDTH = 740; HEIGHT = 740
#BGCOLOR = pygame.Color('grey')
BGCOLOR = (40,40,40)
FGCOLOR = pygame.Color('white')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BGCOLOR)

#drawing the clock for the first time
CENTERX = WIDTH/2
CENTERY = HEIGHT/2
CENTER = (CENTERX, CENTERY)
RADIUS = 200

def rotateh(x,y,a):
	xn = int(x*math.cos(a)-y*math.sin(a))
	yn = int(x*math.sin(a)+y*math.cos(a))
	return xn, yn
def rotate(x,y,a):
	xn = x*math.cos(a)-y*math.sin(a)
	yn = x*math.sin(a)+y*math.cos(a)
	return xn, yn

minx = float(0)
miny = float(-180) #length of the minute arrow with a minus sign
pygame.draw.line(screen, (255,30,30), CENTER, (CENTERX+ minx, CENTERY+ miny), 2)

hourx = float(0)
houry = float(-100) #length of the hour arrow with a minus sign
pygame.draw.line(screen, (255,30,30), CENTER, (CENTERX+ hourx, CENTERY+ houry), 3)

secx = float(0)
secy = float(-170) #length of the second arrow with a minus sign
secNotchx = float(0)
secNotchy = float(20)
pygame.draw.line(screen, (255,255,30), (CENTERX+ secNotchx, CENTERY+ secNotchy), (CENTERX+ secx, CENTERY+ secy), 1)


pygame.font.init()
myfont = pygame.font.Font(None, 20) # font, size

speed = 0.1
am= math.radians(speed)
ah= math.radians(speed/12) # 30/(360/a)
asec=  math.radians(speed*12)
text = "Speed (white/minute arrow): " + str(round(speed,2)) + "°"
circlecolor = (255,255,255) #also used by notches and numbers
textcolor = (255,255,255)
hourcolor = (30,255,30)
secondcolor = (255,30,30) # also used by top notch

x1 = 0
y1 = -RADIUS-5
x2 = 0
y2 = -RADIUS+5
while RUNNING:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUNNING = False
		if event.type == pygame.KEYDOWN:
			key=pygame.key.get_pressed() 
			#if key[pygame.K_a]:
			if key[pygame.K_c]:
				BGCOLOR = (33,44,57)
				circlecolor = (184, 176, 141)
				textcolor = (242, 212, 146)
				hourcolor = (184, 176, 141)
				secondcolor = (242, 149, 89)
			if key[pygame.K_d]:
				BGCOLOR = (40,40,40)
				circlecolor = (255,255,255) #also used by notches and numbers
				textcolor = (255,255,255)
				hourcolor = (30,255,30)
				secondcolor = (255,30,30) # also used by top notch
			if key[pygame.K_0]:
				speed = 0
			if key[pygame.K_1]:
				speed = 0.1
			if key[pygame.K_2]:
				speed = 0.2
			if key[pygame.K_3]:
				speed = 0.3
			if key[pygame.K_4]:
				speed = 0.4
			if key[pygame.K_5]:
				speed = 0.5
			if key[pygame.K_6]:
				speed = 0.6
			if key[pygame.K_7]:
				speed = 0.7
			if key[pygame.K_8]:
				speed = 0.8
			if key[pygame.K_9]:
				speed = 0.9

			if key[pygame.K_ESCAPE]: RUNNING = False
			if key[pygame.K_e]: RUNNING = False
			if key[pygame.K_UP]: speed+=0.1
			if key[pygame.K_GREATER]: speed+=0.1
			if key[pygame.K_DOWN]: speed-=0.1
			if key[pygame.K_LESS]: speed-=0.1
			if key[pygame.K_RIGHT]: speed+=1
			if key[pygame.K_LEFT]: speed-=1
			if key[pygame.K_r]:
				secNotchx = float(0)
				secNotchy = float(20)
				minx = float(0)
				miny = float(-180)
				hourx = float(0)
				houry = float(-100)
				secx = float(0)
				secy = float(-170)
				speed = 0.1
			text = "Speed (white/minute arrow): " + str(round(speed,2)) + "°"
			am= math.radians(speed)
			ah= math.radians(speed/12) # 30/(360/a)
			asec=  math.radians(speed*12)
			




	screen.fill(BGCOLOR)
	#		Draw a clock face
	# Draw a circle
	pygame.draw.circle(screen, circlecolor,CENTER, RADIUS, 1)
	# Draw a notch around on the circle (the top one)
	pygame.draw.line(screen, secondcolor, (int(CENTERX + x1), int(CENTERY + y1)),(int(CENTERX + x2), int(CENTERY + y2)), 10)
	#	Draw 3 notches around on the circle (right, bottom, left)
	for i in range(1,4):
		a= math.radians(i*90)
		xn1,yn1  = rotate(x1,y1,a)
		xn2, yn2 = rotate(x2,y2,a)
		pygame.draw.line(screen, circlecolor, (int(CENTERX + xn1), int(CENTERY + yn1)),(int(CENTERX + xn2), int(CENTERY + yn2)), 5)
	#		Draw white marks around the circe
	for i in range(1,12):
		a= math.radians(i*360/12)
		xn1,yn1  = rotate(x1,y1,a)
		xn2, yn2 = rotate(x2,y2,a)
		pygame.draw.line(screen, circlecolor, (int(CENTERX + xn1), int(CENTERY + yn1)),(int(CENTERX + xn2), int(CENTERY + yn2)), 1)
	#		Display the numbers
	for i in range(1,6):
		a= math.radians(i*360/12+4)
		xn1,yn1  = rotate(x1-15,y1-15,a)
		textRender = myfont.render(str(i), True, circlecolor)
		xn1 -=5
		yn1 -=5
		screen.blit(textRender, (int(CENTERX + xn1), int(CENTERY + yn1)))
	# 6 on the bottom doesnt look good (it isn't centered) so this centeres it
	a= math.radians(6*360/12+4)
	xn1,yn1  = rotate(x1-17,y1-15,a)
	textRender = myfont.render("6", True, circlecolor)
	xn1 -=5
	yn1 -=5
	screen.blit(textRender, (int(CENTERX + xn1), int(CENTERY + yn1)))
	for i in range(7,13):
		a= math.radians(i*360/12+4)
		xn1,yn1  = rotate(x1-15,y1-15,a)
		textRender = myfont.render(str(i), True, circlecolor)
		xn1 -=5
		yn1 -=5
		screen.blit(textRender, (int(CENTERX + xn1), int(CENTERY + yn1)))
    

	#		Draw the arrows
	# The minute hand
	minx,miny = rotate(minx,miny,am)
	pygame.draw.line(screen, textcolor, CENTER, (int(CENTERX+ minx), int(CENTERY+ miny)), 2)
	# The hour hand
	hourx,houry = rotate(hourx,houry,ah)
	pygame.draw.line(screen, hourcolor, CENTER, (int(CENTERX+ hourx), int(CENTERY+ houry)), 3)
	# The second hand
	secNotchx,secNotchy = rotate(secNotchx,secNotchy,asec)
	pygame.draw.line(screen, secondcolor, CENTER, (int(CENTERX+ secNotchx), int(CENTERY+ secNotchy)), 1)
	secx,secy = rotate(secx,secy,asec)
	pygame.draw.line(screen, secondcolor, CENTER, (int(CENTERX+ secx), int(CENTERY+ secy)), 1)
	pygame.draw.circle(screen, secondcolor,(int(CENTERX+ secx), int(CENTERY+ secy)), 10)

	#		Display all the text
	textRender = myfont.render(text, True, textcolor)
	screen.blit(textRender, (WIDTH-300, 15))
	textRender = myfont.render("- Use arrows (<>) or numbers (1..9) on ", True, textcolor)
	screen.blit(textRender, (40, HEIGHT-160))
	textRender = myfont.render("the keyboard to change the speed.", True, textcolor)
	screen.blit(textRender, (60, HEIGHT-145))
	textRender = myfont.render("- Use R to reset the speed and arrows.", True, textcolor)
	screen.blit(textRender, (40, HEIGHT-125))
	textRender = myfont.render("- Use these keys to change the color scheme.", True, textcolor)
	screen.blit(textRender, (40, HEIGHT-105))
	textRender = myfont.render("C - a bit of a nicer theme.", True, textcolor)
	screen.blit(textRender, (60, HEIGHT-90))
	textRender = myfont.render("D - the default theme.", True, textcolor)
	screen.blit(textRender, (60, HEIGHT-75))
	textRender = myfont.render("Use Esc. or E to exit.", True, textcolor)
	screen.blit(textRender, (40, HEIGHT-45))
	
	clock.tick(FRAMERATE)
	pygame.display.flip()
pygame.quit()










# do the sync time thing
# write commens all over
# in the shablon write the algorythm theory