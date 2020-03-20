# This program makes a multiplication table with a specific range of
# numbers, both _across and _down.


def get_across_min():
    print("Input the starting number for the multiplication table " +
          "going left to right.")
    across_min = int(input())
    return across_min


def get_across_max():
    print("Input the ending number for the multiplication table " +
          "going left to right.")
    across_max = int(input())
    return across_max


def get_down_min():
    print("Input the starting number for the multiplication table " +
          "going top to bottom.")
    down_min = int(input())
    return down_min


def get_down_max():
    print("Input the ending number for the multiplication table " +
          "going top to bottom.")
    down_max = int(input())
    return down_max


def loop():
    for i in range(down_min, down_max + 1, 1):
        for j in range(across_min, across_max + 1, 1):
            print("{:^3}".format(i * j), end=" ")
        print()


# Main
def main():
    across_min = get_across_min()
    across_max = get_across_max()
    down_min = get_down_min()
    down_max = get_down_max()
    loop()


main()
