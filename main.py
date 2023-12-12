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


"""
Function: 
Description:
"""
def main():
    print("INSTAGRAM BOT")
    #insta_bot = Bot()
    recipients = fetch_recipients_json()
    print(recipients)
    for recipient in recipients:
        print("\n")
        recipient.print_recipient()
    #recent1 = get_most_recent_post(insta_bot, "")
    #insta_bot.message_persona("")
    #insta_bot.message_post("", recent1)

    




# Calls Main
if __name__ == "__main__":
    main()