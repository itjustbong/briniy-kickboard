#include <ArduinoJson.h>

const int MOTOR_R_DIR = 4;
const int MOTOR_L_DIR = 2;
const int MOTOR_R_POW = 6;
const int MOTOR_L_POW = 5;

String str = "";

void setup() {
  Serial.begin(9600);
  
  pinMode(MOTOR_R_DIR, OUTPUT);         // Motor 1 방향설정
  pinMode(MOTOR_L_DIR, OUTPUT);         // Motor 2 방향설정
  
  while (!Serial) continue;while (!Serial) continue;
}

void go(int motorDir, int motorPow, int power, int dir){ 
  digitalWrite(motorDir, dir);
  analogWrite(motorPow, power);
}

void loop() {
  if(Serial.available()){
    str = Serial.readStringUntil("\n");
    DeserializationError error = deserializeJson(doc, str);

    if (error){
      Serial.print(F("deserializeJsondeserializeJson() failed : "));
      Serial.println(error.f_str());
      return;
    }
  }
  int rPow = doc["rPow"];
  int lPow = doc["lPow"];
  
  go(MOTOR_R_DIR, MOTOR_R_POW, 100, LOW);
  go(MOTOR_L_DIR, MOTOR_L_POW, 100, LOW);
  delay(500);

}
