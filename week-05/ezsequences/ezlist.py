#################################
# ezsequences/ezlist.py
#
# This skeleton script contains a series of functions that
#  return

ez_list = [0, 1, 2, 3, 4, ['a', 'b', 'c'], 5, ['apples', 'oranges'], 42]



def foo_hello():
    """
    This function should simply return the `type`
     of the `ez_list` object.

    This guarantees that you'll past at least one of
      the tests/assertions in test_ezlist.py
    """
    return type(ez_list)



##################
# Exercises foo_a through foo_e cover basic list access
##################

def foo_a():
    """
    Return the very first member of `ez_list`
    """
    return ez_list [0]

def foo_b():
    """
    Return the sum of the 2nd and 4th members of
      `ezlist`
    """
    sum_second_and_forth = ez_list [1] + ez_list [3]
    return sum_second_and_forth



def foo_c():
    """
    Return the very last member of `ez_list`.

    Use a negative index to specify this member
    """
    return ez_list [-1]


def foo_cx():
    """
    Return the type of the object that is the
        second-to-last member of `ez_list`
    """
    return type(ez_list [-2])


def foo_d():
    """
    Return the very last member of the sequence that itself
        is the second-to-last member of `ez_list`
    """
    second_to_last_member_of_ez_list = ez_list [-2]
    last_member_of_sequence = second_to_last_member_of_ez_list [-1]
    return last_member_of_sequence


def foo_e():
    """
    Calculate and return the length of `ez_list`,  i.e., the
      number of members it contains.
    """
    return len(ez_list)


def foo_f():
    """
    Return the 6th member of `ez_list` as a single,
      semi-colon delimited string

      i.e. the separate values are joined with the
        semi-colon character
    """
    whole_string = ""
    sixth_member = ez_list [5]
    for i in sixth_member:
        single_string = str(i)
        if i == sixth_member [0]:
            whole_string = single_string
        else:
            whole_string = whole_string + ";" + single_string
    return whole_string
    """
    Alternatively, I could have used the join function:
    return ';'.join(ez_list[5])
        """


def foo_g():
    """
    Return a list that contains the 2nd through 5th
      elements of `ez_list`

      (it should have 4 members total)
    """
    new_list = ez_list [1:5]
    return new_list


def foo_h():
    """
    Return a list that consists of the last
      3 members of `ez_list` in *reverse* order
    """
    new_list = ez_list [-3::]
    reverse_list = list(reversed(new_list))
    return reverse_list