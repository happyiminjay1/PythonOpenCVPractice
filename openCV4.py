import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,2560)
cap.set(4,1440)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()) :
    ret, frame = cap.read()
    if ret == True:

        gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    else :
        break

cap.release()
cv2.destroyAllWindows()
