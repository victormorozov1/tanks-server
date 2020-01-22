import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, id, picture, x, y, group):
        super().__init__(group)
        self.id = id
        self.image = picture
        self.pictures = {'down': picture,
                         'up': pygame.transform.rotate(picture, 180),
                         'left': pygame.transform.rotate(picture, -90),
                         'right': pygame.transform.rotate(picture, 90)}
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def turn(self, direction):
        self.image = self.pictures[direction]
        print('rotated', direction)
