import pygame
import random

negro = (0, 0, 0)
azul = (0, 0, 255)
rojo = (255, 0, 0)
blanco = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((500, 500))

game_area = pygame.Rect(50, 50, 400, 400)

font = pygame.font.Font(None, 30)
font_title = pygame.font.Font(None, 70)
font_signature = pygame.font.Font(None, 10)
fps = pygame.time.Clock()

def food(snake_body):
    random_pos = random.randint(0, 39) * 10
    food_pos = [random_pos + 50, random_pos + 50]
    if food_pos in snake_body:
        return food(snake_body)
    else:
        return food_pos
    
def game():
    pass

def start_game(bool = False):

    title_snake_pos = [100, 150]
    title_snake_body = [[100, 150], [90, 150], [80, 150]]
    title_change = "RIGHT"
    title_run = True

    while title_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:                    
                    title_run = False
                    game()

        if title_change == "RIGHT":
            title_snake_pos[0] += 10
            if title_snake_pos[0] == 400:               
                title_snake_pos[0] = 100
        title_snake_body.insert(0, list(title_snake_pos))
        title_snake_body.pop()

        screen.fill(negro)
        pygame.draw.rect(screen, azul, pygame.Rect(40, 40, 420, 420), 10)
        title = font_title.render("SNAKE", True, rojo)
        title_rect = title.get_rect(center=(250, 100))
        screen.blit(title, title_rect)  
        signature = font_signature.render("by Sanchez De Bock", True, azul)
        signature_rect = signature.get_rect(center=(300, 120))
        screen.blit(signature, signature_rect)
        you_lose = bool
        if you_lose:
            you_lose_text = font.render("GAME OVER", True, rojo)
            you_lose_rect = you_lose_text.get_rect(center=(250, 200))
            screen.blit(you_lose_text, you_lose_rect)

        text = font.render("PRECIONA ESPACIO PARA INICIAR", True, rojo)
        text_rect = text.get_rect(center=(250, 350))
        screen.blit(text, text_rect)
        text2 = font.render("ESCAPE PARA SALIR", True, rojo)
        text2_rect = text2.get_rect(center=(250, 400))
        screen.blit(text2, text2_rect)

        for pos in title_snake_body:
            pygame.draw.rect(screen, blanco, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.display.flip()

        pygame.time.Clock().tick(10)  

def game():
    for i in range(3,0,-1):
        screen.fill(negro)
        pygame.draw.rect(screen, azul, pygame.Rect(40, 40, 420, 420), 10)
        text = font.render(str(i), 0, rojo)
        screen.blit(text, (250, 250))
        pygame.display.flip()
        pygame.time.delay(1000)

    snake_pos = [150, 100]
    snake_body = [[150, 100], [140, 100], [130, 100]]
    change = "RIGHT"
    run = True
    food_pos = food(snake_body)
    score = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and change != "LEFT":
                    change = "RIGHT"
                elif event.key == pygame.K_LEFT and change != "RIGHT":
                    change = "LEFT"
                elif event.key == pygame.K_UP and change != "DOWN":
                    change = "UP"
                elif event.key == pygame.K_DOWN and change != "UP":
                    change = "DOWN"

        if change == "RIGHT":
            snake_pos[0] += 10
        if change == "LEFT":
            snake_pos[0] -= 10
        if change == "UP":
            snake_pos[1] -= 10
        if change == "DOWN":
            snake_pos[1] += 10

        snake_body.insert(0, list(snake_pos))

        if snake_pos == food_pos:
            food_pos = food(snake_body)
            score += 1
            print(score)
        else:
            snake_body.pop()

        head = snake_body[-1]
        for i in range(len(snake_body) - 1):
            part = snake_body[i]
            if head[0] == part[0] and head[1] == part[1]:
                run = False
                print("YOU LOSE")

        screen.fill(negro)
        pygame.draw.rect(screen, azul, pygame.Rect(40, 40, 420, 420), 10)

        for pos in snake_body:
            pygame.draw.rect(screen, blanco, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(screen, rojo, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        score_text = font.render(str(score), 0, rojo)
        score_text_rect = score_text.get_rect(center=(250, 30))
        screen.blit(score_text, score_text_rect)

        if score < 10:
            fps.tick(10)
        if score >= 10:
            fps.tick(20)

        if snake_pos[0] < game_area.left or snake_pos[0] >= game_area.right:
            run = False
            print("YOU LOSE")
        if snake_pos[1] < game_area.top or snake_pos[1] >= game_area.bottom:
            run = False
            print("YOU LOSE")

        pygame.display.flip()

    start_game(True)

start_game()