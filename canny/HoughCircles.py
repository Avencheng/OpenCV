import cv2

src = cv2.imread('coin.jpg',-1)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0) #高斯模糊(5X5為正方形)
cv2.imshow('gray',gray)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1,20,None,10,80,5,75)
print(circles)

if circles is not None:
    circles = circles.astype(int)
    out = src.copy()
    for x,y, r in circles[0]:
        #draw circle
        cv2.circle(out,(x,y),r,(0,0,255),3,cv2.LINE_AA)
        #draw center of circle
        cv2.circle(out,(x,y),2,(0,255,0),3,cv2.LINE_AA)
    src = cv2.hconcat([src,out])

cv2.imshow('image', src)
cv2.waitKey(0)
cv2.destroyAllWindows()