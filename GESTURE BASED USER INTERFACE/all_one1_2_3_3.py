#race game updates

import pygame,cv2,numpy as np,sys
from colors import *
import os
from pygame.locals import *

'''--------------------- OpenCv --------------------------------'''

cap=cv2.VideoCapture(1)
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
DISPLAY=pygame.display.set_mode((WIDTH,HEIGHT))#,FULLSCREEN)
pygame.display.set_caption('FOR U')

cwd=os.getcwd()   # get crrent working directory
blit_dir=cwd+os.sep+'blits'
print blit_dir
#roi=pygame.image.load('pointer.png')
pointer=pygame.image.load(blit_dir+'\\'+ 'pointer.png')   # load pointer img
pointer=pygame.transform.scale(pointer,(30,30))
p_rect=pointer.get_rect()     #pointer rect or positiing
pointg=pygame.image.load(blit_dir+'\\'+ 'pointerg.png')
pg_rect=pointg.get_rect()


#backgrond
appback=pygame.image.load(blit_dir+'\\'+ 'back_app.jpg')
appback=pygame.transform.scale(appback,(640,480))
homeback=pygame.image.load(blit_dir+'\\'+ 'back_home.jpg')
homeback=pygame.transform.scale(homeback,(640,480))

#other images
close=pygame.image.load(blit_dir+'\\'+ 'close.png')
close=pygame.transform.scale(close,(80,50))
close_rect=close.get_rect()

''' icons load ------'''
paint_icon=pygame.image.load(blit_dir+'\\'+ 'paint.png')
camera_icon=pygame.image.load(blit_dir+'\\'+ 'camera.png')
game_icon=pygame.image.load(blit_dir+'\\'+ 'game.png')
paint_icon=pygame.transform.scale(paint_icon,(100,100))
camera_icon=pygame.transform.scale(camera_icon,(100,100))
game_icon=pygame.transform.scale(game_icon,(100,100))
paint_rect=paint_icon.get_rect()
camera_rect=camera_icon.get_rect()
game_rect=game_icon.get_rect()
#up=pygame.image.load('.png')

''' Other var ------------------------------'''

xb,yb=0,0
xg,yg=0,0

'''fnctions ---------------------------'''
def img_viewer():
    DISPLAY.fill(WHITE)
    
    global p_rect,pg_rect
    '''loading image data '''
    img_dir=blit_dir+os.sep+'clicks'
    backimg=pygame.image.load(img_dir+os.sep+'back.jpg')
    img_list=os.listdir(img_dir)
    back=pygame.image.load(blit_dir+os.sep+'back.png')
    back=pygame.transform.scale(back,(60,80))
    back_rect=back.get_rect()
    back_rect.left=520
    back_rect.top=30
    
    '''init variables '''
    imgRect_list1=[]  # 1 for icon
    imgRect_list2=[]  # 2 for image 
    load_img1=[]      #pygame image for icon
    load_img2=[]      #for main image 
    for i in xrange(len(img_list)):
        img=pygame.image.load(img_dir+os.sep+img_list[i])
        img_main=pygame.transform.scale(img,(400,400))
        img_icon=pygame.transform.scale(img,(100,100))
        imgRect1=img_icon.get_rect()
        imgRect2=img_main.get_rect()
        load_img1.append(img_icon)
        load_img2.append(img_main)
        imgRect_list1.append(imgRect1)
        imgRect_list2.append(imgRect2)
    '''functions '''
    def view(load_img2,i):
        while True:
            DISPLAY.fill(WHITE)
            pos=get_coordinate()
            p_rect.left,p_rect.top=pos[0]
            pg_rect.left,pg_rect.top=pos[1]

            DISPLAY.blit(load_img2[i],(40,40))
            DISPLAY.blit(back,back_rect)

            if p_rect.colliderect(back_rect):
                pygame.draw.rect(DISPLAY,RED,back_rect,3)
                if pg_rect.colliderect(back_rect):
                    return (1)
            DISPLAY.blit(pointer,p_rect)
            DISPLAY.blit(pointg,pg_rect)
            event_get()
            pygame.display.update()
            fpsClock.tick(FPS)
            
        
        '''main loop'''
    while True:
        DISPLAY.fill(WHITE)
        pos=get_coordinate()
        p_rect.left,p_rect.top=pos[0]
        pg_rect.left,pg_rect.top=pos[1]

        '''blit images'''

        xpos=40
        ypos=80
        count=0
        for i in xrange(len(load_img1)):
            DISPLAY.blit(load_img1[i],(xpos,ypos))
            imgRect_list1[i].left=xpos
            imgRect_list1[i].top=ypos
            if count==3:
                xpos=40
                ypos+=110
                count=0
            else:
                xpos+=110
                count+=1
        #DISPLAY.blit(img_list[1],(0,0))
        cam_pip()
        
        event_get()

        '''img open logic'''
        for i in xrange(len(load_img1)):
            #print imgRect_list1[i]
            if p_rect.colliderect(imgRect_list1[i]):
                zoom=pygame.transform.scale(load_img1[i],(110,110))
                DISPLAY.blit(zoom,(imgRect_list1[i].left-5,imgRect_list1[i].top-5))
                if pg_rect.colliderect(imgRect_list1[i]):
                    view(load_img2,i)
                    
        DISPLAY.blit(pointer,p_rect)
        DISPLAY.blit(pointg,pg_rect)
        pygame.display.update()
        fpsClock.tick(FPS)
        
