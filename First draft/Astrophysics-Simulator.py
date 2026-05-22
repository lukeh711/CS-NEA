#----Objects----
class PhysicsObject:
    _mass = 10  #mass in kg
    _velocityX = 0
    _velocityY = 0

    def __init__(self, massIn, velocityXIn, velocityYIn):
        self._mass = massIn
        self._velocityX = velocityXIn
        self._velocityY = velocityYIn


class Planet(PhysicsObject):
    _gravity = 9.81

    def __init__(self, massIn, velocityXIn, velocityYIn, gravityIn):
        super().__init__(massIn, velocityXIn, velocityYIn)
        self._gravity = gravityIn

class Renderer:
    def __init__(self):
        pass

    def renderCircleXXYY(self, coords1In, coords2In, colourIn):
        x1 = coords1In[0]
        x2 = coords2In[0]
        y1 = coords1In[1]
        y2 = coords2In[1]
        

    def renderCircleXYR(self, coordsIn, radiusIn, colourIn):
        x = coordsIn[0]
        y = coordsIn[0]

        pygame.draw.circle(screen, colourIn, (x, y), radiusIn)
        


import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
screenRenderer = Renderer()
upKeyPressed = False
downKeyPressed = False
leftKeyPressed = False
rightKeyPressed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                upKeyPressed = True
            elif event.key == pygame.K_s:
                downKeyPressed = True
            elif event.key == pygame.K_a:
                leftKeyPressed = True
            elif event.key == pygame.K_d:
                rightKeyPressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                upKeyPressed = False
            elif event.key == pygame.K_s:
                downKeyPressed = False
            elif event.key == pygame.K_a:
                leftKeyPressed = False
            elif event.key == pygame.K_d:
                rightKeyPressed = False

    screen.fill("purple")
    
    # Game rendering + game loop here
    tempX = 500
    tempY = 500
    if upKeyPressed:
        tempY += 1
    elif downKeyPressed:
        tempY -= 1
    elif leftKeyPressed:
        tempX -= 1
    elif rightKeyPressed:
        tempX += 1
    
    screenRenderer.renderCircleXYR([tempX, tempY], 10, (255, 255, 255))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()