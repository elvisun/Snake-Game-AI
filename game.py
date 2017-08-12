# CNN Deep Reinforcement Learning Snake AI 
# By Elvis Sun

import numpy as np
import random, pygame, sys, operator, os, time, argparse
import keras.utils
from pygame.locals import *

FPS = 60

CELLWIDTH = 5
CELLHEIGHT = 5
CELLSIZE = 50
WINDOWWIDTH = CELLWIDTH * CELLSIZE
WINDOWHEIGHT = CELLHEIGHT * CELLSIZE
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."


#             R    G    B
WHITE     = (255, 255, 255)
GREY      = (200, 200, 200)
PINK      = (198, 134, 156)
BLACK     = ( 17,  18,  13)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
ORANGE    = (255, 155, 111)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'



HEAD = 0 # syntactic sugar: index of the worm's head

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    display = False
    if (len(sys.argv) > 1) and sys.argv[1] == '-d':
        display = True
    
    if display:
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Wormy')

    game = Game()
    while True: # main game loop
        game.move(RIGHT)
        if display:
            updateDisplay(game)
        if game.is_terminal():
            break
    print(game.get_score())
    


class Game():

    def render(self):
        global FPSCLOCK, DISPLAYSURF, BASICFONT
        if self.firstCall:
            self.firstCall = False
            pygame.init()
            FPSCLOCK = pygame.time.Clock()
            DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
            BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
            pygame.display.set_caption('CNN Snake')
        updateDisplay(self)

    def __init__(self):
        self.observation_space = np.zeros((CELLWIDTH + 2,CELLHEIGHT + 2))
        self.action_space = 4
        self.firstCall = True

    def __getattr__(self, name):
        if hasattr(self.st, name):
            return getattr(self.st, name)
        else:
            raise AttributeError

    def reset(self):
        self.head = {'x': 0, 'y': 0}
        self.gameOver = False
        self.direction = RIGHT
        self.score = 0
        startx = 0
        starty = 0 
        self.wormCoords = [{'x': startx + 3, 'y': starty},
                      {'x': startx + 2, 'y': starty},
                      {'x': startx + 1, 'y': starty},
                      ]
        self.apple = getRandomLocation(self.wormCoords)
        return self.get_state_map()


    def get_state(self):    
        return (self.wormCoords, self.apple)

    def move(self, action):
        action = num_to_action(action)
        assert not self.gameOver, "Game over!"
        appleReward = 50
        deathReward = -50
        moveReward = 10
        reward = 0
        apple = self.apple
        newHead = findNewHead(action, self.wormCoords)
        self.wormCoords.insert(0, newHead)
        if self.wormCoords[HEAD]['x'] == -1 or self.wormCoords[HEAD]['x'] == CELLWIDTH or self.wormCoords[HEAD]['y'] == -1 or self.wormCoords[HEAD]['y'] == CELLHEIGHT:
            self.gameOver = True
            reward = deathReward

        for wormBody in self.wormCoords[1:]:
            if wormBody['x'] == self.wormCoords[HEAD]['x'] and wormBody['y'] == self.wormCoords[HEAD]['y']:
                self.gameOver = True
                reward = deathReward
        
        #if didn't die, move snake
        if not self.gameOver:
            if self.wormCoords[HEAD]['x'] == apple['x'] and self.wormCoords[HEAD]['y'] == apple['y']:
                self.apple = getRandomLocation(self.wormCoords) # set a new apple somewhere
                reward = appleReward
            else:
                self.wormCoords.pop() # remove worm's tail segment
                reward = moveReward
        self.score = self.score + reward
        #print(reward,self.gameOver,self.score)
        return (self.get_state_map(),reward,self.gameOver,self.score)

    def is_terminal(self):
        return self.gameOver

    def get_score(self):
        return self.score

    def get_state_map(self):
        #return pygame.surfarray.array3d(pygame.display.get_surface())

        stateMap = [[0 for i in range(CELLWIDTH + 2)] for j in range(CELLHEIGHT + 2)]
        #label walls as 4
        for i, row in enumerate(stateMap):
          for j, cell in enumerate(row):
            if i==0 or i==(CELLWIDTH+1) or j==0 or j==(CELLHEIGHT+1):
              stateMap[i][j] = 1
        for i, cell in enumerate(self.wormCoords):
            #print(cell)  #this goes to 10
            #mark worm body as 1
            stateMap[cell['y'] + 1][cell['x'] + 1] = 2
            #mark head as 2
            if i == 0:
                stateMap[cell['y'] + 1][cell['x'] + 1] = 3
        #mark apple as 3
        stateMap[self.apple['y'] + 1][self.apple['x'] + 1] = 4
        
        categorical_2d_map = keras.utils.to_categorical(np.array(stateMap), num_classes = 5)
        categorical_2d_map_for_conv2D = np.array(stateMap).reshape(1,CELLWIDTH+2,CELLHEIGHT+2,1)
        
        #one_hot_3d_map = keras.utils.to_categorical(categorical_2d_map.reshape((CELLWIDTH + 2) * (CELLHEIGHT + 2)), num_classes = 5)
        #one_hot_4d_map = one_hot_3d_map.reshape(1,CELLWIDTH+2,CELLHEIGHT+2,5)
        #print(categorical_2d_map.shape)
        #print(categorical_2d_map)
        return categorical_2d_map
        # 
        # print("\n")        
        # print(categorical_2d_map.reshape(1,(CELLWIDTH + 2) * (CELLHEIGHT + 2)))
        # print("\n")  
        # print(one_hot_3d_map)
        # print("\n")
        # print(one_hot_4d_map)
        # print("\n")


