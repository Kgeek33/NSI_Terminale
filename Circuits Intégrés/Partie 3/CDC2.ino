const int BROCHE_LED=2;
const int DELAI_MAX_MS=500;
const int DELAI_MIN_MS=10;
const int ACCELERATION=30;
int delai=DELAI_MAX_MS;
int sens=-1;


void setup() {
  // put your setup code here, to run once:
  pinMode(BROCHE_LED,OUTPUT);
}


void loop() {
  // put your main code here, to run repeatedly:

  delai=delai+sens*ACCELERATION;
  if (delai>DELAI_MAX_MS) {
    delai=DELAI_MAX_MS;
    sens=-sens;
  }
  if (delai<DELAI_MIN_MS) {
    delai=DELAI_MIN_MS;
    sens=-sens;
  }
  
  digitalWrite(BROCHE_LED,HIGH);
  delay(delai);
  digitalWrite(BROCHE_LED,LOW);
  delay(delai);
}
