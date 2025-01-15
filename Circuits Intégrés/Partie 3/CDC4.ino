const int BROCHE_LED_ROUGE = 2;
const int BROCHE_POUSSOIR = 3;
const int PERIOD = 100;

const int OFF = 0;
const int CHANGE_TO_ON = 1;
const int ON = 2;
const int CHANGE_TO_OFF = 3;

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
    int etatCligno = digitalRead(BROCHE_LED_ROUGE);
    switch (etatCligno)
    {
    case CHANGE_TO_ON:
        if (bouton == LOW)
            etatCligno = ON;
        break;
    case ON:
        if (bouton == HIGH)
            etatCligno = CHANGE_TO_OFF;
        break;
    case CHANGE_TO_OFF:
        if (bouton == LOW)
            etatCligno = OFF;
        break;
    default:
        if (bouton == HIGH)
            etatCligno = CHANGE_TO_ON;
        break;
    }

    if (etatCligno == ON)
        clignotement();

    digitalWrite(BROCHE_LED_ROUGE, etatCligno);
}