"""
Author: Henry Keena
License: MIT
Date: 
Version: 
Description: Class file for Bot Reciepients
"""

import json

"""
"""
class Recipient():  
    """
    Function: 
    Description:
    """
    def __init__(self, recipient_username, persona_enabled, post_timer, sources):
        self.RECIPIENT_USERNAME = recipient_username
        self.PERSONA_ENABLED = persona_enabled
        self.POST_TIMER = post_timer
        self.SOURCES = sources

    """
    Function: 
    Description:
    """
    def print_recipient(self):
        print("RECIPIENT USERNAME:", self.RECIPIENT_USERNAME)
        print("IS PERSONA ENABLED:", self.PERSONA_ENABLED)
        print("POST TIMER(IN HOURS):", self.POST_TIMER)
        print("RECIPIENT SOURCES:", self.SOURCES)
    
    """
    Function: 
    Description:
    """
    def write_recipient_json(self):
        file_name = "bots/"+self.RECIPIENT_USERNAME+".json"
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(self.__dict__, file, ensure_ascii=True, indent=4)