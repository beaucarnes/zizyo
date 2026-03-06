import pygame, random
pygame.init()
screen, font = pygame.display.set_mode((400, 600)), pygame.font.Font(None, 36)

player, lava, score, vy = pygame.Rect(200, 520, 20, 20), pygame.Rect(0, 580, 400, 20), 0, 0
plats, coin = [], None

def reset(win=False):
    global score, vy, plats, coin
    score += win 
    player.topleft, vy = (200, 520), 0

    plats = [pygame.Rect(170, 550, 60, 10)] + [pygame.Rect(random.randint(50, 290), y, 60, 10) for y in (450, 350, 250, 150)]
    coin = pygame.Rect(plats[-1].x + 20, 130, 20, 20)

reset()

while True:
    screen.fill((135, 206, 235))

    for e in pygame.event.get():
        if e.type == pygame.QUIT: exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and vy == 0: vy = -12

    keys = pygame.key.get_pressed()
    player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    vy += 0.5; player.y += vy 

    for p in plats:
        pygame.draw.rect(screen, (0, 255, 0), p)
        if player.colliderect(p):
            if vy > 0: player.bottom, vy = p.top, 0
            elif vy < 0: player.top, vy = p.bottom, 0

    pygame.draw.rect(screen, (255, 0, 0), lava)
    pygame.draw.ellipse(screen, (255, 215, 0), coin)

    if player.colliderect(lava): reset(False)
    if player.colliderect(coin): reset(True)

    pygame.draw.rect(screen, (200, 200, 200), player)
    screen.blit(font.render(f"Score: {score}", True, (0,0,0)), (10, 10))
    pygame.display.flip(); pygame.time.delay(30)
