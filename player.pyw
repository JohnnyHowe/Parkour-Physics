from game import *

print(windowX)

class PlayerClass:
    scale = 5
    height = 12 * scale
    width = 5 * scale

    x = windowX / 2 - width / 2
    y = windowY - height

    maxSpeed = 5
    maxFallSpeed = 15
    acceleration = 0.5 #and deceleration

    def __init__(self):
        self.still = pg.transform.scale(pg.image.load('still.png'), (self.width, self.height))
        self.wallSlideRight = pg.transform.scale(pg.image.load('wallSlide.png'), (self.width, self.height))
        self.run1Right = pg.transform.scale(pg.image.load('run1.png'), (self.width, self.height))
        self.run2Right = pg.transform.scale(pg.image.load('run2.png'), (self.width, self.height))
        self.run3Right = pg.transform.scale(pg.image.load('run3.png'), (self.width, self.height))
        self.run4Right = pg.transform.scale(pg.image.load('run4.png'), (self.width, self.height))
        self.run5Right = pg.transform.scale(pg.image.load('run5.png'), (self.width, self.height))
        self.roofWalk1Right = pg.transform.scale(pg.image.load('roofWalk1.png'), (self.width, self.height))
        self.roofWalk2Right = pg.transform.scale(pg.image.load('roofWalk2.png'), (self.width, self.height))
        self.roofWalk3Right = pg.transform.scale(pg.image.load('roofWalk3.png'), (self.width, self.height))
        self.roofStill = pg.transform.scale(pg.image.load('roofStill.png'), (self.width, self.height))

        self.wallSlideLeft = pg.transform.flip(self.wallSlideRight, True, False)
        self.run1Left = pg.transform.flip(self.run1Right, True, False)
        self.run2Left = pg.transform.flip(self.run2Right, True, False)
        self.run3Left = pg.transform.flip(self.run3Right, True, False)
        self.run4Left = pg.transform.flip(self.run4Right, True, False)
        self.run5Left = pg.transform.flip(self.run5Right, True, False)
        self.roofWalk1Left = pg.transform.flip(self.roofWalk1Right, True, False)
        self.roofWalk2Left = pg.transform.flip(self.roofWalk2Right, True, False)
        self.roofWalk3Left = pg.transform.flip(self.roofWalk3Right, True, False)


    def update(self):
        self.chooseSprite()
        
        self.parkourElements()
        self.input()
        self.physics()
        
                                
        self.x += self.velocityX
        self.y += self.velocityY

        self.onGround(True)
        for wall in walls:
            if self.y < wall[2]:
                if self.y + self.height > wall[1]:
                    if wall[3] == "right":
                        if self.x + self.width >= wall[0]:
                            if self.x + self.width < wall[0] + 15:
                                self.x = wall[0] - self.width
                                if self.velocityX > 0:
                                    self.x = wall[0] - self.width
                    else:
                        if self.x <= wall[0]:
                            if self.x > wall[0] - 15:
                                self.x = wall[0]
                                if self.velocityX < 0:
                                    self.x = wall[0]

        return (self.img, self.x, self.y)
        

    runTick = 0
    imgChangeSpeed = 5
    roofTick = 0

    
    def chooseSprite(self):
        if self.velocityX == 0:
            self.runTick = 0

        #self.runTick is now set

        if self.onRoof:
            if self.velocityX == 0:
                img = self.roofStill
            elif self.velocityX > 0:
                if self.roofTick <= self.imgChangeSpeed:
                    img = self.roofWalk1Right
                elif self.roofTick <= self.imgChangeSpeed * 2:
                    img = self.roofWalk2Right
                elif self.roofTick <= self.imgChangeSpeed * 3:
                    img = self.roofWalk1Right
                elif self.roofTick <= self.imgChangeSpeed * 4:
                    img = self.roofWalk3Right
                else:
                    self.roofTick = 0
                    img = self.roofWalk1Right
            else:
                if self.roofTick <= self.imgChangeSpeed:
                    img = self.roofWalk1Left
                elif self.roofTick <= self.imgChangeSpeed * 2:
                    img = self.roofWalk2Left
                elif self.roofTick <= self.imgChangeSpeed * 3:
                    img = self.roofWalk1Left
                elif self.roofTick <= self.imgChangeSpeed * 4:
                    img = self.roofWalk3Left
                else:
                    img = self.roofWalk1Left
                    self.roofTick = 0
                    
            self.roofTick += 1

            
        elif self.velocityX < 2 and self.velocityX > -2:
            img = self.still
            self.roofTick = 0
        

        else:
            self.roofTick = 0
            self.runTick += 1
            if self.velocityX > 0:
                if self.runTick < self.imgChangeSpeed:
                    img = self.run1Right
                elif self.runTick < self.imgChangeSpeed * 2:
                    img = self.run2Right
                elif self.runTick < self.imgChangeSpeed * 3:
                    img = self.run3Right
                elif self.runTick < self.imgChangeSpeed * 4:
                    img = self.run4Right
                elif self.runTick < self.imgChangeSpeed * 5:
                    img = self.run5Right
                else:
                    self.runTick = 0
                    img = self.run1Right
                    
             
            if self.velocityX < 0:
                if self.runTick < self.imgChangeSpeed:
                    img = self.run1Left
                elif self.runTick < self.imgChangeSpeed * 2:
                    img = self.run2Left
                elif self.runTick < self.imgChangeSpeed * 3:
                    img = self.run3Left
                elif self.runTick < self.imgChangeSpeed * 4:
                    img = self.run4Left
                elif self.runTick < self.imgChangeSpeed * 5:
                    img = self.run5Left
                else:
                    self.runTick = 0
                    img = self.run1Left
                    
        self.img = img


    def onGround(self, set_values):
        for ground in platforms:
            if self.x < ground[2]:
                if self.x + self.width > ground[0]:
                    if self.y + self.height >= ground[1]:
                        if self.y + self.height <= ground[1] + 15:
                            if self.velocityY >= 0:
                                if set_values:
                                    self.y = ground[1] - self.height
                                    self.velocityY = 0
                                return True
        
        

    velocityX = 0
    velocityY = 0

    def physics(self):
        if not self.onRoof:
            if self.velocityY < self.maxFallSpeed:
                self.velocityY += 0.5

        self.onGround(True)


        for wall in walls:
            if self.y < wall[2]:
                if self.y + self.height > wall[1]:
                    if wall[3] == "right":
                        if self.x + self.width >= wall[0]:
                            if self.x + self.width < wall[0] + 15:
                                self.x = wall[0] - self.width
                                if self.velocityX > 0:
                                    self.velocityX = 0
                    else:
                        if self.x <= wall[0]:
                            if self.x > wall[0] - 15:
                                self.x = wall[0]
                                if self.velocityX < 0:
                                    self.velocityX = 0

        
    
        
    
    def input(self):
        pressedKeys = pg.key.get_pressed()


        if self.onRoof:
            multiplyer = 0.5
            self.maxSpeed = 2
        elif not self.onGround(False):
            multiplyer = 0.5
            self.maxSpeed = 5
        else:
            multiplyer = 1
            self.maxSpeed = 5

        if pressedKeys[pg.K_a] and pressedKeys[pg.K_d]:
            if self.velocityX > 0:
                self.velocityX -= self.acceleration * multiplyer
            elif self.velocityX < 0:
                self.velocityX += self.acceleration * multiplyer

        elif pressedKeys[pg.K_a]:
            if self.velocityX > -(self.maxSpeed):  
                self.velocityX -= self.acceleration * multiplyer
            else:
                self.velocityX = -(self.maxSpeed)
                
        elif pressedKeys[pg.K_d]:
            if self.velocityX < self.maxSpeed:  
                self.velocityX += self.acceleration * multiplyer
            else:
                self.velocityX = self.maxSpeed

        else:
            if self.velocityX > 0:
                self.velocityX -= self.acceleration * multiplyer
            elif self.velocityX < 0:
                self.velocityX += self.acceleration * multiplyer

        if pressedKeys[pg.K_w]:
            if self.onGround(False):
                if not self.onRoof:
                    self.velocityY -= 10

        for wall in walls:
            if self.y + self.height > wall[1]:
                if self.y < wall[2]:
                    if wall[3] == "right":
                        if self.x + self.width >= wall[0]:
                            if self.x + self.width <= wall[0] + 10:
                                self.x = wall[0] - self.width
                    else:
                        if self.x < wall[0]:
                            if self.x > wall[0] - 10:
                                self.x = wall[0]


    onRoof = False

    def touchingWall(setValues):
        for wall in walls:
            if self.y + self.height > wall[1]:
                if self.y < wall[2]:
                    if wall[3] == "right":
                        if self.x + self.width >= wall[0]:
                            if self.x + self.width < wall[0] + 15:
                                if setValues:
                                    self.x = wall[0] - self.width
                                return True
                    else:
                        if self.x <= wall[0]:
                            if self.x > wall[0] - 15:
                                if setValues:
                                    self.x = wall[0]
                                return True

    
    
    
    def parkourElements(self):
        pressedKeys = pg.key.get_pressed()
        self.onRoof = False

        for wall in walls:
            if self.y + self.height > wall[1]:
                if self.y < wall[2]:
                    if wall[3] == "right":
                        if self.x + self.width >= wall[0]:
                            if self.x + self.width < wall[0] + 15:
                                for ground in platforms:
                                    if self.y + self.height <= ground[1] + 20:
                                        if self.velocityY > 0:
                                            self.img = self.wallSlideRight
                                            if not pressedKeys[pg.K_s]:
                                                self.velocityY = 2
                                                    
                                        
                                            #Wall Grab
                                                if self.y + self.height * 0.25 <= wall[1]:
                                                    if self.y + self.height > wall[1]:
                                                        if self.y + self.scale * 5 + 2 >= wall[1]:
                                                            self.y = wall[1] - self.scale * 5
                                                            self.velocityY = 0
                                                            if pressedKeys[pg.K_w]:
                                                                self.velocityY = 2
                                                                self.velocityX = 7
                                                        else:
                                                            self.velocityY = 2
                                                            
                                                if pressedKeys[pg.K_w]:
                                                    self.velocityY -= 10
                                                    self.velocityX -= 7
                                            
                                                        
                                
                    else:
                        if self.x <= wall[0]:
                            if self.x > wall[0] - 15:
                                for ground in platforms:
                                    if self.y + self.height <= ground[1] + 20:
                                        if self.velocityY > 0:
                                            self.img = self.wallSlideLeft
                                            if not pressedKeys[pg.K_s]:
                                                self.velocityY = 2

                                            #Wall Grab
                                                if self.y + self.height * 0.25 <= wall[1]:
                                                    if self.y + self.height > wall[1]:
                                                        if self.y + self.scale * 5 + 2 >= wall[1]:
                                                            self.y = wall[1] - self.scale * 5
                                                            self.velocityY = 0
                                                            if pressedKeys[pg.K_w]:
                                                                self.velocityY = 2
                                                                self.velocityX = -7
                                                        else:
                                                            self.velocityY = 2
                                                            
                                                if pressedKeys[pg.K_w]:
                                                    self.velocityY -= 10
                                                    self.velocityX += 7


                    #Celing walk
                    for roof in roofs:
                        if self.x + self.width / 2 < roof[2]:
                            if self.x + self.width / 2 > roof[0]:
                                if self.y <= roof[1]:
                                    if self.y > roof[1] - 15:
                                        self.y = roof[1]
                                        self.velocityY = 0
                                        if pressedKeys[pg.K_w]:
                                            self.onRoof = True
                                        else:
                                            self.onRoof = False


player = PlayerClass()
