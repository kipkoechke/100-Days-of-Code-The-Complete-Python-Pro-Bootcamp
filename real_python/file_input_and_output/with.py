#!/usr/bin/env python3

with open("hello.txt", "r") as input_file:
    for line in input_file.readlines():
        print(line, end="")
