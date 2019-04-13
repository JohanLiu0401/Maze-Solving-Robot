#coding:utf-8
import sensor as rf

current_path = 0
cross = 0


class Stack:
    """
    stack
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
    还需要添加机器人移动代码
    """

    def __init__(self, x, y):
        self.position = Position(x, y)

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
        self.calculate_coordinate()
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

    def calculate_coordinate(self):
        # 对当前方向进行检测，计算坐标的改变
        direction = rf.judge_direction()
        if direction == "x_plus":
            self.position.x += 1
        elif direction == "x_minus":
            self.position.x -= 1
        elif direction == "y_plus":
            self.position.y += 1
        elif direction == "y_minus":
            self.position.y -= 1
        else:
            print ("Wrong direction information!")


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


def go_maze(start):
    # 将当前位置入栈
    current_path.push(start)

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


robot = Robot()
current_path = Stack()
cross = Stack()
start = Position(0, 0)
go_maze(start)

# current_path.push(start)
# pop_cross(current_path, start)
# print(current_path.size(), current_path.is_empty())
# print(current_path.peek().print_position())
# print(current_path.pop().print_position())
# print(current_path.peek().print_position())
# print(current_path.pop().print_position())
# print(current_path.size(), current_path.is_empty())





