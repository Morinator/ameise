from control.AntRobot import AntRobot

if __name__ == '__main__':


    a = AntRobot('/dev/serial0', 2400)
    a.open()
    a.reset()

    a.forwards(2)
    a.turn_right(2)
    a.turn_left(4)
    a.turn_right(2)
    a.backwards(2)
