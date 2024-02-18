import pygame
pygame.font.init()
Window = pygame.display.set_mode((500,500))
pygame.display.set_caption("SUDOKU")
x = 0
z = 0
diff = 500 / 9
value = 0
defaultgrid =[
        [0, 0, 4, 0, 6, 0, 0, 0, 5],
        [7, 8, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 2, 6, 0, 1, 0, 7, 8],
        [6, 1, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 7, 5, 4, 0, 0, 6, 1],
        [0, 0, 1, 7, 5, 0, 9, 3, 0],
        [0, 7, 0, 3, 0, 0, 0, 1, 0],
        [0, 4, 0, 2, 0, 6, 0, 0, 7],
        [0, 2, 0, 0, 0, 7, 4, 0, 0],
    ]

font = pygame.font.SysFont("comicsans",40)
font1 = pygame.font.SysFont("comicsans",20)

# Timer variables
start_time = None
current_time = None
elapsed_time = None

def start_timer():
    global start_time
    start_time = pygame.time.get_ticks()

def stop_timer():
    global elapsed_time
    elapsed_time = pygame.time.get_ticks() - start_time

def format_time(milliseconds):
    seconds = milliseconds // 1000
    minutes = seconds // 60
    seconds %= 60
    milliseconds %= 1000
    return "{:02}:{:02}.{:03}".format(minutes, seconds, milliseconds)

def cord(pos):
    global x
    x = pos[0] // diff
    global z
    z = pos[1] // diff

def highlightbox():
    for k in range(2):
        pygame.draw.line(Window, (0, 0, 0), (x * diff - 3, (z + k) * diff), (x * diff + diff + 3, (z + k) * diff), 7)
        pygame.draw.line(Window, (0, 0, 0), ((x + k) * diff, z * diff), ((x + k) * diff, z * diff + diff), 7)

def drawlines():
    for i in range(9):
        for j in range(9):
            if defaultgrid[i][j] != 0:
                pygame.draw.rect(Window, (255, 255, 0), (i * diff, j * diff, diff, diff))
                text1 = font.render(str(defaultgrid[i][j]), 1, (0, 0, 0))
                text_rect = text1.get_rect(center=(i * diff + diff / 2, j * diff + diff / 2))  # Centering the text
                Window.blit(text1, text_rect)
    for l in range(10):
        if l % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(Window, (0, 0, 0), (0, l * diff), (500, l * diff), thick)
        pygame.draw.line(Window, (0, 0, 0), (l * diff, 0), (l * diff, 500), thick)


def raise_error():
    text1 = font.render("Wrong!", 1, (0, 0, 0))
    Window.blit(text1, (20, 570))

def raise_error1():
    text1 = font.render("Wrong! Enter a valid key for the game", 1, (0, 0, 0))
    Window.blit(text1, (20, 570))

def validvalue(m, k, l, value):
    for it in range(9):
        if m[k][it] == value:
            return False
        if m[it][l] == value:
            return False
    it = k // 3
    jt = l // 3
    for k in range(it * 3, it * 3 + 3):
        for l in range(jt * 3, jt * 3 + 3):
            if m[k][l] == value:
                return False
    return True

def solve_game(m, i, j):
    while m[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    for it in range(1, 10):
        if validvalue(m, i, j, it):
            m[i][j] = it
            if solve_game(m, i, j):
                return True
            else:
                m[i][j] = 0
    return False

def game_result():
    stop_timer()  # Stop the timer when the game is finished
    text1 = font.render("Game Finished", 1, (0, 0, 0))
    Window.blit(text1, (20, 570))
    time_str = format_time(elapsed_time)
    score_text = font.render("Time: {}".format(time_str), 1, (0, 0, 0))
    Window.blit(score_text, (20, 610))

flag = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

start_timer()  # Start the timer when the game starts

while flag:
    Window.fill((255, 182, 193))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                value = 1
            if event.key == pygame.K_2:
                value = 2
            if event.key == pygame.K_3:
                value = 3
            if event.key == pygame.K_4:
                value = 4
            if event.key == pygame.K_5:
                value = 5
            if event.key == pygame.K_6:
                value = 6
            if event.key == pygame.K_7:
                value = 7
            if event.key == pygame.K_8:
                value = 8
            if event.key == pygame.K_9:
                value = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                start_timer()  # Restart the timer when the game restarts
                defaultgrid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                start_timer()  # Restart the timer when the game restarts
                defaultgrid = [
                    [0, 0, 4, 0, 6, 0, 0, 0, 5],
                    [7, 8, 0, 4, 0, 0, 0, 2, 0],
                    [0, 0, 2, 6, 0, 1, 0, 7, 8],
                    [6, 1, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 7, 5, 4, 0, 0, 6, 1],
                    [0, 0, 1, 7, 5, 0, 9, 3, 0],
                    [0, 7, 0, 3, 0, 0, 0, 1, 0],
                    [0, 4, 0, 2, 0, 6, 0, 0, 7],
                    [0, 2, 0, 0, 0, 7, 4, 0, 0],
                ]
    if flag2 == 1:
        if solve_game(defaultgrid, 0, 0) == False:
            error = 1
        else:
            rs = 1
        flag2 = 0
    if value != 0:
        if validvalue(defaultgrid, int(x), int(z), value):
            defaultgrid[int(x)][int(z)] = value
            flag1 = 0
        else:
            defaultgrid[int(x)][int(z)] = 0
            raise_error1()
        value = 0

    if error == 1:
        raise_error()
    if rs == 1:
        game_result()
    drawlines()
    if flag1 == 1:
        highlightbox()
    current_time = pygame.time.get_ticks() - start_time
    time_str = format_time(current_time)
    score_text = font1.render("Time: {}".format(time_str), 1, (0, 0, 0))
    Window.blit(score_text, (20, 540))
    pygame.display.update()

pygame.quit()
