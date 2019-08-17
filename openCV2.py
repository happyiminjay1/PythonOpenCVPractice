import cv2

cap = cv2.VideoCapture(0) #camera : 0 or file name
fourcc =cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output1.mp4',fourcc, 20.0, (1280,720))

while(cap.isOpened()) :
    ret, frame = cap.read() #ret : true, false # frame: source
    if ret == True :

        out.write(frame)
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
    else :
        break;

cap.release()
out.release()
cv2.destroyAllWindows()

print("Ended")


'''The list of available codes can be found in fourcc.org - http://www.fourcc.org/codecs.php

Gist of code I used in this video (Display the webcam in Python using OpenCV (cv2)) - http://www.codebind.com/python/opencv...

VideoCaptureProperties
https://docs.opencv.org/4.0.0/d4/d15/...'''
