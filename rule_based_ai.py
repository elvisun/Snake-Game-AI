# Wormy 
# By Elvis Sun
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

import random, pygame, sys, operator, os, time
from pygame.locals import *

FPS = 60
WINDOWWIDTH = 1700
WINDOWHEIGHT = 1000
CELLSIZE = 50
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

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
    global wallCoords,softWallCoords
    wallCoords = []
    softWallCoords = []
    softWallCoords = findSoftWall()
    wallCoords = findWall()
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')

    # OUTPUT PRINT TO FILE
    #os.remove("test.txt")
    #sys.stdout=open("test.txt","w")

    while True:
        runGame()
        showGameOverScreen()


def runGame():
    global stalling
    stalling = False
    stallingCount = -1
    # Set a random start point.
    #startx = random.randint(5, CELLWIDTH - 6)
    #starty = random.randint(5, CELLHEIGHT - 6)
    startx = 5
    starty = 0 
    wormCoords = [{'x': startx + 6, 'y': starty},
                  {'x': startx + 5, 'y': starty},
                  {'x': startx + 4, 'y': starty},
                  ]
                  
    direction = RIGHT
    directionList = [RIGHT]
    PATH = []

    # Start the apple in a random place.
    #apple = getRandomLocation(wormCoords)
    apple = {'x': startx+8,     'y': starty}
    #apple = {'x': startx-1,     'y': starty-1}
    lastApple = {'x':startx-1,   'y': starty -1}
    PATH = calculatePath(wormCoords,apple,True)
    directionList = calcDirection(PATH)
    lastWall = 0

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                      terminate()
        # check if the worm has hit itself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            terminate()
            return # game over
        
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                terminate()
                return # game over
        # check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worm's tail segment
            lastApple = apple
            apple = getRandomLocation(wormCoords) # set a new apple somewhere
            drawApple(apple,lastApple)                        #for testing purposes
            #drawApple(lastApple)
            #sectionBreak() #just print some crap
            PATH = calculatePath(wormCoords,apple,True) #calculate path to go 
            if not PATH:
              stalling = True
              stallingCount = 10000
            elif PATH == 'stall':
              stalling = True
              stallingCount = int(len(wormCoords)/2)
            else:
              directionList = calcDirection(PATH)
        else:
            del wormCoords[-1] # remove worm's tail segment


        lastDirection = direction

        '''finding next direction'''
        #if stalling and len(directionList) == 1 and wormCoords[0] in softWallCoords:
          #print('special case')
          #directionList.extend(findBetterDirection(wormCoords,direction,0))
        if stalling and not directionList:
          onlyDirection = calcOnlyDirection(wormCoords)
          if onlyDirection and onlyDirection == lastDirection:
            directionList.append(onlyDirection)
            print('only direction:', direction)
          else:
            if safeToGo(wormCoords,direction,lastWall):       
              #print('safe')
              directionList.append(direction)      #continue the previous direction
            elif (not findNewHead(direction,wormCoords) in wormCoords) or (findNewHead(direction,wormCoords) in wallCoords):
              directionList.append(direction)
            else:
              lastDirection = direction
              #check if path can be found, if yes override previous calcualtion 
              PATH = calculatePath(wormCoords,apple,False)
              if PATH != [] and PATH != 'stall':
                stalling = False
                stallingCount = -1
                directionList = calcDirection(PATH)
              else:
                if checkLastWall(wormCoords):
                  lastWall = checkLastWall(wormCoords)
                directionList.extend(findBetterDirection(wormCoords,direction,lastWall))
                if calcArea(findNewHead(directionList[0],wormCoords), wormCoords, lastWall)<3:
                  directionList = [lastDirection]
                #print(directionList)
            stallingCount = stallingCount - 1
            #print ('stalling Count:', stallingCount)
            if stallingCount < 1:
              #print('stalling Count',stallingCount)
              stalling = False
              prevLastWall = lastWall
              lastWall = 0
              directionList.append(lastDirection)
              PATH = calculatePath(wormCoords,apple,True) #calculate path to go 
              if not PATH:
                stalling = True
                stallingCount = 10000
                lastWall = prevLastWall
              elif PATH == 'stall':
                stalling = True
                stallingCount = int(len(wormCoords)/2)
                lastWall = prevLastWall
              else:
                directionList = calcDirection(PATH)
        nextHead = findNewHead(directionList[0],wormCoords)
        '''
        if nextHead in wormCoords or nextHead in wallCoords or nextHead in getNextWallCoords(lastWall):  #if gonig to die go into tunnel
          lastWall = 0
          directionList = findNextDirection(wormCoords, directionList[0],0)
          print('going into tunnel')
        '''
        if stalling:
          if AreaIsTooSmall(CELLWIDTH,nextHead, wormCoords, lastWall):      #return true if the area going in is too small
            lastWall = 0
            directionList = findNextDirection(wormCoords, directionList[0],0)
            print('almost died, recalcualting...',wormCoords[0],directionList)          
        

        direction = directionList.pop(0)
        newHead = findNewHead(direction, wormCoords)
        wormCoords.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple,lastApple)
        drawScore(len(wormCoords) - 3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def calcOnlyDirection(worm):
    count = 4 
    ways = getNeighborhood(worm[0])
    theWay = 0
    for each in ways:
      if each in worm:
        count = count - 1
      else:
        theWay = each
    if count == 1:
      return calcDirection([worm[0],theWay])
    else:
      return 0

def getNextWallCoords(lastWall):
    walls = []
    #append LEFT RIGHT walls
    loopcount = 0 
    for _ in range(CELLHEIGHT):
      if lastWall == RIGHT:
        walls.append({'x':0, 'y':loopcount})
      if lastWall == LEFT:
        walls.append({'x':CELLWIDTH-1, 'y':loopcount})
      loopcount = loopcount + 1
    #append TOP BOTTOM walls
    loopcount = 0 
    for _ in range(CELLWIDTH):
      if lastWall == DOWN:
        walls.append({'x':loopcount, 'y':0})
      if lastWall == UP:
        walls.append({'x':loopcount, 'y':CELLHEIGHT-1})
      loopcount = loopcount + 1
    return walls

def safeToGo(worm,direction,lastWall):
    listOfNo = wallCoords + worm
    listOfNo.extend(getNextWallCoords(lastWall))
    head = worm[0]
    forward = worm[0]
    forwardLeft = worm[0]
    forwardRight = worm[0]
    left = worm[0]
    right = worm[0]
    if direction == UP:
        newHead = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] - 1}
        forward = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] - 2}
        forwardLeft = {'x': worm[HEAD]['x']-1, 'y': worm[HEAD]['y'] - 1}
        forwardRight = {'x': worm[HEAD]['x']+1, 'y': worm[HEAD]['y'] - 1}
        left = {'x': worm[HEAD]['x']-1, 'y': worm[HEAD]['y']}
        right = {'x': worm[HEAD]['x']+1, 'y': worm[HEAD]['y']}
    elif direction == DOWN:
        newHead = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] + 1}
        forward = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] + 2}
        forwardLeft = {'x': worm[HEAD]['x']-1, 'y': worm[HEAD]['y'] + 1}
        forwardRight = {'x': worm[HEAD]['x']+1, 'y': worm[HEAD]['y'] + 1}
        left = {'x': worm[HEAD]['x']-1, 'y': worm[HEAD]['y']}
        right = {'x': worm[HEAD]['x']+1, 'y': worm[HEAD]['y']}
    elif direction == LEFT:
        newHead = {'x': worm[HEAD]['x'] - 1, 'y': worm[HEAD]['y']}
        forward = {'x': worm[HEAD]['x'] - 2, 'y': worm[HEAD]['y']}
        forwardLeft = {'x': worm[HEAD]['x']-1, 'y': worm[HEAD]['y'] + 1}
        forwardRight = {'x': worm[HEAD]['x']-1, 'y': worm[HEAD]['y'] - 1}
        left = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y']+1}
        right = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y']-1}
    elif direction == RIGHT:
        newHead = {'x': worm[HEAD]['x'] + 1, 'y': worm[HEAD]['y']}
        forward = {'x': worm[HEAD]['x'] + 2, 'y': worm[HEAD]['y']}
        forwardLeft = {'x': worm[HEAD]['x']+1, 'y': worm[HEAD]['y'] - 1}
        forwardRight = {'x': worm[HEAD]['x']+1, 'y': worm[HEAD]['y'] + 1}
        left = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y']-1}
        right = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y']+1}

    #print ('newhead',newHead,'no go:',listOfNo)
    if (forwardLeft in listOfNo and not left in listOfNo) or (forwardRight in listOfNo and not right in listOfNo):
      #print ('forwardleft left detected',forwardLeft,left,'right:',forwardRight,right)
      return False
    if newHead in listOfNo:
      return False
    waysToGo = []
    waysToGo = getNeighborhood(newHead)
    count = len(waysToGo)
    for each in waysToGo:
      if each in listOfNo:
        count = count - 1
    #print (waysToGo,count)
    if count < 1:
      return False
    elif count < 2 and not (forward in listOfNo):
      return False
    else:
      return True

