#!/usr/bin/python3

class Tape:
    def __init__(self):
        self.reset()

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

    def set_val(self, val):
        self.cells[self.pointer] = val

    def reset(self):
        self.cells = [0]
        self.pointer = 0

class Brainfuck:
    def __init__(self, tape, program, input_tape = None, allow_nested_loops = True, debug = False, eof_ord = 0):
        self.tape = tape
        self.program = program
        self.input_tape = input_tape
        self.pointer = 0
        self.allow_nested_loops = allow_nested_loops
        self.debug = debug
        self.eof_ord = eof_ord
        self.basic_ops = {
            "+" : self.tape.inc_val,
            "-" : self.tape.dec_val,
            ">" : self.tape.move_right,
            "<" : self.tape.move_left,
        }

    def reset(self):
        self.tape.reset()
        self.pointer = 0
        if self.input_tape is not None:
            self.input_tape.seek(0)

    def read_input(self):
        if self.input_tape is None:
            return 0
        char = self.input_tape.read(1)
        if char == "":
            return self.eof_ord
        else:
            return ord(char)

    def end_loop(self):
        nested_loop_count = 0
        while True:
            self.pointer += 1
            if self.program[self.pointer] == "]":
                if nested_loop_count == 0:
                    self.pointer += 1
                    break
                else:
                    nested_loop_count -= 1
            elif self.program[self.pointer] == "[":
                nested_loop_count += 1

    def print_val(self):
        print(chr(self.tape.get_val()), end="")

    def run_program(self):
        if self.debug == True:
            import time
        loop_pointers = []
        program_length = len(self.program)
        while self.pointer < program_length:
            char = self.program[self.pointer]

            if self.debug == True:
                debug_string = str(self.pointer) + "\t" + char + "\t"

            if char in self.basic_ops.keys():
                self.basic_ops[char]()
                self.pointer += 1
            elif char == ".":
                self.print_val()
                self.pointer += 1
            elif char == "[":
                if self.tape.get_val() == 0:
                    if self.allow_nested_loops == True:
                        self.end_loop()
                    else:
                        self.pointer = self.program.index("]", self.pointer) + 1
                else:
                    loop_pointers.append(self.pointer)
                    self.pointer += 1
            elif char == "]":
                loop_start = loop_pointers.pop()
                if self.tape.get_val() == 0:
                    self.pointer += 1
                else:
                    self.pointer = loop_start
            elif char == ",":
                charval = self.read_input()
                self.tape.set_val(charval)
                self.pointer += 1
            else:
                self.pointer += 1

            if self.debug == True:
                debug_string += str(self.tape.pointer) + "\t" + str(self.tape.get_val())
                if self.input_tape is not None:
                    debug_string += "\t" + str(self.input_tape.tell())
                print("\n" + debug_string)
                time.sleep(0.01)


if __name__ == "__main__":
    import sys

    def read_program_file(filename):
        with open(filename, encoding="utf-8") as program_file:
            return program_file.read()

    def parse_bool(string):
        if string == "true" or string == "y" or string == "yes" or string == "1":
            return True
        elif string == "false" or string == "n" or string == "no" or string == "0":
            return False
        else:
            return None

    program = ""
    input_tape = None
    allow_nested_loops = True
    debug = False
    eof_ord = 0
    dump_tape = False

    args = sys.argv[1:]
    for x, arg in enumerate(args):
        if arg == "--program":
            program = args[x + 1]
        elif arg == "--program-file":
            program = read_program_file(args[x + 1])
        elif arg == "--input":
            from io import StringIO
            input_tape = StringIO(args[x + 1])
        elif arg == "--input-file":
            input_tape = open(args[x + 1], encoding="utf-8")
        elif arg == "--nested-loops":
            allow_nested_loops = parse_bool(args[x + 1])
        elif arg == "--debug":
            debug = parse_bool(args[x + 1])
        elif arg == "--eof":
            eof_ord = int(args[x + 1])
        elif arg == "--dump-tape":
            dump_tape = True

    tape = Tape()
    brainfuck = Brainfuck(tape, program, input_tape, allow_nested_loops, debug, eof_ord)
    brainfuck.run_program()

    if dump_tape == True:
        print("\n", tape.cells)

    # Cleanup
    if input_tape is not None:
        input_tape.close()

