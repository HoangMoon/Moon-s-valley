import pygame
from settings import *

class Overlay:
    def __init__(self, player):
        # General setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # imports
        Overlay_path = './graphics/overlay/'
        self.tools_surf = {tool: pygame.image.load(f'{Overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
        self.seeds_surf = {seed: pygame.image.load(f'{Overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}
        
    def display(self):
        #tool
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_react = tool_surf.get_rect(midbottom = OVERLAY_POSITION['tool'])
        self.display_surface.blit(tool_surf,(0, 0))

        

        #seed