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
    Serial.println(true);
    Serial.flush();
    // wait for whatever song to finish
    delay(30000);
  }
  // the button change happens in the 200ms delay
  prevBtn = digitalRead(BTN);
  delay(200);
}
