const int BROCHE_LED_ROUGE = 2;
const int BROCHE_POUSSOIR = 3;
const int PERIOD = 500;

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
    const int bouton = digitalRead(BROCHE_POUSSOIR);
    const int etatCligno = digitalRead(BROCHE_LED_ROUGE);
    switch (etatCligno)
    {
    case 1:
        if (bouton == 1) digitalWrite(BROCHE_LED_ROUGE, ON);
        break;
    case 2:
        if (bouton == 1) digitalWrite(BROCHE_LED_ROUGE, CHANGE_TO_OFF);
        break;
    case 3:
        if (bouton == 1) digitalWrite(BROCHE_LED_ROUGE, OFF);
        break;
    default:
        digitalWrite(BROCHE_LED_ROUGE, CHANGE_TO_ON);
        break;
    }
}