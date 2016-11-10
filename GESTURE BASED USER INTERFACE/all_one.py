import pygame,cv2,numpy as np,sys
from colors import *
import os
from pygame.locals import *

''' Open cv --------------------------------'''
cap=cv2.VideoCapture(1)

cap.read()
kernel=np.ones((5,5),dtype=np.uint8)
 #transform
pt1=np.float32([[0,0],[640/2,480/2],[640,0]])
pt2=np.float32([[640,0],[640/2,480/2],[0,0]])
M=cv2.getAffineTransform(pt1,pt2)

lb=np.array([110,60,60])
ub=np.array([130,255,255])
lg=np.array([50,100,100])
ug=np.array([70,255,255])
'''pygame ------------------------------------'''
pygame.init()
FPS=30
fpsClock=pygame.time.Clock()
WIDTH,HEIGHT=640,480
DISPLAY=pygame.display.set_mode((WIDTH,HEIGHT))#,FULLSCREEN)
pygame.display.set_caption('FOR U ')
roi=pygame.image.load('pointer.png')
pointer=pygame.image.load('pointer.png')   # load pointer img
p_rect=pointer.get_rect()     #pointer rect or positiin
''' Other var ------------------------------'''

x,y=0,0

while(1):
    '''CV '''
    ret,im=cap.read()
    hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    mask_blue=cv2.inRange(hsv,lb,ub)
    mask_green=cv2.inRange(hsv,lg,ug)
    #im=cv2.warpAffine(im,M,(640,480))
    cv2.circle(im,(x,y),5,RED,5)
    cv2.imwrite('cam_img.jpg',im)
    erosion_blue=cv2.erode(mask_blue,kernel,iterations=1)
    erosion_green=cv2.erode(mask_green,kernel,iterations=1)
    dilation_blue=cv2.dilate(erosion_blue,kernel,iterations=5)
    dilation_green=cv2.dilate(erosion_green,kernel,iterations=5)
    for i in range(10,480,10):
        for j in range(10,640,10):
            if dilation_blue[i][j]>200:
                #print i,j
                roi=dilation_blue[10:200,20:50]
                print roi
                cv2.imwrite('roi.jpg',roi)
                yb=i
                xb=j
                break
    
    '''pointer '''
    p_rect.left=x
    p_rect.top=y

    '''pygame '''
    roi=pygame.image.load('roi.jpg')
    
    cam_img=pygame.image.load('cam_img.jpg')
    cam_img=pygame.transform.scale(cam_img,(145,105))
    DISPLAY.fill(AWHITE)
    DISPLAY.blit(roi,(10,400))
    DISPLAY.blit(pointer,p_rect)
    pygame.draw.rect(DISPLAY,AZURE,(640-150-5,HEIGHT-110-5,160,120))
    DISPLAY.blit(cam_img,(640-150,HEIGHT-110))
    #pygame.draw.circle(DISPLAY, BLUE, (x,y), 20, 0)    
    font = pygame.font.Font('freesansbold.ttf', 36)
    menu=font.render("MENU " ,True,BLUE)
    menu_rect=menu.get_rect(centerx=WIDTH/2,centery=250)
    text_image = font.render("WELCOME ", True, (0, 0, 255))
    text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100)
    DISPLAY.blit(text_image, text_rect)
    if p_rect.colliderect(text_rect):
        pygame.draw.rect(DISPLAY,RED,text_rect)
        print 'collide'
    
    DISPLAY.blit(menu,menu_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    #pygame.draw.circle(DISPLAY, BLUE, (x,y), 20, 0)
    pygame.display.update()
    fpsClock.tick(FPS)
    
 
