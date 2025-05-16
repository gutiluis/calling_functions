def print_files(data):
    import os
    k = os.listdir()
    print(k)


if __name__ == "__main__":
    import sys
    print_files(sys.argv[1])
