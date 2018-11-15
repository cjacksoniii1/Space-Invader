import os, pygame
from pygame.locals import *
from pygame.compat import geterror

if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

def load_image(name, colorkey = None):
    fullname = os.path.join('DBDATA',name)
    #try:
    image = pygame.image.load(fullname)
    #except pygame.error message:
     #   print ('Cannot load image:'), name
      #  raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get__at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('DBDATA',name)
    sound = pygame.mixer.Sound(fullname)
    return sound;        

display_width = 800
display_height = 600
dark = (250,250,250)
text_size = 36

#guy that shoots tha dudes
class player(pygame.sprite.Sprite):

    def _init_(self):
        pygame.sprite.Sprite.__init__(self)   #initialize sprite
        self.image, self.rect = load_image('shoota.png', -1)

    #move based on mouse
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos

#daniels to blast
class daniel(pygame.sprite.Sprite):
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

        
#bullets to shoot
class bullet(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('shot.png',-1)
        self.x = 0
        self.y = 0
        self.speed = 0


def main():
    
    pygame.init()
    screen = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Daniel Blaster')
    pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(dark)

    if pygame.font:
        font = pygame.font.Font(None,text_size)
        text = font.render("Blast Daneil to BITS!")
        textpos = text.get_rect (centerx=background.get_width()/2)
        background.blit(text, textpos)

    screen.blit(background, (0, 0) )
    pygame.display.flip()

    clock = pygame.time.Clock()
    #example_sound = load_sound('soundfile.wav')
    player = player()
    daniel = daniel()
    allsprites = pygame.sprite.RenderPlain((player, daniel))  
    

    #can i have an event loop, brother?
    playing = True
    while playing:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                playing = False
            elif event.type == MOUSEBUTTONDOWN:
                playing = False
        allsprites.update()
        screen.blit(background, (0,0))
        allsprites.draw(screen)
        pygame.display.flip()

    
    pygame.quit()