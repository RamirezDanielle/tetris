import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_UP, K_p, K_s
from game import Game
from colors import Colors

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("01 Never Gonna Give You Up.mp3")

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
pause_surface = title_font.render("PAUSED", True, Colors.white)
start_surface = title_font.render("PRESS 'S'", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

pause_rect = pygame.Rect(350, 580, 150, 30)
start_rect = pygame.Rect(350, 580, 150, 30)



screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")


clock = pygame.time.Clock()
game = Game()
paused = False
started = False
game_over_music_played = False

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if started:  
                    paused = not paused
                    if paused:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                if not started:
                    started = True
                    pygame.mixer.music.stop()  
            elif game.game_over == True and event.key == pygame.K_RETURN:
                game.game_over = False
                game.reset()
                pygame.mixer.music.stop()  # Stop the music when the game is reloaded
                game_over_music_played = False 
        if not paused and started:
            if event.type == KEYDOWN:
                if event.key == K_LEFT and not game.game_over:
                    game.move_left()
                elif event.key == K_RIGHT and not game.game_over:
                    game.move_right()
                elif event.key == K_DOWN and not game.game_over:
                    game.move_down()
                    game.update_score(0, 1)
                elif event.key == K_UP and not game.game_over:
                    game.rotate()

            if event.type == GAME_UPDATE and not game.game_over:
                game.move_down()

    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.black)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))  
        if not game_over_music_played:
            pygame.mixer.music.play()  # Play the music when the game is over
            game_over_music_played = True
    elif paused:
        screen.blit(pause_surface, (350, 580, 150, 30))
    elif not started:
        screen.blit(start_surface, start_rect)
    
    pygame.draw.rect(screen, Colors.white, score_rect, 1)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.white, next_rect, 1)

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

