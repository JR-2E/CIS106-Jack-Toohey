# This program asks for a first and last name,
# then puts it in the format 'last name, first initial.'


def get_name():
    print("Enter first and last name, with a space between.")
    name = input()
    return name


def get_formatted_name(name):
    name = ' '.join(name.split())
    split_name = name.split(" ")
    if len(split_name) != 2:
        print("Invalid entry.")
        name = get_name()
        formatted_name = get_formatted_name(name)
        return formatted_name
    else:
        formatted_name = str(split_name[1] + ", " + name[:1] + ".")
        return formatted_name


def display_results(formatted_name):
    print(formatted_name)


def main():
    name = get_name()
    formatted_name = get_formatted_name(name)
    display_results(formatted_name)


main()
