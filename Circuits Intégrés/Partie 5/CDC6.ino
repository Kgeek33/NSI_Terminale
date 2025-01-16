const int BROCHE_LED = 2;
const int BROCHE_BP = 3;      // Bouton Poussoir
const int DELAI_MAX_MS = 500; // clignotement lent
const int DELAI_MIN_MS = 10;  // clignotement rapide
const int PAS = 30;
int delai = DELAI_MAX_MS;
int sens = -1;
int etatBP;

void setup()
{
    Serial.begin(9600);
    pinMode(BROCHE_LED, OUTPUT);
    pinMode(BROCHE_BP, INPUT);
}

void clignote(int del)
{
    digitalWrite(BROCHE_LED, HIGH);
    delay(del);
    digitalWrite(BROCHE_LED, LOW);
    delay(del);
}
<
void loop()
{
    int luminosite = analogRead(A0);
    Serial.println(luminosite);
    if (luminosite < 100)
    {

        clignote(delai);
    }

    delay(500);
}