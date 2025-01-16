const int BROCHE_LED = 2;
const int BROCHE_BP = 3;    // Bouton Poussoir
const int DELAI_MAX_MS = 500;  // clignotement lent
const int DELAI_MIN_MS = 10;  // clignotement rapide
const int PAS = 30;
int delai = DELAI_MAX_MS;
int sens = -1;
int etatBP;                 // etat du Bouton Poussoir


void setup() {
  // put your setup code here, to run once:
  pinMode(BROCHE_LED, OUTPUT);
  pinMode(BROCHE_BP, INPUT);
}

void clignote (int del) {
  digitalWrite(BROCHE_LED, HIGH);
  delay(del);
  digitalWrite(BROCHE_LED, LOW);
  delay(del);
}

void loop() {

  // lecture du bouton poussoir
  etatBP = digitalRead(BROCHE_BP);
  delai = delai + sens * PAS;
  if (delai > DELAI_MAX_MS) {
    delai = DELAI_MAX_MS;
    sens = -sens;
  }
  if (delai < DELAI_MIN_MS) {
    delai = DELAI_MIN_MS;
    sens = -sens;
  }

  if (etatBP == HIGH) {
    clignote(delai);
  } 
}
