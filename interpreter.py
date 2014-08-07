#!/usr/bin/python3

class Tape:
    def __init__(self):
        self.cells = [0]
        self.pointer = 0

    def inc_val(self):
        self.cells[self.pointer] += 1

    def dec_val(self):
        self.cells[self.pointer] -= 1

    def move_right(self):
        self.pointer += 1
        if self.pointer == len(self.cells):
            self.cells.append(0)

    def move_left(self):
        if self.pointer == 0:
            raise Error("Cannot move past the start of the tape")
        self.pointer -= 1

    def get_val(self):
        return self.cells[self.pointer]

    def print_val(self):
        print(chr(self.cells[self.pointer]), end="")

brainfuck = Tape()
oper = {
    "+" : brainfuck.inc_val,
    "-" : brainfuck.dec_val,
    ">" : brainfuck.move_right,
    "<" : brainfuck.move_left,
    "." : brainfuck.print_val
}

program = "++++++++[>++++++++++<-]>++.>++++++++[>++++++++++<-]>-.>++++++[>++++++++++<-]>++++++.>++++++[>++++++++++<-]>++++++.[>+<-]>+++++++.[>+<-]>----."

x = 0
loop_pointers = []
while x < len(program):
    char = program[x]
    if char in oper.keys():
        oper[char]()
        x += 1
    elif char == "[":
        if brainfuck.get_val() == 0:
            nested_loop_count = 0
            while True:
                x += 1
                if program[x] == "]":
                    if nested_loop_count == 0:
                        break
                    nested_loop_count -= 1
                elif program[x] == "[":
                    nested_loop_count += 1
        else:
            loop_pointers.append(x)
            x += 1
    elif char == "]":
        pointer = loop_pointers.pop()
        if brainfuck.get_val() == 0:
            x += 1
        else:
            x = pointer

