#!/usr/bin/env python3
input_file = open("hello.txt", "r")
for line in input_file.readlines():
    print(line, end="")
input_file.close()

print("\n\n********using readline()*********")

input_file = open("hello.txt", "r")

line = input_file.readline()
while line != "":
    print(line, end="")
    line = input_file.readline()
input_file.close()
