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


"""
Class: Config()
Description: Object Class for Instagram Bot
"""
class Bot():
    __slots__ = ["BOT_USERNAME", "BOT_PASSWORD", "BOT_PERSONA", "BOT_CLIENT"]
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
            self.BOT_PERSONA = "persona.txt"
            self.BOT_CLIENT = Client()
            self.BOT_CLIENT.login(self.BOT_USERNAME, self.BOT_PASSWORD)
            print("\nBot Instance Created...\n")
        except Exception as error:
            print("\nBOT CONSTRUCTOR INSTANTIATION ERROR:", error)
        
    
    """
    sends persona message
    """
    def message_persona(self, recipient):
        try:
            with open(self.BOT_PERSONA) as persona:
                message = random.choice(persona.readlines()).strip()
            self.BOT_CLIENT.direct_send(message, user_ids=[self.BOT_CLIENT.user_id_from_username(recipient)])
        except Exception as error:
            print("\nBOT PERSONA MESSAGE ERROR:", error)
        #self.BOT_CLIENT.direct_send(message, user_ids=[self.BOT_CLIENT.user_id_from_username(recipient.username)])
        
        # cl.direct_send('How are you?', user_ids=[cl.user_id])
        #self.BOT_CLIENT.direct_send()



    """
    sends post
    """
    def message_post(self, recipient, media):
        try:
            self.BOT_CLIENT.direct_media_share(media['pk'], user_ids=[self.BOT_CLIENT.user_id_from_username(recipient)])
        except Exception as error:
            print("\nBOT POST SHARE ERROR:", error)
    




# cl.direct_send('How are you?', user_ids=[cl.user_id]) 
# cl.direct_media_share(media.pk, user_ids=[cl.user_id])



def test_instagrapi():
    print("Testing instagrapi Library...\n")
    cl = Client()
    cl.login("", "")
    #print("Account Information:",cl.account_info().dict())
    #print(cl.collections())
    user_id = cl.user_id_from_username("")
    medias = cl.user_medias(user_id, 10)
    #print(medias)
    #print("Saving to JSON")
    #json_object = json.dumps(medias, default=set_default, indent=4)
    #with open('media_data.json', 'w') as fil:
    #    fil.write(json_object)
    
    
    
    for media in media_list:
        print(media['taken_at'], "\n")
        
    print("Testing Direct Message")
    
    # Direct Message Call
    cl.direct_send("", user_ids=[cl.user_id_from_username("")])
    
    # Direct Video Message
    cl.direct_media_share(media_list[0]['pk'], user_ids=[cl.user_id_from_username("")])

    
    
        #print(media_dict['taken_at'], "\n")
        #fil_name = "video_"+str(i)+".json"
        #with open(fil_name, "w") as outfile: 
        #    json.dump(media_dict, outfile)
        #print("Data Written to JSON File -",fil_name,"\n")

        #print(media.dict())
        #print(media.username)
        #print(media.taken_at)
        #print(media.video_url)
        #print("\n")

