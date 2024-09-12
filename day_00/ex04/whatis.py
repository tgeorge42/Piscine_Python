import sys

try:
    if len(sys.argv) < 2:
        sys.exit(1)
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    else:
        try:
            N = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if N % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")    
except AssertionError as e:
    print(type(e).__name__, ":", e)
    sys.exit(1)