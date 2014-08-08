Brainfuck interpreter

This is a simple but fast Brainfuck interpreter written in Python.

A summary of the parameters accepted by the program:

- "-- program '++++++++++.'"

    Used to pass a program to the interpreter from the commandline.

- "--program-file 'myprogram.txt'"

    Used to pass a program contained within a file to the interpreter. The
    program will read in the entire contents of the file before the interpreter
    commences execution.

- "--nested-loops true|false"

    If your program doesn't have any nested loops, you can speed up the
    interpreter by passing '--nested-loops false' to the program.
    This parameter is optional and defaults to true.

- "--debug true|false"

    When debug mode is on, each operation, and the result of each
    operation, will be printed to the terminal. Four columns will be printed;
    two before an instruction is executed and two after execution.

    1. The position of the pointer on the program tape (starting at zero)
    2. The character at the current position of the pointer on the program tape
    3. The current register on the record tape.
    4. The value of the current register on the record tape.

    This parameter is optional and defaults to false.

Some notes:

-   Programs that rely on integer overflow are unlikely to work in this
    interpreter due to the nature of how Python allocates memory for integers.

-   You can pass multiple programs to the program, but only the last one will
    be executed.

This program is released into the public domain without any warranty.

