const int BROCHE_LED_ROUGE = 2;
const int BROCHE_POUSSOIR = 3;
const int PERIOD = 500;
bool fifi = false;

void setup()
{
    pinMode(BROCHE_POUSSOIR, INPUT);
    pinMode(BROCHE_LED_ROUGE, OUTPUT);
}

void clignotement()
{
    digitalWrite(BROCHE_LED_ROUGE, HIGH);
    delay(PERIOD);
    digitalWrite(BROCHE_LED_ROUGE, LOW);
    delay(PERIOD);
}

void loop()
{
    int bouton = digitalRead(BROCHE_POUSSOIR);
    if (bouton == HIGH)
    {
        fifi = !fifi;
    }

    if (fifi)
    {
        clignotement();
    }
    else
    {
        digitalWrite(BROCHE_LED_ROUGE, LOW);
    }
}