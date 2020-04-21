# This program reads from a address file,
# and outputs the addresses in a certain format.


def get_file_len(addresses):
    with open(addresses) as f:
        for file_len, l in enumerate(f):
            pass
    file_len = file_len + 1
    return file_len


def check_len(addresses, file_len):
    if file_len % 4:
        with open('~addresses.txt', 'r') as f:
            flat_list = [word for line in f for word in line.split()]
            for x in range(0, (file_len), 8):
                print(flat_list[x + 1] + ", " + flat_list[x] + ", " +
                      flat_list[x + 2] + " " + flat_list[x + 3] + " " +
                      flat_list[x + 4] + ", " + flat_list[x + 5] + " " +
                      flat_list[x + 6] + ", " + flat_list[x + 7])
            print(flat_list[file_len * 2 - 5] + ", " +
                  flat_list[file_len * 2 - 6] + ", " +
                  flat_list[file_len * 2 - 4] + " " +
                  flat_list[file_len * 2 - 3] + " " +
                  flat_list[file_len * 2 - 2] + ", " +
                  flat_list[file_len * 2 - 1] + flat_list[file_len * 2 + 1])
    else:
        print("File line count is incorrect for format. " +
              "Make sure there is no more than one" +
              "blank line after the final address.")


def main():
    addresses = "~addresses.txt"
    file_len = get_file_len(addresses)
    check_len(addresses, file_len)

f = open('~addresses.txt')
lines = f.readlines()
main()

