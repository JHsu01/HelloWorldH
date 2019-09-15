    # Purdue Hello World Project 2019

    # Team "BGR > RGB"

    # Version 2019-09-14

    # Authors: Kanti Bharat, Joseph Hsu, Bram Lovelace, James Yin, & Andy Yoo

    # Made with <3 and Kedar OwO 

    # ACTUAL CODE/COMMENTS STARTS HERE



    # + Code below imports math stuff, open cv, and the ability to wait. A lot of waiting.
import numpy as np
import cv2
import time


def myFunction():
    e=open("output.txt", "w").close()

    # Starts Video Recording, and sets "counters"

    cap = cv2.VideoCapture(0)
    prevColorGuess = 'null'
    countColor = 0
    capturin = False
    isCorrect = 'n'

    # Main Loop
    while(True):

        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #lower_blue = np.array([110,50,50])
        #upper_blue = np.array([130,255,255])

        #mask = cv2.inRange(hsv, lower_blue, upper_blue)
        #res = cv2.bitwise_and(frame, frame, mask= mask)

        #draw box
        cv2.line(frame,(295,225),(325,225),(255,255,255),2)
        cv2.line(frame,(295,255),(325,255),(255,255,255),2)
        cv2.line(frame,(295,225),(295,255),(255,255,255),2)
        cv2.line(frame,(325,225),(325,255),(255,255,255),2)

        #rgb analysis of grey, black, whit
        
        redSum = 0
        greenSum = 0
        blueSum = 0
        hueSum = 0
        valSum = 0
        for x in range(295,326):
            for y in range(225,256):
                redSum+=frame[x,y][2]
                greenSum+=frame[x,y][1]
                blueSum+=frame[x,y][2]
                hueSum+=hsv[x,y][0]
                valSum+=hsv[x,y][2]
        redAvg = redSum/900
        greenAvg = greenSum/900
        blueAvg = blueSum/900
        hueAvg = hueSum/900
        valAvg = valSum/900


       # blue = frame[310,240][0]
       # green = frame[310,240][1]
       # red = frame[310,240][2]
        maxColor = max(redAvg, blueAvg, greenAvg)
        minColor = min(redAvg, blueAvg, greenAvg)
        isGrey  = maxColor-minColor<12

        if isGrey:    
           # print('greyscale') 
            if valAvg<100:
                colorGuess = 'black'
            elif valAvg>150:
                colorGuess = 'white'
            else:
                colorGuess = 'grey'
            print('greyscale %i guess %s'%(valAvg, colorGuess))
       
        else:
           # print('red: %i blue: %i green: %i'%(red,blue,green))






        #480x620 - 240,310 is center
        #px = frame[310,240]
        #print(px)

        
        #    hueSum = 0
           # for x in range(295,326):
           #     for y in range(225,256):
           #         hueSum+=hsv[x,y][0]

         #   hueAvg = hueSum/900

        
        #pxhsv = hsv[310,240]
        #hvalue = int(pxhsv[0])
         
     




        #make a guess as to the color - simple
            hue = hueAvg#pxhsv[0]
           # colorGuess = 'other'
            if hue<120 and hue>100:
                colorGuess = 'blue'
            elif hue<100 and hue>30:
                colorGuess = 'green'
            elif hue<10 or hue >165:
                colorGuess = 'red'
            elif hue<25 and hue>10:
                colorGuess = 'yellow'

    #   output guess for color along with debug of raw h value

       # if isGrey:
        #    print('greyscale')
       # else:
            print('avg hue: %i color guess: %s' % (hueAvg, colorGuess))

    #counting if its the same as other ones before it
        if cv2.waitKey(1) & 0xFF == ord(' '):
            capturin = True 
        if capturin:
            print('capturing')
            if prevColorGuess == colorGuess:
                countColor+=1
            else:
                countColor=0
            prevColorGuess = colorGuess
            if countColor>15:
                print(colorGuess)
                time.sleep(.5)
                countColor = 0
                break
                """print('is this correct? ')
                isCorrect = raw_input('y/n ')
                #print(isCorrect)
                if isCorrect == 'y':
                    f=open("output.txt", "w")
                    f.write("trigger \r\n")
                    f.write(colorGuess)
                    f.close()
                    break
                else:
                    capturin = False"""
		
       # time.sleep(.05)


        # Display the resulting frame
        cv2.imshow('frame',frame)
       # cv2.imshow('mask',mask)
       # cv2.imshow('res',res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return colorGuess

