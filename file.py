#!/usr/bin/python3

######################################################################################
##                                                                                  ##
## Filehandler                                                                      ##
##                                                                                  ##
## Phillip Blunck, 2020-10-06                                                       ##
##                                                                                  ##
######################################################################################

import sys
import json

######################################################################################

DEBUG_FLAG = True
EMPTY = ""

######################################################################################

class FileHandler:

    def __init__(self, file=EMPTY):
        self.filename = file

    def read(self):
        """Opens the json file and returns a list with the settings.
        If no file is found it returns an error message.
        """
        retdata = []
        try:
            with open(self.filename) as json_file:
                data = json.load(json_file)
                retdata.append(data["server1"])
                retdata.append(data["webhook1"])
                retdata.append(data["server2"])
                retdata.append(data["webhook2"])
        except FileNotFoundError:
            retdata.append("No json file found!")
        return retdata

    def write(self):
        pass

######################################################################################

if __name__ == "__main__":
    if DEBUG_FLAG: hdl = FileHandler("settings.json"); test = hdl.read(); print(test)