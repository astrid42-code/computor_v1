import sys

def main():
    argv = sys.argv
    argc = len(argv)
    if argc != 2:
        print("Wrong number of argments")
        exit()
    else:
        print("Let's have fun with some polynomial equations!")


if __name__ == "__main__":
    main()
