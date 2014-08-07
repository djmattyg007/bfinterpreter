Brainfuck interpreter

This is a simple but fast Brainfuck interpreter written in Python. It accepts
two arguments.

- "-- program '++++++++++.'"

    This is how you pass a program to the interpreter.
    This argument is compulsory.

- "--nested-loops true|false"

    If your program doesn't have any nested loops, you can speed up the
    interpreter by passing '--nested-loops false' to the program.
    This parameter is optional and defaults to true.

This Brainfuck interpreter does not currently support the "," operator.

This program is released into the public domain without any warranty.

