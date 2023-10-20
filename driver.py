"""
Taylor Turner
10/17/23
The purpose of this program is to experiment with visualization of changing data using graphs
and sorting algorithms
"""

import pygame 
import random
from math import floor

pygame.init() 

# Time variables
clock = pygame.time.Clock()
deltaTime = 0

# CREATING CANVAS 
screenInfo = pygame.display.Info()

canvasSize = (
    pygame.display.Info().current_w/2, 
    pygame.display.Info().current_h/2
    )
canvas = pygame.display.set_mode((canvasSize[0], canvasSize[1]))
  
# TITLE OF CANVAS 
pygame.display.set_caption("Sorting Algorithm Visualizer") 
exit = False

# RECTANGLE OBJECT DECLARATION
class RectangleList:
    def __init__(self):
        self.rectangles = [] # List of rectangle objects
        self.size = 20 # The number of pixels wide the rectangles will be when displayed
        self.countMax = floor((canvasSize[0]-(self.size*2))/self.size) # Takes the size of the window, add a buffer of 40 to leave a blank space at the first and last rectangle slot
        self.count = self.countMax # The number of rectangles, provided if you want less than the max
        self.randomHeightMin = 20 # The minimum height each rectangle can be. Technically this can cause problems if the window is smaller than 20 pixels, but that
        self.randomHeightMax = floor((canvasSize[1]-max(10, self.size))) # The maximum height based on the size of the window. This allows this program to run on any computer and still work
        self.swapped = True
        self.isSorted = False
        self.stepTime = 250 # Time between each step in miliseconds
        
        pygame.time.set_timer(pygame.USEREVENT, self.stepTime) # Sends the userevent to trigger sorting every self.stepTime miliseconds
        
        if self.count > self.countMax: # If the rectangle count is too high, this will overwrite it with the maximum. Doesn't do much for now, added for future use. TODO: Add a slider or button to increase scale during runtime.
            self.count = self.count
        # Adds the rectangles to the rectangle[] list
        for x in range(0, self.count):
            randHeight = random.randrange(10, self.randomHeightMax)
            self.rectangles.append(pygame.Rect(self.size*(x+1), canvasSize[1]-randHeight,self.size,randHeight))

    def randomizeHeights(self):
        for x in range(0,self.count):
            randHeight = random.randrange(10, self.randomHeightMax)
            self.rectangles[x].height = randHeight
            self.rectangles[x].top = canvasSize[1]-randHeight

    def doSort(self):
        self.isSorted = False
    # Swaps the height and y position of two rectangles. It DOES NOT change the index different points are stored at
    def swap(self, arr, i, j):
        # Swap the heights of two elements
        temp = arr[i].height
        arr[i].height = arr[j].height
        arr[j].height = temp
        # Swaps the y position of the cubes, allowing them to be properly oriented.
        temp = arr[i].top
        arr[i].top = arr[j].top
        arr[j].top = temp

    def draw(self,canvas):
        for count in range(0, self.count):
            currentRect = self.rectangles[count]
            # if count == ghost:
            #     pygame.draw.rect(canvas, "#851e3e", currentRect) # Draws red
            #     continue
            if count % 2 == 0:
                pygame.draw.rect(canvas, "#011f4b", currentRect) # Draws blue1 on even count rects
            else:
                pygame.draw.rect(canvas, "#005b96", currentRect) # Draws blue2 on odd count rects

    # COCKTAIL SHAKER SORTING ALGORITHM
    def sort(self):
        if not self.isSorted: # If swapped is true (indicating the previous iteration has caused a swap or the sorting algorithm has been activated)
            for x in range(0, self.count - 1):
                if self.rectangles[x].height > self.rectangles[x+1].height:
                    self.swap(self.rectangles, x, x+1)
                    self.swapped = True
            if not self.swapped:
                self.isSorted = False
                for y in range(self.count - 1, 0):
                    if self.rectangles[y].height > self.rectangles[y+1].height:
                        self.swap(self.rectangles, y, y+1)
                        self.swapped = True
                        
        
# BUTTON OBJECT DECLARATION
class Button:
    def __init__(self, xinput,yinput, widthInput, heightInput, triggerFunctionInput, textInput = 'Button', ):
        # Location Variables
        self.x = xinput
        self.y = yinput
        # Dimension Variables
        self.width = widthInput
        self.height = heightInput
        # Content Variables
        self.text = textInput
        # Config Variables
        self.triggerFunction = triggerFunctionInput # This is the function that is called when the button is pressed
        self.fillColors = {
            'normal': '#ffffff', # Default color
            'hover': '#666666', # When the mouse hovers over the button
            'pressed': '#333333', # When the button is pressed
        }
        # Render Variables
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.fontRenderer = pygame.font.SysFont('Verdana', 40).render(self.text, True, (0, 0, 0))
    
    def update(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                self.triggerFunction()
        self.buttonSurface.blit(self.buttonSurface, [
            self.buttonRect.width/2 - self.buttonSurface.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurface.get_rect().height/2
        ])
        canvas.blit(self.buttonSurface, self.buttonRect)


rect = RectangleList() # Declare rect as the Rectangle object
shuffleButton = Button(20, 20, 40, 20, rect.randomizeHeights, "Shuffle")

while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
        if event.type == pygame.USEREVENT:
            rect.sort()
    canvas.fill("#b3cde0")
    rect.draw(canvas)

    shuffleButton.update()
    pygame.display.update()

    # deltaTime in seconds.
    deltaTime = clock.tick(60) / 1000.0