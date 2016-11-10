import pygame,cv2,numpy as np,sys
from colors import *
import os
from pygame.locals import *

''' Open cv --------------------------------'''
cap=cv2.VideoCapture(0)

cap.read()
kernel=np.ones((5,5),dtype=np.uint8)
 #transform
pt1=np.float32([[0,0],[640/2,480/2],[640,0]])
pt2=np.float32([[640,0],[640/2,480/2],[0,0]])
M=cv2.getAffineTransform(pt1,pt2)

lb=np.array([110,60,60])
ub=np.array([130,255,255])
'''pygame ------------------------------------'''
pygame.init()
FPS=30
fpsClock=pygame.time.Clock()
WIDTH,HEIGHT=640,480
DISPLAY=pygame.display.set_mode((WIDTH,HEIGHT))#,FULLSCREEN)
pygame.display.set_caption('FOR U ')

''' Other var ------------------------------'''


x,y=0,0

while(1):
    '''CV '''
    ret,im=cap.read()
    hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lb,ub)
    #im=cv2.warpAffine(im,M,(640,480))
    cv2.circle(im,(x,y),5,RED,5)
    cv2.imwrite('cam_img.jpg',im)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(erosion,kernel,iterations=5)

    for i in range(10,480,10):
        for j in range(10,640,10):
            if dilation[i][j]>200:
                #print i,j
                y=i
                x=j
                break
    
    

    '''pygame '''
    cam_img=pygame.image.load('cam_img.jpg')
    cam_img=pygame.transform.scale(cam_img,(145,105))
    DISPLAY.fill(AWHITE)
    pygame.draw.rect(DISPLAY,AZURE,(640-150-5,HEIGHT-110-5,160,120))
    DISPLAY.blit(cam_img,(640-150,HEIGHT-110))
    pygame.draw.circle(DISPLAY, BLUE, (x,y), 20, 0)    
    font = pygame.font.Font('freesansbold.ttf', 36)
    text_image = font.render("WELCOME ", True, (0, 0, 255))
    text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100)
    DISPLAY.blit(text_image, text_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.circle(DISPLAY, BLUE, (x,y), 20, 0)
    pygame.display.update()
    fpsClock.tick(FPS)
    
