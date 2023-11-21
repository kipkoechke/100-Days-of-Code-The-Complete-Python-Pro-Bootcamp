import os

path = (
    "C:/Real Python/python-basics-exercises"
    "/ch11-file-input-and-output/practice_files/images"
)
for current_folder, subfolders, file_names in os.walk(path):
    for file_name in file_names:
        print(os.path.join(current_folder, file_name))
