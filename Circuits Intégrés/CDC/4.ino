const int BROCHE_LED_ROUGE = 2;
const int BROCHE_POUSSOIR = 3;
const int PERIOD = 500;
bool statutBouton = false;

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
    const int etatCligno = digitalRead(BROCHE_LED_ROUGE);

    if (bouton == 1)
    {
        statutBouton = !statutBouton;
    }

    if (statutBouton)
    {
        clignotement();
    }
    else
    {
        switch (etatCligno)
        {
        case ON:
            digitalWrite(BROCHE_LED_ROUGE, HIGH);
            break;
        default:
            digitalWrite(BROCHE_LED_ROUGE, LOW);
            break;
        }
    }
}