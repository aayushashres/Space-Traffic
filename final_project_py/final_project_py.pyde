add_library('minim')
import os, time, random
player = Minim(this)
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
        return
            
    def update(self):
        return 
class Alien(Character):
    def __init__(self,x,y,r,img,w,h):
        Character.__init__(self,x,y,r,img,w,h)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False, DOWN:False}
    def update(self):
        
        if game.gamestate1=="play": #character only moves if in play state
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
        #checking boundaries
            if self.x-self.r<0:
                self.x=self.r
            if self.x+(self.r*2)>=game.w//2:
                self.x=(game.w//2)-(self.r*2)
                
            if self.y <= game.h // 2 and self.y > game.maxmid: 
                game.y0 += self.dy
                
            if self.y+(self.r*2)>=game.h:
                self.y=game.h - (self.r*2)
                
            if self.y<=game.maxy:
                self.y=game.maxy
        
             #gameover if time limit exceeded    
            if game.time1>60:
                game.gamestate1="over"
            
            #COIN COLLECTION
            for x in game.coins1:
                if self.distance(x)<=self.r+x.r:
                    game.coins1.remove(x)
                    game.coincount1+=1
            # asteroid collision
            for x in game.asteroids1:
                if self.distance(x) <= self.r+ x.r :
                    game.numlives1-=1
                    x.music.rewind()
                    x.music.play()
                    # the delay function built in to processing will prevent one collision from counting as many and removing all three lives at one 
                    delay(200)
                    self.y=750
                    game.y0=0
                    # print(game.numlives1)
                    if game.numlives1<=0:
                        game.gamestate1="over"
            # fireball collision        
            for x in game.fireballs1:
                 if self.distance(x) <= self.r+ x.r :
                    game.numlives1-=1
                    x.music.rewind()
                    x.music.play()
                    delay(200)
                    self.y=750
                    game.y0=0
                    # print(game.numlives1)
                    if game.numlives1<=0:
                        game.gamestate1="over"
            # Rocket Part
            ys = [] 
            for i in game.rockets2: 
                ys.append(i.y)
            if self.y <= max(ys) + game.rockets2[1].h and self.y >= min(ys):  
           # if self.y <= 350 and self.y >= 20: # if the alien is in the segment of the game that contains the rockets 
               
                # part of the game is that you must move on the next row of rockets before they move off screen, so if you dont, you still lose a life and start over
                for x in game.rockets:
                    if self.distance(x) <= self.r + x.r: 
                        self.dy = 0
                        self.x = x.x
                     #   self.dx = x.dx
                        # rocket update
                        if x.side == "left":     
                            if x.x > x.x2:
                                self.x = r.x1  
                        elif x.side == "right":
                            if x.x < x.x1:
                                self.x = x.x2
                # this if statment already iterates over the rocket list, therefore, it should not be under the above if statment since that is redundant
                # this was causing all three lives to be lost before
                if self.between_rockets(game.rockets) == False: #self.keyHandler[UP] == True 
                    for i in range(1): # to prevent losing all three lives at once 
                        game.numlives1-=1
                        x.music.rewind()
                        x.music.play()
                        self.y=750
                        game.y0 = 0
                    
                        if game.numlives1<=0:                               
                            game.gamestate1="over"
                    delay(200)
            # win check when destination is reached 
            if self.distance(game.dest1) <= (self.r + game.dest1.r):
                game.score1+= (game.numlives1*100) + (game.coincount1*10) +((60-game.time1)*10) #score calculation
                
                game.gamestate1 = "won"
                
                           
        
    def distance(self,target):
        return ((self.x-target.x)**2 + (self.y-target.y)**2)**0.5
    
    def between_rockets(self, rocket_list):
        closest_in_line = rocket_list[0]
        for r in rocket_list:
            if r.y - self.y < 50:
                closest_in_line = r
                # this function checks if the outer limit of the alien is within the limits of the rocket, if only the two outer limits of the alien and the object 
                # are intersecting, that is enough, this is to keep the game lenient, espectially as it is really easy to lose in section 
                if (self.x + self.w) >= closest_in_line.x and self.x <= (closest_in_line.x + closest_in_line.w):
                    return True
        return False 
    
    def display(self):
        self.update()
        image(self.img,self.x,self.y-game.y0,self.w,self.h)
        
class Alien2(Character):
    def __init__(self,x,y,r,img,w,h):
        Character.__init__(self,x,y,r,img,w,h)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False, DOWN:False}

    def update(self):
        if game.gamestate2=="play":
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

            if self.x<=game.w//2:
                self.x=(game.w//2)
                
            if self.x+(self.r*2)>game.w:
                self.x=game.w-(self.r*2)

            if self.y <= game.h // 2 and self.y > game.maxmid: 
                game.y1 += self.dy
                
            if self.y+(self.r*2)>=game.h:
                self.y=game.h-(self.r*2)
                
            if self.y<=game.maxy:
                self.y=game.maxy
            
            if game.time1>60:
                game.gamestate2="over"
            
            
            # asteroid collision   
            for x in game.asteroids2:
                # print(self.distance(x))
                if self.distance(x) <= self.r+ x.r :
                    game.numlives2-=1
                    x.music.rewind()
                    x.music.play()
                    delay(200)
                    self.y=750
                    game.y1=0
                    # print(game.numlives2)
                    if game.numlives2<=0:
                        game.gamestate2="over"
            # fireball collision
            for x in game.fireballs2: #WORK ON COLLISION FOR FIREBALL
                if self.distance(x) <= self.r+ x.r :
                    game.numlives2-=1
                    x.music.rewind()
                    x.music.play()
                    delay(200)
                    self.y=750
                    game.y1=0
                
                    if game.numlives1<=0:
                        game.gamestate2="over"
                        
            #COINS
            for x in game.coins2:
                if self.distance(x)<=self.r+x.r:
                    game.coins2.remove(x)
                    game.coincount2+=1
            
            # Rocket Part 
            ys = [] # in order to avoid hardcoding the range in which there are rockets so that we can include rockets in other levels at different ranges
            for i in game.rockets2: # ys is a list of all the y values of the rockets which are all in the list rockets2, this for loop appends all the y values to this list
                ys.append(i.y)
            if self.y <= max(ys) + game.rockets2[1].h and self.y >= min(ys):  # the range is between the minimum and maximum y
         #   if self.y <= 350 and self.y >= 20: # if the alien is in the segment of the game that contains the rockets 
                for x in game.rockets2: # change from alien 1
                    if self.distance(x) <= self.r + x.r: 
                        self.dy = 0
                        self.x = x.x
                     #   self.dx = x.dx
                        # rocket update
                        if x.side == "left":     
                            if x.x > x.x2:
                                self.x = r.x1  
                        elif x.side == "right":
                            if x.x < x.x1:
                                self.x = x.x2
                # this if statment already iterates over the rocket list, therefore, it should not be under the above if statment since that is redundant
                # this was causing all three lives to be lost before
                if self.between_rockets(game.rockets2) == False: #self.keyHandler[UP] == True 
                    for i in range(1): # to prevent losing all three lives at once 
                        game.numlives2-=1 # different from alien 1
                        x.music.rewind()
                        x.music.play()
                        self.y=750
                        game.y1 = 0 # change from alien 1 
                    
                        if game.numlives2<=0:                               
                            game.gamestate2="over"
                    delay(200)
            # win check when destination is reached 
            if self.distance(game.dest2) <= (self.r + game.dest2.r):
                game.score2+= (game.numlives2*100) + (game.coincount2*10) +((60-game.time1)*10)
                game.gamestate2 = "won"
                
            #if time up, gameover
            
            # if game.time1>60 and game.gamestate2!="over":
            #     game.gamestate2=="over"
    
                           
    
    def distance(self,target): #dist between asteroid and player
        return ((self.x-target.x)**2 + (self.y-target.y)**2)**0.5
    
    def between_rockets(self, rocket_list):
        closest_in_line = rocket_list[0]
        for r in rocket_list:
            if r.y - self.y < 50:
                closest_in_line = r
                # this function checks if the outer limit of the alien is within the limits of the rocket, if only the two outer limits of the alien and the object 
                # are intersecting, that is enough, this is to keep the game lenient, espectially as it is really easy to lose in section 
                if (self.x + self.w) >= closest_in_line.x and self.x <= (closest_in_line.x + closest_in_line.w):
                    return True
        return False 
    
    def display(self):
        self.update()
        image(self.img,self.x,self.y-game.y1,self.w,self.h)
    
    
class Asteroid(Character):
     def __init__(self,x, x1, x2, dx, y,r,img,w,h, which_y): #x1, x2 are start and end of asteroid
        Character.__init__(self,x,y,r,img,w,h)
        self.x1=x1
        self.x2=x2
        self.dx=dx
        self.which_y = which_y  
        self.music = player.loadFile(path+"/sounds/collision.mp3")   
     def update(self):
         self.x+=self.dx
         if self.x > self.x2:
             self.x = self.x1
     def display(self):
        if self.which_y == 0:
            image (self.img,self.x,self.y-game.y0) 
        else:
            image (self.img,self.x,self.y-game.y1)
   
class Fireball(Asteroid):
    def __init__(self,x, x1, x2,dx ,y,r,img,w,h,which_y): #x1, x2 are start and end of asteroid
        Asteroid.__init__(self,x, x1, x2,dx ,y,r,img,w,h,which_y)
        
    def update(self):
        self.x+=self.dx
        if self.x < self.x2:
            self.x = self.x1
    def display(self):
        if self.which_y==0:
            image (self.img,self.x,self.y-game.y0) 
        else:
            image(self.img,self.x,self.y-game.y1)
            
    
class Rocket(Character):
    def __init__(self,x,x1,x2,dx,y,r,img,w,h, which_y,side):
        Character.__init__(self,x,y,r,img,w,h)
        self.x1=x1
        self.x2=x2
        self.y1=self.y #y1 to check initial position)
        self.dx=dx
        self.which_y=which_y
        self.side = side 
        self.music = player.loadFile(path+"/sounds/rocket.mp3")   
        if self.side == "right":
            self.dx = -self.dx
    def update(self):
        self.x += self.dx
        if self.side == "left":     
            if self.x > self.x2:
                self.x = self.x1  
        elif self.side == "right":
            if self.x < self.x1:
                self.x = self.x2   
    def display(self):        
        if self.which_y == 0:
            image (self.img,self.x,self.y-game.y0) 
        else:
            image (self.img,self.x,self.y-game.y1)

class Destination(Character):
    def __init__(self,x,y,r,img,w,h,which_y):
        Character.__init__(self,x,y,r,img,w,h) 
        self.dx=0
        self.dy=0
        # self.y1=self.y
        self.which_y=which_y
        
    def update(self):
        return
        
        
    def display(self):
        if self.which_y==0:
            image(self.img,self.x,self.y-game.y0)
        else:
            image(self.img,self.x,self.y-game.y1)
        
class Coins(Character):
    def __init__(self,x,y,r,img,w,h,which_y):
        Character.__init__(self,x,y,r,img,w,h)
        self.which_y=which_y 
        
        
    def display(self):
        if self.which_y==0:
            image(self.img,self.x,self.y-game.y0)
        else:
            image(self.img,self.x,self.y-game.y1)
    
    #to make sure coins dont overlap
    def coincollision(self):
        if self.which_y==0: #0 is for player1, 1 is for player2
            
            for x in game.coins1:
                
                if self.distance(x) <= self.r+ x.r :
                    return True
            return False
        else:
            for x in game.coins2:
                
                if self.distance(x) <= self.r+ x.r : # collides
                    return True
            return False # doesn't collide with ANY coins
        
    
    def distance(self,target): #dist between two coins
        return ((self.x-target.x)**2 + (self.y-target.y)**2)**0.5

level=0
maxy=0
maxmid=0
time=0

class Game():
    def __init__(self,w,h,level,maxy,maxmid,time): 
        self.w=w
        self.h=h
        self.level=level
        self.maxy=maxy  #This will check the upper boundry for the character
        self.maxmid=maxmid #This is the y position after which alien can move to the uper half of the screen)
        self.time=time
    
        self.pause=False
        self.alien=Alien(self.w//4,self.h-20,20,"alien2.png",40,40)
        self.alien2=Alien2(self.w//2,self.h-20,20,"alien2.png",40,40)
        self.y0=0
        self.y1=0
        self.gamestate1="menu"
        self.gamestate2="menu"
        self.framerate=0
        self.time1=0
        self.music = player.loadFile(path+"/sounds/music1.mp3")
        self.score1=0
        self.score2=0
        
        self.coincount1=0
        self.coincount2=0
        
        self.TESTLIST = [1,2,3,4,10]
        #initial num of lives is 3 for each player
        self.numlives1=3
        self.numlives2=3
        
        self.lives=loadImage(path+"/images/life.png")
        self.coin=loadImage(path+"/images/coin.png")
        
        self.bg=loadImage(path+"/images/spaceBG.png")
        self.bg2=loadImage(path+"/images/spaceBG.png")
        self.rocketbg1=loadImage(path+"/images/rocketbg.jpg")
        self.bgmenu=loadImage(path+"/images/menubg.png")
        self.instr=loadImage(path+"/images/instructions.png")
        
        self.asteroids1=[]
        self.asteroids2=[]
        self.rockets=[]
        self.rockets2=[]
        self.fireballs1=[]
        self.fireballs2=[]
        self.dest1=None
        self.dest2=None
        self.coins1=[]
        self.coins2=[]
        
    def loadStage(self):
    
        file=open(path+"/level"+str(self.level)+".csv","r")
        for l in file:
            l=l.strip().split(",")
            if l[0] == "AsteroidP1": #P1 means player1, P2 is player2. adding asteroids to list
                cnt=0
                for i in range(2): #first layer of asteroids
                    self.asteroids1.append(Asteroid(cnt*int(l[1])+cnt*100,int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"asteroid.png",int(l[8]),int(l[9]),0)) #l[7] has some garbage????
                    cnt+=1
                cnt=0
                for i in range(3): #second layer of asteroids
                    self.asteroids1.append(Asteroid((cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-100,int(l[6]),"asteroid.png",int(l[8]),int(l[9]),0))
                    cnt+=1
            if l[0]=="AsteroidP2":
                cnt=0
                for i in range(2):
                    self.asteroids2.append(Asteroid(625+(cnt*int(l[1])+cnt*100),int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"asteroid.png",int(l[8]),int(l[9]),1))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.asteroids2.append(Asteroid(625+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-100,int(l[6]),"asteroid.png",int(l[8]),int(l[9]),1))
                    cnt+=1

                
            if l[0] == "AsteroidL2P1": #P1 means player1, only available for level2
                cnt=0
                for i in range(2): #third layer of asteroids
                    self.asteroids1.append(Asteroid(cnt*int(l[1])+cnt*100,int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"asteroid.png",int(l[8]),int(l[9]),0)) 
                    cnt+=1
                    
            if l[0] == "AsteroidL2P2": #P1 means player1, only available for level2
                cnt=0
                for i in range(2): #third layer of asteroids
                    self.asteroids2.append(Asteroid(cnt*int(l[1])+cnt*100,int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"asteroid.png",int(l[8]),int(l[9]),1)) 
                    cnt+=1
                
            if l[0]=="RocketP1":
                cnt=0
                for i in range(3):
                    self.rockets.append(Rocket((cnt*int(l[1])+cnt*100),int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"left"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets.append(Rocket(120+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-100,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"right"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets.append(Rocket(240+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-200,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"left"))
                    cnt+=1
                cnt = 0
                for i in range(3):
                    self.rockets.append(Rocket(360+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-300,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"right"))
                    cnt+=1
            if l[0]=="RocketP2":
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket((600+(cnt*int(l[1])+cnt*100)),int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"left"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket(720+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-100,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"right"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket(840+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-200,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"left"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket(960+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-300,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"right"))
                    cnt+=1
            if l[0]=="RocketL2P1":
                cnt=0
                for i in range(3):
                    self.rockets.append(Rocket((cnt*int(l[1])+cnt*100),int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"left"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets.append(Rocket(120+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-100,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"right"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets.append(Rocket(240+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-200,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"left"))
                    cnt+=1
                cnt = 0
                for i in range(3):
                    self.rockets.append(Rocket(360+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-300,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"right"))
                    cnt+=1 
            if l[0]=="RocketL2P2":
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket((600+(cnt*int(l[1])+cnt*100)),int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"left"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket(720+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-100,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"right"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket(840+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-200,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"left"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket(960+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-300,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"right"))
                    cnt+=1  
                     
            if l[0]=="RocketL3P1":
                cnt=0
                for i in range(3):
                    self.rockets.append(Rocket((cnt*int(l[1])+cnt*100),int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"left"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets.append(Rocket(120+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-100,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"right"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets.append(Rocket(240+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-200,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"left"))
                    cnt+=1
                cnt = 0
                for i in range(3):
                    self.rockets.append(Rocket(360+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-300,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),0,"right"))
                    cnt+=1   
            if l[0]=="RocketL3P2":
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket((600+(cnt*int(l[1])+cnt*100)),int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"left"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket(720+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-100,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"right"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket(840+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-200,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"left"))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.rockets2.append(Rocket(960+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-300,int(l[6]),"spaceship.png",int(l[8]),int(l[9]),1,"right"))
                    cnt+=1     
                    
            if l[0]=="FireballP1":
                cnt=0
                for i in range(3):
                    self.fireballs1.append(Fireball((550-(cnt*int(l[1])+cnt*100)) ,int(l[2]) ,int(l[3]) ,int(l[4]), int(l[5]) ,int(l[6]) ,"fireball(left).png",int(l[8]),int(l[9]),0))
                    cnt+=1
                cnt=0    
            if l[0]=="FireballP2":
                cnt=0
                for i in range(3):
                    self.fireballs2.append(Fireball((1200-(cnt*int(l[1])+cnt*100)) ,int(l[2]) ,int(l[3]) ,int(l[4]), int(l[5]) ,int(l[6]) ,"fireball(left).png",int(l[8]),int(l[9]),1))
                    cnt+=1
                # print (self.fireballs2)
            if l[0]=="FireballP1L3":
                cnt=0
                for i in range(3):
                    self.fireballs1.append(Fireball((550-(cnt*int(l[1])+cnt*100)) ,int(l[2]) ,int(l[3]) ,int(l[4]), int(l[5]) ,int(l[6]) ,"fireball(left).png",int(l[8]),int(l[9]),0))
                    cnt+=1
            if l[0]=="FireballP2L3":
                cnt=0
                for i in range(3):
                    self.fireballs2.append(Fireball((550-(cnt*int(l[1])+cnt*100)) ,int(l[2]) ,int(l[3]) ,int(l[4]), int(l[5]) ,int(l[6]) ,"fireball(left).png",int(l[8]),int(l[9]),1))
                    cnt+=1
                
            if l[0]=="Coin1":
                numcoins1=0 #to check number of coins in the level
                numcoins2=0
                cointemp=None
                cointemp2=None
                # for i in range(5):    
                while numcoins1 < int(l[1]) and numcoins2 < int(l[1]):
                    # print("CHECK")
                    x=random.randint(0,550)
                    y=random.randrange(maxy,700)
                    x1=random.randint(620,1150)
                    y1=random.uniform(maxy,700)
                    # print(x,y)
                    cointemp=(Coins(x,y,12,"coin.png",24,24,0)) #temp coin to add a coin to check if there is collision.
                    cointemp2=(Coins(x1,y1,12,"coin.png",24,24,1))
                    
                    
                    if not cointemp.coincollision():
                        self.coins1.append(cointemp)
                        numcoins1+=1
                    if not cointemp2.coincollision():
                        self.coins2.append(cointemp2)
                        numcoins2+=1
                
            if l[0]=="Dest1":
                self.dest1=Destination(int(l[1]),int(l[2]),int(l[3]),"planet.png",int(l[5]),int(l[6]),0)
            if l[0]=="Dest2":
                self.dest2=Destination(int(l[1]),int(l[2]),int(l[3]) ,"planet.png", int(l[5]) ,int(l[6]),1)
                

                    
    def loseLife(self, side):
        # print("Subtract 1 from player's life")
        if side == "RIGHT":
            self.numlives1-=1
            self.alien2.y = 750
            self.y1 = 0
        elif side == "LEFT":
            self.numlives2-=1
            self.alien.y = 750
            self.y0 = 0
                
    def display(self):
        # print("now displaying")
        self.framerate+=1
        y0=self.y0 % self.h
        y1=self.y1%self.h
        
        image (self.bg,0,0,self.w,self.h-y0,0,y0,self.w,self.h) 
        image (self.bg,0,self.h-y0,self.w,y0,0,0,self.w,y0)
        
        
        
        image (self.bg2,self.w//2,0,self.w,self.h-y1,0,y1,self.w,self.h) 
        image (self.bg2,self.w//2,self.h-y1,self.w,y1,0,0,self.w,y1)
 
        line(self.w//2,0,self.w//2,800)
        for x in self.asteroids1:
            x.display()        
        for x in self.asteroids2:
            x.display()
            
        for r in self.rockets:
            r.display()
            
        for r in self.rockets2:
            r.display()
        for f in self.fireballs1:
            f.display()
        for f in self.fireballs2:
            f.display()
            
        for c in self.coins1:
            c.display()
        for c in self.coins2:
            c.display()
        self.dest1.display()
        self.dest2.display()
        
        # Timer bars
        stroke(255)
        fill(255)
        text("TIME",50,40)
        text("TIME",self.w//2+50,40)       
        fill(0)
        rect(50,50,120,20)
        if self.gamestate1 == "play": # when the game is lost, the time will stop counting down
            self.time1=(self.framerate//60)
            fill(255)
            rect(50,50,max(0,120-(self.time1*2)),20) #TIME is exactly 60 sec right now, may change as per level by using game.time
        fill(0)
        rect((self.w//2)+50,50,120,20)
        if self.gamestate2 == "play": # when the game is lost, the time will stop counting down 
            self.time1=(self.framerate//60)       
            fill(255)
            rect((self.w//2)+50,50,max(0,120-(self.time1*2)),20)

        # textSize(30)
        # text(self.time1,160,20)

        #LIVES DISPLAY
        for i in range(self.numlives1):
            image(self.lives, 40 +(i*45),80)
        for i in range(self.numlives2):
            image(self.lives, 640+(i*45),80)
            
        for x in self.coins1:
            x.display()
            
        #COINS DISPLAY
        fill(255,0,0)
        rect(505,60,60,25)
        rect(1105,60,60,25)
    
        image(self.coin,540,60)
        image(self.coin,1140,60)
   
        textSize(20)
        fill(255)
        text(str(self.coincount2)+"X", 1110,80)
        text(str(self.coincount1)+"X", 510,80)
        
        self.alien.display()
        self.alien2.display()
        
        
    def update(self):
        self.alien.update()
        self.alien2.update()
        for x in self.asteroids1:
            x.update()
            
        for x in self.asteroids2:
            x.update()
            
        for x in self.rockets:
            x.update()
            
        for r in self.rockets2:
            r.update()
            
        for f in self.fireballs1:
            f.update()
        for f in self.fireballs2:
            f.update()
    
        if game.time1>60 and game.gamestate2!="over":
            game.gamestate2="over"
        
            
            
        
game=Game(1200,800,level,maxy,maxmid,time)

def setup():
   size(game.w,game.h)
   
   
def draw():
    # print("{}, {}".format(game.gamestate1, game.gamestate2))
    # print(game.gamestate1, game.gamestate2, level)
    if game.pause==False:
        
        background(0)
        game.update()
        
        if game.gamestate1=="menu" and game.gamestate2=="menu":

            image(game.bgmenu,0,0,1200,800)
            textSize(30)
            if game.w//2.5 < mouseX < game.w//2.5 + 200 and game.h//3 < mouseY < game.h//3 + 50:
                fill(0,255,0)
            else:
                fill(255)
            text("Level 1", game.w//2.5, game.h//3+40)
            if game.w//2.5 < mouseX < game.w//2.5 + 200 and game.h//3+100 < mouseY < game.h//3 + 150:
                fill(0,255,0)
            else:
                fill(255)
            text("Level 2", game.w//2.5, game.h//3+140)
            if game.w//2.5 < mouseX < game.w//2.5 + 200 and game.h//3+200 < mouseY < game.h//3 + 250:
                 fill(0,255,0)
            else:
                fill(255)
            text("Level 3", game.w//2.5, game.h//3+240)
            if game.w//2.5 < mouseX < game.w//2.5 + 200 and game.h//3+300 < mouseY < game.h//3 + 350: 
                fill(0,255,0)
            else:
                fill(255)
            text("Instructions",game.w//2.6,game.h//3+340)
            
            
        elif game.gamestate1=="instruction" and game.gamestate2=="instruction":
                image(game.bgmenu,0,0,1200,800)
                image(game.instr,game.w//5.5,game.h//5,800,400)
                
                if game.w//2 < mouseX < game.w//2 + 200 and game.h//3+400 < mouseY < game.h//3 + 450:
                    fill(0,255,0)
                else:
                    fill(255)
                text("Return",game.w//2,game.h//3+440) 
                
        
        
        elif game.gamestate1=="play" and game.gamestate2=="play":

            game.display()
            game.music.play()
            
   #CONDITIONS TO DISPLAY GAME WON/OVER MESSAGE ON EACH SIDE 
        if game.gamestate1=="over":
            game.display()
            fill(255,0,0)
            textSize(50)
            text("Gameover",0,game.h//2)
        if game.gamestate2=="over":
            game.display()
            fill(255,0,0)
            textSize(50)
            text("Gameover",game.w//2,game.h//2)
        # if both games are lost, the gameover sign will display on both
        if game.gamestate1 == "over" and game.gamestate2 == "over":
            game.display()
            fill(255,0,0)
            textSize(50)
            text("Gameover",0,game.h//2)
            text("SCORE: "+str(game.score1),0,game.h//3)
            text("Gameover",game.w//2,game.h//2)
            text("SCORE: "+str(game.score2),game.w//2,game.h//3)
            
        if game.gamestate1=="won":
            game.display()
            fill(0,255,0) # won will be in green 
            textSize(50)
            text("Game Won!",0,game.h//2)
            text("SCORE: "+str(game.score1),0,game.h//3)
        if game.gamestate2=="won":
            game.display()
            fill(0,255,0)
            textSize(50)
            text("Game Won!",game.w//2,game.h//2)
            text("SCORE: "+str(game.score2),game.w//2,game.h//3)
        if game.gamestate1 == "won" and game.gamestate2 == "won":
            game.display()
            fill(0,255,0)
            textSize(50)
            text("SCORE: "+str(game.score2),game.w//2,game.h//3)
            text("SCORE: "+str(game.score1),0,game.h//3)
            if game.score1>game.score2:
                
                text("Game Won by Player 1!",0,game.h//2)
                
            elif game.score2>game.score1:
                text("Game Won by player 2!",game.w//2,game.h//2)
                
        if game.gamestate1=="won" and game.gamestate2=="over":
            game.display()
            fill(0,255,0)
            textSize(50)
            text("Game Won by Player 1!",0,game.h//2)
            text("SCORE: "+str(game.score1),0,game.h//3)
            fill(255,0,0)
            text("Gameover",game.w//2,game.h//2)
            text("SCORE: "+str(game.score2),game.w//2,game.h//3)
        if game.gamestate2=="won" and game.gamestate1=="over":
            game.display()
            fill(255,0,0)
            textSize(50)
            text("Gameover",0,game.h//2)
            text("SCORE: "+str(game.score1),0,game.h//3)
            fill(0,255,0)
            text("Game Won by Player 2!",game.w//2,game.h//2)
            text("SCORE: "+str(game.score2),game.w//2,game.h//3)
        if ((game.gamestate1=="over" and game.gamestate2=="over") or (game.gamestate1=="won" and game.gamestate2=="won") or (game.gamestate1=="over" and game.gamestate2=="won") or (game.gamestate1=="won" and game.gamestate2=="over")) :   
            fill(109,108,104)
            rect(500,650,200,50)
            textSize(30)
            fill(0)
            text("NEW GAME" ,510,680)
            
        
            
            

            
        
        

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


def mouseClicked():
    global level #global var accessed in order to change the level
    if game.level==0:
        if game.w//2.5 < mouseX < game.w//2.5 + 200 and game.h//3 < mouseY < game.h//3 + 50: #for level 1
            game.gamestate1="play" 
            game.gamestate2="play"
            level=1 #SETTING LEVEL
            game.level = level
            maxy=-1000
            game.maxy=-1000
            maxmid=-620
            game.maxmid=-620
            time=60
            game.time=60
            game.loadStage()
            #set max, endpoint,time
            
        if game.w//2.5 < mouseX < game.w//2.5 + 200 and game.h//3+100 < mouseY < game.h//3 + 150: #for level 2
            game.gamestate1="play" 
            game.gamestate2="play"
            level=2 #SETTING LEVEL
            game.level = level
            maxy=-1500
            game.maxy=-1500  
            maxmid=-1280
            game.maxmid=-1280
            time=60
            game.time=60
            
            game.loadStage()
        
        if game.w//2.5 < mouseX < game.w//2.5 + 200 and game.h//3+200 < mouseY < game.h//3 + 250: 
            game.gamestate1="play" 
            game.gamestate2="play"
            level=3 #SETTING LEVEL
            game.level = level
            maxy=-2000
            game.maxy=-2000  
            maxmid=-1620
            game.maxmid=-1620
            time=60
            game.time=60
            
            game.loadStage()
        
        
    if game.w//2.5 < mouseX < game.w//2.5 + 200 and game.h//3+300 < mouseY < game.h//3 + 350 and   game.gamestate1=="menu" and game.gamestate2=="menu":
        game.gamestate1="instruction"
        game.gamestate2="instruction"
        # print(game.gamestate1,game.gamestate2)
    if game.w//2 < mouseX < game.w//2 + 200 and game.h//3+400 < mouseY < game.h//3 + 450 and   game.gamestate1=="instruction" and game.gamestate2=="instruction":
        game.gamestate1="menu"
        game.gamestate2="menu"
    if 500<mouseX<700 and 650<mouseY<700 and ((game.gamestate1=="over" and game.gamestate2=="over") or (game.gamestate1=="won" and game.gamestate2=="won") or (game.gamestate1=="over" and game.gamestate2=="won") or (game.gamestate1=="won" and game.gamestate2=="over")) : #NEW GAME, reinitialize everything to None or empty lists
        game.level=0
        game.gamestate1="menu"
        game.gamestate2="menu"
        game.level=0
        game.asteroids1=[]
        game.asteroids2=[]
        
        game.rockets=[]
        game.rockets2=[]
        game.fireballs1=[]
        game.fireballs2=[]
        game.dest1=None
        game.dest2=None
        game.coins1=[]
        game.coins2=[]
        
        game.time=60
        game.framerate=0
        game.time1=0
        
        game.coincount1=0
        game.coincount2=0
        
        game.numlives1=3
        game.numlives2=3
        game.y0=0
        game.y1=0
        #put aliens back at starting line
        game.alien.y = game.h-20
        game.alien.x = 300
        
        game.alien2.y = game.h-20
        game.alien2.x = 900
        # print(game.gamestate1, game.level)
        
    
        

    
     
         
