"""
Author: Henry Keena
License: MIT
Date: 11/22/23
Version: 0.1
"""

# Imports Ensta Library
#from ensta import Host

# Imports instagrapi Library
from instagrapi import Client


import json



"""
"""
def test_ensta():
    print("Testing Ensta Library...\n")



"""
"""
def test_instagrapi():
    print("Testing instagrapi Library...\n")
    cl = Client()
    cl.login("", "")
    #print("Account Information:",cl.account_info().dict())
    #print(cl.collections())
    user_id = cl.user_id_from_username("austinnasso")
    medias = cl.user_medias(user_id, 20)
    print(medias)
    print("Saving to JSON")
    json_object = json.dumps(medias, default=set_default, indent=4)
    with open('media_data.json', 'w') as fil:
        fil.write(json_object)
    print("\nData Written to JSON File...\n")
    
    #for media in medias:
    #    print(media)


# Helper
def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


"""
"""
def main():
    print("INSTAGRAM VIDEO BOT")
    print("Calling Main...\n")
    #test_ensta()
    test_instagrapi()
    


# Calls Main
if __name__ == "__main__":
    main()