def num_to_action(num):
    if num == 0:
        return UP
    elif num == 1:
        return DOWN
    elif num == 2:
        return LEFT
    elif num == 3:
        return RIGHT
    assert False, "Wrong action number"

def updateDisplay(game):
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                  terminate()
    DISPLAYSURF.fill(BGCOLOR)
    drawGrid()
    drawWorm(game.get_state()[0])
    drawApple(game.get_state()[1])
    drawScore(len(game.get_state()[0]) - 3)
    pygame.display.update()
    FPSCLOCK.tick(FPS)


def calcDistance(point, apple):
  distance = abs(point['x'] - apple['x']) + abs(point['y'] - apple['y'])
  return distance


def pauseGame():
  pauseGame = True
  while (pauseGame):
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_SPACE:
          pauseGame = False

def oppositeDirection(direction):
    if direction == UP:
        return DOWN
    elif direction == DOWN:
        return UP
    elif direction == LEFT:
        return RIGHT
    elif direction == RIGHT:
        return LEFT

def findNewHead(direction,wormCoords):
    newHead = {}
    if direction == UP:
        newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
    elif direction == DOWN:
        newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
    elif direction == LEFT:
        newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
    elif direction == RIGHT:
        newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
    return newHead

"""
////////////////////////////////////////////////////////////////////////////
"""


def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Wormy!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Wormy!', True, GREEN)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame


def terminate():
    print('YOU DIED!')
    pauseGame()
    pygame.quit()
    sys.exit()


def getRandomLocation(worm):
    location = {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}
    while(location in worm):
        location = {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}
    return location


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        #wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        #pygame.draw.rect(DISPLAYSURF, WHITE, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 1, y + 1, CELLSIZE - 2, CELLSIZE - 2)
        pygame.draw.rect(DISPLAYSURF, WHITE, wormInnerSegmentRect) 

def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)  


def drawGrid():
    return  #do nothing
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()


