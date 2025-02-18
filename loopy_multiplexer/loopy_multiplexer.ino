#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_APDS9960.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <assert.h>

#define PCAADDR0 0x70
#define NUM_MUXES 5
#define SENSORS_PER_MUX 8

#define DEV_I2C Wire
#define SerialPort Serial

Adafruit_APDS9960 apds_2d[NUM_MUXES][SENSORS_PER_MUX];

void pcaselect(uint8_t m,uint8_t i) {
  if (i > 7 || m > 7) return;
  for(int j = 0;j < 8; j++){
    Wire.beginTransmission(PCAADDR0+j);
    Wire.write(0);
    Wire.endTransmission();
  }
  
  Wire.beginTransmission(PCAADDR0 + m);
  Wire.write(1 << i);
  Wire.endTransmission();  
}

void setup() {
    while (!Serial);
    delay(1000);
    Wire.begin();
    
    Serial.begin(57600);

    for (int m = 0; m < NUM_MUXES; ++m) {
        for (int i = 0; i < SENSORS_PER_MUX; ++i) {
            if (!(i == 3 && m != 0)){
                pcaselect(m, i);
                if (!apds_2d[m][i].begin()) {

                } else {

                    apds_2d[m][i].enableColor(true);
                    
          
                }
            }
        }
    }
}

//uint16_t r[NUM_MUXES][SENSORS_PER_MUX], g[NUM_MUXES][SENSORS_PER_MUX], b[NUM_MUXES][SENSORS_PER_MUX], c[NUM_MUXES][SENSORS_PER_MUX];

uint16_t r, g,b,c;

void loop() {
    Serial.println("start");
    for (int m = 0; m < NUM_MUXES; ++m) {
        for (int i = 0; i < SENSORS_PER_MUX; ++i) {
            if (!(i == 3 && m != 0)){
                pcaselect(m, i);
                while(!apds_2d[m][i].colorDataReady()) {
                    delay(5);
                }
                apds_2d[m][i].getColorData(&r, &g, &b, &c);
                

                Serial.println(r);

                Serial.println(g);

                Serial.println(b);

                Serial.println(c);
            }
        }
    }

    delay(50);
}
