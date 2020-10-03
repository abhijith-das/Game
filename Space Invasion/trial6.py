import pygame
import random
import time
pygame.init()
win=pygame.display.set_mode((600,600))

pygame.display.set_caption("Space Invasion")

ship=pygame.image.load('ship.png')

bullet_image=pygame.image.load('laser.png')
enemy1=pygame.image.load('enemy2.png')
bg=pygame.image.load('bg.jpg')
enemyship=pygame.image.load('enemyship1.png')
enemy_laser=pygame.image.load('enemylaser.png')
main_enemy=pygame.image.load('main.png')
clock=pygame.time.Clock()

alien=[]
i=1
for i in range(1,5):
    alien.append(pygame.image.load('mystery1.png'))

    
def aliendraw(x,y,j):

    win.blit(alien[j],(x,y))



plexplo=pygame.mixer.Sound('player_explosion.wav')

enexplo=pygame.mixer.Sound('enemy_explosion.wav')

shoot=pygame.mixer.Sound('shoot.wav')

e_blast=pygame.image.load('e_explosion.png')

f_blast=pygame.image.load('final_explosion.png')

p_blast=pygame.image.load('p_explosion.png')

redbullet=pygame.image.load('finallaser.png')

shipblast=pygame.mixer.music.load('dilwale.wav')

music=pygame.mixer.music.load("music.mp3")
musicloop=True
if musicloop==True:
    pygame.mixer.music.play(-1)


class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=1
        self.life=10
        self.standing=True
        self.walkcount=0
        self.hitbox=(self.x,self.y,50,50)


    def draw(self,win):
        if self.walkcount+1>=27:
            self.walkcount=0
        if not(self.standing):
            self.walkcount=0
            win.blit(ship,(self.x,self.y))
        else:
            win.blit(ship,(self.x,self.y))
        
        
        self.hitbox=(self.x,self.y,50,50)
        font1=pygame.font.SysFont('comicsans',27,False,True)
        lives=font1.render('LIFE:',1,(255,255,255))
        win.blit(lives,(385,26))
        pygame.draw.rect(win,(255,0,0),(450,30,100,10))
        pygame.draw.rect(win,(0,128,0),(450,30,100-(10*(10-self.life)),10))
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

        
    def hit(self):
        #redraw()
        #self.x=x
        #self.y=y
        win.blit(p_blast,(self.x-27,self.y-13))
        #self.x=x
        #self.y=y
        self.life-=1
        self.walkcount=0
        plexplo.play()
        font=pygame.font.SysFont('comicsans',100)
        text=font.render('YOU ARE HIT',1,(255,0,0))
        win.blit(text,(100,250))
        pygame.display.update()
        i=0
       # while i<300:
           # pygame.time.delay(10)
           # i+=1
           # for event in pygame.event.get():
            #    if event.type==pygame.QUIT:
             #       i=301
              #      pygame.quit()
        
        if self.life==0:
            musicloop=False
            music=pygame.mixer.music.load('dilwale.wav')
            pygame.mixer.music.play(-1)
            
            font1=pygame.font.SysFont('comicsans',100)
            gameover=font1.render('GAME OVER',1,(255,255,255))
            win.blit(gameover,(100,300))
            #score=font1.render('SCORE: '+str(score),1,(255,0,0))
            
            #win.blit(score,(10,450))
            pygame.display.update()
            j=0
            while j<900:
                pygame.time.delay(9000)
                j+=1
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        j=901
                        pygame.quit()
                pygame.quit()
            pygame.quit()




        

def redraw():
    no=0
    win.blit(bg,(0,0))

    p1.draw(win)
    
    if no<3:
        
        e1.draw(win)
        no+=1

    
    
    

    for bullet in bullets:
        bullet.draw(win)
    
    for elaser in enbullet:
        elaser.draw(win)

    for enemy2 in enemy_2:
        enemy2.draw(win)

    for x in red:
        x.draw(win)
    
    #win.blit(enemyship,(0,0))
    if entryvariable==1:
        ramanan.draw(win)

    for y in r_laser:
        y.draw(win)
    pygame.draw.rect(win,(0,255,0),(0,575,600,25))
    font=pygame.font.SysFont('comicsans',30,True,True)
    text=font.render('SCORE: '+str(score),1,(255,255,255))
    win.blit(text,(450,5))

    
    
    pygame.display.update()

