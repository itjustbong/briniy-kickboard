
import jetson.inference
import jetson.utils

import serial
import time
import json



# msg = {'car_cnt' : 0, 'car_area' : [], 'person_cnt' : 0, 'person_area' : []}
pCount = 0

ser = serial.Serial(
    port = '/dev/ttyACM0',
    baudrate = 9600
)

dict_result = {}


# load the object detection network
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

# create video sources & outputs
input = jetson.utils.videoSource("/dev/video0") #/dev/video0
output = jetson.utils.videoOutput()

ser.write( str( 5 ).encode() )
# process frames until the user exits
while True:

    # capture the next image
    img = input.Capture()

    # detect objects in the image (with overlay)
    detections = net.Detect(img, overlay="box,labels,conf")

    for detection in detections:

        if detection.ClassID == 1:
            pCount += 1

        elif detection.ClassID == 3:
            pass

    
    # output.Render(img)

    # net.PrintProfilerTimes()

    print( "인식된 사람의 수 :: ", pCount )
    ser.write( str( 50 - pCount * 20 ).encode() )
    pCount = 0
    ser.write( str( 0 ).encode() )

    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break



