windows_tmp = "Run this package on windows: \"{}\""


def pprint(val):
    print(windows_tmp.format(val))


def index_print():
    printer(index)


if __name__ == "__main__":
    printer("test")
