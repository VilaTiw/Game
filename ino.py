import pygame

class Ino(pygame.sprite.Sprite):
    """клас інопланетянина"""

    def init(self, screen):
        """ініціалізація і початкова позиція"""
        super(Ino, self).init()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вивід інопланетянина на екран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """переміщення інопланетянина"""
        self.y += 0.1
        self.rect.y = self.y