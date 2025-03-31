# Arden Boettcher
# PLACEHOLDER
# Ship Class

import pygame as pg


class Ship:
  def __init__(self, pos, color):
    self.pos = pos
    self.color = color
    self.destination = pg.mouse.get_pos()

  def update(self, dt):
    self.update_dest()
    self.move(dt)

  def update_dest(self):
    self.destination = pg.mouse.get_pos()
    difference = [self.destination[0] - self.pos[0], self.destination[1] - self.pos[1]]
    self.vector = pg.math.Vector2(difference)

  def move(self, dt):
    self.pos += self.vector * dt * 10

  def draw(self, surface):
    pg.draw.rect(surface, self.color, pg.Rect(self.pos, (10, 10)))