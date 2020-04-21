import os


def get_info():
    print("Enter your first name, last name, street address, city," +
          "state/province/region, and postal code, separated by commas.")
    info = input()
    return info


def get_split_info(info):
    info = info.replace(" ", "")
    info = ' '.join(info.split())
    split_info = info.split(",")
    return split_info


def create_file(split_info, address):
    file = open(address, "w")
    file.write(split_info[0] + " " + split_info[1] + "\n")
    file.write(split_info[2] + "\n")
    file.write(split_info[3] + ", " + split_info[4] + " " + split_info[5])
    file.write("\n" + "\n")
    file.close()


def append_file(address):
    info = get_info()
    split_info = get_split_info(info)
    file = open(address, "a")
    file.write(split_info[0] + " " + split_info[1] + "\n")
    file.write(split_info[2] + "\n")
    file.write(split_info[3] + ", " + split_info[4] + " " + split_info[5])
    file.write("\n" + "\n")
    file.close()


def read_file(address):
    file = open(address, "r")
    for line in file:
        line = line.strip()
        print(line)
    file.close()
    print("")


def main():
    address = "~addresses.txt"
    if os.path.isfile(address):
        print("File already exists.")
        info = get_info()
        split_info = get_split_info(info)
        create_file(split_info, address)
        append_file(address)
        append_file(address)
        read_file(address)


main()
