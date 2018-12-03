import os

path=os.getcwd()

class Character():
    def __init__(self,x,y,r,img,w,h):
        self.x=x
        self.y=y
        self.r=r
        self.img = loadImage(path+"/images/"+img)
        self.w=w 
        self.h=h
        self.dx=0
        self.dy=0
    
    def display(self):
        print("xyz")
        
        
        # stroke(255,0,0)
        # fill(255)
        # ellipse(self.x,self.y,self.r*2,self.r*2)
        # self.update()
        # image(self.img,self.x,self.y-game.y1,self.w,self.h)
        
        
    def update(self):
        print("xyz")
    
        # if self.keyHandler[LEFT]:
        #     self.dx = -10
        # elif self.keyHandler[RIGHT]:
        #     self.dx = 10
        # elif self.keyHandler[UP]:
        #     self.dx = 0
        #     self.dy = -10
        # elif self.keyHandler[DOWN]:
        #     self.dx=0
        #     self.dy = 10
        # else:
        #     self.dx = self.dy = 0
            
        # self.x+=self.dx
        # self.y+=self.dy
        
        # if self.y+self.r>game.h:
        #     self.y=game.h-self.r
        # if self.y <= game.h // 2:
        #     game.y += self.dy
        # if self.y+self.r<game.h//2:
        #     self.y=game.h//2 
        
        
    
