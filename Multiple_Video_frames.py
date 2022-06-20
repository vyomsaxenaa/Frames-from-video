import cv2
import os
#To read the Video
path="C:/Users/Sid/Desktop/Vyom's Python/Video Sample/"
for file in os.listdir(path):
  if file.endswith(".mp4"):
    path=os.path.join(path,file)
cap=cv2.VideoCapture(file) 
ret, frame=cap.read()
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cv2.imshow("Frame",frame)       
count=0
while(True):
   #To read the frames
    ret, frame=cap.read()
    print("read a new frame:",frame)
    img=cap.read()
    """ Face Detectiion"""
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,3)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 3)
    # To capture frame at specific time
    fps=cap.get(cv2.CAP_PROP_FPS)
    time=fps*30
    if(count%time==0):
    #if(faces):
        cv2.imwrite("frame%d.jpg"%count,frame)
    count+=1
    # To stop the Iteration 
    if(cv2.waitKey(1)& 0xFF==ord("q") or ret==False):
        cap.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow("Frame",frame)
cap.release()

