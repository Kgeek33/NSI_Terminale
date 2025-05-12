const int BROCHE_LED=2;
const int PERIODE_MS=500;

void setup() {
  // put your setup code here, to run once:
  pinMode(BROCHE_LED,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(BROCHE_LED,HIGH);
  delay(PERIODE_MS);
  digitalWrite(BROCHE_LED,LOW);
  delay(PERIODE_MS);
}  
