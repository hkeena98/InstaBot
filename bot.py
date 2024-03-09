"""
Author: Henry Keena
License: MIT
Date: 3/9/2024
Version: 1.0
Description: File for Bot Class Object
"""

# Import Declarations
from instagrapi import Client
from pathlib import Path
from openai import OpenAI
import random
import json
import time

"""
Class: Bot()
Description: Main Bot Object Class for InstBot
"""
class Bot():
    __slots__ = ["CONFIG_FILE", "BOT_USERNAME", "BOT_PASSWORD", "ENABLE_PERSONA", "PERSONA_TYPE", "PERSONA_FILE", "OPENAI_API_KEY", "GPT_PERSONA", "BOT_TIMER", "BOT_CLIENT", "OPENAI_CLIENT"]
    """
    Function: __init__(self)
    Description: Initialization/Constructor Function for Bot Object Instance
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
                self.BOT_TIMER = config_data["BOT_TIMER"]
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
    Function: message_file_persona(self, recipient)
    Description: Function for sending persona file messages
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
            print("\nBOT FILE PERSONA MESSAGE ERROR:", error)
            
    """
    Function: message_gpt_persona(self, recipient)
    Description: Function for sending GPT powered persona messages
    """
    def message_gpt_persona(self, recipient):
        try: 
            if self.OPENAI_CLIENT == None:
                return None
            else:
                # Generic placeholder message for future work.
                message = "Message the bot user with a witty statement about themselves."
                chat_completion_message = self.OPENAI_CLIENT.chat.completions.create(
                    messages=[
                        {
                            "role": self.GPT_PERSONA,
                            "content": message
                        }
                    ],
                    model="gpt-3.5-turbo",
                )
                self.BOT_CLIENT.direct_send(chat_completion_message, user_ids=[self.BOT_CLIENT.user_id_from_username(recipient)])
        except Exception as error:
            print("\nBOT GPT PERSONA MESSAGE ERROR:", error)

    """
    Function: message_post(self, recipient, media)
    Description: Function for sending posts from a target account to a recipient account
    """
    def message_post(self, recipient, media):
        try:
            self.BOT_CLIENT.direct_media_share(media, user_ids=[self.BOT_CLIENT.user_id_from_username(recipient)])
        except Exception as error:
            print("\nBOT POST SHARE ERROR:", error)
            
    """
    Function: wait_period(self)
    Description: Function for waiting between Bot operations
    """
    def wait_period(self):
        print("\nBOT WAITING PERIOD:", self.BOT_TIMER, "Minutes...\n")
        wait_time = (self.BOT_TIMER * 60)
        time.sleep(wait_time)
    
    """
    Function: print_bot(self)
    Description: Print function for Bot Instance
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
        print("BOT_TIMER:", self.BOT_TIMER)
        print("BOT_CLIENT:", self.BOT_CLIENT)
        print("\n")
        