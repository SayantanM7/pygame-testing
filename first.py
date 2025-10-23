import pygame

# Initialize required modules
pygame.init()  

# Setup window geometry (width, height)
screen = pygame.display.set_mode((400, 500))  

# Create a loop to run till the game is quit by the user
done = False  

while not done: 
    # Clear the event queue
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  # Set done to True to exit the loop
    
    
    screen.fill((255, 128, 0))
    
    # Make the changes visible
    pygame.display.flip()  

# Quit pygame properly after loop ends
pygame.quit()