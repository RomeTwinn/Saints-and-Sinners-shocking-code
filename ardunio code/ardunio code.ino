#define shock_button 7
int shocking_pause = 200;

void setup() {
  Serial.begin(9600);
  pinMode(shock_button, OUTPUT);
  digitalWrite(shock_button, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    String shock = Serial.readString();
    if(shock == "s") {
      digitalWrite(shock_button, HIGH);
      delay(shocking_pause);
      digitalWrite(shock_button, LOW);
      delay(shocking_pause);

      digitalWrite(shock_button, HIGH);
      delay(shocking_pause);
      digitalWrite(shock_button, LOW);
      delay(shocking_pause);

      digitalWrite(shock_button, HIGH);
      delay(shocking_pause);
      digitalWrite(shock_button, LOW);
      delay(shocking_pause);

      digitalWrite(shock_button, HIGH);
      delay(shocking_pause);
      digitalWrite(shock_button, LOW);
      delay(shocking_pause);
    }
  }
}
