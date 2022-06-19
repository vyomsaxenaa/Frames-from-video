import cv2
import os
import frames_func as fn

frame=fn.video_read(file)
cv2.imshow("Frame",frame)
print(frame)

face_detect=fn.coordinates(frame)
specific_time=fn.frame_specific_time(5,frame)

