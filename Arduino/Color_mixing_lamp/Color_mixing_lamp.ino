const int RedLEDpin = 9;
const int BlueLEDpin = 10;
const int GreenLEDpin = 11;
const int RedSensorpin = A0;
const int BlueSensorpin = A1;
int RedValue = 0;
int BlueValue = 0; 
int GreenValue = 0;
int RedSensorValue = 0;
int BlueSensorValue = 0;
int GreenSensorValue = 0;
void setup() {
  Serial.begin(9600);
  pinMode(RedLEDpin,OUTPUT);
  pinMode(BlueLEDpin,OUTPUT);
  pinMode(GreenLEDpin,OUTPUT);
}
void loop() {
RedSensorValue = analogRead(RedSensorpin);
delay(5);
BlueSensorValue = analogRead(BlueSensorpin);
delay(5);
GreenSensorValue = RedSensorValue + BlueSensorValue;
Serial.print("Raw Sensor Values \t Red: ");
Serial.print(RedSensorValue);
Serial.print("\t Blue: ");
Serial.print(GreenSensorValue);
Serial.print("\t Green: ");
Serial.println(BlueSensorValue);
RedValue = RedSensorValue/4;
BlueValue = BlueSensorValue/4;
GreenValue = GreenSensorValue/4;
Serial.print("Mapped Sensor Values \t Red: ");
Serial.print(RedValue);
Serial.print("\t Blue: ");
Serial.print(BlueValue);
Serial.print("\t Green: ");
Serial.println(GreenValue);
analogWrite(RedLEDpin, RedValue);
analogWrite(BlueLEDpin, BlueValue);
analogWrite(GreenLEDpin, GreenValue);
}