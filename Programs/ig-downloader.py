# Import modules/ libraries
from instaloader import Instaloader

# getting instagram username whose profile picture will be downloaded
username = input("Enter Instagram username : ")

# downloading actual instagram profile picture of user
Instaloader().download_profile(username, profile_pic_only = True)
