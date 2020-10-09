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

DEBUG_FLAG = True
EMPTY = ""
CHAR_LIM = 500
NO_FILE = "No json file found!"

######################################################################################

class Gateway:

    def __init__(self):
        # read settings file and set init gateway settings
        self.filehdl = file.FileHandler("settings.json")
        self.config = self.filehdl.read()
        if NO_FILE in self.config:
            self.config.clear()
            self.webhook = DiscordWebhook(
                url=""
            )
        else:
            if DEBUG_FLAG: print(self.config[1])
            self.webhook = DiscordWebhook(
                url=self.config[1]
            )

    def get_config(self):
        return self.config

    def send(self, data, server):
        """Sends the user defined message to a Discord Server
        and returns the execution response.
        """
        # get selected webhook
        if server in self.config and server is not EMPTY:
            self.webhook.url = self.config[self.config.index(server)+1]
        else:
            self.webhook.url = EMPTY
        # Collect data and assemble
        if self.webhook.url != EMPTY and not self.check_data_limit(data):
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
            ret = response.status_code
        else:
            ret = 1337
        return ret

    def check_data_limit(self, data):
        """Checks if the characters of the data is in set bounds.
        Returns True when one input is out of bounds.
        Returns False when each input is in bounds.
        """
        ret = False
        for dat in data:
            if DEBUG_FLAG: print(f"Len of DATA o: {len(dat)}")
            if len(dat) > CHAR_LIM:
                ret = True
                break
        return ret
        
######################################################################################
