#coding:utf-8
import sensor as rf

current_path = None
cross = None
start = None
robot = None


class Stack:
    """
    The Stack Class
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Position:
    """
    coordinate
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_equal(self, position):
        return self.x == position.x and self.y == position.y

    def print_position(self):
        print("x:", self.x, "y:", self.y)


class Robot:
    """
    The Robot Class
    """

    def __init__(self, position):
        self.position = position
        self.direction_name = self.set_direction_name()
        self.direction = self.set_direction()

    def is_not_used(self):
        pass

    def set_direction_name(self):
        self.is_not_used()

        while True:
            direction_name = input("set the initial direction:\n1. X+\n2. X-\n3. Y+\n4. Y-")
            if direction_name == "X+" or direction_name == "X-" or direction_name == "Y+" or direction_name == "Y-":
                break
            else:
                print "Invalid direction, enter again!"

        return direction_name

    def set_direction(self):
        if self.direction_name == "X+":
            return 0
        elif self.direction_name == "X-":
            return 2
        elif self.direction_name == "Y+":
            return 1
        elif self.direction_name == "Y-":
            return -1
        else:
            print "Invalid direction!"

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
        self.calculate_coordinate()    # Robot move and calculate coordinate

    def turn_left(self):
        self.is_not_used()
        print("Turn left")
        rf.motor_turnLeft()
        self.direction = self.direction + 1
        self.calculate_direction_name()

    def turn_right(self):
        self.is_not_used()
        print("Turn Right")
        rf.motor_turnRight()
        self.direction = self.direction + 1
        self.calculate_direction_name()

    def calculate_coordinate(self):
        # 对当前方向进行检测，计算坐标的改变
        if self.direction_name == "X+":
            self.position.x += 1
        elif self.direction_name == "X-":
            self.position.x -= 1
        elif self.direction_name == "Y+":
            self.position.y += 1
        elif self.direction_name == "Y-":
            self.position.y -= 1
        else:
            print ("Wrong direction information!")

    def calculate_direction_name(self):
        self.test_direction_reset()

        if self.direction == 0:
            self.direction_name = "X+"
        elif self.direction == -2 or 2:
            self.direction_name = "X-"
        elif self.direction == 1 or -3:
            self.direction_name = "Y+"
        elif self.direction == -1 or 3:
            self.direction_name = "Y-"
        else:
            print "invalid direction"

    def test_direction_reset(self):
        if self.direction == 4:
            self.direction = 0  # 旋转一圈重置
        elif self.direction == -4:
            self.direction = 0  # 旋转一圈重置


def init():
    global current_path, cross, start, robot
    current_path = Stack()
    cross = Stack()
    start = Position(0, 0)
    robot = Robot(Position(0, 0))


def check_cross():
    """检查当前位置是否为路口"""
    counter = 0

    if rf.detect_left():
        counter += 1
    if rf.detect_front():
        counter += 1
    if rf.detect_right():
        counter += 1

    if counter > 1:
        return True
    else:
        return False


def pop_cross(stack, position):
    """出栈到上一次该路口出现的地方"""
    while True:
        last_cross = stack.peek()
        if last_cross.is_equal(position):
            break
        stack.pop()


def repeat_check(position):
    """检查是否曾经到达过该路口"""
    arrived = False
    if position in cross:
        arrived = True
    return arrived


def perform_cross_action():
    global robot

    if rf.detect_left():
        robot.turn_left()
        robot.move_forward()
    elif rf.detect_front():
        robot.move_forward()
    elif rf.detect_right():
        robot.turn_right()
        robot.move_forward()


def perform_not_cross_action():
    global robot

    if rf.detect_left():
        robot.turn_left()
        robot.move_forward()
    elif rf.detect_front():
        robot.move_forward()
    elif rf.detect_right():
        robot.turn_right()
        robot.move_forward()
    else:
        # 如果没有可移动的方向，倒头前进
        robot.turn_right()
        robot.turn_right()
        robot.move_forward()


def perform_action(position):
    global robot

    # 如果为路口，执行对应动作
    if position in cross:
        perform_cross_action()
    else:      # 如果不为路口，寻找可行的地方
        perform_not_cross_action()


def test_end():
    """
    Algorithm function:
    Detect if the current position is destination
    """
    if rf.detect_end():
        return True
    else:
        return False


def go_maze(position):
    # 将当前位置入栈
    current_path.push(position)

    # 从已记录路径返回当前位置
    current_position = current_path.peek()

    if test_end():      # 检查当前位置是否为终点
        print("Reach the end")
        return
    else:
        # 检查当前位置是否为路口(这里通过传感器检测)
        if check_cross():
            # 如果是路口，检查是否曾经到达过该路口
            if repeat_check(current_position):
                # 如果到达过该路口，出栈到上一次该路口出现的地方
                pop_cross(current_path, current_position)
            else:
                # 如果没有到达过该路口，将该路口记录进cross栈
                cross.push(current_position)

        perform_action(current_position)
        next_position = Position(robot.position.x, robot.position.y)
        go_maze(next_position)


init()
go_maze(start)






