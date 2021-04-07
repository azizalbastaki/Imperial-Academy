import pygame # importing module
import random
pygame.init() # initiates pygame
window = pygame.display.set_mode((500,500)) # creates a 500x500px window
pygame.display.set_caption("STAR WARS: IMPERIAL ACADEMY") # sets caption, self explanatory
randomx = random.randint(-10,470)
randomy = random.randint(-10,470)
font = pygame.font.SysFont('timesnewromanboldttf',20)

class player(object):
    def __init__(self,x,y,width,height,jH):
        self.x= x # x coordinate of the character
        self.y = y # y coordinate of the character
        self.w = width  # width of the character
        self.h = height # Height of the character
        self.v = 15 # Speed of the character
        self.jump = False # Will determine whether the character is jumping
        self.jumpC = jH # Jump variable
        self.direction = "left"
        self.isWalking = 0
        self.walkRight = [pygame.image.load('right1.png'), pygame.image.load('right2.png'), pygame.image.load('right3.png')]
        self.walkLeft = [pygame.image.load('left1.png'), pygame.image.load('left2.png'), pygame.image.load('left3.png')]
        self.walkUp = [pygame.image.load('front1.png'), pygame.image.load('front2.png'), pygame.image.load('front3.png')]
        self.walkDown = [pygame.image.load('back1.png'), pygame.image.load('back2.png'), pygame.image.load('back3.png')]
    def redraw(self):
        global selectedimage
        global window
        previousnumber = number
        window.blit(selectedimage,(self.x,self.y))
class blaster(object):
    @classmethod
    def __init__(self,x,y,r):
        self.lasers = 0
        self.x = x
        self.y = y
        self.radius = r
        self.xvelocity = 5
        self.yvelocity = 0
        self.blastercount = 0
        self.xarray = []
        self.yarray = []
        self.xcounter = []
        self.ycounter = []
        self.age = []
    @classmethod
    def initiate_blast(self,xx,yy,dx,dy):
        self.lasers +=1
        self.xarray.append(int(xx))
        self.yarray.append(int(yy+20))
        self.xcounter.append(int(dx))
        self.ycounter.append(int(dy))
        self.age.append(0)

    @classmethod
    def updateblast(self):
        self.forcounter = 0
        for i in self.xarray:
           # pygame.draw.circle(window,(255,0,0), (i,(self.yarray[self.xarray.index(i)])), self.radius)
            pygame.draw.circle(window,(255,0,0), (i,(self.yarray[self.forcounter])), self.radius)
            self.xarray[self.forcounter] += self.xcounter[self.forcounter]
            self.yarray[self.forcounter] += self.ycounter[self.forcounter]
            self.age[self.forcounter] += 1
            #print(self.age[self.forcounter])
            if self.age[self.forcounter] >= 10:
                self.age.pop(self.forcounter)
                self.ycounter.pop(self.forcounter)
                self.xcounter.pop(self.forcounter)
                self.yarray.pop(self.forcounter)
                self.xarray.pop(self.forcounter)
                self.lasers -= 1
                trainingbot.forcounter =- 1
            self.forcounter+= 1
class trainingbot():
    @classmethod
    def __init__(self):
        self.xLimits = 0
        self.xLimitsTWO = 0
        self.yLimits = 0
        self.yLimitsTWO = 0
        self.droidArrayX = 0
        self.droidArrayY = 0
        self.droidXmultipliers = 0
        self.droidYmultipliers = 0
    @classmethod
    def createDroid(self,x,y,FX,FY):
        self.droidArrayX = (x)
        self.droidArrayY = (y)
        self.xLimits = (FX+(random.randint(5,200)))
        self.xLimitsTWO = (FX-(random.randint(5,200)))
        self.yLimits = (FY+(random.randint(5,200)))
        self.yLimitsTWO= (FY-(random.randint(5,200)))
        self.droidXmultipliers = (1)
        self.droidYmultipliers = (1)
    @classmethod
    def updateDroids(self):
        self.forcounter = 0
        i = self.droidArrayX
        self.box = [(i-20),(i+20),(self.droidArrayY-20),(self.droidArrayY+20)]
        for x in blaster.xarray:
            if ((x>= self.box[0]) and (self.box[1]>= x)) and ((blaster.yarray[self.forcounter] >= self.box[2]) and (self.box[3]>= blaster.yarray[self.forcounter])):
                global bots
                global level
                level += 1+(blaster.age[self.forcounter]*2)
                bots = 0
                #for i in blaster.xarray:
                
                global randomx
                global randomy
                blaster.age.pop(self.forcounter)
                blaster.ycounter.pop(self.forcounter)
                blaster.xcounter.pop(self.forcounter)
                blaster.yarray.pop(self.forcounter)
                blaster.xarray.pop(self.forcounter)
                blaster.lasers -=1
                self.forcounter =- 1
                randomx = random.randint(-10,470)
                randomy = random.randint(-10,470)
                trainingbot.createDroid(randomx,randomy,1,1)
        #pygame.draw.circle(window,(98,98,98),(i,(self.droidArrayY)),20)
        updateBots()
        pygame.draw.circle(window,(98,98,98),(randomx,(randomy)),20)
        self.forcounter+=1
        
