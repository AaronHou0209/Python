# Example file showing a basic pygame "game loop"
import pygame

# pygame setup 
pygame.init()
# make a surface 
screen = pygame.display.set_mode((1280,640))
clock = pygame.time.Clock()
running = True

# pygame.image.load == downloading the photo
# pygame consider any photo is another surface
# convert == pixel to photo 

potato_img = pygame.image.load('potato.jpg').convert()
x = 0
#resize
potato_img = pygame.transform.scale(potato_img,
                                    (potato_img.get_width()*0.5,
                                     potato_img.get_height()*0.5))

# setup a clock 
clock = pygame.time.Clock()
while running:
    # fill the screen with a color to wipe away anything from last frame

    screen.fill("red")
    # draw this photo on another 
    screen.blit(potato_img,(x,30))
    
    hitbox = pygame.Rect(x,30,potato_img.get_width(),potato_img.get_height())

    target = pygame.Rect(300,0,160,280) 
    collision = hitbox.colliderect(target)
    pygame.draw.rect(screen,(255 * collision ,255,0),target)

    x += 1 
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    # for quit the surface and make it smooth closed. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the screen 
    pygame.display.flip()
    #upload a clock - 60 is the masmiun 
    clock.tick(60)
   
pygame.quit()
