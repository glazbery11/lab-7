import pygame
import os

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

playlist = ["1.mp3", "2.mp3", "3.mp3"]
track_names = ["FE!N", "CARNIVAL", "Дом"]
current_track = 0
paused = False

font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def play_music():
    global paused
    if not os.path.exists(playlist[current_track]):
        print(f"Файл {playlist[current_track]} не найден!")
        return
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.load(playlist[current_track])
        pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

running = True
while running:
    screen.fill((0, 0, 0))  

    draw_text("Music Player", 180, 30, (255, 215, 0))
    draw_text("Controls:", 20, 100)
    draw_text("P - Play/Pause", 20, 130)
    draw_text("S - Stop", 20, 160)
    draw_text("N - Next", 20, 190)
    draw_text("B - Previous", 20, 220)
    draw_text(f"Now Playing: {track_names[current_track]}", 20, 300, (0, 255, 0))

    pygame.display.flip()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()
    
pygame.quit()
