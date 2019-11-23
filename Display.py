import pygame
import math
from Screen import *

class Display():
        def __init__(self, width, height):
                pygame.init()
                self.width = width
                self.height = height
                self.display = pygame.display.set_mode((width,height))
                pygame.display.set_caption("Title")
                self.clock = pygame.time.Clock()
                self.running = True 
                self.screen = Screen(256, 256, self.width, self.height, 50)
                self.t = 0
                self.n = 1

        def run(self):
                while self.running:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        self.running = False
                        self.tick()
                        self.render()
                        pygame.display.flip()
                        self.clock.tick(60)#set frame rat5

        def tick(self):
                self.t += 1
                self.screen.tick_screen()
                if self.t % (5 * 60 + 30)== 0 and False:
                        self.n += 1
                        self.screen = Screen(256, 256, self.width, self.height, self.n)

        def render(self):
                self.display.fill((255,255,255))
                pixels = pygame.surfarray.array2d(self.display)# 2d array of pixel values
                self.screen.render_screen(pixels)#makes screen class have render fuctions
                pygame.surfarray.blit_array(self.display, pixels)#projects the modified pixels
                
def main():
        screen = Display(612, 612)
        screen.run()

if __name__ == '__main__':
        main()