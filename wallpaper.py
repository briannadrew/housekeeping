import os
import os.path
import requests
import json
import ctypes

SPI_SETDESKWALLPAPER = 20
FOLDER = "D:/wallpapers/" # folder path

# function to check if the image has previously been used
def check_unique(fileSearch):
    print(fileSearch)
    unique = True
    for root, dir, files in os.walk(FOLDER): # search through existing files in the wallpaper folder
        print(files)
        if(fileSearch in files):
            print("hello")
            unique = False # if the file was found in the wallpaper folder already, it is not unique
    return unique

# supply user agent in the header so it will be recognized by the server
myHeaders={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

imgData = requests.get("https://www.reddit.com/r/wallpaper/hot.json",headers=myHeaders).content # make request to get posts as JSON
jsonData = json.loads(imgData) # load JSON data as a dictionary
posts = jsonData["data"]["children"] # access children (the reddit posts)

unique = False
for i in range(len(posts)): # search through posts received
    print("hey")
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
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, completeName, 3) # set the image as the desktop background