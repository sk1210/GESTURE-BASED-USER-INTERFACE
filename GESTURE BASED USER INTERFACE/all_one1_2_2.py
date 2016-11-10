import pygame,cv2,numpy as np,sys
from colors import *
import os
from pygame.locals import *

'''import apps '''


'''--------------------- OpenCv --------------------------------'''
cap=cv2.VideoCapture(0)

cap.read()
kernel=np.ones((5,5),dtype=np.uint8)
#transform
pt1=np.float32([[0,0],[640/2,480/2],[640,0]])
pt2=np.float32([[640,0],[640/2,480/2],[0,0]])
M=cv2.getAffineTransform(pt1,pt2)

lb=np.array([110,60,60])
ub=np.array([130,255,255])

lg=np.array([40,70,70])
ug=np.array([80,255,255])

'''pygame ------------------------------------'''
pygame.init()
FPS=30
fpsClock=pygame.time.Clock()
WIDTH,HEIGHT=640,480
DISPLAY=pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)
pygame.display.set_caption('FOR U ')
#roi=pygame.image.load('pointer.png')
pointer=pygame.image.load('pointer.png')   # load pointer img
pointer=pygame.transform.scale(pointer,(30,30))
p_rect=pointer.get_rect()     #pointer rect or positiing
pointg=pygame.image.load('pointerg.png')
pg_rect=pointg.get_rect()
''' Other var ------------------------------'''

xb,yb=0,0
xg,yg=0,0

'''fnctions ---------------------------'''
def paint():
    global p_rect,pg_rect
    dx,dy=0,0
    DISPLAY.fill(WHITE)
    def color_select():
        while (1):
            pos=get_coordinate()
            p_rect.left,p_rect.top=pos[0]
            pg_rect.left,pg_rect.top=pos[1]

            x,y=p_rect.left,p_rect.top
            event_get()
            cam_pip()

            drop_rect=pygame.draw.rect(DISPLAY,AQUA,(color_rect.left,color_rect.top,100,400))
            if p_rect.collide_rect(drop_rect):
                DISPLAY.blit(pointer,p_rect)
                DISPLAY.blit(pointg,pg_rect)
        

            
            pygame.display.update()
            fpsClock.tick(FPS)
    
    
    while True:
        pos=get_coordinate()
        p_rect.left,p_rect.top=pos[0]
        pg_rect.left,pg_rect.top=pos[1]

        x,y=p_rect.left,p_rect.top
        event_get()

        '''Window'''
        opt_rect=pygame.draw.rect(DISPLAY,GREEN,(WIDTH-150-5,0,160,HEIGHT))
        

        font = pygame.font.Font('freesansbold.ttf', 30)
        color_opt=font.render("COLOR" ,True,BLUE)
        color_rect = color_opt.get_rect()
        color_rect.left=WIDTH-150+20
        color_rect.top=30
        
    

        '''Paint bg '''
        cam_pip()
        
        pygame.draw.line(DISPLAY,RED,(x,y),(dx,dy),3)
        DISPLAY.blit(color_opt,color_rect)

        '''logic'''
        if p_rect.colliderect(color_rect):
            pygame.draw.rect(DISPLAY,WHITE,color_rect,4)
            if pg_rect.colliderect(color_rect):
                color_select()
        #DISPLAY.blit(pointer,p_rect)
        #DISPLAY.blit(pointg,pg_rect)

        pygame.display.update()
        fpsClock.tick(FPS)
        dx,dy=x,y
    
        
    


def get_coordinate():
    global xg,yg,xb,yb
    ret,im=cap.read()
    im=cv2.warpAffine(im,M,(640,480))
    hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    mask_blue=cv2.inRange(hsv,lb,ub)
    mask_green=cv2.inRange(hsv,lg,ug)
    
    cv2.circle(im,(xb,yb),5,RED,5)
    cv2.circle(im,(xg,yg),5,GREEN,5)
    
    cv2.imwrite('cam_img.jpg',im)
    erosion_blue=cv2.erode(mask_blue,kernel,iterations=1)
    erosion_green=cv2.erode(mask_green,kernel,iterations=1)
    dilation_blue=cv2.dilate(erosion_blue,kernel,iterations=5)
    dilation_green=cv2.dilate(erosion_green,kernel,iterations=5)
    for i in range(10,480,10):
        for j in range(10,640,10):
            if dilation_blue[i][j]>200:
                #print i,j
                #roi=dilation_blue[10:200,20:50]
                #print roi
                #cv2.imwrite('roi.jpg',roi)
                yb=i
                xb=j
                break
            if dilation_green[i][j]>200:
                yg=i
                xg=j
    return ((xb,yb),(xg,yg))

