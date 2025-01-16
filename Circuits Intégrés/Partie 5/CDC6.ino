void setup()
{
    Serial.begin(9600);
}

void loop()
{
    int luminosite = analogRead(A0);
    Serial.println(luminosite);
    delay(500);
}