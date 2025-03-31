# Arden Boettcher
# Insert date here
# Insert title here

import pygame as pg
from random import randint
from math import radians, cos, sin

# Screen size constants
WIDTH = 500
HEIGHT = 500

# Framerate
FPS = 60

# Color Constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)




# Outline

def outline(rect, weight = 2):
  outrect = pg.Rect(rect.x - weight, rect.y - weight, rect.width + weight * 2, rect.height + weight * 2)
  # pg.draw.rect(surface, color, outrect)
  return outrect


# Rainbow

def rainbow(color: list[int], step = 1):
  hsva = pg.color.Color(color)
  try:
    hsva.hsva = (hsva.hsva[0] + step, hsva.hsva[1], hsva.hsva[2], hsva.hsva[3])
  except ValueError:
    hsva.hsva = (hsva.hsva[0] - 360 + step, hsva.hsva[1], hsva.hsva[2], hsva.hsva[3])
  rgb = (hsva.r,  hsva.g, hsva.b)
  return rgb


# Random Vector

def rand_vector(min_angle = 0, max_angle = 360):
  angle = radians(randint(min_angle, max_angle))
  x = cos(angle)
  y = sin(angle)
  return pg.math.Vector2(x, y)


# Draw Text

def draw_text(surface: pg.Surface, words: str, font: pg.font.Font, pos: tuple, color: tuple, center: tuple = None, antialias = True):
  text = font.render(words, antialias, color)
  if center:
    pos = text.get_rect(center=center)
  surface.blit(text, pos)