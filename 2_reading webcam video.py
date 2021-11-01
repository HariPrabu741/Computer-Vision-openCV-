import cv2

capture = cv2.VideoCapture(0)  # used to capture video...  0 is for camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(capture.isOpened()):     # if camera not opened... while loop won't execute
    ret,frame = capture.read() # ret takes the bool(true or false)
    if ret == True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==ord('q'):
            break

capture.release()               # Allways use release function after capture
out.release()
cv2.destroyAllWindows()