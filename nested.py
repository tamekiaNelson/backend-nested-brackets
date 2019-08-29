#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Module docstring: checks for proper brackets. """
__author__ = "tamekiaNelson"

import sys

open_li = ["[","(","{","(*"]
closed_li = ["]",")","}","*)",""]


def valid_parentheses(string):
    stack = []
    for i in string:
        if i in open_li:
            stack.append(i)
        elif i in closed_li:
            x = closed_li.index(i)
            if ((len(stack) > 0) and (open_li[x] == stack[len(stack) -1])):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

def main():
    with open("input.txt", "r") as file_open:
        with open("output.txt", "w") as output:
            for row in file_open:
                results = valid_parentheses(row)
                print(results)
                output.write(results + "\n")

if __name__ == '__main__':
    main()
