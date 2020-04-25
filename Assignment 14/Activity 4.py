# This program reads from a address file,
# and outputs the addresses in a certain format.


def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    return lines


def output_results(filename):
    lines = get_lines(filename)
    file_len = len(lines)
    if file_len % 4:
        flat_list = [word for line in lines for word in line.split()]
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
    filename = "addresses.txt"
    output_results(filename)


main()
