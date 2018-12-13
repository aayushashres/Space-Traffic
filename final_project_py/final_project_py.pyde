import os, time

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
            
    def update(self):
        print("xyz")    
class Alien(Character):
    def __init__(self,x,y,r,img,w,h):
        Character.__init__(self,x,y,r,img,w,h)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False, DOWN:False}
    def update(self):
        if game.gamestate1=="play":
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
            if self.x+(self.r*2)>=game.w//2:
                self.x=(game.w//2)-(self.r*2)
                
            if self.y <= game.h // 2 and self.y > game.maxmid: #CHANGE 620 to endgame
                game.y0 += self.dy
                
            if self.y+(self.r*2)>=game.h:
                self.y=game.h - (self.r*2)
                
            if self.y<=game.maxy:
                self.y=game.maxy
            #COIN COLLECTION
            for x in game.coins1:
                if self.distance(x)<=self.r+x.r:
                    game.coins1.remove(x)
                    game.coincount1+=1
            # asteroid collision
            for x in game.asteroids1:
                if self.distance(x) <= self.r+ x.r :
                    game.numlives1-=1
                    # the delay function built in to processing will prevent one collision from counting as many and removing all three lives at one 
                    delay(200)
                    self.y=750
                    game.y0=0
                    print(game.numlives1)
                    if game.numlives1<=0:
                        game.gamestate1="over"
            # fireball collision        
            for x in game.fireballs1:
                 if self.distance(x) <= self.r+ x.r :
                    game.numlives1-=1
                    delay(200)
                    self.y=750
                    game.y0=0
                    print(game.numlives1)
                    if game.numlives1<=0:
                        game.gamestate1="over"
            # Rocket Part
            if self.y <= 350 and self.y >= 20: # if the alien is in the segment of the game that contains the rockets 
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
                        self.y=750
                        game.y0 = 0
                        print(game.numlives1)
                        if game.numlives1<=0:                               
                            game.gamestate1="over"
                    delay(200)
            # win check when destination is reached 
            if self.distance(game.dest1) <= (self.r + game.dest1.r):
                game.score1+= (game.numlives1*100) + (game.coincount1*10) +((60-game.time)*10) #score calculation
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

            if self.y <= game.h // 2 and self.y > game.maxmid: #CHANGE 620 to endgame
                game.y1 += self.dy
                
            if self.y+(self.r*2)>=game.h:
                self.y=game.h-(self.r*2)
                
            if self.y<=game.maxy:
                self.y=game.maxy
                
            
            
            # asteroid collision   
            for x in game.asteroids2:
                # print(self.distance(x))
                if self.distance(x) <= self.r+ x.r :
                    game.numlives2-=1
                    delay(200)
                    self.y=750
                    game.y1=0
                    print(game.numlives2)
                    if game.numlives2<=0:
                        game.gamestate2="over"
            # fireball collision
            for x in game.fireballs2: #WORK ON COLLISION FOR FIREBALL
                if self.distance(x) <= self.r+ x.r :
                    game.numlives2-=1
                    delay(200)
                    self.y=750
                    game.y1=0
                    print(game.numlives2)
                    if game.numlives1<=0:
                        game.gamestate2="over"
            # Rocket Part 
            if self.y <= 350 and self.y >= 20: # if the alien is in the segment of the game that contains the rockets 
                # part of the game is that you must move on the next row of rockets before they move off screen, so if you dont, you still lose a life and start over
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
                        self.y=750
                        game.y1 = 0 # change from alien 1 
                        print(game.numlives2)
                        if game.numlives2<=0:                               
                            game.gamestate2="over"
                    delay(200)
            # win check when destination is reached 
            if self.distance(game.dest2) <= (self.r + game.dest2.r):
                game.gamestate2 = "won"
    
                           
    
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
        self.x-=2
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
            image (self.img,self.x,self.y-game.y0) #errorhere
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
            # print("dest2: ",self.y)
        # print("planet y: ", self.y)
        

        
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
        if self.which_y==0:
            
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
        # self.start_x = s_x
        # self.end_x = e_x
        self.pause=False
        self.alien=Alien(self.w//4,self.h-20,20,"alien2.png",40,40)
        self.alien2=Alien2(self.w//2,self.h-20,20,"alien2.png",40,40)
        self.y0=0
        self.y1=0
        self.gamestate1="menu"
        self.gamestate2="menu"
        self.framerate=0
        self.time=0
        
        self.score1=0
        
        self.coincount1=0
        
        self.TESTLIST = [1,2,3,4,10]
        #initial num of lives is 3 for each player
        self.numlives1=3
        self.numlives2=3
        
        self.lives=loadImage(path+"/images/life.png")
        self.coin=loadImage(path+"/images/coin.png")
        
        
        # self.dest1=Destination1(self.w//4,-1000,30,"planet.png",60,60,0)
        # self.dest2=Destination1(self.w//2,-1000,30,"planet.png",60,60,1)
        
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
        self.coin2=[]
        
    def loadStage(self):
        print("Now loading stage")
        
        file=open(path+"/level"+str(self.level)+".csv","r")
        print(file)
        for l in file:
            l=l.strip().split(",")
            # print(l)
            if l[0] == "AsteroidP1": #P1 means player1, P2 is player2. adding asteroids to list
                cnt=0
                for i in range(2): #first layer of asteroids
                    self.asteroids1.append(Asteroid(cnt*int(l[1])+cnt*100,int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"asteroid.png",int(l[8]),int(l[9]),0)) #l[7] has some garbage????
                    cnt+=1
                cnt=0
                for i in range(3): #second layer of asteroids
                    self.asteroids1.append(Asteroid((cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-100,int(l[6]),"asteroid.png",int(l[8]),int(l[9]),0))
                    cnt+=1
                # print(self.asteroids1)
            if l[0]=="AsteroidP2":
                cnt=0
                for i in range(2):
                    self.asteroids2.append(Asteroid(625+(cnt*int(l[1])+cnt*100),int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"asteroid.png",int(l[8]),int(l[9]),1))
                    cnt+=1
                cnt=0
                for i in range(3):
                    self.asteroids2.append(Asteroid(625+(cnt*int(l[1])+cnt*50),int(l[2]),int(l[3]),int(l[4]),int(l[5])-100,int(l[6]),"asteroid.png",int(l[8]),int(l[9]),1))
                    cnt+=1
                # print(self.asteroids2)
                
                
            if l[0] == "AsteroidL2P1": #P1 means player1, only available for level2
                cnt=0
                for i in range(2): #first layer of asteroids
                    self.asteroids1.append(Asteroid(cnt*int(l[1])+cnt*100,int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6]),"asteroid.png",int(l[8]),int(l[9]),0)) 
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
                print (self.fireballs2)
                
            if l[0]=="Coin1":
                numcoins1=0 #to check number of coins in the level
                cointemp=None
                # for i in range(5):    
                while numcoins1 < int(l[1]):
                    # print("CHECK")
                    x=random(0,550)
                    y=random(maxy,700)
                    cointemp=(Coins(x,y,12,"coin.png",24,24,0)) #temp coin to add a coin to check if there is collision.
                    
                    
                    if not cointemp.coincollision():
                        self.coins1.append(cointemp)
                        numcoins1+=1
                
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
        
        
       # image(self.rocketbg1,0,20,self.w,350-y0,0,y0,self.w,330)
       # image(self.rocketbg1,0,350-self.y0,self.w,y0,0,20,self.w,y0)
       # image (self.rocketbg1,0,30,self.w,300-self.y0,0,y0,self.w,self.h)
        #image (self.rocketbg1,0,250-y0,self.w,y0,0,0,self.w,y0)
        
        image (self.bg2,self.w//2,0,self.w,self.h-y1,0,y1,self.w,self.h) 
        image (self.bg2,self.w//2,self.h-y1,self.w,y1,0,0,self.w,y1)
        # print (self.h-y)

        # image (self.bg,0,0,self.w,self.h)
        line(self.w//2,0,self.w//2,800)
        for x in self.asteroids1:
            #print("Displaying asteriods now")
            x.display()
        # self.dest.display()
        
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
        self.dest1.display()
        self.dest2.display()
        
        # Timer bar for game 1
        stroke(255)
        fill(255)
        text("TIME",50,40)      
        fill(0)
        rect(50,50,120,20)
        if self.gamestate1 == "play": # when the game is lost, the time will stop counting downwww
            self.time=(self.framerate//60)
            fill(255)
            rect(50,50,max(0,120-(self.time)),20) #TIME is exactly 60 sec right now, may change as per level by using game.time
        # textSize(30)
        text(self.time,160,20)
        
        # right now the word time turns black when the state in game one changes -- work on that 
        
        #time bar for game 2
        stroke(255)
        fill (255)
        text("TIME",self.w//2+50,40)        
        fill(0)
        rect((self.w//2)+50,50,120,20)
        if self.gamestate2 == "play": # when the game is lost, the time will stop counting down 
            self.time=(self.framerate//60)   
                   
            fill(255)
            rect((self.w//2)+50,50,max(0,120-(self.time)),20)

  
        
        #LIVES DISPLAY
        for i in range(self.numlives1):
            image(self.lives, 40 +(i*45),80)
        for i in range(self.numlives2):
            image(self.lives, 640+(i*45),80)
            
        for x in self.coins1:
            x.display()
            
        #COINS DISPLAY
    
        image(self.coin,550,75)
   
        textSize(20)
        fill(255)
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
    
            
        # self.dest1.update()
        # self.dest2.update()
            
            
        
game=Game(1200,800,level,maxy,maxmid,time)

def setup():
   size(game.w,game.h)
   # game.loadStage()
   
   
   
   # if game.gamestate1=="play" and game.gamestate2=="play":
   #     # print(game.gamestate1, game.gamestate2)
   #     game.loadStage()
        
   #game.loadStage()
   
def draw():
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
                # print("reached")
                image(game.bgmenu,0,0,1200,800)
                image(game.instr,game.w//5.5,game.h//5,800,400)
                
                if game.w//2 < mouseX < game.w//2 + 200 and game.h//3+400 < mouseY < game.h//3 + 450:
                    fill(0,255,0)
                else:
                    fill(255)
                text("Return",game.w//2,game.h//3+440) 
        
        elif game.gamestate1=="play" and game.gamestate2=="play":
            # print("states ok")
            game.display()
    
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
            text("Gameover",game.w//2,game.h//2)
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
        if game.gamestate1 == "won" and game.gamestate2 == "won":
            game.display()
            fill(0,255,0)
            textSize(50)
            text("Game Won!",0,game.h//2)
            text("Game Won!",game.w//2,game.h//2)
        if game.gamestate1=="won" and game.gamestate2=="over":
            game.display()
            fill(0,255,0)
            textSize(50)
            text("Game Won!",0,game.h//2)
            fill(255,0,0)
            text("Gameover",game.w//2,game.h//2)
        if game.gamestate2=="won" and game.gamestate1=="over":
            game.display()
            fill(255,0,0)
            textSize(50)
            text("Gameover",0,game.h//2)
            fill(0,255,0)
            text("Game Won!",game.w//2,game.h//2)
            
        
            
            

            
        
        

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
        game.maxy=-1500  #USING VAL FROM LEVEL 1 FOR NOW
        maxmid=-1050
        game.maxmid=-1050
        time=60
        game.time=60
        
        game.loadStage()
    
    if game.w//2.5 < mouseX < game.w//2.5 + 200 and game.h//3+200 < mouseY < game.h//3 + 250: 
        game.gamestate1="play" 
        game.gamestate2="play"
        level=3 #SETTING LEVEL
        game.level = level
        maxy=-2000
        game.maxy=-2000  #USING VAL FROM LEVEL 1 FOR NOW
        maxmid=-1050
        game.maxmid=-1050
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
        

    
     
         
