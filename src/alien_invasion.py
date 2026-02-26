import sys
import pygame

class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""
    def __init__(self):
        """Construtor da classe Inicializa o jogo e cria os recursos do jogo."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        