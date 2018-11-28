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
        ellipse(self.x,self.y,self.r,self.r)
        
        
        
    def update(self):
        
       
        self.x+=dx
        self.y+=dy
        
    
    



class Frog(Character):
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
frog=Frog(10,20,20,None,None,None)

def setup():
   size(800,800)
   
def draw():
    background(0)
    frog.update()
    frog.display()

def keyPressed():
    if keyCode == LEFT:
        frog.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        frog.keyHandler[RIGHT] = True
    elif keyCode == UP:
        frog.keyHandler[UP] = True
    elif keyCode == DOWN:
        frog.keyHandler[DOWN]=True
        
        
def keyReleased():
    if keyCode == LEFT:
        frog.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        frog.keyHandler[RIGHT] = False
    elif keyCode == UP:
        frog.keyHandler[UP] = False
    elif keyCode ==DOWN:
        frog.keyHandler[DOWN]=False
