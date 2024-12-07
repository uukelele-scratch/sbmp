import pygame
import sys




if len(sys.argv) < 2:
    sys.stderr.write("File not specified")
    sys.exit()

filename = sys.argv[1]

# Initialize Pygame
pygame.init()

with open(filename,'r') as file:
    lines = file.read().splitlines()
img_size = int(lines[0])
img_data = lines[1]

img_data = img_data.replace('[','')
img_data = img_data.replace(']','')
img_data = img_data.replace(',','')
pixels = img_data.split(' ')

# Set up display
size = (img_size, img_size)  # Window size
window = pygame.display.set_mode(size)
pygame.display.set_caption(filename)

# Define a function to draw a pixel
def draw_pixel(surface, color, pos):
    surface.set_at(pos, color)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    i = 0
    for y in range(img_size):
        for x in range(img_size):
            pixel = int(pixels[i])
            r = (pixel / 65536) % 256
            g = (pixel / 256) % 256
            b = pixel % 256
            draw_pixel(window, (r,g,b),(x,y))
            i += 1
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
