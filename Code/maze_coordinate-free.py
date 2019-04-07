#coding:utf-8
import sensor as rf


class Robot:
    """
    Robot class
    """
    def __init__(self):
        pass

    def is_not_used(self):
        pass

    def detect_left(self):
        self.is_not_used()
        if rf.detect_left():
            return True
        else:
            return False

    def detect_front(self):
        self.is_not_used()
        if rf.detect_front():
            return True
        else:
            return False

    def detect_right(self):
        self.is_not_used()
        if rf.detect_right():
            return True
        else:
            return False

    def move_forward(self):
        self.is_not_used()
        print("Move forward")
        rf.motor_forward()

    def turn_left(self):
        self.is_not_used()
        print("Turn left")
        rf.motor_turnLeft()

    def turn_right(self):
        self.is_not_used()
        print("Turn Right")
        rf.motor_turnRight()

    def retreat(self):
        self.is_not_used()
        print("Turn around")
        rf.motor_turnRight()
        rf.motor_turnRight()

    def is_not_used(self):
        pass


def cross_check():
    """
    Algorithm function:
    Check if current position is cross.
    """
    global robot
    counter = 0

    if robot.detect_left():
        counter += 1
    if robot.detect_front():
        counter += 1
    if robot.detect_right():
        counter += 1

    if counter > 1:
        return True
    else:
        return False


def move_available_direction():
    """
    Algorithm function:
    Perform the available action
    """
    global robot
    available = False

    if robot.detect_left():
        robot.turn_left()
        robot.move_forward()
        available = True
    elif robot.detect_front():
        robot.move_forward()
        available = True
    elif robot.detect_right():
        robot.turn_right()
        robot.move_forward()
        available = True

    return available


def test_end():
    """
    Algorithm function:
    Detect if the current position is destination
    """
    if rf.detect_end():
        return True
    else:
        return False


def go_maze():
    """
    Maze solving algorithm function
    """
    if test_end():      # 检查当前位置是否为终点
        print("Reach the end")
        return
    else:
        # 检查当前位置是否为路口
        if cross_check():
            move_available_direction()
        else:
            if move_available_direction():
                return
            else:
                # 如果没有可移动的方向，倒头
                robot.turn_right()
                robot.turn_right()
        go_maze()


robot = Robot()
go_maze()




