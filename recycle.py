import os
import winshell
import datetime
import shutil

DAYS = 30

def empty_bin():
    midnight = datetime.datetime.now(datetime.timezone.utc).replace(hour=0, minute=0, second=0) # get midnight of current day
    cutoffDate = midnight - datetime.timedelta(days=DAYS) # calculate cutoff date

    for item in winshell.recycle_bin():
        if item.recycle_date() <= cutoffDate: # if item was deleted 30 or more days ago...
            try:
                winshell.undelete(item.original_filename()) # restore the file to its original location
            except Exception as e:
                print(f"Error restoring {item.original_filename()}: {e}") # unable to restore file
            try:
                # if item is a folder, permanently delete it
                if os.path.isdir(item.original_filename()):
                    shutil.rmtree(item.original_filename())
                # if item is a file, permanently delete it
                else:
                    os.remove(item.original_filename())
            except Exception as err:
                print(f"Error deleting {item.original_filename()}: {err}") # unable to remove folder/file

if __name__ == "__main__":
    print("Cleaning Recycling Bin...")
    empty_bin()
