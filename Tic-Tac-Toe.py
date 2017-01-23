#Tic-Tac-Toe.py

from random import *
from pygame import *
from math import*


init()
timesFontSm = font.SysFont("Times New Roman",20)
timesFont = font.SysFont("Times New Roman",30)

gameBackground = image.load("Images/game-background.png")
xPic = image.load("Images/x-button.png")
oPic = image.load("Images/o-button.png")
xIcon = image.load("Images/x-icon.png")
oIcon = image.load("Images/o-icon.png")
noSolution = image.load("Images/no-solution.png")
playAgain = image.load("Images/play-again.png")
yesPic = image.load("Images/yes-button.png")


class Player:
    def __init__ (self,name,score,symbol,symPic,value,icon):
        self.name=name
        self.score=score
        self.symbol=symbol
        self.symPic=symPic
        self.value=value
        self.icon=icon
    def win(self):
        self.score=self.score+1
        

class Button:
    def __init__(self,name,x,y,width,height,nextPage,pic):
        self.name=name
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.nextPage=nextPage
        self.pic=pic
        self.rect=Rect(x,y,width,height)
    def select(self):
        highlight((self.width,self.height),(self.x,self.y))


gridButtons=[Button("0",180,100,125,105,None,None),
             Button("1",330,100,130,105,None,None),
             Button("2",485,100,115,105,None,None),
             Button("3",180,230,125,130,None,None),
             Button("4",330,230,130,130,None,None),
             Button("5",485,230,115,130,None,None),
             Button("6",180,385,125,120,None,None),
             Button("7",330,385,130,120,None,None),
             Button("8",485,385,115,120,None,None),]
                    
yesButton=Button("yes",325,310,150,30,"game",yesPic)

player1 = Player("player 1",0,"X",xPic,1,xIcon)
player2 = Player("player 2",0,"O",oPic,-1,oIcon)



screen=display.set_mode((800,600))
display.set_caption("Tic-Tac-Toe")
page = "game"
currentP=player1

def highlight(size, pos):
    s = Surface(size)
    s.set_alpha(100)
    s.fill((0,0,0))
    screen.blit(s,pos)

def changePlayer():
    global currentP
    if currentP==player1:
        currentP=player2
    else:
        currentP=player1

def game():
    global page
    global currentP
    clicked=False
    # 1 is player1
    # -1 is player2
    grid=[0,0,0,0,0,0,0,0,0]
    winning=False

    running=True
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                page="exit"
                running=False
        
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        #Displays everything
        screen.blit(gameBackground,(0,0))
        player1Text = timesFontSm.render(player1.name, True, (0,0,0))
        player2Text = timesFontSm.render(player2.name, True, (0,0,0))
        player1Score = timesFont.render(str(player1.score), True, (0,0,0))
        player2Score = timesFont.render(str(player2.score), True, (0,0,0))
        screen.blit(player1Text, (10,10))
        screen.blit(player2Text, ((800-(len(player2.name)*11)),10))
        screen.blit(player1.icon,(15,40))
        screen.blit(player2.icon,(735,40))
        screen.blit(player1Score,(25,90))
        screen.blit(player2Score,(755,90))       
        for i in range(9):
            button=gridButtons[i]
            if grid[i]==player1.value:
                screen.blit(player1.symPic,(button.x,button.y))
            elif grid[i]==player2.value:
                screen.blit(player2.symPic,(button.x,button.y))
        screen.blit(currentP.icon,(mx-25,my-25))

        display.flip()
                
        #Checks for winning and tie cases
        for n in range(3):
            rowPoints = grid[n*3]+grid[n*3+1]+grid[n*3+2]
            colPoints = grid[n]+grid[n+3]+grid[n+6]
            if abs(rowPoints)==3:
                winning=rowPoints
            elif abs(colPoints)==3:
                winning=colPoints
        diag1 = grid[0]+grid[4]+grid[8]
        if abs(diag1)==3:
            winning=diag1
        diag2 = grid[2]+grid[4]+grid[6]
        if abs(diag2)==3:
            winning=diag2
        if winning>0:
            player1.win()
            won(grid)
            running=False
        elif winning<0:
            player2.win()
            won(grid)
            running=False

        if running:
            for i in range(9):
                if grid[i]==0:
                    break
                elif i==8:
                    tie()
                    running=False

        for i in range(9):
            button=gridButtons[i]
            if button.rect.collidepoint((mx,my)):
                if mb[0]==1 and grid[i]==0:
                    grid[i]=currentP.value
                    clicked=True
        if clicked:
            clicked=False
            changePlayer()



def won(grid):
    global page
    changePlayer()
    screen.blit(gameBackground,(0,0))
    player1Text = timesFontSm.render(player1.name, True, (0,0,0))
    player2Text = timesFontSm.render(player2.name, True, (0,0,0))
    player1Score = timesFont.render(str(player1.score), True, (0,0,0))
    player2Score = timesFont.render(str(player2.score), True, (0,0,0))
    screen.blit(player1Text, (10,10))
    screen.blit(player2Text, ((800-(len(player2.name)*11)),10))
    screen.blit(player1.icon,(15,40))
    screen.blit(player2.icon,(735,40))
    screen.blit(player1Score,(25,90))
    screen.blit(player2Score,(755,90))       
    for i in range(9):
        button=gridButtons[i]
        if grid[i]==player1.value:
            screen.blit(player1.symPic,(button.x,button.y))
        elif grid[i]==player2.value:
            screen.blit(player2.symPic,(button.x,button.y))
    highlight((800,600),(0,0))
    running=True
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                page="exit"
                running=False
        
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        screen.blit(playAgain,(250,225))
        screen.blit(yesButton.pic,(yesButton.x,yesButton.y))

        if yesButton.rect.collidepoint((mx,my)):
            yesButton.select()           
            if mb[0]==1:
                page=yesButton.nextPage
                time.wait(200)
                running=False

        display.flip()

def tie():
    global page
    changePlayer()
    highlight((800,600),(0,0))
    running=True
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                page="exit"
                running=False
        
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        screen.blit(noSolution,(250,225))
        screen.blit(yesButton.pic,(yesButton.x,yesButton.y))

        if yesButton.rect.collidepoint((mx,my)):
            yesButton.select()           
            if mb[0]==1:
                page=yesButton.nextPage
                time.wait(200)
                running=False

        display.flip()

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    if page=="exit":
        break
    elif page=="game":
        game()


quit()
