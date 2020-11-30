#define MAX 180
#define MIN 0
#define MIN_DUTY 306
#define MAX_DUTY 1194

#define OFFSET 55
#define UP 0
#define DOWN 90
#define FRONT MIN + OFFSET
#define BACK MAX - OFFSET

#define DELAY 2500

void setup() {
  Serial.begin(2400);
  delay(5000);
  turnLeft(2);
  delay(DELAY);
  reset();
}

void loop() {
    

}

void reset() {
  moveLegWalkingGroup0(90);
  moveLegWalkingGroup1(90);
  moveKneeWalkingGroup0(DOWN);
  moveKneeWalkingGroup1(DOWN);
}

void turnLeft(uint8_t steps) {
  for (uint8_t i = 0; i < steps; i++) {
    moveKnee(0, UP);
    moveKnee(2, UP);
    moveKnee(4, UP);
    delay(DELAY);
    moveLeg(0, BACK);
    moveLeg(2, BACK);
    moveLeg(4, FRONT);
    delay(DELAY);
    moveKnee(0, DOWN);
    moveKnee(2, DOWN);
    moveKnee(4, DOWN);
    delay(DELAY);
    moveKnee(1, UP);
    moveKnee(3, UP);
    moveKnee(5, UP);
    delay(DELAY);
    moveLeg(0, FRONT);
    moveLeg(2, FRONT);
    moveLeg(4, BACK);
    moveLeg(1, BACK);
    moveLeg(3, FRONT);
    moveLeg(5, FRONT);
    delay(DELAY);
    moveKnee(1, DOWN);
    moveKnee(3, DOWN);
    moveKnee(5, DOWN);
    delay(DELAY);
  }
}

void turnRight(uint8_t steps) {
  for (uint8_t i = 0; i < steps; i++) {
    moveKnee(0, UP);
    moveKnee(2, UP);
    moveKnee(4, UP);
    delay(DELAY);
    moveLeg(0, FRONT);
    moveLeg(2, FRONT);
    moveLeg(4, BACK);
    delay(DELAY);
    moveKnee(0, DOWN);
    moveKnee(2, DOWN);
    moveKnee(4, DOWN);
    delay(DELAY);
    moveKnee(1, UP);
    moveKnee(3, UP);
    moveKnee(5, UP);
    delay(DELAY);
    moveLeg(0, BACK);
    moveLeg(2, BACK);
    moveLeg(4, FRONT);
    moveLeg(1, FRONT);
    moveLeg(3, BACK);
    moveLeg(5, BACK);
    delay(DELAY);
    moveKnee(1, DOWN);
    moveKnee(3, DOWN);
    moveKnee(5, DOWN);
    delay(DELAY);
  }
}


void backwards(uint8_t steps) {
  for (uint8_t i = 0; steps > i; i++) {
    moveKneeWalkingGroup0(UP);
    moveLegWalkingGroup0(BACK);
    delay(DELAY);
    moveKneeWalkingGroup0(DOWN);
    delay(DELAY);
    moveKneeWalkingGroup1(UP);
    delay(DELAY);
    moveLegWalkingGroup0(FRONT);
    moveLegWalkingGroup1(BACK);
    delay(DELAY);
    moveKneeWalkingGroup1(DOWN);
    delay(DELAY);
    moveLegWalkingGroup1(FRONT);
  }
}



void frowards(uint8_t steps) {
  for (uint8_t i = 0; steps > i; i++) {
    moveKneeWalkingGroup0(UP);
    moveLegWalkingGroup0(FRONT);
    delay(DELAY);
    moveKneeWalkingGroup0(DOWN);
    delay(DELAY);
    moveKneeWalkingGroup1(UP);
    delay(DELAY);
    moveLegWalkingGroup0(BACK);
    moveLegWalkingGroup1(FRONT);
    delay(DELAY);
    moveKneeWalkingGroup1(DOWN);
    delay(DELAY);
    moveLegWalkingGroup1(BACK);
  }
}

void moveLegWalkingGroup0(uint16_t deg) {
  moveLeg(0, deg);
  moveLeg(2, deg);
  moveLeg(4, deg);
}


void moveLegWalkingGroup1(uint16_t deg) {
  moveLeg(1, deg);
  moveLeg(3, deg);
  moveLeg(5, deg);
}


void moveKneeWalkingGroup0(uint16_t deg) {
  moveKnee(0, deg);
  moveKnee(2, deg);
  moveKnee(4, deg);
}


void moveKneeWalkingGroup1(uint16_t deg) {
  moveKnee(1, deg);
  moveKnee(3, deg);
  moveKnee(5, deg);
}


void moveKnee(uint8_t knee, uint16_t deg) {
  moveServo((2 * knee) + 1, map(deg, MIN, MAX, MIN_DUTY, MAX_DUTY));
}

void moveLeg(uint8_t leg, uint16_t deg) {
  if (leg <= 2) {
    moveServo(2 * leg, map(deg, MIN, MAX, MIN_DUTY, MAX_DUTY));
  } else {
    moveServo(2 * leg, map(MAX - deg, MIN, MAX, MIN_DUTY, MAX_DUTY));
  }
}


void moveServo(uint8_t channel, uint16_t pos) {
  uint8_t hi = (uint8_t)((pos & (0xFF << 8)) >> 8);
  uint8_t lo = (uint8_t) (pos & 0xFF);

  Serial.print("!SC");
  Serial.write(channel);
  Serial.write(0x00);
  Serial.write(lo);
  Serial.write(hi);
  Serial.write(0x0d);
}


