"""
Author: Henry Keena
License: MIT
Date: 3/9/2024
Version: 1.0
Description: Class file for Bot Reciepients
"""

# Import Declarations
import json

"""
"""
class Recipient():  
    """
    Function: __init__(self, recipient_username, persona_enabled, sources)
    Description: Initialization/Constructor Function for Recipient Object Instance
    """
    def __init__(self, recipient_username, persona_enabled, sources):
        self.RECIPIENT_USERNAME = recipient_username
        self.PERSONA_ENABLED = persona_enabled
        self.SOURCES = sources

    """
    Function: print_recipient(self)
    Description: Print function for Recipient Object Instance
    """
    def print_recipient(self):
        print("RECIPIENT USERNAME:", self.RECIPIENT_USERNAME)
        print("IS PERSONA ENABLED:", self.PERSONA_ENABLED)
        print("RECIPIENT SOURCES:", self.SOURCES)
    
    """
    Function: write_recipient_json(self)
    Description: Function for writing account data to recipient JSON file
    """
    def write_recipient_json(self):
        file_name = "bots/"+self.RECIPIENT_USERNAME+".json"
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(self.__dict__, file, ensure_ascii=True, indent=4)
