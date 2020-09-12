import pygame

pygame.init()
window = pygame.display.set_mode((500,500))

pygame.display.set_caption("crazy-farmer.py")

x = 50
y = 50
w = 40
h = 60
s = 5


run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= s
    elif keys[pygame.K_RIGHT]:
        x += s
    elif keys[pygame.K_UP]:
        y -= s
    elif keys[pygame.K_DOWN]:
        y += s
    else:
        window.fill((0,0,0))

    pygame.draw.rect(window, (0, 0, 255), (x, y, w, h))
    pygame.display.update()
pygame.quit()
