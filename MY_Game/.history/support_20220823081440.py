from os import walk
import pygame
def import_folder(path):
    surface_list = []

    for folder in walk(path):
        print(folder)

    return surface_list


    