class enemy(object):
    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=2
        self.end=end
        self.path=[self.end,self.y]
        self.hitbox=(self.x,self.y,210,100)
        self.health=10
        self.visible=True
        self.walkcount=0
    def draw(self,win):
        self.move()
        
        if self.visible:
            win.blit(alien[0],(self.x,self.y))
            if self.walkcount+1>=27:
                self.walkcount=0
            self.hitbox=(self.x,self.y,50,50)
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
            pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,50-(5*(10-self.health)),10))

        else:    
            win.blit(e_blast,(self.x,self.y))
            self.visible=False
            
            
            
    def move(self):
        if self.y<600:
            self.y+=0.5
        else:
            self.visible=False

    def hit(self):
        if self.health>0:
            self.health-=1
        else:
            self.visible=False
            enexplo.play()
            run=False

            
            
            
            

                


class laser(object):
    def __init__(self,x,y,height,width):
        self.x=x
        self.y=y  
        self.height=height
        self.width=width
        self.visible=True
    def draw(self,win):
        self.move()
        if self.visible:
            win.blit(bullet_image,(self.x,self.y))
    def move(self):
        if self.y>0:
            self.y-=2
        else:
            run=False
            self.visible=False
            
    
class enemylaser(object):
    def __init__(self,x,y,height,width,vel):
        self.x=random.randint(10,550)
        
        self.height=height
        self.y=0+self.height
        self.width=width
        self.vel=vel
        self.visible=True
    def draw(self,win):
        self.move()
        if self.visible:
            win.blit(enemy_laser,(self.x,self.y))
    def move(self):
        if self.y<600:
            self.y+=vel
        else:
            run=False
            self.visible=False

class ramanan_laser(object):
    def __init__(self,x,y,height,width,vel):
        self.x=x
        self.height=height
        self.y=y
        self.width=width
        self.vel=vel
        self.visible=True
    def draw(self,win):
        self.move()
        if self.visible:
            win.blit(redbullet,(self.x,self.y))
    def move(self):
        if self.y<600:
            self.y+=vel
        else:
            run=False
            self.visible=False


class more_enemies(object):
    def __init__(self,x,y,height,width):
        self.x=random.randint(10,550)
        
        self.height=height
        self.y=0-self.height
        self.width=width
        self.hitbox=(self.x,self.y,210,100)
        self.visible=True
    def draw(self,win):
        self.move()
        
        if self.visible:
            self.hitbox=(self.x,self.y,50,40)
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
            win.blit(enemy1,(self.x,self.y))
        else:
            win.blit(e_blast,(self.x,self.y))
            
    def move(self):
        if self.y<650:
            self.y+=1.5
        else:
            run=False
            self.visible=False


class red_enemy(object):
    def __init__(self,x,y,height,width):
                                                                                 
        self.height=height
        self.y=150
        self.width=width
        self.x=0-self.width
        self.hitbox=(self.x,self.y,101,45)
        self.visible=True
    def draw(self,win):
        self.move()
                    
        if self.visible:
            self.hitbox=(self.x,self.y,100,50)
            win.blit(enemyship,(self.x,self.y))
            #pygame.draw.rect(win,(255,255,255),self.hitbox,2)
        else:
            pass
          #  win.blit(e_blast,(self.x,self.y))
            
    def move(self):
        if self.x<650:
            self.x+=1
        else:
            run=False
            self.visible=False
        
                
