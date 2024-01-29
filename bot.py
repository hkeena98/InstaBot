"""
Author: Henry Keena
License: MIT
Date: 
Version: 
Description: File for Bot Class Object
"""

# Imports instagrapi Library
from instagrapi import Client
from pathlib import Path
from openai import OpenAI
import requests
import random
import json

"""
Class: Bot()
Description: Object Class for Instagram Bot
"""
class Bot():
    __slots__ = ["CONFIG_FILE", "BOT_USERNAME", "BOT_PASSWORD", "ENABLE_PERSONA", "PERSONA_TYPE", "PERSONA_FILE", "OPENAI_API_KEY", "GPT_PERSONA", "BOT_CLIENT", "OPENAI_CLIENT"]
    """
    Function: __init__(self)
    Description: Initialization Function for Object Instance of InstBot
    """
    def __init__(self):
        print("\nConstructing InstaBot Instance...\n")
        try:
            self.CONFIG_FILE = 'config.json'
            with open(self.CONFIG_FILE) as config_file:
                config_data = json.load(config_file)
                self.BOT_USERNAME = config_data["BOT_USERNAME"]
                self.BOT_PASSWORD = config_data["BOT_PASSWORD"]
                self.ENABLE_PERSONA = config_data["ENABLE_PERSONA"]
                self.PERSONA_TYPE = config_data["PERSONA_TYPE"]
                self.PERSONA_FILE = config_data["PERSONA_FILE"]
                self.OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
                self.GPT_PERSONA = config_data["GPT_PERSONA"]
            self.BOT_CLIENT = Client()
            if self.OPENAI_API_KEY is None or self.OPENAI_API_KEY == "":
                self.OPENAI_CLIENT = None
            else:
                self.OPENAI_CLIENT = OpenAI(api_key=self.OPENAI_API_KEY)
            self.BOT_CLIENT.login(self.BOT_USERNAME, self.BOT_PASSWORD)
            print("\nBot Instance Created...\n")
        except Exception as error:
            print("\nBOT CONSTRUCTOR INSTANTIATION ERROR:", error)
            
    """
    Function: 
    Description: 
    """
    def message_file_persona(self, recipient):
        try:
            if Path(self.PERSONA_FILE).is_file():
                with open(self.PERSONA_FILE) as persona:
                    message = random.choice(persona.readlines()).strip()
                self.BOT_CLIENT.direct_send(message, user_ids=[self.BOT_CLIENT.user_id_from_username(recipient)])
            else:
                print("\nNO PERSONA FILE SET...\n")
        except Exception as error:
            print("\nBOT PERSONA MESSAGE ERROR:", error)
            
    """
    Function: 
    Description: 
    """
    def message_gpt_persona(self, message):  
        chat_completion = self.OPENAI_CLIENT.chat.completions.create(
            messages=[
                {
                    "role": self.GPT_PERSONA,
                    "content": message
                }
            ],
            model="gpt-3.5-turbo",
        )
        return chat_completion

    """
    Function: 
    Description:
    """
    def message_post(self, recipient, media):
        try:
            self.BOT_CLIENT.direct_media_share(media, user_ids=[self.BOT_CLIENT.user_id_from_username(recipient)])
        except Exception as error:
            print("\nBOT POST SHARE ERROR:", error)
    
    """
    Function: 
    Description:
    """
    def print_bot(self):
        print("\n")
        print("CONFIG_FILE:", self.CONFIG_FILE)
        print("BOT_USERNAME:", self.BOT_USERNAME)
        print("BOT_PASSWORD:", self.BOT_PASSWORD)
        print("ENABLE_PERSONA:", self.ENABLE_PERSONA)
        print("PERSONA_TYPE:", self.PERSONA_TYPE)
        print("PERSONA_FILE:", self.PERSONA_FILE)
        print("OPENAI_API_KEY:", self.OPENAI_API_KEY)
        print("BOT_CLIENT:", self.BOT_CLIENT)
        print("\n")