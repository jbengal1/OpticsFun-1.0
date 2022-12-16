import pygame, sys
from pygame.locals import *
from settings import *
from sim1 import Sim1
from sim2 import Sim2

SIM_NUM = 1
if len(sys.argv) > 1:
    SIM_NUM = int(sys.argv[1])

class OpticSimulation:
    def __init__(self):
        
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()

        # Set the simulation I want to run
        
        if SIM_NUM == 1:
            self.sim = Sim1()
        elif SIM_NUM == 2:
            self.sim = Sim2()
        else:
            self.sim = None

    def run(self):
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (pygame.key.get_pressed()[K_x]):
                    pygame.quit()
                    sys.exit()
            
            
            self.screen.fill('black')
            # run
            if self.sim is not None:
                self.sim.run()
                pygame.display.update()
                self.clock.tick(FPS)
            
            else:
                print("No simulation was selected. Give an input number (currently 1 or 2).")
                print("1: Free laser simulation. Controled by mouse.")
                print("2: Scripted laser simulation, determined by given range of angles.")


if __name__ == "__main__":
    optic_sim = OpticSimulation()
    optic_sim.run()
