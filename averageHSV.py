import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask= mask)

    #draw box
    cv2.line(frame,(295,225),(325,225),(255,255,255),2)
    cv2.line(frame,(295,255),(325,255),(255,255,255),2)
    cv2.line(frame,(295,225),(295,255),(255,255,255),2)
    cv2.line(frame,(325,225),(325,255),(255,255,255),2)

    #480x620 - 240,310 is center
    #px = frame[310,240]
    #print(px)
    hueSum = 0
    for x in range(295,326):
        for y in range(225,256):
            hueSum+=hsv[x,y][0]

    hueAvg = hueSum/900


    pxhsv = hsv[310,240]
    #hvalue = int(pxhsv[0])
  
 




    #make a guess as to the color - simple
    hue = hueAvg#pxhsv[0]
    colorGuess = 'other'
    if hue<120 and hue>100:
        colorGuess = 'blue'
    elif hue<100 and hue>30:
        colorGuess = 'green'
    elif hue<10 or hue >165:
        colorGuess = 'red'
    elif hue<25 and hue>10:
        colorGuess = 'yellow'

#   output guess for color along with debug of raw h value
    #print(type(value))
    #print('h: %i s: %i v: %i' % (pxhsv[0], pxhsv[1], pxhsv[2]))
    print('avg hue: %i color guess: %s' % (hueAvg, colorGuess))



    # Display the resulting frame
    cv2.imshow('frame',frame)
   # cv2.imshow('mask',mask)
   # cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
