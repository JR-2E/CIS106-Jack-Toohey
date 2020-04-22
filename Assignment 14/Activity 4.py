# This program reads from a address file,
# and outputs the addresses in a certain format.


def get_file_len(addresses):
    with open(addresses) as f:
        for file_len, l in enumerate(f):
            pass
    file_len = file_len + 1
    return file_len


def output_results(addresses, file_len, lines):
    if file_len % 4:
        with open('~addresses.txt', 'r') as f:
            flat_list = [word for line in f for word in line.split()]
            print(flat_list[1] + ", " + flat_list[0] + ", " +
                  f"{lines[1].strip()}" + ", " + f"{lines[2].strip()}")
            for x in range(4, (file_len), 4):
                line = lines[x].split(" ")
                print(line[1].strip() + ", " + line[0].strip() +
                      ", " + f"{lines[x + 1].strip()}" + ", " +
                      f"{lines[x + 2].strip()}")
    else:
        print("File line count is incorrect for format. " +
              "Make sure there is no more than one" +
              "blank line after the final address.")


def main():
    addresses = "~addresses.txt"
    file_len = get_file_len(addresses)
    output_results(addresses, file_len, lines)

f = open('~addresses.txt')
lines = f.readlines()
main()
