#img viewer updates
#update of paint

import pygame,cv2,numpy as np,sys,time
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
FPS=50
fpsClock=pygame.time.Clock()
WIDTH,HEIGHT=640,480
DISPLAY=pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)
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
user=pygame.image.load(blit_dir+os.sep+"user.png")
user=pygame.transform.scale(user,(100,120))

user_rect=user.get_rect()
user_rect.left=80
user_rect.top=100

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
img_view=pygame.image.load(blit_dir+os.sep+'img_viewer.png')
img_view=pygame.transform.scale(img_view,(100,100))
img_rect=img_view.get_rect()

key_icon=pygame.image.load(blit_dir+os.sep+'key_icon.png')
key_icon=pygame.transform.scale(key_icon,(100,100))
key_rect=key_icon.get_rect()

''' Other var ------------------------------'''

xb,yb=0,0
xg,yg=0,0

'''fnctions ---------------------------'''

def keyboard():
    font = pygame.font.Font('freesansbold.ttf',20)
    textfont=pygame.font.Font('freesansbold.ttf',20)
    font_obj=font.render("GALLERY" ,True,PURPLE)

    
    global p_rect,pg_rect
    x1=10
    key_width,key_height=73,57
    main_rect=pygame.Rect(0,480-280,640,300)
    alpha1=[('q','Q'),('w','W'),('e''E'),('r','R'),('t','T'),('y','Y'),('u','U'),('i','I')]
    alpha2=[('a','A'),('s','S'),('d','D'),('f','F'),('g','G'),('h','H'),('j','J'),('k','K')]
    alpha3=[('z','Z'),('x','X'),('c','C'),('v','V'),('b','B'),('n','N'),('m','M'),('p','P')]
    alpha4=[('o','O'),('l','L'),('_____','_____'),('Caps Lock','Caps Lock'),('Backspace','Backspace')]
    alpha_rect1=[]
    alpha_rect2=[]
    alpha_rect3=[]
    alpha_rect4=[]
    alpha_rect5=[]
    caps=0
    select=None
    text=''
    
    
    while (1):
                            
        pos=get_coordinate()
        p_rect.left,p_rect.top=pos[0]
        pg_rect.left,pg_rect.top=pos[1]
        DISPLAY.fill(WHITE)
        pygame.draw.rect(DISPLAY,SILVER,main_rect)
        '''draw keys '''
        x1,y1=main_rect.left+10,main_rect.top+10
        
        for i in xrange(8):
            temp=pygame.draw.rect(DISPLAY,MAROON,(x1,y1,key_width,key_height))
            font_obj=font.render(alpha1[i][caps] ,True,WHITE)
            font_rect=font_obj.get_rect(centerx=x1+int(key_width/2),centery=y1+int(key_height/2))
            DISPLAY.blit(font_obj,font_rect)
            x1+=(key_width+5)
            alpha_rect1.append(temp)
        x1,y1=main_rect.left+10,main_rect.top+10+key_height+10
        for i in xrange(8):
            temp=pygame.draw.rect(DISPLAY,MAROON,(x1,y1,key_width,key_height))
            font_obj=font.render(alpha2[i][caps] ,True,WHITE)
            font_rect=font_obj.get_rect(centerx=x1+int(key_width/2),centery=y1+int(key_height/2))
            DISPLAY.blit(font_obj,font_rect)
            x1+=(key_width+5)
            alpha_rect2.append(temp)
        x1,y1=main_rect.left+10,main_rect.top+key_height*2+10*3
        for i in xrange(8):
            temp=pygame.draw.rect(DISPLAY,MAROON,(x1,y1,key_width,key_height))
            font_obj=font.render(alpha3[i][caps] ,True,WHITE)
            font_rect=font_obj.get_rect(centerx=x1+int(key_width/2),centery=y1+int(key_height/2))
            DISPLAY.blit(font_obj,font_rect)
            x1+=(key_width+5)
            alpha_rect3.append(temp)
        x1,y1=main_rect.left+10,main_rect.top+key_height*3+10*4
        for i in xrange(5):
        
            if i<2:
                temp=pygame.draw.rect(DISPLAY,MAROON,(x1,y1,key_width,key_height))
                font_obj=font.render(alpha4[i][caps] ,True,WHITE)
                font_rect=font_obj.get_rect(centerx=x1+int(key_width/2),centery=y1+int(key_height/2))
                DISPLAY.blit(font_obj,font_rect)
                x1+=(key_width+5)
                alpha_rect4.append(temp)
            if i==2:
                temp=pygame.draw.rect(DISPLAY,MAROON,(x1,y1,int(key_width*2.5),key_height))
                font_obj=font.render(alpha4[i][caps] ,True,WHITE)
                font_rect=font_obj.get_rect(centerx=x1+int(key_width*2.5/2),centery=y1+int(key_height/2))
                DISPLAY.blit(font_obj,font_rect)
                x1+=int(key_width*2.5+5)
                alpha_rect4.append(temp)
            if i==3:
                temp=pygame.draw.rect(DISPLAY,MAROON,(x1,y1,int(key_width*1.5),key_height))
                font_obj=font.render(alpha4[i][caps] ,True,WHITE)
                font_rect=font_obj.get_rect(centerx=x1+int(key_width*1.5/2),centery=y1+int(key_height/2))
                DISPLAY.blit(font_obj,font_rect)
                x1+=int(key_width*1.5+5)
                alpha_rect4.append(temp)
            if i==4:
                temp=pygame.draw.rect(DISPLAY,MAROON,(x1,y1,int(key_width*2),key_height))
                font_obj=font.render(alpha4[i][caps] ,True,WHITE)
                font_rect=font_obj.get_rect(centerx=x1+int(key_width*2/2),centery=y1+int(key_height/2))
                DISPLAY.blit(font_obj,font_rect)
                x1+=int(key_width*2+5)
                alpha_rect4.append(temp)
                
                
                
        for i in xrange(8):
            if p_rect.colliderect(alpha_rect1[i]):
                pygame.draw.rect(DISPLAY,RED,alpha_rect1[i],4)
                if pg_rect.colliderect(alpha_rect1[i]) and not (select==i):
                    text+=alpha1[i][caps]
                    select=i
            if p_rect.colliderect(alpha_rect2[i]):
                pygame.draw.rect(DISPLAY,RED,alpha_rect2[i],4)
                if pg_rect.colliderect(alpha_rect2[i]) and not (select==i):
                    text+=alpha2[i][caps]
                    select=i
            if p_rect.colliderect(alpha_rect3[i]):
                pygame.draw.rect(DISPLAY,RED,alpha_rect3[i],4)
                if pg_rect.colliderect(alpha_rect3[i]) and not (select==i):
                    text+=alpha3[i][caps]
                    select=i
            if i<=4:
                if p_rect.colliderect(alpha_rect4[i]):
                    pygame.draw.rect(DISPLAY,RED,alpha_rect4[i],4)
                    if pg_rect.colliderect(alpha_rect4[i]) and not (select==i):
                        select=i
                        if i<2:
                            text+=alpha1[i][caps]
                            select=i
                        elif i==2:
                            text+=''
                            select=i
                        elif i==3:
                            select=i
                            if caps==1:
                                caps=0
                            else:
                                caps=1
                        elif i==4:
                            text=text[0:len(text)-1]
                            print text
        text_obj=textfont.render(text,True,BLACK)
        text_rect=text_obj.get_rect()
        text_rect.left=30
        text_rect.top=30
        DISPLAY.blit(text_obj,text_rect)
        DISPLAY.blit(pointer,p_rect)
        DISPLAY.blit(pointg,pg_rect)
        event_get()
        pygame.display.update()
        fpsClock.tick(FPS)
    
def img_viewer():
            
    DISPLAY.fill(AWHITE)

    global p_rect,pg_rect

    '''loading image data '''

    img_dir=blit_dir+os.sep+'clicks'
    backimg=pygame.image.load(img_dir+os.sep+'back.jpg')
    img_list=os.listdir(img_dir)
    back=pygame.image.load(blit_dir+os.sep+'back.png')
    back=pygame.transform.scale(back,(100,80))
    back_rect=back.get_rect()
    back_rect.left=520
    back_rect.top=30
    close_rect.left=10
    close_rect.top=HEIGHT-55
    font = pygame.font.Font('freesansbold.ttf',45)
    font_obj=font.render("GALLERY" ,True,PURPLE)
    font_rect=font_obj.get_rect()
    font_rect.left=200
    font_rect.top=20
    
    
    '''init variables '''
    
    imgRect_list1=[]  # 1 for icon
    imgRect_list2=[]  # 2 for image 
    load_img1=[]      #pygame image for icon
    load_img2=[]      #for main image
    
    for i in xrange(len(img_list)):
        img=pygame.image.load(img_dir+os.sep+img_list[i])
        img_main=pygame.transform.scale(img,(450,400))
        img_icon=pygame.transform.scale(img,(100,100))
        imgRect1=img_icon.get_rect()
        imgRect2=img_main.get_rect()
        load_img1.append(img_icon)
        load_img2.append(img_main)
        imgRect_list1.append(imgRect1)
        imgRect_list2.append(imgRect2)
    '''functions '''
    def trans((loadimg1,img_rect1),(loadimg2,img_rect2),side):      #1 is right and 0 is left
        if side==1:
            img_rect2.right=0
            img_rect1.left=40
        elif side==2:
            img_rect1.left=40
            img_rect2.left=640
        while True:
            #pos=get_coordinate()
            #p_rect.left,p_rect.top=pos[0]
            #pg_rect.left,pg_rect.top=pos[1]
            #px,py=p_rect.left,p_rect.top
            
            DISPLAY.fill(WHITE)
            if side==1:
                if img_rect1.left<640:
                    DISPLAY.blit(loadimg1,(img_rect1.left,40))
                    img_rect1.left+=20
                else:
                    break
                if img_rect2.left<=40:
                    DISPLAY.blit(loadimg2,(img_rect2.left,40))
                    img_rect2.left+=20
            if side==2:
                if img_rect1.right>0:
                    DISPLAY.blit(loadimg1,(img_rect1.left,40))
                    img_rect1.right-=20
                else:
                    break
                if img_rect2.left>=40:
                    DISPLAY.blit(loadimg2,(img_rect2.left,40))
                    img_rect2.right-=10
                    
                
            pygame.draw.rect(DISPLAY,WHITE,(640-150,0,160,480))
            DISPLAY.blit(back,back_rect)
            DISPLAY.blit(pointer,p_rect)
            DISPLAY.blit(pointg,pg_rect)

            cam_pip()
            pygame.display.update()
            fpsClock.tick(60)
    
    def view(load_img2,i):
        rmovcount=0
        lmovcount=0
        while True:
            DISPLAY.fill(WHITE)
            pos=get_coordinate()
            p_rect.left,p_rect.top=pos[0]
            pg_rect.left,pg_rect.top=pos[1]
            cam_pip()
            mov1=pygame.draw.rect(DISPLAY,RED,(40,0,60,200))
            mov2=pygame.draw.rect(DISPLAY,RED,(300,0,60,200))
            mov3=pygame.draw.rect(DISPLAY,RED,(40,250,60,200))
            mov4=pygame.draw.rect(DISPLAY,RED,(300,250,60,200))
            DISPLAY.blit(load_img2[i],(40,40))
            DISPLAY.blit(back,back_rect)
            DISPLAY.blit(font_obj,font_rect)
            DISPLAY.blit(close,close_rect)
            if i==len(load_img2):
                i=0
            if p_rect.colliderect(mov1):
                rmovcount=1
            if (p_rect.colliderect(mov2) and rmovcount==1):
                rmovcount=0
                trans((load_img2[i],imgRect_list2[i]),(load_img2[i+1],imgRect_list2[i+1]),side=1)
                i=i+1
            if p_rect.colliderect(mov4):
                lmovcount=1
            if (p_rect.colliderect(mov3) and lmovcount==1):
                lmovcount=0
                trans((load_img2[i],imgRect_list2[i]),(load_img2[i-1],imgRect_list2[i-1]),side=2)
                i=i-1

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

        DISPLAY.fill(YELLOW)
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
        DISPLAY.blit(font_obj,font_rect)
        DISPLAY.blit(back,back_rect)
        if p_rect.colliderect(back_rect):
                pygame.draw.rect(DISPLAY,RED,back_rect,3)
                if pg_rect.colliderect(back_rect):
                    return (1)
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

        #coordinate
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
        b_flag=0
        g_flag=0
        for i in range(10,240,15):
            for j in range(10,640,15):
                if dilation_blue[i][j]>200:
                    yb=i
                    xb=j
                    b_flag=1
                    if g_flag==1:
                        break
                if dilation_green[i][j]>200:
                    yg=i
                    xg=j
                    g_flag=1
                    if b_flag==1:
                        break
            if(b_flag and g_flag):
                break
                    
        pos=((xb,yb),(xg,yg))
        #pos=((10,10),(10,10))
        #end of get coordinate
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
        DISPLAY.blit(backimg,(back_x-100,back_y-480))
        DISPLAY.blit(backimg,(back_x-100,back_y))
        opt_box=pygame.draw.rect(DISPLAY,BLACK,(WIDTH-160,0,160,HEIGHT))
        bottom_box=pygame.draw.rect(DISPLAY,BLACK,(0,HEIGHT-40,WIDTH,40))
        pygame.draw.rect(DISPLAY,PURPLE,(0,0,WIDTH-160,HEIGHT-40),3)
        left1=pygame.draw.rect(DISPLAY,RED,(0,HEIGHT-38,160,38))
        center=pygame.draw.rect(DISPLAY,WHITE,(160,HEIGHT-38,160,38))
        right1=pygame.draw.rect(DISPLAY,RED,(320,HEIGHT-38,160,38))
        pygame.draw.rect(DISPLAY,SILVER,(0,HEIGHT-40,WIDTH,40),3)
        pygame.draw.circle(DISPLAY,SILVER,(px,HEIGHT-20),20)
        DISPLAY.blit(car_image,(cx,cy))                     #blit car
        cam_pip()
        DISPLAY.blit(close,close_rect)

        '''pointer visibility '''
        
        if p_rect.left>640-170:
            DISPLAY.blit(pointer,p_rect)
        if p_rect.colliderect(close_rect):
            pygame.draw.rect(DISPLAY,WHITE,close_rect,3)
            if pg_rect.colliderect(close_rect):
                return "return to app "


        pygame.display.update()
        fpsClock.tick(40)
        
        
        
        
def paint():
    global p_rect,pg_rect
    dx,dy=0,0
    dxg,dyg=0,0
    DISPLAY.fill(WHITE)
    close_rect.left=10
    close_rect.top=HEIGHT-55
    p_color=RED


    def color_select():
        global p_color
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
            col_posx=WIDTH-150+10+60+10
            '''COLORS '''
            red_color=pygame.draw.rect(DISPLAY,RED,(WIDTH-150+10,col_posy +5,60,60))
            purple_color=pygame.draw.rect(DISPLAY,PURPLE,(col_posx,col_posy +5,60,60))
            col_posy+=5+60+10

            blue_color=pygame.draw.rect(DISPLAY,BLUE,(WIDTH-150+10,col_posy,60,60))
            maroon_color=pygame.draw.rect(DISPLAY,MAROON,(col_posx,col_posy,60,60))
            col_posy+=60+10
            
            green_color=pygame.draw.rect(DISPLAY,GREEN,(WIDTH-150+10,col_posy,60,60))
            black_color=pygame.draw.rect(DISPLAY,BLACK,(col_posx,col_posy,60,60))
            col_posy+=60+10
            
            yellow_color=pygame.draw.rect(DISPLAY,YELLOW,(WIDTH-150+10,col_posy,60,60))
            olive_color=pygame.draw.rect(DISPLAY,OLIVE,(col_posx,col_posy,60,60))
            col_posy+=60+10

            pygame.draw.rect(DISPLAY,BLACK,drop_rect,4)
            
            if p_rect.colliderect(drop_rect):
                #DISPLAY.blit(red_color,red_color_rect)
                #DISPLAY.blit(blue_color,blue_color_rect)
                DISPLAY.blit(pointer,p_rect)
                DISPLAY.blit(pointg,pg_rect)
                '''color collide '''
                if p_rect.colliderect(red_color):
                    pygame.draw.rect(DISPLAY,WHITE,red_color,3)
                    if pg_rect.colliderect(red_color):
                        p_color=RED
                        return(p_color)
                elif p_rect.colliderect(purple_color):
                    pygame.draw.rect(DISPLAY,WHITE,purple_color,3)
                    if pg_rect.colliderect(purple_color):
                        p_color=PURPLE
                        return(p_color)
                elif p_rect.colliderect(blue_color):
                    pygame.draw.rect(DISPLAY,WHITE,blue_color,3)
                    if pg_rect.colliderect(blue_color):
                        p_color=BLUE
                        return(p_color)
                elif p_rect.colliderect(maroon_color):
                    pygame.draw.rect(DISPLAY,WHITE,maroon_color,3)
                    if pg_rect.colliderect(maroon_color):
                        p_color=MAROON
                        return(p_color)
                elif p_rect.colliderect(green_color):
                    pygame.draw.rect(DISPLAY,WHITE,green_color,3)
                    if pg_rect.colliderect(green_color):
                        p_color=GREEN
                        return(p_color)
                
                elif p_rect.colliderect(black_color):
                    pygame.draw.rect(DISPLAY,WHITE,black_color,3)
                    if pg_rect.colliderect(black_color):
                        p_color=BLACK
                        return(p_color)
                elif p_rect.colliderect(yellow_color):
                    pygame.draw.rect(DISPLAY,WHITE,yellow_color,3)
                    if pg_rect.colliderect(yellow_color):
                        p_color=YELLOW
                        return(p_color)
                elif p_rect.colliderect(olive_color):
                    pygame.draw.rect(DISPLAY,WHITE,olive_color,3)
                    if pg_rect.colliderect(olive_color):
                        p_color=OLIVE
                        return(p_color)
                
                

            pygame.display.update()
            fpsClock.tick(FPS)
    
    
    while True:
        pos=get_coordinate()
        p_rect.left,p_rect.top=pos[0]
        pg_rect.left,pg_rect.top=pos[1]
        x,y=p_rect.left,p_rect.top
        xg,yg=pg_rect.left,pg_rect.top
        event_get()
        #touch_box=pygame.Rect(p_rect.centerx-50,p_rect.centery-50,80,80)
        '''
        img1=cv2.imread('cam_img.jpg')
        img2=cv2.imread('white.jpg')
        
        cv2.line(img2,(x,y),(dx,dy),p_color,6)
        dst=cv2.addWeighted(img1,0.5,img2,0.5,0)
        cv2.imwrite('white.jpg',img2)
        cv2.imwrite('dst.jpg',dst)
        im=pygame.image.load('dst.jpg')'''
        
        

        '''Window'''
        #DISPLAY.blit(im,(0,0))
        opt_rect=pygame.draw.rect(DISPLAY,SILVER,(WIDTH-150-5,0,160,HEIGHT))   #side rectangle
        
        font = pygame.font.Font('freesansbold.ttf', 30)
        color_opt=font.render("COLOR" ,True,MAROON)
        color_rect = color_opt.get_rect()
        color_rect.left=WIDTH-150+20
        color_rect.top=30

        '''Paint bg '''
        #if ((dxg==xg) and (dyg==yg)):
        pygame.draw.line(DISPLAY,p_color,(x,y),(dx,dy),6)
        DISPLAY.blit(color_opt,color_rect)
        base_rect=pygame.draw.rect(DISPLAY,(0,128,128),(0,HEIGHT-60,WIDTH,60))
        DISPLAY.blit(close,close_rect)
        cam_pip()

        '''logic'''

        if p_rect.left>640-160:
            DISPLAY.blit(pointer,p_rect)
        if p_rect.colliderect(color_rect):
            pygame.draw.rect(DISPLAY,WHITE,color_rect,4)
            
            if pg_rect.colliderect(color_rect):
                p_color=color_select()
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
        #DISPLAY.blit(pointer,p_rect)

        pygame.display.update()
        fpsClock.tick(FPS)
        dx,dy=x,y
        dxg,dyg=xg,yg
    
        
    
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
    img_rect.left,img_rect.top=245,100
    game_rect.left,game_rect.top=440,100
    key_rect.left,key_rect.top=50,250

    while True:
        pos=get_coordinate()
        p_rect.left,p_rect.top=pos[0]
        pg_rect.left,pg_rect.top=pos[1]
        

        ''' APPLICATION RECT '''
        DISPLAY.fill(AWHITE)
        DISPLAY.blit(appback,(0,0))

        DISPLAY.blit(paint_icon,paint_rect)
        DISPLAY.blit(img_view,img_rect)
        DISPLAY.blit(game_icon,game_rect)
        DISPLAY.blit(key_icon,key_rect)
        
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
        elif p_rect.colliderect(img_rect):
            pygame.draw.rect(DISPLAY,WHITE,img_rect,5)
            if pg_rect.colliderect(img_rect):
                img_viewer()
        elif p_rect.colliderect(game_rect):
            pygame.draw.rect(DISPLAY,WHITE,game_rect,5)
            if pg_rect.colliderect(game_rect):
                game()                             #call game
        elif p_rect.colliderect(key_rect):
            pygame.draw.rect(DISPLAY,WHITE,key_rect,5)
            if pg_rect.colliderect(key_rect):
                keyboard() 

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
            elif event.key==K_k:
                keyboard()
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

    font = pygame.font.Font('freesansbold.ttf', 25)
    menu=font.render("user" ,True,WHITE)
    menu_rect=menu.get_rect(centerx=WIDTH/2,centery=250)
    menu_rect.left=user_rect.left+10
    menu_rect.top=user_rect.bottom+5
    DISPLAY.blit(menu,menu_rect)
    DISPLAY.blit(user,user_rect)
    pygame.draw.rect(DISPLAY,WHITE,user_rect,3)

    if p_rect.colliderect(user_rect):
        pygame.draw.rect(DISPLAY,RED,user_rect,5)
        if pg_rect.colliderect(user_rect):
            Application()
    event_get()
    #DISPLAY.blit(menu,menu_rect)
    pygame.display.update()

    #pygame.draw.circle(DISPLAY, BLUE, (x,y), 20, 0)
    pygame.display.update()
    fpsClock.tick(FPS) 


    
 
