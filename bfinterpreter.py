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

class Brainfuck:
    def __init__(self, tape, program, allow_nested_loops = True, debug = False):
        self.tape = tape
        self.program = program
        self.pointer = 0
        self.allow_nested_loops = allow_nested_loops
        self.debug = debug
        self.basic_ops = {
            "+" : self.tape.inc_val,
            "-" : self.tape.dec_val,
            ">" : self.tape.move_right,
            "<" : self.tape.move_left,
            "." : self.tape.print_val
        }

    def end_loop(self):
        nested_loop_count = 0
        while True:
            self.pointer += 1
            if self.program[self.pointer] == "]":
                if nested_loop_count == 0:
                    break
                else:
                    nested_loop_count -= 1
            elif self.program[self.pointer] == "[":
                nested_loop_count += 1

    def run_program(self):
        if self.debug == True:
            import time
        loop_pointers = []
        program_length = len(self.program)
        while self.pointer < program_length:
            char = self.program[self.pointer]
            if char in self.basic_ops.keys():
                self.basic_ops[char]()
                self.pointer += 1
            elif char == "[":
                if self.tape.get_val() == 0:
                    if self.allow_nested_loops == True:
                        self.end_loop()
                    else:
                        self.pointer = self.program.index("]", self.pointer)
                else:
                    loop_pointers.append(self.pointer)
                    self.pointer += 1
            elif char == "]":
                loop_start = loop_pointers.pop()
                if self.tape.get_val() == 0:
                    self.pointer += 1
                else:
                    self.pointer = loop_start
            else:
                self.pointer += 1
            if self.debug == True and self.pointer < program_length:
                print(self.pointer, "\t", self.program[self.pointer], "\t", self.tape.pointer, "\t", self.tape.get_val())
                time.sleep(0.1)


if __name__ == "__main__":
    import sys

    def parse_bool(string):
        if string == "true" or string == "y" or string == "yes":
            return True
        elif string == "false" or string == "n" or string == "no":
            return False
        else:
            return None

    program = ""
    allow_nested_loops = True
    debug = False

    args = sys.argv[1:]
    for x, arg in enumerate(args):
        if arg == "--program":
            program = args[x + 1]
        elif arg == "--nested-loops":
            allow_nested_loops = parse_bool(args[x + 1])
        elif arg == "--debug":
            debug = parse_bool(args[x + 1])

    tape = Tape()
    brainfuck = Brainfuck(tape, program, allow_nested_loops, debug)
    brainfuck.run_program()

