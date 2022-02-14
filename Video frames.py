cap=cv2.VideoCapture("sid concert.mpg")
ret, frame=cap.read()
while(1):
    ret, frame=cap.read()
    cv2.imshow("frame",frame)
    fps=cap.get(cv2.CAP_PROP_FPS)
    frame_count=(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    duration=frame_count/fps
    cv2.imwrite("Frames.jpg",duration)
    if(cv2.waitKey(1)& 0xFF==ord("q") or ret==False):
        cap.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow("frame",frame)
