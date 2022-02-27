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
    
    
#Face Detection
import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#read the image
img=cv2.imread("friends.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,3)

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w, y+h), (0,255,0), 3)

cv2.imshow("image",img)
cv2.waitkey()
