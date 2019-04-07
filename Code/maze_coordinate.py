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
    #
    # def go_straight(self):
    #     print("坐标上移")
    #     self.position.y+1
    #
    # def move_down(self):
    #     print("坐标下移")
    #     self.position.y-1
    #
    # def move_right(self):
    #     print("坐标右移")
    #     self.position.x+1
    #
    # def move_left(self):
    #     print("坐标左移")
    #     self.position.x-1


    def move_forward(self):
        print("前进")
        rf.motor_forward()
        calculate_coordinate()

    def turn_left(self):
        print("左转")
        rf.motor_turnLeft()

    def turn_right(self):
        print("右转")
        rf.motor_turnRight()

    def retreat(self):
        print("向后转")
        rf.motor_turnRight()
        rf.motor_turnRight()

    def detect(self):
        print("探测是否有障碍")


def calculate_coordinate():
    # 对当前方向进行检测，计算坐标的改变
    return


def cross_check(position):
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


def move_available_direction():
    global robot
    available = False

    if rf.detect_left():
        robot.turn_left()
        robot.move_forward()
        available = True
    elif rf.detect_front():
        robot.move_forward()
        available = True
    elif rf.detect_right():
        robot.turn_right()
        robot.move_forward()
        available = True

    return available


def perform_action(position):
    global robot

    # 如果为路口，执行对应动作
    if position in cross:
        move_available_direction()
    else:      # 如果不为路口，寻找可行的地方
        if move_available_direction():
            return
        else:
            # 如果没有可移动的方向，倒头
            robot.turn_right()
            robot.turn_right()


def go_maze(start, end):
    # 将当前位置入栈
    current_path.push(start)

    # 从已记录路径返回当前位置
    current_position = current_path.peek()

    if current_position.is_equal(end):      # 检查当前位置是否为终点
        print("Reach the end")
        return
    else:
        # 检查当前位置是否为路口
        if cross_check(current_position):

            # 检查是否曾经到达过该路口
            if repeat_check(current_position):

                # 出栈到上一次该路口出现的地方
                pop_cross(current_path, current_position)
            else:
                # 将该路口记录
                cross.push(current_position)

        next_position = perform_action(current_position)
        go_maze(next_position, end)


robot = Robot()
current_path = Stack()
cross = Stack()
start = Position(0, 0)
end = Position(5, 5)
# go_maze(start, end)

current_path.push(start)
current_path.push(end)
pop_cross(current_path, start)
# print(current_path.size(), current_path.is_empty())
print(current_path.peek().print_position())
# print(current_path.pop().print_position())
# print(current_path.peek().print_position())
# print(current_path.pop().print_position())
print(current_path.size(), current_path.is_empty())





