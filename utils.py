"""
Author: Henry Keena
License: MIT
Date: 
Version: 
Description: File for Bot Logic and Utility Functions
"""

# Imports Configuration File
from bot import *

# Imports Utility File
from recipient import *

# Imports Ensta Library
#from ensta import Host

# Imports instagrapi Library
from instagrapi import Client

# Other Imports
import json
import datetime
import os
import time

"""
Function: 
Description:
"""
def fetch_recipients_json():
    file_list = []
    bots_path = 'bots/'
    obj = os.scandir(bots_path)
    for entry in obj :
        if entry.is_dir() or entry.is_file():
            file_list.append(entry.name)
    recipient_list = []
    for file in file_list:
        with open(bots_path+file) as json_file:
            data = json.load(json_file)
            new_recipient = Recipient(data['RECIPIENT_USERNAME'], data['PERSONA_ENABLED'], data['SOURCES'])
            recipient_list.append(new_recipient)
    return recipient_list

"""
Function: 
Description:
"""
def get_most_recent_post(bot, account_name):
    user_id = bot.BOT_CLIENT.user_id_from_username(account_name)
    medias = bot.BOT_CLIENT.user_medias(user_id, 10)
    media_list = []
    for media in medias:
        media_dict = media.dict()
        media_list.append(media_dict)
    media_list = sorted(media_list, key=lambda media: media['taken_at'], reverse=True)
    return media_list[0]['pk']

"""
Function: 
Description:
"""
def wait_time(period):
    print("\nBOT WAITING PERIOD:", period, "Minutes...\n")
    time.sleep(period)