'''
                  {'x': startx + 3, 'y': starty},
                  {'x': startx + 2, 'y': starty},
                  {'x': startx + 1, 'y': starty},
                  {'x': startx, 'y': starty},
                  {'x': startx, 'y': starty + 1},
                  {'x': startx, 'y': starty + 2},
                  {'x': startx, 'y': starty + 3},
                  {'x': startx, 'y': starty + 4},
                  {'x': startx, 'y': starty + 5},
                  {'x': startx - 1, 'y': starty + 5},
                  {'x': startx - 2, 'y': starty + 5},
                  {'x': startx - 3, 'y': starty + 5},
                  {'x': startx - 4, 'y': starty + 5},
                  {'x': startx - 5, 'y': starty + 5},
                  {'x': startx - 5, 'y': starty + 6},
                  {'x': startx - 5, 'y': starty + 7},
                  {'x': startx - 5, 'y': starty + 8},
                  {'x': startx - 5, 'y': starty + 9},
                  {'x': startx - 5, 'y': starty + 10},
                  {'x': startx - 5, 'y': starty + 11},
                  {'x': startx - 5, 'y': starty + 12},
                  {'x': startx - 5, 'y': starty + 13},
                  {'x': startx - 5, 'y': starty + 14},
                  {'x': startx - 5, 'y': starty + 15},
                  {'x': startx - 5, 'y': starty + 16},
                  {'x': startx - 5, 'y': starty + 17},
                  {'x': startx - 5, 'y': starty + 18},
                  {'x': startx - 5, 'y': starty + 19},
                  {'x': startx - 5, 'y': starty + 20},
                  {'x': startx - 4, 'y': starty + 20},
                  {'x': startx - 3, 'y': starty + 20},
                  {'x': startx - 2, 'y': starty + 20},
                  {'x': startx - 1, 'y': starty + 20},
                  {'x': startx - 0, 'y': starty + 20},
                  {'x': startx + 1, 'y': starty + 20},
                  {'x': startx + 2, 'y': starty + 20},
                  {'x': startx + 3, 'y': starty + 20},
                  {'x': startx + 4, 'y': starty + 20},
                  {'x': startx + 5, 'y': starty + 20},
                  {'x': startx + 6, 'y': starty + 20},
                  {'x': startx + 7, 'y': starty + 20},
                  {'x': startx + 8, 'y': starty + 20},
                  {'x': startx + 9, 'y': starty + 20},
                  {'x': startx + 10, 'y': starty + 20},
                  {'x': startx + 11, 'y': starty + 20},
                  {'x': startx + 12, 'y': starty + 20},
                  {'x': startx + 13, 'y': starty + 20},
                  {'x': startx + 14, 'y': starty + 20},
                  {'x': startx + 15, 'y': starty + 20},
                  {'x': startx + 16, 'y': starty + 20},
                  {'x': startx + 17, 'y': starty + 20},
                  {'x': startx + 18, 'y': starty + 20},
                  {'x': startx + 19, 'y': starty + 20},
                  {'x': startx + 19, 'y': starty + 19},
                  {'x': startx + 18, 'y': starty + 19},
                  {'x': startx + 17, 'y': starty + 19},
                  {'x': startx + 16, 'y': starty + 19},
                  {'x': startx + 15, 'y': starty + 19},
                  {'x': startx + 14, 'y': starty + 19},
                  {'x': startx + 13, 'y': starty + 19},
                  {'x': startx + 12, 'y': starty + 19},
                  {'x': startx + 11, 'y': starty + 19},
                  {'x': startx + 10, 'y': starty + 19}, 
                  {'x': startx + 10, 'y': starty + 18},
                  {'x': startx + 11, 'y': starty + 18},
                  {'x': startx + 12, 'y': starty + 18},
                  {'x': startx + 13, 'y': starty + 18},
                  {'x': startx + 14, 'y': starty + 18},
                  {'x': startx + 15, 'y': starty + 18},
                  {'x': startx + 16, 'y': starty + 18},
                  {'x': startx + 17, 'y': starty + 18},
                  {'x': startx + 18, 'y': starty + 18},
                  {'x': startx + 19, 'y': starty + 18},
                  {'x': startx + 19, 'y': starty + 17},
                  {'x': startx + 18, 'y': starty + 17},
                  {'x': startx + 17, 'y': starty + 17},
                  {'x': startx + 16, 'y': starty + 17},
                  {'x': startx + 15, 'y': starty + 17},
                  {'x': startx + 14, 'y': starty + 17},
                  {'x': startx + 13, 'y': starty + 17},
                  {'x': startx + 12, 'y': starty + 17},
                  {'x': startx + 11, 'y': starty + 17},
                  {'x': startx + 10, 'y': starty + 17}
'''