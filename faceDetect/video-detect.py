
import cv2

cap=cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
side_cascade=cv2.CascadeClassifier('lpbcascade_profileface.xml')

if not cap.isOpened():
    raise IOError("Cannot find camera")

while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_flip=cv2.flip(frame,1)
    faces=face_cascade.detectMultiScale(gray,1.3,3)
    gray_flip = cv2.cvtColor(frame_flip, cv2.COLOR_BGR2GRAY)
    side=side_cascade.detectMultiScale(gray,1.3,3)
    side_flip=side_cascade.detectMultiScale(gray_flip,1.3,3)


    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)        #Frontal profile
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    
    for (x,y,w,h) in side:                  
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)        #Right profile
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    
    for (x,y,w,h) in side_flip:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)   #Left profile
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow('Camera input',frame)

    c=cv2.waitKey(1)
    if c==27:   #ESC key
        break

cap.release()
cv2.destroyAllWindows()
