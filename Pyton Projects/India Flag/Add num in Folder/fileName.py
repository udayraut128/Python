import os

def add_numbers_to_folders(n):
    # Get the current working directory
    current_directory = os.getcwd()

    # Get a list of all folders in the current directory
    folders = [folder for folder in os.listdir(current_directory) if os.path.isdir(folder)]

    # Iterate over each folder and add numbers to their names
    for i, folder in enumerate(folders[:n], start=1):
        new_folder_name = f"{i}_{folder}"
        os.rename(os.path.join(current_directory, folder), os.path.join(current_directory, new_folder_name))
        print(f"Renamed {folder} to {new_folder_name}")

# Specify the number (n) of folders you want to rename
n = int(input("Enter the number of folders you want to rename: "))
add_numbers_to_folders(n)
