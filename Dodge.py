import pygame
import sys
import time
import random
import os
import sys
import pickle
import math
from pygame.locals import *

WIDTH, HEIGHT = 1200, 650

pygame.init()
pygame.display.set_caption("Dodge !")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

#############

### Font

normal_font = pygame.font.SysFont("sherif", 40)
title_font = pygame.font.Font(os.path.join("Assets_dodge","Berry Rotunda.ttf"), 60)
bigger_font = pygame.font.Font(os.path.join("Assets_dodge","Berry Rotunda.ttf"), 40)
big_font = pygame.font.Font(os.path.join("Assets_dodge","Berry Rotunda.ttf"), 30)
font = pygame.font.Font(os.path.join("Assets_dodge","Berry Rotunda.ttf"), 20)
small_font = pygame.font.Font(os.path.join("Assets_dodge","Berry Rotunda.ttf"), 15)
button_font = pygame.font.Font(os.path.join("Assets_dodge","Berry Rotunda.ttf"), 10)


### Colors

RED = (255, 0, 0)
DARK_RED = (180, 0, 0)
YELLOW = (255,235,42)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GRAYISH = (150, 150, 150)
DARK_GRAY = (100, 100, 100)
GREEN = (0, 128, 0)
BROWN = (83, 61, 50)


### Rects

# General

# General
BACK_BUTTON_T_LEFT = pygame.Rect(15, 10, 100, 40)
BACK_BUTTON_T_MIDDLE = pygame.Rect(WIDTH//2 - 20, 10, 100, 40)
BACK_BUTTON_T_RIGHT = pygame.Rect(WIDTH - 55, 10, 100, 40)

BACK_BUTTON_B_LEFT = pygame.Rect(15, HEIGHT - 50, 100, 40)
BACK_BUTTON_B_MIDDLE = pygame.Rect(WIDTH//2 - 20, HEIGHT - 50, 100, 40)
BACK_BUTTON_B_RIGHT = pygame.Rect(WIDTH - 115, HEIGHT - 50, 100, 40)

# Main Menu
PLAY_BUTTON = pygame.Rect(WIDTH//2 - 125, HEIGHT//3, 250, 40)
SHOP_BUTTON = pygame.Rect(WIDTH//2 - 125, HEIGHT//3 + 100, 250, 40)
RANKING_BUTTON = pygame.Rect(WIDTH//2 - 125, HEIGHT//3 + 200, 250, 40)
SETTING_BUTTON = pygame.Rect(WIDTH//2 - 125, HEIGHT//3 + 300, 250, 40)
NAME_ENTRY = pygame.Rect(WIDTH//2 - 150, HEIGHT - 45, 300, 40)

# Settings
ST_LEFT_BUTTON = pygame.Rect(75, 200, 100, 50)
ST_LEFT_INPUT_ZONE = pygame.Rect(185, 200, 350, 50)
ST_RIGHT_BUTTON = pygame.Rect(75, 300, 100, 50)
ST_RIGHT_INPUT_ZONE = pygame.Rect(185, 300, 350, 50)
ST_JUMP_BUTTON = pygame.Rect(75, 400, 100, 50)
ST_JUMP_INPUT_ZONE = pygame.Rect(185, 400, 350, 50)
ST_STOMP_BUTTON = pygame.Rect(75, 500, 100, 50)
ST_STOMP_INPUT_ZONE = pygame.Rect(185, 500, 350, 50)
ST_DASH_BUTTON = pygame.Rect(600, 200, 100, 50)
ST_DASH_INPUT_ZONE = pygame.Rect(710, 200, 350, 50)
ST_SPECIAL_BUTTON = pygame.Rect(600, 300, 100, 50)
ST_SPECIAL_INPUT_ZONE = pygame.Rect(710, 300, 350, 50)
ST_RESTART_BUTTON = pygame.Rect(600, 400, 100, 50)
ST_RESTART_INPUT_ZONE = pygame.Rect(710, 400, 350, 50)

ST_AZERTY_QWERTY_BUTTON = pygame.Rect(150, HEIGHT - 70, 150, 50)
ST_RESET_BUTTON = pygame.Rect(525, HEIGHT - 70, 150, 50)
ST_SAVE_BUTTON = pygame.Rect(900, HEIGHT - 70, 150, 50)

# Ranking
RK_JOB1_BUTTON = pygame.Rect(50, 152, 200, 40)
RK_JOB2_BUTTON = pygame.Rect(50, 257, 200, 40)
RK_JOB3_BUTTON = pygame.Rect(50, 364, 200, 40)
RK_JOB4_BUTTON = pygame.Rect(50, 470, 200, 40)

RK_ARROW_UP_BUTTON = pygame.Rect(275, 257, 40, 50)
RK_ARROW_DOWN_BUTTON = pygame.Rect(275, 364, 40, 50)

RK_HEAD_NUMBER = pygame.Rect(350, 122, 50, 40)
RK_COLUMN_NUMBER = pygame.Rect(350, 167, 50, 400)
RK_DIVIDER_NUMBER_1 = pygame.Rect(355, 206, 40, 2)
RK_DIVIDER_NUMBER_2 = pygame.Rect(355, 246, 40, 2)
RK_DIVIDER_NUMBER_3 = pygame.Rect(355, 286, 40, 2)
RK_DIVIDER_NUMBER_4 = pygame.Rect(355, 326, 40, 2)
RK_DIVIDER_NUMBER_5 = pygame.Rect(355, 366, 40, 2)
RK_DIVIDER_NUMBER_6 = pygame.Rect(355, 406, 40, 2)
RK_DIVIDER_NUMBER_7 = pygame.Rect(355, 446, 40, 2)
RK_DIVIDER_NUMBER_8 = pygame.Rect(355, 486, 40, 2)
RK_DIVIDER_NUMBER_9 = pygame.Rect(355, 526, 40, 2)

RK_HEAD_NAME = pygame.Rect(405, 122, 190, 40)
RK_COLUMN_NAME = pygame.Rect(405, 167, 190, 400)
RK_DIVIDER_NAME_1 = pygame.Rect(410, 206, 180, 2)
RK_DIVIDER_NAME_2 = pygame.Rect(410, 246, 180, 2)
RK_DIVIDER_NAME_3 = pygame.Rect(410, 286, 180, 2)
RK_DIVIDER_NAME_4 = pygame.Rect(410, 326, 180, 2)
RK_DIVIDER_NAME_5 = pygame.Rect(410, 366, 180, 2)
RK_DIVIDER_NAME_6 = pygame.Rect(410, 406, 180, 2)
RK_DIVIDER_NAME_7 = pygame.Rect(410, 446, 180, 2)
RK_DIVIDER_NAME_8 = pygame.Rect(410, 486, 180, 2)
RK_DIVIDER_NAME_9 = pygame.Rect(410, 526, 180, 2)

RK_HEAD_TIME = pygame.Rect(600, 122, 170, 40)
RK_COLUMN_TIME = pygame.Rect(600, 167, 170, 400)
RK_DIVIDER_TIME_1 = pygame.Rect(605, 206, 160, 2)
RK_DIVIDER_TIME_2 = pygame.Rect(605, 246, 160, 2)
RK_DIVIDER_TIME_3 = pygame.Rect(605, 286, 160, 2)
RK_DIVIDER_TIME_4 = pygame.Rect(605, 326, 160, 2)
RK_DIVIDER_TIME_5 = pygame.Rect(605, 366, 160, 2)
RK_DIVIDER_TIME_6 = pygame.Rect(605, 406, 160, 2)
RK_DIVIDER_TIME_7 = pygame.Rect(605, 446, 160, 2)
RK_DIVIDER_TIME_8 = pygame.Rect(605, 486, 160, 2)
RK_DIVIDER_TIME_9 = pygame.Rect(605, 526, 160, 2)

RK_HEAD_SKIN = pygame.Rect(775, 122, 50, 40)
RK_COLUMN_SKIN = pygame.Rect(775, 167, 50, 400)
RK_DIVIDER_SKIN_1 = pygame.Rect(780, 206, 40, 2)
RK_DIVIDER_SKIN_2 = pygame.Rect(780, 246, 40, 2)
RK_DIVIDER_SKIN_3 = pygame.Rect(780, 286, 40, 2)
RK_DIVIDER_SKIN_4 = pygame.Rect(780, 326, 40, 2)
RK_DIVIDER_SKIN_5 = pygame.Rect(780, 366, 40, 2)
RK_DIVIDER_SKIN_6 = pygame.Rect(780, 406, 40, 2)
RK_DIVIDER_SKIN_7 = pygame.Rect(780, 446, 40, 2)
RK_DIVIDER_SKIN_8 = pygame.Rect(780, 486, 40, 2)
RK_DIVIDER_SKIN_9 = pygame.Rect(780, 526, 40, 2)

RK_ARROW_LEFT_BUTTON = pygame.Rect(460, 600, 60, 40)
RK_ARROW_RIGHT_BUTTON = pygame.Rect(680, 600, 60, 40)

RK_STATS_RECT = pygame.Rect(875, 197, 250, 350)


# Job Select
TITLE_EMPLACEMENT = pygame.Rect(WIDTH//3, 50, WIDTH//3, 100)
JOB_PREVIEW = pygame.Rect(WIDTH//2 - 40, 250, 80, 80)
STATS_RECT = pygame.Rect(WIDTH - 325, 150, 250, 350)

MAGE_ICON_EMPLACEMENT = pygame.Rect(419, 500, 62, 62)
KNIGHT_ICON_EMPLACEMENT = pygame.Rect(519, 500, 62, 62)
JOB3_ICON_EMPLACEMENT = pygame.Rect(619, 500, 62, 62)
JOB4_ICON_EMPLACEMENT = pygame.Rect(719, 500, 62, 62)

PLAY_JOB_BUTTON = pygame.Rect(WIDTH//2 - 75, HEIGHT - 50, 150, 40)

## Shop
JOB_SKIN_BUTTON = pygame.Rect(WIDTH//2 - 125, HEIGHT//3, 250, 40)
BACKGROUND_SHOP_BUTTON = pygame.Rect(WIDTH//2 - 125, HEIGHT//3 + 100, 250, 40)
DUNGEON_BACKGROUND_SHOP_BUTTON = pygame.Rect(WIDTH//2 - 125, HEIGHT//3 + 200, 250, 40)

BUY_BUTTON = pygame.Rect(WIDTH//2 - 75, HEIGHT - 50, 150, 40)

SHOP_GOLD_EMPLACEMENT = pygame.Rect(WIDTH - 225, 50, 150, 50)

# Item Slot Small
ITEM_1_S = pygame.Rect(400, 150, 62, 62)
ITEM_2_S = pygame.Rect(500, 150, 62, 62)
ITEM_3_S = pygame.Rect(600, 150, 62, 62)
ITEM_4_S = pygame.Rect(700, 150, 62, 62)
ITEM_5_S = pygame.Rect(400, 250, 62, 62)
ITEM_6_S = pygame.Rect(500, 250, 62, 62)
ITEM_7_S = pygame.Rect(600, 250, 62, 62)
ITEM_8_S = pygame.Rect(700, 250, 62, 62)
ITEM_9_S = pygame.Rect(400, 350, 62, 62)
ITEM_10_S = pygame.Rect(500, 350, 62, 62)
ITEM_11_S = pygame.Rect(600, 350, 62, 62)
ITEM_12_S = pygame.Rect(700, 350, 62, 62)
ITEM_13_S = pygame.Rect(400, 450, 62, 62)
ITEM_14_S = pygame.Rect(500, 450, 62, 62)
ITEM_15_S = pygame.Rect(600, 450, 62, 62)
ITEM_16_S = pygame.Rect(700, 450, 62, 62)

# Job Skin Shop
MAGE_SKIN_BUTTON = pygame.Rect(50, 152, 200, 40)
KNIGHT_SKIN_BUTTON = pygame.Rect(50, 257, 200, 40)
JOB3_SKIN_BUTTON = pygame.Rect(50, 364, 200, 40)
JOB4_SKIN_BUTTON = pygame.Rect(50, 470, 200, 40)


## Main Game

# In Game
GROUND = pygame.Rect(0, HEIGHT - 50, WIDTH, 50)
LIMIT = pygame.Rect(WIDTH//2, 0, 10, HEIGHT)
TOP_BAND = pygame.Rect(0, 0, WIDTH, 80)

RESTART_BUTTON = pygame.Rect(1100, 25, 50, 30)

RANK_IMG_EMPLACEMENT = pygame.Rect(WIDTH//3 - 15, 5, 70, 70)
RANK_IMG_EMPLACEMENT_BIS = pygame.Rect(WIDTH - 250, 75, 70, 70)

JOB_ICON_EMPLACEMENT_IG = pygame.Rect(WIDTH//2 + 200, HEIGHT - 46, 42, 42)

# Abilities
DOUBLE_JUMP_EMPLACEMENT = pygame.Rect( WIDTH//8, HEIGHT - 46, 42, 42)
SLOWFALL_EMPLACEMENT = pygame.Rect( WIDTH//8 + 50, HEIGHT - 46, 42, 42)
DASH_EMPLACEMENT = pygame.Rect( WIDTH//8 + 100, HEIGHT - 46, 42, 42)


## Game Over Screen

# Misc
JOB_ICON_EMPLACEMENT_GO = pygame.Rect(WIDTH//2 - 21, HEIGHT - 50, 42, 42)
CHANGE_JOB_BUTTON = pygame.Rect(WIDTH//2 - 225, HEIGHT - 50, 150, 42)
RETRY_BUTTON = pygame.Rect(WIDTH//2 + 75, HEIGHT - 50, 150, 42)

# Quest
Q1_EMPLACEMENT = pygame.Rect(10, HEIGHT/3 - 30, 300, 50)
Q2_EMPLACEMENT = pygame.Rect(10, HEIGHT/3 - 30 + 70, 300, 50)
Q3_EMPLACEMENT = pygame.Rect(10, HEIGHT/3 - 30 + 140, 300, 50)

# Ranking End Screen
RANKING_INDEX_HEAD = pygame.Rect(WIDTH//3 - 6 - 25, HEIGHT//2, 50, 30)
RANKING_NAME_HEAD = pygame.Rect(WIDTH//3 - 3 + 25, HEIGHT//2, WIDTH//9, 30)
RANKING_TIME_HEAD = pygame.Rect(WIDTH//3 + WIDTH//9 + 25, HEIGHT//2, WIDTH//9, 30)
RANKING_JOB_HEAD = pygame.Rect(WIDTH//3 + WIDTH//9 * 2 + 3 + 25, HEIGHT//2, WIDTH//9, 30)

RANKING_INDEX_COLUMN = pygame.Rect(WIDTH//3 - 6 - 25, HEIGHT//2 + 35, 50, 175)
RANKING_NAME_COLUMN = pygame.Rect(WIDTH//3 - 3 + 25, HEIGHT//2 + 35, WIDTH//9, 175)
RANKING_TIME_COLUMN = pygame.Rect(WIDTH//3 + WIDTH//9 + 25, HEIGHT//2 + 35, WIDTH//9, 175)
RANKING_JOB_COLUMN = pygame.Rect(WIDTH//3 + WIDTH//9 * 2 + 3 + 25, HEIGHT//2 + 35, WIDTH//9, 175)

# Gold Recap
GAME_OVER_GOLD_RECAP = pygame.Rect(10, HEIGHT//3 + 230, 300, 150)
GAME_OVER_GOLD_DIV = pygame.Rect(11, GAME_OVER_GOLD_RECAP.bottom - 41, 298, 2)


### Image ##

# Background
BACKGROUND_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("background", "background.bmp"))),(WIDTH, HEIGHT))
BG_STARS_1 = pygame.image.load(os.path.join("Assets_dodge", os.path.join("background", "bg_stars_1.jpg")))
BG_STARS_2 = pygame.image.load(os.path.join("Assets_dodge", os.path.join("background", "bg_stars_2.jpg")))
BG_STARS_3 = pygame.image.load(os.path.join("Assets_dodge", os.path.join("background", "bg_stars_3.jpg")))
BG_GRAY_WALL = pygame.image.load(os.path.join("Assets_dodge", os.path.join("background", "bg_gray_wall.jpg")))
BG_DUNGEON = pygame.image.load(os.path.join("Assets_dodge", os.path.join("background", "bg_dungeon.jpg")))

# Panels
PANEL_IMG = pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "Panel.png")))
PANEL_2_IMG = pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "Panel_2.png")))

ARROW_IMG = pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "arrow.png")))

# Player Characters
PLAYER_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "player.png"))),(40, 40))),1,0)
PLAYER_HIT_IMG = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "player_hit.png"))),(40, 40)),1,0)

PLAYER_DEAD_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "player_dead.png"))),(40, 40))

# Mage
MaHuRe_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaHuRe_N.png"))),(40, 40))),1,0)
MaHuRe_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaHuRe_H.png"))),(40, 40))),1,0)

MaHuDa_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaHuDa_N.png"))),(40, 40))),1,0)
MaHuDa_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaHuDa_H.png"))),(40, 40))),1,0)

MaHuBl_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaHuBl_N.png"))),(40, 40))),1,0)
MaHuBl_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaHuBl_H.png"))),(40, 40))),1,0)

MaHuGr_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaHuGr_N.png"))),(40, 40))),1,0)
MaHuGr_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaHuGr_H.png"))),(40, 40))),1,0)

MaGoBa_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaGoBa_N.png"))),(40, 40))),1,0)
MaGoBa_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaGoBa_H.png"))),(40, 40))),1,0)

MaFoBa_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaFoBa_N.png"))),(40, 40))),1,0)
MaFoBa_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaFoBa_H.png"))),(40, 40))),1,0)

MaFeGr_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaFeGr_N.png"))),(40, 40))),1,0)
MaFeGr_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaFeGr_H.png"))),(40, 40))),1,0)

MaDeBl_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaDeBl_N.png"))),(40, 40))),1,0)
MaDeBl_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaDeBl_H.png"))),(40, 40))),1,0)

MaDeVi_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaDeVi_N.png"))),(40, 40))),1,0)
MaDeVi_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaDeVi_H.png"))),(40, 40))),1,0)

MaGnBa_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaGnBa_N.png"))),(40, 40))),1,0)
MaGnBa_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaGnBa_H.png"))),(40, 40))),1,0)

MaLiBl_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaLiBl_N.png"))),(40, 40))),1,0)
MaLiBl_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaLiBl_H.png"))),(40, 40))),1,0)

MaSkBa_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaSkBa_N.png"))),(40, 40))),1,0)
MaSkBa_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaSkBa_H.png"))),(40, 40))),1,0)

MaWiGr_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaWiGr_N.png"))),(40, 40))),1,0)
MaWiGr_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaWiGr_H.png"))),(40, 40))),1,0)

MaWiBl_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaWiBl_N.png"))),(40, 40))),1,0)
MaWiBl_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaWiBl_H.png"))),(40, 40))),1,0)

MaFaBa_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaFaBa_N.png"))),(40, 40))),1,0)
MaFaBa_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaFaBa_H.png"))),(40, 40))),1,0)

MaDvRe_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaDvRe_N.png"))),(40, 40))),1,0)
MaDvRe_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "MaDvRe_H.png"))),(40, 40))),1,0)


# Knight
KnSpHuRe_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpHuRe_N.png"))),(40, 40))),1,0)
KnSpHuRe_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpHuRe_H.png"))),(40, 40))),1,0)

KnSpHuBl_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpHuBl_N.png"))),(40, 40))),1,0)
KnSpHuBl_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpHuBl_H.png"))),(40, 40))),1,0)

KnSwHuRe_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwHuRe_N.png"))),(40, 40))),1,0)
KnSwHuRe_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwHuRe_H.png"))),(40, 40))),1,0)

KnSwHuBl_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwHuBl_N.png"))),(40, 40))),1,0)
KnSwHuBl_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwHuBl_H.png"))),(40, 40))),1,0)

KnSwSkBa_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwSkBa_N.png"))),(40, 40))),1,0)
KnSwSkBa_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwSkBa_H.png"))),(40, 40))),1,0)

KnSwFeGr_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwFeGr_N.png"))),(40, 40))),1,0)
KnSwFeGr_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwFeGr_H.png"))),(40, 40))),1,0)

KnSwFeBl_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwFeBl_N.png"))),(40, 40))),1,0)
KnSwFeBl_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwFeBl_H.png"))),(40, 40))),1,0)

KnSwArRe_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwArRe_N.png"))),(40, 40))),1,0)
KnSwArRe_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwArRe_H.png"))),(40, 40))),1,0)

KnSwArGo_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwArGo_N.png"))),(40, 40))),1,0)
KnSwArGo_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwArGo_H.png"))),(40, 40))),1,0)

KnSwArBl_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwArBl_N.png"))),(40, 40))),1,0)
KnSwArBl_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSwArBl_H.png"))),(40, 40))),1,0)

KnSpWoBa_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpWoBa_N.png"))),(40, 40))),1,0)
KnSpWoBa_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpWoBa_H.png"))),(40, 40))),1,0)

KnSpLiBa_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpLiBa_N.png"))),(40, 40))),1,0)
KnSpLiBa_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpLiBa_H.png"))),(40, 40))),1,0)

KnSpHuGr_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpHuGr_N.png"))),(40, 40))),1,0)
KnSpHuGr_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpHuGr_H.png"))),(40, 40))),1,0)

KnSpHuGo_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpHuGo_N.png"))),(40, 40))),1,0)
KnSpHuGo_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnSpHuGo_H.png"))),(40, 40))),1,0)

KnMaDwRe_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnMaDwRe_N.png"))),(40, 40))),1,0)
KnMaDwRe_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnMaDwRe_H.png"))),(40, 40))),1,0)

KnMaDwBl_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnMaDwBl_N.png"))),(40, 40))),1,0)
KnMaDwBl_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "KnMaDwBl_H.png"))),(40, 40))),1,0)


# Dragon
Dragon_N_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("dragon_skin", "Dragon_N.png"))),(40, 40))),1,0)
Dragon_H_IMG = pygame.transform.flip((pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("dragon_skin", "Dragon_H.png"))),(40, 40))),1,0)


# Job Icons
MAGE_ICON = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "mage_icon.png"))),(40, 40))
KNIGHT_ICON = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "knight_icon.png"))),(40, 40))
DRAGON_ICON = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("dragon_skin", "dragon_icon.png"))),(40, 40))

## Abilities Icons/VFX

# Stomp (All)
STOMP_FX_1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "stomp_fx_1.png"))),(40, 40))
STOMP_FX_2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "stomp_fx_2.png"))),(40, 40))
STOMP_FX_3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "stomp_fx_3.png"))),(40, 40))

# Double Jump (All)
DOUBLE_JUMP_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "double_jump.png"))),(40, 40))
DOUBLE_JUMP_CD_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "double_jump_cd.png"))),(40, 40))

DOUBLE_JUMP_FX_1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "double_jump_fx_1.png"))),(40, 40))
DOUBLE_JUMP_FX_2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "double_jump_fx_2.png"))),(40, 40))

# Dash (Mage)
DASH_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "dash.png"))),(40, 40))
DASH_CD_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "dash_cd.png"))),(40, 40))

DASH_PHANTOM_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "dash_phantom.png"))),(40, 40))

DASH_FX_1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "dash_fx_1.png"))),(40, 40))
DASH_FX_2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "dash_fx_2.png"))),(40, 40))
DASH_FX_3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "dash_fx_3.png"))),(40, 40))
DASH_FX_4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "dash_fx_4.png"))),(40, 40))

# Slow Fall (Mage)
SLOWFALL_ON_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "slowfall_on.png"))),(40, 40))
SLOWFALL_OFF_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "slowfall_off.png"))),(40, 40))

SLOWFALL_FX = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("mage_skin", "slowfall_fx.png"))),(40, 20))

# Charge (Knight)
CHARGE_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "charge.png"))),(40, 40))
CHARGE_ON_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "charge_on.png"))),(40, 40))
CHARGE_CD_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "charge_cd.png"))),(40, 40))

# Shield Up (Knight)
SHIELD_UP_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "shield_up.png"))),(40, 40))
SHIELD_UP_ON_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "shield_up_on.png"))),(40, 40))
SHIELD_UP_CD_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "shield_up_cd.png"))),(40, 40))

SHIELD_UP_FX = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("knight_skin", "shield_up_fx.png"))),(40, 40))

# Flight (Dragon)
FLIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("dragon_skin", "flight.png"))),(40, 40))
FLIGHT_CD_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("dragon_skin", "flight_cd.png"))),(40, 40))

# Soar (Dragon)
SOAR_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("dragon_skin", "soar.png"))),(40, 40))
SOAR_CD_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("dragon_skin", "soar_cd.png"))),(40, 40))

# Shield Up (Dragon)
ROAR_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("dragon_skin", "roar.png"))),(40, 40))
ROAR_CD_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("dragon_skin", "roar_cd.png"))),(40, 40))


## Game img / VFX

# Bullets / Pick Ups
BULLET_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "bullet.png"))),(25, 10))
GROUND_BULLET_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "barrel.png"))),(40, 40))
HEALTH_PICK_UP_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "health_pick_up.png"))),(30, 30))
COIN_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "coin.png"))),(30, 30))

# Damage
DMG_1_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "dmg_1.png"))),(60, 60))
DMG_2_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "dmg_2.png"))),(60, 60))

# Heal
HEAL_FX_1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "heal_fx_1.png"))),(50, 50))
HEAL_FX_2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "heal_fx_2.png"))),(50, 50))
HEAL_FX_3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "heal_fx_3.png"))),(50, 50))


