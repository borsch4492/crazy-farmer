import pygame

pygame.init()

sc = pygame.display.set_mode((300, 300))
sc.fill((200, 255, 200))

surf1 = pygame.Surface((200, 200))
surf1.fill((220, 200, 0))  # желтая
surf2 = pygame.Surface((100, 100))
surf2.fill((255, 255, 255))  # белая

rect = pygame.Rect((70, 20, 0, 0))

surf1.blit(surf2, rect)
sc.blit(surf1, rect)

pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
