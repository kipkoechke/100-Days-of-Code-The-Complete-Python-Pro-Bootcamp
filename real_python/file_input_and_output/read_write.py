output_file = open("hello.txt", "w")
lines_to_write = [
    "This is my file.",
    "There are many like it,",
    "but this one is mine.",
]
output_file.writelines(lines_to_write)
output_file.close()
