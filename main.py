"""
Author: Henry Keena
License: MIT
Date: 3/9/2024
Version: 1.0
Description: Main File for Instagram Bot
"""

# Import Declarations
from bot import *
from recipient import *
from utils import *
import sys

"""
Function: main()
Description: Main Function
"""
def main():
    # Start of operations
    print("INSTAGRAM BOT...\n")
    # Checks if Recipient Bot folders exist
    if not any(fname.endswith('.json') for fname in os.listdir('bots/')):
        print("\nNo Recipient Files Detected...\n")
        sys.exit()
    # Declares & Instantiates Bot Object Instance
    insta_bot = Bot()
    insta_bot.print_bot()
    # Primary infinite loop for InstaBot
    # Operations end when the user manually ends the program
    while True:
        # Enforces Bot waiting period between operations
        insta_bot.wait_period()
        # Fetches Recipient data from JSON files
        recipients = fetch_recipients_json()
        print(recipients)
        # Begins iteration of Recipient setup operations
        for recipient in recipients:
            # Checks if Persona is enabled, if true sends Persona Message
            if recipient.PERSONA_ENABLED == True:
                if insta_bot.PERSONA_TYPE == "FILE":
                    insta_bot.message_file_persona(recipient.RECIPIENT_USERNAME)
                elif insta_bot.PERSONA_TYPE == "GPT":
                    insta_bot.message_gpt_persona(recipient.RECIPIENT_USERNAME)
            # Iterates through recipient Sources
            for key, val in recipient.SOURCES.items():
                print("Account:", key, ", Post ID:", val)
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

# Calls Main
if __name__ == "__main__":
    main()
    