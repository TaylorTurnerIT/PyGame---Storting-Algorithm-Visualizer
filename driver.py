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

# SORTING VARIABLES
ghost = 0
swapped = True

# RECTANGLE OBJECT DECLARATION
class RectangleList:
    rectangles = [] # List of rectangle objects
    size = 20 # The number of pixels wide the rectangles will be when displayed
    countMax = floor((canvasSize[0]-(size*2))/size) # Takes the size of the window, add a buffer of 40 to leave a blank space at the first and last rectangle slot
    count = countMax # The number of rectangles, provided if you want less than the max
    randomHeightMin = 20 # The minimum height each rectangle can be. Technically this can cause problems if the window is smaller than 20 pixels, but that
    randomHeightMax = floor((canvasSize[1]-max(10, size))) # The maximum height based on the size of the window. This allows this program to run on any computer and still work
    swapped = False
    stepTime = 250 # Time between each step in miliseconds

    def __init__(self):
        pygame.time.set_timer(pygame.USEREVENT, self.stepTime) # Sends the userevent to trigger sorting every self.stepTime miliseconds
        if self.count > self.countMax: # If the rectangle count is too high, this will overwrite it with the maximum. Doesn't do much for now, added for future use. TODO: Add a slider or button to increase scale during runtime.
            self.count = self.count
        # Adds the rectangles to the rectangle[] list
        for x in range(0, self.count):
            randHeight = random.randrange(10, self.randomHeightMax)
            self.rectangles.append(pygame.Rect(self.size*(x+1), canvasSize[1]-randHeight,self.size,randHeight))

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

            if count == ghost:
                pygame.draw.rect(canvas, "#851e3e", currentRect) # Draws red
                continue
            if count % 2 == 0:
                pygame.draw.rect(canvas, "#011f4b", currentRect) # Draws blue1 on even count rects
            else:
                pygame.draw.rect(canvas, "#005b96", currentRect) # Draws blue2 on odd count rects

    # COCKTAIL SHAKER SORTING ALGORITHM
    def sort(self):
        swapped = True
        if swapped: # If swapped is true (indicating the previous iteration has caused a swap)
            swapped = False
            for x in range(0, self.count - 1):
                ghost = x
                self.draw(canvas)
                if self.rectangles[x].height > self.rectangles[x+1].height:
                    self.swap(self.rectangles, x, x+1)
                    swapped = True
            if swapped:
                swapped = False
                for y in range(self.count - 1, 0):
                    ghost = y
                    self.draw(canvas)
                    if self.rectangles[y].height > self.rectangles[y+1].height:
                        self.swap(self.rectangles, y, y+1)
                        swapped = True    
        
rect = RectangleList() # Declare rect as the Rectangle object

while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
        if event.type == pygame.USEREVENT:
            rect.sort()
            
    
    canvas.fill("#b3cde0")
    rect.draw(canvas)
    pygame.display.update()
    
    
    
    # deltaTime in seconds.
    deltaTime = clock.tick(60) / 1000.0


    """ https://en.wikipedia.org/wiki/Cocktail_shaker_sort 

procedure cocktailShakerSort(A : list of sortable items) is
    do
        swapped := false
        for each i in 0 to length(A) − 1 do:
            if A[i] > A[i + 1] then // test whether the two elements are in the wrong order
                swap(A[i], A[i + 1]) // let the two elements change places
                swapped := true
            end if
        end for
        if not swapped then
            // we can exit the outer loop here if no swaps occurred.
            break do-while loop
        end if
        swapped := false
        for each i in length(A) − 1 to 0 do:
            if A[i] > A[i + 1] then
                swap(A[i], A[i + 1])
                swapped := true
            end if
        end for
    while swapped // if no elements have been swapped, then the list is sorted
end procedure
    """