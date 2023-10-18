import os
import shutil

# define directories for cache and temp files
CACHE_DIR = "C:/Windows/Prefetch/"
TEMP_DIR = "C:/Windows/Temp/"
TEMP_DIR_LOC = "C:/Users/brian/AppData/Local/Temp/"

def clear_folder(directoryPath):
    contents = os.listdir(directoryPath) # make a list of items in the current directory
    for items in contents: # iterate through each file and folder in the directory
        itemPath = os.path.join(directoryPath, items)
        try:
            # if the item is a file, permanently delete it
            if os.path.isfile(itemPath):
                os.remove(itemPath)

            # if the item is a folder, permanently delete it and its contents    
            elif os.path.isdir(itemPath):
                shutil.rmtree(itemPath)

            # if the item is neither a file or folder, leave it alone    
            else:
                print(f"Skipped: {itemPath} (Not a file or directory)")
        except Exception as e:
            print(f"Error deleting {itemPath}: {e}") # catch deletion errors

if __name__ == "__main__":
    print("Cleaning Cache...")
    clear_folder(CACHE_DIR)

    print("Cleaning Temp Files...")
    clear_folder(TEMP_DIR)
    clear_folder(TEMP_DIR_LOC)