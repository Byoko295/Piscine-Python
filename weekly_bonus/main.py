import pygame

pygame.init()
print("Driver:", pygame.display.get_driver())  # Should print x11
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("SSH X11 Test")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
