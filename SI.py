import pygame

windowWidth = 400
windowHeight = 600
gamesSideMargin = 20
gameTopMargin = 40
gameBottomMargin = gameTopMargin
gameBorderWidth = 3

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
ind = (128,0,255)
titlecolor = (51, 204, 204)


pygame.init() 



gameDisplay = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption('Daniel Blaster')

titleFont = pygame.font.SysFont('Ariel', 40, True)

clock = pygame.time.Clock()

playerImg = pygame.image.load("si-player.gif")
#backgroundImg = pygame.image.load("si-background.gif")

class Player:
    xcor = 60
    ycor = windowHeight - gameBottomMargin - gameBorderWidth - playerImg.get_height()
    speed = 5
    direction = 0

    def show(self):
        movementAmount = self.direction * self.speed
        newX = self.xcor + movementAmount

        if newX < gamesSideMargin + gameBorderWidth or newX > windowWidth - gamesSideMargin - gameBorderWidth - playerImg.get_width():
            self.xcor = self.xcor
        else:
            self.xcor = newX

        gameDisplay.blit(playerImg, (self.xcor,self.ycor))
    def moveRight(self):
        self.direction  = 1
    def moveLeft(self):
        self.direction = -1
    def stopMoving(self):
        self.direction = 0    
player = Player()



isAlive = True
while isAlive:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isAlive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moveLeft()
            elif event.key == pygame.K_RIGHT:
                player.moveRight()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stopMoving()


    gameDisplay.blit(gameDisplay, (0, 0))
    gameDisplay.fill(ind)

    #gameDisplay.blit(backgroundImg,(gamesSideMargin,gameTopMargin))
    gameX = gamesSideMargin + gameBorderWidth
    gameY = gameTopMargin + gameBorderWidth
    gameWidth = windowWidth - (gamesSideMargin * 2) - (gameBorderWidth * 2)
    gameHeight = windowHeight - gameTopMargin - gameBottomMargin - (gameBorderWidth * 2)

    #aww yiss
    pygame.draw.rect(gameDisplay, white,
    (gamesSideMargin, gameTopMargin,  windowWidth - gamesSideMargin * 2, windowHeight - gameBottomMargin - gameTopMargin))
    #motha-fucking border rectangles
    pygame.draw.rect(gameDisplay, black, (gameX, gameY, gameWidth, gameHeight))
    #gameDisplay.blit(backgroundImg, (gamesSideMargin + gameBorderWidth, gameTopMargin + gameBorderWidth), (0, 0, gameWidth, gameHeight))
    player.show()

    titleText = titleFont.render('DANIEL BLASTER', False, titlecolor)
    gameDisplay.blit(titleText, (windowWidth / 2 - titleText.get_width / 2, 0))

    pygame.display.update()
    clock.tick(60)


