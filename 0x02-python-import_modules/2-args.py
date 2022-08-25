#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argc))
    for arg_no in range(argc):
        print("{:d}: {}".format(arg_no + 1, argv[arg_no +1]))
