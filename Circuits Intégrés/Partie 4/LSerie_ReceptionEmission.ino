void setup()
{
    Serial.begin(9600);
}

void loop()
{
    if (Serial.available() > 0)
    {
        int num = Serial.parseInt();
        Serial.print("j'ai recu :");
        Serial.println(num);
    }
}