#import neccessary modules

import cv2
import time

lmt=int(input("Enter Max Vehicle Count: "))

#Read video from a video file or CCTV or Your webcam
cap = cv2.VideoCapture("video.avi")
#load the classifier
car_cascade = cv2.CascadeClassifier("cars.xml")

#loop through each frame counting number of vehicles in each
while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    #convert tyhe video to gray scale for easier processing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #introduc detector inorder to detect vehicles
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    time.sleep(0.5)
    print(f"There are {len(cars)} On Road A")
    count=len(cars)
   #draw rectagle on each detected vehicle
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      
    cv2.imshow('video', img)
    #check to se if the vehicles in frame have exceded the set limit by user
    if(int(count)>lmt):
        print("Number Of vehicles have excedded the max Limit\n\n\n\n!!!! WARNING JAM IMMINENT !!!!\n\n\n\n")
        time.sleep(4)

    #The program waits for the user to press the esc key
    if cv2.waitKey(20) == 27:
        break
#kill the programm when done
cv2.destroyAllWindows()