"""
Read Me
This Python script automates the process of organizing image files. It copies only images from a specified source folder to a newly created destination folder, and optionally deletes the original images.
Kavinda Kiridana developed this on October 25, 2024.
"""

import os
import shutil
import random

def get_random_digits():
    return str(random.randint(1000, 9999))

# Get the source folder path from the user
source_folder = input("Enter the path to the source folder: ")

# Create the destination folder name with random digits
destination_folder_name = "imageFilter" + get_random_digits()
destination_folder = os.path.join(os.path.dirname(source_folder), destination_folder_name)

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

#asking the user if they wish to delete the original file. 
answer = input('Press "y" if you want to remove the original files.\nOtherwise, press any other key:').lower()
if answer == 'y':
    is_delete = True
else:
    is_delete = False
if is_delete:
    print("Deleting the original files...")# Code to delete the original file (assuming you have the necessary permissions)
else:
    print("Original files not deleted.")

# Define the list of image extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp','.webp','.heic']

# Check if destination folder exists; if not, create it
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through each file in the source folder
i=0
for file_name in os.listdir(source_folder):
    # Get the file extension
    _, extension = os.path.splitext(file_name)
    
    # Check if the file is an image based on extension
    if extension.lower() in image_extensions:
        # Construct full file path
        source_file_path = os.path.join(source_folder, file_name)
        destination_file_path = os.path.join(destination_folder, file_name)

        file_size = os.path.getsize(source_file_path)#get the size of the image file
        if(file_size>9999):#we don't want very small images, so we just delete small files and get only large image file
            # Copy the file to the destination folder
            shutil.copy(source_file_path, destination_file_path)
            print(f'Copied: {file_name}')
            if is_delete:
                os.remove(source_file_path)
                print(f'Deleted: {file_name}')
            i=i+1 
       
print(f"{i} Number of image files have been successfully copied to the destination folder.")