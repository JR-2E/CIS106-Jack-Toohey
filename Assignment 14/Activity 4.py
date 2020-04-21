import os


def read_file(address):
    file = open(address, "r")
    for line in file:
        line = line.strip()
        print(line)
    file.close()
    print("")


def main():
    address = "address.txt"
    if os.path.isfile(address):
        print("File already exists.")
        read_file(address)


main()
