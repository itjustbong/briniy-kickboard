// 아두이노와 모터 드라이버 연결 포트 
const int MOTOR_R_DIR = 4;
const int MOTOR_L_DIR = 2;
const int MOTOR_R_POW = 6;
const int MOTOR_L_POW = 5;

// 아두이노와 압력센서 연결 포트 및 압력 센서의 저항에 따라 달라지는 변수 
const int FSRsensor = A0;
int preValue = 0;          

// 시리얼 통신을 통해서 받아올 속도 데이터 
char jetPower;

void setup() {
  //  시리얼 통신 및 핀모드 설정
  Serial.begin(9600);
  
  pinMode(MOTOR_R_DIR, OUTPUT);         // Motor 1 방향설정
  pinMode(MOTOR_L_DIR, OUTPUT);         // Motor 2 방향설정
  
}

// 앞으로 전진할 수 있도록 하는 제어 함수 
void go(int motorDir, int motorPow, int power, int dir){ 
  digitalWrite(motorDir, dir);
  analogWrite(motorPow, power);
}

void loop() {
  if(Serial.available()){
    jetPower = Serial.read();
    value = analogRead(FSRsensor);
  } 
  // 압력센서로부터 들어온 값이 1000 이상인 경우에만 작동
  // 그리고 젯슨에서 시리얼 통신을 통해서 들어온 값이 20 이상일 경우에만 작동 
  if( preValue > 1000 && jetPower > 20 ){
    // 젯슨의 시리얼 통신을 통해서 들어온 값을 제어 함수에 전
    go(MOTOR_R_DIR, MOTOR_R_POW, jetPower, HIGH);
    go(MOTOR_L_DIR, MOTOR_L_POW, jetPower, HIGH);
    delay(500);
  }
}
