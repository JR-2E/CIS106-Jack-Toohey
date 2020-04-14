# This program gets a line of comma-separated-values from the user,
# gets rid of the commas and spaces,
# then outputs the list back out to the user,
# one by one.


def get_string():
    print("Enter a line of comma-separated-values.")
    string = input()
    return string


def format_string(string):
    string_no_spaces = string.replace(" ", "")
    print(string_no_spaces)
    split_string = string_no_spaces.split(",")
    return split_string


def display_results(split_string):
    count = 0
    while count < len(split_string):
        print(split_string[count])
        count = count + 1


def main():
    string = get_string()
    split_string = format_string(string)
    display_results(split_string)

main()