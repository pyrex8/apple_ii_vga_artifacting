#!/usr/bin/env python3
"""
Apple II HIRES Color palette
"""

import os
import time
import pygame
import pygame.sndarray
import pygame.surfarray
import numpy
import sys
import serial

# Resistors from schematic image
R3 = 330 # R3 = R4 = R5
R6 = 680 # R6 = R7 = R8

C0 = 0x00
C1 = int((0xFF * R3) / (R3 + R6))
C2 = int((0xFF * R6) / (R3 + R6))
C3 = 0xFF

PIXELS_X = 100
PIXELS_Y = 100
SCREEN_SCALE = 4
SCREEN_X = PIXELS_X * SCREEN_SCALE
SCREEN_Y = PIXELS_Y * SCREEN_SCALE
CHAR_X = 7 * SCREEN_SCALE
CHAR_Y = 8 * SCREEN_SCALE
SCREEN_X_TOTAL = SCREEN_X
SCREEN_Y_TOTAL = SCREEN_Y

# Apple II colors from https://en.wikipedia.org/wiki/Apple_II_graphics
BLACK  = 0x000000
GREEN  = 0x43C300
PURPLE = 0xB63DFF
ORANGE = 0xEA5D15
BLUE   = 0x10A4E3
WHITE  = 0xFFFFFF

# Artifact colors
G_ART    = (C1<<16) + (C2<<8) + C0
P_ART    = (C1<<16) + (C0<<8) + C2
O_ART    = (C2<<16) + (C1<<8) + C0
B_ART    = (C1<<16) + (C2<<8) + C3
UNUSED_1 = (C3<<16) + (C1<<8) + C2
UNUSED_2 = (C2<<16) + (C3<<8) + C1

APPLE_II_HIRES   = [BLACK, GREEN, PURPLE, ORANGE,  BLUE, WHITE]
#  3 bit RGB value [  000,   010,    001,    100,   011,   111,      101,      110]
APPLE_II_VGA_ART = [BLACK, G_ART,  P_ART,  O_ART, B_ART, WHITE, UNUSED_1, UNUSED_2]

pygame.init()
pygame.display.set_caption('Apple II HIRES pallet')
pygame.font.init()
screen = pygame.display.set_mode([SCREEN_X_TOTAL, SCREEN_Y_TOTAL])
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Comic Sans MS', 25)

running = True

T = 30
L = 120
H = 70
V = 40
S = 20
G = 4

while running:

    keycode = 0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_X_TOTAL, SCREEN_Y_TOTAL))

    for i in range(len(APPLE_II_HIRES)):
        if APPLE_II_HIRES[i] == 0:
            pygame.draw.rect(screen, WHITE, (L, T + i * (V + G), H, V), width=1)
        else:
            pygame.draw.rect(screen, APPLE_II_HIRES[i], (L, T + i * (V + G), H, V))

    for i in range(len(APPLE_II_VGA_ART)):
        if APPLE_II_VGA_ART[i] == 0:
            pygame.draw.rect(screen, WHITE, (L + 1 * (H + S), T + i * (V + G), H, V), width=1)
        else:
            pygame.draw.rect(screen, APPLE_II_VGA_ART[i], (L + 1 * (H + S), T + i * (V + G), H, V))

    textsurface = myfont.render('                      24bit RGB   3bit Artifacting', False, (255,255,255))
    screen.blit(textsurface,(0,5))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
