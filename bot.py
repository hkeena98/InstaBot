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
from pathlib import Path
import json

"""
Class: Bot()
Description: Object Class for Instagram Bot
"""
class Bot():
    __slots__ = ["CONFIG_FILE", "BOT_USERNAME", "BOT_PASSWORD", "PERSONA_TYPE", "ENABLE_PERSONA", "PERSONA_FILE", "OPENAI_API_KEY", "BOT_CLIENT"]
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
                self.PERSONA_TYPE = config_data["PERSONA_TYPE"]
                self.ENABLE_PERSONA = config_data["ENABLE_PERSONA"]
                self.PERSONA_FILE = config_data["PERSONA_FILE"]
                self.OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
            self.BOT_CLIENT = Client()
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
    def message_gpt_persona(self, recipient):
        pass
        """
        import requests
        import openai

        def get_chatgpt_response(user_message):
            openai.api_key = "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"

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Specify the GPT-3.5 Turbo model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=150,
            )

            return response["choices"][0]["message"]["content"].strip()
        """

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
        print(self.CONFIG_FILE)
        print(self.BOT_USERNAME)
        print(self.BOT_PASSWORD)
        print(self.PERSONA_TYPE)
        print(self.ENABLE_PERSONA)
        print(self.PERSONA_FILE)
        print(self.OPENAI_API_KEY)
        print(self.BOT_CLIENT)
        print("\n")