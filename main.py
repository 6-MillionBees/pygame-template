# Arden Boettcher
# Insert date here
# Insert title here

import pygame
import config
pygame.init()


# Setting up the window
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("PLACEHOLDER")

# Setting up the clock
clock = pygame.time.Clock()

# Event handling
def main_events():
  for event in pygame.event.get():
    # Quits the game when you press the x
    if event.type == pygame.QUIT:
      return False
  return True



# Main loop
def main():
  # The bool for the main loop
  running = True
  
  while running:

    # Call events / update running
    running = main_events()

    # Fills window
    screen.fill(config.WHITE)

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate
    clock.tick(config.FPS)

  # Close the pygame modules
  pygame.quit()


# Calls the code
if __name__ == "__main__":
  main()
