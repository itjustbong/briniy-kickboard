import jetson.inference
import jetson.utils

import serial
import time
import json


# 혼잡도 계산을 위해 아두이노로 전송할 message (차 개수, 보이는 차의 면적, 사람 수, 보이는 사람의 면적)
msg = {'car_cnt' : 0, 'car_area' : [], 'person_cnt' : 0, 'person_area' : []}

ser = serial.Serial( # 시리얼 통신 설정
    port = '/dev/ttyACM0',
    baudrate = 9600
)

# load the object detection network
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

# 영상의 sources & outputs 생성
input = jetson.utils.videoSource("/dev/video0")
output = jetson.utils.videoOutput()

ser.write(str( 5 ).encode()) # 시리얼 통신

while True:
    img = input.Capture()

    # 감지된 objects를 리턴
    detections = net.Detect(img, overlay="box,labels,conf")

    # 감지된 objects 결과를 아두이노로 전송할 message로 저장
    for detection in detections:
        if detection.ClassID == 1: # Person ClassID = 1
            msg[car_cnt] += 1
            msg[car_area].append(detection.Area)
        elif detection.ClassID == 3: # Car ClassID = 3
            msg[person_cnt] += 1
            msg[person_area].append(detection.Area)

    print( "인식된 사람의 수 :: ", msg[person_cnt] )
    
    # 시연 예시)
    # 속도 제어 : 50 - 사람 수 * 20
    ser.write(str( 50 - msg[person_cnt] * 20 ).encode()) # 시리얼 통신

    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break
