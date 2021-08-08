import serial
import time
import json
 
msg = {'lPow' : 0, 'rPow' : 0}
port = '/dev/ttyUSB0' # 시리얼 포트
baud = 9600 # 시리얼 보드레이트(통신속도)
 
ser = serial.Serial(port,baud)
 
end_str = '\n'
 
while True:
    # 모터 출력값 설정
    msg['lPow'] = input() 
    msg['rPow'] = input() 

    json_msg = json.dumps(msg)
    ser.write(json_msg.encode())
    ser.write(end_str.encode())