class final_enemy(object):
    def __init__(self,x,y,width,height):

        self.width=width
        self.height=height
        self.x=0-self.width
        self.y=20#-self.height
        self.vel=1
        #self.end=end
        #self.path=[self.end,self.y]
        self.dir=1
        self.hitbox=(self.x,self.y,210,100)
        self.health=20
        self.visible=True
        self.walkcount=0
    def draw(self,win):
        self.move()
        
        if self.visible:
            win.blit(main_enemy,(self.x,self.y))
            if self.walkcount+1>=27:
                self.walkcount=0
            self.hitbox=(self.x,self.y,100,100)
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,100,10))
            pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,50-(5*(10-self.health)),10))
            #randc=random.randint(1,50)
            #randd=random.randint(1,50)
            #if randc==randd:
                #pass
            
               # finalbullet.append()
        else:    
            win.blit(f_blast,(self.x,self.y))
            self.visible=False
            victory()
            
            
            
    def move(self):
        if self.dir==1:
            if self.x<500:
                self.x+=self.vel
            else:
                self.y+=20
                self.dir=-1
        elif self.dir==-1:
            if self.x>0:
                self.x-=self.vel
            else:
                self.y+=20
                self.dir=1
        
        #else:
        #    self.visible=False

    def hit(self):
        if self.health>0:
            self.health-=1
        else:
            self.visible=False
            enexplo.play()
            run=False

     # def bullet(self)

     
def game_over():
    
    
    musicloop=False
    music=pygame.mixer.music.load('dilwale.wav')
    pygame.mixer.music.play(-1)
            
    font1=pygame.font.SysFont('comicsans',100)
    gameover=font1.render('GAME OVER',1,(255,255,255))
    win.blit(gameover,(100,300))
            #score=font1.render('SCORE: '+str(score),1,(255,0,0))
            
            #win.blit(score,(10,450))
    pygame.display.update()
    j=0
    while j<900:
        pygame.time.delay(9000)
        j+=1
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                j=901
                pygame.quit()
            pygame.quit()
    pygame.quit()



def victory():
    musicloop=False
    music=pygame.mixer.music.load('cradles.mp3')
    pygame.mixer.music.play(-1)
            
    font1=pygame.font.SysFont('comicsans',100)
    victory=font1.render('VICTORY',1,(255,255,255))
    win.blit(victory,(150,275))
            #score=font1.render('SCORE: '+str(score),1,(255,0,0))
            
            #win.blit(score,(10,450))
    pygame.display.update()
    j=0
    while j<900:
        pygame.time.delay(9000)
        j+=1
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                j=901
                pygame.quit()
            pygame.quit()
    pygame.quit()
    
    

#MAIN LOOP
finalbullet=[]
score=0
p1=player(300,525,50,48)
no=0
run=True
j=1
ramanan=final_enemy(0,0,100,100)
r_laser=[]
bullets=[]
enbullet=[]
enemy_2=[]
red=[]
entryvariable=0
shootloop=0
shootenemy=0
redloop=0
ramananloop=0
final_entry=0
for images in alien:
        ranno=random.randint(1,500)
        e1=enemy(ranno,-20,64,64,800)
    

