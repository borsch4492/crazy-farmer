import pygame
from inputs import get_gamepad


pygame.init()
window = pygame.display.set_mode((500,500))

pygame.display.set_caption("crazy-farmer.py")


x = 50
y = 50
w = 40
h = 60
s = 5
joysticks = []
gamebutt = ""

isUp = False

run = True
while run:
    events = get_gamepad()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #if keys[pygame.K_UP]:
    if len(events) > 0:


        for event in events:
            #print(event.ev_type, event.code, event.state)
            if event.code != 'SYN_REPORT':
                gamebutt = event.code, event.state
                print(gamebutt)

    if gamebutt == ('ABS_HAT0Y', -1):
        isUp = True
    else:
        isUp = False
    if gamebutt == ('ABS_HAT0Y', 1):
        isDown = True
    else:
        isDown = False
    if gamebutt == ('ABS_HAT0X', -1):
        isLeft = True
    else:
        isLeft = False
    if gamebutt == ('ABS_HAT0X', 1):
        isRight = True
    else:
        isRight = False

    if keys[pygame.K_LEFT] or isLeft:
        x -= s
    elif keys[pygame.K_RIGHT] or isRight:
        x += s
    elif keys[pygame.K_UP] or isUp:
        y -= s
    elif keys[pygame.K_DOWN] or isDown:
        y += s
    else:
        window.fill((0,0,0))

    pygame.draw.rect(window, (0, 0, 255), (x, y, w, h))
    pygame.display.update()
pygame.quit()
