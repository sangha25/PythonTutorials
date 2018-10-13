import cv2

#for accessing The Webcam we use Video Capture Function.
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()#return value through cap.
    cv2.imshow("The Canera is Opened", frame)
    # ascii code For Enter is 13.
    if cv2.waitKey(1)==13:
        break

#camera will Realeased or closed.
cap.release()
#all windows opened by CV2 lib will be destroyed.
cv2.destroyAllWindows()