def Application():
    global p_rect,pg_rect
    
    while True:
        pos=get_coordinate()
        p_rect.left,p_rect.top=pos[0]
        pg_rect.left,pg_rect.top=pos[1]
        

        ''' APPLICATION RECT '''
        DISPLAY.fill(AWHITE)
        app1=pygame.draw.rect(DISPLAY,BLACK,(40,100,165,80))
        app2=pygame.draw.rect(DISPLAY,BLACK,(235,100,165,80))
        app3=pygame.draw.rect(DISPLAY,BLACK,(430,100,165,80))
        app4=pygame.draw.rect(DISPLAY,BLACK,(40,250,165,80))
        app5=pygame.draw.rect(DISPLAY,BLACK,(235,250,165,80))
        app6=pygame.draw.rect(DISPLAY,BLACK,(430,250,165,80))
        '''logic'''
        if p_rect.colliderect(app1):
            pygame.draw.rect(DISPLAY,GREEN,app1,10)
            if pg_rect.colliderect(app1):
                paint()
        elif p_rect.colliderect(app2):
            pygame.draw.rect(DISPLAY,GREEN,app2,10)
        elif p_rect.colliderect(app3):
            pygame.draw.rect(DISPLAY,GREEN,app3,10)
        elif p_rect.colliderect(app4):
            pygame.draw.rect(DISPLAY,GREEN,app4,10)
        elif p_rect.colliderect(app5):
            pygame.draw.rect(DISPLAY,GREEN,app5,10)
        elif p_rect.colliderect(app6):
            pygame.draw.rect(DISPLAY,GREEN,app6,10)
        
        
        '''DISPLAY '''
        cam_pip()
        
        '''cam_img=pygame.image.load('cam_img.jpg')
        cam_img=pygame.transform.scale(cam_img,(145,105))
        pygame.draw.rect(DISPLAY,RED,(640-150-5,HEIGHT-110-5,160,120))
        DISPLAY.blit(cam_img,(640-150,HEIGHT-110))'''
        
        DISPLAY.blit(pointer,p_rect)
        DISPLAY.blit(pointg,pg_rect)
        event_get()

            
        pygame.display.update()
        fpsClock.tick(FPS)
        
        
def event_get():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:
            if event.key==K_RIGHT:
                pygame.quit()
                sys.exit()
def cam_pip():
    cam_img=pygame.image.load('cam_img.jpg')
    cam_img=pygame.transform.scale(cam_img,(145,105))
    pygame.draw.rect(DISPLAY,RED,(640-150-5,HEIGHT-110-5,160,120))
    DISPLAY.blit(cam_img,(640-150,HEIGHT-110))
        
    
                
        
        
while(1):
    '''CV '''
    pos=get_coordinate()

    '''pointer '''
    p_rect.left,p_rect.top=pos[0]
    pg_rect.left,pg_rect.top=pos[1] 

    '''pygame '''
    #roi=pygame.image.load('roi.jpg')

    cam_img=pygame.image.load('cam_img.jpg')
    cam_img=pygame.transform.scale(cam_img,(145,105))
    DISPLAY.fill(AWHITE)

    #DISPLAY.blit(roi,(10,400))
    
    DISPLAY.blit(pointer,p_rect)
    DISPLAY.blit(pointg,pg_rect)
    
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
        if pg_rect.colliderect(text_rect):
            pygame.draw.rect(DISPLAY,GREEN,text_rect)
            print 'dfksdf'
            Application()
        print 'collide'

    event_get()
    DISPLAY.blit(menu,menu_rect)
    pygame.display.update()

    #pygame.draw.circle(DISPLAY, BLUE, (x,y), 20, 0)
    pygame.display.update()
    fpsClock.tick(FPS)
    
 
