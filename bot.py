"""
Author: Henry Keena
License: MIT
Date: 
Version: 
Description: File for Bot Class & Configuration
"""

# Imports instagrapi Library
from instagrapi import Client

import random


"""
Class: Config()
Description: Object Class for Instagram Bot
"""
class Bot():
    __slots__ = ["BOT_USERNAME", "BOT_PASSWORD", "BOT_PERSONA", "BOT_CLIENT"]
    """
    Function: __init__(self)
    Description: Initialization Function for Object Instance of InstBot
    """
    def __init__(self):
        print("\nConstructing InstaBot Instance...\n")
        try:
            # Set this value to Bot Username
            self.BOT_USERNAME = ""
            # Set this value to Bot Password
            self.BOT_PASSWORD = ""
            # Set this value to Bot Persona File
            self.BOT_PERSONA = "persona.txt"
            self.BOT_CLIENT = Client()
            self.BOT_CLIENT.login(self.BOT_USERNAME, self.BOT_PASSWORD)
            print("\nBot Instance Created...\n")
        except Exception as error:
            print("\nBOT CONSTRUCTOR INSTANTIATION ERROR:", error)
        
    """
    Function: 
    Description: 
    """
    def message_persona(self, recipient):
        try:
            with open(self.BOT_PERSONA) as persona:
                message = random.choice(persona.readlines()).strip()
            self.BOT_CLIENT.direct_send(message, user_ids=[self.BOT_CLIENT.user_id_from_username(recipient)])
        except Exception as error:
            print("\nBOT PERSONA MESSAGE ERROR:", error)

    """
    Function: 
    Description:
    """
    def message_post(self, recipient, media):
        try:
            self.BOT_CLIENT.direct_media_share(media['pk'], user_ids=[self.BOT_CLIENT.user_id_from_username(recipient)])
        except Exception as error:
            print("\nBOT POST SHARE ERROR:", error)
    