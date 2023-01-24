import pygame
import random

class ObJect:
    screen=None
    color=None
    pos=None
    direct=None
    def __init__(self,screen,color, pos):
        self.screen=screen
        self.color=color
        self.pos=pos
        rd=[-1,1]
        self.direct=[random.choices(rd)[0],random.choices(rd)[0]]

    def getPos(self):
        return self.pos

    def collision(self,orthor):
        this_pos=[[self.pos[0],self.pos[1]],[self.pos[0]+self.pos[2],self.pos[1]+self.pos[3]]]
        #               X1           Y1               X2                      Y2
        orthor_pos=[[orthor[0],orthor[1]],[orthor[0]+orthor[2],orthor[1]+orthor[3]]]
        
        if this_pos[1][1]>=orthor_pos[0][1] and this_pos[0][1]<=orthor_pos[1][1]:
            if this_pos[0][0]<=orthor_pos[1][0] and this_pos[1][0]>=orthor_pos[0][0]:
                if this_pos[0][0]>orthor_pos[0][0]:
                    return "left"
                elif this_pos[1][0]<orthor_pos[1][0]:
                    return "right"
        return "False"

    def show(self):
        pygame.draw.rect(self.screen,self.color, self.pos)

class player(ObJect):
    def move(self,pos):
        if 0<=self.pos[0]+pos[0]<=700:
            self.pos[0]+=pos[0]
        if 0<=self.pos[1]+pos[1]<=500:
            self.pos[1]+=pos[1]

class bot(ObJect):
    score=None
    def __init__(self, screen, color, pos):
        super().__init__(screen, color, pos)
        self.score=[0,0]
    def pongmove(self,speed,orthors):
        for orthor in orthors:
            match self.collision(orthor):
                case "left":
                    self.direct[0]=1
                case "right": 
                    self.direct[0]=-1
        if 0<=self.pos[0]+speed[0]*self.direct[0]<=670:
            self.pos[0]+=speed[0]*self.direct[0]
        else:
            if self.pos[0]<350:
                self.score[0]+=1
            else:
                self.score[1]+=1
            self.pos=[335,235, 30, 30]

        if 0<=self.pos[1]+speed[1]*self.direct[1]<=470:
            self.pos[1]+=speed[1]*self.direct[1]
        else:
            self.direct[1]*=-1  
    def get_score (self):
        return self.score         

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Bouncing Rectangle")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
w=[0,0]
v=[0,0]
# -------- Main Program Loop -----------
all=[]
for i in range(1):
    all.append(bot(screen, WHITE, [335,235, 30, 30]))
P=[player(screen, RED, [50,100, 10, 100]),player(screen, GREEN,[650,100, 10, 100])]

while not done:
    # --- Event Processing
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                v[1]=-5
            if event.key == pygame.K_DOWN:
                v[1]=5
            if event.key == pygame.K_w:
                w[1]=-5
            if event.key == pygame.K_s:
                w[1]=5
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP and v[1] == -5:
                v[1]=0
            if event.key == pygame.K_DOWN and v[1] == 5:
                v[1]=0
            if event.key == pygame.K_w and w[1] == -5:
                w[1]=0
            if event.key == pygame.K_s and w[1] == 5:
                w[1]=0
    

    # --- Drawing
    # Set the screen background
    screen.fill(BLACK)


    P[0].move(w)
    P[1].move(v)

    for i in all:
        i.pongmove([3,3],[P[0].getPos(),P[1].getPos()])
    # Draw the rectangle
    for i in all:
        i.show()

    for i in P:
        i.show()

    font = pygame.font.Font('freesansbold.ttf', 32)
    temp=all[0].get_score()
    text = font.render(str(temp[0])+" : "+str(temp[1]), False,WHITE)

    textscore = text.get_rect()
 
    textscore.center = (350, 100)

    screen.blit(text, textscore)
    
    
    # --- Wrap-up
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Close everything down
pygame.quit()