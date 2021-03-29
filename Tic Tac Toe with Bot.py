import pygame
import random

pygame.init()

#Window size
Window = pygame.display.set_mode((480, 520))
screen_height = 540
screen_width = 480
pygame.display.set_caption('Tic Tac Toe')

#Color values & font
Blue = (103, 199, 188)
Darkblue = (0, 139, 139)
Black = (0, 0 ,0)
White = (255, 255, 255)
Window.fill(Darkblue)
font = pygame.font.SysFont("Arial.ttf", 200, bold=False, italic=False)
font2 = pygame.font.SysFont("Arial.ttf", 35, bold=False, italic=False)

#X's and O's
X = font.render("X", True, Black)
draw_object = 'x'

def circle1():
    global clickable1
    pygame.draw.circle(Window, White, (76, 76), 58, 58)
    pygame.draw.circle(Window, Blue, (76, 76), 38, 38)
    tictactoeboard[0][0] = 2
    clickable1 = False
def circle2():
    global clickable2
    pygame.draw.circle(Window, White, (240, 76), 58, 58)
    pygame.draw.circle(Window, Blue, (240, 76), 38, 38)
    tictactoeboard[0][1] = 2
    clickable2 = False
def circle3():
    global clickable3
    pygame.draw.circle(Window, White, (404, 76), 58, 58)
    pygame.draw.circle(Window, Blue, (404, 76), 38, 38)
    tictactoeboard[0][2] = 2
    clickable3 = False
def circle4():
    global clickable4
    pygame.draw.circle(Window, White, (76, 240), 58, 58)
    pygame.draw.circle(Window, Blue, (76, 240), 38, 38)
    tictactoeboard[1][0] = 2
    clickable4 = False
def circle5():
    global clickable5
    pygame.draw.circle(Window, White, (240, 240), 58, 58)
    pygame.draw.circle(Window, Blue, (240, 240), 38, 38)
    tictactoeboard[1][1] = 2
    clickable5 = False
def circle6():
    global clickable6
    pygame.draw.circle(Window, White, (404, 240), 58, 58)
    pygame.draw.circle(Window, Blue, (404, 240), 38, 38)
    tictactoeboard[1][2] = 2
    clickable6 = False
def circle7():
    global clickable7
    pygame.draw.circle(Window, White, (76, 404), 58, 58)
    pygame.draw.circle(Window, Blue, (76, 404), 38, 38)
    tictactoeboard[2][0] = 2
    clickable7 = False
def circle8():
    global clickable8
    pygame.draw.circle(Window, White, (240, 404), 58, 58)
    pygame.draw.circle(Window, Blue, (240, 404), 38, 38)
    tictactoeboard[2][1] = 2
    clickable8 = False
def circle9():
    global clickable9
    pygame.draw.circle(Window, White, (404, 404), 58, 58)
    pygame.draw.circle(Window, Blue, (404, 404), 38, 38)
    tictactoeboard[2][2] = 2
    clickable9 = False

circles = [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9]

#Touch squares
Square1 = pygame.draw.rect(Window, Blue, (0, 0, 152, 152))
Square2 = pygame.draw.rect(Window, Blue, (164, 0, 152, 152))
Square3 = pygame.draw.rect(Window, Blue, (328, 0, 152, 152))
Square4 = pygame.draw.rect(Window, Blue, (0, 164, 152, 152))
Square5 = pygame.draw.rect(Window, Blue, (164, 164, 152, 152))
Square6 = pygame.draw.rect(Window, Blue, (328, 164, 152, 152))
Square7 = pygame.draw.rect(Window, Blue, (0, 328, 152, 152))
Square8 = pygame.draw.rect(Window, Blue, (164, 328, 152, 152))
Square9 = pygame.draw.rect(Window, Blue, (328, 328, 152, 152))