while run: 

    
    keys=pygame.key.get_pressed()
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run=False

    if final_entry==31:
        entryvariable=1
        #ramanan=final_enemy(0,0,100,100)
        
    randc=random.randint(1,50)
    randd=random.randint(1,50)

    
    if randc==randd and entryvariable==1:
        if ramanan.visible==True and ramananloop==0:
            r_laser.append(ramanan_laser(ramanan.x+50,ramanan.y+100,5,15,2))
         #   pass
        #    enbullet.append(enemylaser(ramanan.x,ramanan.y,5,15,2.5))
        #for elaser in enbullet:
         #   if elaser.y<600 and elaser.y>0:
          #      if elaser.y<p1.hitbox[1]+p1.hitbox[3] and elaser.y>p1.hitbox[1]:
           #                 if elaser.x+elaser.width>p1.hitbox[0] and elaser.x-elaser.width<p1.hitbox[0]+p1.hitbox[3]:
    
                                # p1explo.play()
     #                           p1.hit()
      #                          score-=5
       #                         enbullet.pop(enbullet.index(elaser))


    if ramanan.y+ramanan.height>=550:
        gameover()


    for bullet in bullets:
        if bullet.y-bullet.height<ramanan.hitbox[1]+ramanan.hitbox[3] and bullet.y+bullet.height>ramanan.hitbox[1]:
            
            if bullet.x+bullet.width>ramanan.hitbox[0] and bullet.x-bullet.width<ramanan.hitbox[0]+ramanan.hitbox[2]:
                ramanan.hit()
                score+=1
                bullets.pop(bullets.index(bullet))
               # final_entry+=1


    if p1.hitbox[1]<ramanan.hitbox[1]+ramanan.hitbox[3] and p1.hitbox[1]+p1.hitbox[3]>ramanan.hitbox[1]:
        if p1.hitbox[0]+p1.hitbox[2]>ramanan.hitbox[0] and p1.hitbox[0]<ramanan.hitbox[0]+ramanan.hitbox[2]:
            #p1.life=0
            #p1.hit()
            game_over()

            
    for relaser in r_laser:
        if relaser.y<600 and relaser.y>0:
            if relaser.y<p1.hitbox[1]+p1.hitbox[3] and relaser.y>p1.hitbox[1]:
                        if relaser.x+relaser.width>p1.hitbox[0] and relaser.x-relaser.width<p1.hitbox[0]+p1.hitbox[3]:
                            p1.hit()
                            score-=5
                            r_laser.pop(r_laser.index(relaser))

    for bullet in bullets:
        for relaser in r_laser:
            if relaser.y-relaser.height<bullet.y+bullet.height and relaser.y+relaser.height>bullet.y-bullet.height:
                if relaser.x-relaser.width<bullet.x+bullet.width and relaser.x+relaser.width>bullet.x-bullet.width:
                    bullets.pop(bullets.index(bullet))
                    r_laser.pop(r_laser.index(relaser))


        
    rand1=random.randint(1,50)
    rand2=random.randint(1,50)

    
    if(rand1==rand2):
        #enemylaser(rand1,100,5,15)
        enbullet.append(enemylaser(rand1,100,5,15,2.5))
    if e1.visible==True:

        
        for bullet in bullets:
            if bullet.y-bullet.height<e1.hitbox[1]+e1.hitbox[3] and bullet.y+bullet.height>e1.hitbox[1]:
                if bullet.x+bullet.width>e1.hitbox[0] and bullet.x-bullet.width<e1.hitbox[0]+e1.hitbox[2]:
                    e1.hit()
                    score+=1
                    bullets.pop(bullets.index(bullet))
                    final_entry+=1

                

            if bullet.y<600 and bullet.y>0:
                bullet.y-=2.5

                
            else:
                bullets.pop(bullets.index(bullet))
        if p1.hitbox[1]<e1.hitbox[1]+e1.hitbox[3] and p1.hitbox[1]+p1.hitbox[3]>e1.hitbox[1]:
            if p1.hitbox[0]+p1.hitbox[2]>e1.hitbox[0] and p1.hitbox[0]<e1.hitbox[0]+e1.hitbox[2]:
                p1.hit()
                score-=5

                  
    else:
        for bullet in bullets:
            if bullet.y<600 and bullet.y>0:
                bullet.y-=2.5
            else:
                bullets.pop(bullets.index(bullet))
       # if p1.y<=100:
        #    p1.round2()
        rand5=random.randint(1,5)
        rand6=random.randint(1,5)

    #if e1.visible==False and p1.y<100:
       # p1.round2()
        rand7=random.randint(1,100)
        rand8=random.randint(1,100)


        if(rand7==rand8) and shootenemy==0:
            enemy_2.append(more_enemies(rand7,100,50,36))
            shootenemy=0
        for more in enemy_2:
            if more.y<570 and more.y>0:
                if p1.hitbox[1]<more.hitbox[1]+more.hitbox[3] and p1.hitbox[1]+p1.hitbox[3]>more.hitbox[1]:
                    if p1.hitbox[0]+p1.hitbox[2]>more.hitbox[0] and p1.hitbox[0]<more.hitbox[0]+more.hitbox[2]:

                                #p1explo.play
                                p1.hit()
                                score-=5
                                enemy_2.pop(enemy_2.index(more))

        for bullet in bullets:
            for more in enemy_2:
                if bullet.y-bullet.height<more.hitbox[1]+more.hitbox[3] and bullet.y+bullet.height>more.hitbox[1]:
                    if bullet.x+bullet.width>more.hitbox[0] and bullet.x-bullet.width<more.hitbox[0]+more.hitbox[2]:
                       # more.visible=False
                        enexplo.play()
                        bullets.pop(bullets.index(bullet))
                        enemy_2.pop(enemy_2.index(more))
                        
                        score+=1
                        final_entry+=1

                #if more.y>570:
                    #p1.hit()
                    #score-=5
                    #pygame.display.update()
        


        
           # pass
    for elaser in enbullet:
        if elaser.y<600 and elaser.y>0:
            if elaser.y<p1.hitbox[1]+p1.hitbox[3] and elaser.y>p1.hitbox[1]:
                        if elaser.x+elaser.width>p1.hitbox[0] and elaser.x-elaser.width<p1.hitbox[0]+p1.hitbox[3]:

                           # p1explo.play()
                            p1.hit()
                            score-=5
                            enbullet.pop(enbullet.index(elaser))
        
    
        
            #enbullet.pop(enbullet.index(elaser))
    for bullet in bullets:
        for elaser in enbullet:
            if elaser.y-elaser.height<bullet.y+bullet.height and elaser.y+elaser.height>bullet.y-bullet.height:
                if elaser.x-elaser.width<bullet.x+bullet.width and elaser.x+elaser.width>bullet.x-bullet.width:
                    bullets.pop(bullets.index(bullet))
                    enbullet.pop(enbullet.index(elaser))                
                    

                    


              #  enbullet.append(enemylaser(rand1,100,5,15,5))
            
      #  pass
    
    if shootloop>0:
        shootloop+=1
        
    if shootloop>9:
         shootloop=0

    if shootenemy>0:
        shootenemy+=1
        
    if shootenemy>3:
        shootenemy=0

        
    if redloop==0:
        redloop+=1
        
    if redloop>5:
        redloop=0

    if ramananloop>0:
        ramananloop+=1
        
    if ramananloop>9:
        ramananloop=0

    redloop+=1
    randa=random.randint(1,100)
    randb=random.randint(1,100)
    
    if(randa==randb) and redloop==2:
        red.append(red_enemy(0,200,100,44))
        redloop+=1


    for redship in red:
        if redship.x<600 and redship.x>0:
            if p1.hitbox[1]<redship.hitbox[1]+redship.hitbox[3] and p1.hitbox[1]+p1.hitbox[3]>redship.hitbox[1]:
                if p1.hitbox[0]+p1.hitbox[2]>redship.hitbox[0] and p1.hitbox[0]<redship.hitbox[0]+redship.hitbox[2]:
                            #p1explo.play()    
                            p1.hit()
                            score-=5
                            red.pop(red.index(redship))




    for bullet in bullets:

        for redship in red:
            if bullet.y-bullet.height<redship.hitbox[1]+redship.hitbox[3] and bullet.y+bullet.height>redship.hitbox[1]:
                if bullet.x+bullet.width>redship.hitbox[0] and bullet.x-bullet.width<redship.hitbox[0]+redship.hitbox[2]:
                    score+=5
                    final_entry+=1
                    enexplo.play()
                    bullets.pop(bullets.index(bullet))
                    red.pop(red.index(redship))                
    
    
    vel=2.5
    
    if keys[pygame.K_LEFT] and p1.x>0:
        p1.x-=vel
    if keys[pygame.K_RIGHT] and p1.x<600-p1.width:
        p1.x+=vel
    if keys[pygame.K_UP] and p1.y>0:
        p1.y-=vel
    if keys[pygame.K_DOWN] and p1.y<600-p1.height:
        p1.y+=vel
    if keys[pygame.K_SPACE] and shootloop==0:
        if len(bullets)<10:
            shoot.play()
            bullets.append(laser(round(p1.x+p1.width//2),round(p1.y+p1.height//2),5,15))
        #    enbullet.append(enemylaser(rand1,100,5,15))

        shootloop=1
        

    if e1.y>575 and e1.visible==True:
        p1.hit()
        score-=5
        e1.visible=False

                            
    redraw()
