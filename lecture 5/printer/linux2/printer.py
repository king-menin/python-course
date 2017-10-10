linux_tmp = "Run this package on linux: \"{}\""


def pprint(val):
    print(linux_tmp.format(val))


if __name__ == "__main__":
    printer("test")
