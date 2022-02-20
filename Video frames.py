import cv2
cap=cv2.VideoCapture("sid concert.mpg")
count=0
while(True):
    #To read the frames
    ret, frame=cap.read()
    print("read a new frame:",frame)
    # To capture frame at specific time
    fps=cap.get(cv2.CAP_PROP_FPS)
    time=fps*5
    if(count%time==0):
        cv2.imwrite("frame%d.jpg"%count,frame)
    count+=1
    # To stop the Iteration 
    if(cv2.waitKey(1)& 0xFF==ord("q") or ret==False):
        cap.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow("frame",frame)

