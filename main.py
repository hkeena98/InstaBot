"""
Author: Henry Keena
License: MIT
Date: 11/22/23
Version: 0.1
Description: Main File for Instagram Bot
"""

# Imports Bot File
from bot import *

# Imports Utility File
from recipient import *

# Imports Utility Functions
from utils import *

# Imports Sys
import sys

"""
Function: 
Description:
"""
def operations():
    # Checks if Recipient Bot folders exist
    if not any(fname.endswith('.json') for fname in os.listdir('bots/')):
        print("\nNo Recipient Files Detected...\n")
        sys.exit()
    
    # Declares & Instantiates Bot Object Instance
    insta_bot = Bot()
    
    # Fetches Recipient data from JSON files
    recipients = fetch_recipients_json()
    print(recipients)
  
    # Begins iteration of Recipient setup operations
    for recipient in recipients:
        # Checks if Persona is enabled, if true sends Persona Message
        if recipient.PERSONA_ENABLED == True:
            insta_bot.message_file_persona(recipient.RECIPIENT_USERNAME)
            
        # Iterates through recipient Sources
        for key, val in recipient.SOURCES.items():
            # Gets most recent post from a listed source
            most_recent = get_most_recent_post(insta_bot, key)
            # Checks if most recent post is also the most recent tracked by bot
            if val != most_recent:
                # If not most recent, set most recent to recipient
                recipient.SOURCES[key] = most_recent
                # Sends Most recent Post from Source
                insta_bot.message_post(recipient.RECIPIENT_USERNAME, most_recent)
            else:
                # If last sent post is most recent, does not send post
                continue
        # Updates recipient JSON file    
        recipient.write_recipient_json()
        
    # Prints Recipient Data
    for recipient in recipients:
        print("\n")
        recipient.print_recipient()  
            
"""
Function: 
Description:
"""
def main():
    # Start of operations
    print("INSTAGRAM BOT...\n")
    # Input for Main Options
    option = input("Single Use or Timed? (S/T): ")
    # Main Options Divergent Conditional
    if option == 'S' or option == 's':
        operations()
        sys.exit()
    elif option == 'T' or option == 't':
        operation_period = int(input("Enter Bot Operational Run Period(Minutes): "))
        while True:
            if operation_period < 0:
                exit()
            else:
                wait_time(operation_period)
                operations()
    else:
        print("\nINVAID OPTION\n")
        sys.exit()

# Calls Main
if __name__ == "__main__":
    main()