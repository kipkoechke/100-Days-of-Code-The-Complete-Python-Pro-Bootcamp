#!/usr/bin/env python3
import csv
import os

path = (
    "C:/Real Python/python-basics-exercises"
    "/ch11-file-input-and-output/practice_files"
)

with open(os.path.join(path, "wonka.csv"), "r") as my_file:
    reader = csv.reader(my_file)
    for row in reader:
        print(row)
