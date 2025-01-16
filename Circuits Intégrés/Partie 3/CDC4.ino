const int BROCHE_LED = 2;
const int BROCHE_BP = 3;    // Bouton Poussoir
const int DELAI_MAX_MS = 500;  // clignotement lent
const int DELAI_MIN_MS = 10;  // clignotement rapide
const int PAS = 30;
int delai = DELAI_MAX_MS;
int sens = -1;
int etatBP;                 // etat du Bouton Poussoir
// les etats possibles du clignotement
const int CLIGNO_ON = 0;
const int CLIGNO_CHANGE_TO_OFF = 1;
const int CLIGNO_OFF = 2;
const int CLIGNO_CHANGE_TO_ON = 3;
// gestion du clignotement : le bouton provoque les transitions entre les quatre états
int etatCligno = CLIGNO_OFF;


void setup() {
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

  // etat du clignotement en fonction de l'état du bouton
  // *selon* etatCligno ...
  switch (etatCligno) {
    // dans le cas d'un clignotement en cours ...
    case CLIGNO_ON:
      if (etatBP == HIGH) {
        etatCligno = CLIGNO_CHANGE_TO_OFF;
      }
      break;
    // dans le cas d'une transition vers l'extinction de la led ...
    case CLIGNO_CHANGE_TO_OFF:
      if (etatBP == LOW) {
        etatCligno = CLIGNO_OFF;
      }
      break;
    // dans le cas d'une led éteinte...
    case CLIGNO_OFF:
      if (etatBP == HIGH) {
        etatCligno = CLIGNO_CHANGE_TO_ON;
      }
      break;
    // dans le cas d'une transition vers le clignotement de la led ...
    case CLIGNO_CHANGE_TO_ON:
      if (etatBP == LOW) {
        etatCligno = CLIGNO_ON;
      }
      break;
    default :
      break;

  }
  if (etatCligno == CLIGNO_ON) {
    clignote (delai);
  }
}
