
import pygame


pygame.init()

BLOCK_SIZE = 15

r_val = 100
g_val = 100
b_val = 100
# Uppercase names are for constants.
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
FONT = pygame.font.Font(None, 25)

displaysurf = pygame.display.set_mode((600, 600))
# This allows you to hold a key and after 200 ms the
# same event is emitted every 50 ms.
pygame.key.set_repeat(200, 50)
# A clock is useful to limit the frame rate.
clock = pygame.time.Clock()
running = True
# I replaced colUp colDown with this variable. Just set it
# to the desired value and then increment the rgb values.
col_change = 5


def drawColorValues():
    """Re-render all text surfaces."""
    text = FONT.render('Red Value: {}  '.format(r_val), True, WHITE, BLACK)
    displaysurf.blit(text,[10,500])
    text = FONT.render('Green Value: {}  '.format(g_val), True, WHITE, BLACK)
    displaysurf.blit(text,[10,530])
    text = FONT.render('Blue Value: {}  '.format(b_val), True, WHITE, BLACK)
    displaysurf.blit(text,[10,560])
    pygame.display.update()


def clamp(value, min_, max_):
    """Clamp value between min_ and max_."""
    return max(min_, min(value, max_))


drawColorValues()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(
                displaysurf, (r_val,g_val,b_val),
                [*event.pos, BLOCK_SIZE, BLOCK_SIZE])
            pygame.display.update()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                col_change = 5
            elif event.key == pygame.K_DOWN:
                col_change = -5
            elif event.key == pygame.K_r:
                r_val += col_change
                r_val = clamp(r_val, 0, 255)
            elif event.key == pygame.K_g:
                g_val += col_change
                g_val = clamp(g_val, 0, 255)
            elif event.key == pygame.K_b:
                # Increment and clamp in one line.
                b_val = clamp(b_val+col_change, 0, 255)
            drawColorValues()

    clock.tick(30)  # Cap at 30 fps.

pygame.quit()