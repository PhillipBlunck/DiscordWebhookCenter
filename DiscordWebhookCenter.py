#!/usr/bin/python3

######################################################################################
##                                                                                  ##
## Discord Webhook Center                                                           ##
##                                                                                  ##
## Phillip Blunck, 2020-09-27                                                       ##
##                                                                                  ##
######################################################################################

import sys
import tkinter as tk
import gateway as gate

######################################################################################

DEBUG_FLAG = True
REQUEST_SUCCESS = 204

######################################################################################

class MainApp:

    def __init__(self, master, gateway):

        # Create main frame for the application
        frame = tk.Frame(master, bg="lightblue")
        frame.pack(fill=tk.BOTH, expand=1)

        # Create frame for settings
        self.frm_settings = tk.Frame(master=frame)
        # Create and place content of frame
        self.lbl_select = tk.Label(master=self.frm_settings, text="Active Webhook:")
        self.lbl_select.pack(side=tk.LEFT)

        # Create frame for webhook content
        self.frm_content = tk.LabelFrame(master=frame,
            text="Webhook message", relief=tk.SUNKEN, width=600
        )
        self.frm_content.grid_propagate(0)
        # Create and place content of frame
        self.lbl_author = tk.Label(master=self.frm_content, text="Author:", padx=20)
        self.entr_author = tk.Entry(master=self.frm_content, width=80)
        self.lbl_title = tk.Label(master=self.frm_content, text="Title:", padx=20)
        self.entr_title = tk.Entry(master=self.frm_content, width=80)
        self.lbl_descrpt = tk.Label(master=self.frm_content,
            text="Description:", padx=20
        )
        self.txt_descrpt = tk.Text(master=self.frm_content, width=60, height=28)
        self.lbl_fields = tk.Label(master=self.frm_content, text="Fields:", padx=20)
        self.entr_fields = tk.Entry(master=self.frm_content, width=80)
        self.lbl_picture = tk.Label(master=self.frm_content, text="Picture:", padx=20)
        self.entr_picture = tk.Entry(master=self.frm_content, width=80)
        self.lbl_footer = tk.Label(master=self.frm_content, text="Footer:", padx=20)
        self.entr_footer = tk.Entry(master=self.frm_content, width=80)

        self.lbl_author.grid(row=0, column=0, sticky="w")
        self.entr_author.grid(row=0, column=1, sticky="w")
        self.lbl_title.grid(row=1, column=0, sticky="w")
        self.entr_title.grid(row=1, column=1, sticky="w")
        self.lbl_descrpt.grid(row=2, column=0, sticky="nw")
        self.txt_descrpt.grid(row=2, column=1, sticky="w")
        self.lbl_fields.grid(row=3, column=0, sticky="w")
        self.entr_fields.grid(row=3, column=1, sticky="w")
        self.lbl_picture.grid(row=4, column=0, sticky="w")
        self.entr_picture.grid(row=4, column=1, sticky="w")
        self.lbl_footer.grid(row=5, column=0, sticky="w")
        self.entr_footer.grid(row=5, column=1, sticky="w")

        # Create frame for result
        self.frm_result = tk.Frame(master=frame, width=200)
        # Create and place content of frame
        self.lbl_result = tk.Label(master=self.frm_result,
            text="Webhook status history:", pady=5
        )
        self.txt_return = tk.Text(master=self.frm_result)
        self.txt_return.config(state=tk.NORMAL)
        self.txt_return.insert(tk.INSERT, "Return status of webhook message.\n")
        self.txt_return.config(state=tk.DISABLED)

        self.btn_settings = tk.Button(master=self.frm_result,
            text="Settings", bg="lightyellow", pady=10,
            command=self.settings_btn_exec
        )
        self.btn_send = tk.Button(master=self.frm_result,
            text="Send", bg="lightblue", pady=10,
            command=self.send_btn_exec
        )
        self.lbl_result.pack(side=tk.TOP)
        self.txt_return.pack(fill=tk.BOTH, side=tk.TOP, expand=1)
        self.btn_settings.pack(fill=tk.X, side=tk.BOTTOM)
        self.btn_send.pack(fill=tk.X, side=tk.BOTTOM)

        # place frames and content in window
        self.frm_settings.pack(fill=tk.X, side=tk.TOP)
        self.frm_content.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)
        self.frm_result.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)

        # gateway for client server handling
        self.gateway = gateway

        # generate and update option menu
        self.mboptions = self.gateway.get_config()
        self.mbvar = tk.StringVar(self.frm_settings)
        self.mbvar.set(self.mboptions[0])
        self.mb = tk.OptionMenu(self.frm_settings, self.mbvar,
            self.mboptions[0], self.mboptions[2]
        )
        self.mb.config(height=1)
        self.mb.pack(side=tk.LEFT)

    def send_btn_exec(self):
        """When a user pressed the send button, the data of all input fields
        is send to a discord server by the gateway.
        """
        data = []
        data.append(self.entr_title.get())
        data.append(self.txt_descrpt.get(0.0, tk.END))
        data.append(self.entr_author.get())
        data.append(self.entr_picture.get())
        data.append(self.entr_footer.get())
        # TODO: Extend and add field
        
        # send data
        msg = self.gateway.send(data, self.mbvar.get())
        # See https://discord.com/developers/docs/topics/opcodes-and-status-codes
        # for status codes
        if msg <= REQUEST_SUCCESS: # TODO: Maybe exception handling better
            msg = "Message successfully\nsend.\n"
        else:
            msg = f"Failed to send message.\nError code: {msg}\n"
        # show response in history
        self.txt_return.config(state=tk.NORMAL)
        self.txt_return.insert(tk.INSERT, msg)
        self.txt_return.config(state=tk.DISABLED)
        # clear all inputs
        self.clearInputs()

    def settings_btn_exec(self):
        if DEBUG_FLAG: print("Open settings!")
        # TODO: Add methods for edit the settings

    def clearInputs(self):
        self.entr_author.delete(0, 'end')
        self.entr_title.delete(0, 'end')
        self.txt_descrpt.delete(0.0, 'end')
        self.entr_fields.delete(0, 'end')
        self.entr_picture.delete(0, 'end')
        self.entr_footer.delete(0, 'end')

######################################################################################

def main():
    """This function starts the Discord Webhook Center application.
    It generates a new window, where the user can send content to a discord server.
    """
    # create window
    root = tk.Tk()
    root.title("Discord Webhook Center")
    root.resizable(width=False, height=False)
    root.geometry("800x610")
    # set gateway instance
    gateway = gate.Gateway()
    # load gui
    app = MainApp(root, gateway)
    app.clearInputs()
    # Run mainloop
    root.mainloop()
    # destroy explicit (used for other development environments)
    # root.destroy()

######################################################################################

if __name__ == "__main__":
    main()

######################################################################################
