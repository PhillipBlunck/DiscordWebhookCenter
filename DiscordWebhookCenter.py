#!/usr/bin/python3

######################################################################################
##                                                                                  ##
## Discord Webhook Center                                                           ##
## Phillip Blunck, 2020-09-27                                                       ##
##                                                                                  ##
######################################################################################

import sys
import tkinter as tk

######################################################################################

class MainApp:

    def __init__(self, master):

        # Create main frame for the application
        frame = tk.Frame(master, bg="lightblue")
        frame.pack(fill=tk.BOTH, expand=1)

        # Create frame for settings
        self.frm_settings = tk.Frame(master=frame)
        # Create and place content of frame
        self.lbl_select = tk.Label(master=self.frm_settings, text="Active Webhook:")
        self.lbl_select.pack(side=tk.LEFT)
        
        self.mb = tk.Menubutton(master=self.frm_settings, text="Select Webhook",
            relief=tk.RAISED
        )
        self.mb.pack(side=tk.LEFT)
        self.mb.menu = tk.Menu(self.mb, tearoff=0)
        self.mb["menu"] = self.mb.menu
        self.mb.menu.add_checkbutton(label="Webhook 1", variable=0)
        self.mb.menu.add_checkbutton(label="Webhook 2", variable=1)

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
        self.entr_descrpt = tk.Entry(master=self.frm_content, width=80)
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
        self.lbl_descrpt.grid(row=2, column=0, sticky="w")
        self.entr_descrpt.grid(row=2, column=1, sticky="w")
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
        self.txt_return.insert(tk.INSERT,"Return status of webhook message.")
        self.txt_return.config(state=tk.DISABLED)

        self.btn_settings = tk.Button(master=self.frm_result,
            text="Settings", bg="lightyellow", pady=10, command=self.settings_btn_exec
        )
        self.btn_send = tk.Button(master=self.frm_result,
            text="Send", bg="lightblue", pady=10, command=self.send_btn_exec
        )
        self.lbl_result.pack(side=tk.TOP)
        self.txt_return.pack(fill=tk.BOTH, side=tk.TOP, expand=1)
        self.btn_settings.pack(fill=tk.X, side=tk.BOTTOM)
        self.btn_send.pack(fill=tk.X, side=tk.BOTTOM)

        # place frames and content in window
        self.frm_settings.pack(fill=tk.X, side=tk.TOP)
        self.frm_content.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)
        self.frm_result.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)

    def send_btn_exec(self):
        print("Sending data!")

    def settings_btn_exec(self):
        print("Open settings!")

######################################################################################

def main():
    """This function starts the Discord Webhook Center application.
    It generates a new window, where the user can send content to a discord server.
    """

    # create window
    root = tk.Tk()
    root.title("Discord Webhook Center")
    root.resizable(width=False, height=False)
    root.geometry("800x600")

    app = MainApp(root)
    # Run mainloop
    root.mainloop()
    # destroy explicit (used for other development environments)
    root.destroy()

######################################################################################

if __name__ == "__main__":
    main()

######################################################################################
