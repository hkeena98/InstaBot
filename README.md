# InstaBot

Instagram Bot for automating sending posts and videos to followers and friends.

I made this because I figured it would be a fun little side project to work on.

The bot operates by being fed configuration files that include the usernames of desired recipient accounts, as well as a list of the accounts that recipient is to be sent posts from, as well as a timer for how often they will be sent those posts. The bot has been also designed to account for posts that have already been sent to a recipient. If the timed post share trigger is hit and an account tied to a recipient hasn't made a new post, it will not send them that post. It will only send new posts.

Additionally, individual configurations, or the entire bot itself, can be configured with a fun little persona that it will adopt whenever it sends out a message to users. The bot can have this personality either via integration with OpenAI's GPT-3.5 API, or through a manually created "persona" text file.

**IMPORTANT NOTE:**

InstaBot works by sending messages through an existing Instagram account. You will need to configure the bot to operate through either your own account, or make a new one and operate it through that one.

**DISCLAIMER:**

This project is fully open source, and written under the MIT license. Anyone is free to use and extend it as they see fit. Enjoy.

That being said, the creator of this project does not encourage or endorse its use and abuse for online harrassment or any action that could be construed as such. Just be nice.

## Dependencies/Libraries, Installation, & Operation

Most of the bot is just pure Python 3 code, but there is two notably utilized external dependencies:
- [instagrapi](https://github.com/subzeroid/instagrapi) - This is the Instagram API library that handles most of the actual Instagram interactions.
- [openai](https://github.com/openai/openai-python) - This is OpenAI's official Python library. We are using it for some fun little messaging integrations.

Operating InstaBot is pretty simple:
1. [Create an Instagram account.](https://www.instagram.com/accounts/emailsignup/) 
2. Create a virtual environment: `python3 -m venv .venv`
3. Install necessary dependencies: `pip3 install -r requirements.txt`
4. Create a new subdirectory for the recipient configurations: `mkdir bots`
5. Configure the bot and recipient settings in the necessary configuration files, as explained in the following section of this README.
6. Run the actual bot via the main: `python3 main.py`

## Settings & Configurations

There are three main types of configuration files that InstaBot uses, two use JSON and the other is a text file:
1. The primary bot configuration file named: `config.json`. This is the config file that determines the global settings for the bot itself. This file should be in the base package directory.
2. The recipient configuration files that are to be placed in the newly made `bots/` subdirectory. These can be named whatever you want them to be, but best practice(and easiest way to keep track of them) is to name them after a recipient username, for example a configuration for "user123" would be `user123.json`.
3. The "persona" configuration file. This is an entirely optional file that is meant to be for if you want to give your Bot a charming personality without using GPT. This file can also be named whatever you want, but it must be a text file. For example: `persona.txt`. This file should be in the base package directory.

**The bot and recipient configuration files must be manually created by the user prior to operation.**

### Global Bot Configuration

`config.json` is the main configuration file for IntaBot's global settings. 

- `BOT_USERNAME` - String value of the username of the Instagram account that the Bot will be operating under.
- `BOT_PASSWORD` - String value of the password of the Bot's account.
- `ENABLE_PERSONA` - A boolean value determining whether or not the Bot will have a 'persona' or not. Optional, default is `false`.
- `PERSONA_TYPE` - String value for whether the Bot's persona is being generated from a custom file, or through OpenAI's GPT-3.5 language model. Value should be either: `FILE` or `GPT`.
- `PERSONA_FILE` - String value of text file name for the Bot's persona, assuming you set the persona type to `FILE`. You can also leave this blank if you desire.
- `OPENAI_API_KEY` - String value of your OpenAI API Key. Necessary if you want the Bot's persona to use the GPT language model. **NOTE: This will require OpenAI credits**
- `GPT_PERSONA` - String value of what you want the Bot's persona or personality to be like, assuming you have the persona type set to `GPT`. You can also leave this blank if you desire.

Example `config.json` File structure:
```
{
    "BOT_USERNAME": "instagram_username",
    "BOT_PASSWORD": "instagram_password",
    "ENABLE_PERSONA": true,
    "PERSONA_TYPE": "GPT",
    "PERSONA_FILE": "example_persona.txt",
    "OPENAI_API_KEY": "example_key12345",
    "GPT_PERSONA: "You are a helpful and friendly robot."
}
```

### Recipient Configuration

These configuration files are for applying specific settings to specific intended recipient accounts. You are free to create as many, or as few of these files as you desire, but all must be located in the `bots/` subdirectory.

- `RECIPIENT_USERNAME` - String value of a recipient account. This is the account you want InstaBot to send posts to.
- `PERSONA_ENABLED` - Boolean value that determines whether this specific recipient will have the bot's persona feature enabled. If the persona is not enabled in the bot's global config file, it will not send persona messages regardless of this value.
- `POST_TIMER` - Integer value of how often the Bot will send post's to this account. It operates by hours, so for example if you put `24`, as the value the bot will send new posts every once a day.
- `SOURCES` - Dictionary value for storing what account sources you want the bot to pull new posts from. Each entry in the dictionary should be a simple key value pair of the desired post account, and an empty String value. For example: `"example_recipient1": ""`. You can add as many accounts as you want to the sources dictionary. An important note is when adding a new source account to this file, leave the value of the key empty, the bot will automatically fill the value when it reads the new source for the first time.

Example `bots/example_recipient_instagram_username.json` file structure:
```
{
    "RECIPIENT_USERNAME": "example_recipient_instagram_username",
    "PERSONA_ENABLED": true,
    "POST_TIMER": 24,
    "SOURCES": {
        "example_recipient1": "",
        ... ,
        ... ,
        ...
    }
}
```

### Bot Persona Text File

The final configuration file is the "persona" text file. This is an optional file for if you desire a fun persona for your InstaBot but do not want to use OpenAI/GPT. It is really as simple as just writing a bunch of phrases into a text file and seperating by a new line. You can name the file whatever you want, just make sure you specify its name in the global `config.json` file.

Example `persona.txt` file structure:
```
Example phrase one.
Example phrase two.
Example phrase three.
```

## Future/Eventual Work

There are a number of potential extra features to work on and add in future releases of this project:
- A CLI menu or some form of better user experience.
- Automated process for recipient configuration generation.
- Configuration file integrity checking. Right now, the Bot just assumes you did/wrote everything correctly.
- More GPT and OpenAI functionality integrations.
- Various other functionality additions I haven't thought of yet.

Those interested in furthering the project are encouraged to reach out about it.