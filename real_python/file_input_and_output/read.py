#!/usr/bin/env python3
input_file = open("hello.txt", "r")
for line in input_file.readlines():
    print(line)
input_file.close()
