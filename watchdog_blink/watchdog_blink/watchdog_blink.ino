/**
 * File: watchdog_blink
 * Author: Nicholas Chan
 * Date: 4th May 2018
 * 
 * Use watchdog timer to reset Arduino after set interval
 */

//Include header file for watchdog
#include <avr/wdt.h>

void setup() {
  //Setup watchdog
  cli();
  wdt_reset();
  WDTCSR |= (1<<WDCE)|(1<<WDE);
  WDTCSR  = (1<<WDE) |(1<<WDP3)|(0<<WDP2)|(0<<WDP1)|(0<<WDP0);
  sei();
  wdt_reset();
  //Blink LED once
  DDRB   = B00100000;   //Pin 13 to output
  PORTB = B00100000;    //Pin 13 to high
  delay(500);
  PORTB = B00000000;    //Pin 13 to low
}

void loop() {
  ;
}
