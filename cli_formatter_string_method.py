def cli_formatter_with_argument(data):
    formatter = "{}"
    print(formatter.format(data))


if __name__ == "__main__":
    import sys
    n(sys.argv[1])
