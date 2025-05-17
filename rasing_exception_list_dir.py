def get_ls_with_argument(data):
    if data != "os.listdir()":
        raise Exception("User din't choose list directory content with files and hidden files.")
    else:
        import os
        k = os.listdir()
        print(k)


if __name__ == "__main__":
    import sys
    get_ls_with_argument(sys.argv[1])
