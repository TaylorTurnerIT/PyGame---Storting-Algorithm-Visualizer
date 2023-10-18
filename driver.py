"""
Taylor Turner
10/17/23
The purpose of this program is to experiment with visualization of changing data using graphs
and sorting algorithms
"""

import pygame 
  
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

# Initialize the rectangle list
rectangleSize = 20
rectangleCount = 5
rectangles = []
for x in range(0, rectangleCount):
    rectangles.append(pygame.Rect(rectangleSize*(x+1), rectangleSize,rectangleSize,rectangleSize))
  
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    canvas.fill("white")

    for count in range(0, rectangleCount):
        currentRect = rectangles[count]
        if count % 2 == 0:
            pygame.draw.rect(canvas, "blue", currentRect)
        else:
            pygame.draw.rect(canvas, "red", currentRect)

    pygame.display.update() 
    
    
    # deltaTime in seconds.
    deltaTime = clock.tick(60) / 1000.0