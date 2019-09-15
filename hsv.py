import numpy as np
import cv2

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

    #draw crosshairs
    cv2.line(frame,(295,240),(325,240),(255,255,255),2)
    cv2.line(frame,(310,225),(310,255),(255,255,255),2)


    #480x620 - 240,310 is center
    px = frame[310,240]
    #print(px)
    pxhsv = hsv[310,240]
    #hvalue = int(pxhsv[0])
   
    #ranges for colors
    #blue 110-130
    #red 170-180, 0-10
    #green 50-70

    #make a guess as to the color - simple
    hue = pxhsv[0]
    colorGuess = 'other'
    if hue<135 and hue>105:
        colorGuess = 'blue'
    elif hue<75 and hue>45:
        colorGuess = 'green'
    elif hue<10 or hue >165:
        colorGuess = 'red'
    

   #output guess for color along with debug of raw h value
    #print(type(value))
    #print('h: %i s: %i v: %i' % (pxhsv[0], pxhsv[1], pxhsv[2]))
    print('hue value: %i color guess: %s' % (pxhsv[0], colorGuess))



    # Display the resulting frame
    cv2.imshow('frame',frame)
   # cv2.imshow('mask',mask)
   # cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
