import cv2
import os
path="C:/Users/Sid/Desktop/Vyom's Python/Video Sample/"
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#read  video frame
def video_read(file):
    cap=cv2.VideoCapture(file)
    ret,frame=cap.read()
    return frame

def coordinates(frame):
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,3)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
    return faces

def frame_specific_time(sec,frame):
    fps=cap.get(cv2.CAP_PROP_FPS)
    time=fps*sec
    count=0
    if count%time==0:
        cv2.imwrite("frame%d.jpg"%count,frame)
    count+=1
    return frame

for file in os.listdir(path):
    if file.endswith(".mp4"):
        loc=os.path.join(path,file)
        video_read(loc)


   
    

    
