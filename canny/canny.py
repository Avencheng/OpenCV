import cv2
cap = cv2.VideoCapture('coin.jpg')
ret,frame = cap.read()
 
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (13,13),0)
edged = cv2.Canny(gray,5,10)
 
contours, hierarchy = cv2.findContours(
     edged,
     cv2.RETR_EXTERNAL,
     cv2.CHAIN_APPROX_SIMPLE)
 
cv2.drawContours(frame, contours,-1,(0,255,128),2)
 
cv2.imshow('frame',edged)
cv2.waitKey(0)
cv2.destroyAllWindows()
 