### Misc

# Health Indicator
HEART_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "heart.png"))),(50, 50))
HEART_EMPTY_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "heart_empty.png"))),(50, 50))

# Rank
RANK_1_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("rank", "rank_1.png"))),(70, 70))
RANK_2_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("rank", "rank_2.png"))),(70, 70))
RANK_3_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("rank", "rank_3.png"))),(70, 70))
RANK_4_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("rank", "rank_4.png"))),(70, 70))
RANK_5_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("rank", "rank_5.png"))),(70, 70))
RANK_6_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("rank", "rank_6.png"))),(70, 70))
RANK_7_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("rank", "rank_7.png"))),(70, 70))

# Name Entry Panel (scaled)
NAME_ENTRY_OFF = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "Panel.png"))),(NAME_ENTRY.width - 2, NAME_ENTRY.height - 2))
NAME_ENTRY_ON = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "Panel_2.png"))),(NAME_ENTRY.width - 2, NAME_ENTRY.height - 2))

LIMIT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_dodge", os.path.join("general", "limit.png"))),(LIMIT.width, LIMIT.height))

###################
###################


class game:
    main_on = False
    game_over = False
    pause = True
    restart = False
    start_timer = 0
    timer = 0
    best_time = 0
    new_best = False

    name_box_active = False
    player_name = ""

    ranking_list = []
    player_rank_number = "Unranked"
    best_time_ever = 0
    player_best_time_job = ""
    next_in_rank_index = 0
    next_in_rank_name = ""
    next_in_rank_time = 0
    next_in_rank_job = ""

    run_gold = 0
    player_old_gold = 0


class player:
    job = "Mage"
    best_time_mage = 0
    best_time_knight = 0
    best_time_dragon = 0

    rank = 0
    rank_name = "Unranked"
    rank_goal = "Survive 10s"
    rank_img = None

    gold = 0
    quest_dic = {}

    player_ch = pygame.Rect(475, 550, 40, 40)

    hp = 3
    i_frame = False
    i_frame_timer = 0
    i_frame_duration = 0.3
    immune = False

    speed = 10
    speed_multiplier = 1
    ground = False
    jump_power = 12
    jump_velocity = 0
    jump_velocity_multiplier = 1
    double_jump = True
    double_jump_multiplier = 1.3

    special_type = "Slowfall"
    special_desc_1 = "Hold to slow the fall"
    special_desc_2 = "speed of the player."
    special_timer = 0
    special_duration = 0.5
    special_cd = 10
    shield_up = False
    slowfall = False
    dash_type = "Warp"
    dash_desc_1 = "Teleport a short distance"
    dash_desc_2 = "in front."
    dash_cd = 3
    dash_timer = 0
    dash_power = 250
    dash_phantom = pygame.Rect(0, 0, 40, 40)
    charge = False
    charge_end = 0
    endurance = 100
    grounded = True
    grounded_timer = 0
    soar = False
    roar_radius = 150

    skin_mage_list = ["MaHuRe"]
    skin_knight_list = ["KnSpHuBl"]
    skin_dragon_list = ["Dragon"]
    current_mage_skin_name = "MaHuRe"
    mage_skin = MaHuRe_N_IMG
    mage_skin_hit = MaHuRe_H_IMG
    current_knight_skin_name = "KnSpHuBl"
    knight_skin = KnSpHuBl_N_IMG
    knight_skin_hit = KnSpHuBl_H_IMG
    current_dragon_skin_name = "Dragon"
    dragon_skin = Dragon_N_IMG
    dragon_skin_hit = Dragon_H_IMG

class projectile:
    list = []
    projectile_timer = 0
    projectile_frequency = 3
    speed_modifier = 1
    heal = False
    heal_timer = 0
    heal_cd = 15
    heal_cd_min = 15
    coin_timer = 0

class animations:
    list = []

def switch_job():
    if player.job == "Mage":
        player.dash_type = "Warp"
        player.dash_desc_1 = "Teleport a short distance"
        player.dash_desc_2 = "in front."
        player.dash_cd = 3
        player.dash_power = 250
        player.special_type = "Slowfall"
        player.special_desc_1 = "Hold to slow the fall"
        player.special_desc_2 = "speed of the player."
    if player.job == "Knight":
        player.dash_type = "Charge"
        player.dash_desc_1 = "Charge ahead while"
        player.dash_desc_2 = "being immune to damage."
        player.dash_cd = 5
        player.dash_power = 400
        player.special_type = "Shield Up"
        player.special_desc_1 = "Damage immunity for"
        player.special_desc_2 = "a short amount of time."
        player.special_timer = 0
        player.special_duration = 1
        player.special_cd = 10
    if player.job == "Dragon":
        player.dash_type = "Soar"
        player.dash_desc_1 = "desc_1"
        player.dash_desc_2 = "desc_2"
        player.dash_cd = 5
        player.dash_power = 30
        player.special_type = "Roar"
        player.special_desc_1 = "desc_1"
        player.special_desc_2 = "desc_2"
        player.special_cd = 12

def generate_projectile_basic():
    amount = random.randint(2, 5)
    for i in range(amount):
        y = random.randint(200, GROUND.y - 15)
        velocity = random.randint(4, 10)
        projectile.list.append({"type" : "basic", "rect" : pygame.Rect(WIDTH, y, 25, 10), "velocity" : velocity})
    
def generate_projectile_linear():
    amount = random.randint(6,10)
    y = random.randint(200, GROUND.y - 15)
    velocity = random.randint(4, 10)
    x_offset = random.randint(-20,20)
    for i in range(amount):
        projectile.list.append({"type" : "basic", "rect" : pygame.Rect(WIDTH + 50 + (i - 1) * x_offset, y - (i - 1) * 15, 25, 10), "velocity" : velocity})

def generate_projectile_ground():
    velocity = random.randint(4, 12)
    projectile.list.append({"type" : "ground", "rect" : pygame.Rect(WIDTH, GROUND.top - 40, 40, 40), "velocity" : velocity})

def generate_health_pick_up():
    #velocity = random.randint(3, 6)
    y = random.randint(200, GROUND.y - 30)
    projectile.list.append({"type" : "heal", "rect" : pygame.Rect(WIDTH, y, 30, 30), "velocity" : 3})
    
def generate_coins():
    amount = random.randint(3,5)
    y = random.randint(200, GROUND.y - 40)
    #velocity = random.randint(4, 10)
    x_offset = random.choice([90,45,0,-45,-90])
    for i in range(amount):
        projectile.list.append({"type" : "coin", "rect" : pygame.Rect(WIDTH + 200 + (i - 1) * x_offset, y - (i - 1) * 40, 30, 30), "velocity" : 3})

def projectile_logic():
    bullet_type = [generate_projectile_basic, generate_projectile_linear]
    roll = random.choice(bullet_type)
    roll()
    generate_projectile_ground()
    if game.timer > 60:
        projectile.projectile_frequency = 0.5
    if game.timer > 50:
        projectile.projectile_frequency = 0.75
    elif game.timer > 40:
        projectile.projectile_frequency = 1
    elif game.timer > 30:
        projectile.projectile_frequency = 1.5
    elif game.timer > 20:
        projectile.projectile_frequency = 2
    elif game.timer > 10:
        projectile.projectile_frequency = 2.5
    elif game.timer <= 10:
        projectile.projectile_frequency = 3

def update_all_projectile():
    temp_list = []
    for bullet in projectile.list:
        bullet["rect"].x -= bullet["velocity"]
        if bullet["rect"].x < -(bullet["rect"].width):
            temp_list.append(bullet)
    for item in temp_list:
        projectile.list.remove(item)

def display_all_projectile():
    for bullet in projectile.list:
        if bullet["type"] == "basic":
            screen.blit(BULLET_IMG, (bullet["rect"].x, bullet["rect"].y))
        if bullet["type"] == "ground":
            screen.blit(GROUND_BULLET_IMG, (bullet["rect"].x, bullet["rect"].y))
        if bullet["type"] == "heal":
            screen.blit(HEALTH_PICK_UP_IMG, (bullet["rect"].x, bullet["rect"].y))
        if bullet["type"] == "coin":
            screen.blit(COIN_IMG, (bullet["rect"].x, bullet["rect"].y))

