#include "DHT.h"

#define DHTPIN 15      // DHT22 Data pin
#define DHTTYPE DHT22
#define MQ2_PIN 34     // MQ-2 A0 pin
#define LED_PIN 2      // LED pin
#define BUZZER_PIN 5   // Buzzer pin

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  Serial.println("Smart Home Safety System Started!");
}

void loop() {
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  int gasValue = analogRead(MQ2_PIN);

  Serial.print("Temp: ");
  Serial.print(temp);
  Serial.print(" C | Humidity: ");
  Serial.print(hum);
  Serial.print(" % | Gas: ");
  Serial.println(gasValue);

  // Gas leak illa Fire vandha Alarm adikkum!
  if (gasValue > 1500 || temp > 45) {
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, HIGH);
    Serial.println("!!! DANGER - GAS / FIRE DETECTED !!!");
  } else {
    digitalWrite(LED_PIN, LOW);
    digitalWrite(BUZZER_PIN, LOW);
    Serial.println("Safe - All Normal");
  }
  Serial.println("--------------------");
  delay(2000);
}