run = True # variable used in a loop, its true if the program is still running.
troop = player(25,25,20,20,10)
blasted = blaster(troop.x,troop.y,5)
bg = pygame.image.load('bg.png')
clock = pygame.time.Clock()
number = 0
selectedimage = troop.walkUp[number]
bot = trainingbot()
level = 0
bots = 0

def spriteupdate(d,a,man):
    global number
    if man.direction != d:
        man.direction  = d
        changed(0,a)
    else:
        number+= 1
        if number>2:
            number = 0
            changed(number,a)
        else:
            changed(number,a)
def changed(numb, direct):
    global number
    global selectedimage
    number = numb
    selectedimage = direct[number]

def updateBots():
    global bots
    global level
    if bots == 0:
        level+= 1
        bots = 1
        randomx = random.randint(-10,470)
        randomy = random.randint(-10,470)
        trainingbot.createDroid(randomx,randomy,1,1)
        
def update():
    window.blit(bg,(0,0))
    troop.redraw()
    blaster.updateblast()
    bot.updateDroids()
    updateBots()
    trainingbot.createDroid(randomx,randomy,20,20)
    textScore = font.render(str(level) + " Points", 1,(0,0,0))
    window.blit(textScore,(400,0))
    pygame.display.update()
while run:
    clock.tick(15)# FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if event quits, presses the x button
            run = False # breaks loop
        keys = pygame.key.get_pressed() # gets the keys pressed

    if keys[pygame.K_LEFT]:# pressed left arrow, x coordinate changes by - speed
        #direction, array
        spriteupdate("left",troop.walkLeft,troop)
        if troop.x <= -10:
            pass
        else:
            troop.x-=troop.v
    if keys[pygame.K_RIGHT]: # similar here
        spriteupdate("right", troop.walkRight,troop)
        if troop.x >= 470:
            pass
        else:
            troop.x+=troop.v
            
    
    if keys[pygame.K_SPACE]:
        pygame.mixer.music.load('blaster.mp3')
        pygame.mixer.music.play(0)
        usedx = troop.x
        usedy = troop.y
        if troop.direction == "left":
            blaster.initiate_blast(troop.x,troop.y,-48,0)
            blaster.initiate_blast(troop.x,troop.y,-47,0)
            blaster.initiate_blast(troop.x,troop.y,-46,0)
            blaster.initiate_blast(troop.x,troop.y,-45,0)
            blaster.initiate_blast(troop.x,troop.y,-44,0)
            blaster.initiate_blast(troop.x,troop.y,-43,0)
        elif troop.direction == "right":
            blaster.initiate_blast(troop.x,troop.y,48,0)
            blaster.initiate_blast(troop.x,troop.y,47,0)
            blaster.initiate_blast(troop.x,troop.y,46,0)
            blaster.initiate_blast(troop.x,troop.y,45,0)
            blaster.initiate_blast(troop.x,troop.y,44,0)
            blaster.initiate_blast(troop.x,troop.y,43,0)
        elif troop.direction == "up":
            blaster.initiate_blast(troop.x+15,troop.y,0,48)
            blaster.initiate_blast(troop.x+15,troop.y,0,47)
            blaster.initiate_blast(troop.x+15,troop.y,0,46)
            blaster.initiate_blast(troop.x+15,troop.y,0,45)
            blaster.initiate_blast(troop.x+15,troop.y,0,44)
            blaster.initiate_blast(troop.x+15,troop.y,0,43)
        else:
            blaster.initiate_blast(troop.x+15,troop.y,0,-48)
            blaster.initiate_blast(troop.x+15,troop.y,0,-47)
            blaster.initiate_blast(troop.x+15,troop.y,0,-46)
            blaster.initiate_blast(troop.x+15,troop.y,0,-45)
            blaster.initiate_blast(troop.x+15,troop.y,0,-44)
            blaster.initiate_blast(troop.x+15,troop.y,0,-43)

    if keys[pygame.K_UP]: # same here
        spriteupdate("down",troop.walkDown,troop)
        if troop.y <= -10:
            pass
        else:
            troop.y-=troop.v
    if keys[pygame.K_DOWN]: # same here
        spriteupdate("up",troop.walkUp,troop)
        if troop.y >= 470:
            pass
        else:
            troop.y+=troop.v
    
    update()
        
pygame.quit()
