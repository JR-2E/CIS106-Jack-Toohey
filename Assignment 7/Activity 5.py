# This program asks for shoe size, and gives sock size.


def get_shoe_size():
    print("Enter your shoe size.")
    shoe_size = int(input())
    return shoe_size


def sock_size_extra_small():
    print("Your sock size is extra small.")


def sock_size_small():
    print("Your sock size is small.")


def sock_size_medium():
    print("Your sock size is medium.")


def sock_size_large():
    print("Your sock size is large.")


def sock_size_extra_large():
    print("Your sock size is extra large.")


def main():
    shoe_size = get_shoe_size()
    if shoe_size < 4:
        sock_size_extra_small()
    elif shoe_size >= 4 and shoe_size <= 6:
        sock_size_small()
    elif shoe_size >= 7 and shoe_size <= 9:
        sock_size_medium()
    elif shoe_size >= 10 and shoe_size <= 12:
        sock_size_large()
    elif shoe_size >= 13:
        sock_size_extra_large()
    else:
        print("You must only enter either circle or rectangle.")


main()
