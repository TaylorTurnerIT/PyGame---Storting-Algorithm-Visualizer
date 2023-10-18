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
    rectangles = [] # Array of rectangle objects
    size = 20 # The number of pixels wide the rectangles will be when displayed
    countMax = floor((canvasSize[0]-(size*2))/size) # Takes the size of the window, add a buffer of 40 to leave a blank space at the first and last rectangle slot
    count = countMax # The number of rectangles, provided if you want less than the max
    randomHeightMin = 20 # The minimum height each rectangle can be. Technically this can cause problems if the window is smaller than 20 pixels, but that
    randomHeightMax = floor((canvasSize[1]-max(10, size))) # The maximum height based on the size of the window. This allows this program to run on any computer and still work
    swapped = False

    def swap(self, rect1, rect2):
        temp = rect1
        rect1 = rect2
        rect2 = temp
    
    def cocktailSort(self):
        swapped = True
        while swapped:
            
            swapped = False
            for x in range(0, rect.count):
                if rect.rectangles[x].height > rect.rectangles[x+1].height:
                    rect.swap(rect.rectangles[x], rect.rectangles[x+1])
                    swapped = True
            
            if not swapped:
                break

            swapped = False
            for y in range(rect.count-1, 0):
                if rect.rectangles[y].height > rect.rectangles[y+1].height:
                    rect.swap(rect.rectangles[y], rect.rectangles[y+1])
                    swapped = True

        


rect = RectangleList # Declare rect as the Rectangle object

if rect.count > rect.countMax: # If the rectangle count is too high, this will overwrite it with the maximum. Doesn't do much for now, added for future use. TODO: Add a slider or button to increase scale during runtime.
    rect.count = rect.count

# Adds the rectangles to the rectangle[] list
for x in range(0, rect.count):
    randHeight = random.randrange(10, rect.randomHeightMax)
    rect.rectangles.append(pygame.Rect(rect.size*(x+1), canvasSize[1]-randHeight,rect.size,randHeight))

# SORTING VARIABLES
ghost = 0
swapped = False

while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    canvas.fill("#b3cde0")
    
    rect.cocktailSort
    for count in range(0, rect.count):
        currentRect = rect.rectangles[count]

        if count == ghost:
            pygame.draw.rect(canvas, "#851e3e", currentRect) # Draws red
            continue
        if count % 2 == 0:
            pygame.draw.rect(canvas, "#011f4b", currentRect) # Draws blue1 on even count rects
        else:
            pygame.draw.rect(canvas, "#005b96", currentRect) # Draws blue2 on odd count rects
    ghost += 1 # Iterates the ghost to the next rect
    ghost %= rect.count # This bounds the "ghost" to repeat at the beginning of the list when it reaches the end
    
    


        

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