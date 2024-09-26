void setup() {
  Serial.begin(115200);
}

void loop() {
}

void serialEvent() {
  while (Serial.available()) {
    int inChar = (int)Serial.read(); 

    Serial.print(inChar);
    Serial.print(" ");
  }
}
