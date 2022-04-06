import cv2
import frames_func as fn

frame=fn.video_read("sid concert.mpg")
cv2.imshow("Frame",frame)
print(frame)

face_detect=fn.coordinates(frame)
fps=cap.get(cv2.CAP_PROP_FPS)
time=fps*5
