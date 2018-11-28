class Character():
    def __init__(self,x,y,r,img,w,h):
        self.x=x
        self.y=y
        self.r=r
        self.img= img #HAVE TO LOAD IMAGE
        self.w=w #w, h for image not there yet
        self.h=h
        self.dx=0
        self.dy=0
    
    def display(self):
        
        stroke(255,0,0)
        fill(255)
        ellipse(self.x,self.y,self.r*2,self.r*2)
        
        
        
    def update(self):
        self.x+=dx
        self.y+=dy
        
    
    



class Alien(Character):
    def __init__(self,x,y,r,img,w,h):
        Character.__init__(self,x,y,r,img,w,h)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False, DOWN:False}

    def update(self):
        
       
        if self.keyHandler[LEFT]:
            self.dx = -5
            
        elif self.keyHandler[RIGHT]:
            self.dx = 5
        
        elif self.keyHandler[UP]:
            self.dx = 0
            self.dy = -5
        elif self.keyHandler[DOWN]:
            self.dx=0
            self.dy = 5
        else:
            self.dx = self.dy = 0
            
        self.x+=self.dx
        self.y+=self.dy
        
        if self.x-self.r<0:
            self.x=self.r
            
        if self.y+self.r>game.h:
            self.y=game.h-self.r  
            
        if self.x+self.r>game.w:
            self.x=game.w-self.r
        
class Asteroid(Character):
     def __init__(self,x,y,r,img,w,h):
        Character.__init__(self,x,y,r,img,w,h)
        
        
     def update(self):
         self.x+=2
         if self.x > 800:
             self.x = 0
         
         
        
     def display(self):
         stroke(255)
         fill(255)
         rect(self.x,self.y,30,10)
         
class Rocket(Character):
    def __init__(self,x,y,r,img,w,h):
        Character.__init__(self,x,y,r,img,w,h)
        
    def update(self):
        self.x+=2
        if self.x > 800:
            self.x = 0
        
    def display(self):
        stroke(255)
        fill(255,0,0)
        rect(self.x,self.y,30,10)
        
        
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
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.pause=False
        self.alien=Alien(self.w//2,self.h-20,20,None,None,None)
        self.gamestate="play"
        self.dest=Destination(self.w//2,5,30,None,None,None)
        self.asteroids=[]
        for i in range(10):
            
            self.asteroids.append(Asteroid(i*100,self.h-100,30,None,None,None))
            
        self.rockets=[]
        for i in range(10):
            self.rockets.append(Rocket(i*100,self.h-500,30,None,None,None))
            
        
    def display(self):
        
        
        
        for x in self.asteroids:
            x.display()
        self.dest.display()
            
        for r in self.rockets:
            r.display()
            
        self.alien.display()
        
        
    def update(self):
        self.alien.update()
        for x in self.asteroids:
            x.update()
            
        for x in self.rockets:
            x.update()
            
        
game=Game(800,800)

def setup():
   size(game.w,game.h)
   
def draw():
    
    if game.pause==False:
        
        background(0)
        game.update()
        game.display()

def keyPressed():
    if keyCode == LEFT:
        game.alien.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        game.alien.keyHandler[RIGHT] = True
    elif keyCode == UP:
        game.alien.keyHandler[UP] = True
    elif keyCode == DOWN:
        game.alien.keyHandler[DOWN]=True
    elif keyCode==80:
        if game.pause == True:
            game.pause=False
        else:
            game.pause=True
            
            
        
        
        
def keyReleased():
    if keyCode == LEFT:
        game.alien.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        game.alien.keyHandler[RIGHT] = False
    elif keyCode == UP:
        game.alien.keyHandler[UP] = False
    elif keyCode ==DOWN:
        game.alien.keyHandler[DOWN]=False