def check_collision():
    temp_list = []
    for bullet in projectile.list:
        if player.player_ch.colliderect(bullet["rect"]):
            temp_list.append(bullet)
            if bullet["type"] == "heal":
                if player.hp < 5:
                    player.hp += 1
                animations.list.append({"type" : "heal", "x" : player.player_ch.centerx - HEAL_FX_1.get_width()//2, "y" : player.player_ch.centery - HEAL_FX_1.get_height()//2, "max_frame" : 15, "current_frame" : 0})
            elif bullet["type"] == "coin":
                game.run_gold += 1
                animations.list.append({"type" : "coin", "x" : player.player_ch.centerx - COIN_IMG.get_width()//2, "y" : player.player_ch.centery - COIN_IMG.get_height()//2, "max_frame" : 12, "current_frame" : 0})
            else:
                if player.i_frame == False and player.immune == False:
                    player.hp -= 1
                    player.i_frame = True
                    player.i_frame_timer = time.time()
                    animations.list.append({"type" : "dmg", "x" : player.player_ch.x - 10, "y" : player.player_ch.y - 10, "max_frame" : 8, "current_frame" : 0})
    for item in temp_list:
        projectile.list.remove(item)

def check_best_timer():
    if game.timer > game.best_time:
        game.best_time = game.timer
        game.new_best = True
    if game.timer > game.best_time_ever:
        game.best_time_ever = game.timer

def rank_award():
    if game.best_time >= 120 and player.rank < 7:
        player.rank = 7
        player.rank_name = "Ascended"
        player.rank_goal = "???"
        player.rank_img = RANK_7_IMG
    if game.best_time >= 60 and player.rank < 6:
        player.rank = 6
        player.rank_name = "Legend"
        player.rank_goal = "Reach For The Stars !"
        player.rank_img = RANK_6_IMG
    if game.best_time >= 50 and player.rank < 5:
        player.rank = 5
        player.rank_name = "Hero"
        player.rank_goal = "Survive 60s"
        player.rank_img = RANK_5_IMG
    if game.best_time >= 40 and player.rank < 4:
        player.rank = 4
        player.rank_name = "Gold"
        player.rank_goal = "Survive 50s"
        player.rank_img = RANK_4_IMG
    if game.best_time >= 30 and player.rank < 3:
        player.rank = 3
        player.rank_name = "Iron"
        player.rank_goal = "Survive 40s"
        player.rank_img = RANK_3_IMG
    if game.best_time >= 20 and player.rank < 2:
        player.rank = 2
        player.rank_name = "Bronze"
        player.rank_goal = "Survive 30s"
        player.rank_img = RANK_2_IMG
    if game.best_time >= 10 and player.rank < 1:
        player.rank = 1
        player.rank_name = "Wood"
        player.rank_goal = "Survive 20s"
        player.rank_img = RANK_1_IMG

def reorder_ranking():
    global_ranking = game.ranking_list
    number_of_ranked = len(global_ranking)
    game.ranking_list = []
    while number_of_ranked != 0:
        temp_selected = global_ranking[0]
        for each in global_ranking:
            if each["time"] > temp_selected["time"]:
                temp_selected = each
        game.ranking_list.append(temp_selected)
        global_ranking.remove(temp_selected)
        number_of_ranked = len(global_ranking)

def get_ranking_info():
    global_ranking = game.ranking_list
    if player.rank != "Unranked":
        index = 0
        if global_ranking[0]["name"] == game.player_name:
            game.next_in_rank = f"You are at the top !"
        else:
            previous = global_ranking[0]
            for each in global_ranking:
                if each["name"] == game.player_name:
                    game.player_rank_number = index + 1
                    game.next_in_rank_index = index
                    game.next_in_rank_name = previous['name']
                    game.next_in_rank_time = previous['time']
                    game.next_in_rank_job = previous['job']
                else:
                    previous = each
                    index += 1


### Quest

class quest_database():
    all_quest = ["Q1", "Q2", "Q3", "Q4", "Q5"]
    potential_quest = ["Q1", "Q2", "Q3", "Q4", "Q5"]
    quest_reward = 0

    Q1 = "Collect 10 coins in a single run."
    Q1_objective = 10
    Q1_reward = 20
    
    Q2 = "Collect 20 coins in a single run."
    Q2_objective = 20
    Q2_reward = 50
    
    Q3 = "Collect 30 coins in a single run."
    Q3_objective = 30
    Q3_reward = 100
    
    Q4 = "Collect 40 coins in a single run."
    Q4_objective = 40
    Q4_reward = 175
    
    Q5 = "Collect 50 coins in a single run."
    Q5_objective = 50
    Q5_reward = 250

    def update(self, window = None):
        self.give_quest()

        if window == "game_on":
            self.quest_progress()

        if window == "game_over" and animations.list == []:
            self.give_reward()

    def give_quest(self):
        if len(player.quest_dic) < 3 and animations.list == []:
            potential_quest = []
            for quest in self.all_quest:
                if quest not in player.quest_dic:
                    potential_quest.append(quest)
            player.quest_dic[random.choice(potential_quest)] = 0
            
    def quest_progress(self):
        if "Q1" in player.quest_dic:
            if player.quest_dic["Q1"] != "Completed !":
                player.quest_dic["Q1"] = game.run_gold
                if player.quest_dic["Q1"] >= self.Q1_objective:
                    player.quest_dic["Q1"] = "Completed !"
                
        if "Q2" in player.quest_dic:
            if player.quest_dic["Q2"] != "Completed !":
                player.quest_dic["Q2"] = game.run_gold
                if player.quest_dic["Q2"] >= self.Q2_objective:
                    player.quest_dic["Q2"] = "Completed !"
                    
        if "Q3" in player.quest_dic:
            if player.quest_dic["Q3"] != "Completed !":
                player.quest_dic["Q3"] = game.run_gold
                if player.quest_dic["Q3"] >= self.Q3_objective:
                    player.quest_dic["Q3"] = "Completed !"
                    
        if "Q4" in player.quest_dic:
            if player.quest_dic["Q4"] != "Completed !":
                player.quest_dic["Q4"] = game.run_gold
                if player.quest_dic["Q4"] >= self.Q4_objective:
                    player.quest_dic["Q4"] = "Completed !"
                    
        if "Q5" in player.quest_dic:
            if player.quest_dic["Q5"] != "Completed !":
                player.quest_dic["Q5"] = game.run_gold
                if player.quest_dic["Q5"] >= self.Q5_objective:
                    player.quest_dic["Q5"] = "Completed !"
                    
    def give_reward(self):
        key_list = list(player.quest_dic)
        # Giving Reward depending on the quest
        for key in key_list:
            if key == "Q1" and player.quest_dic[key] == "Completed !":
                player.gold += self.Q1_reward
                self.quest_reward += self.Q1_reward
                offset = key_list.index(key)
                animations.list.append({"type" : "quest", "amount" : self.Q1_reward, "x" : Q1_EMPLACEMENT.centerx, "y" : Q1_EMPLACEMENT.centery + 70 * offset, "max_frame" : 180, "current_frame" : 0})
                del player.quest_dic["Q1"]
            if key == "Q2" and player.quest_dic[key] == "Completed !":
                player.gold += self.Q2_reward
                self.quest_reward += self.Q2_reward
                offset = key_list.index(key)
                animations.list.append({"type" : "quest", "amount" : self.Q2_reward, "x" : Q1_EMPLACEMENT.centerx, "y" : Q1_EMPLACEMENT.centery + 70 * offset, "max_frame" : 180, "current_frame" : 0})
                del player.quest_dic["Q2"]
            if key == "Q3" and player.quest_dic[key] == "Completed !":
                player.gold += self.Q3_reward
                self.quest_reward += self.Q3_reward
                offset = key_list.index(key)
                animations.list.append({"type" : "quest", "amount" : self.Q3_reward, "x" : Q1_EMPLACEMENT.centerx, "y" : Q1_EMPLACEMENT.centery + 70 * offset, "max_frame" : 180, "current_frame" : 0})
                del player.quest_dic["Q3"]
            if key == "Q4" and player.quest_dic[key] == "Completed !":
                player.gold += self.Q4_reward
                self.quest_reward += self.Q4_reward
                offset = key_list.index(key)
                animations.list.append({"type" : "quest", "amount" : self.Q4_reward, "x" : Q1_EMPLACEMENT.centerx, "y" : Q1_EMPLACEMENT.centery + 70 * offset, "max_frame" : 180, "current_frame" : 0})
                del player.quest_dic["Q4"]
            if key == "Q5" and player.quest_dic[key] == "Completed !":
                player.gold += self.Q5_reward
                self.quest_reward += self.Q5_reward
                offset = key_list.index(key)
                animations.list.append({"type" : "quest", "amount" : self.Q5_reward, "x" : Q1_EMPLACEMENT.centerx, "y" : Q1_EMPLACEMENT.centery + 70 * offset, "max_frame" : 180, "current_frame" : 0})
                del player.quest_dic["Q5"]



def play_animations():
    temp_list = []
    for anim in animations.list:
        if anim["type"] == "dmg":
            if anim["current_frame"] <= anim["max_frame"]//2:
                screen.blit(DMG_1_IMG, (anim["x"], anim["y"]))
            elif anim["current_frame"] > anim["max_frame"]//2:
                screen.blit(DMG_2_IMG, (anim["x"], anim["y"]))

        if anim["type"] == "dash":
            if anim["current_frame"] <= anim["max_frame"]//4:
                screen.blit(DASH_FX_1, (anim["x"], anim["y"]))
            elif anim["current_frame"] <= anim["max_frame"]//2 and anim["current_frame"] > anim["max_frame"]//4:
                screen.blit(DASH_FX_2, (anim["x"], anim["y"]))
            elif anim["current_frame"] <= (anim["max_frame"]//4 * 3) and anim["current_frame"] > anim["max_frame"]//2:
                screen.blit(DASH_FX_3, (anim["x"], anim["y"]))
            elif anim["current_frame"] > (anim["max_frame"]//4 * 3):
                screen.blit(DASH_FX_4, (anim["x"], anim["y"]))

        if anim["type"] == "afterdash":
            if anim["current_frame"] <= anim["max_frame"]//4:
                screen.blit(DASH_FX_4, (anim["x"], anim["y"]))
            elif anim["current_frame"] <= anim["max_frame"]//2 and anim["current_frame"] > anim["max_frame"]//4:
                screen.blit(DASH_FX_3, (anim["x"], anim["y"]))
            elif anim["current_frame"] <= (anim["max_frame"]//4 * 3) and anim["current_frame"] > anim["max_frame"]//2:
                screen.blit(DASH_FX_2, (anim["x"], anim["y"]))
            elif anim["current_frame"] > (anim["max_frame"]//4 * 3):
                screen.blit(DASH_FX_1, (anim["x"], anim["y"]))
                
        if anim["type"] == "double_jump":
            if anim["current_frame"] <= anim["max_frame"]//2:
                screen.blit(DOUBLE_JUMP_FX_1, (anim["x"], anim["y"]))
            elif anim["current_frame"] > anim["max_frame"]//2:
                screen.blit(DOUBLE_JUMP_FX_2, (anim["x"], anim["y"]))
                
        if anim["type"] == "slowfall":
            if anim["current_frame"] <= anim["max_frame"]:
                screen.blit(SLOWFALL_FX, (anim["x"], anim["y"]))
                
        if anim["type"] == "stomp":
            if anim["current_frame"] <= anim["max_frame"]//3:
                screen.blit(STOMP_FX_1, (anim["x"], anim["y"]))
            elif anim["current_frame"] <= (anim["max_frame"]//3 * 2) and anim["current_frame"] > anim["max_frame"]//3:
                screen.blit(STOMP_FX_2, (anim["x"], anim["y"]))
            elif anim["current_frame"] > (anim["max_frame"]//3 * 2):
                screen.blit(STOMP_FX_3, (anim["x"], anim["y"]))
                
        if anim["type"] == "heal":
            if anim["current_frame"] <= anim["max_frame"]//3:
                screen.blit(HEAL_FX_1, (anim["x"], anim["y"]))
            elif anim["current_frame"] <= (anim["max_frame"]//3 * 2) and anim["current_frame"] > anim["max_frame"]//3:
                screen.blit(HEAL_FX_2, (anim["x"], anim["y"]))
            elif anim["current_frame"] > (anim["max_frame"]//3 * 2):
                screen.blit(HEAL_FX_3, (anim["x"], anim["y"]))
                
        if anim["type"] == "coin":
            if anim["current_frame"] <= anim["max_frame"]:
                screen.blit(pygame.transform.scale(COIN_IMG,(20,20)), (anim["x"], anim["y"] - anim["current_frame"] * 3))

        if anim["type"] == "quest":
            if anim["current_frame"] <= anim["max_frame"]:
                reward_text = font.render(f"{anim['amount']}", 1, GREEN)
                screen.blit(reward_text, (anim["x"], anim["y"] - anim["current_frame"]/5))
                screen.blit(pygame.transform.scale(COIN_IMG,(30,30)), (anim["x"] + reward_text.get_width() + 3, anim["y"] - anim["current_frame"]/5))

        anim["current_frame"] += 1
        if anim["max_frame"] <= anim["current_frame"]:
            temp_list.append(anim)

    for anim in temp_list:
        animations.list.remove(anim)

    if player.immune and player.job == "Knight":
        screen.blit(SHIELD_UP_FX, (player.player_ch.centerx, player.player_ch.y))

class background:
    overall_bg = BACKGROUND_IMG
    bg_x = 0
    dungeon_bg = BG_DUNGEON

def update_bg(window = None):
    if window == "game":
        if game.pause == False and game.game_over == False:
            background.bg_x -= 3
        if background.bg_x <= -background.dungeon_bg.get_width():
            background.bg_x = 0
        screen.blit(background.dungeon_bg, (background.bg_x, 0))
        screen.blit(background.dungeon_bg, (background.bg_x + background.dungeon_bg.get_width(), 0))
    else:
        screen.blit(background.overall_bg, (0,0))

def restart_game():
    game.pause = True
    game.game_over = False
    game.restart = False
    game.timer = 0
    game.start_timer = time.time()
    game.new_best = False
    projectile.heal_timer = time.time()
    projectile.projectile_timer = time.time()
    projectile.coin_timer = time.time()
    player.hp = 3
    player.player_ch.x = 475
    player.player_ch.y = 550
    player.jump_velocity = 0
    player.dash_timer = 0
    player.special_timer = 0
    player.i_frame = False
    player.ground = False
    player.endurance = 100
    projectile.list = []
    game.run_gold = 0
    quest_database.quest_reward = 0

def main_game_draw_window():
    update_bg("game")

    screen.blit(LIMIT_IMG, (LIMIT.x, LIMIT.y))
    pygame.draw.rect(screen, DARK_GRAY, GROUND)
    pygame.draw.rect(screen, DARK_GRAY, (0, TOP_BAND.bottom, WIDTH, 2))
    pygame.draw.rect(screen, GRAY, TOP_BAND)

    pygame.draw.rect(screen, GRAYISH, RESTART_BUTTON)
    restart_text = button_font.render("Restart", 1, BLACK)
    screen.blit(restart_text, (RESTART_BUTTON.centerx - restart_text.get_width()//2, RESTART_BUTTON.centery - restart_text.get_height()//2))

    pygame.draw.rect(screen, GRAY, NAME_ENTRY)
    screen.blit(NAME_ENTRY_OFF, (NAME_ENTRY.x + 1, NAME_ENTRY.y + 1))
    if game.player_name == "":
        name_text = font.render("Player Name", 1, WHITE)
    else:
        name_text = font.render(f"{game.player_name}", 1, WHITE)
    screen.blit(name_text, (NAME_ENTRY.centerx - name_text.get_width()//2, NAME_ENTRY.centery - name_text.get_height()//2))

    screen.blit(COIN_IMG, (WIDTH - 40, TOP_BAND.bottom + 10))
    gold_text = font.render(f"{game.run_gold}", 1, WHITE)
    screen.blit(gold_text, (WIDTH - 50 - gold_text.get_width(), TOP_BAND.bottom + 12 + COIN_IMG.get_height()//2 - gold_text.get_height()//2))

    timer_text = font.render(f"Time : {game.timer:.2f}s", 1, BLACK)
    screen.blit(timer_text, (WIDTH//4 * 3, 10))
    if game.new_best:
        best_timer_text = font.render(f"New Best !", 1, GREEN)
    else:
        best_timer_text = font.render(f"Best : {game.best_time:.2f}s", 1, BLACK)
    screen.blit(best_timer_text, (WIDTH//4 * 3, 20 + timer_text.get_height()))

    rank_text = big_font.render(f"Rank : {player.rank_name}", 1, BLACK)
    screen.blit(rank_text, (RANK_IMG_EMPLACEMENT.right + 10, 10))
    rank_goal_text = font.render(f"Next rank : {player.rank_goal}", 1, BLACK)
    screen.blit(rank_goal_text, (RANK_IMG_EMPLACEMENT.right + 10, 15 + rank_text.get_height()))
    if player.rank_img != None:
        #pygame.draw.rect(screen, GRAYISH, RANK_IMG_EMPLACEMENT)
        screen.blit(player.rank_img, (RANK_IMG_EMPLACEMENT.x, RANK_IMG_EMPLACEMENT.y))

    if player.hp >= 1:
        screen.blit(HEART_IMG, ( 10, TOP_BAND.centery - HEART_IMG.get_height()//2))
    else:
        screen.blit(HEART_EMPTY_IMG, ( 10, TOP_BAND.centery - HEART_EMPTY_IMG.get_height()//2))
    if player.hp >= 2:
        screen.blit(HEART_IMG, ( 10 + HEART_IMG.get_width() + 20, TOP_BAND.centery - HEART_IMG.get_height()//2))
    else:
        screen.blit(HEART_EMPTY_IMG, ( 10 + HEART_EMPTY_IMG.get_width() + 20, TOP_BAND.centery - HEART_EMPTY_IMG.get_height()//2))
    if player.hp >= 3:
        screen.blit(HEART_IMG, ( 10 + (HEART_IMG.get_width() + 20) * 2, TOP_BAND.centery - HEART_IMG.get_height()//2))
    else:
        screen.blit(HEART_EMPTY_IMG, ( 10 + (HEART_EMPTY_IMG.get_width() + 20) * 2, TOP_BAND.centery - HEART_EMPTY_IMG.get_height()//2))
    if player.hp >= 4:
        screen.blit(HEART_IMG, ( 10 + (HEART_IMG.get_width() + 20) * 3, TOP_BAND.centery - HEART_IMG.get_height()//2))
    else:
        screen.blit(HEART_EMPTY_IMG, ( 10 + (HEART_EMPTY_IMG.get_width() + 20) * 3, TOP_BAND.centery - HEART_EMPTY_IMG.get_height()//2))
    if player.hp >= 5:
        screen.blit(HEART_IMG, ( 10 + (HEART_IMG.get_width() + 20) * 4, TOP_BAND.centery - HEART_IMG.get_height()//2))
    else:
        screen.blit(HEART_EMPTY_IMG, ( 10 + (HEART_EMPTY_IMG.get_width() + 20) * 4, TOP_BAND.centery - HEART_EMPTY_IMG.get_height()//2))

    pygame.draw.rect(screen, BLACK, DASH_EMPLACEMENT)
    if player.job == "Mage":
        if time.time() - player.dash_timer >= player.dash_cd:
            screen.blit(DASH_IMG, (DASH_EMPLACEMENT.x + 1, DASH_EMPLACEMENT.y + 1))
            screen.blit(DASH_PHANTOM_IMG, (player.dash_phantom.x, player.dash_phantom.y))
        else:
            screen.blit(DASH_CD_IMG, (DASH_EMPLACEMENT.x + 1, DASH_EMPLACEMENT.y + 1))
            dash_cd_text = font.render(f"{(player.dash_timer + player.dash_cd - time.time()):.1f}", 1, WHITE)
            screen.blit(dash_cd_text, (DASH_EMPLACEMENT.centerx - dash_cd_text.get_width()//2, DASH_EMPLACEMENT.centery - dash_cd_text.get_height()//2))
    if player.job == "Knight":
        if player.charge:
            pygame.draw.rect(screen, YELLOW, DASH_EMPLACEMENT)
            screen.blit(CHARGE_ON_IMG, (DASH_EMPLACEMENT.x + 1, DASH_EMPLACEMENT.y + 1))
        elif time.time() - player.dash_timer >= player.dash_cd:
            screen.blit(CHARGE_IMG, (DASH_EMPLACEMENT.x + 1, DASH_EMPLACEMENT.y + 1))
        else:
            screen.blit(CHARGE_CD_IMG, (DASH_EMPLACEMENT.x + 1, DASH_EMPLACEMENT.y + 1))
            dash_cd_text = font.render(f"{(player.dash_timer + player.dash_cd - time.time()):.1f}", 1, WHITE)
            screen.blit(dash_cd_text, (DASH_EMPLACEMENT.centerx - dash_cd_text.get_width()//2, DASH_EMPLACEMENT.centery - dash_cd_text.get_height()//2))
    if player.job == "Dragon":
        if time.time() - player.dash_timer >= player.dash_cd:
            screen.blit(SOAR_IMG, (DASH_EMPLACEMENT.x + 1, DASH_EMPLACEMENT.y + 1))
        else:
            screen.blit(SOAR_CD_IMG, (DASH_EMPLACEMENT.x + 1, DASH_EMPLACEMENT.y + 1))
            dash_cd_text = font.render(f"{(player.dash_timer + player.dash_cd - time.time()):.1f}", 1, WHITE)
            screen.blit(dash_cd_text, (DASH_EMPLACEMENT.centerx - dash_cd_text.get_width()//2, DASH_EMPLACEMENT.centery - dash_cd_text.get_height()//2))

    pygame.draw.rect(screen, BLACK, DOUBLE_JUMP_EMPLACEMENT)
    if player.job == "Dragon":
        if player.endurance >= 25:
            pygame.draw.rect(screen, YELLOW, (player.player_ch.x - 10, player.player_ch.y, 5, 5))
            screen.blit(FLIGHT_IMG, (DOUBLE_JUMP_EMPLACEMENT.x + 1, DOUBLE_JUMP_EMPLACEMENT.y + 1))
            remaining_charge_text = font.render(f"1", 1, WHITE)
        if player.endurance >= 50:
            pygame.draw.rect(screen, YELLOW, (player.player_ch.x - 10, player.player_ch.y + 10, 5, 5))
            screen.blit(FLIGHT_IMG, (DOUBLE_JUMP_EMPLACEMENT.x + 1, DOUBLE_JUMP_EMPLACEMENT.y + 1))
            remaining_charge_text = font.render(f"2", 1, WHITE)
        if player.endurance >= 75:
            pygame.draw.rect(screen, YELLOW, (player.player_ch.x - 10, player.player_ch.y + 20, 5, 5))
            screen.blit(FLIGHT_IMG, (DOUBLE_JUMP_EMPLACEMENT.x + 1, DOUBLE_JUMP_EMPLACEMENT.y + 1))
            remaining_charge_text = font.render(f"3", 1, WHITE)
        if player.endurance >= 100:
            pygame.draw.rect(screen, YELLOW, (player.player_ch.x - 10, player.player_ch.y + 30, 5, 5))
            screen.blit(FLIGHT_IMG, (DOUBLE_JUMP_EMPLACEMENT.x + 1, DOUBLE_JUMP_EMPLACEMENT.y + 1))
            remaining_charge_text = font.render(f"4", 1, WHITE)
        elif player.endurance < 25:
            screen.blit(FLIGHT_CD_IMG, (DOUBLE_JUMP_EMPLACEMENT.x + 1, DOUBLE_JUMP_EMPLACEMENT.y + 1))
            remaining_charge_text = font.render(f"0", 1, WHITE)
        screen.blit(remaining_charge_text, (DOUBLE_JUMP_EMPLACEMENT.centerx - remaining_charge_text.get_width()//2, DOUBLE_JUMP_EMPLACEMENT.centery - remaining_charge_text.get_height()//2))
        pygame.draw.circle(screen, RED, player.player_ch.center, player.roar_radius, 1)
    elif player.double_jump:
        screen.blit(DOUBLE_JUMP_IMG, (DOUBLE_JUMP_EMPLACEMENT.x + 1, DOUBLE_JUMP_EMPLACEMENT.y + 1))
    else:
        screen.blit(DOUBLE_JUMP_CD_IMG, (DOUBLE_JUMP_EMPLACEMENT.x + 1, DOUBLE_JUMP_EMPLACEMENT.y + 1))
            
    pygame.draw.rect(screen, BLACK, SLOWFALL_EMPLACEMENT)
    if player.job == "Mage":
        if player.slowfall:
            screen.blit(SLOWFALL_ON_IMG, (SLOWFALL_EMPLACEMENT.x + 1, SLOWFALL_EMPLACEMENT.y + 1))
        else:
            screen.blit(SLOWFALL_OFF_IMG, (SLOWFALL_EMPLACEMENT.x + 1, SLOWFALL_EMPLACEMENT.y + 1))
    elif player.job == "Knight":
        if player.shield_up:
            pygame.draw.rect(screen, YELLOW, SLOWFALL_EMPLACEMENT)
            screen.blit(SHIELD_UP_ON_IMG, (SLOWFALL_EMPLACEMENT.x + 1, SLOWFALL_EMPLACEMENT.y + 1))
            special_duration_text = font.render(f"{player.special_timer + player.special_duration - time.time():.1f}", 1, WHITE)
            screen.blit(special_duration_text, (SLOWFALL_EMPLACEMENT.centerx - special_duration_text.get_width()//2, SLOWFALL_EMPLACEMENT.centery - special_duration_text.get_height()//2))
        elif time.time() - player.special_timer >= player.special_cd:
            screen.blit(SHIELD_UP_IMG, (SLOWFALL_EMPLACEMENT.x + 1, SLOWFALL_EMPLACEMENT.y + 1))
        else:
            screen.blit(SHIELD_UP_CD_IMG, (SLOWFALL_EMPLACEMENT.x + 1, SLOWFALL_EMPLACEMENT.y + 1))
            special_cd_text = font.render(f"{player.special_timer + player.special_cd - time.time():.1f}", 1, WHITE)
            screen.blit(special_cd_text, (SLOWFALL_EMPLACEMENT.centerx - special_cd_text.get_width()//2, SLOWFALL_EMPLACEMENT.centery - special_cd_text.get_height()//2))
    elif player.job == "Dragon":
        if time.time() - player.special_timer >= player.special_cd:
            screen.blit(ROAR_IMG, (SLOWFALL_EMPLACEMENT.x + 1, SLOWFALL_EMPLACEMENT.y + 1))
        else:
            screen.blit(ROAR_CD_IMG, (SLOWFALL_EMPLACEMENT.x + 1, SLOWFALL_EMPLACEMENT.y + 1))
            special_cd_text = font.render(f"{player.special_timer + player.special_cd - time.time():.1f}", 1, WHITE)
            screen.blit(special_cd_text, (SLOWFALL_EMPLACEMENT.centerx - special_cd_text.get_width()//2, SLOWFALL_EMPLACEMENT.centery - special_cd_text.get_height()//2))

    else:
        screen.blit(SLOWFALL_OFF_IMG, (SLOWFALL_EMPLACEMENT.x + 1, SLOWFALL_EMPLACEMENT.y + 1))
            
    if player.hp <= 0:
        screen.blit(PLAYER_DEAD_IMG,(player.player_ch.x, player.player_ch.y))
    elif player.i_frame:
        if player.job == "Mage":
            screen.blit(player.mage_skin_hit, (player.player_ch.x, player.player_ch.y))
        elif player.job == "Knight":
            screen.blit(player.knight_skin_hit, (player.player_ch.x, player.player_ch.y))
        elif player.job == "Dragon":
            screen.blit(player.dragon_skin_hit, (player.player_ch.x, player.player_ch.y))
        else:
            screen.blit(PLAYER_HIT_IMG, (player.player_ch.x, player.player_ch.y))
    else:
        if player.job == "Mage":
            screen.blit(player.mage_skin, (player.player_ch.x, player.player_ch.y))
        elif player.job == "Knight":
            screen.blit(player.knight_skin, (player.player_ch.x, player.player_ch.y))
        elif player.job == "Dragon":
            screen.blit(player.dragon_skin, (player.player_ch.x, player.player_ch.y))
        else:
            screen.blit(PLAYER_IMG, (player.player_ch.x, player.player_ch.y))


    play_animations()
    display_all_projectile()

    pygame.draw.rect(screen, BLACK, JOB_ICON_EMPLACEMENT_IG)
    if player.job == "Mage":
        screen.blit(MAGE_ICON, (JOB_ICON_EMPLACEMENT_IG.x + 1, JOB_ICON_EMPLACEMENT_IG.y + 1))
    elif player.job == "Knight":
        screen.blit(KNIGHT_ICON, (JOB_ICON_EMPLACEMENT_IG.x + 1, JOB_ICON_EMPLACEMENT_IG.y + 1))
    elif player.job == "Dragon":
        screen.blit(DRAGON_ICON, (JOB_ICON_EMPLACEMENT_IG.x + 1, JOB_ICON_EMPLACEMENT_IG.y + 1))
    

    pygame.display.update()


def main_game():
    click = False
    game.main_on = True
    left = False
    right = False
    special = False
    down = False
    jump = False
    player.ground = False
    stomp = False
    dash = False
    game.restart = False
    game.pause = True
    game.start_timer = time.time()
    projectile.projectile_timer = time.time()
    projectile.heal_timer = time.time()
    projectile.coin_timer = time.time()
    while game.main_on:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        if game.game_over == False:
            rank_award()

        quest_database.update("game_on")


        if game.game_over == False and game.pause == False:
            game.timer = time.time() - game.start_timer
            check_best_timer()

            # Go Left
            if left and stomp == False and player.charge == False:
                if player.player_ch.x > 0:
                    player.player_ch.x -= player.speed * player.speed_multiplier

            # Go Right
            if right and stomp == False and player.charge == False:
                if player.player_ch.right < LIMIT.left:
                    player.player_ch.x += player.speed * player.speed_multiplier

            # Specials
            if special or (jump and player.double_jump == False and stomp == False and player.special_type == "Slowfall"):

                # Mage
                if player.special_type == "Slowfall":
                    if player.jump_velocity < 0:
                        player.slowfall = True
                        animations.list.append({"type" : "slowfall", "x" : player.player_ch.x, "y" : player.player_ch.bottom - SLOWFALL_FX.get_height()//4, "max_frame" : 0, "current_frame" : 0})
                        player.jump_velocity_multiplier = 0.5
                    else:
                        player.slowfall = False
                
                # Knight
                elif player.special_type == "Shield Up":
                    if time.time() - player.special_timer >= player.special_cd:
                        player.immune = True
                        player.special_timer = time.time()
                        player.shield_up = True

                # Dragon
                elif player.special_type == "Roar":
                    if time.time() - player.special_timer >= player.special_cd:
                        player.special_timer = time.time()
                        to_be_removed = []
                        for bullet in projectile.list:
                            if bullet["type"] == "basic" or bullet["type"] == "ground":
                                dist_to_player = int(math.dist((player.player_ch.x, player.player_ch.y),(bullet["rect"].x, bullet["rect"].y)))
                                if dist_to_player <= player.roar_radius:
                                    to_be_removed.append(bullet)
                        if len(to_be_removed) > 0:
                            for bullet in to_be_removed:
                                projectile.list.remove(bullet)
            else:
                player.slowfall = False

            # Stomp
            if down:
                if player.ground == False:
                    player.jump_velocity = -(player.jump_power * 2.5)
                    stomp = True

            # Jumping and double jump
            if jump and player.ground:
                player.jump_velocity = player.jump_power
                player.ground = False
            elif jump and player.double_jump and player.ground == False and stomp == False:
                if player.job == "Dragon" and player.endurance >= 10:
                    player.grounded = False
                    player.grounded_timer = 0
                    player.jump_velocity = player.jump_power
                    player.endurance -= 25
                elif player.job != "Dragon":
                    player.jump_velocity = player.jump_power * player.double_jump_multiplier
                    player.double_jump = False
                    animations.list.append({"type" : "double_jump", "x" : player.player_ch.x, "y" : player.player_ch.centery, "max_frame" : 8, "current_frame" : 0})

            # Falling
            if player.ground == False and player.charge == False:
                player.player_ch.y -= player.jump_velocity * player.jump_velocity_multiplier
                player.jump_velocity -= 0.5 * player.jump_velocity_multiplier
                if player.player_ch.y < TOP_BAND.bottom:
                    player.player_ch.y = TOP_BAND.bottom
                    player.jump_velocity /= 5

            # Touch ground
            if player.player_ch.colliderect(GROUND):
                player.jump_velocity = 0
                player.ground = True
                player.player_ch.bottom = GROUND.top
                if stomp:
                    animations.list.append({"type" : "stomp", "x" : player.player_ch.x, "y" : player.player_ch.centery, "max_frame" : 15, "current_frame" : 0})
                stomp = False
                player.double_jump = True
                if player.job == "Dragon":
                    player.grounded = True
                    player.grounded_timer = time.time()

            # Dragon logic
            if player.job == "Dragon":
                # Endurance regen/timer
                if player.grounded and time.time() - player.grounded_timer >= 0.5 and player.endurance < 100:
                    player.endurance += 25
                    player.grounded_timer = time.time()
                    if player.endurance > 100:
                        player.endurance = 100
                # Soar logic
                if player.soar and player.player_ch.y <= TOP_BAND.bottom + 100:
                    player.soar = False
                    player.jump_velocity /= 5


            # Mage dash preview update (Can probably move it elsewhere)
            if time.time() - player.dash_timer >= player.dash_cd:
                player.dash_phantom.x = player.player_ch.x + player.dash_power
                if player.dash_phantom.right > LIMIT.x:
                    player.dash_phantom.x = LIMIT.x - player.dash_phantom.width
                player.dash_phantom.y = player.player_ch.y

            # Dash Logic
            if dash:
                if time.time() - player.dash_timer >= player.dash_cd:
                    if player.dash_type == "Warp":
                        animations.list.append({"type" : "dash", "x" : player.player_ch.x, "y" : player.player_ch.y, "max_frame" : 16, "current_frame" : 0})
                        player.dash_timer = time.time()
                        player.player_ch.x += player.dash_power
                        if player.player_ch.x > LIMIT.x:
                            player.player_ch.right = LIMIT.x
                        animations.list.append({"type" : "afterdash", "x" : player.player_ch.x, "y" : player.player_ch.y, "max_frame" : 16, "current_frame" : 0})
                    elif player.dash_type == "Charge":
                        player.charge = True
                        player.immune = True
                        player.dash_timer = time.time()
                        player.charge_end = player.player_ch.x + player.dash_power
                        player.jump_velocity = 0
                        if player.charge_end > LIMIT.x:
                            player.charge_end = LIMIT.x - player.player_ch.width - 5
                    elif player.dash_type == "Soar":
                        player.soar = True
                        player.dash_timer = time.time()
                        player.ground = False
                        player.jump_velocity = player.dash_power

            # Knight Dash logic (need to fix endless dash)
            if player.charge:
                player.player_ch.x += player.dash_power//25
                if player.player_ch.x >= player.charge_end or time.time() - player.dash_timer >= 0.75:
                    player.charge = False
                if player.player_ch.right >= LIMIT.x:
                    player.player_ch.right = LIMIT.x

            # i-frame logic
            if player.i_frame:
                if time.time() - player.i_frame_timer >= player.i_frame_duration:
                    player.i_frame = False

            # Knight active logic
            if player.shield_up:
                if time.time() - player.special_timer >= player.special_duration:
                    player.shield_up = False
                    player.immune = False

            # Knight immunity reset (failsafe)
            if player.shield_up == False and player.charge == False:
                player.immune = False

            check_collision()

            # Game over processing / saving
            if player.hp <= 0:
                game.game_over = True
                rank_award()
                animations.list.append({"type" : "death", "max_frame" : 30, "current_frame" : 0})
                game.player_old_gold = player.gold
                player.gold += game.run_gold

                for entry in game.ranking_list:
                    if entry["name"] == game.player_name:
                        if game.best_time_ever > entry["time"]:
                            entry["time"] = game.best_time_ever
                            entry["job"] = player.job
                        if player.job == "Mage":
                            if game.best_time > entry["best_time_mage"]:
                                entry["best_time_mage"] = game.best_time
                                player.best_time_mage = game.best_time
                        elif player.job == "Knight":
                            if game.best_time > entry["best_time_knight"]:
                                entry["best_time_knight"] = game.best_time
                                player.best_time_knight = game.best_time
                        elif player.job == "Dragon":
                            if game.best_time > entry["best_time_dragon"]:
                                entry["best_time_dragon"] = game.best_time
                                player.best_time_dragon = game.best_time
                        entry["gold"] = player.gold

                with open("dodge_save.txt", "wb") as f:
                    pickle.dump(game.ranking_list, f)

            # Projectiles spawner
            if time.time() - projectile.projectile_timer >= projectile.projectile_frequency:
                projectile.projectile_timer = time.time()
                projectile_logic()
            
            # Healing item generator
            if time.time() - projectile.heal_timer >= projectile.heal_cd:
                projectile.heal_timer = time.time()
                generate_health_pick_up()

            # Coin generator    
            if time.time() - projectile.coin_timer >= projectile.projectile_frequency * 3:
                projectile.coin_timer = time.time()
                generate_coins()


            update_all_projectile()

            # reset
            player.jump_velocity_multiplier = 1
            dash = False
            if player.double_jump:
                jump = False


        # Restart button
        if (RESTART_BUTTON.collidepoint((mx,my)) and click) or game.restart:
            restart_game()

        # Game over trigger    
        if game.game_over and animations.list == []:
            game_over()

        # Ranking logic
        reorder_ranking()
        get_ranking_info()


        # Event handler
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    player.hp = 0
                elif game.pause:
                    game.start_timer = time.time()
                    projectile.projectile_timer = time.time()
                    projectile.heal_timer = time.time()
                    game.pause = False
                else:
                    if event.key == settings.go_left_key:
                        left = True
                    if event.key == settings.go_right_key:
                        right = True
                    if event.key == settings.jump_key:
                        jump = True
                    if event.key == settings.stomp_key:
                        down = True
                    if event.key == settings.dash_key:
                        dash = True
                    if event.key == settings.special_key:
                        special = True
                    if event.key == settings.restart_key:
                        game.restart = True
            if event.type == KEYUP:
                if event.key == settings.go_left_key:
                    left = False
                if event.key == settings.go_right_key:
                    right = False
                if event.key == settings.jump_key:
                    jump = False
                if event.key == settings.stomp_key:
                    down = False
                if event.key == settings.special_key:
                    special = False
        
        if game.main_on:
            main_game_draw_window()


def game_over_draw_window():
    update_bg()
    
    rank_text = font.render(f"Rank :", 1, WHITE)
    screen.blit(rank_text, (WIDTH//2 + 75, RANK_IMG_EMPLACEMENT_BIS.centery - rank_text.get_height()))
    rank_bis_text = big_font.render(f"{player.rank_name}", 1, WHITE)
    screen.blit(rank_bis_text, (WIDTH//2 + 85 + rank_text.get_width(), RANK_IMG_EMPLACEMENT_BIS.centery - rank_bis_text.get_height() + 3))
    if player.rank_img != None:
        screen.blit(player.rank_img, (WIDTH//2 + 100 + rank_text.get_width() + rank_bis_text.get_width(), RANK_IMG_EMPLACEMENT_BIS.y - rank_bis_text.get_height()//2))
        

    survived_time_text = big_font.render(f"{game.timer:.2f}s", 1, WHITE)
    screen.blit(survived_time_text, (WIDTH//2 - 50 - survived_time_text.get_width(), RANK_IMG_EMPLACEMENT_BIS.centery - survived_time_text.get_height() + 1))
    survived_text = font.render(f"You survived for :", 1, WHITE)
    screen.blit(survived_text, (WIDTH//2 - 60 - survived_text.get_width() - survived_time_text.get_width(), RANK_IMG_EMPLACEMENT_BIS.centery - survived_text.get_height()))
    if game.new_best:
        new_best_text = small_font.render("New Best Time !", 1, GREEN)
        screen.blit(new_best_text, (WIDTH//2 - 60 - survived_text.get_width()//2 - survived_time_text.get_width()//2 - new_best_text.get_width()//2, RANK_IMG_EMPLACEMENT_BIS.centery + 10))

    game_over_text = title_font.render("Game Over", 1, DARK_RED)
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//4))
        
    ranking_title_text = big_font.render("Ranking", 1, WHITE)
    screen.blit(ranking_title_text, (WIDTH//2 - ranking_title_text.get_width()//2, HEIGHT//4 + game_over_text.get_height() + 25))

    pygame.draw.rect(screen, BLACK, RANKING_INDEX_HEAD)
    ranking_index_head_text = font.render("N°", 1, WHITE)
    screen.blit(ranking_index_head_text, (RANKING_INDEX_HEAD.centerx - ranking_index_head_text.get_width()//2, RANKING_INDEX_HEAD.centery - ranking_index_head_text.get_height()//2))
    pygame.draw.rect(screen, BLACK, RANKING_NAME_HEAD)
    ranking_name_head_text = font.render("Name", 1, WHITE)
    screen.blit(ranking_name_head_text, (RANKING_NAME_HEAD.centerx - ranking_name_head_text.get_width()//2, RANKING_NAME_HEAD.centery - ranking_name_head_text.get_height()//2))
    pygame.draw.rect(screen, BLACK, RANKING_TIME_HEAD)
    ranking_time_head_text = font.render("Time", 1, WHITE)
    screen.blit(ranking_time_head_text, (RANKING_TIME_HEAD.centerx - ranking_time_head_text.get_width()//2, RANKING_TIME_HEAD.centery - ranking_time_head_text.get_height()//2))
    pygame.draw.rect(screen, BLACK, RANKING_JOB_HEAD)
    ranking_job_head_text = font.render("Job", 1, WHITE)
    screen.blit(ranking_job_head_text, (RANKING_JOB_HEAD.centerx - ranking_job_head_text.get_width()//2, RANKING_JOB_HEAD.centery - ranking_job_head_text.get_height()//2))

    pygame.draw.rect(screen, BLACK, RANKING_INDEX_COLUMN)
    pygame.draw.rect(screen, BLACK, RANKING_NAME_COLUMN)
    pygame.draw.rect(screen, BLACK, RANKING_TIME_COLUMN)
    pygame.draw.rect(screen, BLACK, RANKING_JOB_COLUMN)

    top_3 = False
    rank_1 = False
    if len(game.ranking_list) >= 1:
        if game.ranking_list[0]["name"] == game.player_name:
            top_3 = True
            rank_1 = True
            rank_one_index_text = font.render(f"1", 1, GREEN)
            screen.blit(rank_one_index_text, (RANKING_INDEX_COLUMN.centerx - rank_one_index_text.get_width()//2, RANKING_INDEX_COLUMN.y + 10))
            rank_one_name_text = font.render(f"{game.ranking_list[0]['name']}", 1, GREEN)
            screen.blit(rank_one_name_text, (RANKING_NAME_COLUMN.centerx - rank_one_name_text.get_width()//2, RANKING_NAME_COLUMN.y + 10))
            rank_one_time_text = font.render(f"{game.ranking_list[0]['time']:.2f}s", 1, GREEN)
            screen.blit(rank_one_time_text, (RANKING_TIME_COLUMN.centerx - rank_one_time_text.get_width()//2, RANKING_TIME_COLUMN.y + 10))
            rank_one_job_text = font.render(f"{game.ranking_list[0]['job']}", 1, GREEN)
            screen.blit(rank_one_job_text, (RANKING_JOB_COLUMN.centerx - rank_one_job_text.get_width()//2, RANKING_JOB_COLUMN.y + 10))
        else:
            rank_one_index_text = font.render(f"1", 1, WHITE)
            screen.blit(rank_one_index_text, (RANKING_INDEX_COLUMN.centerx - rank_one_index_text.get_width()//2, RANKING_INDEX_COLUMN.y + 10))
            rank_one_name_text = font.render(f"{game.ranking_list[0]['name']}", 1, WHITE)
            screen.blit(rank_one_name_text, (RANKING_NAME_COLUMN.centerx - rank_one_name_text.get_width()//2, RANKING_NAME_COLUMN.y + 10))
            rank_one_time_text = font.render(f"{game.ranking_list[0]['time']:.2f}s", 1, WHITE)
            screen.blit(rank_one_time_text, (RANKING_TIME_COLUMN.centerx - rank_one_time_text.get_width()//2, RANKING_TIME_COLUMN.y + 10))
            rank_one_job_text = font.render(f"{game.ranking_list[0]['job']}", 1, WHITE)
            screen.blit(rank_one_job_text, (RANKING_JOB_COLUMN.centerx - rank_one_job_text.get_width()//2, RANKING_JOB_COLUMN.y + 10))

    if len(game.ranking_list) >= 2:
        if game.ranking_list[1]["name"] == game.player_name:
            top_3 = True
            rank_two_index_text = font.render(f"2", 1, GREEN)
            screen.blit(rank_two_index_text, (RANKING_INDEX_COLUMN.centerx - rank_two_index_text.get_width()//2, RANKING_INDEX_COLUMN.y + 40))
            rank_two_name_text = font.render(f"{game.ranking_list[1]['name']}", 1, GREEN)
            screen.blit(rank_two_name_text, (RANKING_NAME_COLUMN.centerx - rank_two_name_text.get_width()//2, RANKING_NAME_COLUMN.y + 40))
            rank_two_time_text = font.render(f"{game.ranking_list[1]['time']:.2f}s", 1, GREEN)
            screen.blit(rank_two_time_text, (RANKING_TIME_COLUMN.centerx - rank_two_time_text.get_width()//2, RANKING_TIME_COLUMN.y + 40))
            rank_two_job_text = font.render(f"{game.ranking_list[1]['job']}", 1, GREEN)
            screen.blit(rank_two_job_text, (RANKING_JOB_COLUMN.centerx - rank_two_job_text.get_width()//2, RANKING_JOB_COLUMN.y + 40))
        else:
            rank_two_index_text = font.render(f"2", 1, WHITE)
            screen.blit(rank_two_index_text, (RANKING_INDEX_COLUMN.centerx - rank_two_index_text.get_width()//2, RANKING_INDEX_COLUMN.y + 40))
            rank_two_name_text = font.render(f"{game.ranking_list[1]['name']}", 1, WHITE)
            screen.blit(rank_two_name_text, (RANKING_NAME_COLUMN.centerx - rank_two_name_text.get_width()//2, RANKING_NAME_COLUMN.y + 40))
            rank_two_time_text = font.render(f"{game.ranking_list[1]['time']:.2f}s", 1, WHITE)
            screen.blit(rank_two_time_text, (RANKING_TIME_COLUMN.centerx - rank_two_time_text.get_width()//2, RANKING_TIME_COLUMN.y + 40))
            rank_two_job_text = font.render(f"{game.ranking_list[1]['job']}", 1, WHITE)
            screen.blit(rank_two_job_text, (RANKING_JOB_COLUMN.centerx - rank_two_job_text.get_width()//2, RANKING_JOB_COLUMN.y + 40))

    if len(game.ranking_list) >= 3:
        if game.ranking_list[2]["name"] == game.player_name:
            top_3 = True
            rank_three_index_text = font.render(f"3", 1, GREEN)
            screen.blit(rank_three_index_text, (RANKING_INDEX_COLUMN.centerx - rank_three_index_text.get_width()//2, RANKING_INDEX_COLUMN.y + 70))
            rank_three_name_text = font.render(f"{game.ranking_list[2]['name']}", 1, GREEN)
            screen.blit(rank_three_name_text, (RANKING_NAME_COLUMN.centerx - rank_three_name_text.get_width()//2, RANKING_NAME_COLUMN.y + 70))
            rank_three_time_text = font.render(f"{game.ranking_list[2]['time']:.2f}s", 1, GREEN)
            screen.blit(rank_three_time_text, (RANKING_TIME_COLUMN.centerx - rank_three_time_text.get_width()//2, RANKING_TIME_COLUMN.y + 70))
            rank_three_job_text = font.render(f"{game.ranking_list[2]['job']}", 1, GREEN)
            screen.blit(rank_three_job_text, (RANKING_JOB_COLUMN.centerx - rank_three_job_text.get_width()//2, RANKING_JOB_COLUMN.y + 70))
        else:
            rank_three_index_text = font.render(f"3", 1, WHITE)
            screen.blit(rank_three_index_text, (RANKING_INDEX_COLUMN.centerx - rank_three_index_text.get_width()//2, RANKING_INDEX_COLUMN.y + 70))
            rank_three_name_text = font.render(f"{game.ranking_list[2]['name']}", 1, WHITE)
            screen.blit(rank_three_name_text, (RANKING_NAME_COLUMN.centerx - rank_three_name_text.get_width()//2, RANKING_NAME_COLUMN.y + 70))
            rank_three_time_text = font.render(f"{game.ranking_list[2]['time']:.2f}s", 1, WHITE)
            screen.blit(rank_three_time_text, (RANKING_TIME_COLUMN.centerx - rank_three_time_text.get_width()//2, RANKING_TIME_COLUMN.y + 70))
            rank_three_job_text = font.render(f"{game.ranking_list[2]['job']}", 1, WHITE)
            screen.blit(rank_three_job_text, (RANKING_JOB_COLUMN.centerx - rank_three_job_text.get_width()//2, RANKING_JOB_COLUMN.y + 70))

    if top_3:
        if rank_1:
            self_rank_one_text = font.render("You are Rank 1 !", 1, GREEN)
            text_rect = self_rank_one_text.get_rect()
            text_rect.x = WIDTH//2 - self_rank_one_text.get_width()//2 - 5
            text_rect.y = RANKING_TIME_COLUMN.bottom - 70
            text_rect.width += 10
            text_rect.height += 10
            pygame.draw.rect(screen, DARK_GRAY, text_rect)
            pygame.draw.rect(screen, BLACK, (text_rect.x + 1, text_rect.y + 1, text_rect.w - 2, text_rect.h - 2))
            #screen.blit(pygame.transform.scale(PANEL_IMG, (text_rect.width - 2, text_rect.height - 2)), (text_rect.x + 1, text_rect.y + 1))
            screen.blit(self_rank_one_text, (text_rect.x + 5, text_rect.y + 5))
    else:
        next_in_rank_index_text = font.render(f"{game.next_in_rank_index}", 1, WHITE)
        screen.blit(next_in_rank_index_text, (RANKING_INDEX_COLUMN.centerx - next_in_rank_index_text.get_width()//2, RANKING_INDEX_COLUMN.y + 115))
        next_in_rank_name_text = font.render(f"{game.next_in_rank_name}", 1, WHITE)
        screen.blit(next_in_rank_name_text, (RANKING_NAME_COLUMN.centerx - next_in_rank_name_text.get_width()//2, RANKING_NAME_COLUMN.y + 115))
        next_in_rank_time_text = font.render(f"{game.next_in_rank_time:.2f}s", 1, WHITE)
        screen.blit(next_in_rank_time_text, (RANKING_TIME_COLUMN.centerx - next_in_rank_time_text.get_width()//2, RANKING_TIME_COLUMN.y + 115))
        next_in_rank_job_text = font.render(f"{game.next_in_rank_job}", 1, WHITE)
        screen.blit(next_in_rank_job_text, (RANKING_JOB_COLUMN.centerx - next_in_rank_job_text.get_width()//2, RANKING_JOB_COLUMN.y + 115))

        player_rank_index_text = font.render(f"{game.player_rank_number}", 1, GREEN)
        screen.blit(player_rank_index_text, (RANKING_INDEX_COLUMN.centerx - player_rank_index_text.get_width()//2, RANKING_INDEX_COLUMN.y + 145))
        player_rank_name_text = font.render(f"{game.player_name}", 1, GREEN)
        screen.blit(player_rank_name_text, (RANKING_NAME_COLUMN.centerx - player_rank_name_text.get_width()//2, RANKING_NAME_COLUMN.y + 145))
        player_rank_time_text = font.render(f"{game.best_time_ever:.2f}s", 1, GREEN)
        screen.blit(player_rank_time_text, (RANKING_TIME_COLUMN.centerx - player_rank_time_text.get_width()//2, RANKING_TIME_COLUMN.y + 145))
        player_rank_job_text = font.render(f"{game.player_best_time_job}", 1, GREEN)
        screen.blit(player_rank_job_text, (RANKING_JOB_COLUMN.centerx - player_rank_job_text.get_width()//2, RANKING_JOB_COLUMN.y + 145))


    gold_title_text = big_font.render("Gold :", 1, WHITE)
    screen.blit(gold_title_text, (15, GAME_OVER_GOLD_RECAP.y - gold_title_text.get_height() - 10))

    pygame.draw.rect(screen, RED, GAME_OVER_GOLD_RECAP)
    screen.blit(pygame.transform.scale(PANEL_IMG, (GAME_OVER_GOLD_RECAP.w - 2, GAME_OVER_GOLD_RECAP.h - 2)), (GAME_OVER_GOLD_RECAP.x + 1, GAME_OVER_GOLD_RECAP.y + 1))
    pygame.draw.rect(screen, GRAY, GAME_OVER_GOLD_DIV)

    old_gold_text = small_font.render(f"Old gold :", 1, WHITE)
    screen.blit(old_gold_text, (GAME_OVER_GOLD_RECAP.x + 5, GAME_OVER_GOLD_RECAP.y + 15))
    old_gold_text_2 = small_font.render(f"{game.player_old_gold}", 1, WHITE)
    screen.blit(old_gold_text_2, (GAME_OVER_GOLD_RECAP.right - COIN_IMG.get_width() - old_gold_text_2.get_width() - 10, GAME_OVER_GOLD_RECAP.y + 15))

    run_gold_text = small_font.render(f"Collected gold :", 1, WHITE)
    screen.blit(run_gold_text, (GAME_OVER_GOLD_RECAP.x + 5, GAME_OVER_GOLD_RECAP.y + 45))
    run_gold_text_2 = small_font.render(f"+ {game.run_gold}", 1, WHITE)
    screen.blit(run_gold_text_2, (GAME_OVER_GOLD_RECAP.right - COIN_IMG.get_width() - run_gold_text_2.get_width() - 10, GAME_OVER_GOLD_RECAP.y + 45))

    quest_gold_text = small_font.render(f"Quest gold :", 1, WHITE)
    screen.blit(quest_gold_text, (GAME_OVER_GOLD_RECAP.x + 5, GAME_OVER_GOLD_RECAP.y + 75))
    quest_gold_text_2 = small_font.render(f"+ {quest_database.quest_reward}", 1, WHITE)
    screen.blit(quest_gold_text_2, (GAME_OVER_GOLD_RECAP.right - COIN_IMG.get_width() - quest_gold_text_2.get_width() - 10, GAME_OVER_GOLD_RECAP.y + 75))

    total_gold_text_1 = small_font.render(f"Total gold :", 1, WHITE)
    screen.blit(total_gold_text_1, (GAME_OVER_GOLD_RECAP.x + 5, GAME_OVER_GOLD_DIV.y + 5 + total_gold_text_1.get_height()//2))
    total_gold_text_2 = small_font.render(f"{player.gold}", 1, WHITE)
    screen.blit(total_gold_text_2, (GAME_OVER_GOLD_RECAP.right - COIN_IMG.get_width() - total_gold_text_2.get_width() - 10, GAME_OVER_GOLD_DIV.y + 5 + total_gold_text_2.get_height()//2))

    screen.blit(COIN_IMG, (GAME_OVER_GOLD_RECAP.right - COIN_IMG.get_width() - 5, GAME_OVER_GOLD_RECAP.bottom - COIN_IMG.get_height() - 5))


    pygame.draw.rect(screen, BLACK, JOB_ICON_EMPLACEMENT_GO)
    if player.job == "Mage":
        screen.blit(MAGE_ICON, (JOB_ICON_EMPLACEMENT_GO.x + 1, JOB_ICON_EMPLACEMENT_GO.y + 1))
    elif player.job == "Knight":
        screen.blit(KNIGHT_ICON, (JOB_ICON_EMPLACEMENT_GO.x + 1, JOB_ICON_EMPLACEMENT_GO.y + 1))
    elif player.job == "Dragon":
        screen.blit(DRAGON_ICON, (JOB_ICON_EMPLACEMENT_GO.x + 1, JOB_ICON_EMPLACEMENT_GO.y + 1))
        
    pygame.draw.rect(screen, RED, CHANGE_JOB_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (CHANGE_JOB_BUTTON.width - 2, CHANGE_JOB_BUTTON.height - 2)), (CHANGE_JOB_BUTTON.x + 1, CHANGE_JOB_BUTTON.y + 1))
    change_job_text = font.render("Change Job", 1, WHITE)
    screen.blit(change_job_text, (CHANGE_JOB_BUTTON.centerx - change_job_text.get_width()//2, CHANGE_JOB_BUTTON.centery - change_job_text.get_height()//2))
    
    pygame.draw.rect(screen, RED, RETRY_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RETRY_BUTTON.width - 2, RETRY_BUTTON.height - 2)), (RETRY_BUTTON.x + 1, RETRY_BUTTON.y + 1))
    retry_text = font.render("Retry", 1, WHITE)
    screen.blit(retry_text, (RETRY_BUTTON.centerx - retry_text.get_width()//2, RETRY_BUTTON.centery - retry_text.get_height()//2))

    quest_title = big_font.render("Quest :", 1, WHITE)
    screen.blit(quest_title, (15, Q1_EMPLACEMENT.top - quest_title.get_height() - 10))

    pygame.draw.rect(screen, RED, Q1_EMPLACEMENT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (Q1_EMPLACEMENT.w - 2, Q1_EMPLACEMENT.h - 2)), (Q1_EMPLACEMENT.x + 1, Q1_EMPLACEMENT.y + 1))
    pygame.draw.rect(screen, RED, Q2_EMPLACEMENT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (Q2_EMPLACEMENT.w - 2, Q2_EMPLACEMENT.h - 2)), (Q2_EMPLACEMENT.x + 1, Q2_EMPLACEMENT.y + 1))
    pygame.draw.rect(screen, RED, Q3_EMPLACEMENT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (Q3_EMPLACEMENT.w - 2, Q3_EMPLACEMENT.h - 2)), (Q3_EMPLACEMENT.x + 1, Q3_EMPLACEMENT.y + 1))

    quest_offset = 0
    for quest in player.quest_dic:
        if quest == "Q1":
            quest_text = small_font.render(f"{quest_database.Q1}", 1, WHITE)
            reward_text = small_font.render(f"Reward : {quest_database.Q1_reward} Gold", 1, WHITE)
        if quest == "Q2":
            quest_text = small_font.render(f"{quest_database.Q2}", 1, WHITE)
            reward_text = small_font.render(f"Reward : {quest_database.Q2_reward} Gold", 1, WHITE)
        if quest == "Q3":
            quest_text = small_font.render(f"{quest_database.Q3}", 1, WHITE)
            reward_text = small_font.render(f"Reward : {quest_database.Q3_reward} Gold", 1, WHITE)
        if quest == "Q4":
            quest_text = small_font.render(f"{quest_database.Q4}", 1, WHITE)
            reward_text = small_font.render(f"Reward : {quest_database.Q4_reward} Gold", 1, WHITE)
        if quest == "Q5":
            quest_text = small_font.render(f"{quest_database.Q5}", 1, WHITE)
            reward_text = small_font.render(f"Reward : {quest_database.Q5_reward} Gold", 1, WHITE)
        if player.quest_dic[quest] == "Completed !":
            completed_text = small_font.render("Completed !", 1, GREEN)
            screen.blit(completed_text, (Q1_EMPLACEMENT.right - completed_text.get_width() - 5, Q1_EMPLACEMENT.y + 25 + quest_offset))
        screen.blit(quest_text, (Q1_EMPLACEMENT.x + 5, Q1_EMPLACEMENT.y + 5 + quest_offset))
        screen.blit(reward_text, (Q1_EMPLACEMENT.x + 5, Q1_EMPLACEMENT.y + 25 + quest_offset))
        quest_offset += 70

    play_animations()

    pygame.display.update()

def game_over():
    run = True
    click = False
    animations.list.append({"type" : "wait", "max_frame" : 120, "current_frame" : 0})
    while run:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()
        
        quest_database.update("game_over")

        if (RETRY_BUTTON.collidepoint((mx,my)) and click) or game.restart:
            restart_game()
            run = False

        if CHANGE_JOB_BUTTON.collidepoint((mx,my)) and click:
            restart_game()
            run = False
            game.main_on = False
            
        if Q1_EMPLACEMENT.collidepoint((mx,my)) and click and animations.list == []:
            key_list = list(player.quest_dic)
            del player.quest_dic[key_list[0]]
        if Q2_EMPLACEMENT.collidepoint((mx,my)) and click and animations.list == []:
            key_list = list(player.quest_dic)
            del player.quest_dic[key_list[1]]
        if Q3_EMPLACEMENT.collidepoint((mx,my)) and click and animations.list == []:
            key_list = list(player.quest_dic)
            del player.quest_dic[key_list[2]]

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    restart_game()
                    run = False
                    game.main_on = False
                if event.key == K_r:
                    game.restart = True
                    run = False

        game_over_draw_window()
        
        for entry in game.ranking_list:
            if entry["name"] == game.player_name:
                entry["quest"] = player.quest_dic
                entry["gold"] = player.gold

        with open("dodge_save.txt", "wb") as f:
            pickle.dump(game.ranking_list, f)

def job_select_draw_window():
    update_bg()

    bg_title_text = bigger_font.render("Select Your Job", 1, DARK_RED)
    screen.blit(bg_title_text, (TITLE_EMPLACEMENT.centerx - bg_title_text.get_width()//2 + 1, TITLE_EMPLACEMENT.centery - bg_title_text.get_height()//2 + 2))
    title_text = bigger_font.render("Select Your Job", 1, WHITE)
    screen.blit(title_text, (TITLE_EMPLACEMENT.centerx - title_text.get_width()//2, TITLE_EMPLACEMENT.centery - title_text.get_height()//2))

    pygame.draw.rect(screen, DARK_GRAY, JOB_PREVIEW)
    screen.blit(pygame.transform.scale(PANEL_IMG, (JOB_PREVIEW.width - 2, JOB_PREVIEW.height - 2)), (JOB_PREVIEW.x + 1, JOB_PREVIEW.y + 1))

    if player.job == "Mage":
        pygame.draw.rect(screen, RED, MAGE_ICON_EMPLACEMENT)
        screen.blit(player.mage_skin, (JOB_PREVIEW.centerx - player.mage_skin.get_width()//2, JOB_PREVIEW.centery - player.mage_skin.get_height()//2))
    else:
        pygame.draw.rect(screen, BLACK, MAGE_ICON_EMPLACEMENT)
    screen.blit(pygame.transform.scale(MAGE_ICON, (60,60)), (MAGE_ICON_EMPLACEMENT.x + 1, MAGE_ICON_EMPLACEMENT.y + 1))

    if player.job == "Knight":
        pygame.draw.rect(screen, RED, KNIGHT_ICON_EMPLACEMENT)
        screen.blit(player.knight_skin, (JOB_PREVIEW.centerx - player.knight_skin.get_width()//2, JOB_PREVIEW.centery - player.knight_skin.get_height()//2))
    else:
        pygame.draw.rect(screen, BLACK, KNIGHT_ICON_EMPLACEMENT)
    screen.blit(pygame.transform.scale(KNIGHT_ICON, (60,60)), (KNIGHT_ICON_EMPLACEMENT.x + 1, KNIGHT_ICON_EMPLACEMENT.y + 1))

    if player.job == "Dragon":
        pygame.draw.rect(screen, RED, JOB3_ICON_EMPLACEMENT)
        screen.blit(player.dragon_skin, (JOB_PREVIEW.centerx - player.dragon_skin.get_width()//2, JOB_PREVIEW.centery - player.dragon_skin.get_height()//2))
    else:
        pygame.draw.rect(screen, BLACK, JOB3_ICON_EMPLACEMENT)
    screen.blit(pygame.transform.scale(DRAGON_ICON, (60,60)), (JOB3_ICON_EMPLACEMENT.x + 1, JOB3_ICON_EMPLACEMENT.y + 1))

    if player.job == "Job4":
        pygame.draw.rect(screen, RED, JOB4_ICON_EMPLACEMENT)
        #screen.blit(KNIGHT_IMG, (JOB_PREVIEW.centerx - KNIGHT_IMG.get_width()//2, JOB_PREVIEW.centery - KNIGHT_IMG.get_height()//2))
    else:
        pygame.draw.rect(screen, BLACK, JOB4_ICON_EMPLACEMENT)
    #screen.blit(pygame.transform.scale(KNIGHT_ICON, (60,60)), (JOB4_ICON_EMPLACEMENT.x + 1, JOB4_ICON_EMPLACEMENT.y + 1))

    pygame.draw.rect(screen, RED, BACK_BUTTON_B_LEFT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (BACK_BUTTON_B_LEFT.width - 2, BACK_BUTTON_B_LEFT.height - 2)), (BACK_BUTTON_B_LEFT.x + 1, BACK_BUTTON_B_LEFT.y + 1))
    back_text = font.render("Back", 1, WHITE)
    screen.blit(back_text, (BACK_BUTTON_B_LEFT.centerx - back_text.get_width()//2, BACK_BUTTON_B_LEFT.centery - back_text.get_height()//2))

    pygame.draw.rect(screen, RED, PLAY_JOB_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (PLAY_JOB_BUTTON.width - 2, PLAY_JOB_BUTTON.height - 2)), (PLAY_JOB_BUTTON.x + 1, PLAY_JOB_BUTTON.y + 1))
    play_text = font.render("Play", 1, WHITE)
    screen.blit(play_text, (PLAY_JOB_BUTTON.centerx - play_text.get_width()//2, PLAY_JOB_BUTTON.centery - play_text.get_height()//2))

    quest_title = big_font.render("Quest :", 1, WHITE)
    screen.blit(quest_title, (15, Q1_EMPLACEMENT.top - quest_title.get_height() - 10))

    pygame.draw.rect(screen, RED, Q1_EMPLACEMENT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (Q1_EMPLACEMENT.w - 2, Q1_EMPLACEMENT.h - 2)), (Q1_EMPLACEMENT.x + 1, Q1_EMPLACEMENT.y + 1))
    pygame.draw.rect(screen, RED, Q2_EMPLACEMENT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (Q2_EMPLACEMENT.w - 2, Q2_EMPLACEMENT.h - 2)), (Q2_EMPLACEMENT.x + 1, Q2_EMPLACEMENT.y + 1))
    pygame.draw.rect(screen, RED, Q3_EMPLACEMENT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (Q3_EMPLACEMENT.w - 2, Q3_EMPLACEMENT.h - 2)), (Q3_EMPLACEMENT.x + 1, Q3_EMPLACEMENT.y + 1))

    quest_offset = 0
    for quest in player.quest_dic:
        if quest == "Q1":
            quest_text = small_font.render(f"{quest_database.Q1}", 1, WHITE)
            reward_text = small_font.render(f"Reward : {quest_database.Q1_reward} Gold", 1, WHITE)
        if quest == "Q2":
            quest_text = small_font.render(f"{quest_database.Q2}", 1, WHITE)
            reward_text = small_font.render(f"Reward : {quest_database.Q2_reward} Gold", 1, WHITE)
        if quest == "Q3":
            quest_text = small_font.render(f"{quest_database.Q3}", 1, WHITE)
            reward_text = small_font.render(f"Reward : {quest_database.Q3_reward} Gold", 1, WHITE)
        if quest == "Q4":
            quest_text = small_font.render(f"{quest_database.Q4}", 1, WHITE)
            reward_text = small_font.render(f"Reward : {quest_database.Q4_reward} Gold", 1, WHITE)
        if quest == "Q5":
            quest_text = small_font.render(f"{quest_database.Q5}", 1, WHITE)
            reward_text = small_font.render(f"Reward : {quest_database.Q5_reward} Gold", 1, WHITE)
        screen.blit(quest_text, (Q1_EMPLACEMENT.x + 5, Q1_EMPLACEMENT.y + 5 + quest_offset))
        screen.blit(reward_text, (Q1_EMPLACEMENT.x + 5, Q1_EMPLACEMENT.y + 25 + quest_offset))
        quest_offset += 70


    pygame.draw.rect(screen, DARK_GRAY, STATS_RECT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (STATS_RECT.width - 2, STATS_RECT.height - 2)), (STATS_RECT.x + 1, STATS_RECT.y + 1))
    stats_text = big_font.render("Stats", 1, WHITE)
    screen.blit(stats_text, (STATS_RECT.centerx - stats_text.get_width()//2, STATS_RECT.y + 10))

    job_text = font.render(f"Job : {player.job}", 1, WHITE)
    screen.blit(job_text, (STATS_RECT.x + 10, STATS_RECT.y + 60))

    if player.job == "Mage":
        best_time = font.render(f"Best time : {player.best_time_mage:.2f}s", 1, WHITE)
    if player.job == "Knight":
        best_time = font.render(f"Best time : {player.best_time_knight:.2f}s", 1, WHITE)
    if player.job == "Dragon":
        best_time = font.render(f"Best time : {player.best_time_dragon:.2f}s", 1, WHITE)
    screen.blit(best_time, (STATS_RECT.x + 10, STATS_RECT.y + 100))

    active_text = font.render(f"Active : {player.special_type}", 1, WHITE)
    screen.blit(active_text, (STATS_RECT.x + 10, STATS_RECT.y + 140))
    active_desc = small_font.render(f"{player.special_desc_1}", 1, WHITE)
    screen.blit(active_desc, (STATS_RECT.x + 10, STATS_RECT.y + 170))
    active_desc = small_font.render(f"{player.special_desc_2}", 1, WHITE)
    screen.blit(active_desc, (STATS_RECT.x + 10, STATS_RECT.y + 190))

    dash_text = font.render(f"Dash : {player.dash_type}", 1, WHITE)
    screen.blit(dash_text, (STATS_RECT.x + 10, STATS_RECT.y + 230))
    active_desc = small_font.render(f"{player.dash_desc_1}", 1, WHITE)
    screen.blit(active_desc, (STATS_RECT.x + 10, STATS_RECT.y + 260))
    active_desc = small_font.render(f"{player.dash_desc_2}", 1, WHITE)
    screen.blit(active_desc, (STATS_RECT.x + 10, STATS_RECT.y + 280))

    pygame.display.update()

def job_select():
    run = True
    click = False
    while run:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        quest_database.update()

        if MAGE_ICON_EMPLACEMENT.collidepoint((mx,my)) and click:
            player.job = "Mage"
            switch_job()
            for entry in game.ranking_list:
                if entry["name"] == game.player_name:
                    game.best_time = entry["best_time_mage"]
        if KNIGHT_ICON_EMPLACEMENT.collidepoint((mx,my)) and click:
            player.job = "Knight"
            switch_job()
            for entry in game.ranking_list:
                if entry["name"] == game.player_name:
                    game.best_time = entry["best_time_knight"]
        if JOB3_ICON_EMPLACEMENT.collidepoint((mx,my)) and click:
            player.job = "Dragon"
            switch_job()
            for entry in game.ranking_list:
                if entry["name"] == game.player_name:
                    game.best_time = entry["best_time_dragon"]

        if Q1_EMPLACEMENT.collidepoint((mx,my)) and click:
            key_list = list(player.quest_dic)
            del player.quest_dic[key_list[0]]
        if Q2_EMPLACEMENT.collidepoint((mx,my)) and click:
            key_list = list(player.quest_dic)
            del player.quest_dic[key_list[1]]
        if Q3_EMPLACEMENT.collidepoint((mx,my)) and click:
            key_list = list(player.quest_dic)
            del player.quest_dic[key_list[2]]
            
        if PLAY_JOB_BUTTON.collidepoint((mx,my)) and click:
            main_game()
            for entry in game.ranking_list:
                if entry["name"] == game.player_name:
                    entry["quest"] = player.quest_dic

            with open("dodge_save.txt", "wb") as f:
                pickle.dump(game.ranking_list, f)
        if BACK_BUTTON_B_LEFT.collidepoint((mx,my)) and click:
            run = False

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

        job_select_draw_window()

##########
## SHOP ##

class shop:
    type = "Skin"
    page = "Mage"
    item = 0
    item_id = ""
    item_name = ""
    item_cost = 0
    item_state = ""
    description1 = ""
    description2 = ""
    description3 = ""
    description4 = ""
    description5 = ""
    
class shop_mage_skin_db:
    item_1 = MaHuRe_N_IMG
    item_1_hit = MaHuRe_H_IMG
    item_1_id = "MaHuRe"
    item_1_name = "Mage (Red)"
    item_1_cost = 50
    item_2 = MaHuDa_N_IMG
    item_2_hit = MaHuDa_H_IMG
    item_2_id = "MaHuDa"
    item_2_name = "Mage (Dark)"
    item_2_cost = 50
    item_3 = MaHuBl_N_IMG
    item_3_hit = MaHuBl_H_IMG
    item_3_id = "MaHuBl"
    item_3_name = "Archmage (Blue)"
    item_3_cost = 100
    item_4 = MaHuGr_N_IMG
    item_4_hit = MaHuGr_H_IMG
    item_4_id = "MaHuGr"
    item_4_name = "Archmage (Grey)"
    item_4_cost = 100

    item_5 = MaGoBa_N_IMG
    item_5_hit = MaGoBa_H_IMG
    item_5_id = "MaGoBa"
    item_5_name = "Goblin Mage"
    item_5_cost = 200
    item_6 = MaFoBa_N_IMG
    item_6_hit = MaFoBa_H_IMG
    item_6_id = "MaFoBa"
    item_6_name = "Fomorian Mage"
    item_6_cost = 200
    item_7 = MaFeGr_N_IMG
    item_7_hit = MaFeGr_H_IMG
    item_7_id = "MaFeGr"
    item_7_name = "Fallen Elf Mage"
    item_7_cost = 400
    item_8 = MaDeBl_N_IMG
    item_8_hit = MaDeBl_H_IMG
    item_8_id = "MaDeBl"
    item_8_name = "Drow Mage (M)"
    item_8_cost = 400

    item_9 = MaDeVi_N_IMG
    item_9_hit = MaDeVi_H_IMG
    item_9_id = "MaDeVi"
    item_9_name = "Drow Mage (F)"
    item_9_cost = 500
    item_10 = MaGnBa_N_IMG
    item_10_hit = MaGnBa_H_IMG
    item_10_id = "MaGnBa"
    item_10_name = "Gnome Mage"
    item_10_cost = 500
    item_11 = MaLiBl_N_IMG
    item_11_hit = MaLiBl_H_IMG
    item_11_id = "MaLiBl"
    item_11_name = "Lizardman Mage"
    item_11_cost = 600
    item_12 = MaSkBa_N_IMG
    item_12_hit = MaSkBa_H_IMG
    item_12_id = "MaSkBa"
    item_12_name = "Draugr Mage"
    item_12_cost = 750

    item_13 = MaWiGr_N_IMG
    item_13_hit = MaWiGr_H_IMG
    item_13_id = "MaWiGr"
    item_13_name = "Witch"
    item_13_cost = 1000
    item_14 = MaWiBl_N_IMG
    item_14_hit = MaWiBl_H_IMG
    item_14_id = "MaWiBl"
    item_14_name = "Iceborn Witch"
    item_14_cost = 1000
    item_15 = MaFaBa_N_IMG
    item_15_hit = MaFaBa_H_IMG
    item_15_id = "MaFaBa"
    item_15_name = "Fairy"
    item_15_cost = 1500
    item_16 = MaDvRe_N_IMG
    item_16_hit = MaDvRe_H_IMG
    item_16_id = "MaDvRe"
    item_16_name = "Little Devil"
    item_16_cost = 3000

class shop_knight_skin_db:
    item_1 = KnSpHuBl_N_IMG
    item_1_hit = KnSpHuBl_H_IMG
    item_1_id = "KnSpHuBl"
    item_1_name = "Spearman (Blue)"
    item_1_cost = 50
    item_2 = KnSpHuRe_N_IMG
    item_2_hit = KnSpHuRe_H_IMG
    item_2_id = "KnSpHuRe"
    item_2_name = "Spearman (Red)"
    item_2_cost = 50
    item_3 = KnSwHuBl_N_IMG
    item_3_hit = KnSwHuBl_H_IMG
    item_3_id = "KnSwHuBl"
    item_3_name = "Swordman (Blue)"
    item_3_cost = 100
    item_4 = KnSwHuRe_N_IMG
    item_4_hit = KnSwHuRe_H_IMG
    item_4_id = "KnSwHuRe"
    item_4_name = "Swordman (Red)"
    item_4_cost = 100

    item_5 = KnMaDwBl_N_IMG
    item_5_hit = KnMaDwBl_H_IMG
    item_5_id = "KnMaDwBl"
    item_5_name = "Dwarf (Blue)"
    item_5_cost = 200
    item_6 = KnMaDwRe_N_IMG
    item_6_hit = KnMaDwRe_H_IMG
    item_6_id = "KnMaDwRe"
    item_6_name = "Dwarf (Red)"
    item_6_cost = 200
    item_7 = KnSwFeBl_N_IMG
    item_7_hit = KnSwFeBl_H_IMG
    item_7_id = "KnSwFeBl"
    item_7_name = "Fallen Elf (Blue)"
    item_7_cost = 400
    item_8 = KnSwFeGr_N_IMG
    item_8_hit = KnSwFeGr_H_IMG
    item_8_id = "KnSwFeGr"
    item_8_name = "Fallen Elf (Grey)"
    item_8_cost = 400

    item_9 = KnSwArBl_N_IMG
    item_9_hit = KnSwArBl_H_IMG
    item_9_id = "KnSwArBl"
    item_9_name = "Living Armor (Blue)"
    item_9_cost = 500
    item_10 = KnSwArRe_N_IMG
    item_10_hit = KnSwArRe_H_IMG
    item_10_id = "KnSwArRe"
    item_10_name = "Living Armor (Red)"
    item_10_cost = 500
    item_11 = KnSwArGo_N_IMG
    item_11_hit = KnSwArGo_H_IMG
    item_11_id = "KnSwArGo"
    item_11_name = "Living Armor (Gold)"
    item_11_cost = 600
    item_12 = KnSwSkBa_N_IMG
    item_12_hit = KnSwSkBa_H_IMG
    item_12_id = "KnSwSkBa"
    item_12_name = "Draugr Soldier"
    item_12_cost = 750

    item_13 = KnSpLiBa_N_IMG
    item_13_hit = KnSpLiBa_H_IMG
    item_13_id = "KnSpLiBa"
    item_13_name = "Lizardman Soldier"
    item_13_cost = 1000
    item_14 = KnSpWoBa_N_IMG
    item_14_hit = KnSpWoBa_H_IMG
    item_14_id = "KnSpWoBa"
    item_14_name = "Wolfkin Soldier"
    item_14_cost = 1000
    item_15 = KnSpHuGr_N_IMG
    item_15_hit = KnSpHuGr_H_IMG
    item_15_id = "KnSpHuGr"
    item_15_name = "Elite Knight"
    item_15_cost = 1500
    item_16 = KnSpHuGo_N_IMG
    item_16_hit = KnSpHuGo_H_IMG
    item_16_id = "KnSpHuGo"
    item_16_name = "Royal Knight"
    item_16_cost = 3000

def retrieve_shopping_info():
    owned = False
    if shop.type == "Skin":
        if shop.page == "Mage":
            if shop.item == 1:
                shop.item_id = shop_mage_skin_db.item_1_id
                shop.item_name = shop_mage_skin_db.item_1_name
                shop.item_cost = shop_mage_skin_db.item_1_cost
                
            if shop.item == 2:
                shop.item_id = shop_mage_skin_db.item_2_id
                shop.item_name = shop_mage_skin_db.item_2_name
                shop.item_cost = shop_mage_skin_db.item_2_cost
                
            if shop.item == 3:
                shop.item_id = shop_mage_skin_db.item_3_id
                shop.item_name = shop_mage_skin_db.item_3_name
                shop.item_cost = shop_mage_skin_db.item_3_cost
                
            if shop.item == 4:
                shop.item_id = shop_mage_skin_db.item_4_id
                shop.item_name = shop_mage_skin_db.item_4_name
                shop.item_cost = shop_mage_skin_db.item_4_cost
                
            if shop.item == 5:
                shop.item_id = shop_mage_skin_db.item_5_id
                shop.item_name = shop_mage_skin_db.item_5_name
                shop.item_cost = shop_mage_skin_db.item_5_cost
                
            if shop.item == 6:
                shop.item_id = shop_mage_skin_db.item_6_id
                shop.item_name = shop_mage_skin_db.item_6_name
                shop.item_cost = shop_mage_skin_db.item_6_cost
                
            if shop.item == 7:
                shop.item_id = shop_mage_skin_db.item_7_id
                shop.item_name = shop_mage_skin_db.item_7_name
                shop.item_cost = shop_mage_skin_db.item_7_cost
                
            if shop.item == 8:
                shop.item_id = shop_mage_skin_db.item_8_id
                shop.item_name = shop_mage_skin_db.item_8_name
                shop.item_cost = shop_mage_skin_db.item_8_cost
                
            if shop.item == 9:
                shop.item_id = shop_mage_skin_db.item_9_id
                shop.item_name = shop_mage_skin_db.item_9_name
                shop.item_cost = shop_mage_skin_db.item_9_cost
                
            if shop.item == 10:
                shop.item_id = shop_mage_skin_db.item_10_id
                shop.item_name = shop_mage_skin_db.item_10_name
                shop.item_cost = shop_mage_skin_db.item_10_cost
                
            if shop.item == 11:
                shop.item_id = shop_mage_skin_db.item_11_id
                shop.item_name = shop_mage_skin_db.item_11_name
                shop.item_cost = shop_mage_skin_db.item_11_cost
                
            if shop.item == 12:
                shop.item_id = shop_mage_skin_db.item_12_id
                shop.item_name = shop_mage_skin_db.item_12_name
                shop.item_cost = shop_mage_skin_db.item_12_cost
                
            if shop.item == 13:
                shop.item_id = shop_mage_skin_db.item_13_id
                shop.item_name = shop_mage_skin_db.item_13_name
                shop.item_cost = shop_mage_skin_db.item_13_cost
                
            if shop.item == 14:
                shop.item_id = shop_mage_skin_db.item_14_id
                shop.item_name = shop_mage_skin_db.item_14_name
                shop.item_cost = shop_mage_skin_db.item_14_cost
                
            if shop.item == 15:
                shop.item_id = shop_mage_skin_db.item_15_id
                shop.item_name = shop_mage_skin_db.item_15_name
                shop.item_cost = shop_mage_skin_db.item_15_cost
                
            if shop.item == 16:
                shop.item_id = shop_mage_skin_db.item_16_id
                shop.item_name = shop_mage_skin_db.item_16_name
                shop.item_cost = shop_mage_skin_db.item_16_cost

            for skin in player.skin_mage_list:
                if skin == shop.item_id:
                    owned = True
                    
        if shop.page == "Knight":
            if shop.item == 1:
                shop.item_id = shop_knight_skin_db.item_1_id
                shop.item_name = shop_knight_skin_db.item_1_name
                shop.item_cost = shop_knight_skin_db.item_1_cost
                
            if shop.item == 2:
                shop.item_id = shop_knight_skin_db.item_2_id
                shop.item_name = shop_knight_skin_db.item_2_name
                shop.item_cost = shop_knight_skin_db.item_2_cost
                
            if shop.item == 3:
                shop.item_id = shop_knight_skin_db.item_3_id
                shop.item_name = shop_knight_skin_db.item_3_name
                shop.item_cost = shop_knight_skin_db.item_3_cost
                
            if shop.item == 4:
                shop.item_id = shop_knight_skin_db.item_4_id
                shop.item_name = shop_knight_skin_db.item_4_name
                shop.item_cost = shop_knight_skin_db.item_4_cost
                
            if shop.item == 5:
                shop.item_id = shop_knight_skin_db.item_5_id
                shop.item_name = shop_knight_skin_db.item_5_name
                shop.item_cost = shop_knight_skin_db.item_5_cost
                
            if shop.item == 6:
                shop.item_id = shop_knight_skin_db.item_6_id
                shop.item_name = shop_knight_skin_db.item_6_name
                shop.item_cost = shop_knight_skin_db.item_6_cost
                
            if shop.item == 7:
                shop.item_id = shop_knight_skin_db.item_7_id
                shop.item_name = shop_knight_skin_db.item_7_name
                shop.item_cost = shop_knight_skin_db.item_7_cost
                
            if shop.item == 8:
                shop.item_id = shop_knight_skin_db.item_8_id
                shop.item_name = shop_knight_skin_db.item_8_name
                shop.item_cost = shop_knight_skin_db.item_8_cost
                
            if shop.item == 9:
                shop.item_id = shop_knight_skin_db.item_9_id
                shop.item_name = shop_knight_skin_db.item_9_name
                shop.item_cost = shop_knight_skin_db.item_9_cost
                
            if shop.item == 10:
                shop.item_id = shop_knight_skin_db.item_10_id
                shop.item_name = shop_knight_skin_db.item_10_name
                shop.item_cost = shop_knight_skin_db.item_10_cost
                
            if shop.item == 11:
                shop.item_id = shop_knight_skin_db.item_11_id
                shop.item_name = shop_knight_skin_db.item_11_name
                shop.item_cost = shop_knight_skin_db.item_11_cost
                
            if shop.item == 12:
                shop.item_id = shop_knight_skin_db.item_12_id
                shop.item_name = shop_knight_skin_db.item_12_name
                shop.item_cost = shop_knight_skin_db.item_12_cost
                
            if shop.item == 13:
                shop.item_id = shop_knight_skin_db.item_13_id
                shop.item_name = shop_knight_skin_db.item_13_name
                shop.item_cost = shop_knight_skin_db.item_13_cost
                
            if shop.item == 14:
                shop.item_id = shop_knight_skin_db.item_14_id
                shop.item_name = shop_knight_skin_db.item_14_name
                shop.item_cost = shop_knight_skin_db.item_14_cost
                
            if shop.item == 15:
                shop.item_id = shop_knight_skin_db.item_15_id
                shop.item_name = shop_knight_skin_db.item_15_name
                shop.item_cost = shop_knight_skin_db.item_15_cost
                
            if shop.item == 16:
                shop.item_id = shop_knight_skin_db.item_16_id
                shop.item_name = shop_knight_skin_db.item_16_name
                shop.item_cost = shop_knight_skin_db.item_16_cost

            for skin in player.skin_knight_list:
                if skin == shop.item_id:
                    owned = True


    if owned == True:
        shop.item_state = "Owned"
    else:
        shop.item_state = ""

def reset_shopping_info():
    shop.page = ""
    shop.item = 0
    shop.item_id = ""
    shop.item_name = ""
    shop.item_cost = 0
    shop.item_state = ""
    shop.description1 = ""
    shop.description2 = ""
    shop.description3 = ""
    shop.description4 = ""
    shop.description5 = ""

def select_skin():
    if shop.item_state == "Owned":
        if shop.type == "Skin":
            if shop.page == "Mage":
                if shop.item == 1:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_1
                    player.mage_skin_hit = shop_mage_skin_db.item_1_hit
                    
                if shop.item == 2:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_2
                    player.mage_skin_hit = shop_mage_skin_db.item_2_hit
                    
                if shop.item == 3:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_3
                    player.mage_skin_hit = shop_mage_skin_db.item_3_hit
                    
                if shop.item == 4:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_4
                    player.mage_skin_hit = shop_mage_skin_db.item_4_hit
                    
                if shop.item == 5:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_5
                    player.mage_skin_hit = shop_mage_skin_db.item_5_hit
                    
                if shop.item == 6:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_6
                    player.mage_skin_hit = shop_mage_skin_db.item_6_hit
                    
                if shop.item == 7:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_7
                    player.mage_skin_hit = shop_mage_skin_db.item_7_hit
                    
                if shop.item == 8:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_8
                    player.mage_skin_hit = shop_mage_skin_db.item_8_hit
                    
                if shop.item == 9:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_9
                    player.mage_skin_hit = shop_mage_skin_db.item_9_hit
                    
                if shop.item == 10:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_10
                    player.mage_skin_hit = shop_mage_skin_db.item_10_hit
                    
                if shop.item == 11:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_11
                    player.mage_skin_hit = shop_mage_skin_db.item_11_hit
                    
                if shop.item == 12:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_12
                    player.mage_skin_hit = shop_mage_skin_db.item_12_hit
                    
                if shop.item == 13:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_13
                    player.mage_skin_hit = shop_mage_skin_db.item_13_hit
                    
                if shop.item == 14:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_14
                    player.mage_skin_hit = shop_mage_skin_db.item_14_hit
                    
                if shop.item == 15:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_15
                    player.mage_skin_hit = shop_mage_skin_db.item_15_hit
                    
                if shop.item == 16:
                    player.current_mage_skin_name = shop.item_id
                    player.mage_skin = shop_mage_skin_db.item_16
                    player.mage_skin_hit = shop_mage_skin_db.item_16_hit

            if shop.page == "Knight":
                if shop.item == 1:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_1
                    player.knight_skin_hit = shop_knight_skin_db.item_1_hit
                    
                if shop.item == 2:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_2
                    player.knight_skin_hit = shop_knight_skin_db.item_2_hit
                    
                if shop.item == 3:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_3
                    player.knight_skin_hit = shop_knight_skin_db.item_3_hit
                    
                if shop.item == 4:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_4
                    player.knight_skin_hit = shop_knight_skin_db.item_4_hit
                    
                if shop.item == 5:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_5
                    player.knight_skin_hit = shop_knight_skin_db.item_5_hit
                    
                if shop.item == 6:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_6
                    player.knight_skin_hit = shop_knight_skin_db.item_6_hit
                    
                if shop.item == 7:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_7
                    player.knight_skin_hit = shop_knight_skin_db.item_7_hit
                    
                if shop.item == 8:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_8
                    player.knight_skin_hit = shop_knight_skin_db.item_8_hit
                    
                if shop.item == 9:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_9
                    player.knight_skin_hit = shop_knight_skin_db.item_9_hit
                    
                if shop.item == 10:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_10
                    player.knight_skin_hit = shop_knight_skin_db.item_10_hit
                    
                if shop.item == 11:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_11
                    player.knight_skin_hit = shop_knight_skin_db.item_11_hit
                    
                if shop.item == 12:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_12
                    player.knight_skin_hit = shop_knight_skin_db.item_12_hit
                    
                if shop.item == 13:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_13
                    player.knight_skin_hit = shop_knight_skin_db.item_13_hit
                    
                if shop.item == 14:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_14
                    player.knight_skin_hit = shop_knight_skin_db.item_14_hit
                    
                if shop.item == 15:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_15
                    player.knight_skin_hit = shop_knight_skin_db.item_15_hit
                    
                if shop.item == 16:
                    player.current_knight_skin_name = shop.item_id
                    player.knight_skin = shop_knight_skin_db.item_16
                    player.knight_skin_hit = shop_knight_skin_db.item_16_hit

def job_skin_shop_draw_window():
    update_bg()
    
    title_text = bigger_font.render("Skin", 1, WHITE)
    screen.blit(title_text, (TITLE_EMPLACEMENT.centerx - title_text.get_width()//2, TITLE_EMPLACEMENT.centery - title_text.get_height()//2))

    pygame.draw.rect(screen, DARK_GRAY, SHOP_GOLD_EMPLACEMENT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (SHOP_GOLD_EMPLACEMENT.width - 2, SHOP_GOLD_EMPLACEMENT.height - 2)), (SHOP_GOLD_EMPLACEMENT.x + 1, SHOP_GOLD_EMPLACEMENT.y + 1))
    screen.blit(COIN_IMG, (SHOP_GOLD_EMPLACEMENT.right - COIN_IMG.get_width() - 5, SHOP_GOLD_EMPLACEMENT.centery - COIN_IMG.get_height()//2))
    gold_text = font.render(f"{player.gold}", 1, WHITE)
    screen.blit(gold_text, (SHOP_GOLD_EMPLACEMENT.right - gold_text.get_width() - COIN_IMG.get_width() - 10, SHOP_GOLD_EMPLACEMENT.centery - gold_text.get_height()//2 + 2))

    # Category
    if shop.page == "Mage":
        pygame.draw.rect(screen, YELLOW, MAGE_SKIN_BUTTON)
    else:
        pygame.draw.rect(screen, RED, MAGE_SKIN_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (MAGE_SKIN_BUTTON.width - 2, MAGE_SKIN_BUTTON.height - 2)), (MAGE_SKIN_BUTTON.x + 1, MAGE_SKIN_BUTTON.y + 1))
    mage_skin_text = font.render("Mage", 1, WHITE)
    screen.blit(mage_skin_text, (MAGE_SKIN_BUTTON.centerx - mage_skin_text.get_width()//2, MAGE_SKIN_BUTTON.centery - mage_skin_text.get_height()//2))
    
    if shop.page == "Knight":
        pygame.draw.rect(screen, YELLOW, KNIGHT_SKIN_BUTTON)
    else:
        pygame.draw.rect(screen, RED, KNIGHT_SKIN_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (KNIGHT_SKIN_BUTTON.width - 2, KNIGHT_SKIN_BUTTON.height - 2)), (KNIGHT_SKIN_BUTTON.x + 1, KNIGHT_SKIN_BUTTON.y + 1))
    knight_skin_text = font.render("Knight", 1, WHITE)
    screen.blit(knight_skin_text, (KNIGHT_SKIN_BUTTON.centerx - knight_skin_text.get_width()//2, KNIGHT_SKIN_BUTTON.centery - knight_skin_text.get_height()//2))
    
    if shop.page == "Job3":
        pygame.draw.rect(screen, YELLOW, JOB3_SKIN_BUTTON)
    else:
        pygame.draw.rect(screen, RED, JOB3_SKIN_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (JOB3_SKIN_BUTTON.width - 2, JOB3_SKIN_BUTTON.height - 2)), (JOB3_SKIN_BUTTON.x + 1, JOB3_SKIN_BUTTON.y + 1))
    job3_skin_text = font.render("Job3", 1, WHITE)
    screen.blit(job3_skin_text, (JOB3_SKIN_BUTTON.centerx - job3_skin_text.get_width()//2, JOB3_SKIN_BUTTON.centery - job3_skin_text.get_height()//2))
    
    if shop.page == "Job4":
        pygame.draw.rect(screen, YELLOW, JOB4_SKIN_BUTTON)
    else:
        pygame.draw.rect(screen, RED, JOB4_SKIN_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (JOB4_SKIN_BUTTON.width - 2, JOB4_SKIN_BUTTON.height - 2)), (JOB4_SKIN_BUTTON.x + 1, JOB4_SKIN_BUTTON.y + 1))
    job4_skin_text = font.render("Job4", 1, WHITE)
    screen.blit(job4_skin_text, (JOB4_SKIN_BUTTON.centerx - job4_skin_text.get_width()//2, JOB4_SKIN_BUTTON.centery - job4_skin_text.get_height()//2))

    # Item slot
    if shop.item == 1:
        pygame.draw.rect(screen, YELLOW, ITEM_1_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_1_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_1_S.width - 2, ITEM_1_S.height - 2)), (ITEM_1_S.x + 1, ITEM_1_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_1, (ITEM_1_S.centerx - shop_mage_skin_db.item_1.get_width()//2, ITEM_1_S.centery - shop_mage_skin_db.item_1.get_height()//2))
        if shop_mage_skin_db.item_1_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_1_S.right - 8, ITEM_1_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_1_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_1_S.right - 8, ITEM_1_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_1, (ITEM_1_S.centerx - shop_knight_skin_db.item_1.get_width()//2, ITEM_1_S.centery - shop_knight_skin_db.item_1.get_height()//2))
        if shop_knight_skin_db.item_1_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_1_S.right - 8, ITEM_1_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_1_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_1_S.right - 8, ITEM_1_S.y + 3, 5, 5))
    
    if shop.item == 2:
        pygame.draw.rect(screen, YELLOW, ITEM_2_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_2_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_2_S.width - 2, ITEM_2_S.height - 2)), (ITEM_2_S.x + 1, ITEM_2_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_2, (ITEM_2_S.centerx - shop_mage_skin_db.item_2.get_width()//2, ITEM_2_S.centery - shop_mage_skin_db.item_2.get_height()//2))
        if shop_mage_skin_db.item_2_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_2_S.right - 8, ITEM_2_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_2_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_2_S.right - 8, ITEM_2_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_2, (ITEM_2_S.centerx - shop_knight_skin_db.item_2.get_width()//2, ITEM_2_S.centery - shop_knight_skin_db.item_2.get_height()//2))
        if shop_knight_skin_db.item_2_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_2_S.right - 8, ITEM_2_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_2_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_2_S.right - 8, ITEM_2_S.y + 3, 5, 5))
    
    if shop.item == 3:
        pygame.draw.rect(screen, YELLOW, ITEM_3_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_3_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_3_S.width - 2, ITEM_3_S.height - 2)), (ITEM_3_S.x + 1, ITEM_3_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_3, (ITEM_3_S.centerx - shop_mage_skin_db.item_3.get_width()//2, ITEM_3_S.centery - shop_mage_skin_db.item_3.get_height()//2))
        if shop_mage_skin_db.item_3_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_3_S.right - 8, ITEM_3_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_3_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_3_S.right - 8, ITEM_3_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_3, (ITEM_3_S.centerx - shop_knight_skin_db.item_3.get_width()//2, ITEM_3_S.centery - shop_knight_skin_db.item_3.get_height()//2))
        if shop_knight_skin_db.item_3_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_3_S.right - 8, ITEM_3_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_3_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_3_S.right - 8, ITEM_3_S.y + 3, 5, 5))
    
    if shop.item == 4:
        pygame.draw.rect(screen, YELLOW, ITEM_4_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_4_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_4_S.width - 2, ITEM_4_S.height - 2)), (ITEM_4_S.x + 1, ITEM_4_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_4, (ITEM_4_S.centerx - shop_mage_skin_db.item_4.get_width()//2, ITEM_4_S.centery - shop_mage_skin_db.item_4.get_height()//2))
        if shop_mage_skin_db.item_4_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_4_S.right - 8, ITEM_4_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_4_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_4_S.right - 8, ITEM_4_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_4, (ITEM_4_S.centerx - shop_knight_skin_db.item_4.get_width()//2, ITEM_4_S.centery - shop_knight_skin_db.item_4.get_height()//2))
        if shop_knight_skin_db.item_4_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_4_S.right - 8, ITEM_4_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_4_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_4_S.right - 8, ITEM_4_S.y + 3, 5, 5))
    
    if shop.item == 5:
        pygame.draw.rect(screen, YELLOW, ITEM_5_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_5_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_5_S.width - 2, ITEM_5_S.height - 2)), (ITEM_5_S.x + 1, ITEM_5_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_5, (ITEM_5_S.centerx - shop_mage_skin_db.item_5.get_width()//2, ITEM_5_S.centery - shop_mage_skin_db.item_5.get_height()//2))
        if shop_mage_skin_db.item_5_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_5_S.right - 8, ITEM_5_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_5_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_5_S.right - 8, ITEM_5_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_5, (ITEM_5_S.centerx - shop_knight_skin_db.item_5.get_width()//2, ITEM_5_S.centery - shop_knight_skin_db.item_5.get_height()//2))
        if shop_knight_skin_db.item_5_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_5_S.right - 8, ITEM_5_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_5_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_5_S.right - 8, ITEM_5_S.y + 3, 5, 5))
    
    if shop.item == 6:
        pygame.draw.rect(screen, YELLOW, ITEM_6_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_6_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_6_S.width - 2, ITEM_6_S.height - 2)), (ITEM_6_S.x + 1, ITEM_6_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_6, (ITEM_6_S.centerx - shop_mage_skin_db.item_6.get_width()//2, ITEM_6_S.centery - shop_mage_skin_db.item_6.get_height()//2))
        if shop_mage_skin_db.item_6_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_6_S.right - 8, ITEM_6_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_6_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_6_S.right - 8, ITEM_6_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_6, (ITEM_6_S.centerx - shop_knight_skin_db.item_6.get_width()//2, ITEM_6_S.centery - shop_knight_skin_db.item_6.get_height()//2))
        if shop_knight_skin_db.item_6_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_6_S.right - 8, ITEM_6_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_6_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_6_S.right - 8, ITEM_6_S.y + 3, 5, 5))
    
    if shop.item == 7:
        pygame.draw.rect(screen, YELLOW, ITEM_7_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_7_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_7_S.width - 2, ITEM_7_S.height - 2)), (ITEM_7_S.x + 1, ITEM_7_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_7, (ITEM_7_S.centerx - shop_mage_skin_db.item_7.get_width()//2, ITEM_7_S.centery - shop_mage_skin_db.item_7.get_height()//2))
        if shop_mage_skin_db.item_7_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_7_S.right - 8, ITEM_7_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_7_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_7_S.right - 8, ITEM_7_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_7, (ITEM_7_S.centerx - shop_knight_skin_db.item_7.get_width()//2, ITEM_7_S.centery - shop_knight_skin_db.item_7.get_height()//2))
        if shop_knight_skin_db.item_7_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_7_S.right - 8, ITEM_7_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_7_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_7_S.right - 8, ITEM_7_S.y + 3, 5, 5))
    
    if shop.item == 8:
        pygame.draw.rect(screen, YELLOW, ITEM_8_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_8_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_8_S.width - 2, ITEM_8_S.height - 2)), (ITEM_8_S.x + 1, ITEM_8_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_8, (ITEM_8_S.centerx - shop_mage_skin_db.item_8.get_width()//2, ITEM_8_S.centery - shop_mage_skin_db.item_8.get_height()//2))
        if shop_mage_skin_db.item_8_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_8_S.right - 8, ITEM_8_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_8_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_8_S.right - 8, ITEM_8_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_8, (ITEM_8_S.centerx - shop_knight_skin_db.item_8.get_width()//2, ITEM_8_S.centery - shop_knight_skin_db.item_8.get_height()//2))
        if shop_knight_skin_db.item_8_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_8_S.right - 8, ITEM_8_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_8_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_8_S.right - 8, ITEM_8_S.y + 3, 5, 5))
    
    if shop.item == 9:
        pygame.draw.rect(screen, YELLOW, ITEM_9_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_9_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_9_S.width - 2, ITEM_9_S.height - 2)), (ITEM_9_S.x + 1, ITEM_9_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_9, (ITEM_9_S.centerx - shop_mage_skin_db.item_9.get_width()//2, ITEM_9_S.centery - shop_mage_skin_db.item_9.get_height()//2))
        if shop_mage_skin_db.item_9_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_9_S.right - 8, ITEM_9_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_9_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_9_S.right - 8, ITEM_9_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_9, (ITEM_9_S.centerx - shop_knight_skin_db.item_9.get_width()//2, ITEM_9_S.centery - shop_knight_skin_db.item_9.get_height()//2))
        if shop_knight_skin_db.item_9_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_9_S.right - 8, ITEM_9_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_9_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_9_S.right - 8, ITEM_9_S.y + 3, 5, 5))
    
    if shop.item == 10:
        pygame.draw.rect(screen, YELLOW, ITEM_10_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_10_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_10_S.width - 2, ITEM_10_S.height - 2)), (ITEM_10_S.x + 1, ITEM_10_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_10, (ITEM_10_S.centerx - shop_mage_skin_db.item_10.get_width()//2, ITEM_10_S.centery - shop_mage_skin_db.item_10.get_height()//2))
        if shop_mage_skin_db.item_10_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_10_S.right - 8, ITEM_10_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_10_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_10_S.right - 8, ITEM_10_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_10, (ITEM_10_S.centerx - shop_knight_skin_db.item_10.get_width()//2, ITEM_10_S.centery - shop_knight_skin_db.item_10.get_height()//2))
        if shop_knight_skin_db.item_10_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_10_S.right - 8, ITEM_10_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_10_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_10_S.right - 8, ITEM_10_S.y + 3, 5, 5))
    
    if shop.item == 11:
        pygame.draw.rect(screen, YELLOW, ITEM_11_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_11_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_11_S.width - 2, ITEM_11_S.height - 2)), (ITEM_11_S.x + 1, ITEM_11_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_11, (ITEM_11_S.centerx - shop_mage_skin_db.item_11.get_width()//2, ITEM_11_S.centery - shop_mage_skin_db.item_11.get_height()//2))
        if shop_mage_skin_db.item_11_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_11_S.right - 8, ITEM_11_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_11_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_11_S.right - 8, ITEM_11_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_11, (ITEM_11_S.centerx - shop_knight_skin_db.item_11.get_width()//2, ITEM_11_S.centery - shop_knight_skin_db.item_11.get_height()//2))
        if shop_knight_skin_db.item_11_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_11_S.right - 8, ITEM_11_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_11_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_11_S.right - 8, ITEM_11_S.y + 3, 5, 5))
    
    if shop.item == 12:
        pygame.draw.rect(screen, YELLOW, ITEM_12_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_12_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_12_S.width - 2, ITEM_12_S.height - 2)), (ITEM_12_S.x + 1, ITEM_12_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_12, (ITEM_12_S.centerx - shop_mage_skin_db.item_12.get_width()//2, ITEM_12_S.centery - shop_mage_skin_db.item_12.get_height()//2))
        if shop_mage_skin_db.item_12_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_12_S.right - 8, ITEM_12_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_12_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_12_S.right - 8, ITEM_12_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_12, (ITEM_12_S.centerx - shop_knight_skin_db.item_12.get_width()//2, ITEM_12_S.centery - shop_knight_skin_db.item_12.get_height()//2))
        if shop_knight_skin_db.item_12_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_12_S.right - 8, ITEM_12_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_12_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_12_S.right - 8, ITEM_12_S.y + 3, 5, 5))
    
    if shop.item == 13:
        pygame.draw.rect(screen, YELLOW, ITEM_13_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_13_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_13_S.width - 2, ITEM_13_S.height - 2)), (ITEM_13_S.x + 1, ITEM_13_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_13, (ITEM_13_S.centerx - shop_mage_skin_db.item_13.get_width()//2, ITEM_13_S.centery - shop_mage_skin_db.item_13.get_height()//2))
        if shop_mage_skin_db.item_13_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_13_S.right - 8, ITEM_13_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_13_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_13_S.right - 8, ITEM_13_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_13, (ITEM_13_S.centerx - shop_knight_skin_db.item_13.get_width()//2, ITEM_13_S.centery - shop_knight_skin_db.item_13.get_height()//2))
        if shop_knight_skin_db.item_13_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_13_S.right - 8, ITEM_13_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_13_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_13_S.right - 8, ITEM_13_S.y + 3, 5, 5))
    
    if shop.item == 14:
        pygame.draw.rect(screen, YELLOW, ITEM_14_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_14_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_14_S.width - 2, ITEM_14_S.height - 2)), (ITEM_14_S.x + 1, ITEM_14_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_14, (ITEM_14_S.centerx - shop_mage_skin_db.item_14.get_width()//2, ITEM_14_S.centery - shop_mage_skin_db.item_14.get_height()//2))
        if shop_mage_skin_db.item_14_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_14_S.right - 8, ITEM_14_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_14_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_14_S.right - 8, ITEM_14_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_14, (ITEM_14_S.centerx - shop_knight_skin_db.item_14.get_width()//2, ITEM_14_S.centery - shop_knight_skin_db.item_14.get_height()//2))
        if shop_knight_skin_db.item_14_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_14_S.right - 8, ITEM_14_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_14_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_14_S.right - 8, ITEM_14_S.y + 3, 5, 5))
    
    if shop.item == 15:
        pygame.draw.rect(screen, YELLOW, ITEM_15_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_15_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_15_S.width - 2, ITEM_15_S.height - 2)), (ITEM_15_S.x + 1, ITEM_15_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_15, (ITEM_15_S.centerx - shop_mage_skin_db.item_15.get_width()//2, ITEM_15_S.centery - shop_mage_skin_db.item_15.get_height()//2))
        if shop_mage_skin_db.item_15_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_15_S.right - 8, ITEM_15_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_15_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_15_S.right - 8, ITEM_15_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_15, (ITEM_15_S.centerx - shop_knight_skin_db.item_15.get_width()//2, ITEM_15_S.centery - shop_knight_skin_db.item_15.get_height()//2))
        if shop_knight_skin_db.item_15_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_15_S.right - 8, ITEM_15_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_15_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_15_S.right - 8, ITEM_15_S.y + 3, 5, 5))
    
    if shop.item == 16:
        pygame.draw.rect(screen, YELLOW, ITEM_16_S)
    else:
        pygame.draw.rect(screen, RED, ITEM_16_S)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ITEM_16_S.width - 2, ITEM_16_S.height - 2)), (ITEM_16_S.x + 1, ITEM_16_S.y + 1))
    if shop.page == "Mage":
        screen.blit(shop_mage_skin_db.item_16, (ITEM_16_S.centerx - shop_mage_skin_db.item_16.get_width()//2, ITEM_16_S.centery - shop_mage_skin_db.item_16.get_height()//2))
        if shop_mage_skin_db.item_16_id == player.current_mage_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_16_S.right - 8, ITEM_16_S.y + 3, 5, 5))
        elif shop_mage_skin_db.item_16_id in player.skin_mage_list:
            pygame.draw.rect(screen, GREEN, (ITEM_16_S.right - 8, ITEM_16_S.y + 3, 5, 5))
    elif shop.page == "Knight":
        screen.blit(shop_knight_skin_db.item_16, (ITEM_16_S.centerx - shop_knight_skin_db.item_16.get_width()//2, ITEM_16_S.centery - shop_knight_skin_db.item_16.get_height()//2))
        if shop_knight_skin_db.item_16_id == player.current_knight_skin_name:
            pygame.draw.rect(screen, YELLOW, (ITEM_16_S.right - 8, ITEM_16_S.y + 3, 5, 5))
        elif shop_knight_skin_db.item_16_id in player.skin_knight_list:
            pygame.draw.rect(screen, GREEN, (ITEM_16_S.right - 8, ITEM_16_S.y + 3, 5, 5))


    pygame.draw.rect(screen, DARK_GRAY, STATS_RECT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (STATS_RECT.width - 2, STATS_RECT.height - 2)), (STATS_RECT.x + 1, STATS_RECT.y + 1))
    if shop.item_name != "":
        name_text = font.render(f"{shop.item_name}", 1, WHITE)
        screen.blit(name_text, (STATS_RECT.centerx - name_text.get_width()//2, STATS_RECT.y + 10))
        if shop.item_state == "Owned":
            if shop.item_id == player.current_mage_skin_name or shop.item_id == player.current_knight_skin_name:
                selected_text = font.render(f"Selected", 1, GREEN)
                screen.blit(selected_text, (STATS_RECT.centerx - selected_text.get_width()//2, STATS_RECT.y + 50))
            else:
                owned_text = font.render(f"Owned", 1, GREEN)
                screen.blit(owned_text, (STATS_RECT.centerx - owned_text.get_width()//2, STATS_RECT.y + 50))
        cost_text = font.render(f"Cost : {shop.item_cost}", 1, WHITE)
        screen.blit(cost_text, (STATS_RECT.x + 10, STATS_RECT.y + 80))
        if shop.description1 != "":
            description_text = font.render(f"Description :", 1, WHITE)
            screen.blit(description_text, (STATS_RECT.x + 10, STATS_RECT.y + 130))
            description1_text = font.render(f"{shop.description1}", 1, WHITE)
            screen.blit(description1_text, (STATS_RECT.x + 10, STATS_RECT.y + 160))
            description2_text = font.render(f"{shop.description2}", 1, WHITE)
            screen.blit(description2_text, (STATS_RECT.x + 10, STATS_RECT.y + 190))
            description3_text = font.render(f"{shop.description3}", 1, WHITE)
            screen.blit(description3_text, (STATS_RECT.x + 10, STATS_RECT.y + 220))
            description4_text = font.render(f"{shop.description4}", 1, WHITE)
            screen.blit(description4_text, (STATS_RECT.x + 10, STATS_RECT.y + 250))
            description5_text = font.render(f"{shop.description5}", 1, WHITE)
            screen.blit(description5_text, (STATS_RECT.x + 10, STATS_RECT.y + 280))

    if (shop.item_cost == 0 or shop.item_cost > player.gold) and shop.item_state != "Owned":
        pygame.draw.rect(screen, DARK_GRAY, BUY_BUTTON)
    else:
        pygame.draw.rect(screen, RED, BUY_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (BUY_BUTTON.width - 2, BUY_BUTTON.height - 2)), (BUY_BUTTON.x + 1, BACK_BUTTON_B_LEFT.y + 1))
    if shop.item_state == "Owned":
        buy_text = font.render("Select", 1, WHITE)
    else:
        buy_text = font.render("Buy", 1, WHITE)
    screen.blit(buy_text, (BUY_BUTTON.centerx - buy_text.get_width()//2, BUY_BUTTON.centery - buy_text.get_height()//2))

    pygame.draw.rect(screen, RED, BACK_BUTTON_B_LEFT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (BACK_BUTTON_B_LEFT.width - 2, BACK_BUTTON_B_LEFT.height - 2)), (BACK_BUTTON_B_LEFT.x + 1, BACK_BUTTON_B_LEFT.y + 1))
    back_text = font.render("Back", 1, WHITE)
    screen.blit(back_text, (BACK_BUTTON_B_LEFT.centerx - back_text.get_width()//2, BACK_BUTTON_B_LEFT.centery - back_text.get_height()//2))

    pygame.display.update()

def job_skin_shop():
    run = True
    reset_shopping_info()
    shop.page = "Mage"
    click = False
    while run:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        if MAGE_SKIN_BUTTON.collidepoint((mx,my)) and click:
            reset_shopping_info()
            shop.page = "Mage"
        if KNIGHT_SKIN_BUTTON.collidepoint((mx,my)) and click:
            reset_shopping_info()
            shop.page = "Knight"
        if JOB3_SKIN_BUTTON.collidepoint((mx,my)) and click:
            reset_shopping_info()
            shop.page = "Job3"
        if JOB4_SKIN_BUTTON.collidepoint((mx,my)) and click:
            reset_shopping_info()
            shop.page = "Job4"
        
        if ITEM_1_S.collidepoint((mx,my)) and click:
            shop.item = 1
            retrieve_shopping_info()
        if ITEM_2_S.collidepoint((mx,my)) and click:
            shop.item = 2
            retrieve_shopping_info()
        if ITEM_3_S.collidepoint((mx,my)) and click:
            shop.item = 3
            retrieve_shopping_info()
        if ITEM_4_S.collidepoint((mx,my)) and click:
            shop.item = 4
            retrieve_shopping_info()
        if ITEM_5_S.collidepoint((mx,my)) and click:
            shop.item = 5
            retrieve_shopping_info()
        if ITEM_6_S.collidepoint((mx,my)) and click:
            shop.item = 6
            retrieve_shopping_info()
        if ITEM_7_S.collidepoint((mx,my)) and click:
            shop.item = 7
            retrieve_shopping_info()
        if ITEM_8_S.collidepoint((mx,my)) and click:
            shop.item = 8
            retrieve_shopping_info()
        if ITEM_9_S.collidepoint((mx,my)) and click:
            shop.item = 9
            retrieve_shopping_info()
        if ITEM_10_S.collidepoint((mx,my)) and click:
            shop.item = 10
            retrieve_shopping_info()
        if ITEM_11_S.collidepoint((mx,my)) and click:
            shop.item = 11
            retrieve_shopping_info()
        if ITEM_12_S.collidepoint((mx,my)) and click:
            shop.item = 12
            retrieve_shopping_info()
        if ITEM_13_S.collidepoint((mx,my)) and click:
            shop.item = 13
            retrieve_shopping_info()
        if ITEM_14_S.collidepoint((mx,my)) and click:
            shop.item = 14
            retrieve_shopping_info()
        if ITEM_15_S.collidepoint((mx,my)) and click:
            shop.item = 15
            retrieve_shopping_info()
        if ITEM_16_S.collidepoint((mx,my)) and click:
            shop.item = 16
            retrieve_shopping_info()
            

        if BUY_BUTTON.collidepoint((mx,my)) and click:
            if shop.item_cost != 0 and shop.item_state != "Owned" and shop.item_cost <= player.gold:
                player.gold -= shop.item_cost
                shop.item_state = "Owned"
                if shop.page == "Mage":
                    player.skin_mage_list.append(shop.item_id)
                if shop.page == "Knight":
                    player.skin_knight_list.append(shop.item_id)
                for entry in game.ranking_list:
                    if entry["name"] == game.player_name:
                        entry["mage_skin"] = player.skin_mage_list
                        entry["knight_skin"] = player.skin_knight_list
                        entry["gold"] = player.gold
                select_skin()
                for entry in game.ranking_list:
                    if entry["name"] == game.player_name:
                        entry["current_mage_skin"] = player.current_mage_skin_name
                        entry["current_knight_skin"] = player.current_knight_skin_name
                with open("dodge_save.txt", "wb") as f:
                    pickle.dump(game.ranking_list, f)
            elif shop.item_state == "Owned":
                select_skin()
                for entry in game.ranking_list:
                    if entry["name"] == game.player_name:
                        entry["current_mage_skin"] = player.current_mage_skin_name
                        entry["current_knight_skin"] = player.current_knight_skin_name
                with open("dodge_save.txt", "wb") as f:
                    pickle.dump(game.ranking_list, f)


        if BACK_BUTTON_B_LEFT.collidepoint((mx,my)) and click:
            run = False

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                if event.key == K_a:
                    player.gold += 100

        job_skin_shop_draw_window()

def shopping_draw_window():
    update_bg()
    
    title_text = bigger_font.render("Shop", 1, WHITE)
    screen.blit(title_text, (TITLE_EMPLACEMENT.centerx - title_text.get_width()//2, TITLE_EMPLACEMENT.centery - title_text.get_height()//2))

    pygame.draw.rect(screen, RED, JOB_SKIN_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (JOB_SKIN_BUTTON.width - 2, JOB_SKIN_BUTTON.height - 2)), (JOB_SKIN_BUTTON.x + 1, JOB_SKIN_BUTTON.y + 1))
    skin_text = font.render("Skin", 1, WHITE)
    screen.blit(skin_text, (JOB_SKIN_BUTTON.centerx - skin_text.get_width()//2, JOB_SKIN_BUTTON.centery - skin_text.get_height()//2))
    
    pygame.draw.rect(screen, RED, BACKGROUND_SHOP_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (BACKGROUND_SHOP_BUTTON.width - 2, BACKGROUND_SHOP_BUTTON.height - 2)), (BACKGROUND_SHOP_BUTTON.x + 1, BACKGROUND_SHOP_BUTTON.y + 1))
    background_text = font.render("Background", 1, WHITE)
    screen.blit(background_text, (BACKGROUND_SHOP_BUTTON.centerx - background_text.get_width()//2, BACKGROUND_SHOP_BUTTON.centery - background_text.get_height()//2))
    
    pygame.draw.rect(screen, RED, DUNGEON_BACKGROUND_SHOP_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (DUNGEON_BACKGROUND_SHOP_BUTTON.width - 2, DUNGEON_BACKGROUND_SHOP_BUTTON.height - 2)), (DUNGEON_BACKGROUND_SHOP_BUTTON.x + 1, DUNGEON_BACKGROUND_SHOP_BUTTON.y + 1))
    dungeon_bg_text = font.render("Dungeon", 1, WHITE)
    screen.blit(dungeon_bg_text, (DUNGEON_BACKGROUND_SHOP_BUTTON.centerx - dungeon_bg_text.get_width()//2, DUNGEON_BACKGROUND_SHOP_BUTTON.centery - dungeon_bg_text.get_height()//2))

    pygame.draw.rect(screen, RED, BACK_BUTTON_B_LEFT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (BACK_BUTTON_B_LEFT.width - 2, BACK_BUTTON_B_LEFT.height - 2)), (BACK_BUTTON_B_LEFT.x + 1, BACK_BUTTON_B_LEFT.y + 1))
    back_text = font.render("Back", 1, WHITE)
    screen.blit(back_text, (BACK_BUTTON_B_LEFT.centerx - back_text.get_width()//2, BACK_BUTTON_B_LEFT.centery - back_text.get_height()//2))

    pygame.display.update()

def shopping():
    run = True
    click = False
    while run:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        if JOB_SKIN_BUTTON.collidepoint((mx,my)) and click:
            job_skin_shop()

        if BACKGROUND_SHOP_BUTTON.collidepoint((mx,my)) and click:
            pass

        if DUNGEON_BACKGROUND_SHOP_BUTTON.collidepoint((mx,my)) and click:
            pass

        if BACK_BUTTON_B_LEFT.collidepoint((mx,my)) and click:
            run = False

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

        shopping_draw_window()


#############
## Ranking ##

class ranking:
    all = []
    all_max_page = 1
    #
    mage = []
    mage_max_page = 1
    #
    knight = []
    knight_max_page = 1

    def update(self):
        self.update_all()
        self.update_mage()
        self.update_knight()
        

    def update_all(self):
        self.all = game.ranking_list
        self.all_max_page = len(self.all)//10 + 1

    def update_mage(self):
        temp_mage = []
        for each in self.all:
            if each["best_time_mage"] > 0:
                temp_mage.append(each)
        self.mage = []
        number_of_ranked = len(temp_mage)
        currently_selected = temp_mage[0]
        while number_of_ranked > 0:
            currently_selected = temp_mage[0]
            for entry in temp_mage:
                if entry["best_time_mage"] > currently_selected["best_time_mage"]:
                    currently_selected = entry
            self.mage.append(currently_selected)
            temp_mage.remove(currently_selected)
            number_of_ranked = len(temp_mage)
        self.mage_max_page = len(self.mage)//10 + 1

    def update_knight(self):
        temp_knight = []
        for each in self.all:
            if each["best_time_knight"] > 0:
                temp_knight.append(each)
        self.knight = []
        number_of_ranked = len(temp_knight)
        currently_selected = temp_knight[0]
        while number_of_ranked > 0:
            currently_selected = temp_knight[0]
            for entry in temp_knight:
                if entry["best_time_knight"] > currently_selected["best_time_knight"]:
                    currently_selected = entry
            self.knight.append(currently_selected)
            temp_knight.remove(currently_selected)
            number_of_ranked = len(temp_knight)
        self.knight_max_page = len(self.knight)//10 + 1

ranking = ranking()


def ranking_draw_window(job,page):
    update_bg()

    title_text = title_font.render("Ranking", 1, DARK_RED)
    screen.blit(title_text, (101, 22))
    title_text = title_font.render("Ranking", 1, WHITE)
    screen.blit(title_text, (100, 20))

    if job == "Mage":
        pygame.draw.rect(screen, YELLOW, RK_JOB1_BUTTON)
    else:
        pygame.draw.rect(screen, RED, RK_JOB1_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_JOB1_BUTTON.width - 2, RK_JOB1_BUTTON.height - 2)), (RK_JOB1_BUTTON.x + 1, RK_JOB1_BUTTON.y + 1))
    keybind_text = font.render("Mage", 1, WHITE)
    screen.blit(keybind_text, (RK_JOB1_BUTTON.centerx - keybind_text.get_width()//2, RK_JOB1_BUTTON.centery - keybind_text.get_height()//2))
    
    if job == "Knight":
        pygame.draw.rect(screen, YELLOW, RK_JOB2_BUTTON)
    else:
        pygame.draw.rect(screen, RED, RK_JOB2_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_JOB2_BUTTON.width - 2, RK_JOB2_BUTTON.height - 2)), (RK_JOB2_BUTTON.x + 1, RK_JOB2_BUTTON.y + 1))
    keybind_text = font.render("Knight", 1, WHITE)
    screen.blit(keybind_text, (RK_JOB2_BUTTON.centerx - keybind_text.get_width()//2, RK_JOB2_BUTTON.centery - keybind_text.get_height()//2))
    
    if job == "Job3":
        pygame.draw.rect(screen, YELLOW, RK_JOB3_BUTTON)
    else:
        pygame.draw.rect(screen, RED, RK_JOB3_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_JOB3_BUTTON.width - 2, RK_JOB3_BUTTON.height - 2)), (RK_JOB3_BUTTON.x + 1, RK_JOB3_BUTTON.y + 1))
    keybind_text = font.render("Job3", 1, WHITE)
    screen.blit(keybind_text, (RK_JOB3_BUTTON.centerx - keybind_text.get_width()//2, RK_JOB3_BUTTON.centery - keybind_text.get_height()//2))
    
    if job == "Job4":
        pygame.draw.rect(screen, YELLOW, RK_JOB4_BUTTON)
    else:
        pygame.draw.rect(screen, RED, RK_JOB4_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_JOB4_BUTTON.width - 2, RK_JOB4_BUTTON.height - 2)), (RK_JOB4_BUTTON.x + 1, RK_JOB4_BUTTON.y + 1))
    keybind_text = font.render("Job4", 1, WHITE)
    screen.blit(keybind_text, (RK_JOB4_BUTTON.centerx - keybind_text.get_width()//2, RK_JOB4_BUTTON.centery - keybind_text.get_height()//2))
    
    
    pygame.draw.rect(screen, RED, RK_ARROW_UP_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_ARROW_UP_BUTTON.width - 2, RK_ARROW_UP_BUTTON.height - 2)), (RK_ARROW_UP_BUTTON.x + 1, RK_ARROW_UP_BUTTON.y + 1))
    screen.blit(pygame.transform.scale(ARROW_IMG, (RK_ARROW_UP_BUTTON.width - 2, RK_ARROW_UP_BUTTON.height - 2)), (RK_ARROW_UP_BUTTON.x + 1, RK_ARROW_UP_BUTTON.y + 1))
    
    pygame.draw.rect(screen, RED, RK_ARROW_DOWN_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_ARROW_DOWN_BUTTON.width - 2, RK_ARROW_DOWN_BUTTON.height - 2)), (RK_ARROW_DOWN_BUTTON.x + 1, RK_ARROW_DOWN_BUTTON.y + 1))
    screen.blit(pygame.transform.scale(pygame.transform.rotate(ARROW_IMG, 180), (RK_ARROW_DOWN_BUTTON.width - 2, RK_ARROW_DOWN_BUTTON.height - 2)), (RK_ARROW_DOWN_BUTTON.x + 1, RK_ARROW_DOWN_BUTTON.y + 1))
    
    
    current_job_text = big_font.render(f"{job}", 1, DARK_RED)
    screen.blit(current_job_text, (WIDTH//2 - current_job_text.get_width()//2 + 1, RK_HEAD_NAME.y - current_job_text.get_height() - 20))
    current_job_text = big_font.render(f"{job}", 1, WHITE)
    screen.blit(current_job_text, (WIDTH//2 - current_job_text.get_width()//2, RK_HEAD_NAME.y - current_job_text.get_height() - 20))

    pygame.draw.rect(screen, RED, RK_HEAD_NUMBER)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_HEAD_NUMBER.width - 2, RK_HEAD_NUMBER.height - 2)), (RK_HEAD_NUMBER.x + 1, RK_HEAD_NUMBER.y + 1))
    keybind_text = font.render("N°", 1, WHITE)
    screen.blit(keybind_text, (RK_HEAD_NUMBER.centerx - keybind_text.get_width()//2, RK_HEAD_NUMBER.centery - keybind_text.get_height()//2))
    pygame.draw.rect(screen, RED, RK_COLUMN_NUMBER)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_COLUMN_NUMBER.width - 2, RK_COLUMN_NUMBER.height - 2)), (RK_COLUMN_NUMBER.x + 1, RK_COLUMN_NUMBER.y + 1))
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NUMBER_1)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NUMBER_2)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NUMBER_3)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NUMBER_4)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NUMBER_5)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NUMBER_6)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NUMBER_7)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NUMBER_8)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NUMBER_9)
    
    pygame.draw.rect(screen, RED, RK_HEAD_NAME)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_HEAD_NAME.width - 2, RK_HEAD_NAME.height - 2)), (RK_HEAD_NAME.x + 1, RK_HEAD_NAME.y + 1))
    keybind_text = font.render("Name", 1, WHITE)
    screen.blit(keybind_text, (RK_HEAD_NAME.centerx - keybind_text.get_width()//2, RK_HEAD_NAME.centery - keybind_text.get_height()//2))
    pygame.draw.rect(screen, RED, RK_COLUMN_NAME)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_COLUMN_NAME.width - 2, RK_COLUMN_NAME.height - 2)), (RK_COLUMN_NAME.x + 1, RK_COLUMN_NAME.y + 1))
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NAME_1)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NAME_2)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NAME_3)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NAME_4)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NAME_5)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NAME_6)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NAME_7)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NAME_8)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_NAME_9)
    
    pygame.draw.rect(screen, RED, RK_HEAD_TIME)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_HEAD_TIME.width - 2, RK_HEAD_TIME.height - 2)), (RK_HEAD_TIME.x + 1, RK_HEAD_TIME.y + 1))
    keybind_text = font.render("Time", 1, WHITE)
    screen.blit(keybind_text, (RK_HEAD_TIME.centerx - keybind_text.get_width()//2, RK_HEAD_TIME.centery - keybind_text.get_height()//2))
    pygame.draw.rect(screen, RED, RK_COLUMN_TIME)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_COLUMN_TIME.width - 2, RK_COLUMN_TIME.height - 2)), (RK_COLUMN_TIME.x + 1, RK_COLUMN_TIME.y + 1))
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_TIME_1)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_TIME_2)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_TIME_3)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_TIME_4)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_TIME_5)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_TIME_6)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_TIME_7)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_TIME_8)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_TIME_9)
    
    pygame.draw.rect(screen, RED, RK_HEAD_SKIN)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_HEAD_SKIN.width - 2, RK_HEAD_SKIN.height - 2)), (RK_HEAD_SKIN.x + 1, RK_HEAD_SKIN.y + 1))
    keybind_text = font.render("Skin", 1, WHITE)
    screen.blit(keybind_text, (RK_HEAD_SKIN.centerx - keybind_text.get_width()//2, RK_HEAD_SKIN.centery - keybind_text.get_height()//2))
    pygame.draw.rect(screen, RED, RK_COLUMN_SKIN)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_COLUMN_SKIN.width - 2, RK_COLUMN_SKIN.height - 2)), (RK_COLUMN_SKIN.x + 1, RK_COLUMN_SKIN.y + 1))
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_SKIN_1)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_SKIN_2)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_SKIN_3)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_SKIN_4)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_SKIN_5)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_SKIN_6)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_SKIN_7)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_SKIN_8)
    pygame.draw.rect(screen, GRAY, RK_DIVIDER_SKIN_9)
    
    for i in range(10):
        number_text = font.render(f"{i + 1 + (page - 1) * 10}", 1, WHITE)
        screen.blit(number_text, (RK_COLUMN_NUMBER.centerx - number_text.get_width()//2, RK_COLUMN_NUMBER.y + 10 + i * 40))
    if job == "All":
        offset = 0
        for entry in ranking.all:
            name_text = font.render(f"{entry['name']}", 1, WHITE)
            screen.blit(name_text, (RK_COLUMN_NAME.centerx - name_text.get_width()//2, RK_COLUMN_NAME.y + 10 + offset * 40))
            time_text = font.render(f"{entry['time']:.2f}", 1, WHITE)
            screen.blit(time_text, (RK_COLUMN_TIME.centerx - time_text.get_width()//2, RK_COLUMN_TIME.y + 10 + offset * 40))
            if f"{entry['job']}" == "Mage":
                screen.blit(pygame.transform.scale(get_skin_img(f"{entry['current_mage_skin']}"),(30,30)), (RK_COLUMN_SKIN.x + 10, RK_COLUMN_SKIN.y + 5 + offset * 40))
            elif f"{entry['job']}" == "Knight":
                screen.blit(pygame.transform.scale(get_skin_img(f"{entry['current_knight_skin']}"),(30,30)), (RK_COLUMN_SKIN.x + 10, RK_COLUMN_SKIN.y + 5 + offset * 40))
            else:
                screen.blit(pygame.transform.scale(get_skin_img(f"{entry['current_mage_skin']}"),(30,30)), (RK_COLUMN_SKIN.x + 10, RK_COLUMN_SKIN.y + 5 + offset * 40))
            offset += 1
    if job == "Mage":
        offset = 0
        for entry in ranking.mage:
            name_text = font.render(f"{entry['name']}", 1, WHITE)
            screen.blit(name_text, (RK_COLUMN_NAME.centerx - name_text.get_width()//2, RK_COLUMN_NAME.y + 10 + offset * 40))
            time_text = font.render(f"{entry['best_time_mage']:.2f}", 1, WHITE)
            screen.blit(time_text, (RK_COLUMN_TIME.centerx - time_text.get_width()//2, RK_COLUMN_TIME.y + 10 + offset * 40))
            screen.blit(pygame.transform.scale(get_skin_img(f"{entry['current_mage_skin']}"),(30,30)), (RK_COLUMN_SKIN.x + 10, RK_COLUMN_SKIN.y + 5 + offset * 40))
            offset += 1
    if job == "Knight":
        offset = 0
        for entry in ranking.knight:
            name_text = font.render(f"{entry['name']}", 1, WHITE)
            screen.blit(name_text, (RK_COLUMN_NAME.centerx - name_text.get_width()//2, RK_COLUMN_NAME.y + 10 + offset * 40))
            time_text = font.render(f"{entry['best_time_knight']:.2f}", 1, WHITE)
            screen.blit(time_text, (RK_COLUMN_TIME.centerx - time_text.get_width()//2, RK_COLUMN_TIME.y + 10 + offset * 40))
            screen.blit(pygame.transform.scale(get_skin_img(f"{entry['current_knight_skin']}"),(30,30)), (RK_COLUMN_SKIN.x + 10, RK_COLUMN_SKIN.y + 5 + offset * 40))
            offset += 1


    pygame.draw.rect(screen, RED, RK_STATS_RECT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_STATS_RECT.width - 2, RK_STATS_RECT.height - 2)), (RK_STATS_RECT.x + 1, RK_STATS_RECT.y + 1))
    stats_text = big_font.render("Stats", 1, WHITE)
    screen.blit(stats_text, (RK_STATS_RECT.centerx - stats_text.get_width()//2, RK_STATS_RECT.y + 10))

    job_text = font.render(f"Job : {job}", 1, WHITE)
    screen.blit(job_text, (RK_STATS_RECT.x + 10, RK_STATS_RECT.y + 60))

    if job == "Mage":
        best_time = font.render(f"Best time : {player.best_time_mage:.2f}s", 1, WHITE)
    elif job == "Knight":
        best_time = font.render(f"Best time : {player.best_time_knight:.2f}s", 1, WHITE)
    elif job == "All":
        best_time = font.render(f"Best time : {game.best_time_ever:.2f}s", 1, WHITE)
    else:
        best_time = font.render(f"Best time : None", 1, WHITE)
    screen.blit(best_time, (RK_STATS_RECT.x + 10, RK_STATS_RECT.y + 100))

    # Number of Run/ Gold coins collected (To be changed)
    active_text = font.render(f"Active : {player.special_type}", 1, WHITE)
    screen.blit(active_text, (RK_STATS_RECT.x + 10, RK_STATS_RECT.y + 140))
    active_desc = small_font.render(f"{player.special_desc_1}", 1, WHITE)
    screen.blit(active_desc, (RK_STATS_RECT.x + 10, RK_STATS_RECT.y + 170))
    active_desc = small_font.render(f"{player.special_desc_2}", 1, WHITE)
    screen.blit(active_desc, (RK_STATS_RECT.x + 10, RK_STATS_RECT.y + 190))

    dash_text = font.render(f"Dash : {player.dash_type}", 1, WHITE)
    screen.blit(dash_text, (RK_STATS_RECT.x + 10, RK_STATS_RECT.y + 230))
    active_desc = small_font.render(f"{player.dash_desc_1}", 1, WHITE)
    screen.blit(active_desc, (RK_STATS_RECT.x + 10, RK_STATS_RECT.y + 260))
    active_desc = small_font.render(f"{player.dash_desc_2}", 1, WHITE)
    screen.blit(active_desc, (RK_STATS_RECT.x + 10, RK_STATS_RECT.y + 280))


    page_text = font.render(f"{page}", 1, WHITE)
    screen.blit(page_text, (WIDTH//2 - page_text.get_width()//2, RK_ARROW_LEFT_BUTTON.centery - page_text.get_height()//2))

    pygame.draw.rect(screen, RED, RK_ARROW_LEFT_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_ARROW_LEFT_BUTTON.width - 2, RK_ARROW_LEFT_BUTTON.height - 2)), (RK_ARROW_LEFT_BUTTON.x + 1, RK_ARROW_LEFT_BUTTON.y + 1))
    screen.blit(pygame.transform.scale(pygame.transform.rotate(ARROW_IMG, 90), (RK_ARROW_LEFT_BUTTON.width - 2, RK_ARROW_LEFT_BUTTON.height - 2)), (RK_ARROW_LEFT_BUTTON.x + 1, RK_ARROW_LEFT_BUTTON.y + 1))

    pygame.draw.rect(screen, RED, RK_ARROW_RIGHT_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RK_ARROW_RIGHT_BUTTON.width - 2, RK_ARROW_RIGHT_BUTTON.height - 2)), (RK_ARROW_RIGHT_BUTTON.x + 1, RK_ARROW_RIGHT_BUTTON.y + 1))
    screen.blit(pygame.transform.scale(pygame.transform.rotate(ARROW_IMG, -90), (RK_ARROW_RIGHT_BUTTON.width - 2, RK_ARROW_RIGHT_BUTTON.height - 2)), (RK_ARROW_RIGHT_BUTTON.x + 1, RK_ARROW_RIGHT_BUTTON.y + 1))


    pygame.draw.rect(screen, RED, BACK_BUTTON_B_LEFT)
    screen.blit(pygame.transform.scale(PANEL_IMG, (BACK_BUTTON_B_LEFT.width - 2, BACK_BUTTON_B_LEFT.height - 2)), (BACK_BUTTON_B_LEFT.x + 1, BACK_BUTTON_B_LEFT.y + 1))
    keybind_text = font.render("Back", 1, WHITE)
    screen.blit(keybind_text, (BACK_BUTTON_B_LEFT.centerx - keybind_text.get_width()//2, BACK_BUTTON_B_LEFT.centery - keybind_text.get_height()//2))

    pygame.display.update()

def ranking_screen():
    run = True
    click = False
    job = "All"
    page = 1
    ranking.update()
    max_page = ranking.all_max_page
    while run:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()
        
        if RK_JOB1_BUTTON.collidepoint((mx,my)) and click:
            page = 1
            job = "Mage"
            max_page = ranking.mage_max_page
            
        if RK_JOB2_BUTTON.collidepoint((mx,my)) and click:
            page = 1
            job = "Knight"
            max_page = ranking.knight_max_page
            
        if RK_JOB3_BUTTON.collidepoint((mx,my)) and click:
            page = 1
            job = "Dragon"
            max_page = 1
            
        if RK_JOB4_BUTTON.collidepoint((mx,my)) and click:
            page = 1
            job = "Job4"
            max_page = 1

        if RK_ARROW_UP_BUTTON.collidepoint((mx,my)) and click:
            pass

        if RK_ARROW_DOWN_BUTTON.collidepoint((mx,my)) and click:
            pass
            
        if RK_ARROW_LEFT_BUTTON.collidepoint((mx,my)) and click:
            if page > 1:
                page -= 1
            
        if RK_ARROW_RIGHT_BUTTON.collidepoint((mx,my)) and click:
            if page < max_page:
                page += 1

            
        if BACK_BUTTON_B_LEFT.collidepoint((mx,my)) and click:
            run = False

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                if event.button == 3:
                    job = "All"
                    page = 1
                    max_page = ranking.all_max_page
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

        ranking_draw_window(job, page)


##############
## Settings ##

class settings:
    azerty = True
    go_left_key = K_q
    go_right_key = K_d
    jump_key = K_z
    stomp_key = K_s
    dash_key = K_LSHIFT
    special_key = K_SPACE
    restart_key = K_r

    def azerty_mapping(self):
        self.azerty = True
        self.go_left_key = K_q
        self.go_right_key = K_d
        self.jump_key = K_z
        self.stomp_key = K_s
        self.dash_key = K_LSHIFT
        self.special_key = K_SPACE
        self.restart_key = K_r

    def qwerty_mapping(self):
        self.azerty = False
        self.go_left_key = K_a
        self.go_right_key = K_d
        self.jump_key = K_w
        self.stomp_key = K_s
        self.dash_key = K_LSHIFT
        self.special_key = K_SPACE
        self.restart_key = K_r

    def change_keybind(self,key_type,new_key):
        if key_type == "left":
            self.go_left_key = new_key
        elif key_type == "right":
            self.go_right_key = new_key
        elif key_type == "jump":
            self.jump_key = new_key
        elif key_type == "stomp":
            self.stomp_key = new_key
        elif key_type == "dash":
            self.dash_key = new_key
        elif key_type == "special":
            self.special_key = new_key
        elif key_type == "restart":
            self.restart_key = new_key


settings = settings()

def settings_draw_window(input):
    update_bg()

    title_text = title_font.render("Settings", 1, DARK_RED)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2 + 1, title_text.get_height() + 2))
    title_text = title_font.render("Settings", 1, WHITE)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, title_text.get_height()))

    if bool(input):
        press_key_text = font.render("Press new key", 1, RED)
        screen.blit(press_key_text, (WIDTH//2 - press_key_text.get_width()//2 + 1, ST_LEFT_BUTTON.y - press_key_text.get_height() - 15))
    
    pygame.draw.rect(screen, RED, ST_LEFT_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_LEFT_BUTTON.width - 2, ST_LEFT_BUTTON.height - 2)), (ST_LEFT_BUTTON.x + 1, ST_LEFT_BUTTON.y + 1))
    keybind_text = font.render("Left", 1, WHITE)
    screen.blit(keybind_text, (ST_LEFT_BUTTON.centerx - keybind_text.get_width()//2, ST_LEFT_BUTTON.centery - keybind_text.get_height()//2))

    if input == "left":
        pygame.draw.rect(screen, YELLOW, ST_LEFT_INPUT_ZONE)
    else:
        pygame.draw.rect(screen, RED, ST_LEFT_INPUT_ZONE)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_LEFT_INPUT_ZONE.width - 2, ST_LEFT_INPUT_ZONE.height - 2)), (ST_LEFT_INPUT_ZONE.x + 1, ST_LEFT_INPUT_ZONE.y + 1))
    keybind_text = normal_font.render((f"{pygame.key.name(settings.go_left_key)}".upper()), 1, WHITE)
    screen.blit(keybind_text, (ST_LEFT_INPUT_ZONE.centerx - keybind_text.get_width()//2, ST_LEFT_INPUT_ZONE.centery - keybind_text.get_height()//2))
    
    pygame.draw.rect(screen, RED, ST_RIGHT_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_RIGHT_BUTTON.width - 2, ST_RIGHT_BUTTON.height - 2)), (ST_RIGHT_BUTTON.x + 1, ST_RIGHT_BUTTON.y + 1))
    keybind_text = font.render("Right", 1, WHITE)
    screen.blit(keybind_text, (ST_RIGHT_BUTTON.centerx - keybind_text.get_width()//2, ST_RIGHT_BUTTON.centery - keybind_text.get_height()//2))

    if input == "right":
        pygame.draw.rect(screen, YELLOW, ST_RIGHT_INPUT_ZONE)
    else:
        pygame.draw.rect(screen, RED, ST_RIGHT_INPUT_ZONE)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_RIGHT_INPUT_ZONE.width - 2, ST_RIGHT_INPUT_ZONE.height - 2)), (ST_RIGHT_INPUT_ZONE.x + 1, ST_RIGHT_INPUT_ZONE.y + 1))
    keybind_text = normal_font.render((f"{pygame.key.name(settings.go_right_key)}".upper()), 1, WHITE)
    screen.blit(keybind_text, (ST_RIGHT_INPUT_ZONE.centerx - keybind_text.get_width()//2, ST_RIGHT_INPUT_ZONE.centery - keybind_text.get_height()//2))
    
    pygame.draw.rect(screen, RED, ST_JUMP_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_JUMP_BUTTON.width - 2, ST_JUMP_BUTTON.height - 2)), (ST_JUMP_BUTTON.x + 1, ST_JUMP_BUTTON.y + 1))
    keybind_text = font.render("Jump", 1, WHITE)
    screen.blit(keybind_text, (ST_JUMP_BUTTON.centerx - keybind_text.get_width()//2, ST_JUMP_BUTTON.centery - keybind_text.get_height()//2))

    if input == "jump":
        pygame.draw.rect(screen, YELLOW, ST_JUMP_INPUT_ZONE)
    else:
        pygame.draw.rect(screen, RED, ST_JUMP_INPUT_ZONE)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_JUMP_INPUT_ZONE.width - 2, ST_JUMP_INPUT_ZONE.height - 2)), (ST_JUMP_INPUT_ZONE.x + 1, ST_JUMP_INPUT_ZONE.y + 1))
    keybind_text = normal_font.render((f"{pygame.key.name(settings.jump_key)}".upper()), 1, WHITE)
    screen.blit(keybind_text, (ST_JUMP_INPUT_ZONE.centerx - keybind_text.get_width()//2, ST_JUMP_INPUT_ZONE.centery - keybind_text.get_height()//2))
    
    pygame.draw.rect(screen, RED, ST_STOMP_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_STOMP_BUTTON.width - 2, ST_STOMP_BUTTON.height - 2)), (ST_STOMP_BUTTON.x + 1, ST_STOMP_BUTTON.y + 1))
    keybind_text = font.render("Stomp", 1, WHITE)
    screen.blit(keybind_text, (ST_STOMP_BUTTON.centerx - keybind_text.get_width()//2, ST_STOMP_BUTTON.centery - keybind_text.get_height()//2))

    if input == "stomp":
        pygame.draw.rect(screen, YELLOW, ST_STOMP_INPUT_ZONE)
    else:
        pygame.draw.rect(screen, RED, ST_STOMP_INPUT_ZONE)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_STOMP_INPUT_ZONE.width - 2, ST_STOMP_INPUT_ZONE.height - 2)), (ST_STOMP_INPUT_ZONE.x + 1, ST_STOMP_INPUT_ZONE.y + 1))
    keybind_text = normal_font.render((f"{pygame.key.name(settings.stomp_key)}".upper()), 1, WHITE)
    screen.blit(keybind_text, (ST_STOMP_INPUT_ZONE.centerx - keybind_text.get_width()//2, ST_STOMP_INPUT_ZONE.centery - keybind_text.get_height()//2))
    
    pygame.draw.rect(screen, RED, ST_DASH_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_DASH_BUTTON.width - 2, ST_DASH_BUTTON.height - 2)), (ST_DASH_BUTTON.x + 1, ST_DASH_BUTTON.y + 1))
    keybind_text = font.render("Dash", 1, WHITE)
    screen.blit(keybind_text, (ST_DASH_BUTTON.centerx - keybind_text.get_width()//2, ST_DASH_BUTTON.centery - keybind_text.get_height()//2))

    if input == "dash":
        pygame.draw.rect(screen, YELLOW, ST_DASH_INPUT_ZONE)
    else:
        pygame.draw.rect(screen, RED, ST_DASH_INPUT_ZONE)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_DASH_INPUT_ZONE.width - 2, ST_DASH_INPUT_ZONE.height - 2)), (ST_DASH_INPUT_ZONE.x + 1, ST_DASH_INPUT_ZONE.y + 1))
    keybind_text = normal_font.render((f"{pygame.key.name(settings.dash_key)}".upper()), 1, WHITE)
    screen.blit(keybind_text, (ST_DASH_INPUT_ZONE.centerx - keybind_text.get_width()//2, ST_DASH_INPUT_ZONE.centery - keybind_text.get_height()//2))
    
    pygame.draw.rect(screen, RED, ST_SPECIAL_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_SPECIAL_BUTTON.width - 2, ST_SPECIAL_BUTTON.height - 2)), (ST_SPECIAL_BUTTON.x + 1, ST_SPECIAL_BUTTON.y + 1))
    keybind_text = font.render("Special", 1, WHITE)
    screen.blit(keybind_text, (ST_SPECIAL_BUTTON.centerx - keybind_text.get_width()//2, ST_SPECIAL_BUTTON.centery - keybind_text.get_height()//2))

    if input == "special":
        pygame.draw.rect(screen, YELLOW, ST_SPECIAL_INPUT_ZONE)
    else:
        pygame.draw.rect(screen, RED, ST_SPECIAL_INPUT_ZONE)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_SPECIAL_INPUT_ZONE.width - 2, ST_SPECIAL_INPUT_ZONE.height - 2)), (ST_SPECIAL_INPUT_ZONE.x + 1, ST_SPECIAL_INPUT_ZONE.y + 1))
    keybind_text = normal_font.render((f"{pygame.key.name(settings.special_key)}".upper()), 1, WHITE)
    screen.blit(keybind_text, (ST_SPECIAL_INPUT_ZONE.centerx - keybind_text.get_width()//2, ST_SPECIAL_INPUT_ZONE.centery - keybind_text.get_height()//2))
    
    pygame.draw.rect(screen, RED, ST_RESTART_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_RESTART_BUTTON.width - 2, ST_RESTART_BUTTON.height - 2)), (ST_RESTART_BUTTON.x + 1, ST_RESTART_BUTTON.y + 1))
    keybind_text = font.render("Restart", 1, WHITE)
    screen.blit(keybind_text, (ST_RESTART_BUTTON.centerx - keybind_text.get_width()//2, ST_RESTART_BUTTON.centery - keybind_text.get_height()//2))

    if input == "restart":
        pygame.draw.rect(screen, YELLOW, ST_RESTART_INPUT_ZONE)
    else:
        pygame.draw.rect(screen, RED, ST_RESTART_INPUT_ZONE)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_RESTART_INPUT_ZONE.width - 2, ST_RESTART_INPUT_ZONE.height - 2)), (ST_RESTART_INPUT_ZONE.x + 1, ST_RESTART_INPUT_ZONE.y + 1))
    keybind_text = normal_font.render((f"{pygame.key.name(settings.restart_key)}".upper()), 1, WHITE)
    screen.blit(keybind_text, (ST_RESTART_INPUT_ZONE.centerx - keybind_text.get_width()//2, ST_RESTART_INPUT_ZONE.centery - keybind_text.get_height()//2))


    pygame.draw.rect(screen, RED, ST_AZERTY_QWERTY_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_AZERTY_QWERTY_BUTTON.width - 2, ST_AZERTY_QWERTY_BUTTON.height - 2)), (ST_AZERTY_QWERTY_BUTTON.x + 1, ST_AZERTY_QWERTY_BUTTON.y + 1))
    if settings.azerty:
        keybind_text = normal_font.render("AZERTY", 1, WHITE)
    else:
        keybind_text = normal_font.render("QWERTY", 1, WHITE)
    screen.blit(keybind_text, (ST_AZERTY_QWERTY_BUTTON.centerx - keybind_text.get_width()//2, ST_AZERTY_QWERTY_BUTTON.centery - keybind_text.get_height()//2))

    pygame.draw.rect(screen, RED, ST_RESET_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_RESET_BUTTON.width - 2, ST_RESET_BUTTON.height - 2)), (ST_RESET_BUTTON.x + 1, ST_RESET_BUTTON.y + 1))
    keybind_text = font.render("Reset", 1, WHITE)
    screen.blit(keybind_text, (ST_RESET_BUTTON.centerx - keybind_text.get_width()//2, ST_RESET_BUTTON.centery - keybind_text.get_height()//2))

    pygame.draw.rect(screen, RED, ST_SAVE_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (ST_SAVE_BUTTON.width - 2, ST_SAVE_BUTTON.height - 2)), (ST_SAVE_BUTTON.x + 1, ST_SAVE_BUTTON.y + 1))
    keybind_text = font.render("Save", 1, WHITE)
    screen.blit(keybind_text, (ST_SAVE_BUTTON.centerx - keybind_text.get_width()//2, ST_SAVE_BUTTON.centery - keybind_text.get_height()//2))

    pygame.display.update()

def in_settings():
    run = True
    click = False
    input = False
    while run:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        if ST_LEFT_INPUT_ZONE.collidepoint((mx,my)) and click:
            input = "left"
        if ST_RIGHT_INPUT_ZONE.collidepoint((mx,my)) and click:
            input = "right"
        if ST_JUMP_INPUT_ZONE.collidepoint((mx,my)) and click:
            input = "jump"
        if ST_STOMP_INPUT_ZONE.collidepoint((mx,my)) and click:
            input = "stomp"
            
        if ST_DASH_INPUT_ZONE.collidepoint((mx,my)) and click:
            input = "dash"
        if ST_SPECIAL_INPUT_ZONE.collidepoint((mx,my)) and click:
            input = "special"
        if ST_RESTART_INPUT_ZONE.collidepoint((mx,my)) and click:
            input = "restart"
            

        if ST_AZERTY_QWERTY_BUTTON.collidepoint((mx,my)) and click:
            if settings.azerty:
                settings.qwerty_mapping()
            else:
                settings.azerty_mapping()
            
        if ST_RESET_BUTTON.collidepoint((mx,my)) and click:
            if settings.azerty:
                settings.azerty_mapping()
            else:
                settings.qwerty_mapping()
            
        if ST_SAVE_BUTTON.collidepoint((mx,my)) and click:
            run = False

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                if event.button == 3:
                    input = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if bool(input) == True:
                        input = False
                    else:
                        run = False
                if bool(input) == True:
                    settings.change_keybind(input, event.key)
                    input = False

        settings_draw_window(input)


##########
## Menu ##

def get_skin_img(skin_name):
    # Mage Skins
    if skin_name == "MaHuRe":
        return MaHuRe_N_IMG
    if skin_name == "MaHuDa":
        return MaHuDa_N_IMG
    if skin_name == "MaHuBl":
        return MaHuBl_N_IMG
    if skin_name == "MaHuGr":
        return MaHuGr_N_IMG
    if skin_name == "MaGoBa":
        return MaGoBa_N_IMG
    if skin_name == "MaFoBa":
        return MaFoBa_N_IMG
    if skin_name == "MaFeGr":
        return MaFeGr_N_IMG
    if skin_name == "MaDeBl":
        return MaDeBl_N_IMG
    if skin_name == "MaDeVi":
        return MaDeVi_N_IMG
    if skin_name == "MaGnBa":
        return MaGnBa_N_IMG
    if skin_name == "MaLiBl":
        return MaLiBl_N_IMG
    if skin_name == "MaSkBa":
        return MaSkBa_N_IMG
    if skin_name == "MaWiGr":
        return MaWiGr_N_IMG
    if skin_name == "MaWiBl":
        return MaWiBl_N_IMG
    if skin_name == "MaFaBa":
        return MaFaBa_N_IMG
    if skin_name == "MaDvRe":
        return MaDvRe_N_IMG

    # Knight Skins
    if skin_name == "KnSpHuBl":
        return KnSpHuBl_N_IMG
    if skin_name == "KnSpHuRe":
        return KnSpHuRe_N_IMG
    if skin_name == "KnSwHuBl":
        return KnSwHuBl_N_IMG
    if skin_name == "KnSwHuRe":
        return KnSwHuRe_N_IMG
    if skin_name == "KnSwSkBa":
        return KnSwSkBa_N_IMG
    if skin_name == "KnSwFeGr":
        return KnSwFeGr_N_IMG
    if skin_name == "KnSwFeBl":
        return KnSwFeBl_N_IMG
    if skin_name == "KnSwArRe":
        return KnSwArRe_N_IMG
    if skin_name == "KnSwArBl":
        return KnSwArBl_N_IMG
    if skin_name == "KnSwArGo":
        return KnSwArGo_N_IMG
    if skin_name == "KnSpWoBa":
        return KnSpWoBa_N_IMG
    if skin_name == "KnSpLiBa":
        return KnSpLiBa_N_IMG
    if skin_name == "KnSpHuGr":
        return KnSpHuGr_N_IMG
    if skin_name == "KnSpHuGo":
        return KnSpHuGo_N_IMG
    if skin_name == "KnMaDwRe":
        return KnMaDwRe_N_IMG
    if skin_name == "KnMaDwBl":
        return KnMaDwBl_N_IMG
##

def reassign_skin():
    if player.current_mage_skin_name == "MaHuRe":
        player.mage_skin = MaHuRe_N_IMG
        player.mage_skin_hit = MaHuRe_H_IMG
    if player.current_mage_skin_name == "MaHuDa":
        player.mage_skin = MaHuDa_N_IMG
        player.mage_skin_hit = MaHuDa_H_IMG
    if player.current_mage_skin_name == "MaHuBl":
        player.mage_skin = MaHuBl_N_IMG
        player.mage_skin_hit = MaHuBl_H_IMG
    if player.current_mage_skin_name == "MaHuGr":
        player.mage_skin = MaHuGr_N_IMG
        player.mage_skin_hit = MaHuGr_H_IMG
    if player.current_mage_skin_name == "MaGoBa":
        player.mage_skin = MaGoBa_N_IMG
        player.mage_skin_hit = MaGoBa_H_IMG
    if player.current_mage_skin_name == "MaFoBa":
        player.mage_skin = MaFoBa_N_IMG
        player.mage_skin_hit = MaFoBa_H_IMG
    if player.current_mage_skin_name == "MaFeGr":
        player.mage_skin = MaFeGr_N_IMG
        player.mage_skin_hit = MaFeGr_H_IMG
    if player.current_mage_skin_name == "MaDeBl":
        player.mage_skin = MaDeBl_N_IMG
        player.mage_skin_hit = MaDeBl_H_IMG
    if player.current_mage_skin_name == "MaDeVi":
        player.mage_skin = MaDeVi_N_IMG
        player.mage_skin_hit = MaDeVi_H_IMG
    if player.current_mage_skin_name == "MaGnBa":
        player.mage_skin = MaGnBa_N_IMG
        player.mage_skin_hit = MaGnBa_H_IMG
    if player.current_mage_skin_name == "MaLiBl":
        player.mage_skin = MaLiBl_N_IMG
        player.mage_skin_hit = MaLiBl_H_IMG
    if player.current_mage_skin_name == "MaSkBa":
        player.mage_skin = MaSkBa_N_IMG
        player.mage_skin_hit = MaSkBa_H_IMG
    if player.current_mage_skin_name == "MaWiGr":
        player.mage_skin = MaWiGr_N_IMG
        player.mage_skin_hit = MaWiGr_H_IMG
    if player.current_mage_skin_name == "MaWiBl":
        player.mage_skin = MaWiBl_N_IMG
        player.mage_skin_hit = MaWiBl_H_IMG
    if player.current_mage_skin_name == "MaFaBa":
        player.mage_skin = MaFaBa_N_IMG
        player.mage_skin_hit = MaFaBa_H_IMG
    if player.current_mage_skin_name == "MaDvRe":
        player.mage_skin = MaDvRe_N_IMG
        player.mage_skin_hit = MaDvRe_H_IMG

    if player.current_knight_skin_name == "KnSpHuBl":
        player.knight_skin = KnSpHuBl_N_IMG
        player.knight_skin_hit = KnSpHuBl_H_IMG
    if player.current_knight_skin_name == "KnSpHuRe":
        player.knight_skin = KnSpHuRe_N_IMG
        player.knight_skin_hit = KnSpHuRe_H_IMG
    if player.current_knight_skin_name == "KnSwHuBl":
        player.knight_skin = KnSwHuBl_N_IMG
        player.knight_skin_hit = KnSwHuBl_H_IMG
    if player.current_knight_skin_name == "KnSwHuRe":
        player.knight_skin = KnSwHuRe_N_IMG
        player.knight_skin_hit = KnSwHuRe_H_IMG
    if player.current_knight_skin_name == "KnSwSkBa":
        player.knight_skin = KnSwSkBa_N_IMG
        player.knight_skin_hit = KnSwSkBa_H_IMG
    if player.current_knight_skin_name == "KnSwFeGr":
        player.knight_skin = KnSwFeGr_N_IMG
        player.knight_skin_hit = KnSwFeGr_H_IMG
    if player.current_knight_skin_name == "KnSwFeBl":
        player.knight_skin = KnSwFeBl_N_IMG
        player.knight_skin_hit = KnSwFeBl_H_IMG
    if player.current_knight_skin_name == "KnSwArRe":
        player.knight_skin = KnSwArRe_N_IMG
        player.knight_skin_hit = KnSwArRe_H_IMG
    if player.current_knight_skin_name == "KnSwArBl":
        player.knight_skin = KnSwArBl_N_IMG
        player.knight_skin_hit = KnSwArBl_H_IMG
    if player.current_knight_skin_name == "KnSwArGo":
        player.knight_skin = KnSwArGo_N_IMG
        player.knight_skin_hit = KnSwArGo_H_IMG
    if player.current_knight_skin_name == "KnSpWoBa":
        player.knight_skin = KnSpWoBa_N_IMG
        player.knight_skin_hit = KnSpWoBa_H_IMG
    if player.current_knight_skin_name == "KnSpLiBa":
        player.knight_skin = KnSpLiBa_N_IMG
        player.knight_skin_hit = KnSpLiBa_H_IMG
    if player.current_knight_skin_name == "KnSpHuGr":
        player.knight_skin = KnSpHuGr_N_IMG
        player.knight_skin_hit = KnSpHuGr_H_IMG
    if player.current_knight_skin_name == "KnSpHuGo":
        player.knight_skin = KnSpHuGo_N_IMG
        player.knight_skin_hit = KnSpHuGo_H_IMG
    if player.current_knight_skin_name == "KnMaDwRe":
        player.knight_skin = KnMaDwRe_N_IMG
        player.knight_skin_hit = KnMaDwRe_H_IMG
    if player.current_knight_skin_name == "KnMaDwBl":
        player.knight_skin = KnMaDwBl_N_IMG
        player.knight_skin_hit = KnMaDwBl_H_IMG


def menu_draw_window():
    update_bg()

    title_text = title_font.render("Dodge", 1, DARK_RED)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2 + 1, title_text.get_height() + 2))
    title_text = title_font.render("Dodge", 1, WHITE)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, title_text.get_height()))

    pygame.draw.rect(screen, RED, PLAY_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (PLAY_BUTTON.width - 2, PLAY_BUTTON.height - 2)), (PLAY_BUTTON.x + 1, PLAY_BUTTON.y + 1))
    play_text = font.render("Play", 1, WHITE)
    screen.blit(play_text, (PLAY_BUTTON.centerx - play_text.get_width()//2, PLAY_BUTTON.centery - play_text.get_height()//2))

    pygame.draw.rect(screen, RED, SHOP_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (SHOP_BUTTON.width - 2, SHOP_BUTTON.height - 2)), (SHOP_BUTTON.x + 1, SHOP_BUTTON.y + 1))
    shop_text = font.render("Shop", 1, WHITE)
    screen.blit(shop_text, (SHOP_BUTTON.centerx - shop_text.get_width()//2, SHOP_BUTTON.centery - shop_text.get_height()//2))

    pygame.draw.rect(screen, RED, RANKING_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (RANKING_BUTTON.width - 2, RANKING_BUTTON.height - 2)), (RANKING_BUTTON.x + 1, RANKING_BUTTON.y + 1))
    ranking_text = font.render("Ranking", 1, WHITE)
    screen.blit(ranking_text, (RANKING_BUTTON.centerx - ranking_text.get_width()//2, RANKING_BUTTON.centery - ranking_text.get_height()//2))

    pygame.draw.rect(screen, RED, SETTING_BUTTON)
    screen.blit(pygame.transform.scale(PANEL_IMG, (SETTING_BUTTON.width - 2, SETTING_BUTTON.height - 2)), (SETTING_BUTTON.x + 1, SETTING_BUTTON.y + 1))
    settings_text = font.render("Settings", 1, WHITE)
    screen.blit(settings_text, (SETTING_BUTTON.centerx - settings_text.get_width()//2, SETTING_BUTTON.centery - settings_text.get_height()//2))

    if game.name_box_active:
        pygame.draw.rect(screen, YELLOW, NAME_ENTRY)
        screen.blit(NAME_ENTRY_ON, (NAME_ENTRY.x + 1, NAME_ENTRY.y + 1))
    else:
        pygame.draw.rect(screen, RED, NAME_ENTRY)
        screen.blit(NAME_ENTRY_OFF, (NAME_ENTRY.x + 1, NAME_ENTRY.y + 1))
    if game.player_name == "" and game.name_box_active == False:
        name_text = font.render("Enter Player Name", 1, WHITE)
    else:
        name_text = font.render(f"{game.player_name}", 1, WHITE)
    screen.blit(name_text, (NAME_ENTRY.centerx - name_text.get_width()//2, NAME_ENTRY.centery - name_text.get_height()//2))

    pygame.display.update()

def menu():
    try:
        with open("dodge_save.txt", "rb") as f:
            game.ranking_list = pickle.load(f)
    except:
        game.ranking_list.append({"name" : game.player_name,
                                  "time" : game.best_time,
                                  "job" : player.job,
                                  "best_time_mage" : 0,
                                  "best_time_knight" : 0,
                                  "best_time_dragon" : 0,
                                  "gold" : player.gold,
                                  "mage_skin" : ["MaHuRe"],
                                  "knight_skin" : ["KnSpHuBl"],
                                  "dragon_skin" : ["KnSpHuBl"],
                                  "current_mage_skin" : "MaHuRe",
                                  "current_knight_skin" : "KnSpHuBl",
                                  "current_dragon_skin" : "KnSpHuBl",
                                  "quest" : {}})

    run = True
    click = False
    while run:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        if game.name_box_active:
            player.rank = 0
            player.rank_name = "Unranked"
            player.rank_img = None
            player.rank_goal = "Survive 10s"
            if click:
                game.name_box_active = False

        exist = False
        for entry in game.ranking_list:
            if entry["name"] == game.player_name:
                game.best_time_ever = entry["time"]
                game.player_best_time_job = entry["job"]
                game.best_time = entry["best_time_mage"]
                player.best_time_mage = entry["best_time_mage"]
                player.best_time_knight = entry["best_time_knight"]
                player.gold = entry["gold"]
                player.skin_mage_list = entry["mage_skin"]
                player.skin_knight_list = entry["knight_skin"]
                player.current_mage_skin_name = entry["current_mage_skin"]
                player.current_knight_skin_name = entry["current_knight_skin"]
                player.quest_dic = entry["quest"]
                reassign_skin()
                exist = True
        if exist == False:
            game.player_rank_number = "N/A"
            game.best_time_ever = 0
            game.player_best_time_job = ""
            game.best_time = 0
            player.best_time_mage = 0
            player.best_time_knight = 0
            player.best_time_dragon = 0
            player.gold = 0
            player.skin_mage_list = ["MaHuRe"]
            player.skin_knight_list = ["KnSpHuBl"]
            player.skin_dragon_list = ["KnSpHuBl"]
            player.current_mage_skin_name = "MaHuRe"
            player.current_knight_skin_name = "KnSpHuBl"
            player.current_dragon_skin_name = "KnSpHuBl"
            player.quest_dic = {}
            if game.name_box_active == False:
                game.ranking_list.append({"name" : game.player_name,
                                          "time" : 0,
                                          "job" : "Mage",
                                          "best_time_mage" : 0,
                                          "best_time_knight" : 0,
                                          "best_time_dragon" : 0,
                                          "gold" : 0,
                                          "mage_skin" : ["MaHuRe"],
                                          "knight_skin" : ["KnSpHuBl"],
                                          "dragon_skin" : ["KnSpHuBl"],
                                          "current_mage_skin" : "MaHuRe",
                                          "current_knight_skin" : "KnSpHuBl",
                                          "current_dragon_skin" : "KnSpHuBl",
                                          "quest" : {}})
        exist = False

        reorder_ranking()
        get_ranking_info()

        quest_database.give_quest()
            
        if NAME_ENTRY.collidepoint((mx,my)) and click:
            if game.name_box_active:
                game.name_box_active = False
            else:
                game.name_box_active = True

        if PLAY_BUTTON.collidepoint((mx,my)) and click:
            job_select()

        if SHOP_BUTTON.collidepoint((mx,my)) and click:
            shopping()

        if RANKING_BUTTON.collidepoint((mx,my)) and click:
            ranking_screen()

        if SETTING_BUTTON.collidepoint((mx,my)) and click:
            in_settings()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if game.name_box_active:
                    if event.key == K_BACKSPACE:
                        game.player_name = game.player_name[:-1]
                    elif event.key == K_RETURN:
                        game.name_box_active = False
                    else:
                        game.player_name += event.unicode
                elif event.key == K_RETURN:
                    game.name_box_active = True

        menu_draw_window()


############
quest_database = quest_database()

menu()