class Alien(Character):
    def __init__(self,x,y,r,img,w,h):
        Character.__init__(self,x,y,r,img,w,h)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False, DOWN:False}

    def update(self):
        # Character.update(self)    
        
        if self.keyHandler[LEFT]:
            self.dx = -10
        elif self.keyHandler[RIGHT]:
            self.dx = 10
        elif self.keyHandler[UP]:
            self.dx = 0
            self.dy = -10
        elif self.keyHandler[DOWN]:
            self.dx=0
            self.dy = 10
        else:
            self.dx = self.dy = 0
            
        self.x+=self.dx
        self.y+=self.dy
        
        if self.x-self.r<0:
            self.x=self.r
            
        if self.x+self.r>=game.w//2:
            self.x=(game.w//2)-self.r
            
   
        # if self.y+self.r>game.h:
        #     self.y=game.h-self.r
        if self.y <= game.h // 2:
            game.y0 += self.dy
        if self.y+self.r>=game.h:
            self.y=game.h - (self.r*2)
        

         #COLLISION detection   
       
        for x in game.asteroids1:
            # print(self.distance(x))
            if self.distance(x) <= self.r+ x.r :
                game.gamestate="over"
                 
        
    def distance(self,target):
        
        return ((self.x-target.x)**2 + (self.y-target.y)**2)**0.5
    
    def display(self):
        self.update()
        image(self.img,self.x,self.y-game.y0,self.w,self.h)
        
    
    
class Alien2(Character):
    def __init__(self,x,y,r,img,w,h):
        Character.__init__(self,x,y,r,img,w,h)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False, DOWN:False}

    def update(self):
        
        if self.keyHandler[LEFT]:
            self.dx = -10
        elif self.keyHandler[RIGHT]:
            self.dx = 10
        elif self.keyHandler[UP]:
            self.dx = 0
            self.dy = -10
        elif self.keyHandler[DOWN]:
            self.dx=0
            self.dy = 10
        else:
            self.dx = self.dy = 0
            
        self.x+=self.dx
        self.y+=self.dy
    
            
        if self.x+self.r<=game.w//2:
            self.x=(game.w//2)+self.r
            
        if self.x+self.r>game.w:
            self.x=game.w-self.r
            
        # if self.y>=game.h//2:
        #     game.y=self.dy
    
        
        
        if self.y <= game.h // 2:
            game.y1 += self.dy
        if self.y+self.r>=game.h:
            self.y=game.h-(self.r*2)
            
        print(self.y)
        
       
        
         #COLLISION detection   
       
        for x in game.asteroids2:
            # print(self.distance(x))
            if self.distance(x) <= self.r+ x.r :
                game.gamestate="over"
                 
        
    def distance(self,target):
        
        return ((self.x-target.x)**2 + (self.y-target.y)**2)**0.5
    
    def display(self):
        self.update()
        image(self.img,self.x,self.y-game.y1,self.w,self.h)
    
    
class Asteroid(Character):
     def __init__(self,x, x1, x2, y,r,img,w,h):
        Character.__init__(self,x,y,r,img,w,h)
        self.x1=x1
        self.x2=x2
    
        
        
     def update(self):
         self.x+=2
         if self.x > self.x2:
             self.x = self.x1
         for x in game.asteroids1:
             
             #moves asteroids across screen (vertically, when the alien moves forward)
            if game.alien.dy<0 and game.alien.y<=game.h//2:
                self.dy=(game.alien.dy)*-1
                self.y+=self.dy
            else:
                self.dy=game.alien.dy 
                if self.y>=650 : #WORK
                    self.y-=self.dy  
            
         # print (self.y, self.dy, game.alien.y, game.h//2)
            
                
    
         
         
        
     def display(self):
    
        stroke(255)
        fill(255)
        rect(self.x,self.y,30,10)
        fill(0,255,0)
        # rect(self.x+game.w//2,self.y,30,10)
        
        image (self.img,self.x,self.y)
        # image (self.img, self.x+game.w//2, self.y)
         
class Rocket(Character):
    def __init__(self,x,y,r,img,w,h):
        Character.__init__(self,x,y,r,img,w,h)
        
    def update(self):
        self.x+=2
        if self.x > game.w:
            self.x = 0
        
    # def display(self):
    #     stroke(255)
    #     fill(255,0,0)
    #     rect(self.x,self.y,30,10)
        
        
class Destination(Character):
    def __init__(self,x,y,r,img,w,h):
        Character.__init__(self,x,y,r,img,w,h) 
        
    def update(self):
        self.dx=0
        self.dy=0
        
    def display(self):
        stroke(255)
        fill(0,0,255)
        rect(self.x,self.y,50,50)
        
    
    
        
class Game():
    def __init__(self,w,h): #s_x, e_x
        self.w=w
        self.h=h
        # self.start_x = s_x
        # self.end_x = e_x
        self.pause=False
        self.alien=Alien(self.w//4,self.h-20,20,"alien2.png",40,40)
        self.alien2=Alien2(self.w//2,self.h-20,20,"alien2.png",40,40)
        self.y0=0
        self.y1=0
        self.gamestate="play"
        self.framerate=0
        self.time=0
        # self.dest=Destination(self.w//2,5,30,None,None,None)
        
        self.bg=loadImage(path+"/images/spaceBG.png")
        self.bg2=loadImage(path+"/images/spaceBG.png")
        self.asteroids1=[]
        for i in range(1):
            self.asteroids1.append(Asteroid(i*100 + i*100,0, self.w//2 -(50*2),self.h-100,50,"asteroid.png",50,50))
        self.asteroids2=[]    
        
        for i in range(1):
            self.asteroids2.append((Asteroid(self.w//2+(i*100 + i*100),self.w//2+50*2, self.w -50*2,self.h-100,50,"asteroid.png",50,50)))
            
        self.rockets=[]
        for i in range(4):
            self.rockets.append(Rocket(i*100 + i*100,self.h-500,30,"spaceship.png",96,80))
            
        
    def display(self):
        self.framerate+=2
        y0=self.y0 % self.h
        # print(self.y, self.h, y)
        # print(self.y)
        
        y1=self.y1%self.h
        
        image (self.bg, 0,0,self.w,self.h-y0,              0,y0,self.w,self.h) 
        image (self.bg, 0,self.h-y0,self.w,y0,    0,0,self.w,y0)
        
        image (self.bg2, self.w//2,0,self.w,self.h-y1,              0,y1,self.w,self.h) 
        image (self.bg2, self.w//2,self.h-y1,self.w,y1,    0,0,self.w,y1)
        # print (self.h-y)
       

        
        # image (self.bg,0,0,self.w,self.h)
        line(self.w//2,0,self.w//2,800)
        
        for x in self.asteroids1:
            x.display()
        # self.dest.display()
        
        for x in self.asteroids2:
            x.display()
            
        for r in self.rockets:
            r.display()
            
        
        self.alien.display()
        self.alien2.display()
        
        stroke(255)
        fill(255)
        text("TIME",50,40)
        fill(0)
        rect(50,50,100,20)
        self.time=(self.framerate//60)
        fill(255)
        rect(50,50,max(0,100-(self.time*1)),20)
        
    
        
        
        
    def update(self):
        self.alien.update()
        self.alien2.update()
        for x in self.asteroids1:
            x.update()
            
        for x in self.asteroids2:
            x.update()
            
        for x in self.rockets:
            x.update()
            
        
game=Game(1200,800)

def setup():
   size(game.w,game.h)
   
def draw():
    
    if game.pause==False:
        
        background(0)
        game.update()
        
        
        game.display()
        
        if game.gamestate=="play":
            game.display()
        elif game.gamestate=="over":
            fill(255,0,0)
            textSize(50)
            text("Gameover",game.w//2,game.h//2)

def keyPressed():
    if keyCode == LEFT:
        game.alien2.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        game.alien2.keyHandler[RIGHT] = True
    elif keyCode == UP:
        game.alien2.keyHandler[UP] = True
    elif keyCode == DOWN:
        game.alien2.keyHandler[DOWN]=True
        
    if keyCode == 65:
        game.alien.keyHandler[LEFT] = True
    elif keyCode == 68:
        game.alien.keyHandler[RIGHT] = True
    elif keyCode == 87:
        game.alien.keyHandler[UP] = True
    elif keyCode == 83:
        game.alien.keyHandler[DOWN]=True
    elif keyCode==80:
        if game.pause == True:
            game.pause=False
        else:
            game.pause=True    
        
def keyReleased():
    if keyCode == LEFT:
        game.alien2.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        game.alien2.keyHandler[RIGHT] = False
    elif keyCode == UP:
        game.alien2.keyHandler[UP] = False
    elif keyCode ==DOWN:
        game.alien2.keyHandler[DOWN]=False
        
    if keyCode==65:
        game.alien.keyHandler[LEFT] = False
    elif keyCode==68:
        game.alien.keyHandler[RIGHT] = False
    elif keyCode == 87:
        game.alien.keyHandler[UP] = False
    elif keyCode==83:
        game.alien.keyHandler[DOWN] = False
     
         
