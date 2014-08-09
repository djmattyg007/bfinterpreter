Brainfuck interpreter

This is a simple but fast Brainfuck interpreter written in Python.

A summary of the parameters accepted by the program:

- "-- program '++++++++++.'"

    Used to pass a program to the interpreter from the command line.

- "--program-file 'myprogram.txt'"

    Used to pass a program contained within a file to the interpreter. The
    program will read in the entire contents of the file before the interpreter
    commences execution. This is more efficient when there are lots of loops,
    which is the case for pretty much all Brainfuck programs.

- "--input 'my input string'"

    Used to provide input to the program (to be read by the "," operator) from
    the command line.

- "--input-file 'myinput.txt'"

    Used to provide input contained within a file to the program (to be read by
    the "," operator).

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
    5. If an input tape was supplied, this will count how many characters have
       been read from the input tape so far.

    This parameter is optional and defaults to false.

- "--eof int"

    Used to change the value used as the EOF byte value by the interpreter when
    dealing with input.
    This parameter is optional and defaults to 0.

- "--dump-tape"

    Specifying this will print the contents of the tape to the terminal once
    the program has finished executing.

Some notes:

-   The recording tape used by the interpreter is boundless on the right side
    only. All integers are regular signed Python integers.

-   Programs that rely on integer overflow are unlikely to work in this
    interpreter due to the nature of how Python allocates memory for integers.

-   The interpreter doesn't know whether an input tape was passed in as a string
    from the command line, or as a file, and it doesn't care.

-   You can pass multiple Brainfuck programs to the Python program, but only the
    last one will be executed.

This program is released into the public domain without any warranty.

