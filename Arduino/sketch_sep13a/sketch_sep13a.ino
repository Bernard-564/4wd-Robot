const int buttonPin = 2;
const int ledPins[] = {4, 5, 6};

void setup() {
  pinMode(buttonPin, INPUT);
  for (int i = 0; i < 3; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  if (digitalRead(buttonPin) == HIGH) {
    // Blink LEDs when button is pressed
    for (int i = 0; i < 3; i++) {
      digitalWrite(ledPins[i], HIGH);
    }
    delay(0.2);
    for (int i = 0; i < 3; i++) {
      digitalWrite(ledPins[i], LOW);
    }
    delay(1000);
  } else {
    // Turn off LEDs when button is not pressed
    for (int i = 0; i < 3; i++) {
      digitalWrite(ledPins[i], LOW);
    }
  }
}
