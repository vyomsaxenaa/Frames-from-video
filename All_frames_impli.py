import cv2
import os
import frames_func as fn
#path="C:/Users/Sid/Desktop/Vyom's Python/Video Sample/"
#for file in os.listdir(path):
 #   if file.endswith(".mp4"):
  #      loc=os.path.join(path,file)
   #     video_read(loc)
#frame=fn.video_read("sid concert.mpg")
frame=fn.video_read(file)
cv2.imshow("Frame",frame)
print(frame)

face_detect=fn.coordinates(frame)
specific_time=fn.frame_specific_time(5,frame)

