# Housekeeping

A collection of Python automation scripts to assist with various tasks on your computer such as file organization, tidying, and spicing things up with a wallpaper change. Meant to be used in conjunction with Windows Task Scheduler.

![](https://i.imgur.com/XSEYGzT.png)



## Installation

1. Please note, this guide is for usage on Windows operating systems.

1. To use any of these scripts, ensure you have the latest edition of [Python](https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare) installed on your computer (as of October 2023, this is 3.11).

2. Download this repository as a zip file to your machine.

4. Unzip the files to your desired location.

   

## clean.py

When run, this script will delete cache and temp files from your system. I recommend running this **monthly** to free up space and improve performance. Good news is, no customization is required for this script! It is ready to run as is!

<u>Required packages:</u>  os, shutil *(please install with 'pip install' if not installed already)*



## recycle.py

When run, this script will attempt to permanently delete any files in your recycling bin that were deleted 30 or more days ago. You can run this script as often as you'd like, I personally do it **daily**. Good news is, no customization is required for this script! It is ready to run as is! However, you may have to provide confirmation for certain files while the script is running. Certain types of files, such as shortcuts, will need to be deleted manually. 

<u>Required packages:</u>  os, winshell, datetime, shutil *(please install with 'pip install' if not installed already)*



## wallpaper.py

When run, this script will download and change your desktop background to the current hottest wallpaper on the r/wallpaper subreddit on Reddit. It will also ensure you haven't already downloaded the wallpaper and if so, will use the first unique wallpaper it can find. You will need to change the value of the constant FOLDER to your desired path to store your wallpapers, but PLEASE ensure that this directory will include ONLY wallpapers (no subdirectories, no non-image file types). I personally like to have this run **daily** at midnight.

<u>Required packages:</u>  os, requests, json, ctypes, filetype *(please install with 'pip install' if not installed already)*



## Permission Errors

You might have to grant permissions to access certain directories. If you run into any permission errors, go to File Explorer and navigate to the directory that is causing the issue(s). If you do not currently have permission to access the directory, it should prompt you to grant permission when trying to enter the directory. Once you grant permission, you should no longer have any permission-related errors.



## Windows Task Scheduler

While you can always run any of these scripts manually if you desire, it is much more convenient to use Window's Task Scheduler to have these scripts run automatically at times you specify. To do this, you can follow this [very simple and straightforward guide](https://www.geeksforgeeks.org/schedule-a-python-script-to-run-daily/). Try to choose times when you know your computer will be up and running, as they will not run at all if the time passes and your system was turned off. Another great option would be to have the script(s) run on startup, which is even simpler to do by following [this guide](https://www.geeksforgeeks.org/autorun-a-python-script-on-windows-startup/). I would recommend that more for the wallpaper script, and less for the clean script.
