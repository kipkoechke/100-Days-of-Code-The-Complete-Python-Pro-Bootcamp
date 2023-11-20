#!/usr/bin/env python3
output_file = open("hello.txt", "w")
lines_to_write = [
    "\nThis is my file.",
    "\nThere are many like it,",
    "\nbut this one is mine.",
]
output_file.writelines(lines_to_write)
output_file.close()
