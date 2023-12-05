"""
Author: Henry Keena
License: MIT
Date: 
Version: 
Description: File for Bot Logic and Utility Functions
"""

# Imports Ensta Library
#from ensta import Host

# Imports instagrapi Library
from instagrapi import Client

# Other Imports
import json
import datetime




"""
sends persona message
"""
def message_persona():
    pass


"""
sends po
"""
def message_post():
    pass


"""
reads recipient json file to make class object
"""
def read_recipient():
    pass



"""
creates new recipient
"""
def create_recipient():
    pass


"""
gets most recent post from account
"""
def get_most_recent_post():
    pass




# cl.direct_send('How are you?', user_ids=[cl.user_id]) 
# cl.direct_media_share(media.pk, user_ids=[cl.user_id])

"""
"""
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
    
    i = 0
    media_list = []
    for media in medias:
        #i = i+1
        media_dict = media.dict()
        media_list.append(media_dict)
    
    media_list = sorted(media_list, key=lambda media: media['taken_at'], reverse=True)
    
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


















# Helper Function
def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError