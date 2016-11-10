import cv2

kernel=np.ones((5,5),dtype=np.uint8)
''' transform ---------------------------------------'''
pt1=np.float32([[0,0],[640/2,480/2],[640,0]])
pt2=np.float32([[640,0],[640/2,480/2],[0,0]])
M=cv2.getAffineTransform(pt1,pt2)

lb=np.array([110,60,60])
ub=np.array([130,255,255])

lg=np.array([40,70,70])
ug=np.array([80,255,255])
def position(im):
    im=cv2.imread('cam_img.jpg')
    im=cv2.warpAffine(im,M,(640,480))
    hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)

    erosion=cv2.erode(mask,kernel,iterations=1)
    
    
    
