# 🚀 Image Filtering Application

## 📂 ***About this program***

A Python script that automates the process of organizing and filtering image files from your computer.

## 📂 Features

### Image Organization

- Automatically collects and organizes image files (jpg, jpeg, png, gif, bmp, webp, heic) from a source folder
- Creates a new folder with a random number (e.g., "imageFilter1234") to avoid overwriting existing folders
- Filters out small images by only copying files larger than 9,999 bytes (removes thumbnails/icons)

### File Cleanup

You can choose to either keep or delete the original files after copying. This is useful when you want to:

- Clean up a messy folder while preserving important images
- Extract images from a folder containing mixed file types
- Create a backup of just your images

## 📂 Common Use Cases

### Photo Management

- Extracting photos from a downloads folder
- Organizing images scattered across different folders
- Creating an image-only backup

### Data Organization

- Separating images from documents and other files
- Creating a clean collection of images for a project
- Filtering out small/unwanted images while keeping full-size photos

### Storage Cleanup

- Moving images to a different drive
- Creating organized archives of images
- Removing duplicate images from the source location if desired

## 📂 ***Instructions to run this program***

## 📂 Requirements

- Python installed on your computer
- The ImageFilter application files

## 📂 Installation Steps

1. Install Python

   - Download Python from the official website (https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"

2. Get the Application
   - Download the ZIP file from GitHub
   - Extract the ZIP file to your preferred location

## 📂 Running the Application

### Step 1: Open Command Prompt (Terminal)

- Press `Windows + R`
- Type `cmd` and press Enter

### Step 2: Navigate to Application Folder

- Use the `cd` command to navigate to where you extracted the files
- Example: If your file is in Downloads folder:
  ```
  C:\Users\YourName>cd Downloads\ImageFilter
  ```

### Step 3: Run the Program

- Type: `python imageFilter.py`
- Press Enter

### Step 4: Follow the Prompts

1. When asked for source folder path:

   - Enter the full path of the folder containing your images
   - Example: `C:\Users\YourName\Pictures`

2. Choose whether to delete original files:
   - Press `y` to delete original files after copying
   - Press any other key to keep original files

## 📂 What Happens Next

- The program will create a new folder named "imageFilter" followed by random numbers
- It will copy all image files (jpg, jpeg, png, gif, bmp, webp, heic) to this new folder
- Only images larger than 9,999 bytes will be copied
- You'll see messages showing which files are being copied/deleted
- At the end, it will show how many images were processed

## 📂 Example Output

```
Enter the path to the source folder: C:\Users\YourName\Pictures
Press "y" if you want to remove the original files.
Otherwise, press any other key: y
Deleting the original files...
Copied: vacation.jpg
Deleted: vacation.jpg
...
15 Number of image files have been successfully copied to the destination folder.
```
