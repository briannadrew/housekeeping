import os
import os.path
import requests
import json
import ctypes
import filetype

SPI_SETDESKWALLPAPER = 20
FOLDER = "D:/wallpapers/img" # folder path

# function to check if the image has previously been used
def check_unique(fileSearch):
    unique = True
    for root, dir, files in os.walk(FOLDER): # search through existing files in the wallpaper folder
        if(fileSearch in files):
            unique = False # if the file was found in the wallpaper folder already, it is not unique
    return unique

# function to delete all non-image files that were downloaded in the process
def del_files():
    for root, dir, files in os.walk(FOLDER): # search through existing files in the wallpaper folder
        for filename in files:
            curr_path = os.path.join(root, filename) # get full path of current file
            if not filetype.is_image(curr_path):
                os.remove(curr_path) # if the current file is not an image, remove it

# supply user agent in the header so it will be recognized by the server
myHeaders={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

imgData = requests.get("https://www.reddit.com/r/wallpaper/hot.json",headers=myHeaders).content # make request to get posts as JSON
jsonData = json.loads(imgData) # load JSON data as a dictionary
posts = jsonData["data"]["children"] # access children (the reddit posts)

unique = False
for i in range(len(posts)): # search through posts received
    imgurl = posts[i]["data"]["url"] # get the url of the current image
    imgname = os.path.basename(imgurl) # extract the image name from the url
    unique = check_unique(imgname) # check if this image was already used
    if(unique):
        break

# if a new image was found, set it as desktop background. If not, don't change anything (this is not likely to happen)
if(unique):
    imageContents = requests.get(imgurl, headers=myHeaders).content # retrieve the image itself
    completeName = os.path.join(FOLDER, imgname) # path to where the image will be saved
    with open(completeName, "wb") as imageFile:
        imageFile.write(imageContents) # save the image to wallpapers folder
    if filetype.is_image(completeName): # if the file downloaded is a valid image file
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, completeName, 3) # set the image as the desktop background
        del_files() # call function to delete non-image files in the directory
    else:
        os.system('python wallpaper.py') # restart the script
