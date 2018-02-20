#define BTN 4
int btn;
int prevBtn;
void setup(){
  pinMode(BTN, INPUT);
  // start value based on current switch position
  prevBtn = digitalRead(BTN);
  Serial.begin(9600);
}
void loop(){
  btn = digitalRead(BTN);
  if (btn != prevBtn){
    prevBtn = btn;
    Serial.println(true);
    delay(25000); // the duration of DAS-DASS
  }
  delay(300);
  Serial.flush();
}
