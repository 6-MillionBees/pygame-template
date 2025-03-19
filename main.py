# Arden Boettcher
# Insert date here
# Insert title here

import pygame as pg
import sys
import config as c
pg.init()

class Main:
  def __init__(self):
    # Window
    self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
    pg.display.set_caption("PLACEHOLDER")

    # Clock
    self.clock = pg.time.Clock()

  def run(self):
    # The bool for the main loop
    self.running = True

    # Main loop
    while self.running:

      # Call events / update running
      self.main_events()

      # Fills window
      self.screen.fill(c.WHITE)

      # Updates the Display
      pg.display.flip()

      # Limits the framerate
      self.clock.tick(c.FPS)

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
