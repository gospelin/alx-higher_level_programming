#!/usr/bin/python3

def no_c(my_string):
    new_string = list(my_string)

    for i, alpha in enumerate(my_string):
        if alpha == 'c' or alpha == 'C':
            new_string[i] = ""
            my_string = "".join(new_string)

    return (my_string)
