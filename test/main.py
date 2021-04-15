from moviepy.editor import *
import pygame
 
pygame.display.set_caption('Видео')
 
clip = VideoFileClip(r"video.mp4")
clip.preview()
 
pygame.quit()