from datastubs import STRING_LIST


def reverse_alpha():
    """
    return the list of strings sorted in
    reverse alphabetical order.
    """

    return sorted(STRING_LIST, reverse=True)


def alpha_case_insensitive():
    """
    return the list of strings sorted in
    alphabetical order, but without regard to
    capitalization
    """
    # fill it out
    def no_regard_to_caps(x):
        return x.lower()
    return sorted(STRING_LIST, key=no_regard_to_caps)



def by_longest_length():
    """
    Sort in descending order of length of strings
    """
    # fill it out
    def sorted_by_len(x):
        return len(x)
    return sorted(STRING_LIST, key=sorted_by_len, reverse=True)


def filter_and_sort_number_strings():
    """
    Filter the original list for strings that
    contain numbers. Then sort that list of number
    strings but as strings (i.e. alphaebtical order)

    Hint: string objects have a method named .isnumeric()
    https://www.geeksforgeeks.org/python-string-isnumeric-application/

    """
    # fill it out
    number_strings = []
    for i in STRING_LIST:
        if i.isnumeric():
            number_strings.append(i)
    def sort_as_strings(x):
        return str(x)
    return sorted(number_strings, key=sort_as_strings)


def filter_and_sort_number_strings_as_numbers():
    """
    Filter the list for strings that contain numbers
    and then sort that list of strings in *numerical* order

    Hint: string objects have a method named .isnumeric()
    https://www.geeksforgeeks.org/python-string-isnumeric-application/

    Hint: Use the int() or float() method to convert a numeric string
       into an actual number
    """
    # fill it out
    number_strings = []
    for i in STRING_LIST:
        if i.isnumeric():
            number_strings.append(i)
    def sort_as_numbers(x):
        return int(x)
    return sorted(number_strings, key=sort_as_numbers)