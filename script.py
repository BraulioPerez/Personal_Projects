import os
import shutil

location = os.getcwd()

for file in os.listdir(location):
    file_location = os.path.join(location, file)

    if os.path.isfile(file_location):
        name = os.path.basename(file_location)
        extension = file.split(".")[-1]
        extension_folder = os.path.join(location, extension)
        if not os.path.exists(extension_folder):
            os.mkdir(extension_folder)
        if extension != "py":
            shutil.move(file_location, os.path.join(extension_folder, name))