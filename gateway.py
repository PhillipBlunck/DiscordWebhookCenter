#!/usr/bin/python3

######################################################################################
##                                                                                  ##
## Gateway                                                                          ##
##                                                                                  ##
## Phillip Blunck, 2020-10-06                                                       ##
##                                                                                  ##
######################################################################################

from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import file

######################################################################################

class Gateway:

    def __init__(self):
        # TODO: Set Gateway settings
        self.filehdl = file.FileHandler()
        self.set_config()
        self.webhook = DiscordWebhook(
            url=""
        )

    def get_config(self):
        # TODO: returns the parameter
        pass

    def set_config(self):
        """Reads textfile and sets the settings of an Gateway instance.
        """
        # TODO: open file and save configs
        pass

    def send(self, data):
        """Sends the user defined message to a Discord Server
        and returns the execution response.
        """
        # Collect data
        # TODO: Check for character limitation !
        embed = DiscordEmbed(
            title=data[0],
            description=data[1],
            color=242424
        )
        embed.set_author = data[2]
        embed.set_image(url=data[3])
        embed.set_footer(text=data[4])
        embed.set_timestamp()
        self.webhook.add_embed(embed)
        # send data and get response
        response = self.webhook.execute()
        return response.status_code

######################################################################################