def game():
    '''loading game data '''
    game_dir=blit_dir+os.sep+'game'
    print game_dir
    backimg=pygame.image.load(game_dir+os.sep+"newbg.jpg")
    backimg_rect=backimg.get_rect()
    car_image=pygame.image.load(game_dir+os.sep+'car.png')
    car_rect=car_image.get_rect()
    
    global p_rect,pg_rect
    '''init variables '''
    close_rect.left=WIDTH-160+20
    close_rect.top=20
    cx,cy=200,340
    px,py=200,340
    speed=20
    back_x,back_y=0,0
    turn=0
    DISPLAY.fill(WHITE)

    #main loop
    while True:
        
        pos=get_coordinate()
        p_rect.left,p_rect.top=pos[0]
        pg_rect.left,pg_rect.top=pos[1]
        px,py=p_rect.left,p_rect.top
        #event and update value
        event_get()
        back_y+=speed
        if back_y>=480:
            back_y=0
        '''logic '''
        
        if (px<160 and px >0):
            turn=-10
        elif (px>320 and px<460):
            turn=10
        elif (px>160 and px<320):
            turn=0
        if (cx>120 and cx <280): 
            cx+=turn
            if cx <=120 or cx >=280:
                cx-=turn
        
        '''DISPLAY'''
        DISPLAY.fill(BLACK)
        DISPLAY.blit(backimg,(back_x,back_y-480))
        DISPLAY.blit(backimg,(back_x,back_y))
        opt_box=pygame.draw.rect(DISPLAY,BLACK,(WIDTH-160,0,160,HEIGHT))
        bottom_box=pygame.draw.rect(DISPLAY,BLACK,(0,HEIGHT-40,WIDTH,40))
        pygame.draw.rect(DISPLAY,PURPLE,(0,0,WIDTH-160,HEIGHT-40),3)
        left1=pygame.draw.rect(DISPLAY,RED,(0,HEIGHT-38,160,38))
        center=pygame.draw.rect(DISPLAY,WHITE,(160,HEIGHT-38,160,38))
        right1=pygame.draw.rect(DISPLAY,RED,(320,HEIGHT-38,160,38))
        pygame.draw.rect(DISPLAY,SILVER,(0,HEIGHT-40,WIDTH,40),3)
        pygame.draw.circle(DISPLAY,SILVER,(px,HEIGHT-20),20)
        DISPLAY.blit(car_image,(cx,cy))     #blit car
        cam_pip()
        DISPLAY.blit(close,close_rect)

        '''pointer visibility '''
        
        if p_rect.left>640-170:
            DISPLAY.blit(pointer,p_rect)
        if p_rect.colliderect(close_rect):
            pygame.draw.rect(DISPLAY,WHITE,close_rect,3)
            if pg_rect.collide_rect(close_rect):
                return "return to app "

        pygame.display.update()
        fpsClock.tick(40)
        
        
        
        
