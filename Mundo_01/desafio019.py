import pygame

pygame.init()
pygame.mixer.init()  # Inicializa o mixer

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()
pygame.event.wait()