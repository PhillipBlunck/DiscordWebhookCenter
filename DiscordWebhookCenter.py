#!/usr/bin/python3

######################################################################################
#                                                                                    #
# Discord Webhook Center                                                             #
# Phillip Blunck, 2020-09-27                                                         #
#                                                                                    #
######################################################################################

import sys
import tkinter as tk

######################################################################################

def main():
    """This function starts the Discord Webhook Center application.
    It generates a new window, where the user can send content to a discord server.
    """
    # create window
    window = tk.Tk()
    window.title("Discord Webhook Center")
    window.resizable(width=False, height=False)

    # Create Frame for settings 
    frm_settings = tk.Frame(master=window, width=800)
    # Create and place content of frame
    lbl_select = tk.Label(master=frm_settings, text="Active Webhook:")
    lbl_select.grid(row=0, column=0)
    mb = tk.Menubutton(master=frm_settings, text="Select Webhook", relief=tk.RAISED)
    mb.grid(row=0, column=1)
    mb.menu = tk.Menu(mb, tearoff=0)
    mb["menu"] = mb.menu
    mb.menu.add_checkbutton(label="Webhook 1", variable=0)
    mb.menu.add_checkbutton(label="Webhook 2", variable=1)

    # Create frame for webhook content
    frm_content = tk.LabelFrame(master=window, width=650, height=500, text="Webhook message", relief=tk.SUNKEN)
    frm_content.grid_propagate(0)
    # Create and place content of frame
    lbl_author = tk.Label(master=frm_content, text="Author:")
    lbl_title = tk.Label(master=frm_content, text="Title:")
    lbl_descrpt = tk.Label(master=frm_content, text="Description:")
    lbl_fields = tk.Label(master=frm_content, text="Fields:")
    lbl_picture = tk.Label(master=frm_content, text="Picture:")
    lbl_footer = tk.Label(master=frm_content, text="Footer:")
    lbl_author.grid(row=0,column=0, sticky="w")
    lbl_title.grid(row=1,column=0, sticky="w")
    lbl_descrpt.grid(row=2,column=0, sticky="w")
    lbl_fields.grid(row=3,column=0, sticky="w")
    lbl_picture.grid(row=4,column=0, sticky="w")
    lbl_footer.grid(row=5,column=0, sticky="w")

    # Create frame for result
    frm_result = tk.Frame(master=window, width=150, height=500)
    frm_result.grid_propagate(0)
    # Create and place content of frame
    msg_return = tk.Message(master=frm_result, text="Return status of webhook message.")
    btn_send = tk.Button(master=frm_result, text="Send", bg="lightblue")
    msg_return.grid(row=0, sticky="nesw")
    btn_send.grid(row=1,sticky="nesw")

    # place frames and content in window
    frm_settings.pack(fill=tk.BOTH, side=tk.TOP)
    frm_content.pack(fill=tk.BOTH, side=tk.LEFT)
    frm_result.pack(fill=tk.BOTH, side=tk.LEFT)

    # Run mainloop
    window.mainloop()

######################################################################################

if __name__ == "__main__":
    main() # execute main window

######################################################################################