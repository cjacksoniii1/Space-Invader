import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def load_image(name, colorkey = None):
    fullname = os.path.join('DBDATA',name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get__at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()



#guy that shoots tha dudes
class player(pygame.sprite.Sprte)

    def _init_(self):
        pygame.sprite.Sprite.__init__(self)   #initialize sprite
        self.image, self.rect = load__image('shoota.png', -1)

    #move based on mouse
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos

class daniel(pygame.sprite.Sprite)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('dan1.png'-1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9

    def update(self):
        self._float()

    def _float(self):
        newpos = self.rect.move((self.movve, 0))
        if self.rect.left < self.area.left or \
            self.rect.right > self.area.right:
            self.move = -self.move
            newpos = self.rect.move
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos

        

class bullet(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load__image('shot.png',-1)
        self.x = 0
        self.y = 0
        self.speed = 0
        self.forwardx = 1
        self.forwardy = 0
        self.fired = false


def main():
    
    pygame.init
    

    #can i have an event loop, brother?
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
    
