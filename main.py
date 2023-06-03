# Импорти
import pygame 
import sys
import random
import time

# Запуск гри
pygame.init()

# Кадри за секунду
c = pygame.time.Clock()

# Розміри вікна
width = 900
height = 600

# Відкриття гри
screen = pygame.display.set_mode((width, height))

# Ікона та назва
pygame.display.set_caption("Ping Pong Game")

# Ігровий прямокутник
ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30, )
player1 = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
player2 = pygame.Rect(10, height / 2 - 70, 10, 140)

# Зміни
ball_speedx = 6 * random.choice((1, -1))
ball_speedy = 6 * random.choice((1, -1))
player1_speed = 0
player2_speed = 6
player1_score = 0
player2_score = 0


pygame.mixer.init()
Udar = pygame.mixer.Sound('Udar1.ogg')
Mimo = pygame.mixer.Sound('Mimo2.ogg')

# Мьячик двигаеться
def ball_movement():
    global ball_speedx, ball_speedy, player1_score, player2_score
    ball.x += ball_speedx
    ball.y += ball_speedy

    # Відбивання м'яча
    if ball.top <= 0 or ball.bottom >= height:
        ball_speedy *= -1
    if ball.left <= 0:
        player1_score += 1
        ball_restart()
    if ball.right >= width:
        player2_score += 1
        ball_restart()

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speedx *= -1
        Udar.play()


# Функція на ігрока 1
def player1_movement():
    global player1_speed
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= height:
        player1.bottom = height


# Функція на ігрока 2
def player2_movement():
    global player2_speed
    if player2.top < ball.y:
        player2.top += player2_speed
    if player2.bottom > ball.y:
        player2.bottom -= player2_speed
    if player2.top <= 0:
        player2_top = 0
    if player2.bottom >= height:
        player2.bottom = height


# Ресет м'яча на свою позицію
def ball_restart():
    global ball_speedx, ball_speedy
    ball.center = (width / 2, height / 2)
    ball_speedy *= random.choice((1, -1))
    ball_speedx *= random.choice((1, -1))
    Mimo.play()


# Зміна шрифта
font = pygame.font.SysFont("calibri", 25)

# Цикл Гри
while True:
    for event in pygame.event.get():
        # Вихід з гри
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Ігрок 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 8
            if event.key == pygame.K_UP:
                player1_speed -= 8
        # checking for key released event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 8
            if event.key == pygame.K_UP:
                player1_speed += 8

    # Функція
    ball_movement()
    player1_movement()
    player2_movement()


    # Наданя балів
    if ball.x < 0:
        player1_score += 1
    elif ball.x > width:
        player2_score += 1

        

    # Візуалізація
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (220, 220, 220), player1)
    pygame.draw.rect(screen, (220, 220, 220), player2)
    pygame.draw.ellipse(screen, (220, 220, 220), ball)
    pygame.draw.aaline(screen, (220, 220, 220), (width / 2, 0), (width / 2, height))

    # Дрокує Бали
    player1_text = font.render("Бали:" + str(player1_score), False, (255, 255, 255))
    screen.blit(player1_text, [600, 50])
    player2_text = font.render("Бали:" + str(player2_score), False, (255, 255, 255))
    screen.blit(player2_text, [300, 50])

    # Обновлення картинки
    pygame.display.update()

    # ФПС
    c.tick(60)