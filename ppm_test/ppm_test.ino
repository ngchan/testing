/**
 * PPM READER
 * -Author: Nicholas Chan
 * -Date:   May 12th 2019
 * 
 * Reads PPM signal from RC Receiver, variable number of channels
 * Outputs in the ch array, 0th element is not used
 * ch[i] -> i = 1; channel 1
 *          i = 2; channel 2
 *          i = 3; channel 3...
 */

//Number of useful channels
#define NUM_CHANNEL 8

//Variables for time tracking
unsigned long time_now, last_time, ch[NUM_CHANNEL+1], delta;
int count = 0;

/*
 * Setup interrupts and serial
 * Uses RISING interrupt because PPM depends on time between pulses
 * FALLING also works
 */
void setup() {
  attachInterrupt(digitalPinToInterrupt(2), read_ppm, FALLING);
  Serial.begin(115200); //Works better with higher baud rates (interrupts can mess with serial)
  last_time = micros(); //Initialize timer
}

/*
 * Prints out channel data every 100ms
 */
void loop() {
  for(int i = 0; i < NUM_CHANNEL+1; i++) {
    Serial.print(ch[i]);
    Serial.print('\t');
  }
  Serial.println();
  delay(100);
}

/*
 * ISR for reading PPM recevier
 */
void read_ppm(){
  time_now = micros();
  delta = time_now - last_time;
  if(delta > 4000){
    count = 0;
  }
  else{
    count++;
  }
  ch[count] = delta;
  last_time = time_now;
}