def paint():
    global p_rect,pg_rect
    dx,dy=0,0
    DISPLAY.fill(WHITE)
    close_rect.left=10
    close_rect.top=HEIGHT-55

    def color_select():
        font = pygame.font.Font('freesansbold.ttf', 30)
        red_color=font.render("RED" ,True,BLUE)
        red_color_rect=red_color.get_rect()
        blue_color=font.render("BLUE",True,RED)
        blue_color_rect=blue_color.get_rect()
        red_color_rect.left=WIDTH-150+15
        blue_color_rect.left=WIDTH-150+15
        red_color_rect.top=color_rect.bottom
        blue_color_rect.top=color_rect.bottom+50
        
        while(1):
            pos=get_coordinate()
            p_rect.left,p_rect.top=pos[0]
            pg_rect.left,pg_rect.top=pos[1]

            x,y=p_rect.left,p_rect.top
            event_get()
            cam_pip()

            drop_rect=pygame.draw.rect(DISPLAY,WHITE,(WIDTH-150,color_rect.bottom,150,300))
            col_posy=color_rect.bottom
            col_posx=WIDTH-150+10+50+10
            '''COLORS '''
            red_color=pygame.draw.rect(DISPLAY,RED,(WIDTH-150+10,col_posy +5,50,50))
            purple_color=pygame.draw.rect(DISPLAY,PURPLE,(col_posx,col_posy +5,50,50))
            col_posy+=5+50+10

            blue_color=pygame.draw.rect(DISPLAY,BLUE,(WIDTH-150+10,col_posy,50,50))
            maroon_color=pygame.draw.rect(DISPLAY,MAROON,(col_posx,col_posy,50,50))
            col_posy+=50+10
            
            green_color=pygame.draw.rect(DISPLAY,GREEN,(WIDTH-150+10,col_posy,50,50))
            black_color=pygame.draw.rect(DISPLAY,BLACK,(col_posx,col_posy,50,50))
            col_posy+=50+10
            
            yellow_color=pygame.draw.rect(DISPLAY,YELLOW,(WIDTH-150+10,col_posy,50,50))
            olive_color=pygame.draw.rect(DISPLAY,OLIVE,(col_posx,col_posy,50,50))
            col_posy+=50+10

            pygame.draw.rect(DISPLAY,BLACK,drop_rect,4)
            print drop_rect
            if p_rect.colliderect(drop_rect):
                #DISPLAY.blit(red_color,red_color_rect)
                #DISPLAY.blit(blue_color,blue_color_rect)
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
        opt_rect=pygame.draw.rect(DISPLAY,GREEN,(WIDTH-150-5,0,160,HEIGHT))   #side rectangle
        
        font = pygame.font.Font('freesansbold.ttf', 30)
        color_opt=font.render("COLOR" ,True,BLUE)
        color_rect = color_opt.get_rect()
        color_rect.left=WIDTH-150+20
        color_rect.top=30

        '''Paint bg '''
        pygame.draw.line(DISPLAY,RED,(x,y),(dx,dy),6)
        DISPLAY.blit(color_opt,color_rect)
        base_rect=pygame.draw.rect(DISPLAY,(0,0,255,20),(0,HEIGHT-60,WIDTH,60))
        DISPLAY.blit(close,close_rect)
        cam_pip()

        '''logic'''
        if p_rect.left>640-160:
            DISPLAY.blit(pointer,p_rect)
        if p_rect.colliderect(color_rect):
            pygame.draw.rect(DISPLAY,WHITE,color_rect,4)
            
            if pg_rect.colliderect(color_rect):
                color_select()
            DISPLAY.blit(pointer,p_rect)
            DISPLAY.blit(pointg,pg_rect)
        elif p_rect.top> 480-60:
            DISPLAY.blit(pointer,p_rect)
            if p_rect.colliderect(close_rect):
                pygame.draw.rect(DISPLAY,WHITE,close_rect,5)
                if pg_rect.colliderect(close_rect):
                    return ('retrn to app ')
            if pg_rect.top>480-55:
                DISPLAY.blit(pointg,pg_rect)

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
    paint_rect.left,paint_rect.top=50,100
    camera_rect.left,camera_rect.top=245,100
    game_rect.left,game_rect.top=440,100

    while True:
        pos=get_coordinate()
        p_rect.left,p_rect.top=pos[0]
        pg_rect.left,pg_rect.top=pos[1]
        

        ''' APPLICATION RECT '''
        DISPLAY.fill(AWHITE)
        DISPLAY.blit(appback,(0,0))

        DISPLAY.blit(paint_icon,paint_rect)
        DISPLAY.blit(camera_icon,camera_rect)
        DISPLAY.blit(game_icon,game_rect)
        
        '''app1=pygame.draw.rect(DISPLAY,BLACK,(40,100,165,80))
        app2=pygame.draw.rect(DISPLAY,BLACK,(235,100,165,80))
        app3=pygame.draw.rect(DISPLAY,BLACK,(430,100,165,80))
        app4=pygame.draw.rect(DISPLAY,BLACK,(40,250,165,80))
        app5=pygame.draw.rect(DISPLAY,BLACK,(235,250,165,80))
        app6=pygame.draw.rect(DISPLAY,BLACK,(430,250,165,80))'''
        '''logic'''
        if p_rect.colliderect(paint_rect):
            pygame.draw.rect(DISPLAY,WHITE,paint_rect,5)
            if pg_rect.colliderect(paint_rect):
                paint()
        elif p_rect.colliderect(camera_rect):
            pygame.draw.rect(DISPLAY,WHITE,camera_rect,5)
            if pg_rect.colliderect(camera_rect):
                img_viewer()
        elif p_rect.colliderect(game_rect):
            pygame.draw.rect(DISPLAY,WHITE,game_rect,5)
            if pg_rect.colliderect(game_rect):
                game()                             #call game 

        '''DISPLAY '''
        cam_pip()

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
            elif event.key==K_1:
                Application()
            elif event.key==K_p:
                paint()
            elif event.key==K_g:
                game()
            elif event.key==K_i:
                img_viewer()
def cam_pip():
    cam_img=pygame.image.load('cam_img.jpg')
    cam_img=pygame.transform.scale(cam_img,(145,105))
    pygame.draw.rect(DISPLAY,AZURE,(640-150-5,HEIGHT-110-5,160,120))
    DISPLAY.blit(cam_img,(WIDTH-150,HEIGHT-110))
        
    
'''MAIN PROGRAM LOOP '''        
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
    DISPLAY.blit(homeback,(0,0))

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
            Application()
    event_get()
    DISPLAY.blit(menu,menu_rect)
    pygame.display.update()

    #pygame.draw.circle(DISPLAY, BLUE, (x,y), 20, 0)
    pygame.display.update()
    fpsClock.tick(FPS)


    
 
