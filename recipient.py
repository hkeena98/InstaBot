"""
Author: Henry Keena
License: MIT
Date: 
Version: 
Description: Class file for Bot Reciepients
"""

"""
"""
class Recipient():
    __slots__ = ["RECIPIENT_USERNAME", "PERSONA_ENABLED", "SOURCES"]
    
    """
    Function: 
    Description:
    """
    def __init__(self, recipient_username, persona_enabled, sources):
        self.RECIPIENT_USERNAME = recipient_username
        self.PERSONA_ENABLED = persona_enabled
        self.SOURCES = sources


    """
    Function: 
    Description:
    """
    def print_recipient(self):
        print("RECIPIENT USERNAME:", self.RECIPIENT_USERNAME)
        print("IS PERSONA ENABLED:", self.PERSONA_ENABLED)
        print("RECIPIENT SOURCES:", self.SOURCES)
    
    """
    Function: 
    Description:
    """
    def create_recipient_json(self):
        pass