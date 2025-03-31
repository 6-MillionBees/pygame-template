# Arden Boettcher
# Insert date here
# Insert title here

import pygame as pg
import sys
import config as c
from ship import Ship
pg.init()

class Main:
  def __init__(self):
    # Window
    self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
    pg.display.set_caption("PLACEHOLDER")

    # Clock
    self.clock = pg.time.Clock()

    # Ship
    self.ship = Ship([c.WIDTH / 2, c.HEIGHT / 2], c.RED)


  def run(self):
    # The bool for the main loop
    self.running = True

    dt = 0
    # Main loop
    while self.running:

      # Call events / update running
      self.main_events()

      self.ship.update(dt)

      # Fills window
      self.screen.fill(c.WHITE)

      self.ship.draw(self.screen)

      # Updates the Display
      pg.display.flip()

      # Limits the framerate
      dt = self.clock.tick(c.FPS) / 1000

    # Close everything
    self.quit()

  # Event Handling
  def main_events(self):
    for event in pg.event.get():
      # Quits the game when you press the x
      if event.type == pg.QUIT:
        self.running = False

  # Exits the code
  def quit(self):
    pg.quit()
    sys.exit()


if __name__ == "__main__":
  main = Main()
  main.run()
