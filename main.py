# coded by 010mak
# give credit if you use it please

import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800
FALLING_SPEED_INCREMENT = 0.05
FALLING_ITEM_SIZE = 50
BASKET_SIZE = 60
BASKET_MOVE_SPEED = 10
SIZE_DECREMENT = 0.5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Mr. Cornish")

basket_img_original = pygame.image.load('images/basket.png')
basket_img = pygame.transform.scale(basket_img_original, (BASKET_SIZE, BASKET_SIZE))
basket_rect = basket_img.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT))

cornish_img = pygame.image.load('images/Cornish.png')
cornish_img = pygame.transform.scale(cornish_img, (FALLING_ITEM_SIZE, FALLING_ITEM_SIZE))

dincer_img = pygame.image.load('images/Dincer.png')
dincer_img = pygame.transform.scale(dincer_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_icon(cornish_img)

pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

violin_sound = pygame.mixer.Sound('sounds/violin.mp3')

font_size = 24
font = pygame.font.Font('fonts/custom_font.ttf', font_size)
button_font = pygame.font.Font('fonts/custom_font.ttf', font_size)

score = 0
high_score = 0
current_basket_size = BASKET_SIZE
basket_x = SCREEN_WIDTH // 2
falling_item_x = random.randint(0, SCREEN_WIDTH - FALLING_ITEM_SIZE)
falling_item_y = -FALLING_ITEM_SIZE
falling_speed = 5
dincer_alpha = 0
dincer_visible = False
dincer_timer = 0
dragging = False

button_width, button_height = 200, 50
button_hover = False

def reset_game():
    global score, current_basket_size, falling_speed, falling_item_y, falling_item_x, basket_x, dincer_alpha, dincer_visible, dincer_timer, dragging
    score = 0
    current_basket_size = BASKET_SIZE
    falling_speed = 5
    falling_item_y = -FALLING_ITEM_SIZE
    falling_item_x = random.randint(0, SCREEN_WIDTH - FALLING_ITEM_SIZE)
    basket_x = SCREEN_WIDTH // 2
    dincer_alpha = 0
    dincer_visible = False
    dincer_timer = 0
    dragging = False

def game_over_screen():
    global button_hover
    fade_music('down', target_volume=0)
    game_over = True
    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2, button_width, button_height)

    while game_over:
        mouse_pos = pygame.mouse.get_pos()
        button_hover = button_rect.collidepoint(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and button_hover:
                reset_game()
                fade_music('up', target_volume=0.5)
                game_over = False

        screen.fill(GRAY)
        game_over_text = font.render("Game Over: You didn't catch Mr. Cornish!", True, BLACK)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(game_over_text, game_over_rect)

        if button_hover:
            inflated_rect = button_rect.inflate(10, 10)
        else:
            inflated_rect = button_rect

        pygame.draw.rect(screen, WHITE, inflated_rect, border_radius=5)
        try_again_text = button_font.render("Try Again", True, BLACK)
        try_again_rect = try_again_text.get_rect(center=inflated_rect.center)
        screen.blit(try_again_text, try_again_rect)

        pygame.display.update()

def fade_music(direction, step=0.05, target_volume=0.5):
    current_volume = pygame.mixer.music.get_volume()
    while direction == 'down' and current_volume > target_volume:
        current_volume = max(target_volume, current_volume - step)
        pygame.mixer.music.set_volume(current_volume)
        pygame.time.delay(100)
    while direction == 'up' and current_volume < target_volume:
        current_volume = min(target_volume, current_volume + step)
        pygame.mixer.music.set_volume(current_volume)
        pygame.time.delay(100)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    if dincer_visible:
        dincer_img.set_alpha(dincer_alpha)
        screen.blit(dincer_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if basket_rect.collidepoint(event.pos):
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            basket_x, _ = event.pos
            basket_rect.centerx = basket_x

    basket_rect.clamp_ip(screen.get_rect())

    falling_item_y += falling_speed
    falling_speed += FALLING_SPEED_INCREMENT

    if falling_item_y > SCREEN_HEIGHT:
        game_over_screen()

    if (falling_item_y + FALLING_ITEM_SIZE > SCREEN_HEIGHT - BASKET_SIZE and
        basket_rect.left < falling_item_x + FALLING_ITEM_SIZE / 2 < basket_rect.right):
        score += 1
        if score > high_score:
            high_score = score
        if score % 10 == 0 and not dincer_visible:
            violin_sound.play()
            dincer_visible = True
            dincer_timer = pygame.time.get_ticks()
        falling_item_y = -FALLING_ITEM_SIZE
        falling_speed = 5
        falling_item_x = random.randint(0, SCREEN_WIDTH - FALLING_ITEM_SIZE)

    if dincer_visible:
        current_time = pygame.time.get_ticks()
        if current_time - dincer_timer < 3000:
            dincer_alpha = min(255, dincer_alpha + 5)
        elif current_time - dincer_timer < 6000:
            dincer_alpha = max(0, dincer_alpha - 5)
        else:
            dincer_visible = False

    screen.blit(basket_img, basket_rect.topleft)
    screen.blit(cornish_img, (falling_item_x, falling_item_y))

    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (20, 10))

    high_score_text = font.render(f'High Score: {high_score}', True, BLACK)
    screen.blit(high_score_text, (20, score_text.get_height() + 15))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
