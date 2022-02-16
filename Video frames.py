import cv2
#To read the Video
cap=cv2.VideoCapture("sid concert.mpg")
ret, frame=cap.read()
count=0
while(True):
    #To read the frames
    ret, frame=cap.read()
    print("read a new frame:",frame)
    # To capture frame at specific time
    if(count%30==0):
        cv2.imwrite("frame%d.jpg"%count,frame)
    count+=1
    # To stop the Iteration 
    if(cv2.waitKey(1)& 0xFF==ord("q") or ret==False):
        cap.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow("frame",frame)

