import pygame, Game.controls
from Game.gun import Gun
from pygame.sprite import Group
from Game.stats import Stats
from Game.scores import Scores



def run():
    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("Space invaders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    Game.controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)


    while True:
        Game.controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            Game.controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            Game.controls.update_bullets(screen, stats, sc, inos, bullets)
            Game.controls.update_inos(stats, screen, sc, gun, inos, bullets)

run()
