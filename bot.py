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

"""
Class: Config()
Description: Object Class for Instagram Bot
"""
class Bot():
    __slots__ = ["BOT_USERNAME", "BOT_PASSWORD", "PERSONA_FILE", "BOT_CLIENT"]
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
            self.PERSONA_FILE = "persona.txt"
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
    