#Miscellanious
clickable1 = True
clickable2 = True
clickable3 = True
clickable4 = True
clickable5 = True
clickable6 = True
clickable7 = True
clickable8 = True
clickable9 = True

clickables = [clickable1, clickable2, clickable3, clickable4, clickable5, clickable6, clickable7, clickable8, clickable9]

#Screen text:
def Screenmessage(msg, color):
    screentext = font2.render(msg, True, White)
    Window.blit(screentext, (50, 490))

#Board [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tictactoeboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def Winner1(num):
    for row in tictactoeboard:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in tictactoeboard:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True

    #[0, 0], [1, 1], [2, 2]
    for tile in range(3):
        if tictactoeboard[tile][tile] == num:
            continue
        else:
            break
    else:
        return True

    #[2, 0], [1, 1], [2, 0]
    for tile in range(3):
        if tictactoeboard[tile][2-tile] == num:
            continue
        else:
            break
    else:
        return True

Run = True
winner = False

while Run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                clickable1 = True
                clickable2 = True
                clickable3 = True
                clickable4 = True
                clickable5 = True
                clickable6 = True
                clickable7 = True
                clickable8 = True
                clickable9 = True
                winner = False
                tictactoeboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos() #Position
            if winner != True:
                if Square1.collidepoint(pos) and clickable1: #If top-left square gets clicked
                    Window.blit(X, (30, 20))
                    draw_object = 'circle'
                    tictactoeboard[0][0] = 1
                    clickable1 = False
                    circles.remove(circle1)


                if Square2.collidepoint(pos) and clickable2: #If top-mid square gets clicked
                    Window.blit(X, (194, 20))
                    draw_object = 'circle'
                    tictactoeboard[0][1] = 1
                    clickable2 = False
                    circles.remove(circle2)


                if Square3.collidepoint(pos) and clickable3: #If top-right square gets clicked
                    Window.blit(X, (358, 20))
                    draw_object = 'circle'
                    tictactoeboard[0][2] = 1
                    clickable3 = False
                    circles.remove(circle3)


                if Square4.collidepoint(pos) and clickable4: #If center-left square gets clicked
                    Window.blit(X, (30, 184))
                    draw_object = 'circle'
                    tictactoeboard[1][0] = 1
                    clickable4 = False
                    circles.remove(circle4)


                if Square5.collidepoint(pos) and clickable5: #If middle square gets clicked
                    Window.blit(X, (194, 184))
                    draw_object = 'circle'
                    tictactoeboard[1][1] = 1
                    clickable5 = False
                    circles.remove(circle5)

                if Square6.collidepoint(pos) and clickable6: #If center-right square gets clicked
                    Window.blit(X, (358, 184))
                    draw_object = 'circle'
                    tictactoeboard[1][2] = 1
                    clickable6 = False
                    circles.remove(circle6)


                if Square7.collidepoint(pos) and clickable7: #If bottom-left square gets clicked
                    Window.blit(X, (30, 348))
                    draw_object = 'circle'
                    tictactoeboard[2][0] = 1
                    clickable7 = False
                    circles.remove(circle7)


                if Square8.collidepoint(pos) and clickable8: #If bottom-mid square gets clicked
                    Window.blit(X, (194, 348))
                    draw_object = 'circle'
                    tictactoeboard[2][1] = 1
                    clickable8 = False
                    circles.remove(circle8)


                if Square9.collidepoint(pos) and clickable9: #If bottom-right square gets clicked
                    Window.blit(X, (358, 348))
                    draw_object = 'circle'
                    tictactoeboard[2][2] = 1
                    clickable9 = False
                    circles.remove(circle9)

                #Bot's turn
                if clickable1 or clickable2 or clickable3 or clickable4 or clickable5 or clickable6\
                    or clickable7 or clickable8 or clickable9 == False:
                    random.choice(circles)()


        if Winner1(1):
            winner = True
        if Winner1(2):
            winner = True

    pygame.display.update()
pygame.quit()