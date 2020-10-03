import pygame
import random
pygame.init()
win=pygame.display.set_mode((600,600))

pygame.display.set_caption("Space Invasion")

ship=pygame.image.load('ship.png')

bullet_image=pygame.image.load('laser.png')

bg=pygame.image.load('bg.jpg')
enemyship=pygame.image.load('espaceship2.png')
enemy_laser=pygame.image.load('enemylaser.png')
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

p_blast=pygame.image.load('p_explosion.png')

music=pygame.mixer.music.load("music.mp3")
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
        lives=font1.render('LIFE:',1,(255,0,0))
        win.blit(lives,(385,26))
        pygame.draw.rect(win,(255,0,0),(450,30,100,10))
        pygame.draw.rect(win,(0,128,0),(450,30,100-(10*(10-self.life)),10))
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
    def hit(self):
        win.blit(p_blast,(self.x-27,self.y-13))
        self.x=300
        self.y=300
        self.life-=1
        self.walkcount=0
        plexplo.play()
        font=pygame.font.SysFont('comicsans',100)
        text=font.render('YOU ARE HIT',1,(255,0,0))
        win.blit(text,(100,250))
        pygame.display.update()
        i=0
        while i<300:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()
        
        if self.life==0:
            font1=pygame.font.SysFont('comicsans',100)
            gameover=font1.render('GAME OVER',1,(255,0,0))
            win.blit(gameover,(100,390))
            #score=font1.render('SCORE: '+str(score),1,(255,0,0))
            
            #win.blit(score,(10,450))
            pygame.display.update()
            j=0
            while j<300:
                pygame.time.delay(10)
                j+=1
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        j=301
                        pygame.quit()
                pygame.quit()

        

def redraw():
    no=0
    win.blit(bg,(0,0))
    p1.draw(win)
    if no<3:
        
        e1.draw(win)
        no+=1

    font=pygame.font.SysFont('comicsans',30,True,True)
    text=font.render('SCORE: '+str(score),1,(255,0,0))
    
    win.blit(text,(450,5))

    for bullet in bullets:
        bullet.draw(win)
    
    for elaser in enbullet:
        elaser.draw(win)
    pygame.draw.rect(win,(0,255,0),(0,575,600,25))
    win.blit(enemyship,(0,0))
    
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
            self.y+=0.25
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
            self.y-=.25
        else:
            run=False
            self.visible=False
            
    
class enemylaser(object):
    def __init__(self,x,y,height,width):
        self.x=random.randint(10,550)
        self.y=0 
        self.height=height
        self.width=width
        self.visible=True
    def draw(self,win):
        self.move()
        if self.visible:
            win.blit(enemy_laser,(self.x,self.y))
    def move(self):
        if self.y<550:
            self.y+=2.5
        else:
            run=False
            self.visible=False
            
        


#MAIN LOOP

score=0
p1=player(300,525,50,48)
no=0

run=True
j=1
bullets=[]
enbullet=[]
shootloop=0
for images in alien:
        ranno=random.randint(1,500)
        e1=enemy(ranno,-20,64,64,800)
    

while run: 

    
    keys=pygame.key.get_pressed()
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run=False
    rand1=random.randint(1,50)
    rand2=random.randint(1,50)
    if(rand1==rand2):
      #  enemylaser(rand1,100,5,15)
        enbullet.append(enemylaser(rand1,100,5,15))
    if e1.visible==True:  
        for bullet in bullets:
            if bullet.y-bullet.height<e1.hitbox[1]+e1.hitbox[3] and bullet.y+bullet.height>e1.hitbox[1]:
                if bullet.x+bullet.width>e1.hitbox[0] and bullet.x-bullet.width<e1.hitbox[0]+e1.hitbox[2]:
                    e1.hit()
                    score+=1
                    bullets.pop(bullets.index(bullet))

                

            if bullet.y<600 and bullet.y>0:
                bullet.y-=2.5
            else:
                bullets.pop(bullets.index(bullet))


                    
    else:
        for bullet in bullets:
            if bullet.y<600 and bullet.y>0:
                bullet.y-=2.5
            else:
                bullets.pop(bullets.index(bullet))

    for elaser in enbullet:
        
        if elaser.y-elaser.height<p1.hitbox[1]+p1.hitbox[3] and elaser.y+elaser.height>p1.hitbox[1]:
                    if elaser.x+elaser.width>p1.hitbox[0] and elaser.x-elaser.width<p1.hitbox[0]+p1.hitbox[2]:
                        p1.hit()
                        score-=5
                        enbullet.pop(enbullet.index(elaser))
    for bullet in bullets:
        for elaser in enbullet:
            if elaser.y-elaser.height<bullet.y+bullet.height and elaser.y+elaser.height>bullet.y-bullet.height:
                if elaser.x-elaser.width<bullet.x+bullet.width and elaser.x+elaser.width>bullet.x-bullet.width:
                    bullets.pop(bullets.index(bullet))
                    enbullet.pop(enbullet.index(elaser))                

    if e1.visible==True:
        
        if p1.hitbox[1]<e1.hitbox[1]+e1.hitbox[3] and p1.hitbox[1]+p1.hitbox[3]>e1.hitbox[1]:
            if p1.hitbox[0]+p1.hitbox[2]>e1.hitbox[0] and p1.hitbox[0]<e1.hitbox[0]+e1.hitbox[2]:
                p1.hit()
                score-=5
            
    
    if shootloop>0:
        shootloop+=1
        
    if shootloop>9:
        shootloop=0
    
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
