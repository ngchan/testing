#include "DHT.h"
#include <SoftwareSerial.h>

#define DHTPIN 9
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

SoftwareSerial bluetooth(2,3);

void setup() {
  Serial.begin(9600);
  bluetooth.begin(9600);

  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1500);

  float h = dht.readHumidity();

  if (isnan(h)) return;

  Serial.println(h);
  bluetooth.println(h);
}
