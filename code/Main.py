from control.AsyncAntRobot import AsyncAntRobot
from obstacle_detection.Scanner import Scanner
import pyrealsense2 as rs
import sys

if __name__ == '__main__':

    # init robot
    max_steps = 5

    if len(sys.argv) > 1:
        try:
            max_steps = int(sys.argv[1])
        except:
            pass

    a = AsyncAntRobot('/dev/serial0', 2400)
    a.open()
    a.reset()
    a.join_reset()

    # init camera
    scanner = Scanner(rs.pipeline())

    steps = 0
    method = ""

    while steps < max_steps:
        direction = scanner.scan_output()
        print(direction)
        if direction is Scanner.straight:
            a.forwards(1)
        elif direction is Scanner.right:
            a.turn_right(1)
        elif direction is Scanner.left:
            a.turn_left(1)
        steps += 1
        a.join_action()

    # close all connections
    scanner.close()
