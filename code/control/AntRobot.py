import serial
import time
from .AntRobotBase import AntRobotBase


class AntRobot(AntRobotBase):

    def __init__(self, port, baud_rate=2400):
        self.baud_rate = baud_rate
        self.port = port
        self.ser = None

    def open(self):
        self.ser = serial.Serial(self.port, self.baud_rate)

    def close(self):
        self.ser.close()
        self.ser = None

    def __del__(self):
        self.close()

    def reset(self):
        self.move_leg_walking_group_0(90)
        self.move_leg_walking_group_1(90)
        self.move_knee_walking_group_0(self.DOWN)
        self.move_leg_walking_group_1(self.DOWN)

    def turn_left(self, steps=1):
        tmp = self.SPEED
        for _ in range(steps):
            self.move_knee(0, self.UP)
            self.move_knee(2, self.UP)
            self.move_knee(4, self.UP)
            time.sleep(self.DELAY)

            self.SPEED = 10

            self.move_leg(1, self.FRONT)
            self.move_leg(3, self.BACK)
            self.move_leg(5, self.BACK)

            self.move_leg(0, self.BACK)
            self.move_leg(2, self.BACK)
            self.move_leg(4, self.FRONT)

            self.SPEED = tmp

            time.sleep(self.DELAY + self.DELAY_OFFSET)
            self.move_knee(0, self.DOWN)
            self.move_knee(2, self.DOWN)
            self.move_knee(4, self.DOWN)
            time.sleep(self.DELAY)
            self.move_knee(1, self.UP)
            self.move_knee(3, self.UP)
            self.move_knee(5, self.UP)
            time.sleep(self.DELAY)

            self.SPEED = 10

            self.move_leg(0, self.FRONT)
            self.move_leg(2, self.FRONT)
            self.move_leg(4, self.BACK)

            self.move_leg(1, self.BACK)
            self.move_leg(3, self.FRONT)
            self.move_leg(5, self.FRONT)

            time.sleep(self.DELAY + self.DELAY_OFFSET)
            self.SPEED = tmp

            self.move_knee(1, self.DOWN)
            self.move_knee(3, self.DOWN)
            self.move_knee(5, self.DOWN)
            time.sleep(self.DELAY)

        AntRobot.reset(self)

    def turn_right(self, steps=1):
        tmp = self.SPEED
        for _ in range(steps):
            self.move_knee(0, self.UP)
            self.move_knee(2, self.UP)
            self.move_knee(4, self.UP)
            time.sleep(self.DELAY)

            self.SPEED = 10

            self.move_leg(1, self.BACK)
            self.move_leg(3, self.FRONT)
            self.move_leg(5, self.FRONT)
            self.move_leg(0, self.FRONT)
            self.move_leg(2, self.FRONT)
            self.move_leg(4, self.BACK)

            self.SPEED = tmp

            time.sleep(self.DELAY + self.DELAY_OFFSET)
            self.move_knee(0, self.DOWN)
            self.move_knee(2, self.DOWN)
            self.move_knee(4, self.DOWN)
            time.sleep(self.DELAY)
            self.move_knee(1, self.UP)
            self.move_knee(3, self.UP)
            self.move_knee(5, self.UP)
            time.sleep(self.DELAY)

            self.SPEED = 10

            self.move_leg(0, self.BACK)
            self.move_leg(2, self.BACK)
            self.move_leg(4, self.FRONT)

            self.move_leg(1, self.FRONT)
            self.move_leg(3, self.BACK)
            self.move_leg(5, self.BACK)

            time.sleep(self.DELAY + self.DELAY_OFFSET)
            self.SPEED = tmp

            self.move_knee(1, self.DOWN)
            self.move_knee(3, self.DOWN)
            self.move_knee(5, self.DOWN)
            time.sleep(self.DELAY)

        AntRobot.reset(self)

    def backwards(self, steps=1):
        tmp = self.SPEED
        for _ in range(steps):
            self.move_knee_walking_group_0(self.UP)
            time.sleep(self.DELAY)
            self.move_leg_walking_group_0(self.BACK)
            time.sleep(self.DELAY)
            self.move_knee_walking_group_0(self.DOWN)
            time.sleep(self.DELAY)
            self.move_knee_walking_group_1(self.UP)
            time.sleep(self.DELAY)

            self.SPEED = 10
            self.move_leg_walking_group_0(self.FRONT)
            self.move_leg_walking_group_1(self.BACK)
            time.sleep(self.DELAY + self.DELAY_OFFSET)
            self.SPEED = tmp

            self.move_knee_walking_group_1(self.DOWN)
            time.sleep(self.DELAY)
            self.move_knee_walking_group_0(self.UP)
            time.sleep(self.DELAY)

            self.SPEED = 10
            self.move_leg_walking_group_0(self.BACK)
            self.move_leg_walking_group_1(self.FRONT)
            time.sleep(self.DELAY)
            self.SPEED = tmp

        AntRobot.reset(self)

    def forwards(self, steps=1):
        tmp = self.SPEED
        for _ in range(steps):
            self.move_knee_walking_group_0(self.UP)
            time.sleep(self.DELAY)
            self.move_leg_walking_group_0(self.FRONT)
            time.sleep(self.DELAY)
            self.move_knee_walking_group_0(self.DOWN)
            time.sleep(self.DELAY)
            self.move_knee_walking_group_1(self.UP)
            time.sleep(self.DELAY)

            self.SPEED = 10
            self.move_leg_walking_group_0(self.BACK)
            self.move_leg_walking_group_1(self.FRONT)
            time.sleep(self.DELAY + self.DELAY_OFFSET)
            self.SPEED = tmp

            self.move_knee_walking_group_1(self.DOWN)
            time.sleep(self.DELAY)
            self.move_knee_walking_group_0(self.UP)
            time.sleep(self.DELAY)

            self.SPEED = 10
            self.move_leg_walking_group_0(self.FRONT)
            self.move_leg_walking_group_1(self.BACK)
            time.sleep(self.DELAY)
            self.SPEED = tmp

        AntRobot.reset(self)

    def move_leg_walking_group_0(self, deg):
        self.move_leg(0, deg)
        self.move_leg(2, deg)
        self.move_leg(4, deg)

    def move_leg_walking_group_1(self, deg):
        self.move_leg(1, deg)
        self.move_leg(3, deg)
        self.move_leg(5, deg)

    def move_knee_walking_group_0(self, deg):
        self.move_knee(0, deg)
        self.move_knee(2, deg)
        self.move_knee(4, deg)

    def move_knee_walking_group_1(self, deg):
        self.move_knee(1, deg)
        self.move_knee(3, deg)
        self.move_knee(5, deg)

    def move_knee(self, knee, deg):
        self.__move_servo((2 * knee) + 1, AntRobot.map(deg, self.IN_MIN, self.IN_MAX,
                                                       self.OUT_MIN, self.OUT_MAX))

    def move_leg(self, leg, deg):
        if leg <= 2:
            self.__move_servo(2 * leg, AntRobot.map(deg, self.IN_MIN, self.IN_MAX,
                                                    self.OUT_MIN, self.OUT_MAX))
        else:
            self.__move_servo(2 * leg, AntRobot.map(self.IN_MAX - deg, self.IN_MIN, self.IN_MAX,
                                                    self.OUT_MIN, self.OUT_MAX))

    def __move_servo(self, channel, pos):
        pos = int(pos)
        hi = ((pos & (0xFF << 8)) >> 8)
        lo = (pos & 0xFF)

        self.ser.write(b'!SC')
        self.ser.write(bytes([channel]))
        self.ser.write(bytes([self.SPEED]))
        self.ser.write(bytes([lo]))
        self.ser.write(bytes([hi]))
        self.ser.write(bytes([0x0d]))
        
        # Could also work:
        # self.ser.write(b'!SC')
        # self.ser.write(bytes([channel, self.SPEED, lo, hi, 0x0d]))

    @staticmethod
    def map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
