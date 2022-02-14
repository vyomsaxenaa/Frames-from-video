# Problem 1: No import packages

cap=cv2.VideoCapture("sid concert.mpg")
ret, frame=cap.read() # Problem 2: Dont need to read the video here
while(1): # why use while(1): trying to use boolean True as one?
    ret, frame=cap.read()
    cv2.imshow("frame",frame) # We dont need this. System will hang. Too many open windows.
    #Comment for each line; what and why you are doing.
    fps=cap.get(cv2.CAP_PROP_FPS)
    frame_count = (int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    duration=frame_count/fps
    cv2.imwrite("Frames.jpg",duration)
    if(cv2.waitKey(1)& 0xFF==ord("q") or ret==False):
        cap.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow("frame",frame)
