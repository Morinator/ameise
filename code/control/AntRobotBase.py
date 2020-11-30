
class AntRobotBase:
    IN_MAX = 180
    IN_MIN = 0
    OUT_MAX = 1194  # 1194
    OUT_MIN = 306   # 306

    OFFSET = 55
    UP = 0
    DOWN = 90
    FRONT = IN_MIN + OFFSET
    BACK = IN_MAX - OFFSET

    DELAY = 0.5
    DELAY_OFFSET = 0.8

    SPEED = 7

    def recalculate(self):
        self.FRONT = self.IN_MIN + self.OFFSET
        self.BACK = self.IN_MAX - self.OFFSET
