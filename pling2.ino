int handle;
bool activate_pling = false;
void setup(){
  Serial.begin(9600);
}
void loop(){
  handle = analogRead(A0);
  if (handle < 200 && activate_pling == false){
    activate_pling = true;
    Serial.println(true);
    delay(10000);
    activate_pling = false;
  }
  delay(200);
  Serial.flush();
}

