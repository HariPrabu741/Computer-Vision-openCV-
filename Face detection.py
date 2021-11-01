import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # to load the classifier face
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')  # to load the classifier eye

# img = cv2.imread('9894620186.JPG')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(grey,1.1,4)

    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y), (x+w , y+h), (255,0,0),3)
        roi_grey=grey[y:y+h , x:x+w]
        roi_col=frame[y:y+h , x:x+w]
        eye = eye_cascade.detectMultiScale(roi_grey)

        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_col, (ex,ey), (ex+ew, ey+eh),(0,255,0), 5)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()