def checkLastWall(worm):
    x = worm[0]['x']
    y = worm[0]['y']
    if x == 0:
      return LEFT
    elif x == CELLWIDTH - 1:
      return RIGHT
    elif y == 0:
      return UP
    elif y == CELLHEIGHT -1:
      return DOWN
    else:
      return 0

def checkSmartTurn(worm,listOfNo,direction1,direction2):
    if direction1 == UP or direction1 == DOWN:
      if direction2 == RIGHT:
        if {'x': worm[HEAD]['x']+3, 'y': worm[HEAD]['y']} in listOfNo and (not {'x': worm[HEAD]['x']+2, 'y': worm[HEAD]['y']} in listOfNo):
          return True
        else:
          return False
      if direction2 == LEFT:
        if {'x': worm[HEAD]['x']-3, 'y': worm[HEAD]['y']} in listOfNo and (not {'x': worm[HEAD]['x']-2, 'y': worm[HEAD]['y']} in listOfNo):
          return True
        else:
          return False
    if direction1 == LEFT or direction1 == RIGHT:
      if direction2 == UP:
        if {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y']-3} in listOfNo and (not {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y']-2} in listOfNo):
          return True
        else:
          return False
      if direction2 == DOWN:
        if {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y']+3} in listOfNo and (not {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y']+2} in listOfNo):
          return True
        else:
          return False    

