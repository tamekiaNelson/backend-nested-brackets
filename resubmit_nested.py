#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Module docstring: checks for proper brackets. """
__author__ = "tamekiaNelson with instructor help"

import sys

# declare two sets of lists with matching opener/closer tokens
# They must be lined up by index, because we will cross-index between them.
open_li = ["[", "(", "{", "(*", "<"]
closed_li = ["]", ")", "}", "*)", ">"]

def valid_parentheses(string):
    stack = []
    c = 0
    while string:
        token = string[0]  # look at first char of string as token
        # handle 'eyebrows'
        if string.startswith('(*'):
            # eyebrow opener
            token = '(*'
        elif string.startswith('*)'):
            # eyebrow closer
            token = '*)'
        c = c+1

        if token in open_li:
            stack.append(token)
        elif token in closed_li:
            # we have a closing token.  Find its opener buddy
            closer_index = closed_li.index(token)
            matching_opener = open_li[closer_index]
            # if things are balanced, the matching opener should be at top of stack.
            # Test if stack is empty, or is not balanced.
            if len(stack) == 0 or matching_opener != stack.pop():
                # early exit from while loop
                return "NO " + str(c)
        string = string[len(token):]

    # Final check after while loop is done.
    # If there is anything left on stack, that is unbalanced.    
    if stack:
        return "NO " + str(c)
    else:
        return "YES"

def main():
    with open("input.txt", "r") as file_open:
        with open("output.txt", "w") as output:
            for row in file_open:
                results = valid_parentheses(row)
                print(results)
                output.write(results + "\n")

if __name__ == '__main__':
    main()