def findBetterDirection(worm, direction,lastWall):
    listOfNo = list(worm)
    smartTurn = False   #dont kill yourself in the corner 
    if direction == UP:
        areaLeft = calcArea({'x': worm[HEAD]['x']-1, 'y': worm[HEAD]['y']},worm,lastWall)
        areaRight = calcArea({'x': worm[HEAD]['x']+1, 'y': worm[HEAD]['y']},worm,lastWall)
        if areaLeft == 0 and areaRight == 0:
          return [direction]
        areaStraight = calcArea({'x': worm[HEAD]['x'], 'y': worm[HEAD]['y']-1},worm,lastWall)
        maxArea = max(areaLeft,areaRight,areaStraight)
        print ('Options:', 'left:',areaLeft,'right:',areaRight,'straight:',areaStraight)
        if maxArea == areaStraight:
          return [direction]
        elif maxArea == areaLeft:
          if checkSmartTurn(worm,listOfNo,direction,LEFT):
            print('Smart Turn Enabled')
            return [LEFT, LEFT]
          else:
            return [LEFT, DOWN]
        else:
          if checkSmartTurn(worm,listOfNo,direction,RIGHT):
            print('Smart Turn Enabled')
            return [RIGHT, RIGHT]
          else:
            return [RIGHT,DOWN]

    if direction == DOWN:
        areaLeft = calcArea({'x': worm[HEAD]['x']-1, 'y': worm[HEAD]['y']},worm,lastWall)
        areaRight = calcArea({'x': worm[HEAD]['x']+1, 'y': worm[HEAD]['y']},worm,lastWall)
        if areaLeft == 0 and areaRight == 0:
          return [direction]
        areaStraight = calcArea({'x': worm[HEAD]['x'], 'y': worm[HEAD]['y']+1},worm,lastWall)
        maxArea = max(areaLeft,areaRight,areaStraight)
        print ('Options:','left:',areaLeft,'right:',areaRight,'straight:',areaStraight)
        if maxArea == areaStraight:
          return [direction]
        elif areaLeft == maxArea:
          if checkSmartTurn(worm,listOfNo,direction,LEFT):
            print('Smart Turn Enabled')
            return [LEFT, LEFT]
          else:
            return [LEFT, UP]
        else:
          if checkSmartTurn(worm,listOfNo,direction,RIGHT):
            print('Smart Turn Enabled')
            return [RIGHT, RIGHT]
          else:
            return [RIGHT,UP]

    elif direction == LEFT:
        areaUp = calcArea({'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] - 1},worm,lastWall)
        areaDown = calcArea({'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] + 1},worm,lastWall)
        if areaUp == 0 and areaDown == 0:
          return [direction]
        areaStraight = calcArea({'x': worm[HEAD]['x']-1, 'y': worm[HEAD]['y']},worm,lastWall)
        maxArea = max(areaStraight,areaUp,areaDown)
        print ('Options:','up:',areaUp,'down:',areaDown,'straight:',areaStraight)
        if maxArea == areaStraight:
          return [direction]       
        elif maxArea == areaUp:
          if checkSmartTurn(worm,listOfNo,direction,UP):
            print('Smart Turn Enabled')
            return [UP, UP]
          else:
            return [UP,RIGHT]
        else:
          if checkSmartTurn(worm,listOfNo,direction,DOWN):
            print('Smart Turn Enabled')
            return [DOWN, DOWN]
          else:
            return [DOWN,RIGHT]

    elif direction == RIGHT:
        areaUp = calcArea({'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] - 1},worm,lastWall)
        areaDown = calcArea({'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] + 1},worm,lastWall)
        if areaUp == 0 and areaDown == 0:
          return [direction]
        areaStraight = calcArea({'x': worm[HEAD]['x']+1, 'y': worm[HEAD]['y']},worm,lastWall)
        maxArea = max(areaStraight,areaUp,areaDown)
        print ('Options:','up:',areaUp,'down:',areaDown,'straight:',areaStraight)
        if maxArea == areaStraight:
          return [direction]              
        elif areaUp ==maxArea:
          if checkSmartTurn(worm,listOfNo,direction,UP):
            print('Smart Turn Enabled')
            return [UP, UP]
          else:
            return [UP,LEFT]
        else:
          if checkSmartTurn(worm,listOfNo,direction,DOWN):
            print('Smart Turn Enabled')
            return [DOWN, DOWN]
          else:
            return [DOWN,LEFT]

def findNextDirection(worm, direction,lastWall):
    listOfNo = list(worm)
    areaLeft = calcArea({'x': worm[HEAD]['x']-1, 'y': worm[HEAD]['y']},worm,lastWall)
    areaRight = calcArea({'x': worm[HEAD]['x']+1, 'y': worm[HEAD]['y']},worm,lastWall)
    areaUp = calcArea({'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] - 1},worm,lastWall)
    areaDown = calcArea({'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] + 1},worm,lastWall)
    maxArea = max(areaLeft,areaRight,areaUp,areaDown)
    if maxArea == areaUp:
      return [UP]
    elif maxArea == areaDown:
      return [DOWN]
    elif maxArea == areaLeft:
      return [LEFT]
    else:
      return [RIGHT]

def calcArea(point, worm, lastWall):
    nextWall = getNextWallCoords(lastWall)
    if point in worm or point in wallCoords or point in nextWall:
      return 0
    tailBonus = 0
    q = []
    searchPoints = []
    searchPoints.append(point)
    while (searchPoints):
      i = searchPoints.pop()
      for each in getNeighborhood(i):
        if not each in q:
          if not (each in worm or each in wallCoords or point in nextWall):
            searchPoints.append(each)
        if each == worm[-1]:
          tailBonus = 200
      q.append(i)
    return len(q)+tailBonus

def AreaIsTooSmall(bound,point, worm, lastWall):
    nextWall = getNextWallCoords(lastWall)
    if point in worm or point in wallCoords or point in nextWall:
      return True
    tailBonus = 0
    q = []
    searchPoints = []
    searchPoints.append(point)
    while (searchPoints):
      i = searchPoints.pop()
      for each in getNeighborhood(i):
        if not each in q:
          if not (each in worm or each in wallCoords or point in nextWall):
            searchPoints.append(each)
        if each == worm[-1]:
          tailBonus = 200
      q.append(i)
      if (len(q) + tailBonus) > bound:
        return False
    return True

def calcCost(point,worm):
    print ('calculating cost of point', point)
    neibors = getNeighborhood(point)
    for each in neibors:
      if each in worm[1:]:
        return worm.index(each)
    return 999

def calcDirection(path):
    '''Converting point-path to step by step direction'''
    lastPoint = path[0]
    directions = []
    nextDirection = ''
    for currentPoint in path:
      if (currentPoint['x'] > lastPoint['x']):
        nextDirection = RIGHT
      elif (currentPoint['x'] < lastPoint['x']):
        nextDirection = LEFT
      else:
        if (currentPoint['y'] > lastPoint['y']):
          nextDirection = DOWN
        elif (currentPoint['y'] < lastPoint['y']):
          nextDirection = UP
        else:
          #print ('Apple Found...')
          continue
      #print ('Last Point:', lastPoint, 'currentPoint:', currentPoint, ' --> ', nextDirection)
      lastPoint = currentPoint
      directions.append(nextDirection)
    #print (directions)
    return directions

def calculatePath(worm,apple,softCalculation):
  oldWorm = list(worm)
  #print(newWorm)
  path = mainCalculation(worm,apple,softCalculation)
  if not path:
    return []
  else:
    pathCopy = list(path)
    pathCopy.reverse()
    newWorm = pathCopy + oldWorm
    pathOut = mainCalculation(newWorm,newWorm[-1],False)
    if not pathOut:
      print('No path out, dont go for apple')
      return 'stall'
    else:
      return path

def mainCalculation(worm,apple,softCalculation):
  pointsToPath= []
  discoverEdge = []
  newPoints = []
  exhaustedPoints = []
  numberOfPoints = 1         #if all point tested go back one point
  findingPath = True  #false
  listOfNo = getListOfNo(worm)
  softListOfNo = getSoftListOfNo(worm)
  softListOfNo.extend(softWallCoords)
  discoverEdge.append(worm[0])
  exhaustedPoints.append(worm[0])
  lastPoint = discoverEdge[-1]
  pointsToPath.append(lastPoint)

  if (apple in softWallCoords) or (apple in softListOfNo):
    softCalculation = False

  #calculate avialable path
  while(findingPath and softCalculation):
    lastPoint = discoverEdge[-1]
    newPoints = getNeighborhood(lastPoint)
    newPoints = sorted(newPoints, key = lambda k: calcDistance(k,apple), reverse = True)  #sort newPoints
    numberOfPoints = len(newPoints)
    for point in newPoints:
      if point in softListOfNo:
        #print ('No Go Point:', point)
        numberOfPoints = numberOfPoints -1
      elif point in exhaustedPoints:
        #print ('considered already:', point)
        numberOfPoints = numberOfPoints -1
      else:                                
        discoverEdge.append(point)        #new points --> discoverEdge, closest one last in
        pointsToPath.append(lastPoint) 
        exhaustedPoints.append(lastPoint)
        #print (point)
      #exhaustedPoints.append(point)
    if numberOfPoints == 0:
      #backtrack
      exhaustedPoints.append(discoverEdge.pop())
      exhaustedPoints.append(pointsToPath.pop())
    if apple in discoverEdge:
      findingPath = 0
    if not discoverEdge:
      softCalculation = False 
      break

  #print ('softCalculation: ', softCalculation)
  if not softCalculation:
    pointsToPath= []
    discoverEdge = []
    newPoints = []
    exhaustedPoints = []
    numberOfPoints = 1         #if all point tested go back one point
    findingPath = True  #false
    listOfNo = getListOfNo(worm)
    discoverEdge.append(worm[0])
    exhaustedPoints.append(worm[0])
    lastPoint = discoverEdge[-1]
    pointsToPath.append(lastPoint)

    #calculate avialable path
    while(findingPath):
      lastPoint = discoverEdge[-1]
      newPoints = getNeighborhood(lastPoint)
      newPoints = sorted(newPoints, key = lambda k: calcDistance(k,apple), reverse = True)  #sort newPoints
      numberOfPoints = len(newPoints)
      for point in newPoints:
        if point in listOfNo:
          #print ('No Go Point:', point)
          numberOfPoints = numberOfPoints -1
        elif point in exhaustedPoints:
          #print ('considered already:', point)
          numberOfPoints = numberOfPoints -1
        else:                                
          discoverEdge.append(point)        #new points --> discoverEdge, closest one last in
          pointsToPath.append(lastPoint) 
          exhaustedPoints.append(lastPoint)
          #print (point)
        #exhaustedPoints.append(point)
      if numberOfPoints == 0:
        #backtrack
        exhaustedPoints.append(discoverEdge.pop())
        exhaustedPoints.append(pointsToPath.pop())
      if apple in discoverEdge:
        findingPath = 0
      if not discoverEdge:
        #print ('stalling...')   #should start stalling since no path found 
        return []
      '''
      #Debugging................
      #Draw path found
      DISPLAYSURF.fill(BGCOLOR)
      drawGrid()
      drawWorm(worm)
      #drawEdgeOfDiscovery(discoverEdge)
      drawEdgeOfDiscovery(pointsToPath)
      drawEdgeOfDiscovery(listOfNo)
      drawApple(apple)
      pygame.display.update()
      pauseGame()
      print ('points to path')
      print (pointsToPath)
      '''      


  ##WHEN DISCOVER EDGE IS EMPTY, TRY FIND TAIL
  pointsToPath.append(apple)       #adding in the last point 
  return pointsToPath

def getNeighborhood(point):      ### NOT NEGATIVE
  neighborhood = []
  if point['x'] < CELLWIDTH:
    neighborhood.append({'x':point['x']+1,'y':point['y']})
  if point['x'] > 0:
    neighborhood.append({'x':point['x']-1,'y':point['y']})
  if point['y'] < CELLHEIGHT:
    neighborhood.append({'x':point['x'],'y':point['y']+1})
  if point['y'] >0:
    neighborhood.append({'x':point['x'],'y':point['y']-1})
  return neighborhood

def calcDistance(point, apple):
  distance = abs(point['x'] - apple['x']) + abs(point['y'] - apple['y'])
  return distance

def getSoftListOfNo(worm):
  listOfNo = []
  listOfNo.extend(getWormSurroundings(worm))
  #listOfNo.extend(softWallCoords)
  #remove duplicates
  return listOfNo 


def getWormSurroundings(worm):
  listOfNo = []
  headx = worm[0]['x']
  heady = worm[0]['y']
  count = 0
  for each in worm:
    if count == 0:
      listOfNo.append(each)
    else:
      dist = abs (each['x'] - headx) + abs(each['y']-heady)
      countFromBehind = len(worm) - count
      if dist < (countFromBehind+1):
        listOfNo.append(each)
        listOfNo.append({'x':each['x']+1,'y':each['y']})
        listOfNo.append({'x':each['x']-1,'y':each['y']})
        listOfNo.append({'x':each['x'],'y':each['y']+1})
        listOfNo.append({'x':each['x'],'y':each['y']-1})
        listOfNo.append({'x':each['x']+1,'y':each['y']+1})
        listOfNo.append({'x':each['x']-1,'y':each['y']-1})
        listOfNo.append({'x':each['x']-1,'y':each['y']+1})
        listOfNo.append({'x':each['x']+1,'y':each['y']-1})
    count = count + 1
  seen = set()
  newList = []
  for d in listOfNo:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        newList.append(d)
  return newList



def getListOfNo(worm):
  listOfNo = []
  headx = worm[0]['x']
  heady = worm[0]['y']
  count = 0
  for each in worm:
    dist = abs (each['x'] - headx) + abs(each['y']-heady)
    countFromBehind = len(worm) - count
    count = count + 1 
    if dist < (countFromBehind+1):
      listOfNo.append(each)
  listOfNo.extend(wallCoords)
  #print ('List of No Go:')
  #print (listOfNo)
  return listOfNo


def findWall():
  walls = []
  #append LEFT RIGHT walls
  loopcount = 0 
  for _ in range(CELLHEIGHT):
    walls.append({'x':-1       , 'y':loopcount})
    walls.append({'x':CELLWIDTH, 'y':loopcount})
    loopcount = loopcount + 1
  #append TOP BOTTOM walls
  loopcount = 0 
  for _ in range(CELLWIDTH):
    walls.append({'x':loopcount, 'y':-1})
    walls.append({'x':loopcount, 'y':CELLHEIGHT})
    loopcount = loopcount + 1
  #print (walls)
  return walls

def findSoftWall():
  walls = []
  #append LEFT RIGHT walls
  loopcount = 0 
  for _ in range(CELLHEIGHT):
    walls.append({'x':0       , 'y':loopcount})
    walls.append({'x':CELLWIDTH-1, 'y':loopcount})
    loopcount = loopcount + 1
  #append TOP BOTTOM walls
  loopcount = 0 
  for _ in range(CELLWIDTH):
    walls.append({'x':loopcount, 'y':0})
    walls.append({'x':loopcount, 'y':CELLHEIGHT-1})
    loopcount = loopcount + 1
  #print (walls)
  return walls


def drawEdgeOfDiscovery(points):
    for point in points:
        x = point['x'] * CELLSIZE
        y = point['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, ORANGE, wormSegmentRect)
    lastPointRect = pygame.Rect(points[-1]['x']*CELLSIZE, points[-1]['y']*CELLSIZE, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, (255,255,255), wormSegmentRect)
    #print('Drawing Edge of Discovery...')
    #time.sleep(0.05)


def sectionBreak():
  print('AAAAAAAAAAAAAAAAAAAA')
  print('AAAAAAAAAAAAAAAAAAAA')
  print('AAAAAAAAAAAAAAAAAAAA')
  print('AAAAAAAAAAAAAAAAAAAA')
  print('AAAAAAAAAAAAAAAAAAAA')
  print('AAAAAAAAAAAAAAAAAAAA')
  print('AAAAAAAAAAAAAAAAAAAA')


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
    '''
    x = wormCoords[0]['x'] * CELLSIZE
    y = wormCoords[0]['y'] * CELLSIZE
    wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, WHITE, wormSegmentRect)
    x = wormCoords[-1]['x'] * CELLSIZE
    y = wormCoords[-1]['y'] * CELLSIZE
    wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, WHITE, wormSegmentRect)
    '''


def drawApple(coord,lastApple):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)
    #x1 = lastApple['x'] * CELLSIZE
    #y1 = lastApple['y'] * CELLSIZE
    #appleRect = pygame.Rect(x1, y1, CELLSIZE, CELLSIZE)
    #pygame.draw.rect(DISPLAYSURF, RED, appleRect)    


def drawGrid():
    return  #do nothing
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()
